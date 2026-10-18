"""Numerical cross-checks for the determinant and sharp stability envelope.

Requires NumPy and SciPy. The all-dimensional argument is analytical;
these calculations test representative finite configurations, not prove it.
"""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull


def data(points):
    d = len(points) // 2
    pair_differences = points[::2] - points[1::2]
    a = pair_differences.T / 2
    singular = np.linalg.svd(a, compute_uv=False)
    distance_squared = 4 * (d - singular.sum())
    volume_formula = 2**d * abs(np.linalg.det(a)) / math.factorial(d)
    envelope = 2**d / math.factorial(d) * (1 - distance_squared / (4*d))**d
    return distance_squared, volume_formula, envelope, singular


def equal_singular_configuration(d, s):
    pts = []
    for i in range(d):
        e = np.eye(d)[i]
        adjacent = np.eye(d)[(i+1) % d]
        midpoint = math.sqrt(1-s*s) * adjacent
        pts.extend([midpoint+s*e, midpoint-s*e])
    return np.array(pts)


def check():
    rng = np.random.default_rng(314159)
    for d in range(2,7):
        basis = np.eye(d)
        base = np.array([sign*basis[i] for i in range(d) for sign in (1,-1)])
        for step in [0.01, 0.04]:
            pts = base + step * rng.normal(size=base.shape)
            pts /= np.linalg.norm(pts,axis=1)[:,None]
            D2, determinant_volume, bound, singular = data(pts)
            independent_volume = ConvexHull(pts).volume
            assert abs(independent_volume-determinant_volume)<1e-9
            assert determinant_volume<=bound+1e-11
            assert D2>=-1e-11
        for s in [0.99, 0.999]:
            pts = equal_singular_configuration(d,s)
            D2,determinant_volume,bound,singular = data(pts)
            independent_volume = ConvexHull(pts).volume
            assert np.allclose(np.linalg.norm(pts,axis=1),1)
            assert np.allclose(singular, np.full(d,s),atol=1e-12)
            assert abs(D2-4*d*(1-s))<1e-11
            assert abs(independent_volume-determinant_volume)<1e-9
            assert abs(determinant_volume-bound)<1e-11
        print(f'd={d}: perturbed and equality cases confirmed')
    print('PASS: independent hull volumes, sharp envelope and equality examples')

if __name__ == '__main__':
    check()
