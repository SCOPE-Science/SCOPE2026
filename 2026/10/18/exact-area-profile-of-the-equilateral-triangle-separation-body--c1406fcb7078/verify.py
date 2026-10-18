#!/usr/bin/env python3
"""Independent numerical checks of the equilateral-triangle separation-body area.

Only Python's standard library is needed.  This computes convex hull perimeters
from the vertices, without using the ellipse decomposition in its area integral.
"""
import math

H = 1.0 / math.sqrt(3.0)
TRIANGLE = ((0.0, 2.0 * H), (-1.0, -H), (1.0, -H))


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull(points):
    ps = sorted(set(points))
    low = []
    for p in ps:
        while len(low) >= 2 and cross(low[-2], low[-1], p) <= 0:
            low.pop()
        low.append(p)
    up = []
    for p in reversed(ps):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return low[:-1] + up[:-1]


def perimeter(points):
    hs = hull(points)
    return sum(math.dist(hs[i], hs[(i + 1) % len(hs)]) for i in range(len(hs)))


def predicted_area(q):
    if q < 0:
        raise ValueError('Nonnegative parameter required')
    if q == 0:
        return math.sqrt(3.0)
    t = q * (q + 4.0) / (2.0 * (q + 3.0))
    af = 1 + q / 2.0
    bf = math.sqrt(af * af - 1)
    ac = 2 + q / 2.0
    bc = math.sqrt(ac * ac - 1)
    phi = math.asin(math.sqrt(3) * t / (2 * bf))
    chi = math.asin(t / (2 * ac))
    return math.sqrt(3) + 1.5 * (af * bf * (math.pi - 2 * phi) + 2 * ac * bc * chi)


def sampled_area(q, n=720):
    # The triangle contains the origin. Its convex radial perimeter sublevel
    # set is measured from the origin by bisection in each polar direction.
    samples = []
    for j in range(n):
        theta = 2 * math.pi * j / n
        c, s = math.cos(theta), math.sin(theta)
        lo, hi = 0.0, q + 10.0
        for _ in range(52):
            mid = (lo + hi) / 2.0
            p = (mid * c, mid * s)
            if perimeter(TRIANGLE + (p,)) - 6.0 <= q:
                lo = mid
            else:
                hi = mid
        samples.append((lo + hi) / 2)
    return math.pi * sum(r * r for r in samples) / n


def check_transition(q):
    t = q * (q + 4.0) / (2.0 * (q + 3.0))
    x = (-1 - t / 2.0, -H - math.sqrt(3.0) * t / 2.0)
    excess = perimeter(TRIANGLE + (x,)) - 6
    assert abs(excess - q) < 1e-10, (q, excess)
    # Both representations of perimeter excess coincide on the edge ray.
    side_excess = t + math.dist(x, (1.0, -H)) - 2.0
    corner_excess = math.dist(x, (0.0, 2 * H)) + math.dist(x, (1.0, -H)) - 4.0
    assert abs(side_excess - q) < 1e-10
    assert abs(corner_excess - q) < 1e-10


def main():
    assert abs(perimeter(TRIANGLE) - 6) < 1e-12
    assert abs(predicted_area(0) - math.sqrt(3)) < 1e-12
    for q in (0.01, 0.1, 0.5, 1.0, 3.0, 10.0):
        check_transition(q)
        formula = predicted_area(q)
        sampled = sampled_area(q)
        error = abs(formula - sampled)
        print('q=%.3f formula=%.12f hull_integral=%.12f error=%.3g' %
              (q, formula, sampled, error))
        assert error < 0.00025, (q, error)
    print('VERIFY_OK equilateral triangle separation-body all-parameter area')


if __name__ == '__main__':
    main()
