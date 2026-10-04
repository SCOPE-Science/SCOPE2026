from fractions import Fraction as F

Lambda = F(1, 1)
mu = F(1, 5)
eps = F(3, 4)
sigma1 = F(3, 5)
a = eps * sigma1
a2 = a * a

k = F(1, 1) + 2 * mu / a2
q = 2 * Lambda / a2

# Zero-current identity: (a^2 s^2 p)'/p = a^2(1-k)s + a^2 q
# for p(s) proportional to s^(-k-1) exp(-q/s).
assert a2 * (1 - k) == -2 * mu
assert a2 * q == 2 * Lambda

assert mu > a2 / 2
assert k == F(241, 81)
assert q == F(800, 81)
mean = q / (k - 1)
variance = q*q / ((k - 1)*(k - 1)*(k - 2))
assert mean == F(5, 1)
assert variance == F(2025, 79)

# The nonzero diffusion coefficient at the deterministic susceptible level.
s_star = Lambda / mu
assert a * s_star != 0

print('VERIFY_OK')
