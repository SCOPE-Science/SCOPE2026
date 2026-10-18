"""Finite independent checks for an analytic solid-angle/fullness theorem.

No finite test establishes the universal statement; see RESULT.md for proof.
"""
from fractions import Fraction
from math import sqrt, atan, pi
from itertools import permutations


def det3(a, b, c):
    return (a[0] * (b[1]*c[2]-b[2]*c[1])
            -a[1] * (b[0]*c[2]-b[2]*c[0])
            +a[2] * (b[0]*c[1]-b[1]*c[0]))


def inspect(x, y, z):
    assert 0 < x <= y <= z
    a, b, c = sqrt(x*x+y*y), sqrt(x*x+z*z), sqrt(y*y+z*z)
    Q = a*b*c + x*x*c + y*y*b + z*z*a
    t = 2*x*y*z/Q
    omega = 2*atan(t)
    volume = 8*x*y*z/3
    diameter = 2*c
    mu = volume/diameter**3
    assert omega*omega < 6*mu*(1+3e-14), (x,y,z,omega*omega/mu)
    assert y*y*b+z*z*a >= a*b*c*(1-3e-14)
    assert (a*b)**2 >= 2*x*y*z*c*(1-3e-14)
    return omega*omega/mu


for x in range(1, 19):
    for y in range(x, 19):
        for z in range(y, 19):
            # Identity checked exactly on rational parameters, without radical evaluation.
            xf, yf, zf = Fraction(x), Fraction(y), Fraction(z)
            cf2 = yf*yf + zf*zf
            left = (xf*xf+yf*yf)*(xf*xf+zf*zf)
            # (xy... radical) identity reduces to polynomial equality.
            reduced = left-(xf**4 + xf*xf*cf2 + yf*yf*zf*zf)
            assert reduced == 0
            inspect(float(x),float(y),float(z))

vertices = [(2,3,5), (2,-3,-5), (-2,3,-5), (-2,-3,5)]
for v in vertices:
    e = [tuple(w[i]-v[i] for i in range(3)) for w in vertices if w != v]
    assert abs(det3(*e)) == 16*2*3*5

values = [inspect(e,e,1.0) for e in (1e-1,1e-2,1e-3,1e-4)]
assert all(a<b for a,b in zip(values,values[1:]))
assert 5.999 < values[-1] < 6
print('DISPHENOID_SHARP_SOLID_ANGLE_CHECKS_OK')
