"""Independent finite checks for the highest-root deletion volume formula.

The proof is given in RESULT.md; finite checks do not prove the universal claim.
Run: python3 verify.py (SciPy volume comparison is optional).
"""
from fractions import Fraction
from math import factorial

def det(a):
    a=[[Fraction(x) for x in r] for r in a]
    n=len(a); d=Fraction(1)
    for j in range(n):
        k=next((k for k in range(j,n) if a[k][j]),None)
        assert k is not None
        if k!=j:
            a[k],a[j]=a[j],a[k];d=-d
        p=a[j][j];d*=p
        for k in range(j+1,n):
            z=a[k][j]/p
            for l in range(j+1,n):a[k][l]-=z*a[j][l]
            a[k][j]=0
    return d

def data(m):
    intervals=[tuple(int(i<=k<j) for k in range(m))
        for i in range(m) for j in range(i+1,m+1)]
    apex=(1,)*m
    prefix=[tuple(int(k<j) for k in range(m)) for j in range(1,m)]
    suffix=[tuple(int(k>=j) for k in range(m)) for j in range(1,m)]
    return intervals,apex,prefix,suffix

for m in range(2,17):
    vertices,apex,prefix,suffix=data(m)
    assert len(vertices)==m*(m+1)//2
    assert set(prefix+suffix).issubset(set(vertices))
    for p,s in zip(prefix,suffix):
        assert all(p[k]+s[k]==1 for k in range(m))
    # Every strict interior interval pairs with the apex to form a prefix/suffix sum.
    for i in range(1,m):
        for j in range(i+1,m):
            if j>=m:continue
            v=tuple(int(i<=k<j) for k in range(m))
            p=tuple(int(k<j) for k in range(m))
            s=tuple(int(k>=i) for k in range(m))
            assert all(apex[k]+v[k]==p[k]+s[k] for k in range(m))
    # Lattice chart (x1,...,x_{m-1}) of x1+x_m=1; contact vectors relative to apex/2.
    U=[[Fraction(prefix[j][i])-Fraction(1,2) for j in range(m-1)]
       for i in range(m-1)]
    assert abs(det(U))==Fraction(1,2)
    # Exact normalized volume of the crosspolytopal cone cap.
    assert (2**(m-1))*abs(det(U))==2**(m-2)

try:
    import numpy as np
    from scipy.spatial import ConvexHull
except ImportError:
    print('EXACT_OK; SciPy not installed, independent hull volumes skipped')
else:
    comparisons=0
    for m in range(2,9):
        vertices,apex,_,_=data(m)
        if m==2:
            full=1
            deleted=0
        else:
            full=ConvexHull(np.array(vertices,float)).volume*factorial(m)
            deleted=ConvexHull(np.array([v for v in vertices if v!=apex],float)).volume*factorial(m)
        assert abs(full-deleted-2**(m-2))<1e-6,(m,full,deleted)
        comparisons+=1
    print(f'VERIFY_OK: exact determinants and identities m=2..16; {comparisons} independent hull-volume comparisons')
