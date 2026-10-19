#!/usr/bin/env python3
"""Finite-dimensional checks for the star-graph Haken--Strobl spectrum.

Requires numpy, scipy, and sympy. Analytical arguments are supplied separately;
these tests do not establish an all-dimension theorem.
"""
import math
import numpy as np
from scipy.optimize import linear_sum_assignment


def generator(m, J, gamma):
    n = m + 1
    H = np.zeros((n, n), dtype=float)
    H[0, 1:] = J
    H[1:, 0] = J
    I = np.eye(n)
    L = -1j * (np.kron(H, I) - np.kron(I, H))
    for a in range(n):
        for b in range(n):
            if a != b:
                L[a * n + b, a * n + b] -= gamma
    return L


def factor_eigenvalues(m, J, gamma):
    roots = [0.0j]
    roots += [-gamma] * ((m - 1) * (m - 2))
    roots += [-gamma + 1j * math.sqrt(m) * J, -gamma - 1j * math.sqrt(m) * J] * (m - 1)
    Pstd = [1, 2 * gamma, gamma * gamma + m * J * J, 2 * J * J * gamma]
    Pscalar = [1, 2 * gamma, gamma * gamma + 4 * m * J * J, 2 * (m + 1) * J * J * gamma]
    roots += list(np.roots(Pstd)) * (m - 1)
    roots += list(np.roots(Pscalar))
    return np.asarray(roots, dtype=complex)


def spectral_gap(values):
    return min(-z.real for z in values if abs(z) > 1.0e-9)


def optimal(m, J):
    if m == 2:
        return (2.0 * math.sqrt(2.0) * J, math.sqrt(2.0) * J)
    return ((m - 1) / math.sqrt(m - 2) * J, J / math.sqrt(m - 2))


def symbolic_small_cases():
    import sympy as sp
    z, gamma = sp.symbols('z gamma')
    for m in (2, 3, 4):
        n = m + 1
        H = sp.zeros(n)
        for j in range(1, n):
            H[0, j] = H[j, 0] = 1
        L = sp.zeros(n * n)
        for a in range(n):
            for b in range(n):
                row = a * n + b
                for k in range(n):
                    L[row, k * n + b] -= sp.I * H[a, k]
                    L[row, a * n + k] += sp.I * H[k, b]
                if a != b:
                    L[row, row] -= gamma
        actual = L.charpoly(z).as_expr()
        expected = (z * (z + gamma)**((m - 1)*(m - 2))
            * ((z + gamma)**2 + m)**(m - 1)
            * (z*(z + gamma)**2 + m*z + 2*gamma)**(m - 1)
            * (z*(z + gamma)**2 + 4*m*z + 2*(m + 1)*gamma))
        assert sp.expand(actual - expected) == 0, m
    return 3


def main():
    symbolic_cases = symbolic_small_cases()
    comparisons = 0
    max_distance = 0.0
    max_gap_error = 0.0
    for m in range(2, 9):
        for J in (0.5, 1.1, 2.0):
            best_gamma, best_gap = optimal(m, J)
            # Spectral matching is intentionally away from the m=2 exceptional point.
            for gamma in (0.15 * J, 0.6 * J, 1.25 * J, 2.1 * J,
                          0.83 * best_gamma, 1.19 * best_gamma, 3.0 * best_gamma):
                expected = factor_eigenvalues(m, J, gamma)
                got = np.linalg.eigvals(generator(m, J, gamma))
                assert len(got) == (m + 1)**2 == len(expected)
                rows, cols = linear_sum_assignment(abs(got[:, None] - expected[None, :]))
                delta = float(np.max(abs(got[rows] - expected[cols])))
                assert delta < 1e-6, (m, J, gamma, delta)
                comparisons += len(got)
                max_distance = max(max_distance, delta)
                computed_gap = spectral_gap(got)
                assert computed_gap <= best_gap + 1.0e-7, (m,J,gamma,computed_gap,best_gap)
                assert computed_gap < best_gap - 1.0e-9, (m,J,gamma,computed_gap,best_gap)
            at_opt = np.linalg.eigvals(generator(m, J, best_gamma))
            delta_gap = abs(spectral_gap(at_opt) - best_gap)
            assert delta_gap < 2e-6, (m, J, delta_gap)
            max_gap_error = max(max_gap_error, delta_gap)
    print('PASS')
    print('Exact symbolic characteristic-polynomial cases:', symbolic_cases)
    print('Full-spectrum matched eigenvalues:', comparisons)
    print('Max eigenvalue matching discrepancy:', f'{max_distance:.3e}')
    print('Max optimum spectral-gap discrepancy:', f'{max_gap_error:.3e}')


if __name__ == '__main__':
    main()
