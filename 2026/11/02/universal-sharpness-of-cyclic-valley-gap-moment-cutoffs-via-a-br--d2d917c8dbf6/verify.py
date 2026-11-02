#!/usr/bin/env python3
"""Independent finite checks for optimal circular valley-gap moment cutoffs.

Requires Python 3.9+ and NumPy for the optional quadrature check.
All permutation enumerations are exhaustive at the stated finite sizes;
the general theorem is proved analytically in RESULT.md.
"""
import itertools
import math
from fractions import Fraction as Q


def a(i):
    return Q(i * 2 ** (i + 1), math.factorial(i) * (i + 1) * (i + 2) * (i + 4))


def moments(K, gap_indices):
    """Return the exact first and second moments over all K! priorities."""
    indices = sorted(set(gap_indices))
    first = {i: 0 for i in indices}
    second = {(i, j): 0 for i in indices for j in indices if i <= j}
    count = 0
    for perm in itertools.permutations(range(K)):
        valley = [t for t in range(K)
                  if perm[t] < perm[(t-1) % K] and perm[t] < perm[(t+1) % K]]
        size = len(valley)
        gaps = [(valley[(j + 1) % size] - valley[j]) % K
                for j in range(size)] if size > 1 else []
        d = {i: gaps.count(i + 1) for i in indices}
        for i in indices:
            first[i] += d[i]
        for i, j in second:
            second[i, j] += d[i] * d[j]
        count += 1
    assert count == math.factorial(K)
    E = {i: Q(first[i], count) for i in indices}
    covariance = {(i, j): Q(second[i, j], count) - E[i] * E[j]
                  for i, j in second}
    return E, covariance


def analytic_checks():
    test_count = 0
    for i in range(1, 5):
        K = i + 3
        E, _ = moments(K, [i])
        assert E[i] == (i + 4) * a(i)
        assert E[i] - K * a(i) == a(i) > 0
        test_count += 2
        print(f'Mean minimal cycle: i={i}, K={K}, E[D]={E[i]}, anomaly={a(i)}')

    constants = { (1, 1): Q(1772, 14175),
                  (2, 2): Q(32, 405),
                  (1, 2): Q(-22, 945),
                  (1, 3): Q(-3182, 155925)}
    anomalies = {(1,1): Q(29,28350),
                 (2,2): Q(1,2025),
                 (1,2): Q(2,2835),
                 (1,3): Q(47,155925)}
    cases = {8:[1],9:[1,2],10:[1,2,3]}
    for K, ii in cases.items():
        E, cov = moments(K, ii)
        for i in ii:
            assert E[i] == K*a(i)
            test_count += 1
        for (i,j), c in constants.items():
            if i+j+6 != K:
                continue
            discrepancy = cov[i,j]/K - c
            assert discrepancy == anomalies[i,j]
            assert discrepancy > 0
            test_count += 2
            print(f'Covariance edge: (i,j)=({i},{j}), K={K}, '
                  f'Cov/K={cov[i,j]/K}, slope={c}, anomaly={discrepancy}')

    try:
        import numpy as np
        from numpy.polynomial.legendre import leggauss
    except ImportError:
        print('Numerical quadrature skipped: NumPy unavailable')
        return test_count

    nodes, weights = leggauss(200)
    nodes, weights = (nodes + 1.0)/2.0, weights/2.0
    x, y = nodes[:,None], nodes[None,:]
    roots = np.sqrt(weights)
    B = roots[:,None]*(np.minimum(x,y)-x*y)*roots[None,:]
    A = {}
    for i in (1,2,3):
        k = ((x+y)**i-np.abs(x-y)**i)/(2*math.factorial(i))
        A[i] = roots[:,None]*k*roots[None,:]
    for (i,j), exact in anomalies.items():
        numerical = float(np.trace(A[i] @ B @ A[j] @ B))
        assert abs(numerical - float(exact)) < 2e-7, (i,j,numerical,exact)
        test_count += 1
        print(f'Brownian-bridge trace: ({i},{j}) = {numerical:.12g}, exact = {exact}')
    return test_count


if __name__ == '__main__':
    total = analytic_checks()
    print(f'PASS: {total} finite equality, positivity and quadrature assertions')
