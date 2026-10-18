#!/usr/bin/env python3
"""Independent exact-rational checks for the three-direction tight-frame extremizers."""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def determinant(a):
    a=[row[:] for row in a]; n=len(a); det=F(1)
    for k in range(n):
        p=next((j for j in range(k,n) if a[j][k]),None)
        if p is None: return F(0)
        if p!=k: a[p],a[k]=a[k],a[p]; det=-det
        z=a[k][k]; det*=z
        for j in range(k+1,n):
            ratio=a[j][k]/z
            for t in range(k+1,n): a[j][t]-=ratio*a[k][t]
            a[j][k]=F(0)
    return det

C=((F(1),F(1,2),F(-1,2)),
   (F(1,2),F(1),F(1,2)),
   (F(-1,2),F(1,2),F(1)))
for m in (6,9,12):
    n=m-2; kinds=[i%3 for i in range(m)]
    g=[[F(m,n)*(F(int(i==j))-F(2,m)*C[kinds[i]][kinds[j]]) for j in range(m)] for i in range(m)]
    assert all(g[i][i]==1 for i in range(m))
    # Projector P=(n/m)G has rank n; this follows analytically from three-line isotropy.
    maxdet=max(determinant([[g[i][j] for j in idx] for i in idx]) for idx in combinations(range(m),n))
    target=F(3*m**(n-2),n**n)
    assert maxdet==target,(m,maxdet,target)
    baseline=F(m**n,n**n*comb(m,n))
    assert target / baseline == F(3*(m-1),2*m)
    print(f'm={m} n={n} maxdet={maxdet} baseline={baseline} verified')
print('EQUAL_LEVERAGE_CODIMENSION_TWO_EXACT_CHECKS_OK')
