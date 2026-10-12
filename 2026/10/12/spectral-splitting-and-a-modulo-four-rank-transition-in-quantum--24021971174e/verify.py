"""Reproduce the finite corroborative checks for sunlet quantum mixing.

Requires Python 3 and numpy. Infinite assertions are proved in RESULT.md.
The finite cases below are not a proof of statements for all n.
"""
from fractions import Fraction as F
import numpy as np


def exact_fourier(n, squares):
    """Schur-square Fourier coefficients, using exact squared eigenvalues."""
    m = n // 2
    assert not n % 2 and len(squares) == m + 1
    R = [F(0) for _ in range(n)]
    S = [F(0) for _ in range(n)]
    for j, lsq in enumerate(squares):
        weight = F(lsq, lsq + 4)
        modes = {0: F(1, n)} if j in (0, m) else {0: F(2, n)}
        if 0 < j < m:
            for k in (2*j % n, (-2*j) % n):
                modes[k] = modes.get(k, F(0)) + F(1, n)
        for k, coeff in modes.items():
            R[k] += coeff
            S[k] += coeff * weight
    return R, S


def average_mix(A):
    values, basis = np.linalg.eigh(A)
    groups = []
    for i, value in enumerate(values):
        if not groups or abs(value - values[groups[-1][0]]) > 1e-8:
            groups.append([i])
        else:
            groups[-1].append(i)
    result = np.zeros_like(A, dtype=float)
    for group in groups:
        projector = basis[:, group] @ basis[:, group].T
        result += projector * projector
    return result


def check_numeric(n):
    A = np.zeros((n, n))
    for u in range(n):
        v = (u + 1) % n
        A[u, v] = A[v, u] = 1.0
    H = np.block([[A, np.eye(n)], [np.eye(n), np.zeros((n, n))]])
    R = average_mix(A)
    actual = average_mix(H)
    vals, basis = np.linalg.eigh(A)
    groups = []
    for i, x in enumerate(vals):
        if not groups or abs(x - vals[groups[-1][0]]) > 1e-8:
            groups.append([i])
        else:
            groups[-1].append(i)
    S = np.zeros((n, n))
    for g in groups:
        P = basis[:, g] @ basis[:, g].T
        lam = vals[g[0]]
        S += (lam * lam / (lam * lam + 4)) * (P * P)
    prediction = np.block([[(R + S)/2, (R - S)/2],
                           [(R - S)/2, (R + S)/2]])
    error = np.max(np.abs(prediction - actual))
    assert error < 2e-10, (n, error)
    rank = np.linalg.matrix_rank(actual, tol=2e-8)
    expected = 2*n if n % 2 else (n-1 if n % 4 == 0 else n)
    assert rank == expected, (n, rank, expected)
    return error


def main():
    exact_cases = {
        4: [4, 0, 4],
        6: [4, 1, 1, 4],
        8: [4, 2, 0, 2, 4],
        12: [4, 3, 1, 0, 1, 3, 4],
    }
    for n, squares in exact_cases.items():
        R, S = exact_fourier(n, squares)
        assert R[0] == 1
        assert all(R[k] == F(2, n) for k in range(2, n, 2))
        assert all(R[k] == 0 for k in range(1, n, 2))
        assert S[0] > 0
        for k in range(1, n):
            expected = (F(0) if k % 2 else F(2, n) * F(squares[k//2], squares[k//2] + 4))
            assert S[k] == expected, (n, k, S[k], expected)
        rank = sum(v != 0 for v in R) + sum(v != 0 for v in S)
        assert rank == (n-1 if n % 4 == 0 else n)
    errors = [check_numeric(n) for n in range(3, 25)]
    print('VERIFY_OK exact_cycle_orders=4,6,8,12 independent_matrix_orders=3..24 '
          f'fourier_modes=30 max_matrix_error={max(errors):.3e} '
          'mod4_boundary_8=7/16')


if __name__ == '__main__':
    main()
