#!/usr/bin/env python3
"""Exact finite regression identities for a power-Hardy commutator.
The analytic asymptotic and operator-ideal statements require the written proof.
"""
from fractions import Fraction as Q
from itertools import combinations

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
           -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
           +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def k(x,t,a):
    return (t**a-x**a)/x

n=0
for a in range(1,7):
    # Direct evaluation of the exact inner/outer Hilbert--Schmidt integrals.
    integral=(1-Q(2,a+1)+Q(1,2*a+1))/Q(2*a)
    closed=Q(a,(a+1)*(2*a+1))
    assert integral==closed
    n+=1
    # Unitary dilation on a lower interval of length d.
    d=Q(1,3)
    for x in [Q(1,3),Q(2,3),Q(4,5)]:
        for t in [Q(1,7),Q(1,4)]:
            if not t<x: continue
            assert k(d*x,d*t,a)==d**(a-1)*k(x,t,a)
            n+=1
    # Cross-block kernel is exactly a sum of two separable channels.
    low=[Q(1,11),Q(1,8),Q(1,5),Q(1,4)]
    high=[Q(3,5),Q(2,3),Q(3,4),Q(7,8)]
    mat=[[k(x,t,a) for t in low] for x in high]
    for i,j,h in combinations(range(4),3):
        for c,d,e in combinations(range(4),3):
            assert det3([[mat[r][s] for s in (c,d,e)] for r in (i,j,h)])==0
            n+=1
    for i,x in enumerate(high):
        for j,t in enumerate(low):
            assert mat[i][j]==(t**a)/x-x**(a-1)
            n+=1
print('HARDY_POWER_COMMUTATOR_EXACT_FINITE_IDENTITIES_OK checks='+str(n))
