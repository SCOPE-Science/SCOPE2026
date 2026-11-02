"""Independent finite checks for exact graph-heat Wasserstein amplification.

Requires Python 3, NumPy, SciPy. Run: python CHECK.py
Checks are supplementary examples and do not certify the infinite family.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog, minimize_scalar
from scipy.sparse.csgraph import shortest_path


def graph(r, m):
    n = 1 + r*m
    adjacency = np.zeros((n, n), dtype=float)
    for j in range(r):
        group = [0] + list(range(1+j*m, 1+(j+1)*m))
        for a in group:
            for b in group:
                if a != b:
                    adjacency[a, b] = 1.0
    laplacian = np.diag(adjacency.sum(axis=1)) - adjacency
    distances = shortest_path(
        np.where(adjacency > 0, 1.0, np.inf), directed=False)
    np.fill_diagonal(distances, 0.0)
    return adjacency, laplacian, distances


def transport(mu, nu, d):
    n = len(mu)
    rows = np.zeros((2*n, n*n))
    for i in range(n):
        for j in range(n):
            rows[i, i*n+j] = 1
            rows[n+j, i*n+j] = 1
    sol = linprog(d.reshape(-1), A_eq=rows, b_eq=np.r_[mu, nu],
                  bounds=(0, None), method='highs')
    assert sol.success, sol.message
    return sol.fun


def coefficient(r, m, t):
    return 2*(r-1)/r*math.exp(-t) - (r-2)/r*math.exp(-(r*m+1)*t)


def peak(r, m):
    if r == 2 or (r, m) == (3, 1):
        return 0.0, 1.0
    ratio = (r-2)*(r*m+1) / (2*(r-1))
    tp = math.log(ratio)/(r*m)
    cp = 2*(r-1)*m/(r*m+1)*ratio**(-1/(r*m))
    return tp, cp


def main():
    checked_edges = 0
    checked_pairs = 0
    for r in range(2, 7):
        for m in range(1, 6):
            adj, L, d = graph(r, m)
            for t in (0.0, .01, .1, .3, 1.0, 3.0):
                P = expm(-t*L)
                assert np.max(abs(P.sum(axis=1)-1)) < 1e-12
                for a, b in ((0, 1), (1, 2)) if m >= 2 else ((0, 1),):
                    found = transport(P[a], P[b], d)
                    expected = coefficient(r, m, t) if a == 0 else math.exp(-(m+1)*t)
                    assert abs(found-expected) < 3e-8, (r, m, t, found, expected)
                    checked_edges += 1
                if r <= 4 and m <= 3:
                    for a in range(len(P)):
                        for b in range(a+1, len(P)):
                            value = transport(P[a], P[b], d)
                            assert value <= d[a, b]*coefficient(r, m, t)+1e-8
                            checked_pairs += 1
    rng = np.random.default_rng(732184)
    checked_distributions = 0
    for r, m in ((2, 4), (3, 2), (4, 1), (4, 3)):
        _, L, d = graph(r, m)
        for t in (0.03, .1, .3):
            P = expm(-t*L)
            for _ in range(12):
                mu, nu = rng.dirichlet(np.ones(len(P)), size=2)
                before = transport(mu, nu, d)
                after = transport(mu@P, nu@P, d)
                assert after <= coefficient(r, m, t)*before+2e-8
                checked_distributions += 1
    checked_peaks = 0
    for r in range(2, 10):
        for m in range(1, 10):
            tp, cp = peak(r, m)
            if tp > 0:
                sol = minimize_scalar(lambda t: -coefficient(r, m, t),
                                      bounds=(0, 2.0), method='bounded',
                                      options={'xatol': 1e-12})
                assert abs(sol.x-tp) < 5e-6
                assert abs(-sol.fun-cp) < 1e-8
            else:
                assert coefficient(r, m, .01) < 1
            checked_peaks += 1
    print('PASS', checked_edges, 'edge/time LP comparisons;',
          checked_pairs, 'global Dirac pair bounds;',
          checked_distributions, 'random probability-pair checks;',
          checked_peaks, 'peak classifications')


if __name__ == '__main__':
    main()
