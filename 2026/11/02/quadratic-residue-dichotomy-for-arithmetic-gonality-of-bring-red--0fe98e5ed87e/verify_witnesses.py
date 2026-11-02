#!/usr/bin/env python3
"""Independently check the two exceptional quadratic-place witnesses in Bring's canonical model."""
from itertools import combinations

def check(p,nonsquare,aa,bb):
    # a + b*w, w^2=nonsquare
    def A(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def M(x,y):return ((x[0]*y[0]+nonsquare*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    u=[(a,b) for a,b in zip(aa,bb)]
    assert len(u)==5 and any(y for x,y in u)
    for k in [1,2,3]:
        s=(0,0)
        for comb in combinations(u,k):
            v=(1,0)
            for x in comb:v=M(v,x)
            s=A(s,v)
        assert s==(0,0),(p,k,s)
    # Frobenius sends w to -w, so not projectively fixed due first coordinate 1
    assert u[0]==(1,0)
    assert all(x[1]==0 for x in u[:3])
    print(f'CHAR_{p}_QUADRATIC_PLACE_OK')

check(3,2,[1,0,2,0,0],[0,0,0,1,2])
check(7,3,[1,0,6,0,0],[0,0,0,3,4])
print('VERIFY_OK')
