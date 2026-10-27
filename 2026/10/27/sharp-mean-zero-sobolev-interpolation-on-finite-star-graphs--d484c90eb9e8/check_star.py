#!/usr/bin/env python3
"""Independent finite-parameter checks for a sharp star-graph Sobolev inequality.

Only the symbolic argument in RESULT.md proves the infinite family. This
program verifies bisection, witnesses, polynomial signs, and sampled inputs.
Requires only the Python standard library.
"""
from decimal import Decimal, getcontext
from random import Random
from math import sqrt

getcontext().prec = 70

def P(n,c):
    return (2*n*(n*n+n-1)*c**3 + 3*(n*n+2*n-1)*c*c
            + (n**3+2*n*n-n+4)*c + 2*n)

def M(n,c):
    return (n*c*c+2*c+n)/(n-1)

def E(n,c):
    return ((n*n+n-1)*c*c+2*c+n)/(n-1)

def solve(n):
    N = Decimal(n)
    lo, hi = -1/N, Decimal(0)
    assert P(N,lo)<0 and P(N,hi)>0
    for k in range(310):
        mid=(lo+hi)/2
        if P(N,mid)<0:lo=mid
        else:hi=mid
    c=(lo+hi)/2
    C=1/(M(N,c)*E(N,c)).sqrt()
    return c,C

def direct_ratio(v):
    mass=sum(x*x for x in v)
    energy=sum((x-v[-1])**2 for x in v[:-1])
    if mass==0 or energy==0:return 0.0
    return max(abs(x) for x in v)**2/sqrt(mass*energy)

rng=Random(732911)
for n in range(2,51):
    c,C=solve(n)
    witness=[float(1), *([-float((1+c)/Decimal(n-1))]*(n-1)), float(c)]
    assert abs(sum(witness))<3e-14
    assert abs(direct_ratio(witness)-float(C))<2e-14
    assert Decimal(n)/(Decimal(n+1)**3).sqrt()<C<1
    for k in range(150):
        z=[rng.uniform(-2,2) for _ in range(n)]
        z.append(-sum(z))
        assert direct_ratio(z) <= float(C)+1e-11
    if n in (2,3,4,7,15,50):
        print(f'n={n}  c={c:.16f}  C={C:.16f}')
print('PASS: n=2..50, witness, root, center comparison and 7,350 sampled mean-zero real inputs')
