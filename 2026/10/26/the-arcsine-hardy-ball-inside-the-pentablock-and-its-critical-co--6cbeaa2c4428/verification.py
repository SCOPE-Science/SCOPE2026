#!/usr/bin/env python3
"""Exact arithmetic checks for the half-Dirichlet sphere Hardy module.
Scientific verification only; asymptotic theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb

def moment(k, l):
    # (1/2)_k (1/2)_l / (k+l)!
    x = Q(1)
    for i in range(k): x *= Q(2*i+1, 2)
    for j in range(l): x *= Q(2*j+1, 2)
    for t in range(2, k+l+1): x /= t
    return x

def diag(k,l):
    n=k+l
    plus=Q(2*k+1, 2*(n+1))
    minus=Q(0) if k==0 else Q(2*k-1,2*n)
    return plus-minus

def count(e):
    # Exact cutoff: outside n<1/e no eigenvalues except none.
    N=int(Q(1,1)/e)+2
    return sum(diag(k,n-k)>e for n in range(N) for k in range(n+1))

for n in range(30):
    for k in range(n+1):
        l=n-k
        assert moment(k+1,l)/moment(k,l)==Q(2*k+1,2*(n+1))
        assert moment(k,l+1)/moment(k,l)==Q(2*l+1,2*(n+1))
        assert moment(k+1,l)+moment(k,l+1)==moment(k,l)
        assert diag(k,l)>=0
        if k:
            assert diag(k,l)==Q(2*l+1,2*n*(n+1))
        else:
            assert diag(k,l)==Q(1,2*(n+1))
print('PASSED exact moments, spherical identity, and commutator spectrum for total degree <=29')
for den in [10,20,40,80,160,320,640,1280]:
    e=Q(1,den)
    num=count(e)
    scaled=Q(num,den**2)
    print('epsilon=1/%-4d count=%-10d epsilon^2*N=%.9f (limit %.9f)'%(den,num,float(scaled),1/6))
