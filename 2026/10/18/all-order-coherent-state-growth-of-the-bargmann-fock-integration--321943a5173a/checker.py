"""Finite diagnostics for the Bargmann--Fock integration resolvent.

Run: python checker.py   (requires numpy and scipy)
Finite experiments corroborate, but do not prove, the asymptotic theorem.
"""
import math
import numpy as np
from scipy.linalg import svdvals
from scipy.special import gammaln


def truncated_resolvent(t, n):
    i, j = np.indices((n, n))
    logarithm = (i - j) * math.log(t) + (gammaln(j + 1) - gammaln(i + 1)) / 2
    return np.where(i >= j, np.exp(logarithm), 0.0)


def asymptotic(t, degree):
    return math.sqrt(sum(math.factorial(k) / t ** (2 * k) for k in range(degree + 1)))


checks = 0
for t in (3.0, 3.5, 4.0, 4.5, 5.0, 6.0):
    n = int(t*t + 12*t + 35)
    R = truncated_resolvent(t, n)
    assert np.max(np.abs(R - np.eye(n) - t * np.diag(np.ones(n-1) / np.sqrt(np.arange(1, n)), -1) @ R)) < 3e-6, "resolvent identity"
    checks += 1
    ratio = float(svdvals(R, overwrite_a=True, check_finite=False)[0]) * math.exp(-t*t/2)
    assert ratio > 1
    assert abs(t*t*(ratio - 1) - .5) < .18
    checks += 2
    first = asymptotic(t, 1)
    second = asymptotic(t, 2)
    assert ratio > first - .005
    assert abs(ratio - second) < .045 / (1 + (t/3.5)**4) + .006
    checks += 2

for m in (2, 3, 4, 5, 6):
    for t in (2.0, 3.0, 4.0):
        n = int(t*t + 12*t + 35)
        R = truncated_resolvent(t, n)
        A = R * math.exp(-t*t/2)
        bound = math.sqrt(math.factorial(m)) * t**(-m) * math.sqrt(2*(1+math.pi*t))
        assert float(svdvals(A[:, m:], check_finite=False)[0]) <= bound*(1+1e-9)
        checks += 1

for s in (0.5, 1, 2, 5, 10, 30):
    n = int(s + 30 * math.sqrt(s+1)+60)
    p = np.exp(-s + np.arange(n)*np.log(s) - gammaln(np.arange(n)+1))
    assert float(np.sum(np.sqrt(p))) <= math.sqrt(2*(2+math.pi*math.sqrt(s)))
    checks += 1

print('PASS:', checks, 'finite diagnostics; not an infinite proof')
