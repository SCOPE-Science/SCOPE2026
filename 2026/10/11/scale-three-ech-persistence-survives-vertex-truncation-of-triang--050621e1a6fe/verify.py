#!/usr/bin/env python3
"""Reproducible finite checks for a graph Čech collapse theorem.
Uses only the Python standard library. The general theorem is proved separately.
"""
from itertools import combinations
from collections import Counter
import random


def normalize(n, edges):
    ee = {tuple(sorted((int(u), int(v)))) for u,v in edges}
    assert all(0 <= u < v < n for u,v in ee)
    adj = [set() for _ in range(n)]
    for u,v in ee: adj[u].add(v); adj[v].add(u)
    assert all(adj)
    seen = {0}; pending = [0]
    for v in pending:
        for u in adj[v]:
            if u not in seen: seen.add(u); pending.append(u)
    assert len(seen) == n
    return adj, sorted(ee)


def data(n, edges):
    adj, ee = normalize(n,edges)
    half = [(v,w) for v in range(n) for w in sorted(adj[v])]
    index = {h:i for i,h in enumerate(half)}
    C = [sum(1<<index[v,w] for w in adj[v]) for v in range(n)]
    bit=lambda v,w: 1<<index[v,w]
    F2 = [C[v] | bit(w,v) for v,w in half]
    Fcross = [C[v]|C[w] for v,w in ee]
    Fstar = [C[v]|bit(w,v)|bit(z,v) for v in range(n) for w,z in combinations(sorted(adj[v]),2)]
    F3=Fcross+Fstar
    return adj,ee,half,C,bit,F2,Fcross,Fstar,F3


def faces(facets):
    acc={0}
    for f in facets:
        sub=f
        while sub: acc.add(sub);sub=(sub-1)&f
    return acc


def subs(mask):
    xs=[]; p=mask
    while p: xs.append(p & -p); p &=p-1
    for count in range(len(xs)+1):
        for cc in combinations(xs,count): yield sum(cc)


def remove_pair(K, lo, hi):
    assert lo in K and hi in K and hi.bit_count()==lo.bit_count()+1 and lo&hi==lo, (lo,hi)
    m=max(hi.bit_length(),max(K).bit_length())
    supers_lo=[lo|(1<<i) for i in range(m) if not (lo>>i)&1 and (lo|(1<<i)) in K]
    supers_hi=[hi|(1<<i) for i in range(m) if not (hi>>i)&1 and (hi|(1<<i)) in K]
    assert supers_lo==[hi] and not supers_hi, (lo,hi,supers_lo,supers_hi)
    K.remove(lo); K.remove(hi)


