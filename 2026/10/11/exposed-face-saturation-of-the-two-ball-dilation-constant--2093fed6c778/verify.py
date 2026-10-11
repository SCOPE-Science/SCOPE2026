"""Finite exact and high-precision checks supplementing the analytic theorem."""
from fractions import Fraction
from decimal import Decimal, localcontext
from math import sin, cos, pi, sqrt

# A rational clipped-disk example in the regime where the modulus test is zero.
a = Fraction(15, 16)
b_squared = 1 - a * a
assert b_squared == Fraction(31, 256)
assert Fraction(1, 4) < 4*b_squared < 1  # 1/2 < 2b < 1, after squaring.
assert Fraction(3,4) < a*a <= Fraction(15,16)

# An exact saturating clipped-disk witness at a=4/5, b=3/5.
a = Fraction(4, 5)
b = Fraction(3, 5)
x = (a,b)
z1 = (a,b)
z2 = (a,-b)
def square_norm(v):
    return v[0]*v[0]+v[1]*v[1]
def clipped_norm_squared(v):
    return max(square_norm(v), (v[0]/a)**2)
assert clipped_norm_squared(x) == 1
assert clipped_norm_squared(z1) == clipped_norm_squared(z2) == 1
assert clipped_norm_squared((z1[0]-z2[0],z1[1]-z2[1])) >= 1
for z in (z1,z2):
    y = (-2*z[0],-2*z[1])
    assert clipped_norm_squared((x[0]-y[0],x[1]-y[1])) == 9

# Spot-check the exact two-step chord formula for centered regular 2m-gons.
for N in range(4, 82, 2):
    R_vertical = 1.0 if N % 4 == 0 else cos(pi/N)
    D_radial = 2*sin(2*pi/N)/R_vertical
    D_formula = 2*sin(2*pi/N) if N%4 == 0 else 4*sin(pi/N)
    assert abs(D_radial-D_formula) < 1e-12
    edge_upper = 2*sin(pi/N)/cos(pi/N)
    assert edge_upper <= D_formula + 1e-12
    assert (D_formula >= 1-1e-12) == (N <= 12)
assert abs(2*sin(2*pi/12)-1) < 1e-14
assert 4*sin(pi/14) < 1

# Independent small-N polygonal gauge computation from support halfspaces.
for N in (4,6,8,10,12,14,16,18,20):
    verts = [(cos(2*pi*j/N),sin(2*pi*j/N)) for j in range(N)]
    halfspaces = [((cos((2*j+1)*pi/N),sin((2*j+1)*pi/N)),cos(pi/N))
                  for j in range(N)]
    def gauge(v):
        return max((u[0]*v[0]+u[1]*v[1])/h for u,h in halfspaces)
    delta = gauge((verts[1][0]-verts[-1][0], verts[1][1]-verts[-1][1]))
    assert abs(delta-(2*sin(2*pi/N) if N%4==0 else 4*sin(pi/N)))<1e-12
    if N <= 12:
        x = verts[0]
        z1,z2 = verts[-1],verts[1]
        assert gauge((z1[0]-z2[0],z1[1]-z2[1]))>=1-1e-12
        for z in (z1,z2):
            assert abs(gauge((x[0]+2*z[0],x[1]+2*z[1]))-3)<1e-11
print('VERIFY_OK')
