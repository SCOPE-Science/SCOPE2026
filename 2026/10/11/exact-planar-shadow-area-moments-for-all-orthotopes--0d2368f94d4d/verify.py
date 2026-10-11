"""Reproducible numerical and algebraic checks for planar shadows of orthotopes.

Requires Python 3, NumPy, and SciPy.  This is diagnostic code; the stated
all-dimensional identities are proved analytically in RESULT.md.
"""
import itertools
import math

import numpy as np
from scipy.spatial import ConvexHull


def exact_first_second(a):
    """Analytic expectation and raw second moment of projected area."""
    a = tuple(float(z) for z in a)
    d = len(a)
    assert d >= 3 and all(x > 0 for x in a)
    pair_sum = sum(a[i] * a[j] for i in range(d) for j in range(i + 1, d))
    diagonal = sum(a[i] ** 2 * a[j] ** 2 for i in range(d)
                   for j in range(i + 1, d))
    triple = sum(a[i] * a[j] * a[k] * (a[i] + a[j] + a[k])
                 for i, j, k in itertools.combinations(range(d), 3))
    quadruple = sum(math.prod(a[i] for i in Q)
                    for Q in itertools.combinations(range(d), 4))
    second = (2 * diagonal + 8 / math.pi * triple + 6 * quadruple) / (d * (d - 1))
    return pair_sum / (d - 1), second


def sample_areas(a, count, rng):
    """Sample Haar frames by vectorized Gaussian Gram-Schmidt."""
    d = len(a)
    g = rng.standard_normal((count, d))
    u = g / np.linalg.norm(g, axis=1)[:, None]
    h = rng.standard_normal((count, d))
    h -= np.sum(u * h, axis=1)[:, None] * u
    v = h / np.linalg.norm(h, axis=1)[:, None]
    area = np.zeros(count)
    minors = {}
    for i, j in itertools.combinations(range(d), 2):
        p = np.abs(u[:, i] * v[:, j] - u[:, j] * v[:, i])
        area += a[i] * a[j] * p
        minors[i, j] = p
    return area, minors


def projected_vertex_hull_area(a, rng):
    """Independent geometric check using projected vertices and a convex hull."""
    d = len(a)
    g = rng.standard_normal((d, 2))
    q, _ = np.linalg.qr(g)
    verts = np.array(list(itertools.product((-0.5, 0.5), repeat=d))) * np.array(a)
    planar = verts @ q
    hull_area = ConvexHull(planar).volume
    minors_area = sum(a[i] * a[j] * abs(np.linalg.det(q[[i, j], :]))
                      for i, j in itertools.combinations(range(d), 2))
    return hull_area, minors_area


def main():
    rng = np.random.default_rng(20261008)
    maximal_hull_error = 0.0
    for d in range(3, 8):
        a = np.array([0.65 + ((7 * i + 3) % 11) / 10.0 for i in range(d)])
        for _ in range(24):
            hull, zonotope = projected_vertex_hull_area(a, rng)
            maximal_hull_error = max(maximal_hull_error, abs(hull - zonotope))
            assert abs(hull - zonotope) <= 1e-10 * max(1, hull)
    print("CONVEX_HULL_CHECK_OK", "max_abs_error", f"{maximal_hull_error:.3e}")

    for d in (3, 4, 5, 7, 12):
        a = np.ones(d)
        expected, second = exact_first_second(a)
        target_variance = (d - 2) * (4 / math.pi - 5 / 4)
        assert abs(expected - d / 2) < 1e-12
        assert abs(second - expected ** 2 - target_variance) < 1e-11
        area, minors = sample_areas(a, 120000, rng)
        mean_error = abs(float(area.mean()) - expected)
        variance_error = abs(float(area.var()) - target_variance)
        print("CUBE", d, "mean_error", f"{mean_error:.6f}",
              "variance_error", f"{variance_error:.6f}")
        assert mean_error < 0.03
        assert variance_error < 0.015
        m = minors[0, 1]
        assert abs(float(m.mean()) - 1 / (d - 1)) < 0.015
        assert abs(float((m * m).mean()) - 2 / (d * (d - 1))) < 0.012
        assert abs(float((m * minors[0, 2]).mean()) - 4 / (math.pi * d * (d - 1))) < 0.012
        if d >= 4:
            assert abs(float((m * minors[2, 3]).mean()) - 1 / (d * (d - 1))) < 0.012

    for d in (3, 4, 6, 9):
        a = np.array([0.7 + ((2 * i + 1) % 9) / 10 for i in range(d)])
        expected, second = exact_first_second(a)
        area, _ = sample_areas(a, 120000, rng)
        print("RECTANGULAR", d, "mean_error", f"{abs(area.mean() - expected):.6f}",
              "second_moment_error", f"{abs((area ** 2).mean() - second):.6f}")
        assert abs(float(area.mean()) - expected) < 0.045
        assert abs(float((area * area).mean()) - second) < 0.25
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
