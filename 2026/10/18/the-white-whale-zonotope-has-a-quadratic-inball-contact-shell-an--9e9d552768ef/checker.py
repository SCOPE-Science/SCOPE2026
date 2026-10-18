#!/usr/bin/env python3
"""Exact finite-dimensional tests for the metric geometry of the White Whale zonotope.

Runs using Python 3 and NumPy. Finite tests are corroboration, not a proof for every dimension.
"""
import itertools
import math
import numpy as np


def binary_generators(d):
    return [tuple((mask >> i) & 1 for i in range(d))
            for mask in range(1, 1 << d)]


def primitive(n):
    ns = [int(z) for z in n]
    g = math.gcd(*ns)
    if not g:
        raise ValueError('zero normal')
    return tuple(t // g for t in ns)


def cofactor_normal(vectors):
    """Integer null vector for a (d-1) by d binary matrix (independent rows)."""
    a = np.asarray(vectors, dtype=np.int64)
    d = a.shape[1]
    coeff = [int(round(np.linalg.det(np.delete(a, j, axis=1)))) * (-1) ** j
             for j in range(d)]
    if any(coeff):
        return primitive(coeff)
    return None


def get_facet_normals(d):
    rows = binary_generators(d)
    normals = set()
    for subset in itertools.combinations(rows, d - 1):
        v = cofactor_normal(subset)
        if v is not None:
            normals.add(v)
            normals.add(tuple(-t for t in v))
    return normals


def twice_support(v, rows):
    return sum(abs(sum(x * y for x, y in zip(v, row))) for row in rows)


def test_dimension(d):
    rows = binary_generators(d)
    expected = {tuple((1 if k == i else -1 if k == j else 0)
                      for k in range(d))
                for i in range(d) for j in range(d) if i != j}
    facets = get_facet_normals(d)
    touching = set()
    drift_cap = float('inf')
    for v in facets:
        v2 = sum(x * x for x in v)
        two_h = twice_support(v, rows)
        # Exact inequality h(v)^2 >= (2^(d-2)/sqrt(2))^2 * ||v||^2.
        delta = two_h * two_h - 2 ** (2 * d - 3) * v2
        assert delta >= 0, (d, v, delta)
        if delta == 0:
            touching.add(v)
        sv = abs(sum(v))
        if sv:
            cap = (two_h / 2 - 2 ** (d - 2) / math.sqrt(2) * math.sqrt(v2)) / sv
            assert cap > 1e-11, (d, v, cap)
            drift_cap = min(drift_cap, cap)
    assert touching == expected, (d, touching, expected)
    assert drift_cap > 1e-11
    print(f'd={d} generators={len(rows)} oriented_facets={len(facets)} '
          f'tangent_facets={len(touching)} diagonal_incenter_half_length={drift_cap:.12g}')
    # Each tangent facet is an anisotropically embedded (d-1)-dimensional White Whale.
    for v in touching:
        i = v.index(1)
        j = v.index(-1)
        annihilated = [r for r in rows if r[i] == r[j]]
        assert len(annihilated) == 2 ** (d - 1) - 1
        reduced = {tuple(r[k] for k in range(d) if k != j)
                   for r in annihilated}
        assert reduced == set(binary_generators(d - 1))


def random_stress():
    rng = np.random.default_rng(20261014)
    for d in range(2, 11):
        mat = np.asarray(binary_generators(d), dtype=np.float64)
        r = 2 ** (d - 2) / math.sqrt(2)
        for batch in range(4):
            u = rng.normal(size=(1000, d))
            u /= np.linalg.norm(u, axis=1)[:, None]
            h = np.abs(mat @ u.T).sum(axis=0) / 2
            assert np.all(h >= r * (1 - 2e-13)), (d, batch, h.min(), r)
        print(f'd={d} 4000 random unit directions: minimum observed >= proven radius')


if __name__ == '__main__':
    for d in range(2, 6):
        test_dimension(d)
    random_stress()
    print('ALL TESTS PASSED. General theorem requires the analytical proof.')
