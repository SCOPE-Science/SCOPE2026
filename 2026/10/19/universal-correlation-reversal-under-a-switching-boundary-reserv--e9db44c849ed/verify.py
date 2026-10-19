"""Independent exact and finite-state checks for the switching-reservoir exclusion theorem.

Requires Python 3, SymPy, and NumPy. Run: python verify.py
"""
from fractions import Fraction
from itertools import combinations

import numpy as np
import sympy as sp


def stationary(n, rate):
    """Stationary joint (configuration, bath state) law, by the full generator."""
    size = 1 << n
    q = np.zeros((2 * size, 2 * size))
    for state in range(2 * size):
        occ = state % size
        bath = state // size
        transitions = []
        if (occ & 1) == 0:
            transitions.append((bath * size + (occ | 1), 1.0))
        if bath == 0 and (occ & (1 << (n - 1))):
            transitions.append((bath * size + (occ ^ (1 << (n - 1))), 1.0))
        elif bath == 1 and not (occ & (1 << (n - 1))):
            transitions.append((bath * size + (occ | (1 << (n - 1))), 1.0))
        for site in range(n - 1):
            if ((occ >> site) & 1) != ((occ >> (site + 1)) & 1):
                transitions.append((bath * size + (occ ^ (3 << site)), 1.0))
        transitions.append(((1 - bath) * size + occ, float(rate)))
        for to, hazard in transitions:
            q[state, to] += hazard
            q[state, state] -= hazard
    matrix = q.T.copy()
    matrix[-1, :] = 1.0
    rhs = np.zeros(2 * size)
    rhs[-1] = 1.0
    pi = np.linalg.solve(matrix, rhs)
    assert abs(pi.sum() - 1) < 3e-12 and pi.min() > -3e-12
    assert np.linalg.norm(pi @ q, ord=np.inf) < 3e-11
    means = np.array([sum(pi[s] * ((s >> i) & 1) for s in range(2 * size)) for i in range(n)])
    covariance = {(i + 1, j + 1):
                  sum(pi[s] * ((s >> i) & 1) * ((s >> j) & 1)
                      for s in range(2 * size)) - means[i] * means[j]
                  for i, j in combinations(range(n), 2)}
    return means, covariance


def test_two_site_exact():
    k = sp.symbols('k', positive=True)
    u, v = sp.symbols('u v')
    mean_1, mean_2 = sp.Rational(5, 6), sp.Rational(2, 3)
    equations = [sp.Rational(1, 2) + v + k * mean_1 - (2 + 2*k) * u,
                 u + sp.Rational(1, 2) + k * mean_2 - (2 + 2*k) * v]
    solution = sp.solve(equations, (u, v))
    pair = (mean_2 + solution[u]) / 2
    covariance = sp.factor(pair - mean_1 * mean_2)
    target = (3 - 4*k - 2*k*k) / (36 * (2*k + 1) * (2*k + 3))
    assert sp.simplify(covariance - target) == 0
    roots = sp.solve(sp.together(target).as_numer_denom()[0], k)
    assert [root for root in roots if root.is_positive] == [-1 + sp.sqrt(10)/2]
    print('Two-site exact covariance and sole positive zero: OK', str(covariance))


def test_limits():
    for n in range(2, 6):
        for rate, slow in [(1e-6, True), (1e6, False)]:
            means, covariance = stationary(n, rate)
            assert max(abs(means[i-1] - (1 - i/(2*(n+1)))) for i in range(1,n+1)) < 2e-9
            for (i, j), actual in covariance.items():
                slow_limit = i * ((n+2)*j - 2*(n+1)) / (4*n*(n+1)**2)
                fast_limit = -i * (n+1-j) / (4*n*(n+1)**2)
                expected = slow_limit if slow else fast_limit
                assert abs(actual - expected) < 1.1e-5, (n, rate, i, j, actual, expected)
                assert actual > 0 if slow else actual < 0
    print('Full joint-generator stationary states, all pair signs and limits, n=2..5: OK')


def test_static_covariance():
    # Static SSEP moment equations: the proposed covariance is harmonic off
    # the diagonal and has a unit-gradient-square adjacent source.
    for n in range(2, 81):
        d = n * (n+1)**2
        c = lambda i,j: -i*(n+1-j)/d if 1 <= i < j <= n else 0
        for i in range(1,n):
            assert sp.Rational(c(i-1,i+1) + c(i,i+2) - 2*c(i,i+1)).limit_denominator() == sp.Rational(1,(n+1)**2)
        for i in range(1,n+1):
            for j in range(i+2,n+1):
                lap = c(i-1,j) + c(i+1,j) + c(i,j-1) + c(i,j+1) -4*c(i,j)
                assert abs(lap) < 1e-10
    print('Finite static open-chain moment equations, n=2..80: OK')


if __name__ == '__main__':
    test_two_site_exact()
    test_static_covariance()
    test_limits()
    print('ALL CHECKS PASSED')
