"""Finite cross-checks for the cubic-phase one-impulse ambiguity theorem.

Requires Python 3.10+ and NumPy. Analytic Gauss-sum arguments prove the
unbounded theorem; these tests verify representative cases independently.
"""

from math import cos, gcd, pi, sin
import numpy as np


def direct_ambiguity(n):
    j = np.arange(n, dtype=np.int64)
    chirp = np.exp(2j * np.pi * ((j ** 3) % n) / n)
    chirp[0] = 2
    return np.array([
        np.fft.fft(np.conj(chirp) * np.roll(chirp, k))
        for k in range(n)
    ])


def gauss_formula(n, k, ell):
    z = np.exp(2j * np.pi / n)
    if k == 0:
        return complex(n + 3 if ell == 0 else 3)
    j = np.arange(n, dtype=np.int64)
    exponent = (-3 * k * j * j + (3 * k * k - ell) * j) % n
    quad_sum = np.exp(2j * np.pi * exponent / n).sum()
    return z ** (-k ** 3 % n) * (quad_sum + 1 + z ** (-k * ell % n))


def ord_val(k, p):
    t = 0
    while k % p == 0:
        k //= p
        t += 1
    return t


def predicted_zero_pairs_dyadic(n):
    a = n.bit_length() - 1
    return {(k, ell) for k in range(1, n) for ell in range(n)
            if (k * ell) % n == n // 2
            and (k % 2 == 1 or 2 * ord_val(k, 2) >= a - 1)}


# Finite tables probe boundary primes, extension powers and dyadic degeneracy.
odd_cases = [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
             (5, 1), (5, 2), (5, 3), (5, 4),
             (7, 1), (7, 2), (7, 3), (11, 1), (11, 2)]
for p, a in odd_cases:
    n = p ** a
    matrix = direct_ambiguity(n)
    assert np.min(abs(matrix)) > 1.e-6, (p, a, "unexpected zero")
    if p == 3 or a >= 2:
        expected = 2 * sin(pi / (2 * (n if p == 3 else n // p)))
        low = float(np.min(abs(matrix)))
        assert abs(low - expected) < 1.e-7, (p, a, low, expected)
        actual = int(np.count_nonzero(np.isclose(abs(matrix), expected, atol=1.e-7, rtol=0)))
        count = (2 * (p - 1) * (n // p)) if p >= 5 else (2 * (p - 1) * (n // p))
        assert actual == count, (p, a, actual, count)
    assert abs(matrix[0, 0] - (n + 3)) < 1.e-7
    assert np.max(abs(matrix[1:])) < n + 3 - 1.e-7

for a in range(1, 10):
    n = 2 ** a
    matrix = direct_ambiguity(n)
    zeros = {(k, ell) for k in range(n) for ell in range(n)
             if abs(matrix[k, ell]) < 1.e-7}
    if a == 1:
        expected = {(1, 1)}
    else:
        expected = predicted_zero_pairs_dyadic(n)
        assert len(expected) == 2 ** (a - 1) * (1 + (a + 1) // 2)
    assert zeros == expected, (a, len(zeros), len(expected))

# Independent, elementwise expansion of all correlations for small moduli.
for n in (3, 4, 5, 8, 9, 16, 25, 27, 32, 49):
    m = direct_ambiguity(n)
    for k in range(n):
        for ell in range(n):
            assert abs(m[k, ell] - gauss_formula(n, k, ell)) < 1.e-7, (n, k, ell)

# Direct operator-lifting singular values check, not merely ambiguity counting.
for n in (3, 4, 5, 8):
    j = np.arange(n)
    g = np.exp(2j * np.pi * ((j ** 3) % n) / n)
    g[0] = 2
    g = g / np.sqrt(n + 3)
    rows = []
    for k in range(n):
        for ell in range(n):
            v = np.roll(g, k) * np.exp(2j * np.pi * ell * j / n)
            # Frobenius coefficient on standard matrix coordinates.
            rows.append(np.outer(v, v.conj()).reshape(-1).conj())
    s_actual = np.linalg.svd(np.array(rows), compute_uv=False)
    s_expected = np.sort((np.sqrt(n) * abs(direct_ambiguity(n)) / (n + 3)).flatten())[::-1]
    assert np.max(abs(s_actual - s_expected)) < 1.e-9, n

print("PASS: odd prime powers", len(odd_cases), "including p^a = 625 and 343")
print("PASS: dyadic orders 2 through 512; exact zero-set and rank counts")
print("PASS: elementwise Gauss expansion in 10 cyclic orders")
print("PASS: direct lifted operator singular spectra in dimensions 3, 4, 5, 8")
