#!/usr/bin/env python3
"""Independent finite checks for a one-defect star Markov semigroup.

Requires numpy and scipy. Numerical checks supplement the analytic argument.
Use: python CHECKER.py
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar


def formula(r, eps, t):
    L = r + 1.0
    gap = math.sqrt(L * L - 4.0 * eps * (1.0 - eps))
    minus = (L + 2.0 * eps - gap) / 2.0
    plus = (L + 2.0 * eps + gap) / 2.0
    amp = (plus - 2.0 * eps + r) / gap
    return amp * math.exp(-minus * t) - (amp - 1.0) * math.exp(-plus * t)


def peak_formula(r, eps):
    L = r + 1.0
    gap = math.sqrt(L * L - 4.0 * eps * (1.0 - eps))
    minus = (L + 2.0 * eps - gap) / 2.0
    plus = (L + 2.0 * eps + gap) / 2.0
    amp = (plus - 2.0 * eps + r) / gap
    if r <= 2.0 * eps:
        return 0.0, 1.0
    t = math.log((amp - 1.0) * plus / (amp * minus)) / gap
    return t, formula(r, eps, t)


def direct(r, eps, t):
    # Vertex 0 is the hub, vertex 1 the slow leaf, remaining leaves fast.
    n = r + 2
    Q = np.zeros((n, n))
    for j in range(1, n):
        rate = eps if j == 1 else 1.0
        Q[0, j] = rate
        Q[j, 0] = rate
        Q[0, 0] -= rate
        Q[j, j] -= rate
    P = expm(t * Q)
    # On a unit-edge star, W1 of two distributions is the sum of
    # absolute discrepancies of their masses at the individual leaves.
    edge_w1 = [float(np.abs(P[j, 1:] - P[0, 1:]).sum()) for j in range(1, n)]
    return edge_w1


def main():
    count = 0
    # Direct heat kernels computed independently from the formula.
    for r in (2, 3, 4, 7, 12):
        for eps in (0.001, 0.017, 0.1, 0.35, 0.7, 0.99, 1.0):
            for t in (0.0, 0.001, 0.02, 0.1, 0.3, 1.0, 2.0, 5.0, 15.0):
                all_edges = direct(r, eps, t)
                target = formula(r, eps, t)
                assert abs(all_edges[0] - target) < 5e-12, (r, eps, t, all_edges[0], target)
                count += 1
                assert all_edges[0] >= max(all_edges[1:]) - 5e-12
                count += 1
    # Exact peak location compared against independent scalar optimization.
    for r in (2, 3, 5, 10):
        for eps in (0.0001, 0.01, 0.2, 0.6, 0.95, 1.0):
            exact_t, exact_a = peak_formula(r, eps)
            res = minimize_scalar(lambda x: -formula(r, eps, x), bounds=(0.0, max(6., exact_t + 2.)),
                                  method='bounded', options={'xatol': 1e-12})
            candidate = max(1.0, -res.fun)
            assert abs(candidate - exact_a) < 1e-8, (r, eps, candidate, exact_a)
            count += 1
            if exact_t > 1e-5:
                assert abs(res.x - exact_t) < 3e-4
                count += 1
    # Two-term small-rate amplitude expansion and logarithmic peak-time law.
    for r in (2, 3, 5, 10):
        L = r + 1.0
        K = r * L * L / ((2 * r + 1) * (r + 2))
        b = (2 * r + 1) * (r + 2) / (L**3)
        d = -b * (1.0 + math.log(K)) - r * (r - 1) / (L**3)
        for eps in (1e-4, 1e-5):
            t, peak = peak_formula(r, eps)
            predicted = 2 - 1/L - b*eps*math.log(1/eps) + d*eps
            assert abs(peak - predicted) < 0.0000005, (r, eps, peak, predicted)
            count += 1
            assert abs(t - math.log(K/eps)/L) < 0.001
            count += 1
    print(f'PASS: {count} independent finite numerical assertions')


if __name__ == '__main__':
    main()
