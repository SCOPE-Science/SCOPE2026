#!/usr/bin/env python3
"""Exact face, directed-Morse, cellular-boundary and mod-two checks.

Requires SymPy for exact Smith form: pip install sympy
Use: python verify.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ORDERS = {
    3: tuple(range(3)),
    4: tuple(range(6)),
    5: tuple(range(10)),
    6: (7, 2, 11, 13, 0, 14, 4, 1, 5, 10, 12, 6, 8, 9, 3),
    7: (17, 20, 6, 15, 12, 0, 9, 13, 5, 8, 16, 7, 2, 19, 10, 18, 3, 14, 4, 1, 11),
}
VECTORS = {
    3: (1, 3, 3),
    4: (1, 6, 15, 12, 3),
    5: (1, 10, 45, 90, 75, 12),
    6: (1, 15, 105, 375, 675, 477, 60),
    7: (1, 21, 210, 1155, 3570, 5607, 3507, 360),
}
CRITICALS = {3:{0:1,1:1},4:{0:1,1:1},5:{0:1,3:9},
             6:{0:1,3:1,4:27},7:{0:1,4:36,5:181}}
BETTIS = {3:{1:1},4:{1:1},5:{3:9},6:{4:26},7:{4:1,5:146}}

def all_faces(n):
    edges = tuple(combinations(range(n), 2))
    m = len(edges)
    forbidden=[]
    for a,b,c in combinations(range(m),3):
        es=(edges[a],edges[b],edges[c])
        if all(set(es[i]).intersection(es[j]) for i,j in ((0,1),(0,2),(1,2))):
            forbidden.append((1<<a)|(1<<b)|(1<<c))
    faces=[0]
    for j in range(m):
        bit=1<<j
        pairs=[f^bit for f in forbidden if f&bit]
        more=[a|bit for a in faces if not any((a&p)==p for p in pairs)]
        faces.extend(more)
    by_size=defaultdict(list)
    for f in faces:by_size[f.bit_count()].append(f)
    assert tuple(len(by_size[k]) for k in range(max(by_size)+1))==VECTORS[n]
    for face in faces:
        assert not any((face&t)==t for t in forbidden)
    return edges,forbidden,by_size

def signed_boundary(face):
    sign=1
    for j in range(face.bit_length()):
        if face&(1<<j):
            yield face^(1<<j),sign
            sign=-sign

def match_faces(n,fs,order):
    faces={f for level in fs.values() for f in level if f}
    unmatched=set(faces); pairs=[]
    for j in order:
        bit=1<<j
        for a in sorted(unmatched,key=lambda x:(x.bit_count(),x)):
            if a in unmatched and not (a&bit) and (a|bit) in unmatched:
                b=a|bit; pairs.append((a,b))
                unmatched.remove(a);unmatched.remove(b)
    cnt=Counter(f.bit_count()-1 for f in unmatched)
    assert dict(cnt)==CRITICALS[n]
    assert 2*len(pairs)+len(unmatched)==len(faces)
    lower_to_upper={a:b for a,b in pairs}
    upper_to_lower={b:a for a,b in pairs}
    indegree={f:0 for f in faces}; arrows=defaultdict(list); incidence_count=0
    for b in faces:
        if b.bit_count()==1:continue
        for a,_ in signed_boundary(b):
            src,dst=(a,b) if upper_to_lower.get(b)==a else (b,a)
            assert src in faces and dst in faces
            arrows[src].append(dst);indegree[dst]+=1;incidence_count+=1
    q=deque(f for f in faces if indegree[f]==0)
    seen=0
    while q:
        f=q.popleft();seen+=1
        for x in arrows[f]:
            indegree[x]-=1
            if indegree[x]==0:q.append(x)
    assert seen==len(faces), 'Gradient matching must be acyclic'
    return sorted(unmatched),lower_to_upper,len(pairs),incidence_count

def morse_boundary(crit,up,low_size):
    low=sorted(f for f in crit if f.bit_count()==low_size)
    high=sorted(f for f in crit if f.bit_count()==low_size+1)
    index={f:i for i,f in enumerate(low)}
    @lru_cache(None)
    def project(f):
        if f in index:return {index[f]:1}
        if f not in up:return {}
        b=up[f]; assert b.bit_count()==f.bit_count()+1
        s={}; matched_coeff=None
        for a,eps in signed_boundary(b):
            if a==f:
                matched_coeff=eps
            else:
                for i,v in project(a).items():
                    s[i]=s.get(i,0)-eps*v
        assert matched_coeff in (-1,1)
        return {i:matched_coeff*v for i,v in s.items() if v}
    rows=[[0]*len(high) for _ in low]
    for j,b in enumerate(high):
        acc={}
        for a,eps in signed_boundary(b):
            for i,v in project(a).items():acc[i]=acc.get(i,0)+eps*v
        for i,v in acc.items():rows[i][j]=v
    return Matrix(rows)

def mod2_betti(fs):
    piv_ranks={}
    for s in range(2,max(fs)+1):
        index={f:i for i,f in enumerate(fs[s-1])}
        piv={}
        for f in fs[s]:
            v=0
            for a,_ in signed_boundary(f):v ^= 1<<index[a]
            while v:
                top=v.bit_length()-1
                if top not in piv:
                    piv[top]=v;break
                v ^= piv[top]
        piv_ranks[s]=len(piv)
    result={}
    for s in range(1,max(fs)+1):
        b=len(fs[s])-piv_ranks.get(s, 1 if s==1 else 0)-piv_ranks.get(s+1,0)
        if b: result[s-1]=b
    return result,piv_ranks

def main():
    for n in range(3,8):
        edges,forbidden,fs=all_faces(n)
        # Independent forbidden-triple count: 3-stars plus cycles.
        assert len(forbidden)==n*((n-1)*(n-2)*(n-3)//6)+(n*(n-1)*(n-2)//6)
        critical,up,paired,inc=match_faces(n,fs,ORDERS[n])
        betti,ranks=mod2_betti(fs)
        assert betti==BETTIS[n],(n,betti)
        critcount=Counter(f.bit_count()-1 for f in critical)
        print('FACES_OK n=%d f=%s forbidden=%d' %(n,VECTORS[n],len(forbidden)),flush=True)
        print('MORSE_OK n=%d pairs=%d critical=%s dag_edges=%d'%(n,paired,dict(critcount),inc),flush=True)
        if n>=6:
            # A critical simplex with k edges has dimension k-1.
            R=morse_boundary(critical,up,low_size=4 if n==6 else 5)
            assert R.shape==((1,27) if n==6 else (36,181)),(n,R.shape)
            S=smith_normal_form(R,domain=ZZ)
            diags=[abs(int(S[j,j])) for j in range(min(S.shape))]
            assert diags==([1] if n==6 else [1]*35+[0]),(n,diags)
            print('SMITH_OK n=%d shape=%s invariant_factors=%s'%(n,R.shape,Counter(diags)),flush=True)
        print('BETTI_OK n=%d reduced_mod2=%s'%(n,betti),flush=True)
    print('ALL_VERIFY_OK triangle_free_2_matching_homotopy_n_3_to_7')
if __name__=='__main__':main()
