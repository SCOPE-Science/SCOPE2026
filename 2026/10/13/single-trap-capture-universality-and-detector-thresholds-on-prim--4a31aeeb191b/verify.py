"""Finite cross-checks for detector ranks of four-regular prime cycles.

Requires numpy and scipy. Analytic statements in RESULT.md do not rely on
finite-precision eigenvalue clustering or the finite sample of detector sets.
"""
from itertools import combinations
import math
import numpy as np
from scipy.linalg import eigvalsh


def adjacency(p, m):
    a = np.zeros((p, p), dtype=float)
    for x in range(p):
        for s in (1, -1, m, -m):
            a[x, (x+s)%p] = 1.0
    return a


def expected(p, m, r):
    degenerate = (m*m + 1) % p == 0
    classes = (p-1)//(4 if degenerate else 2)
    degree = 4 if degenerate else 2
    return 1 + classes * min(r, degree)


def spectral_rank(p, m, sites):
    w, u = np.linalg.eigh(adjacency(p, m))
    group_indices = []
    group = [0]
    for j in range(1, p):
        if abs(w[j] - w[j-1]) < 2.e-8:
            group.append(j)
        else:
            group_indices.append(group)
            group = [j]
    group_indices.append(group)
    rank = 0
    for group in group_indices:
        s = np.linalg.svd(u[np.ix_(sites, group)], compute_uv=False)
        rank += int(sum(v > 1.e-8 for v in s))
    return rank


def check():
    count = 0
    cases = [(p, m) for p in (5, 7, 11, 13, 17, 19, 29, 37)
             for m in range(2, (p-1)//2+1)]
    for p, m in cases:
        a = adjacency(p, m)
        assert np.allclose(a, a.T)
        assert np.all(np.sum(a, axis=1)==4)
        for r in range(1, min(5, p)+1):
            probes = [tuple(range(r)),tuple((2*j)%p for j in range(r))]
            if r <= p-2:
                probes += [tuple(sorted(x)) for x in list(combinations(range(p), r))[-2:]]
            for sites in set(probes):
                assert len(set(sites))==r
                actual = spectral_rank(p, m, sites)
                formula = expected(p, m, r)
                assert actual == formula, (p, m, sites, actual, formula)
                count += 1
    # Independently reconstruct the one-trap absorbing projector and check
    # the predicted identical capture probabilities at every other site.
    localization_count = 0
    for p, m in cases:
        w, u = np.linalg.eigh(adjacency(p, m))
        starts = [0]
        bright = np.zeros((p, p), dtype=float)
        for j in range(p):
            if j == p-1 or abs(w[j+1]-w[j]) > 2.e-8:
                v = u[:,starts[0]:j+1]
                b = v @ v[0, :]
                b = b / np.linalg.norm(b)
                bright += np.outer(b, b)
                starts = [j+1]
        d = 4 if (m*m + 1)%p == 0 else 2
        assert abs(bright[0, 0] - 1) < 1.e-8
        assert np.max(np.abs(np.diag(bright)[1:] - 1/d)) < 1.e-8
        localization_count += p-1
    # Independent dissipative-generator test on the most revealing resonance.
    p, m = 13, 5
    for sites in [(0,), (0,1), (0,1,4), (0,1,3,7)]:
        h = adjacency(p, m).astype(complex)
        for j, v in enumerate(sites):
            h[v,v] = -0.5j * (0.6 + 0.2*j)
        vals = np.linalg.eigvals(h)
        n_dark = sum(abs(v.imag) < 1.e-9 for v in vals)
        assert n_dark == p - expected(p,m,len(sites)), (sites, n_dark)
    print(f'VERIFY_OK graph_detector_cases={count} prime_step_models={len(cases)} sitewise_capture={localization_count} loss_eigenspectrum=4')


if __name__ == '__main__':
    check()
