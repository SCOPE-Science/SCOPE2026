#!/usr/bin/env python3
"""Independent geometric and exact-arithmetic checks for the frustum mixed-volume theorem.

Requires only Python standard library for the planar checks; optional NumPy/SciPy
are used for additional 3-, 4-, and 5-dimensional convex-hull comparisons.
Run: python verify.py
"""
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def polygon_area(points):
    points = sorted(set(points))
    if len(points) < 3:
        return Q(0)
    lo, hi = [], []
    for p in points:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    hull = lo[:-1] + hi[:-1]
    return abs(sum(cross((0, 0), u, v) for u, v in zip(hull, hull[1:] + hull[:1]))) / 2


def predicted_ratio(d, a, t):
    if a == 1:
        return (1 + t) ** d
    return (2 * (1 + t) ** d - (a + t) ** d - (1 + a * t) ** d) / (1 - a ** d)


def normalized_mixed(d, a, k):
    assert 0 <= k <= d
    if k == 0 or k == d or a == 1:
        return Q(1)
    return (2 - a ** k - a ** (d - k)) / (1 - a ** d)


def exact_planar_checks():
    tested = 0
    for a in (Q(0), Q(1, 7), Q(1, 3), Q(1, 2), Q(5, 6), Q(1)):
        for shear in (Q(0), Q(2, 5)):
            for t in (Q(0), Q(1, 5), Q(3, 4), Q(1), Q(7, 3)):
                vertices = [(-Q(1), Q(0)), (Q(1), Q(0)),
                            (shear - a, Q(1)), (shear + a, Q(1))]
                direct = polygon_area([(x - t * u, y - t * v)
                                       for x, y in vertices for u, v in vertices])
                v0 = polygon_area(vertices)
                assert direct / v0 == predicted_ratio(2, a, t), (a, shear, t, direct, v0)
                tested += 1
    return tested


def exact_profile_checks():
    checked = 0
    for d in range(2, 21):
        for a in (Q(0), Q(1, 9), Q(1, 2), Q(4, 5), Q(1)):
            for k in range(1, d):
                v = normalized_mixed(d, a, k)
                assert Q(1) <= v <= Q(2)
                assert v == normalized_mixed(d, a, d-k)
                if a == 0: assert v == 2
                if a == 1: assert v == 1
                if Q(0) < a < Q(1):
                    assert Q(1) < v < Q(2)
                checked += 1
            if Q(0) < a < Q(1):
                for k in range(1, d-1):
                    v1, v2 = normalized_mixed(d, a, k), normalized_mixed(d, a, k+1)
                    sign = (d - 1) - 2*k
                    assert (v2 > v1) == (sign > 0)
                    assert (v2 == v1) == (sign == 0)
        for k in range(1, d):
            seq = [normalized_mixed(d, a, k) for a in
                   (Q(0), Q(1, 9), Q(1, 2), Q(4, 5), Q(1))]
            assert all(x > y for x,y in zip(seq,seq[1:])), (d,k,seq)
    return checked


def independent_hulls():
    try:
        import numpy as np
        from scipy.spatial import ConvexHull
    except ImportError:
        return 'scipy-unavailable'
    tested = 0
    for d in (3, 4, 5):
        m = d-1
        # Crosspolytope base: polytope of the L1 norm in dimension m.
        base = []
        for i in range(m):
            for s in (-1., 1.):
                u = np.zeros(m)
                u[i] = s
                base.append(u)
        for a in (0.2,0.5,0.85):
            for t in (0.2,0.7,1.25):
                bot = [np.r_[u,0.] for u in base]
                top = [np.r_[a*u,1.] for u in base]
                vertices = np.array(bot+top)
                original = ConvexHull(vertices).volume
                minkowski = np.array([u-t*v for u in vertices for v in vertices])
                direct = ConvexHull(minkowski).volume/original
                assert abs(direct-float(predicted_ratio(d,a,t))) < 5e-8 * max(1,direct), (d,a,t,direct)
                tested+=1
    return tested


def main():
    a=exact_planar_checks()
    b=exact_profile_checks()
    c=independent_hulls()
    print(f'FRUSTUM_EXACT_OK planar_hulls={a} rational_profiles={b} independent_high_dim_hulls={c}')

if __name__ == '__main__':
    main()
