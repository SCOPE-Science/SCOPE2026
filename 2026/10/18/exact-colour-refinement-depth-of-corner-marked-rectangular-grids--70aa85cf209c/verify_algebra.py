#!/usr/bin/env python3
"""Separate polynomial/certificate check, without constructing any graph or WL colours."""
from collections import defaultdict
from math import comb

def boundary_series(q, i, cap):
    # coefficients of (r^i+r^(q-1-i))/(1-r^q)
    a=[0]*(cap+1)
    for t in range(i,cap+1,q): a[t]+=1
    for t in range(q-1-i,cap+1,q): a[t]+=1
    return a

def orbit_type(i,j,m,n):
    a=min(i,m-1-i); b=min(j,n-1-j)
    return tuple(sorted((a,b))) if m==n else (a,b)

cases=0; coeffs=0; fingerprints=0
for m in range(2,34):
 for n in range(m,46):
    R=n+m//2-2
    D=m+n-1
    if (m,n) not in ((2,2),(2,3),(3,3),(3,4)):
        assert R-1 >= D//2, (m,n,R,D)
    # Boundary series reflects side distances and includes repeated central residue.
    cache_m=[boundary_series(m,i,R-1) for i in range(m)]
    cache_n=[boundary_series(n,j,R-1) for j in range(n)]
    bins=defaultdict(set)
    for i in range(m):
     for j in range(n):
        fp=tuple(cache_m[i][t]+cache_n[j][t] for t in range(R))
        bins[fp].add(orbit_type(i,j,m,n));fingerprints+=1
    if (m,n) not in ((2,2),(2,3),(3,3),(3,4)):
        if any(len(q)>1 for q in bins.values()):
            raise AssertionError(('boundary fingerprint',m,n,[q for q in bins.values() if len(q)>1][:1]))
    # Sharp witness: row-reflected pair at last column, the nearer distance is R.
    a=m//2
    y1=(a-1,n-1)
    y2=(a if m%2==0 else a+1,n-1)
    assert sum(y1)==R and sum(y2)>R
    assert y1[0]+y2[0]==m-1
    assert orbit_type(*y1,m,n)==orbit_type(*y2,m,n)
    # At each allowed root distance <=R the distance+shortest-walk count
    # is a full unordered-coordinate certificate.
    dct={}
    for i in range(m):
     for j in range(n):
      if i+j>R:continue
      sig=(i+j,comb(i+j,i))
      other=dct.get(sig)
      if other is not None and sorted(other)!=sorted((i,j)):
       raise AssertionError(('geodesic collision',m,n,sig,other,(i,j)))
      dct[sig]=(i,j)
    cases+=1;coeffs+=R
print(f'ALGEBRA_PASS parameter_pairs={cases} fingerprints={fingerprints} coefficient_checks={coeffs}')
