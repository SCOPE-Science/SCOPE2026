"""Finite numerical checks for logarithmically weighted Dirichlet Rhaly matrices.

Run with Python 3 and NumPy: python verify_dirichlet_rhaly.py
No finite check substitutes for the infinite-dimensional proof.
"""
import math
import numpy as np


def matrix(size, exponent):
    n = np.arange(size, dtype=float)
    row = 1.0 / (np.sqrt(n + 1.0) * np.log(n + 2.0) ** exponent)
    col = 1.0 / np.sqrt(n + 1.0)
    return np.tril(np.outer(row, col))


def triangle_singular_formula(size):
    rank = np.arange(1, size + 1, dtype=float)
    return 1.0 / (2.0 * np.sin((2.0 * rank - 1) * math.pi / (4.0 * size + 2.0)))


def main():
    checks = 0
    for size in range(1, 29):
        block = np.tril(np.ones((size, size)))
        measured = np.linalg.svd(block, compute_uv=False)
        exact = triangle_singular_formula(size)
        assert np.allclose(measured, exact, atol=1e-12, rtol=1e-12)
        checks += size
    for exponent in (1.1, 1.5, 2.0, 2.5, 3.0):
        for size in (8, 16, 32, 64):
            A = matrix(size, exponent)
            row = np.arange(size, dtype=float)
            expected_hs_sq = np.sum(
                np.cumsum(1 / (row + 1)) / ((row + 1) * np.log(row + 2) ** (2 * exponent))
            )
            assert abs(np.linalg.norm(A, "fro") ** 2 - expected_hs_sq) < 1e-11
            checks += 1
            trace_norm = np.sum(np.linalg.svd(A, compute_uv=False))
            assert trace_norm >= abs(np.trace(A)) - 1e-10
            checks += 1
    # Actual diagonal dyadic-block singular norm comparisons, not asymptotic proofs.
    for j in range(2, 8):
        start = 2 ** j - 1
        stop = 2 ** (j + 1) - 1
        n = np.arange(start, stop, dtype=float)
        for exponent in (1.25, 2.0, 2.75):
            r = (n + 1) ** (-0.5) * np.log(n + 2) ** (-exponent)
            c = (n + 1) ** (-0.5)
            D = np.tril(np.outer(r, c))
            sval = np.linalg.svd(D, compute_uv=False)
            ref = triangle_singular_formula(2 ** j)
            lower = min(r) * min(c) * ref
            upper = max(r) * max(c) * ref
            assert np.all(sval >= lower * (1 - 1e-10))
            assert np.all(sval <= upper * (1 + 1e-10))
            checks += 2
    print(f"PASS: {checks} finite consistency checks")
    print("Analytic proof required for all infinite-dimensional and asymptotic statements.")


if __name__ == "__main__":
    main()
