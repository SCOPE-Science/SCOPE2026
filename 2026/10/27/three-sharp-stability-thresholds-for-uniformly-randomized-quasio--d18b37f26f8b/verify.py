"""Finite consistency checks for uniformly randomized quasioptimal line projections.

Requires Python >=3.9; uses no third-party dependencies. Infinite-time claims
in the accompanying proof are analytic and are not certified by this program.
"""
from fractions import Fraction as F
from math import sqrt, log, exp, isclose


def second_moment(c, s, r):
    return c*c + s*s*r*r/F(3)


def fourth_moment(c, s, r):
    return c**4 + 2*c*c*s*s*r*r + s**4*r**4/F(5)


def log_exponent(c, r):
    s = sqrt(1-c*c)
    if r == 0:
        return log(c) if c > 0 else float('-inf')
    if c == 0:
        return log(r)-1
    lo, hi = c-s*r, c+s*r
    def primitive(x):
        return x*log(abs(x))-x if x != 0 else 0.0
    return (primitive(hi)-primitive(lo))/(2*s*r)


def solve_root(c):
    lo, hi = sqrt(3), 4.0
    while log_exponent(c, hi) < 0:
        hi *= 2
    for _ in range(100):
        mid = (lo+hi)/2
        if log_exponent(c, mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


# A rational right triangle makes the moment algebra exactly checkable.
c, s = F(3,5), F(4,5)
for r in (F(1,2), F(1), F(3,2), F(2), F(4)):
    m2 = second_moment(c,s,r)
    m4 = fourth_moment(c,s,r)
    # Independently integrate each even polynomial using symmetric moments.
    polynomial_m2 = c*c + (s*r)**2/3
    polynomial_m4 = c**4 + 6*c*c*(s*r)**2/3 + (s*r)**4/5
    assert m2 == polynomial_m2
    assert m4 == polynomial_m4

# The sharp second moment threshold is angle independent.
for (a,b) in ((F(3,5), F(4,5)), (F(5,13),F(12,13)), (F(0),F(1))):
    assert second_moment(a,b,F(1)) < 1
    assert second_moment(a,b,F(3)) > 1
    assert second_moment(a,b,F(0)) == a*a
    assert second_moment(a,b,F(1)) == a*a+b*b/F(3)
    assert second_moment(a,b,F(3)) == a*a+3*b*b
    assert (a*a+b*b)==1

# Numerical tests of the exact log primitive and critical threshold.
for angle_cos in (0.0, 0.2, 0.5, 0.8, 0.95):
    root = solve_root(angle_cos)
    safe = (1-angle_cos)/sqrt(1-angle_cos**2)
    assert safe < sqrt(3) < root
    assert log_exponent(angle_cos, sqrt(3)) < 0
    assert abs(log_exponent(angle_cos,root)) < 2.e-12
    assert log_exponent(angle_cos,1.01*root) > 0
    assert log_exponent(angle_cos,.99*root) < 0
assert isclose(solve_root(0.0), exp(1), rel_tol=1.e-14)

# Geometric admissibility under a signed state: endpoint distances agree.
for x in (F(-3,2), F(2,3)):
    for u in (F(-2), F(-1), F(0), F(1), F(2)):
        y = x*(c+s*u)
        squared_distance = x*x+y*y-2*c*x*y
        minimum_distance = s*s*x*x
        assert squared_distance >= minimum_distance
        assert squared_distance-minimum_distance == (s*x*u)**2

print('VERIFY_OK')
