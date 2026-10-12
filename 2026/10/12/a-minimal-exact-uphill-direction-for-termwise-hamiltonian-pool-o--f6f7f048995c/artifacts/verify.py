from fractions import Fraction
from math import sqrt

# Integer numerators for r, n, and the expected cross-product tangent.
r0 = (-1, -2, -1)
n0 = (2, 1, -4)
t0 = (-3, 2, -1)

assert sum(x*x for x in r0) == 6
assert sum(x*x for x in n0) == 21
assert sum(x*x for x in t0) == 14
assert sum(a*b for a, b in zip(r0, n0)) == 0

cross = (
    n0[1]*r0[2] - n0[2]*r0[1],
    n0[2]*r0[0] - n0[0]*r0[2],
    n0[0]*r0[1] - n0[1]*r0[0],
)
# n x r = cross/sqrt(126) = t0/sqrt(14), hence cross = 3*t0.
assert cross == tuple(3*x for x in t0)

# E*r_y = 1 and E*r_z = 1/2 exactly, where E=-3/sqrt(6).
assert Fraction((-3)*(-2), 6) == 1
assert Fraction((-3)*(-1), 6) == Fraction(1, 2)
v_y = -2 + 2*1
v_z = -2 + 2*Fraction(1, 2)
assert v_y == 0
assert v_z == -1

# J=(2,-1)^T/sqrt(14).
G = Fraction(4+1, 14)
assert G == Fraction(5, 14)
# b=J^T v=1/sqrt(14), and c^T J=1/sqrt(14), so their product is 1/14.
num_product = Fraction(1, 14)

# s_E=(1/14)/(5/14+lambda)=1/(5+14 lambda).
for lam in [Fraction(0), Fraction(1, 10), Fraction(1), Fraction(10)]:
    s = num_product / (G + lam)
    assert s == Fraction(1, 1) / (5 + 14*lam)
    assert s > 0

# H^2=2I and E^2=3/2, hence Var(H)=1/2 and exact ITE energy rate is -1.
var_h = Fraction(2) - Fraction(9, 6)
assert var_h == Fraction(1, 2)
assert -2*var_h == -1

print('VERIFY_OK')
