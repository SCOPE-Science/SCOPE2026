"""Reproduce finite checks for a three-mode additive-preconditioner example.

Requires Python 3 and NumPy. Infinite-dimensional/uniform assertions rely
on the analytical proof, not on these finite tests.
"""
from fractions import Fraction as F
import math
import numpy as np

# Exact small example: the Schur complement is 7/8, and 
# necessary test-vector inequalities make any Type-III weight expansive.
e, delta = F(1, 4), F(1, 65536)
assert e * e + e * e == F(1, 8)
assert 1 - 2 * e * e == F(7, 8)
assert F(1, 16) + F(63, 64) ** 2 == F(65, 64) ** 2
assert delta <= e ** 6 / 4


def matrix(eps, d):
    A = np.array([[1.0, eps, eps * math.sqrt(d)],
                  [eps, 1.0, 0.0],
                  [eps * math.sqrt(d), 0.0, d]])
    assert np.linalg.eigvalsh(A)[0] > 0
    return A


def type3(eps, d, alpha):
    A = matrix(eps, d)
    F = np.diag([1.0, alpha, alpha / d])
    return np.eye(3) - F @ A


for eps in [1 / 16, 1 / 8, 1 / 4, 3 / 8, 0.49]:
    d = min(1 / 1024, eps ** 6 / 8)
    A = matrix(eps, d)
    assert np.linalg.norm(np.eye(3) - A, 2) < 1
    for alpha in np.geomspace(d / 20, 20, 115):
        M = type3(eps, d, alpha)
        assert np.linalg.norm(M, 2) > 1
    # A parameter that is spectrally convergent need not be 2-norm safe.
    M = type3(eps, d, d)
    assert max(abs(np.linalg.eigvals(M))) < 1

for power in [16, 20, 24, 28]:
    d = 2.0 ** -power
    eps = 1 / 4
    xs = np.geomspace(d ** 1.2, d ** 0.3, 2000)
    observed = min(np.linalg.norm(type3(eps, d, float(t)), 2) for t in xs)
    print('delta=2^(-%d), sampled minimum=%.9f, asymptotic=%.9f'
          % (power, observed, math.sqrt(1 + eps**2)))
    assert observed > 1
print('Exact rational witness and 575 safety plus 8000 asymptotic-scan checks passed.')
