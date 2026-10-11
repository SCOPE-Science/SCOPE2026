#!/usr/bin/env python3
"""Finite reproducibility diagnostics for quadratic Bowen coefficient geometry.
The analytic volume identity and asymptotic theorem require the accompanying proof.
"""
from fractions import Fraction as F
from math import comb, sqrt, factorial
import random

# The exact coefficient-body volume follows from two one-dimensional beta integrals.
I_squared = F(32,9)  # (integral_{-1}^1 sqrt(1-u) du)^2
V3 = F(16,1) + 4*I_squared
assert V3 == F(272,9)
assert 2*V3 == F(544,9)

# Exact orbit/finite-difference polynomial equality in dimensions 2..6.
rng = random.Random(11472026)
checks = 0
for d in range(2,7):
    for n in (3,5,9,17):
        for _ in range(35):
            u=[F(rng.randint(-7,7),rng.randint(2,11)) for j in range(d)]
            x=u[:]
            for k in range(n):
                actual=x[-1]
                expected=sum(F(comb(k,j))*u[d-1-j] for j in range(min(k,d-1)+1))
                assert actual==expected, (d,n,k,actual,expected)
                x=[x[0]]+[x[i]+x[i-1] for i in range(1,d)]
                checks+=1

# Independent midpoint quadrature of the exact admissible curvature interval.
for h in (64,256,1024):
    s=0.
    for i in range(h):
        u=-1+(2*i+1)/h
        for j in range(h):
            v=-1+(2*j+1)/h
            w_upper=(sqrt(1-u)+sqrt(1-v))**2
            w_lower=-(sqrt(1+u)+sqrt(1+v))**2
            s+=w_upper-w_lower
    approx=s*(2/h)**2
    assert abs(approx-float(V3))<0.055, (h,approx)
    print('quadratic_volume_grid',h,round(approx,9))

print('EXACT_VOLUME_COEFFICIENT',V3)
print('EXACT_VOLUME_PARABOLIC_D3',2*V3)
print('FINITE_ORBIT_IDENTITY_CHECKS',checks)
print('CHECKS_OK')
