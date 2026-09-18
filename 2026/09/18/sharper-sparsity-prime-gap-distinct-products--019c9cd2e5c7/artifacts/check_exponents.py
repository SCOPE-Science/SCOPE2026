from fractions import Fraction as F

def q(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)

theta = F(1, 20)
rho = F(20, 39)

raw_p2 = F(1, 2) + 5 * theta
raw_pge3 = F(1, 3) + 6 * theta
raw = max(raw_p2, raw_pge3)

assert raw_p2 == F(3, 4)
assert raw_pge3 == F(19, 30)
assert raw == F(3, 4)

equal_desc = (1 - theta) * raw + 2 * theta
raw_lengths = raw + theta
E1 = (raw + theta) * rho + 5 * theta
L1 = 1 - rho + 5 * theta
raw_coeff = raw + theta - 4 * theta / (1 - rho)
long_coeff = (1 - rho) - 4 * theta * rho / (1 - rho)

assert equal_desc == F(13, 16)
assert raw_lengths == F(4, 5)
assert E1 == F(103, 156)
assert L1 == F(115, 156)
assert raw_coeff == F(37, 95) > 0
assert long_coeff == F(205, 741) > 0
assert max(raw_lengths, E1, L1) < equal_desc

theta0 = F(2, 43)
raw0 = F(1, 2) + 5 * theta0
limit = (1 - theta0) * raw0 + 2 * theta0
assert limit == F(2927, 3698)

print("theta =", q(theta))
print("p=2 raw exponent =", q(raw_p2))
print("p>=3 raw exponent <=", q(raw_pge3))
print("refined raw exponent =", q(raw))
print("all-equal descendant exponent =", q(equal_desc))
print("raw-root length exponent =", q(raw_lengths))
print("first unequal raw-root exponent =", q(E1))
print("first long-root exponent =", q(L1))
print("raw-path monotonicity coefficient =", q(raw_coeff))
print("long-path monotonicity coefficient =", q(long_coeff))
print("Li-threshold limiting exponent =", q(limit))
