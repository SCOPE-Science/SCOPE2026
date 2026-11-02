"""Independent finite checks for the weighted-wheel two-input rank formula.

The proof covers all admissible integers and positive weights; these tests
exercise exact rational matrices and separately implemented spectral ranks.
Requires Python 3 with numpy and sympy.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp


def predicted(n, d, resonant_k=None):
    q = math.gcd(d, n if n % 2 else n // 2)
    dim = n + 1 - ((q - 1) // 2 if n % 2 else q - 1)
    if resonant_k is None:
        return dim
    if n % 2 == 0 and resonant_k == n // 2:
        return dim - int(d % 2 == 0)
    special = n % 2 == 0 and (2 * resonant_k * d) % n == 0 and (resonant_k * d) % n != 0
    return dim - int(not special)


def wheel_exact(n, g):
    mat = sp.zeros(n + 1)
    for j in range(n):
        k = (j + 1) % n
        for u, v, w in ((j, k, sp.Integer(1)), (j, n, g)):
            mat[u, u] += w
            mat[v, v] += w
            mat[u, v] -= w
            mat[v, u] -= w
    return mat


def exact_krylov_rank(n, d, g):
    L = wheel_exact(n, g)
    B = sp.zeros(n + 1, 2)
    B[0, 0] = B[d, 1] = 1
    blocks = [B]
    for _ in range(n):
        blocks.append(L * blocks[-1])
    return sp.Matrix.hstack(*blocks).rank()


def numeric_spectral_rank(n, d, g):
    L = np.zeros((n + 1, n + 1), dtype=float)
    for j in range(n):
        k = (j + 1) % n
        for u, v, w in ((j, k, 1.), (j, n, g)):
            L[u, u] += w
            L[v, v] += w
            L[u, v] -= w
            L[v, u] -= w
    vals, vecs = np.linalg.eigh(L)
    rank = 0
    a = 0
    while a < n + 1:
        b = a + 1
        while b < n + 1 and abs(vals[b] - vals[a]) < 1e-7:
            b += 1
        rank += np.linalg.matrix_rank(vecs[[0, d], a:b], tol=1e-7)
        a = b
    return rank


def resonance(n, k):
    return (2 - 2 * math.cos(2 * math.pi * k / n)) / n


def main():
    checks = 0
    for n in range(3, 27):
        for d in range(1, n):
            g0 = 0.123456789
            if all(abs(g0 - resonance(n, k)) > 1e-7 for k in range(1, n // 2 + 1)):
                assert numeric_spectral_rank(n, d, g0) == predicted(n, d)
                checks += 1
            for k in range(1, n // 2 + 1):
                assert numeric_spectral_rank(n, d, resonance(n, k)) == predicted(n, d, k), (n, d, k)
                checks += 1
    # Exact rational matrices. For a rational g, determine resonances only
    # at the integer/rational cycle eigenvalues occurring in these dimensions.
    exact_cases = [(3, sp.Rational(1)), (4, sp.Rational(1, 2)),
                   (4, sp.Rational(1)), (6, sp.Rational(1, 6)),
                   (6, sp.Rational(1, 2)), (6, sp.Rational(2, 3)),
                   (8, sp.Rational(1, 4)), (8, sp.Rational(1, 2)),
                   (12, sp.Rational(1, 12)), (12, sp.Rational(1, 6)),
                   (12, sp.Rational(1, 4)), (12, sp.Rational(1, 3))]
    kcases = {(3, 1): 1, (4, sp.Rational(1, 2)): 1, (4, 1): 2,
              (6, sp.Rational(1, 6)): 1, (6, sp.Rational(1, 2)): 2,
              (6, sp.Rational(2, 3)): 3, (8, sp.Rational(1, 4)): 2,
              (8, sp.Rational(1, 2)): 4, (12, sp.Rational(1, 12)): 2,
              (12, sp.Rational(1, 6)): 3, (12, sp.Rational(1, 4)): 4,
              (12, sp.Rational(1, 3)): 6}
    for n, g in exact_cases:
        for d in range(1, n):
            assert exact_krylov_rank(n, d, g) == predicted(n, d, kcases[(n, g)]), (n, d, g)
            checks += 1
    for n in range(3, 10):
        for d in range(1, n):
            g = sp.Rational(31, 97)
            assert exact_krylov_rank(n, d, g) == predicted(n, d), (n, d, g)
            checks += 1
    print(f"PASS: {checks} individual dimension comparisons; exact rational Krylov and independent numerical eigenspace methods")


if __name__ == '__main__':
    main()
