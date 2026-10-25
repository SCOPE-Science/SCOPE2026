#!/usr/bin/env python3
"""Exact-rational checks of finite-resolution lattice miniature scale laws."""
from math import comb
from fractions import Fraction as Q
from itertools import product

def C(n, k):
    return comb(n, k) if n>=k>=0 else 0

def check(h,t):
    d=len(h)-1
    lp=lambda n:sum(h[j]*C(n+d-j,d) for j in range(d+1))
    native=[lp(t-i) for i in range(t+1)]
    Z=sum(native)
    direct=[Q(x,Z) for x in native]
    delta=[Q(C(t-i+d,d),C(t+d+1,d+1)) for i in range(t+1)]
    assert sum(direct)==sum(delta)==1
    weights=[h[j]*C(t+d+1-j,d+1) for j in range(d+1)]
    assert sum(weights)==Z
    mixture=[]
    for i in range(t+1):
        mixture.append(sum((Q(weights[j],Z)*Q(C(t-j-i+d,d),C(t-j+d+1,d+1)) for j in range(d+1) if j<=t and weights[j]),Q(0)))
    assert mixture==direct
    ratios=[direct[i]/delta[i] for i in range(t+1)]
    assert all(ratios[i]>=ratios[i+1] for i in range(t))
    assert all(sum(direct[i:])<=sum(delta[i:]) for i in range(1,t+1))
    EJ=Q(sum(j*weights[j] for j in range(d+1)),Z)
    mean=sum(Q(i)*direct[i] for i in range(t+1))
    assert mean==Q(t-EJ,d+2)
    if any(h[j]>0 and j<=t for j in range(1,d+1)):
        assert all(sum(direct[i:])<sum(delta[i:]) for i in range(1,t+1))
    else:
        assert direct==delta

def polycount(vertices,k):
    # Testing selected polygons by closed-form Pick counts.
    a2=abs(sum(vertices[i][0]*vertices[(i+1)%len(vertices)][1]-vertices[(i+1)%len(vertices)][0]*vertices[i][1] for i in range(len(vertices))))
    from math import gcd
    B=sum(gcd(abs(vertices[i][0]-vertices[(i+1)%len(vertices)][0]),abs(vertices[i][1]-vertices[(i+1)%len(vertices)][1])) for i in range(len(vertices)))
    return Q(a2*k*k+B*k+2,2)

def trial_polygon(v,t):
    # Reconstruct h* from evaluations and confirm independent Pick enumeration.
    d=2
    L=[polycount(v,i) for i in range(3)]
    h=[1,int(L[1]-3),int(L[2]-3*L[1]+3)]
    assert all(z>=0 for z in h)
    check(h,t)
    for n in range(t+1):
        assert sum(h[j]*C(n+2-j,2) for j in range(3))==polycount(v,n)

N=0
for d in range(1,7):
    for tail in product(range(4),repeat=min(d,3)):
        h=[1]+list(tail)+[0]*(d-min(d,3))
        for t in range(1,13):
            check(h,t);N+=1
for v in (
    [(0,0),(1,0),(0,1)],
    [(0,0),(2,0),(0,1)],
    [(0,0),(3,0),(0,2)],
    [(0,0),(2,1),(1,2)],
    [(0,0),(1,0),(1,1),(0,1)],
    [(0,0),(2,0),(2,2),(0,2)],
):
    for t in range(1,10):
        trial_polygon(v,t);N+=1
print('MINIATURE_LAW_EXACT_OK cases=',N)
