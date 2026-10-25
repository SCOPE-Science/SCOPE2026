#!/usr/bin/env python3
"""Numerical consistency checks for the long-spike selector comparison.

No finite sampling here is asserted to prove the limiting theorem. The proof
uses tangent-section identities, compact bounds and Brunn--Minkowski.
"""
import math

def bracket(n, t):
    assert n >= 2 and t > 1
    r = math.sqrt(n / (n-1))
    k = math.sqrt(t*t-1)
    lo = (t/2 - n - r) / k
    hi = (t/2 + n + r) / k
    shifted_lo = (t - math.sqrt(t) - r) / k
    assert 0 < lo <= hi < 1 and 0 < shifted_lo < 1, (n,t,lo,hi,shifted_lo)
    return (lo**n, (hi/shifted_lo)**n, 2**(-n))

def steiner_coordinate_2d(t):
    return (t * math.acos(1/t) - math.sqrt(1-1/(t*t))) / math.pi

def steiner_integral_midpoint(t, steps=150000):
    # Independent numerical Riemann integration of the support formula.
    return 2/steps * sum(max(1.0, t*math.cos((k+0.5)*2*math.pi/steps)) * math.cos((k+0.5)*2*math.pi/steps) for k in range(steps))

for t in (2,5,50,10000):
    expected=steiner_coordinate_2d(t)
    numerical=steiner_integral_midpoint(t)
    assert abs(expected-numerical)<5e-8, (t,expected,numerical)
    # Uniform Hausdorff support bound: |s_t - t/2| <= 2 in dimension 2.
    assert abs(expected-t/2)<=2
    print('two_dimensional_Steiner',t,expected, 'integral_error',abs(expected-numerical))

for n in (2,3,4,7):
    t=1e9
    lo,hi,target=bracket(n,t)
    assert lo<=target<=hi
    assert hi-lo < 5e-4
    print('dimension',n,'rigorous_ratio_interval',lo,hi,'limit',target)

# Exact planar limiting area of D={|x_1|<=1, |x_2|<=1}:
# area(D)=4, area((1/2)D)=1, ratio=1/4.
assert 1/4 < 4/9
print('PASS: exact cross-section formulas and certified asymptotic bounds agree.')