def collapse_checks(n,edges):
    adj,ee,half,C,bit,F2,Fcross,Fstar,F3=data(n,edges)
    assert all(not (adj[u] & adj[v]) for u,v in ee), 'triangle in input'
    K2=faces(F2);K0=faces(Fcross);K3=faces(F3)
    assert K2<=K0<=K3
    K=set(K3); counts=[]
    # First stage: remove the simplices containing a pair of opposite
    # halfedges reached from two distinct neighbors of one vertex.
    p=0
    for v in range(n):
        for w,z in combinations(sorted(adj[v]),2):
            x=bit(v,w); rest=C[v]^x; e=bit(w,v)|bit(z,v)
            for s in sorted(subs(rest),key=lambda t:(-t.bit_count(),-t)):
                remove_pair(K,e|s,e|s|x);p+=1
    assert K==K0, ('stage1',len(K^K0))
    counts.append(p)
    # Second stage: remove every cross-star face having non-distinguished
    # halfedges on both sides of the same original edge.
    p=0
    for v,w in ee:
        x=bit(v,w); y=bit(w,v);P=C[v]^x; Q=C[w]^y
        raw=[s|t|r for s in subs(P) if s for t in subs(Q) if t for r in (0,y)]
        for lo in sorted(raw,key=lambda a:(-a.bit_count(),-a)):
            remove_pair(K,lo,lo|x);p+=1
    assert K==K2, ('stage2',len(K^K2)); counts.append(p)
    # Third stage: remove the extra facets in the radius-one Čech complex.
    p=0
    R=faces(C+[bit(v,w)|bit(w,v) for v,w in ee])
    for v,w in half:
        x=bit(v,w); y=bit(w,v);P=C[v]^x
        for s in sorted((s for s in subs(P) if s),key=lambda a:(-a.bit_count(),-a)):
            remove_pair(K,y|s,y|s|x);p+=1
    assert K==R, ('stage3',len(K^R));counts.append(p)
    # Fourth stage: star-triangulation collapse to graph thickening of H.
    p=0
    for v in range(n):
        x=bit(v,min(adj[v]));P=C[v]^x
        for s in sorted((s for s in subs(P) if s.bit_count()>=2),key=lambda a:(-a.bit_count(),-a)):
            remove_pair(K,s,s|x);p+=1
    final={0}
    for v in range(n):
        a=bit(v,min(adj[v]))
        for w in adj[v]:
            y=bit(v,w); final.add(y);final.add(a|y)
    for v,w in ee: final.add(bit(v,w)|bit(w,v))
    assert K==final,('stage4',len(K^final))
    counts.append(p)
    f=Counter(s.bit_count()-1 for s in K if s)
    assert not any(d>1 for d in f)
    assert f[1]-f[0]+1 == len(ee)-n+1
    return len(K3)-1,len(K2)-1,counts,dict(f),len(ee)-n+1


def homology2_mod2(facets):
    F=faces(facets); layers={k:sorted([f for f in F if f.bit_count()==k+1]) for k in range(4)}
    def rank(d):
        rows={f:i for i,f in enumerate(layers[d-1])}; piv={}
        for f in layers[d]:
            b=f; vec=0
            while b:
                one=b & -b; vec ^= 1<<rows[f^one];b-=one
            while vec:
                k=vec.bit_length()-1
                if k in piv:vec^=piv[k]
                else:piv[k]=vec;break
        return len(piv)
    r2=rank(2);r3=rank(3)
    return len(layers[2])-r2-r3


def main():
    examples=[
        ('single edge',2,[(0,1)]),
        ('path P4',4,[(i,i+1) for i in range(3)]),
        ('star K1,4',5,[(0,i) for i in range(1,5)]),
        ('cycle C4',4,[(i,(i+1)%4) for i in range(4)]),
        ('cycle C5',5,[(i,(i+1)%5) for i in range(5)]),
        ('K2,3',5,[(i,j) for i in range(2) for j in range(2,5)]),
        ('cube Q3',8,[(i,i^(1<<b)) for i in range(8) for b in range(3) if i<(i^(1<<b))]),
        ('Petersen',10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(i+5,5+(i+2)%5) for i in range(5)]),
    ]
    rng=random.Random(20261010)
    for n in range(5,10):
        for trial in range(6):
            edges=[(i,i+1) for i in range(n-1)];
            for i,j in combinations(range(n),2):
                if (i,j) in edges or rng.random()>.21:continue
                adj,_=normalize(n,edges)
                if not (adj[i]&adj[j]):edges.append((i,j))
            examples.append((f'random {n} #{trial}',n,edges))
    ptotal=[0]*4
    for name,n,edges in examples:
        n3,n2,steps,fg,beta=collapse_checks(n,edges)
        for i,v in enumerate(steps): ptotal[i]+=v
        print(f'{name:15s} F3={n3:5d} F2={n2:5d} steps={steps} graph={fg} b1={beta}')
    n,edges=3,[(0,1),(1,2),(0,2)]
    *_,F2,Fcross,Fstar,F3=data(n,edges)
    assert homology2_mod2(F2)==0
    assert homology2_mod2(F3)==2
    print('C3 sharpness: H2 mod 2 scale2=0, scale3=2')
    print('VERIFY_OK',len(examples),'triangle-free examples', 'total elementary collapses',ptotal)

if __name__=='__main__':main()
