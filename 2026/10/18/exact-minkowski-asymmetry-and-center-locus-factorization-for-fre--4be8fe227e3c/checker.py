#!/usr/bin/env python3
"""Reproducible finite polytope checks for a free-join asymmetry identity.

The universal statement is proved analytically; these checks are finite controls.
Requires numpy and scipy. Run: python checker.py
"""
from itertools import product
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog


def join_vertices(factors):
    factors = [np.asarray(f, dtype=float) for f in factors]
    dims = [f.shape[1] for f in factors]
    k = len(factors)
    D = sum(dims) + k - 1
    vertices = []
    for j, f in enumerate(factors):
        for v in f:
            x = np.zeros(D)
            x[sum(dims[:j]):sum(dims[:j+1])] = v
            if j < k - 1:
                x[sum(dims) + j] = 1.0
            vertices.append(x)
    return np.array(vertices)


def asymmetry_lp(vertices):
    """Exact-in-form facet/vertex containment LP, numerically solved."""
    vertices = np.asarray(vertices, float)
    d = vertices.shape[1]
    if d == 1:
        normals = np.array([[1.], [-1.]])
        offsets = np.array([-np.max(vertices), np.min(vertices)])
    else:
        hull = ConvexHull(vertices)
        normals, offsets = hull.equations[:, :-1], hull.equations[:, -1]
    lo = np.min(normals @ vertices.T, axis=1)
    # (s+1)c - V \subset s K; optimize with z=(s+1)c.
    # H-facets a*x <= -offset -> a*z + offset*s <= min_v a*v.
    constraints = np.column_stack([normals, offsets])
    result = linprog(np.r_[np.zeros(d), 1.], A_ub=constraints,
                     b_ub=lo, bounds=[(None, None)] * d + [(1, None)],
                     method='highs')
    if not result.success:
        raise RuntimeError(result.message)
    return result.x[-1], result.x[:d] / (result.x[-1] + 1)


segment = [[0.0], [1.0]]
triangle = [[0., 0.], [1., 0.], [0., 1.]]
square = [[0., 0.], [1., 0.], [1., 1.], [0., 1.]]
trapezoid = [[-1., -1.], [1., -1.], [0.5, 1.], [-0.5, 1.]]
# A triangular prism has a one-dimensional Minkowski-center locus.
prism = [[*v, float(t)] for v in triangle for t in [0., 1.]]
named = {'segment': segment, 'triangle': triangle, 'square': square,
         'trapezoid': trapezoid, 'triangular prism': prism}
for name, V in named.items():
    s, c = asymmetry_lp(V)
    print('FACTOR', name, 'asymmetry', format(s, '.12g'),
          'one center', np.round(c, 9).tolist())

cases = [
    ('square + square', ['square', 'square']),
    ('triangle + square', ['triangle', 'square']),
    ('trapezoid + square', ['trapezoid', 'square']),
    ('prism + square', ['triangular prism', 'square']),
    ('segment + square + triangle', ['segment', 'square', 'triangle']),
    ('three segments', ['segment', 'segment', 'segment']),
]
for label, names in cases:
    factors = [named[name] for name in names]
    V = join_vertices(factors)
    measured, c = asymmetry_lp(V)
    predicted = sum(asymmetry_lp(F)[0] for F in factors) + len(factors) - 1
    assert abs(measured - predicted) < 2e-7, (label, measured, predicted)
    print('JOIN', label, 'measured', format(measured, '.12g'),
          'predicted', format(predicted, '.12g'),
          'dimension', V.shape[1], 'vertices', len(V))


def center_feasible(V, center, h, tol=2e-8):
    V = np.asarray(V, float)
    hull = ConvexHull(V)
    transformed = (h + 1) * np.asarray(center) - V
    return np.all(transformed @ hull.equations[:, :-1].T
                  + h * hull.equations[:, -1] <= tol)

# The triangular-prism factor has an interval of optimal centers: 
# a triangle centroid, crossed with t in [1/3, 2/3].
tri_cent = np.array([1 / 3, 1 / 3])
for t in [1 / 3, 1 / 2, 2 / 3]:
    assert center_feasible(prism, list(tri_cent) + [t], 2)
assert not center_feasible(prism, list(tri_cent) + [0.2], 2)

# On freely joining a square, these endpoints map to optimal centers of
# the higher-dimensional body; an out-of-interval input is excluded.
Vj = join_vertices([prism, square])
def mapped_prism_square_center(t):
    return np.r_[0.6 * np.array([1 / 3, 1 / 3, t]),
                 0.4 * np.array([0.5, 0.5]), 0.6]
for t in [1 / 3, 1 / 2, 2 / 3]:
    assert center_feasible(Vj, mapped_prism_square_center(t), 4)
assert not center_feasible(Vj, mapped_prism_square_center(0.2), 4)
print('NONUNIQUE CENTER-LOCUS BOUNDARY CHECKS PASSED')
print('ALL FINITE JOIN CHECKS PASSED')
