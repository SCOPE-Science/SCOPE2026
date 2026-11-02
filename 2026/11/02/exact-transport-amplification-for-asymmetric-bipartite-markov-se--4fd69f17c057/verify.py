"""Reproduce finite optimal-transport checks for an asymmetric bipartite heat semigroup.

Requires Python 3, NumPy and SciPy. Run: python verify.py
The analytic statements for arbitrary sizes and times are proved separately.
"""
from itertools import combinations
from math import exp, log
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog


def distances(m, n):
    size = m+n
    d = np.full((size, size), 2.0)
    np.fill_diagonal(d, 0.0)
    d[:m, m:] = d[m:, :m] = 1.0
    return d


def wasserstein_by_duality(signed, d):
    size = len(signed)
    constraints, limits = [], []
    for i, j in combinations(range(size), 2):
        row = np.zeros(size)
        row[i] = 1.0
        row[j] = -1.0
        constraints.extend((row, -row))
        limits.extend((d[i, j], d[i, j]))
    outcome = linprog(-signed, A_ub=constraints, b_ub=limits,
                      bounds=[(0.0, 0.0)]+[(None, None)]*(size-1),
                      method='highs')
    assert outcome.success, outcome.message
    return -float(outcome.fun)


def predicted(m, n, alpha, beta, t):
    a, c = exp(-alpha*t), exp(-beta*t)
    b = a*c
    return max(2*(m-1)/m*a-(m-2)/m*b,
               2*(n-1)/n*c-(n-2)/n*b)


def sample(m, n, alpha, beta, t):
    size = m+n
    generator = np.zeros((size, size))
    for i in range(m):
        generator[i, i] = -alpha
        generator[i, m:] = alpha/n
    for i in range(m, size):
        generator[i, i] = -beta
        generator[i, :m] = beta/m
    semigroup = expm(t*generator)
    assert np.max(np.abs(semigroup.sum(axis=1)-1)) < 1e-10
    assert semigroup.min() >= -1e-12
    d = distances(m, n)
    observed = max(wasserstein_by_duality(semigroup[i]-semigroup[j], d)/d[i, j]
                   for i, j in combinations(range(size), 2))
    formula = predicted(m, n, alpha, beta, t)
    assert abs(observed-formula) < 1e-9, (m, n, alpha, beta, t, observed, formula)


def main():
    count = 0
    # Independent LPs of both same-part and cross-part transport, at varying times.
    for m, n in ((2, 2), (2, 4), (3, 3), (4, 3), (5, 4)):
        for alpha, beta in ((1.0, 1.0), (1.0, 4.0), (3.5, 0.2)):
            for t in (0.0, 0.05, 0.4, 1.6):
                sample(m, n, alpha, beta, t)
                count += 1
    m, n, alpha, beta = 4, 4, 1.0, 4.0
    p, q = 2*(m-1)/m, (m-2)/m
    t_star = log(q*(alpha+beta)/(p*alpha))/beta
    peak = predicted(m, n, alpha, beta, t_star)
    assert 1.05613408415 < peak < 1.05613408416
    assert predicted(m, n, alpha, beta, t_star-0.02) < peak
    assert predicted(m, n, alpha, beta, t_star+0.02) < peak
    # At equality in the sharp no-transient-amplification rate condition.
    assert all(predicted(4, 4, 1.0, 2.0, t) <= 1+1e-12
               for t in (0, 0.01, 0.1, 1, 10))
    assert predicted(4, 4, 1.0, 4.0, 0.01) > 1
    print(f'{count} finite-size/time LP comparisons passed; peak {peak:.11f}')


if __name__ == '__main__':
    main()
