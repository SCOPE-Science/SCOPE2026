#!/usr/bin/env python3
"""Numerical checks for exact symmetry-kernel areas of regular Reuleaux polygons.

The proof is analytic; discretized area integration here is only a diagnostic.
Python 3 standard library only.
"""
import math


def generator_radius(n):
    assert n >= 3 and n % 2 == 1
    return 1.0 / (2.0 * math.cos(math.pi / (2.0 * n)))


def disk_intersection_area(k, r):
    """Claimed analytic area of k unit disks at regular k-gon centers of radius r."""
    a = math.pi / k
    q = r * math.sin(a)
    return k * (a + 0.5 * r * r * math.sin(2 * a)
                - q * math.sqrt(1 - q * q) - math.asin(q))


def brute_area_disk_intersection(centers, directions=8192):
    """Integrate ray/disk inequalities, without selecting a nearest opposite center."""
    norm2 = [x*x + y*y for x, y in centers]
    total = 0.0
    for i in range(directions):
        angle = 2.0 * math.pi * (i + 0.5) / directions
        ux, uy = math.cos(angle), math.sin(angle)
        radius = float('inf')
        for (x, y), cc in zip(centers, norm2):
            dot = ux*x + uy*y
            radicand = 1.0 - cc + dot*dot
            assert radicand >= 0.0, 'Ray starts outside one disk'
            r = dot + math.sqrt(radicand)
            if r < radius:
                radius = r
        total += radius * radius
    return math.pi * total / directions


def centers(k, radius):
    return [(radius * math.cos(2*math.pi*j/k),
             radius * math.sin(2*math.pi*j/k)) for j in range(k)]


def main():
    for n in (3, 5, 7, 11, 21):
        r = generator_radius(n)
        a = disk_intersection_area(n, r)
        sym = disk_intersection_area(2*n, r)
        assert 0.0 < sym < a
        if n <= 11:
            for k, expected in ((n, a), (2*n, sym)):
                estimate = brute_area_disk_intersection(centers(k, r))
                assert abs(estimate - expected) < 1.5e-7, (n, k, estimate, expected)
            original = centers(n, r)
            for c in ((0.04, 0.0), (0.025, -0.015)):
                doubled = original + [(2*c[0]-x, 2*c[1]-y) for x, y in original]
                offcenter = brute_area_disk_intersection(doubled, directions=8192)
                assert offcenter < sym + 2e-7, (n, c, offcenter, sym)
        if n == 3:
            assert abs(a - (math.pi-math.sqrt(3))/2) < 5e-14
        print(f'n={n:2d}: K_area={a:.12f} kernel_area={sym:.12f} ratio={sym/a:.12f}')

    for n in (31, 51, 101):
        r = generator_radius(n)
        ratio = disk_intersection_area(2*n, r)/disk_intersection_area(n, r)
        approx = 1 - math.pi**2/(8*n*n) - 25*math.pi**4/(1536*n**4)
        assert abs(ratio-approx) < 10/n**6, (n, ratio, approx)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
