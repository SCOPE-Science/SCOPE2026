#!/usr/bin/env python3
"""Consistency checks for the reverse-Hölder phase-transition cusp."""
from fractions import Fraction
import math

def simpson(f, a, b, n=20000):
    if n % 2:
        n += 1
    h = (b-a)/n
    s = f(a) + f(b)
    for k in range(1, n):
        s += (4 if k % 2 else 2) * f(a + k*h)
    return s*h/3

def J(p):
    return simpson(lambda x: (x**p)*math.exp(x), 0.0, 1.0)

def M(p):
    return math.exp(-1.0)*(math.gamma(p+1.0)+J(p))

def hfun(p):
    return math.gamma(p+1.0) - (math.e/2.0)**p * M(p)

lo, hi = 2.9414, 2.9415
assert hfun(lo) > 0.0 and hfun(hi) < 0.0
for _ in range(70):
    mid = (lo+hi)/2.0
    if hfun(mid) > 0.0:
        lo = mid
    else:
        hi = mid
p0 = (lo+hi)/2.0

def A(p):
    return math.gamma(p+1.0)**(1.0/p)

def B(p):
    return (math.e/2.0)*(M(p)**(1.0/p))

eps = 2.0e-5
Aprime = (A(p0+eps)-A(p0-eps))/(2.0*eps)
Bprime = (B(p0+eps)-B(p0-eps))/(2.0*eps)
gap = Bprime-Aprime
assert gap > A(p0)/(90.0*p0)
assert gap > A(p0)/270.0

coarse = (Fraction(7,5)+Fraction(1,3))/6 - Fraction(3,10)
assert coarse == -Fraction(1,90)
assert Fraction(59,500) < Fraction(1,6)

print(f"p0≈{p0:.12f}")
print(f"C(p0)≈{A(p0):.12f}")
print(f"branch derivative gap≈{gap:.12f}")
print(f"proved coarse relative lower bound > {1/(90*p0):.12f}")
print("VERIFY_OK")
