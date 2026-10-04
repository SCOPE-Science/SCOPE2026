from fractions import Fraction as F
from math import isqrt

r = F(2)
K = F(100)
mu = F(1)
eta = F(3, 5)
h = F(30)
p1 = F(3, 10)
E = F(2)
p2 = F(1, 10)

c = 1 - p1 * E
A = eta * K - c * h
B = eta * K - h
assert c == F(2, 5)
assert A == F(48)
assert B == F(30)

# The source's flight-time logarithm argument is A/(c B).
log_argument = A / (c * B)
assert log_argument == F(4)
assert r == 2 and mu == 1
# Hence T=(1/2)log(4)=log(2), so exp(-mu*T)=1/2 exactly.
root = isqrt(log_argument.numerator)
assert root * root == log_argument.numerator and log_argument.denominator == 1
exp_minus_mu_T = F(1, root)
assert exp_minus_mu_T == F(1, 2)

pbar = p1 * h / A
assert pbar == F(3, 16)
assert p2 < pbar
assert 0 < p1 * E < 1
assert 0 < p2 * E < 1
assert h < eta * K

# Exact cancellation of the rational endpoint prefactors.
geometric_prefactor = (1 - p2 * E) * A / B
logistic_endpoint_factor = B / A
assert geometric_prefactor * logistic_endpoint_factor == 1 - p2 * E

rho = (1 - p2 * E) * exp_minus_mu_T
assert rho == F(2, 5)
assert 0 < rho < 1

print("VERIFY_OK")
