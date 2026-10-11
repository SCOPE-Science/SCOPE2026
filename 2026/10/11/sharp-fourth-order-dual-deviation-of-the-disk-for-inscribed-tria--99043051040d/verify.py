#!/usr/bin/env python3
"""Independent arithmetic checks for the sharp fourth radial-moment bound."""
from fractions import Fraction
from math import sin, cos, pi, sqrt, isclose

# Exact polynomial identity on a 21^3 rational grid. The identity
# itself follows symbolically by expanding the two products.
for i in range(21):
    a = Fraction(i, 20)
    for j in range(21):
        b = Fraction(j, 20)
        for k in range(21):
            c = Fraction(k, 20)
            lhs = 2 - a - b - c + a*b*c
            rhs = (1-a)*(1-b)+(1-c)*(1-a*b)
            assert lhs == rhs and rhs >= 0

def wedge(a):
    return sin(2*a)*(2+cos(2*a))/3

def independent_moment(angles):
    """Barycentric second area moment, independent of wedge integration."""
    vertices = [(cos(x), sin(x)) for x in angles]
    cross = lambda u,v: u[0]*v[1]-u[1]*v[0]
    area = abs(sum(cross(vertices[i],vertices[(i+1)%3])
                   for i in range(3)))/2
    sx = sum(v[0] for v in vertices)
    sy = sum(v[1] for v in vertices)
    return area*(3+sx*sx+sy*sy)/12

for alpha in [(pi/3,pi/3,pi/3), (0.9,1.1,pi-2.0),
              (pi/2-0.03,pi/4+0.015,pi/4+0.015)]:
    assert all(0<a<pi/2 for a in alpha)
    angles = [0.0,2*alpha[0],2*(alpha[0]+alpha[1])]
    via_wedges = sum(wedge(a) for a in alpha)/4
    via_barycentric = independent_moment(angles)
    assert isclose(via_wedges,via_barycentric,abs_tol=3e-13)
    assert via_wedges < Fraction(1,3)

# The limiting right isosceles triangle has vertices (-1,0),(1,0),(0,1),
# area 1, squared vertex-norm sum 3, squared vertex-sum norm 1.
assert Fraction(1,12)*(3+1) == Fraction(1,3)
assert isclose(3*wedge(pi/3),3*sqrt(3)/4,abs_tol=1e-13)
assert isclose(wedge(pi/2)+2*wedge(pi/4),Fraction(4,3),abs_tol=1e-13)

# The symmetric angular direction exhibits both signs of a cubic saddle.
def difference(t):
    return 2*wedge(pi/3+t)+wedge(pi/3-2*t)-3*wedge(pi/3)
for h in (0.008,0.004,0.002):
    assert difference(h) < 0 < difference(-h)
    assert abs(difference(h)/h**3 + 8) < 1.0
    assert abs(difference(-h)/(-h)**3 + 8) < 1.0

print('DUAL_TRIANGLE_Q4_EXACT_CHECKS_OK')
