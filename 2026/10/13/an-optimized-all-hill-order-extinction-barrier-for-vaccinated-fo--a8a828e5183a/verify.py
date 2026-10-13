"""Reproduce exact examples and finite auxiliary checks for the accompanying theorem.

No external packages, private data, or network access are needed.
"""
from fractions import Fraction as Q
from math import isclose


def dot(row, col):
    return sum((a * b for a, b in zip(row, col)), Q(0))


Lambda = mu = xi = gamma = death = eta = phi = omega = kappa = Q(1)
sigma, p = Q(10), Q(1, 2)
beta1, beta2, alpha2 = Q(5), Q(1, 10), Q(1, 10)
a = xi + mu
b = gamma + death + mu
D = mu * (sigma + eta + mu) + p * eta * sigma
S0 = Lambda * (eta + mu) / D
V0 = Lambda * sigma / D
L2 = Q(1, 2) / kappa
assert D == 17 and S0 == Q(2, 17) and V0 == Q(10, 17)
q0 = beta1 * S0 + beta2 * V0
Rc = xi * q0 / (a * b)
assert q0 == Q(11, 17) and Rc == Q(11, 102)


def epidemic_threshold(alpha1):
    r0 = alpha1 * S0 + alpha2 * V0
    r = L2 * r0
    threshold = xi * (q0 + phi * r / omega) / (a * b)
    coarse = Lambda * xi / (mu * a * b) * (beta1 + phi * L2 * alpha1 / omega)
    return r, threshold, coarse


r, threshold, coarse = epidemic_threshold(Q(10))
assert r == Q(21, 34) and threshold == Q(43, 204)
assert coarse == Q(5, 3) > 1 and threshold < 1
r_crit, threshold_crit, _ = epidemic_threshold(Q(181, 2))
assert r_crit == Q(91, 17) and threshold_crit == 1
B = [[-a, q0, r_crit], [xi, -b, Q(0)], [Q(0), phi, -omega]]
left = [Q(1), a / xi, r_crit / omega]
right = [b / xi, Q(1), phi / omega]
assert all(dot(row, right) == 0 for row in B)
assert all(dot(left, [B[j][i] for j in range(3)]) == 0 for i in range(3))
# n=2 and kappa=1: C/2 - C^2/(1+C^2) = C(C-1)^2/[2(1+C^2)].
for numerator in range(0, 151):
    C = Q(numerator, 31)
    excess = L2 * C - C * C / (C * C + 1)
    closed_form = C * (C - 1) ** 2 / (2 * (1 + C * C))
    assert excess == closed_form >= 0
assert L2 * Q(1) == Q(1, 2)
# Finite checks for n>2 are illustrative only; global bound is proved by calculus.
for n in range(2, 11):
    level = (n - 1) ** (1 / n)
    L = ((n - 1) ** ((n - 1) / n)) / n
    assert isclose(level ** (n - 1) / (level ** n + 1), L,
                   rel_tol=1e-12, abs_tol=1e-12)
    for j in range(1, 500):
        C = j / 101
        assert C ** (n - 1) / (C ** n + 1) <= L + 1e-12
print("VERIFY_OK")
