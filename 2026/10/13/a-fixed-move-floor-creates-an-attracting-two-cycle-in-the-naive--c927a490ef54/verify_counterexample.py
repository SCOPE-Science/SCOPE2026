from fractions import Fraction as F

A = (F(1), F(-50))
B = (F(1), F(-5))
C = (F(2), F(50))
alpha = F(9, 10)


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a-b for a, b in zip(x, y))


def mul(c, x):
    return tuple(c*a for a in x)


def theta(x, p):
    d = sub(p, x)
    return dot(p, d) / dot(d, d)

# Initial step: C is uniquely selected and the cap is active.
assert dot(B, C) < dot(B, B) < dot(B, A)
assert theta(B, C) == F(1376, 1513) > alpha
x1 = add(mul(alpha, B), mul(F(1,10), C))
assert x1 == (F(11,10), F(1,2))
assert dot(x1, A) < dot(x1, B) < dot(x1, C)
assert theta(x1, A) > alpha

# Rectangle endpoint bounds used by the analytic invariant proof.
# R_minus: u in [1,2], v in [-5,-50/19].
assert F(2) + F(55)*F(-50,19) < 0
assert F(2) + F(100)*F(-50,19) < 0
assert F(4) + F(50)*F(-50,19) < 0
# The C-step clipping margin is positive throughout because both summands are nonnegative,
# and the b-summand is strictly positive even at b=55.
assert F(2) - alpha*F(1) > 0
assert F(50) - alpha*F(55) > 0
# Image endpoints for the v-coordinate lie in R_plus.
assert alpha*F(-5) + F(5) == F(1,2)
assert alpha*F(-50,19) + F(5) == F(50,19)

# R_plus: u in [1,2], v in [1/2,50/19].
assert -F(45)*F(1,2) < 0
assert -F(1) - F(100)*F(1,2) < 0
assert F(2) - F(50)*F(1,2) < 0
# Lower bound for the A-step clipping margin.
bmax = F(1000,19)
assert bmax*(F(50)-alpha*bmax) - (F(1)+alpha) > 0
# Image endpoints for v lie in R_minus.
assert alpha*F(1,2) - F(5) >= F(-5)
assert alpha*F(50,19) - F(5) == F(-50,19)

# Exact cycle and two-step contraction.
xm = (F(28,19), F(-50,19))
xp = (F(29,19), F(50,19))
assert add(mul(alpha, xm), mul(F(1,10), C)) == xp
assert add(mul(alpha, xp), mul(F(1,10), A)) == xm
assert theta(xm, C) > alpha
assert theta(xp, A) > alpha
assert dot(xm, C) < 0 and dot(xp, A) < 0
assert alpha*alpha == F(81,100)

# Fixed point of the two-step affine map x -> 81/100 x + 9/100 C + 1/10 A.
rhs = add(mul(F(9,100), C), mul(F(1,10), A))
assert mul(F(19,100), xm) == rhs

print('VERIFY_OK')
