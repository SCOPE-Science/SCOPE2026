#!/usr/bin/env python3
"""Independent finite geometry tests for the odd regular polygon convexification law.

Requires Python 3.10+ and shapely >= 2. No external data or network access.
"""
import math
from shapely.geometry import Polygon
from shapely.ops import unary_union


def polygon(m, scale=1.0, shift=(0.0, 0.0)):
    return Polygon([(shift[0] + scale * math.cos(2 * math.pi * k / m),
                     shift[1] + scale * math.sin(2 * math.pi * k / m))
                    for k in range(m)])


def union_of_translates(m, t):
    return unary_union([polygon(m, t,
                         (math.cos(2 * math.pi * j / m),
                          math.sin(2 * math.pi * j / m)))
                         for j in range(m)])


def close(a, b, tolerance=2e-10):
    assert math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance), (a, b)


def main():
    count = 0
    for m in (5, 7, 9, 11, 15):
        theta = math.pi / m
        c = math.cos(theta)
        cutoff = 1.0 / c
        for f in (0.0, 0.2, 0.5, 0.8, 0.9999, 1.0):
            t = 1.0 + f * (cutoff - 1.0)
            ambient = polygon(m, 1.0 + t)
            union = union_of_translates(m, t)
            missing = ambient.area - union.area
            predicted = m * (1.0 - t * c) ** 2 * math.tan(theta)
            close(missing, predicted)
            count += 1
            close(missing / ambient.area, ((cutoff - t) / (1 + t))**2)
            count += 1
        for t in (cutoff + 0.1, cutoff + 0.5):
            close(union_of_translates(m, t).area, polygon(m, 1 + t).area)
            count += 1
        # For t<1, two endpoint-anchored pieces do not cover an entire outer side.
        t = 0.7
        assert union_of_translates(m, t).area < polygon(m, 1 + t).area - 1e-5
        count += 1
    print('PASSED', count, 'numerical geometry assertions')


if __name__ == '__main__':
    main()
