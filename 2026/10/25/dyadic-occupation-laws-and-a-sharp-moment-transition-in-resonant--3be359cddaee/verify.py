#!/usr/bin/env python3
"""Exact orbit and dyadic valuation checks for a linear proportional-delay recurrence."""
from fractions import Fraction
from math import log2

def valuation2(n):
    r = 0
    while n % 2 == 0:
        r += 1
        n //= 2
    return r

def orbit(d, n):
    a = [Fraction(1)]
    for k in range(n - 1):
        a.append(-a[-1] + d * a[k//2])
    return a

def level(d, r):
    u = d - 1
    for _ in range(r):
        u = d*u - 1
    return u

checks = 0
for d in map(Fraction, ['-3', '-2', '-1', '0', '1/2', '1', '3/2', '2', '3']):
    n = 4096
    x = orbit(d, n)
    for j, z in enumerate(x):
        expected = Fraction(1) if j % 2 == 0 else level(d, valuation2((j+1)//2))
        assert z == expected, (d, j, z, expected)
        checks += 1
    K = n // 2
    for r in range(12):
        observed = sum(1 for k in range(K) if valuation2(k+1) == r)
        expected = K // (2**r) - K // (2**(r+1))
        assert observed == expected
        checks += 1
    if d == 2:
        assert all(z == 1 for z in x)
    if d == 1:
        assert x[2*(2**10-1)+1] == -10
    if d == -1:
        assert all(z in [-2, 1] for z in x)
for d in (-2,3,-3):
    p = log2(2)/log2(abs(d))
    C = d*(d-2)/(d-1)
    target = abs(C)**p/4
    estimates=[]
    for m in (8, 10, 12):
        x = orbit(Fraction(d), 2**(m+1))
        estimate = sum(float(abs(z))**p for z in x)/len(x)/(m+1)
        estimates.append(estimate)
    assert abs(estimates[-1]-target) < abs(estimates[0]-target)
    print('critical',d,'target',round(target,9),'ratios',[round(v,9) for v in estimates])
print('VERIFY_OK exact_orbit_indices=',checks,'parameters=9')
