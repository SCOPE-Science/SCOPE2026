"""Finite diagnostics for the sharp two-point circular-arc interpolation theorem.

The analytical proof in RESULT.md is needed for the assertion at every
real arc angle and every continuous function; the finite grids below are
not a substitute for those quantifiers.
"""
import cmath
import math
import random


def lebesgue_value(t, u, v):
    z, zu, zv = (cmath.exp(1j * a) for a in (t, u, v))
    return (abs(z - zv) + abs(z - zu)) / abs(zv - zu)


def exact_value(theta):
    return math.sqrt(1.0 + math.sin(theta / 2.0) ** 2)


def optimal_nodes(theta):
    a = 2.0 * math.atan(math.sin(theta / 2.0))
    return -a, a


def run():
    rng = random.Random(73819)
    count = 0
    for theta in [0.08, 0.41, 1.1, 2.3, 3.08, 3.13]:
        u, v = optimal_nodes(theta)
        opt = exact_value(theta)
        assert -theta < u < v < theta
        count += 1
        vals = [lebesgue_value(-theta + 2 * theta * j / 4096, u, v)
                for j in range(4097)]
        assert abs(max(vals) - opt) < 3e-12, (theta, max(vals), opt)
        count += 1
        endpoint_value = 1.0 / math.cos(theta / 2.0)
        assert abs(lebesgue_value(0.0, -theta, theta) - endpoint_value) < 3e-12
        assert endpoint_value > opt
        count += 2
        for k in range(250):
            x, y = sorted((rng.uniform(-theta, theta), rng.uniform(-theta, theta)))
            if y - x < 1e-4:
                continue
            m = (x + y) / 2.0
            d = (y - x) / 4.0
            lower = max(1.0 / math.cos(d), math.sin(theta / 2.0) / math.sin(d))
            assert lower + 1e-12 >= opt
            assert abs(lebesgue_value(m, x, y) - 1.0 / math.cos(d)) < 3e-12 * (1 + abs(math.sin(theta / 2.0) / math.sin(d)))
            if m >= 0:
                assert abs(lebesgue_value(m - theta, x, y) -
                           math.sin(theta / 2.0) / math.sin(d)) < 3e-12 * (1 + abs(math.sin(theta / 2.0) / math.sin(d)))
            else:
                assert abs(lebesgue_value(m + theta, x, y) -
                           math.sin(theta / 2.0) / math.sin(d)) < 3e-12 * (1 + abs(math.sin(theta / 2.0) / math.sin(d)))
            count += 3
        # On the optimal separation, every admissible asymmetric shift
        # has a strictly larger exterior Lebesgue value.
        span = theta - v
        for fraction in [0.1, 0.35, 0.75]:
            m = fraction * span
            x, y = u + m, v + m
            eps = min(m / 3.0, (math.pi - theta) / 3.0)
            assert lebesgue_value(m - theta - eps, x, y) > opt
            count += 1
    print('PASS: %d deterministic finite diagnostic assertions' % count)


if __name__ == '__main__':
    run()
