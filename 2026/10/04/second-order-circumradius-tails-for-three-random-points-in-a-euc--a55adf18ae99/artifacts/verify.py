#!/usr/bin/env python3
from fractions import Fraction
from math import gamma, pi, sqrt

def coeff_a(d):
    return Fraction(3*d*(d*d-1)*(3*d-1),
                    2*(2*d+1)*(3*d+1)*(4*d+1))

assert coeff_a(2) == Fraction(1, 7)
assert coeff_a(3) == Fraction(144, 455)
C3 = Fraction(3, 55)
assert C3 * coeff_a(3) == Fraction(432, 25025)
assert coeff_a(3) / C3 + Fraction(1, 2) == Fraction(1147, 182)

def kappa(m):
    return pi**(m/2.0) / gamma(m/2.0 + 1.0)

def simpson(f, a, b, n=20000):
    if n % 2:
        n += 1
    h = (b-a)/n
    s = f(a) + f(b)
    for j in range(1, n):
        s += (4 if j % 2 else 2) * f(a + j*h)
    return s*h/3.0

def exact_segment(d, R, ell):
    def f(s):
        return (sqrt(R*R-s*s)-sqrt(R*R-ell*ell))**(d-1)
    return kappa(d-1) * simpson(f, -ell, ell)

def beta(a, b):
    return gamma(a)*gamma(b)/gamma(a+b)

def approx_segment(d, R, ell):
    q = (d*d-1)/(2.0*(2*d+1))
    lead = (kappa(d-1)*beta(d, 0.5)*ell**(2*d-1)
            /(2.0*R)**(d-1))
    return lead * (1.0 + q*ell*ell/(R*R))

for d in (2, 3, 4):
    ell = 0.73
    vals = []
    for R in (20.0, 40.0):
        exact = exact_segment(d, R, ell)
        approx = approx_segment(d, R, ell)
        vals.append((exact/approx - 1.0)*R**4)
    assert all(abs(v) < 1.0 for v in vals)
    assert abs(vals[1]-vals[0]) < 0.02

print("VERIFY_OK")
