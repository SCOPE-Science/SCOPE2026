#!/usr/bin/env python3
"""Reproduce exact polynomial identities and finite diagnostic checks for the stated theorem.
This diagnostic does not replace the analytic compactness argument for its limit.
"""
from fractions import Fraction
from math import cos, pi, sin

def mul(a, b):
    out = {}
    for power_a, ca in a.items():
        for power_b, cb in b.items():
            mon = (power_a[0] + power_b[0], power_a[1] + power_b[1])
            out[mon] = out.get(mon, Fraction(0)) + ca * cb
    return {k: v for k, v in out.items() if v}

def add(*polys):
    out = {}
    for poly in polys:
        for mon, val in poly.items():
            out[mon] = out.get(mon, Fraction(0)) + val
    return {k: v for k, v in out.items() if v}

def scale(poly, factor):
    return {k: v * factor for k, v in poly.items() if v * factor}

a = {(1, 0): Fraction(1)}
b = {(0, 1): Fraction(1)}
minus = add(b, scale(a, -1))
squares = add(mul(a,a), scale(mul(b,b), -1))
quartic_D = {(4,0): Fraction(3,4), (0,4): Fraction(1,4), (3,1): Fraction(-1)}
identity = add(scale(mul(squares, squares), Fraction(3,8)),
               scale(mul(mul(mul(minus,minus), minus),add(b,scale(a,3))), Fraction(-1,8)))
assert quartic_D == identity, (quartic_D, identity)

for n in (2, 4, 8, 32, 128):
    u = [sin(pi*k/(n+1)) for k in range(1,n+1)]
    ratio = sum(u[k]*u[k+1] for k in range(n-1))/sum(y*y for y in u)
    assert abs(ratio-cos(pi/(n+1))) < 2e-13, (n,ratio)

for p in (1.5, 2.0, 3.0, 4.0, 8.0):
    target = 2*(p-1)*pi*pi/(p*p)
    ratios = []
    for n in (512, 2048):
        u = [sin(pi*k/(n+1)) for k in range(1,n+1)]
        x = [t**(2/p) for t in u]
        defect = 1-sum(x[k]**(p-1)*x[k+1] for k in range(n-1))/sum(t**p for t in x)
        ratios.append((n+1)**2*defect)
    assert abs(ratios[1]-target)<0.07*max(1,target), (p,ratios,target)
    print('p',p,'sine-test scales',tuple(round(x,8) for x in ratios),'limit',round(target,8))
print('CHECK_OK: exact quartic identity, Hilbert sine eigenvector, and finite diagnostic convergence')
