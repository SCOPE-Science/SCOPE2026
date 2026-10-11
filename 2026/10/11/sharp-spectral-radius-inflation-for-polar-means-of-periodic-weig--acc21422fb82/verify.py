#!/usr/bin/env python3
"""Exact rational finite checks for sharp periodic polar-mean spectral inflation."""
from fractions import Fraction as F
from itertools import product

def theta(K, lam):
    return 1 + lam*(1-lam)*(K-1)**2/K

def ratio_power(ws,lam):
    a=F(1)
    n=len(ws)
    for j,w in enumerate(ws):
        a *= (lam*w+(1-lam)*ws[(j+1)%n])/w
    return a

def transitions(bits):
    return sum(bits[i]!=bits[(i+1)%len(bits)] for i in range(len(bits)))

for K in [F(2),F(3),F(7,2)]:
    for lam in [F(1,4),F(1,2),F(3,4)]:
        t=theta(K,lam)
        assert (lam*K+(1-lam))*(lam+(1-lam)*K)/K == t
        for n in range(2,10):
            top=t**(n//2)
            winner=0
            for bits in product([0,1],repeat=n):
                ws=[K if b else F(1) for b in bits]
                actual=ratio_power(ws,lam)
                k=transitions(bits)//2
                assert actual==t**k
                assert actual<=top
                if actual==top:
                    assert transitions(bits)==2*(n//2)
                    winner+=1
            assert winner==(2 if n%2==0 else 2*n)
        for ws in [[F(1),F(3,2),K], [F(1),F(5,4),F(3,2),K], [F(1),F(2),F(3),K] if K>=3 else [F(1),F(7,6),F(5,4),K]]:
            if max(ws)>K: continue
            n=len(ws)
            x=ratio_power(ws,lam)
            assert F(1)<=x<=t**(n//2)
print('PERIODIC_POLAR_MEAN_SPECTRAL_INFLATION_EXACT_OK')
