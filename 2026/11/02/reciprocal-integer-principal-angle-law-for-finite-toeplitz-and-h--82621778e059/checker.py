"""Finite reproducibility tests for the Toeplitz-Hankel principal-angle theorem.
No finite computation establishes the infinite-dimensional asymptotic."""
import math
from fractions import Fraction
import numpy as np

count = 0

def check(condition, explanation):
    global count
    count += 1
    if not condition:
        raise AssertionError(explanation)


def matrix(n):
    ds = range(1 - n, n)
    ss = range(2 * n - 1)
    C = np.zeros((2 * n - 1, 2 * n - 1), dtype=float)
    for i in range(n):
        for j in range(n):
            C[i - j + n - 1, i + j] = 1.0
    ld = np.array([n - abs(d) for d in ds], dtype=float)
    ls = np.array([n - abs(s - (n - 1)) for s in ss], dtype=float)
    C = C / np.sqrt(ld[:, None] * ls[None, :])
    return C

for n in range(3, 33):
    C = matrix(n)
    # Every cell (i,j) contributes to exactly one diagonal/antidiagonal pair.
    for d in range(1 - n, n):
        for s in range(2 * n - 1):
            good = (d - s) % 2 == 0 and abs(d) <= s <= 2 * n - 2 - abs(d)
            expected = (1.0 / math.sqrt((n - abs(d)) * (n - abs(s - (n - 1))))) if good else 0
            check(abs(C[d + n - 1, s] - expected) < 1e-14, (n, d, s))
    singular = np.linalg.svd(C, compute_uv=False)
    check(abs(singular[0] - 1) < 1e-12 and abs(singular[1] - 1) < 1e-12, n)
    check(singular[2] < 1 - 1e-12, n)

# Exact finite polynomial differential-equation certificates, all rational.
for k in range(1, 14):
    F = [Fraction(0) for _ in range(k + 1)]
    F[1] = Fraction(1)
    for j in range(1, k):
        F[j + 1] = F[j] * Fraction((j - k) * (j + k), j * (j + 1))
    # Coefficient of t^j in t(1-t)F'' - tF' + k^2 F.
    for j in range(k + 1):
        one = Fraction(j * (j + 1)) * (F[j + 1] if j + 1 <= k else 0)
        two = Fraction(-j * (j - 1)) * F[j]
        three = -j * F[j]
        four = k * k * F[j]
        check(one + two + three + four == 0, (k, j))
    check(F[k] != 0, ('degree', k))

n = 220
sg = np.linalg.svd(matrix(n), compute_uv=False)
for k in range(1, 9):
    check(abs(sg[2*k - 2] - 1 / k) < 0.004, ('asymptotic', k))
    check(abs(sg[2*k - 1] - 1 / k) < 0.004, ('asymptotic', k))
check(abs(sum(sg * sg) - math.pi**2 / 3) < 0.012, 'Hilbert-Schmidt asymptotic')
print(f'passed {count} finite checks; analytic claims require their proof')
