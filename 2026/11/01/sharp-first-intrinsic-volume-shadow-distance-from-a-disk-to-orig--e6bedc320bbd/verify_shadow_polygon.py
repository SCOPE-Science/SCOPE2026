#!/usr/bin/env python3
"""Numerical cross-checks for optimal planar projection-shadow approximation.

This is a supplementary finite test, not a substitute for the analytic proof.
All computations use the Python standard library.
"""
import math
import random

PI = math.pi


def theta0(gap):
    return math.asin(math.sin(gap / 2) / 2)


def local_bound(gap):
    return gap - 4 * theta0(gap)


def radius(n):
    return 1 / math.cos(theta0(2 * PI / n))


def optimum(n):
    return PI - 2 * n * theta0(2 * PI / n)


def primitive(x, a, b):
    return x - a * math.sin(x) + b * math.cos(x)


def exact_local_integral(gap, a, b):
    """Integrate |1-a*cos(x)-b*sin(x)| on a centered angular cell."""
    left, right = -gap / 2, gap / 2
    boundaries = [left, right]
    magnitude = math.hypot(a, b)
    if magnitude > 1:
        shift = math.atan2(b, a)
        half = math.acos(1 / magnitude)
        for j in range(-2, 3):
            for root in (shift + half + 2 * PI * j,
                         shift - half + 2 * PI * j):
                if left < root < right:
                    boundaries.append(root)
    boundaries.sort()
    total = 0.0
    for lo, hi in zip(boundaries, boundaries[1:]):
        sign = 1 if 1 - a * math.cos((lo + hi) / 2) - b * math.sin((lo + hi) / 2) >= 0 else -1
        total += sign * (primitive(hi, a, b) - primitive(lo, a, b))
    return total


def projected_metric(vertices, samples=16384):
    """Midpoint quadrature of δ1(B,P), for polygons with origin inside."""
    step = 2 * PI / samples
    result = 0.0
    for i in range(samples):
        angle = (i + 0.5) * step
        ct, st = math.cos(angle), math.sin(angle)
        h = max(x * ct + y * st for x, y in vertices)
        result += abs(1 - h)
    return result * step / 2


def regular_vertices(n, r):
    return [(r * math.cos(2 * PI * k / n), r * math.sin(2 * PI * k / n))
            for k in range(n)]


def main():
    rng = random.Random(5172026)
    tests = 0
    # Two independent formulas: the exact signed primitive and the closed form.
    for n in range(3, 91):
        gap = 2 * PI / n
        r = radius(n)
        loss = exact_local_integral(gap, r, 0.0)
        assert abs(loss - local_bound(gap)) < 3e-12, (n, loss, local_bound(gap))
        assert abs(n * loss / 2 - optimum(n)) < 2e-11
        tests += 2

    # The angular dual certificate is tested on arbitrary cosine-sine affine pieces.
    for k in range(3000):
        gap = rng.uniform(0.0004, PI - 0.0004)
        a, b = rng.uniform(-3, 3), rng.uniform(-3, 3)
        value = exact_local_integral(gap, a, b)
        assert value >= local_bound(gap) - 5e-12, (gap, a, b, value)
        tests += 1

    # The exact lower bound, checked against independent angular quadrature
    # for irregular, origin-containing polygons.
    for n in range(3, 15):
        for rep in range(15):
            phase = rng.uniform(-PI, PI)
            rs = [rng.uniform(0.60, 1.40) for _ in range(n)]
            vertices = [
                (rs[k] * math.cos(phase + 2 * PI * k / n),
                 rs[k] * math.sin(phase + 2 * PI * k / n))
                for k in range(n)
            ]
            # Adjacent direction gaps are <= 2π/3 < π, so the origin is in the hull.
            observed = projected_metric(vertices, samples=8192)
            assert observed >= optimum(n) - 2e-7, (n, observed, optimum(n))
            tests += 1

    # Independent quadrature at the optimizer for each n; handle discontinuous
    # derivatives of |1-h| with a conservative quadrature tolerance.
    for n in range(3, 26):
        observed = projected_metric(regular_vertices(n, radius(n)), samples=65536)
        assert abs(observed - optimum(n)) < 8e-8, (n, observed, optimum(n))
        tests += 1

    # Published triangle benchmark (normalization translated to δ_1).
    r3 = radius(3)
    triangle_benchmark = (-2 * PI - 3 * math.sqrt(3) * r3 / 2 +
                          6 * math.sqrt(r3 * r3 - 1) +
                          6 * math.asin(1 / r3))
    assert abs(triangle_benchmark - optimum(3)) < 1e-12
    tests += 1

    # Strict curvature of the gap-energy g and correct finite-N ordering.
    previous = optimum(3)
    for n in range(4, 1000):
        current = optimum(n)
        assert 0 < current < previous, (n, current, previous)
        previous = current
        tests += 1
    for _ in range(1000):
        gap = rng.uniform(0.002, PI - 0.002)
        h = min(1e-3, gap / 10, (PI - gap) / 10)
        second = (local_bound(gap + h) - 2 * local_bound(gap) + local_bound(gap - h)) / (h * h)
        predicted = 3 * math.sin(gap / 2) / (8 * (1 - math.sin(gap / 2) ** 2 / 4) ** 1.5)
        assert second > 0 and abs(second - predicted) < 1e-3, (gap, second, predicted)
        tests += 1

    print('PASS:', tests, 'checks')
    for n in (3, 4, 5, 6, 8, 12, 24):
        print('N=%2d radius=%.12f delta1=%.12f' % (n, radius(n), optimum(n)))
    print('leading limit π³/8 =', PI ** 3 / 8)


if __name__ == '__main__':
    main()
