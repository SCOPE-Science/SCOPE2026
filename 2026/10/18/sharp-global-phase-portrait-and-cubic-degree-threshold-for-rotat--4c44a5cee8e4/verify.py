"""Standalone algebra checks for the rotational cubic map phase portrait.

Uses Python standard library only. These finite checks do not replace the
analytic global-invertibility and convergence proof in RESULT.md.
"""
from fractions import Fraction as Q
import cmath
import math

# Polynomial determinant identity from real Cartesian coordinates:
# Jacobian of (A(s) x-B(s) y, B(s) x+A(s) y), s=x*x+y*y.
def determinant_cartesian(x, y, ar, ai, br, bi):
    s = x*x + y*y
    A = ar + br*s
    B = ai + bi*s
    fx_x = A + 2*br*x*x - 2*bi*x*y
    fx_y = 2*br*x*y - B - 2*bi*y*y
    fy_x = B + 2*bi*x*x + 2*br*x*y
    fy_y = A + 2*bi*x*y + 2*br*y*y
    return fx_x*fy_y - fx_y*fy_x


def determinant_radial(x, y, ar, ai, br, bi):
    s = x*x + y*y
    m = ar*ar + ai*ai
    c = ar*br + ai*bi
    d = br*br + bi*bi
    return m + 4*c*s + 3*d*s*s

for x in [Q(-5, 3), Q(0), Q(7, 6)]:
    for y in [Q(-4, 5), Q(0), Q(2, 3)]:
        for ar, ai, br, bi in [
            (Q(-1, 2), Q(1, 4), Q(-1, 2), Q(-1, 4)),
            (Q(3, 5), Q(-1, 3), Q(4, 7), Q(1, 5)),
        ]:
            assert determinant_cartesian(x,y,ar,ai,br,bi) == determinant_radial(x,y,ar,ai,br,bi)

# Period-two exact rational coefficients, with a+b=-1 and positive Jacobian.
ar, ai, br, bi = Q(-1,2), Q(1,4), Q(-1,2), Q(-1,4)
m = ar*ar+ai*ai
c = ar*br+ai*bi
d = br*br+bi*bi
assert (m,c,d) == (Q(5,16), Q(3,16), Q(5,16))
assert ar+br == -1 and ai+bi == 0
assert determinant_radial(1,0,ar,ai,br,bi) == 2
assert m < 1 and c > 0

# Exact q=3: zeta satisfies zeta**3=1; a=b=zeta/2.
# Its radial Jacobian Q(s)=(1+4s+3s*s)/4; at s=1 it equals 2.
assert (Q(1)+4*Q(1)+3*Q(1))/4 == 2

# Samples of angular q-realization (numerics not used as infinite proof).
for q in range(3,19):
    zeta = cmath.exp(2j*math.pi/q)
    assert abs(zeta**q - 1) < 1e-11
    assert abs((zeta/2+zeta/2) - zeta) < 1e-12
    for k in range(1,q):
        assert abs(zeta**k-1) > 1e-10
print('VERIFY_OK')
