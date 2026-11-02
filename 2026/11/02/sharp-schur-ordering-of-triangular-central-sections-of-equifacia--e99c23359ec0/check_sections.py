"""Reproduce diagnostic checks for Haar-central sections of equifacial tetrahedra.

All exact, dimension-independent conclusions in the accompanying proof are analytic;
finite sampling here is corroborative, not a proof of arbitrary-parameter inequalities.
"""
import math
import random

PI = math.pi


def formula(a, b, c):
    s = a * a + b * b + c * c
    return 4 / PI * sum(math.asin(v / math.sqrt(s)) for v in (a, b, c)) - 2


def crossing_formula(a, b, c):
    s = a * a + b * b + c * c
    return 4 - 2 / PI * sum(math.acos(2 * v * v / s - 1) for v in (a, b, c))


def section_indicator(a, b, c, g):
    x, y, z = (a * g[0], b * g[1], c * g[2])
    values = (x + y + z, x - y - z, -x + y - z, -x - y + z)
    positives = sum(t > 0 for t in values)
    return int(positives in (1, 3))


def half_normal_triangle_indicator(a, b, c, g):
    x, y, z = a * abs(g[0]), b * abs(g[1]), c * abs(g[2])
    return int(x < y + z and y < x + z and z < x + y)


def balance(p, i, j, fraction):
    q = list(p)
    if q[i] < q[j]:
        i, j = j, i
    delta = (q[i] - q[j]) * fraction / 2
    q[i] -= delta
    q[j] += delta
    return q


def p_probability(p):
    return 4 / PI * sum(math.asin(math.sqrt(x)) for x in p) - 2


def verify():
    random.seed(51031)
    # The two independent derivations agree for a broad deterministic sample.
    for _ in range(1000):
        a, b, c = (math.exp(random.uniform(-4, 4)) for _ in range(3))
        assert abs(formula(a, b, c) - crossing_formula(a, b, c)) < 2e-13
    print('SPHERICAL_EDGE_CROSSING_AND_ARCSINE_IDENTITIES_PASSED 1000')

    # The normal-sign criterion is pointwise equivalent to the independent
    # half-normal triangle-inequality criterion, away from measure-zero ties.
    for _ in range(12000):
        g = tuple(random.gauss(0, 1) for _ in range(3))
        a, b, c = (math.exp(random.uniform(-2, 2)) for _ in range(3))
        assert section_indicator(a, b, c, g) == half_normal_triangle_indicator(a, b, c, g)
    print('CENTRAL_SECTION_AND_HALF_NORMAL_TRIANGLE_EQUIVALENCE_PASSED 12000')

    # Robin-Hood equalization of a pair of squared axis proportions.
    for _ in range(10000):
        weights = [math.exp(random.uniform(-5, 5)) for _ in range(3)]
        s = sum(weights)
        p = [x / s for x in weights]
        i, j = random.sample(range(3), 2)
        q = balance(p, i, j, random.uniform(.001, .999))
        assert p_probability(q) > p_probability(p) - 2e-13
    maximum = p_probability([1 / 3] * 3)
    assert abs(maximum - (12 / PI * math.asin(1 / math.sqrt(3)) - 2)) < 1e-14
    print('STRICT_SCHUR_BALANCING_AND_UNIQUE_REGULAR_BENCHMARK_PASSED 10000')

    # Local second variation and the universal square-root boundary cusp.
    coefficient = 9 * math.sqrt(2) / (8 * PI)
    for d in [1e-3, 5e-4, 1e-4]:
        p = [1 / 3 + d, 1 / 3 - d, 1 / 3]
        ratio = (maximum - p_probability(p)) / (2 * d * d)
        assert abs(ratio / coefficient - 1) < 2e-5
    for q in [.15, .39, .75]:
        for eps in [1e-5, 1e-6]:
            p = [q, 1 - q - eps, eps]
            ratio = p_probability(p) / ((4 / PI) * math.sqrt(eps))
            assert abs(ratio - 1) < .012
    print('NONDEGENERATE_HESSIAN_AND_UNIVERSAL_BOUNDARY_CUSP_PASSED')

    # Direct sampling of plane normals, independent of the closed form.
    for a, b, c in [(1, 1, 1), (1, 1, .4), (2, 1, 1), (.2, .4, 1)]:
        n = 80000
        hits = 0
        for _ in range(n):
            g = (random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1))
            hits += section_indicator(a, b, c, g)
        target = formula(a, b, c)
        assert abs(hits / n - target) < .009, (a, b, c, hits / n, target)
    print('INDEPENDENT_HAAR_NORMAL_MONTE_CARLO_PASSED 4x80000')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    verify()
