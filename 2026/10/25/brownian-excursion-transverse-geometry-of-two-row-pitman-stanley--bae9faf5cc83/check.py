"""Finite and stochastic checks for the two-row polytope extrusion limit.

Requirements: Python 3.10+, numpy, scipy.
Usage: python check.py
"""
import itertools
import math
from fractions import Fraction

import numpy as np
from scipy.spatial import ConvexHull


def catalan(m):
    return math.comb(2*m, m) // (m + 1)


def vertices(m):
    # All two-row order-polytope 0/1 vertices, in x coordinates.
    out = []
    for u in range(m + 1):
        for v in range(u, m + 1):
            a = np.array([int(j < u) for j in range(m)], dtype=float)
            b = np.array([int(j < v) for j in range(m)], dtype=float)
            out.append(np.stack((a, b - a), axis=0).ravel())
    return np.array(out)


def constraints(x):
    a, c = np.asarray(x).reshape(2, -1)
    b = a + c
    return min(a.min(), c.min(), 1-a.max(), 1-b.max(),
               *np.diff(a)*(-1), *np.diff(b)*(-1)) >= -1e-10


def enum_rank_gaps(m):
    for ups in itertools.combinations(range(1, 2*m+1), m):
        up = set(ups)
        h = 0
        valid = True
        downs = []
        for r in range(1, 2*m + 1):
            if r in up:
                h += 1
            else:
                h -= 1
                downs.append(r)
            if h < 0:
                valid = False
                break
        if valid:
            yield [b-a for a, b in zip(ups, downs)]


def moment_exact(m):
    s = 0
    count = 0
    for gaps in enum_rank_gaps(m):
        count += 1
        s += sum(d*(d+1) for d in gaps)
    assert count == catalan(m)
    return Fraction(s, count*(2*m+1)*(2*m+2))


def sample_dyck_ranks(m, rng):
    u = d = m
    h = 0
    rank_a, rank_b = [], []
    for rank in range(1, 2*m+1):
        p_up = u*(h+2)/((h+1)*(u+d)) if u > 0 else 0.
        if rng.random() < p_up:
            rank_a.append(rank)
            u -= 1
            h += 1
        else:
            rank_b.append(rank)
            d -= 1
            h -= 1
    assert u == d == h == 0
    return np.asarray(rank_a)-1, np.asarray(rank_b)-1


def sample_uniform_point(m, rng):
    r_a, r_b = sample_dyck_ranks(m, rng)
    order = np.sort(rng.random(2*m))
    a = order[r_a]
    b = order[r_b]
    # Convert from ascending tableau order to decreasing column order.
    return np.stack((a[::-1], (b-a)[::-1]), axis=0)


def main():
    rng = np.random.default_rng(20261021)
    for m in range(1, 5):
        vv = vertices(m)
        assert all(constraints(v) for v in vv)
        got = ConvexHull(vv, qhull_options='Qx').volume
        expected = catalan(m)/math.factorial(2*m)
        assert abs(got-expected) < 5e-12
        print(f'volume m={m}: vertices={len(vv)} volume={got:.13g} exact={expected:.13g}')
    for m in range(1, 9):
        qmean = moment_exact(m)
        print(f'exact mean transverse squared radius m={m}: {qmean}')
    for m, size in [(40, 300), (120, 500), (350, 550)]:
        q = []
        for _ in range(size):
            x = sample_uniform_point(m, rng)
            assert constraints(x)
            q.append(np.sum(x[1]**2))
        ave = float(np.mean(q))
        var = float(np.var(q))
        print(f'samples m={m}: N={size}, mean={ave:.5f}, variance={var:.5f}; limits 1 and 4/15')
        assert 0.35 < ave < 1.30
        assert 0.05 < var < 0.60
    print('CHECKS PASSED; asymptotic limit is supplied by analytic proof, not these experiments.')


if __name__ == '__main__':
    main()
