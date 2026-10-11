from fractions import Fraction as F

mu = F(1, 1000)
sigma = F(161, 500)
m = sigma - 1

assert m == F(-339, 500)
assert mu / 2 == F(1, 2000)

# Abstract stationary moments:
# E[x-m]=0 and E[y'^2-y^2]=0 for y'=y-mu(x-m).
varx = F(17, 13)
cov = mu * varx / 2
assert -2 * mu * cov + mu * mu * varx == 0

vary = F(5, 7)
det4 = 4 * varx * vary - 4 * cov * cov
assert det4 == 4 * varx * vary - mu * mu * varx * varx

# Slow increment identities.
vardy = mu * mu * varx
cov_y_dy = -mu * cov
assert cov_y_dy == -vardy / 2

# Equality-line reflection algebra.
dx = F(23, 19)
centered_y = mu * dx / 2
next_centered_y = centered_y - mu * dx
assert next_centered_y == -mu * dx / 2
next_dx = 2 * next_centered_y / mu
assert next_dx == -dx

print("VERIFY_OK")
