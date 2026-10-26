#!/usr/bin/env python3
"""Standalone algebra checks for the Jacobian fold-topology formula.

Only standard-library dependencies. This is identity verification, not a numerical
certificate of the global connectedness theorem.
"""
from fractions import Fraction as Q
from math import pi, sqrt, cos, sin, atan2


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else Q(0)) +
            (b[i] if i < len(b) else Q(0)) for i in range(n)]


def scale(a, k):
    return [k * v for v in a]


# Circle identity: 3t^4 - 2t^3 - 6t^2 + 6t - 1
# = (t-1)^2 (3t^2 +4t -1).
assert mul([Q(1), Q(-2), Q(1)], [Q(-1), Q(4), Q(3)]) == [Q(-1),Q(6),Q(-6),Q(-2),Q(3)]

# Derivative of f(r)=r*(1+2t)/(2*(1+t+t^2)), t=r^4.
# Numerator under 2*(1+t+t^2)^2 equals -(6t^3+5t^2-7t-1).
g = [Q(1),Q(2)]
d = [Q(1),Q(1),Q(1)]
gp = [Q(2)]
dp = [Q(1),Q(2)]
num = add(mul(g,d),scale(mul([Q(0),Q(1)],add(mul(gp,d),scale(mul(g,dp),Q(-1)))),Q(4)))
assert num == [Q(1),Q(7),Q(-5),Q(-6)]

# Positive critical level and threshold, including one-sided inequalities.
a=3**(-0.25)
kstar=3*a/(4*sqrt(2))
Mstar=1+pi/(8*kstar)
assert abs(Mstar-(1+pi*sqrt(2)/(2*3**0.75)))<1e-12
assert 0.4029<kstar<0.4031 and 1.9744<Mstar<1.9746

# Independent Jacobian check using finite difference of the real harmonic u.
def harmonic(z):
    w=(1-z*z)/(1+z*z)
    return 2/pi*atan2(w.imag,w.real)

for z in (0.15+0.23j,0.45+0.31j,0.7-0.12j):
    eps=1e-6
    uy=(harmonic(z+1j*eps)-harmonic(z-1j*eps))/(2*eps)
    direct=-8/pi*(z/(1-z**4)).real
    assert abs(uy-direct)<1e-8, (z,uy,direct)

# Check the radial angular special cases used in the proof.
for r in (0.3,a,0.9):
    for theta in (pi/4,-pi/4):
        z=r*complex(cos(theta),sin(theta))
        assert abs((z/(1-z**4)).real-r/(sqrt(2)*(1+r**4)))<1e-12
    z=r*complex(.5,sqrt(3)/2)
    assert abs((z/(1-z**4)).real -r*(.5+r**4)/(1+r**4+r**8))<1e-12

print('CHECK_OK')
