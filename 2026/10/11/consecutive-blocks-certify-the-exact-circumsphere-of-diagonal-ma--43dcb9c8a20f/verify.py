#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

def rank_q(mat):
    if not mat:
        return 0
    a=[list(map(Fraction,row)) for row in mat]
    m=len(a); n=len(a[0])
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]),None)
        if piv is None:
            continue
        a[r],a[piv]=a[piv],a[r]
        p=a[r][c]
        a[r]=[x/p for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c]
                a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
        if r==m:
            break
    return r

checks=0
for n in range(3,11):
    for k in range(2,n):
        m=n-k+1
        active=[(i,j) for i in range(k) for j in range(i,i+m)]
        idx={a:t for t,a in enumerate(active)}
        verts=[]
        for I in combinations(range(n),k):
            v=[0]*len(active)
            for i,j in enumerate(I):
                assert i<=j<=i+n-k
                v[idx[(i,j)]]=1
            verts.append(v)

        # Exact affine rank.
        v0=verts[0]
        diffs=[[v[j]-v0[j] for j in range(len(active))] for v in verts[1:]]
        assert rank_q(diffs)==k*(n-k)

        center=[Fraction(1,m)]*len(active)
        R2=Fraction(k*(n-k),m)
        for v in verts:
            d2=sum((Fraction(v[j])-center[j])**2 for j in range(len(active)))
            assert d2==R2

        # Consecutive block certificate.
        acc=[0]*len(active)
        for s in range(m):
            I=tuple(range(s,s+k))
            v=[0]*len(active)
            for i,j in enumerate(I):
                v[idx[(i,j)]]=1
            for j,x in enumerate(v):
                acc[j]+=x
        assert all(x==1 for x in acc)
        assert all(Fraction(x,m)==center[j] for j,x in enumerate(acc))

        checks+=1

print(f"VERIFY_OK diagonal-matching-field-circumsphere parameter_pairs={checks} k>=2 n<=10 exact=yes")
