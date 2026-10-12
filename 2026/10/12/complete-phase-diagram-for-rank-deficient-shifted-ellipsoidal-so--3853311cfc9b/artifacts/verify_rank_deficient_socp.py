from fractions import Fraction as F

def check_compatible(hdiag, b, delta, a):
    # hdiag is nonnegative diagonal; b is required to vanish on zero entries.
    assert len(hdiag) == len(b)
    assert all(h >= 0 for h in hdiag)
    assert all((h != 0 or bi == 0) for h, bi in zip(hdiag, b))

    beta2 = sum((bi * bi / h) for h, bi in zip(hdiag, b) if h != 0)
    # Choose tests with rational Delta supplied by construction outside this helper.
    return beta2

# Strict compatible case with beta = 3/2 and Delta = 2.
# H = diag(1,4,0), b = (1, sqrt(5) is inconvenient), so use a rational beta example.
H = [F(1), F(4), F(0)]
b = [F(1), F(2), F(0)]
delta = F(3, 2)
beta2 = check_compatible(H, b, delta, F(0))
assert beta2 == F(2)

# Use a rational Pythagorean choice beta = 3/4 by changing data.
H = [F(4), F(0), F(9), F(0)]
b = [F(1), F(0), F(3, 2), F(0)]
# beta^2 = 1/4 + 1/4 = 1/2; pick a = 3/2 and keep Delta algebraic would defeat exact fractions.
# Instead verify the formulas algebraically after parameterizing beta and Delta by a Pythagorean triple.

beta = F(3, 4)
Delta = F(1)
a = F(5, 4)
delta = F(7, 5)
assert a * a - beta * beta == Delta * Delta

# A diagonal effective H and b realizing beta = 3/4.
H = [F(4), F(0), F(1), F(0)]
b = [F(3, 2), F(0), F(0), F(0)]
beta2 = check_compatible(H, b, delta, a)
assert beta2 == beta * beta

# Moore-Penrose solution z_R = -(delta/Delta) H^dagger b.
zR = [
    -(delta / Delta) * (bi / h) if h != 0 else F(0)
    for h, bi in zip(H, b)
]
t = delta * a / Delta
quad = sum(h * zi * zi for h, zi in zip(H, zR))
assert t * t == delta * delta + quad
obj = a * t + sum(bi * zi for bi, zi in zip(b, zR))
assert obj == delta * Delta

# Arbitrary nullspace shifts preserve constraint and objective.
for k2, k4 in [(F(5), F(-7)), (F(-11, 3), F(2, 5))]:
    z = [zR[0], k2, zR[2], k4]
    quad2 = sum(h * zi * zi for h, zi in zip(H, z))
    obj2 = a * t + sum(bi * zi for bi, zi in zip(b, z))
    assert quad2 == quad
    assert obj2 == obj

# Incompatible objective: a kernel component gives an explicit feasible ray to -infinity.
Hbad = [F(1), F(0)]
bbad = [F(0), F(2)]
delta_bad = F(1)
a_bad = F(100)
values = []
for s in [F(1), F(10), F(100)]:
    # z = (0,-s), t = delta is feasible because H ignores the second coordinate.
    values.append(a_bad * delta_bad - F(2) * s)
assert values[0] > values[1] > values[2]
assert values[2] < 0

# Zero objective edge case.
Hzero = [F(0), F(0)]
bzero = [F(0), F(0)]
assert check_compatible(Hzero, bzero, F(2), F(0)) == 0

print("VERIFY_OK")
