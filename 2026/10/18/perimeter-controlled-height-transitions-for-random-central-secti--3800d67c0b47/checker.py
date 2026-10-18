"""Reproducibility tests for central sections of cyclic right prisms.

Requires only Python 3.10+ standard library. Run: python checker.py
Monte Carlo checks are supplementary; the proof uses angular probability identities.
"""
import math
import random

PI = math.pi


def regular_vertices(n, radius=1.0):
    return [(radius * math.cos(2 * PI * i / n),
             radius * math.sin(2 * PI * i / n)) for i in range(n)]


def cyclic_from_gaps(gaps, radius=1.0):
    assert abs(sum(gaps) - 2 * PI) < 1e-11
    assert all(0 < d < PI for d in gaps)
    a = 0.0
    out = []
    for d in gaps:
        out.append((radius * math.cos(a), radius * math.sin(a)))
        a += d
    return out


def expectation_from_edges(points, h):
    n = len(points)
    s = 0.0
    for i, (x, y) in enumerate(points):
        radius = math.hypot(x, y)
        s += 2 * math.atan(h / radius)
        x2, y2 = points[(i + 1) % n]
        a = (x * x2 + y * y2 + h * h)
        b = math.hypot(radius, h) * math.hypot(math.hypot(x2, y2), h)
        s += 2 * math.acos(max(-1, min(1, a / b)))
    return s / PI


def expectation_cyclic_from_gaps(gaps, t):
    return 2 / PI * (len(gaps) * math.atan(t) +
                     2 * sum(math.asin(math.sin(d / 2) /
                                       math.sqrt(1 + t * t)) for d in gaps))


def cyclic_derivative_numerator(gaps, t):
    return len(gaps) - 2 * sum(math.sin(d / 2) * t /
                              math.sqrt(t * t + math.cos(d / 2) ** 2)
                              for d in gaps)


def section_edge_count(points, h, normal):
    ux, uy, uz = normal
    n = len(points)
    signs_top = []
    signs_bot = []
    for x, y in points:
        u = ux * x + uy * y
        signs_top.append(u + uz * h)
        signs_bot.append(u - uz * h)
    crossings = 0
    for i in range(n):
        j = (i + 1) % n
        crossings += (signs_top[i] * signs_bot[i] < 0)
        crossings += (signs_top[i] * signs_top[j] < 0)
        crossings += (signs_bot[i] * signs_bot[j] < 0)
    return crossings


def experiment(points, h, draws, rng):
    total = 0
    for _ in range(draws):
        normal = (rng.gauss(0, 1), rng.gauss(0, 1), rng.gauss(0, 1))
        total += section_edge_count(points, h, normal)
    return total / draws


def main():
    rng = random.Random(72918)
    checks = 0
    for n in range(3, 12):
        points = regular_vertices(n)
        gap = [2 * PI / n] * n
        for t in (0.08, 0.3, 0.9, 1.6, 8.0):
            a = expectation_from_edges(points, t)
            b = expectation_cyclic_from_gaps(gap, t)
            assert abs(a - b) < 2e-12, (n, t, a, b)
            eps = 1e-5
            d = (expectation_cyclic_from_gaps(gap, t + eps) -
                 expectation_cyclic_from_gaps(gap, t - eps)) / (2 * eps)
            theory_d = 2 / (PI * (1 + t * t)) * cyclic_derivative_numerator(gap, t)
            assert abs(d - theory_d) < 3e-9, (n, t, d, theory_d)
            checks += 2
        if n <= 5:
            s, c = math.sin(PI / n), math.cos(PI / n)
            optimum = c / math.sqrt(4 * s * s - 1)
            assert abs(cyclic_derivative_numerator(gap, optimum)) < 2e-12
            assert (expectation_cyclic_from_gaps(gap, optimum) >
                    max(expectation_cyclic_from_gaps(gap, optimum * 0.4),
                        expectation_cyclic_from_gaps(gap, optimum * 2)))
            checks += 2
        else:
            for t in (0.03, 0.2, 2.0, 50.0):
                assert cyclic_derivative_numerator(gap, t) > 0
                checks += 1
    eps = 0.03
    thin_gaps = [PI - 2 * eps, PI - 2 * eps, eps, eps, 2 * eps]
    pentagons = [(regular_vertices(5), [2 * PI / 5] * 5),
                 (cyclic_from_gaps(thin_gaps), thin_gaps)]
    for pts, gaps in pentagons:
        perimeter = sum(math.dist(pts[i], pts[(i + 1) % 5]) for i in range(5))
        regime = 1 if perimeter > 5 else -1
        assert regime * cyclic_derivative_numerator(gaps, 1e8) < 0
        # For the centered cyclic example, compare the two independent expressions.
        for t in (0.1, 1.0, 5.0, 20.0):
            assert abs(expectation_from_edges(pts, t) -
                       expectation_cyclic_from_gaps(gaps, t)) < 3e-12
            checks += 1
    # Independent random-plane intersection counts.
    configurations = [
        (regular_vertices(3), .34),
        (regular_vertices(4), .70),
        (regular_vertices(5), 1.30),
        (regular_vertices(6), 1.5),
        (regular_vertices(8), .8),
        (pentagons[1][0], 2.0),
        ([(-1., -1.), (2., -1.), (2., 1.), (0., 2.), (-1., 1.)], 0.9),
    ]
    for points, h in configurations:
        exact = expectation_from_edges(points, h)
        estimated = experiment(points, h, 110_000, rng)
        assert abs(exact - estimated) < 0.045, (len(points), h, exact, estimated)
        checks += 1
    print(f"Passed {checks} analytic, derivative, and sampling comparisons.")
    print("Regular pentagon optimum:", (3 + math.sqrt(5)) / 4)
    print("Mean section vertices at optimum:", expectation_cyclic_from_gaps(
        [2 * PI / 5] * 5, (3 + math.sqrt(5)) / 4))


if __name__ == "__main__":
    main()
