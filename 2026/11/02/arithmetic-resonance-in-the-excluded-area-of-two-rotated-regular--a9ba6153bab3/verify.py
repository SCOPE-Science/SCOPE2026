#!/usr/bin/env python3
"""Independent geometric and numerical checks of rotated regular-polygon sum areas.

Requirements: Python 3, NumPy, SciPy (for Qhull convex hull construction).
Finite checks complement but do not replace the analytic proof.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull


def polygon(n, R, angle=0.0):
    return np.array([
        (R * math.cos(angle + 2.0 * math.pi * j / n),
         R * math.sin(angle + 2.0 * math.pi * j / n))
        for j in range(n)
    ])


def independent_area(n, m, angle, R, S):
    first, second = polygon(n, R), polygon(m, S, angle)
    sums = (first[:, None, :] + second[None, :, :]).reshape((-1, 2))
    return float(ConvexHull(sums).volume)


def constants(n, m, R, S):
    g = math.gcd(n, m)
    q = n // g
    alpha = math.pi * g / (n * m)
    star = math.pi / n - (alpha if q % 2 == 0 else 0.0)
    cross = R * S * g * math.sin(math.pi / n) * math.sin(math.pi / m) / math.sin(alpha)
    base = n * R * R * math.sin(2 * math.pi / n) / 2 + m * S * S * math.sin(2 * math.pi / m) / 2
    return alpha, star, cross, base


def closed_area(n, m, angle, R, S):
    alpha, star, cross, base = constants(n, m, R, S)
    nearest = ((angle - star + alpha) % (2 * alpha)) - alpha
    return base + 2 * cross * math.cos(nearest)


def analytic_moments(n, m, R, S):
    alpha, star, cross, base = constants(n, m, R, S)
    mean = base + 2 * cross * math.sin(alpha) / alpha
    variance = 4 * cross * cross * (
        .5 + math.sin(2 * alpha) / (4 * alpha) - (math.sin(alpha) / alpha)**2
    )
    return mean, variance


def main():
    rng = np.random.default_rng(238991)
    err = 0.0
    count = 0
    for n in range(3, 21):
        for m in range(3, 21):
            for j in range(12):
                angle = float(rng.uniform(-3, 3))
                R = float(rng.uniform(.2, 4.0))
                S = float(rng.uniform(.2, 4.0))
                actual = independent_area(n, m, angle, R, S)
                predicted = closed_area(n, m, angle, R, S)
                rel = abs(actual - predicted) / max(1.0, abs(actual))
                err = max(err, rel)
                assert rel < 4e-12, (n, m, angle, actual, predicted, rel)
                count += 1
    assert count == 3888
    extremal_count = 0
    for n, m in [(3, 3), (3, 4), (4, 6), (5, 7), (8, 9), (12, 18), (20, 20)]:
        for R, S in [(1., 1.), (.73, 1.4)]:
            alpha, star, C, base = constants(n, m, R, S)
            for angle, expected in [(star, base + 2*C), (star+alpha, base+2*C*math.cos(alpha))]:
                actual = independent_area(n, m, angle, R, S)
                assert abs(actual-expected) <= 2e-11*max(1, actual)
                extremal_count += 1
    moment_count = 0
    for n, m in [(3, 3), (3, 4), (4, 6), (5, 7), (8, 9), (12, 18)]:
        alpha, star, C, base = constants(n, m, 1.2, .9)
        N = 25000
        angles = alpha*(np.arange(N)+.5)/N
        areas = base + 2*C*np.cos(angles)
        mean, var = analytic_moments(n, m, 1.2, .9)
        assert abs(areas.mean()-mean) <= 3e-7
        assert abs(areas.var()-var) <= 3e-8
        moment_count += 1
    # Fixed-orientation values from the equal-area polygon-mixture table,
    # independently calculated after normalizing each polygon to area 0.1.
    for n, m, published in [(3,3,6.0000), (3,4,4.9358),
                            (3,5,4.7862), (4,6,4.3971), (5,7,4.2308)]:
        R=math.sqrt(.2/(n*math.sin(2*math.pi/n)))
        S=math.sqrt(.2/(m*math.sin(2*math.pi/m)))
        ratio=closed_area(n,m,math.pi,R,S)/.1
        assert abs(ratio-published)<.000051, (n,m,ratio,published)
    print(f'VERIFY_OK hull={count} extrema={extremal_count} moment_profiles={moment_count} '
          f'published_table=5 max_relative_error={err:.4g}')


if __name__ == '__main__':
    main()
