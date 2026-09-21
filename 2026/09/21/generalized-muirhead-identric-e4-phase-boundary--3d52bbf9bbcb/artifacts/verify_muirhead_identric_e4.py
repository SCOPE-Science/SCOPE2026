#!/usr/bin/env python3
"""Supplementary checks for the Muirhead-identric E4 phase result.

The proof in RESULT.md is analytic.  This file supplies:
1. exact rational checks of the two displayed E4 examples;
2. the exact rational logarithm certificate for the mixed-sign example;
3. floating-point sanity checks of the hyperbolic normal form and a few
   illustrative numerical minima of R_d.
"""
from fractions import Fraction
from math import cosh, exp, log, tanh, sqrt

def L(d):
    return (2*d*d + 1)/3

def U(d):
    return min(d, 1.5*d*d)

def R(d, z):
    return log(cosh(d*z)) / (z/tanh(z) - 1)

def golden_min(f, a, b, steps=200):
    phi = (1 + sqrt(5.0))/2
    c = b - (b-a)/phi
    d = a + (b-a)/phi
    fc, fd = f(c), f(d)
    for _ in range(steps):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - (b-a)/phi
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + (b-a)/phi
            fd = f(d)
    x = (a+b)/2
    return x, f(x)

def atanh_log_bounds(q, m=2):
    """Bounds log((1+q)/(1-q)) by truncating 2*atanh(q)."""
    q = Fraction(q)
    low = 2*sum(q**(2*k+1)/Fraction(2*k+1) for k in range(m+1))
    tail = 2*q**(2*m+3)/(Fraction(2*m+3)*(1-q*q))
    return low, low+tail

# Exact E4 membership for the globally positive example.
d1 = Fraction(3,4)
s1 = Fraction(18,25)
a1, b1 = Fraction(147,200), Fraction(-3,200)
assert a1+b1 == s1 and a1-b1 == d1 and a1*b1 < 0
assert 3*d1*d1 - 2*s1 == Fraction(99,400)
assert 2*d1*d1 - 3*s1 + 1 == Fraction(-7,200)

# Exact E4 membership for the mixed-sign example.
d2 = Fraction(2,3)
s2 = Fraction(33,50)
a2, b2 = Fraction(199,300), Fraction(-1,300)
assert a2+b2 == s2 and a2-b2 == d2 and a2*b2 < 0
assert 3*d2*d2 - 2*s2 == Fraction(1,75)
assert 2*d2*d2 - 3*s2 + 1 == Fraction(-41,450)

# Rigorous sign certificate at y/x=64.
# log(17/8) has q=9/25; log 2 has q=1/3.
ln17_low, ln17_up = atanh_log_bounds(Fraction(9,25), 2)
ln2_low, ln2_up = atanh_log_bounds(Fraction(1,3), 2)
F_upper = Fraction(1) + Fraction(50,33)*ln17_up - Fraction(65,21)*ln2_low
expected = Fraction(-43568079809, 14910328125000)
assert F_upper == expected and F_upper < 0

# Floating sanity check of the exact log-ratio formula at the same point.
z = 3*log(2)
F_float = 1 + (50/33)*log(17/8) - (65/21)*log(2)
assert F_float < 0

# Illustrative numerical phase values.  These are not proof certificates.
for dd in (0.64, 2/3, 0.68, 0.69):
    zz, cc = golden_min(lambda w: R(dd, w), 1e-7, 30.0)
    assert L(dd) < cc < U(dd)
    print(f"d={dd:.12g}  minimizer~{zz:.12g}  C(d)~{cc:.12g}")

print("exact mixed-example upper bound =", F_upper, float(F_upper))
print("direct floating log(M/I) at y/x=64 =", F_float)
print("all checks passed")
