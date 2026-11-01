#!/usr/bin/env python3
"""Numerical cross-checks of the central-section law for right rectangular pyramids.

Standard library only. Finite tests corroborate, but do not replace, the proof.
"""
import math
import random


def closed_probability(a, b, h):
    assert min(a, b, h) > 0
    s = 4.0 * a * a + 4.0 * b * b + h * h
    return 4.0 / math.pi * (
        math.asin(2.0 * a / math.sqrt(s))
        + math.asin(2.0 * b / math.sqrt(s))
        + math.asin(h / math.sqrt(s))
    ) - 2.0


def independent_solid_angle(a, b, h):
    # Direct spherical-triangle formula from three extreme rays of the cone.
    l0 = math.hypot(a, b)
    l1 = math.hypot(h, 2.0 * a)
    l2 = math.hypot(h, 2.0 * b)
    num = 4.0 * a * b * h
    den = l0 * l1 * l2 + b * h * l2 + a * h * l1 + 4.0 * a * b * l0
    return 4.0 / math.pi * math.atan2(num, den)


def polygon_size_from_crossed_edges(a, b, h, nx, ny, nz):
    # Count intersections of an unoriented central plane with the eight edges.
    # Four base edges and four apex-to-base edges are counted independently.
    base = [
        (x * nx + y * ny) / 2.0 - h * nz / 4.0
        for x, y in [(a, b), (-a, b), (-a, -b), (a, -b)]
    ]
    apex = 3.0 * h * nz / 4.0
    base_crossings = sum(base[i] * base[(i + 1) % 4] < 0 for i in range(4))
    side_crossings = sum(apex * v < 0 for v in base)
    return base_crossings + side_crossings


def monte_carlo(a, b, h, count, seed):
    rng = random.Random(seed)
    five = 0
    for _ in range(count):
        nx, ny, nz = rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)
        n = polygon_size_from_crossed_edges(a, b, h, nx, ny, nz)
        assert n in (4, 5)
        five += n == 5
    return five / count


def run():
    max_p = 12.0 / math.pi * math.asin(1.0 / math.sqrt(3.0)) - 2.0
    assert abs(max_p - 0.3509593121836443) < 1e-14
    cases = [
        (1.0, 1.0, 2.0), (1.0, 2.0, 2.9),
        (1.0, 3.0, 3.7), (0.3, 1.0, 2.0),
        (2.0, 3.0, 5.0), (1.0, 1.0, 0.1),
        (1.0, 1.0, 10.0),
    ]
    max_diff = 0.0
    for j, (a, b, h) in enumerate(cases):
        p = closed_probability(a, b, h)
        q = independent_solid_angle(a, b, h)
        assert 0.0 < p <= max_p + 1e-13
        assert abs(p - q) < 3e-14, (a, b, h, p, q)
        observed = monte_carlo(a, b, h, 120000, 41701 + j)
        diff = abs(observed - p)
        max_diff = max(max_diff, diff)
        assert diff < 0.012, (a, b, h, observed, p)
        print('a,b,h=', (a, b, h), 'pred=', round(p, 9),
              'observed=', round(observed, 9), 'difference=', round(diff, 9))

    # Independent global inequality diagnostics over a fixed pseudorandom family.
    rng = random.Random(83521)
    for _ in range(4000):
        a = math.exp(rng.uniform(-4.0, 4.0))
        b = math.exp(rng.uniform(-4.0, 4.0))
        h = math.exp(rng.uniform(-4.0, 4.0))
        assert closed_probability(a, b, h) < max_p + 2e-12
        assert abs(closed_probability(a, b, h) - independent_solid_angle(a, b, h)) < 2e-12

    # Strict maximum at a square base and twice its side.
    pstar = closed_probability(1.0, 1.0, 2.0)
    for delta in (-0.25, -0.1, 0.1, 0.25):
        assert closed_probability(1.0, 1.0, 2.0 * math.exp(delta)) < pstar
        assert closed_probability(math.exp(delta), math.exp(-delta), 2.0) < pstar
    print('checks_passed= true; simulations=', len(cases) * 120000,
          '; parameter_checks= 4000; max_abs_mc_discrepancy=', max_diff,
          '; sharp_pentagon_probability=', max_p)


if __name__ == '__main__':
    run()
