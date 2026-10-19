#!/usr/bin/env python3
"""Numerical corroboration of the exact parabolic phase-only zero-gap theorem.
Run with Python 3: python verify.py. The universal claims require the analytic proof.
"""
import cmath
import itertools
import math
import random

TOL = 2e-9
zeta = cmath.exp(2j*math.pi/3)


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))


def sharp_gap(p):
    eps = 2*math.pi/(3*p)
    sign = -1 if p % 3 == 1 else 1
    return math.sqrt(3)*math.sin(eps)+sign*(1-math.cos(eps))


def minima(p):
    q = p//3
    if p % 3 == 1:
        return {(q,2*q),(q,2*q+1),(q+1,2*q+1)}
    return {(q,2*q+1),(q+1,2*q+1),(q+1,2*q+2)}


checks=0
for p in range(5, 252):
    if not isprime(p):
        continue
    w=[cmath.exp(2j*math.pi*j/p) for j in range(p)]
    delta=sharp_gap(p)
    closest=minima(p)
    assert len(closest)==3
    for r,s in itertools.product(range(p), repeat=2):
        value=abs(1+zeta*w[r]+zeta*zeta*w[s])
        if (r,s)==(0,0):
            assert value < TOL
        elif (r,s) in closest:
            assert abs(value-delta)<TOL, (p,r,s,value,delta)
        else:
            assert value>delta-TOL, (p,r,s,value,delta)
        checks += 1

rng=random.Random(20261016)
for p in (5,7,11,13,17):
    w=[cmath.exp(2j*math.pi*j/p) for j in range(p)]
    supports=list(itertools.combinations(range(p), 3))
    if p >= 11:
        supports=rng.sample(supports, min(15, len(supports)))
    for R in supports:
        v_origins=list(itertools.product(range(p),repeat=2))
        if p>=11:
            v_origins=rng.sample(v_origins,min(12,len(v_origins)))
        for a0,b0 in v_origins:
            for orientation in (-1,1):
                c=[zeta**(orientation*i)*w[(-a0*x*x-b0*x)%p]
                   for i,x in enumerate(R)]
                magnitudes=[]
                for a,b in itertools.product(range(p),repeat=2):
                    y=sum(c[i]*w[(a*x*x+b*x)%p] for i,x in enumerate(R))
                    magnitudes.append((a,b,abs(y)))
                    checks+=1
                zeros=[(a,b) for a,b,v in magnitudes if v<TOL]
                assert zeros==[(a0,b0)], (p,R,a0,b0,orientation,zeros)
                others=[(a,b,v) for a,b,v in magnitudes if (a,b)!=(a0,b0)]
                delta=sharp_gap(p)
                assert abs(min(v for a,b,v in others)-delta)<TOL
                assert sum(abs(v-delta)<TOL for a,b,v in others)==3

print('VERIFY_OK',checks,'numeric comparisons; all primes 5..251 and sampled parabolic triples')
