#!/usr/bin/env python3
"""Finite numerical cross-checks for palindromic language Hankel operators.

The mathematical proof is analytic; these tests cover only finite blocks.
Requires NumPy. Run: python palindrome_schatten_check.py
"""
import itertools
import numpy as np


def words(q, n):
    return list(itertools.product(range(q), repeat=n))


def block(q, m, n, r):
    rows, cols = words(q, m), words(q, n)
    return np.array([
        [r ** (m + n) if u + v == (u + v)[::-1] else 0.0 for v in cols]
        for u in rows
    ], dtype=float)


def run():
    for q, r, cutoff in [(2, 0.41, 5), (3, 0.34, 4)]:
        finite_hs_sq = 0.0
        for m in range(cutoff + 1):
            for n in range(cutoff + 1):
                matrix = block(q, m, n, r)
                singular_values = np.linalg.svd(matrix, compute_uv=False)
                predicted = r ** (m + n) * q ** ((abs(m - n) + 1) // 2 / 2)
                assert len(singular_values) == q ** min(m, n)
                assert np.allclose(singular_values, predicted, rtol=1e-10, atol=1e-12), (
                    q, m, n, singular_values, predicted
                )
                finite_hs_sq += np.sum(matrix ** 2)
        full_hs_sq = (1 + 2 * q * r ** 2 + q * r ** 4) / (1 - q * r ** 4) ** 2
        assert finite_hs_sq < full_hs_sq
        print(f"q={q}, r={r}, max block length={cutoff}: "
              f"finite HS^2={finite_hs_sq:.10f}, full formula={full_hs_sq:.10f}")
    print("Finite block checks passed; they do not establish the infinite theorem.")


if __name__ == "__main__":
    run()
