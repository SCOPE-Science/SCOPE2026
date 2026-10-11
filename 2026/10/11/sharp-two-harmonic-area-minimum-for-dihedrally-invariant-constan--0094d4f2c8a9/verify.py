#!/usr/bin/env python3
"""Numerical diagnostics for a sharp two-frequency constant-width area formula."""
import math
from fractions import Fraction


def norm_cubic(a, b):
    """Exact continuous sup over the circle of a*cos(t)+b*cos(3*t)."""
    vals = [abs(a + b)]
    if b:
        z2 = (3.0*b - a)/(12.0*b)
        if 0 < z2 < 1:
            z = math.sqrt(z2)
            vals.append(abs((a - 3.0*b)*z + 4.0*b*z**3))
    return max(vals)


def m_s(s):
    return 1.0 - s if s <= 1.0/9.0 else math.sqrt((1.0+3.0*s)**3/(27.0*s))


for r in (Fraction(1, 10), Fraction(3, 28), Fraction(6, 55)):
    for s in (Fraction(1, 12), Fraction(1, 9), Fraction(1, 6), Fraction(1, 2), Fraction(5, 3), Fraction(30)):
        poly = 1 - 6*s + 3*r*s*s
        lhs = 27*poly/(1+3*s)**4
        # Exact derivative of 27*s*(1+r*s*s)/(1+3*s)**3.
        rhs = 27*((1+3*r*s*s)*(1+3*s)-9*s*(1+r*s*s))/(1+3*s)**4
        assert lhs == rhs
        assert abs(norm_cubic(1.0, -float(s)) - m_s(float(s))) < 5e-13


for n in (3, 5, 7, 9, 21, 101):
    r = (n*n-1)/(9*n*n-1)
    q = math.sqrt(1.0-r/3.0)
    s = 1.0/(3.0*(1.0+q))
    a = math.sqrt(27.0*s/(1.0+3.0*s)**3)
    b = -s*a
    F = 6.0*(1+q)/(2+q)**2
    assert abs(norm_cubic(a, b)-1.0) < 3e-14
    assert abs(1.0-6.0*s+3.0*r*s*s) < 2e-14
    assert abs(F - (a*a+r*b*b)) < 3e-14
    assert F > 4.0/3.0
    for k in range(4096):
        phi = 2.0*math.pi*k/4096
        x, y = math.cos(phi), math.sin(phi)
        sup = norm_cubic(x, y)
        assert (x*x+r*y*y)/(sup*sup) <= F+2e-12
    # Independent trapezoid integration of the support function and its derivative.
    N = 8192
    sm = 0.0
    min_rad = 1.0
    for k in range(N):
        theta = 2.0*math.pi*k/N
        c1, c3 = math.cos(n*theta), math.cos(3*n*theta)
        h = 0.5 - a*c1/(2*(n*n-1)) - b*c3/(2*(9*n*n-1))
        hprime = a*n*math.sin(n*theta)/(2*(n*n-1)) + b*3*n*math.sin(3*n*theta)/(2*(9*n*n-1))
        sm += h*h - hprime*hprime
        rad = 0.5*(1.0+a*c1+b*c3)
        min_rad = min(min_rad, rad)
    integrated = math.pi*sm/N
    predicted = math.pi/4-math.pi*F/(8*(n*n-1))
    assert abs(integrated-predicted) < 3e-12
    assert min_rad > -2e-12
    xcontact = math.sqrt((1+3*s)/(12*s))
    # At the negative cubic peak the radius-of-curvature density vanishes.
    tcontact = math.acos(-xcontact)
    contact_rad = 0.5*(1+a*math.cos(tcontact)+b*math.cos(3*tcontact))
    assert abs(contact_rad) < 2e-14

print('VERIFY_OK: six odd orders, exact derivative identities, cubic norms,')
print('4096 sampled coefficient directions per order, area quadrature and contacts')
