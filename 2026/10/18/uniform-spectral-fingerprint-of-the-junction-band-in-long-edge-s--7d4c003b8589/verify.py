"""Finite checks of the regular-parent junction-band mapping.
The infinity-uniform theorem is proved analytically in RESULT.md.
"""
import itertools
import math
import numpy as np
from scipy.optimize import brentq


def family():
    yield 'tetrahedron', 4, list(itertools.combinations(range(4), 2))
    yield 'complete-5', 5, list(itertools.combinations(range(5), 2))
    yield 'bipartite-3+3', 6, [(i, j) for i in range(3) for j in range(3, 6)]
    yield 'cube', 8, [(i, i ^ (1 << j)) for i in range(8) for j in range(3) if i < (i ^ (1 << j))]
    yield 'triangular-prism', 6, [(i, (i + 1) % 3) for i in range(3)] + [(i + 3, (i + 1) % 3 + 3) for i in range(3)] + [(i, i + 3) for i in range(3)]
    yield 'Petersen', 10, [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + [(i + 5, ((i + 2) % 5) + 5) for i in range(5)]


def adjacency(n, edges):
    a = np.zeros((n, n), dtype=float)
    for i, j in edges:
        a[i, j] = a[j, i] = 1
    return a


def inflated_adjacency(n, edges, ell):
    N = n + len(edges) * (ell - 1)
    a = np.zeros((N, N), dtype=float)
    idx = n
    for i, j in edges:
        p = i
        for k in range(ell - 1):
            a[p, idx] = a[idx, p] = 1
            p = idx
            idx += 1
        a[p, j] = a[j, p] = 1
    return a


def local_root(d, ell, mu):
    rho = math.sqrt(d - 1)
    def F(u):
        return (u*u-(d-1) + ((d-1)*u*u-1)*u**(-2*ell)
                -mu*(u*u-1)*u**(-ell))
    u = brentq(F, rho - .3, rho + .3, xtol=2e-14)
    return u+1/u


def cheby(n, z):
    if n == 0: return 1.
    if n == 1: return z
    u, v = 1., z
    for _ in range(2, n + 1):
        u, v = v, z*v-u
    return v

count = 0
for name, n, edges in family():
    a = adjacency(n, edges)
    degrees = a.sum(axis=0)
    assert len(set(degrees)) == 1 and degrees[0] >= 3
    count += 1
    d = int(degrees[0])
    parent = np.linalg.eigvalsh(a)[::-1]
    rho = math.sqrt(d-1)
    c = (d-2)**2 / (2*(d-1)**1.5)
    for ell in (8, 12, 16):
        actual = np.linalg.eigvalsh(inflated_adjacency(n, edges, ell))
        band = actual[actual > 2.0000000001][::-1]
        roots = [local_root(d, ell, x) for x in parent]
        assert len(band) == n, (name, ell, len(band), n)
        assert np.max(np.abs(band-roots)) < 2e-10, (name, ell)
        count += 2
        for mu, lam in zip(parent, roots):
            # Independent check of exact Chebyshev secular relation.
            residual = lam*cheby(ell-1,lam)-d*cheby(ell-2,lam)-mu
            assert abs(residual) < 3e-7, (name, ell, residual)
            # Uniform first-order approximation with a coarse safe numeric bound.
            error = abs(lam-(d/rho+c*mu*rho**(-ell)))
            assert error <= 500*ell*rho**(-2*ell), (name, ell, mu, error)
            count += 2
        exactwidth = roots[0]-roots[-1]
        limitingwidth = c*(d-parent[-1])*rho**(-ell)
        assert abs(exactwidth-limitingwidth) <= 1000*ell*rho**(-2*ell)
        count += 1
    print(f'{name}: d={d}, n={n}, ell=8,12,16, all checks passed')
print(f'VERIFY_OK: {count} numerical assertions in six graph families')
