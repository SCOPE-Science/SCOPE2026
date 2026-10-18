"""Reproducible numerical and exact-arithmetic checks for the Euclidean width
of uniform-matroid base polytopes (hypersimplices). Requires numpy and scipy.

Finite checks corroborate, but do not substitute for, the dimension-free proof.
"""
import itertools
import math
from fractions import Fraction

import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull


def intrinsic_width_squared(n, k):
    m = min(k, n - k)
    return min(Fraction(n, n - 1), Fraction(m * m * n, n * n // 4))


def vertex_differences(n, k):
    masks = np.array([tuple(int(i in S) for i in range(n))
                      for S in itertools.combinations(range(n), k)], dtype=float)
    diffs = np.unique((masks[:, None, :] - masks[None, :, :]).reshape(-1, n), axis=0)
    return diffs


def qhull_width_squared(n, k):
    diffs = vertex_differences(n, k)
    basis = null_space(np.ones((1, n)))
    points = diffs @ basis
    hull = ConvexHull(points)
    # Qhull outward facet equation: a.y + b <= 0, with |a| = 1.
    distances = -hull.equations[:, -1] / np.linalg.norm(hull.equations[:, :-1], axis=1)
    assert np.all(distances > 0)
    return float(np.min(distances)**2)


def compare_exhaustive_low_dims():
    num = 0
    for n in range(3, 7):
        for k in range(1, n // 2 + 1):
            target = float(intrinsic_width_squared(n, k))
            actual = qhull_width_squared(n, k)
            assert abs(actual - target) < 4e-9, (n, k, actual, target)
            num += 1
    return num


def random_direction_checks():
    rng = np.random.default_rng(123456)
    count = 0
    for n, k in [(3, 1), (4, 1), (4, 2), (5, 2), (6, 2),
                 (8, 2), (15, 2), (16, 2), (17, 2), (20, 2), (30, 3), (35, 3), (36, 3)]:
        lower = math.sqrt(float(intrinsic_width_squared(n, k)))
        for _ in range(250):
            u = rng.standard_normal(n)
            u -= np.mean(u)
            u /= np.linalg.norm(u)
            sorted_u = np.sort(u)
            width = np.sum(sorted_u[-k:]) - np.sum(sorted_u[:k])
            assert width >= lower - 3e-12, (n, k, width, lower)
            count += 1
        rcoord = math.sqrt(n / (n - 1))
        ubalanced = np.array([math.sqrt((n-n//2)/(n*(n//2)))]*(n//2) +
                             [-math.sqrt((n//2)/(n*(n-n//2)))]*(n-n//2))
        rbalanced = float(np.sum(np.sort(ubalanced)[-k:]) - np.sum(np.sort(ubalanced)[:k]))
        assert abs(min(rcoord, rbalanced) - lower) < 2e-12
    return count


def exact_transition_checks():
    checked = 0
    for n in range(3, 100):
        for k in range(1, n//2 + 1):
            x = Fraction(n, n-1)
            y = Fraction(k*k*n, n*n//4)
            if x == y:
                assert n == 4*k*k - 1, (n,k)
            if n == 4*k*k - 1:
                assert x == y
            checked += 1
    return checked


if __name__ == '__main__':
    nfac = compare_exhaustive_low_dims()
    nrand = random_direction_checks()
    nphase = exact_transition_checks()
    print(f"PASS: {nfac} independent convex-hull facet checks, "
          f"{nrand} random unit-normal support checks, "
          f"{nphase} exact rank/dimension phase checks")
