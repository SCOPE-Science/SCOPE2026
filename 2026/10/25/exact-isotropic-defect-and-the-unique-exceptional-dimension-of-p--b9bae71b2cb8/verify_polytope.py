#!/usr/bin/env python3
"""Independent finite-dimensional polytope integration; optional numpy/scipy."""
from itertools import product
from math import factorial
import numpy as np
from scipy.spatial import ConvexHull

for n in (3, 4, 5, 6):
    vertices = np.asarray([s for s in product((-1., 1.), repeat=n) if np.prod(s) == 1], dtype=float)
    hull = ConvexHull(vertices, qhull_options='Qx')
    sum1 = np.zeros(n)
    sum2 = np.zeros((n, n))
    total = 0.
    # The origin is strictly interior; cones from the origin over a simplicial
    # triangulation of the boundary partition the body up to measure-zero faces.
    for ids in hull.simplices:
        v = vertices[ids]
        vol = abs(np.linalg.det(v)) / factorial(n)
        if vol < 1e-12:  # Degenerate simplicial subdivision pieces
            continue
        s = v.sum(axis=0)
        sum1 += vol * s / (n+1)
        sum2 += vol * (np.outer(s, s) + v.T @ v) / ((n+1)*(n+2))
        total += vol
    mean = sum1 / total
    cov = sum2 / total - np.outer(mean, mean)
    a = 2**(n-1)/factorial(n)
    m = (n*n - n + 2)/((n+1)*(n+2))
    theoretical_volume = 2**n * (1-a)
    theoretical_lambda = (1/3-a*m)/(1-a)
    assert abs(hull.volume - theoretical_volume) < 1e-9
    assert abs(total - theoretical_volume) < 1e-9
    assert np.max(np.abs(mean)) < 5e-15
    assert np.max(np.abs(cov-theoretical_lambda*np.eye(n))) < 5e-15
    print('DIRECT_HULL_OK', n, len(vertices), len(hull.simplices))
print('QHULL_OK dimensions=3..6')
