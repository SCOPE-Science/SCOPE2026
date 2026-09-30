from fractions import Fraction as F


def show(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)

# Original fixed parameter.
theta = F(1, 20)
rho = 1 / (2 - theta)
A = F(1, 2) + 5 * theta
pge3 = F(1, 3) + 6 * theta
Fmass = (1 - theta) * A + 2 * theta
raw_lengths = A + theta
E1 = (A + theta) * rho + 5 * theta
L1 = 1 - rho + 5 * theta
raw_coeff = A + theta - 4 * theta / (1 - rho)
long_coeff = (1 - rho) - 4 * theta * rho / (1 - rho)

assert A == F(3, 4)
assert pge3 == F(19, 30)
assert Fmass == F(13, 16)
assert raw_lengths == F(4, 5)
assert E1 == F(103, 156)
assert L1 == F(115, 156)
assert raw_coeff == F(37, 95) > 0
assert long_coeff == F(205, 741) > 0
assert max(raw_lengths, E1, L1) < Fmass

print("theta =", show(theta))
print("raw p=2 exponent =", show(A))
print("raw p>=3 exponent <=", show(pge3))
print("all-equal mass exponent =", show(Fmass))
print("raw-root length exponent =", show(raw_lengths))
print("first unequal exponent =", show(E1))
print("first long-root exponent =", show(L1))
print("raw monotonicity coefficient =", show(raw_coeff))
print("long monotonicity coefficient =", show(long_coeff))

# Current almost-all short-interval threshold from Li III.
theta0 = F(1, 24)
rho0 = 1 / (2 - theta0)
A0 = F(1, 2) + 5 * theta0
pge30 = F(1, 3) + 6 * theta0
limit = (1 - theta0) * A0 + 2 * theta0
raw_lengths0 = A0 + theta0
E10 = (A0 + theta0) * rho0 + 5 * theta0
L10 = 1 - rho0 + 5 * theta0
raw_coeff0 = A0 + theta0 - 4 * theta0 / (1 - rho0)
long_coeff0 = (1 - rho0) - 4 * theta0 * rho0 / (1 - rho0)

assert A0 == F(17, 24)
assert pge30 == F(7, 12)
assert limit == F(439, 576)
assert raw_lengths0 == F(3, 4)
assert E10 == F(667, 1128)
assert L10 == F(787, 1128)
assert raw_coeff0 == F(113, 276) > 0
assert long_coeff0 == F(341, 1081) > 0
assert max(raw_lengths0, E10, L10) < limit

print("Li III endpoint theta0 =", show(theta0))
print("endpoint raw exponent =", show(A0))
print("endpoint p>=3 exponent <=", show(pge30))
print("limiting short-gap mass exponent =", show(limit))
print("endpoint raw-root length exponent =", show(raw_lengths0))
print("endpoint first unequal exponent =", show(E10))
print("endpoint first long-root exponent =", show(L10))
print("endpoint raw monotonicity coefficient =", show(raw_coeff0))
print("endpoint long monotonicity coefficient =", show(long_coeff0))
