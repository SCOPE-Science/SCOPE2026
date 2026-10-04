from fractions import Fraction as F

# Positive exact parameters satisfying b1 = 1/a1.
a1 = F(2)
b = b1 = F(1, 2)
b2 = F(1, 3)
a2 = F(3, 4)
a3 = F(5, 4)
a4 = F(2, 3)
assert b1 == 1 / a1


def field(u, v, w):
    du = u * (1 - a1 * u) * (u - b1) / (u + b2) - u * v
    dv = v * (u - w - a2)
    dw = w * (a3 * v - a4)
    return du, dv, dw


def critical_field(u, v, w):
    du = -a1 * u * (u - b) ** 2 / (u + b2) - u * v
    dv = v * (u - w - a2)
    dw = w * (a3 * v - a4)
    return du, dv, dw


def Ldot_from_field(u, v, w):
    du, dv, dw = field(u, v, w)
    return du + dv + dw / a3


def Ldot_formula(u, v, w):
    return -a1 * u * (u - b) ** 2 / (u + b2) - a2 * v - (a4 / a3) * w

# The critical reduction is exact for arbitrary rational test states.
for state in [
    (F(0), F(0), F(0)),
    (b, F(0), F(0)),
    (F(1, 4), F(2, 5), F(3, 7)),
    (F(1), F(1, 6), F(2, 9)),
    (F(7, 5), F(4, 11), F(5, 13)),
]:
    assert field(*state) == critical_field(*state)
    assert Ldot_from_field(*state) == Ldot_formula(*state)

# Both points in the Lyapunov zero set are genuine equilibria.
assert field(F(0), F(0), F(0)) == (F(0), F(0), F(0))
assert field(b, F(0), F(0)) == (F(0), F(0), F(0))

# On v=0 the prey drift is negative away from 0 and b.
def axis_du(u):
    return field(u, F(0), F(0))[0]

assert axis_du(F(1, 4)) < 0 < b
assert axis_du(F(1)) < 0 and F(1) > b
assert axis_du(F(0)) == 0
assert axis_du(b) == 0

# Reciprocal-variable coefficient for u -> b from above.
limit_zprime = a1 * b / (b + b2)
assert limit_zprime == 1 / (b + b2)
assert 1 / limit_zprime == b + b2

print('VERIFY_OK')
