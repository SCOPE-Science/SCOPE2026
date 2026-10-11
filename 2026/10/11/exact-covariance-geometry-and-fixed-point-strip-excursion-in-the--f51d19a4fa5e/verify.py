from fractions import Fraction as F

# Stationary shear moment algebra.
Ey2 = F(17, 13)
ExY = -Ey2 / 2
Exy = ExY + Ey2
assert Exy == Ey2 / 2

# Parameter balance and centered-square conversion.
k = F(6, 5)
mu = F(-3, 10)
Vy = F(7, 11)
Exx1 = -(mu * Vy) / (2 * k)
Ecenter2 = Exx1 + F(1, 4)
assert Ecenter2 == F(1, 4) - mu * Vy / (2 * k)
assert Ecenter2 > F(1, 4)

# Covariance determinant inequality.
Vx = F(5, 7)
Cov = Vy / 2
det = Vx * Vy - Cov * Cov
assert det >= 0
assert Vx >= Vy / 4

# Equality reflection algebra.
dx = F(9, 8)
y = 2 * dx
# Image equality: X-m = Y/2, and X-m = dx + Y.
# Solve dx + Y = Y/2.
Y = -2 * dx
Xminusm = dx + Y
assert Y == -y
assert Xminusm == -dx

print("VERIFY_OK")
