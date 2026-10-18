#!/usr/bin/env python3
"""Exact finite checks for the toric small-alpha fan automorphism theorem.
The all-dimensional proof is independent of these finite checks.
"""
from itertools import combinations
from math import gcd

def rank_mod(rows, p):
    if not rows:
        return 0
    a=[list(map(lambda x:x%p, r)) for r in rows]
    n=len(a[0]); m=len(a); k=0
    for j in range(n):
        pivot=next((i for i in range(k,m) if a[i][j]), None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k]
        inv=pow(a[k][j],-1,p)
        a[k]=[u*inv%p for u in a[k]]
        for i in range(k+1,m):
            if a[i][j]:
                d=a[i][j]
                a[i]=[(u-d*v)%p for u,v in zip(a[i],a[k])]
        k+=1
        if k==n:break
    return k

def check(n):
    L=2*n-1
    verts=[]; tags=[]
    for p in range(n+1):
        for q in range(n+1):
            if q==p:continue
            v=[-L if i==p else 1 if i==q else 2 for i in range(n+1)]
            assert sum(v)==0 and gcd(*v)==1
            verts.append(v[:n]);tags.append((p,q))
    assert len(verts)==n*(n+1)
    assert all(sum(v[i] for v in verts)==0 for i in range(n))
    for p in range(n+1):
        lower=[(a,b) for (a,b) in tags if a==p]
        upper=[(a,b) for (a,b) in tags if p not in (a,b)]
        assert len(lower)==n and len(upper)==n*(n-1)
    # Two sparse nonzero ray pairings cannot occur, as the others span N_Q.
    count=0
    for i,j in combinations(range(len(verts)),2):
        rows=[v for k,v in enumerate(verts) if k not in (i,j)]
        assert rank_mod(rows,1009)==n,(n,i,j)
        count+=1
    if n==2:
        det=lambda v,w:v[0]*w[1]-v[1]*w[0]
        v_lower=[verts[k] for k,(p,q) in enumerate(tags) if p==2]
        v_upper=[verts[k] for k,(p,q) in enumerate(tags) if 2 not in (p,q)]
        assert abs(det(*v_lower))==3
        assert abs(det(*v_upper))==8
    return len(verts),count

if __name__=='__main__':
    for n in range(2,9):
        rays,pairs=check(n)
        print('dimension',n,'rays',rays,'rank_verified_after_any_two_deleted',pairs)
    print('VERIFY_OK')
