#!/usr/bin/env python3
"""Independent finite checks for open-neighborhood complexes of K_m Cartesian C_n.
Public scientific/reproducibility artifact. Standard library only.
"""
from itertools import combinations
from collections import deque

def idx(a,i,m,n): return (i%n)*m+a

def faces_and_facets(m,n):
    # Build graph adjacency FIRST, then derive facets from it (not from the proof).
    V=m*n
    adj=[set() for _ in range(V)]
    for i in range(n):
        for a in range(m):
            v=idx(a,i,m,n)
            for b in range(m):
                if b!=a: adj[v].add(idx(b,i,m,n))
            adj[v].add(idx(a,i-1,m,n)); adj[v].add(idx(a,i+1,m,n))
    facets=[]
    for A in adj:
        facets.append(sum(1<<v for v in A))
    S={0}
    for f in facets:
        bits=[v for v in range(V) if f&(1<<v)]
        for k in range(1,len(bits)+1):
            for cmb in combinations(bits,k):
                S.add(sum(1<<v for v in cmb))
    return S,facets

def subsets(A):
    out=[0]
    for v in A:out += [t|(1<<v) for t in out]
    return out

def collapse(S,lower,upper,V):
    assert lower in S and upper in S and upper.bit_count()==lower.bit_count()+1
    count=0
    for v in range(V):
        if not (lower>>v)&1 and lower|(1<<v) in S:
            count+=1
    assert count==1, ('non-free',lower,upper,count)
    S.remove(lower);S.remove(upper)

def collapse_to_core(m,n,S):
    S=set(S);V=m*n; steps=0
    # Unique common-neighbor opposite-level pairs: eliminate all cofaces.
    for i in range(n):
        for a in range(m):
            u=idx(a,i-1,m,n);v=idx(a,i+1,m,n)
            pivot=idx((a+1)%m,i,m,n)
            others=[idx(b,i,m,n) for b in range(m) if b!=a and b!=(a+1)%m]
            for subset in sorted(subsets(others),key=int.bit_count,reverse=True):
                lo=(1<<u)|(1<<v)|subset
                collapse(S,lo,lo|(1<<pivot),V);steps+=1
    # Each one-wing simplex reduces to m-2 fan triangles.
    for i in range(n):
        for a in range(m):
            pivot=idx((a+1)%m,i,m,n)
            others=[idx(b,i,m,n) for b in range(m) if b!=a and b!=(a+1)%m]
            for j in (i-1,i+1):
                u=idx(a,j,m,n)
                for subset in sorted((x for x in subsets(others) if x.bit_count()>=2),key=int.bit_count,reverse=True):
                    lo=(1<<u)|subset
                    collapse(S,lo,lo|(1<<pivot),V);steps+=1
    return S,steps

def expected_core(m,n):
    S={0}
    # Full boundary of a (m-1)-simplex in each row.
    for i in range(n):
        row=[idx(a,i,m,n) for a in range(m)]
        for s in subsets(row):
            if s.bit_count()<m:S.add(s)
    # Edges across each consecutive pair and surviving fan triangles.
    for i in range(n):
        for a in range(m):
            pivot=idx((a+1)%m,i,m,n)
            others=[idx(b,i,m,n) for b in range(m) if b!=a and b!=(a+1)%m]
            for j in (i-1,i+1):
                u=idx(a,j,m,n)
                for b in range(m):
                    if b!=a:S.add((1<<u)|(1<<idx(b,i,m,n)))
                for w in others:S.add((1<<u)|(1<<pivot)|(1<<w))
    return S

def rank_gf2(vectors):
    piv={}
    for x in vectors:
        while x:
            k=x.bit_length()-1
            if k not in piv:
                piv[k]=x;break
            x^=piv[k]
    return len(piv)

def betti_mod2(S,m,n):
    by={}
    for s in S:
        if s:by.setdefault(s.bit_count()-1,[]).append(s)
    ranks={0:0};count={k:len(v) for k,v in by.items()}
    for k in sorted(by):
        if k==0:continue
        lower={s:j for j,s in enumerate(by[k-1])}
        vec=[]
        for s in by[k]:
            bd=0
            for v in range(m*n):
                if s&(1<<v):bd^=1<<lower[s^(1<<v)]
            vec.append(bd)
        ranks[k]=rank_gf2(vec)
    out={k:count[k]-ranks.get(k,0)-ranks.get(k+1,0) for k in by}
    out[0]-=1
    return {k:v for k,v in out.items() if v}

def check_line_graph(m):
    E={(a,b) for a in range(m) for b in range(m) if a!=b}
    q=deque([min(E)]);seen={q[0]}
    while q:
        a,b=q.popleft()
        for c,d in E:
            if (c==a or d==b) and (c,d) not in seen:
                seen.add((c,d));q.append((c,d))
    assert seen==E
    return len(E)

def main():
    checked=0;total_steps=0;face_counts=[]
    for m in range(4,8):
        for n in range(5,9):
            original,facets=faces_and_facets(m,n)
            assert len(facets)==m*n
            core,steps=collapse_to_core(m,n,original)
            assert core==expected_core(m,n)
            E=check_line_graph(m); lam=m*m-3*m+1
            assert 2*m*(m-2)-(E-1)==lam
            prediction={1:1,2:n*lam};prediction[m-2]=prediction.get(m-2,0)+n
            observed=betti_mod2(original,m,n)
            assert observed==prediction, (m,n,observed,prediction)
            checked+=1;total_steps+=steps;face_counts.append(len(original)-1)
    print('VERIFY_OK', 'complexes='+str(checked), 'elementary_collapses='+str(total_steps),
          'total_original_nonempty_faces='+str(sum(face_counts)),
          'range=m4..7,n5..8', 'predictions=integral_homotopy_reduced_mod2')

if __name__=='__main__':main()
