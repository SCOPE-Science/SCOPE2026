"""Deterministic checks for the exact symmetry of a truncated Euclidean ball.

This script is diagnostic only: the universal proof is analytic.
Requires Python 3 standard library only.
"""
import math
import random


def alpha(a):
    assert -1 < a < 1
    return (a + math.sqrt((a - 1) ** 2 + 1)) / 2


def center(a):
    k = alpha(a)
    return (a - k) / (1 + k)


def ball_point(rng, dimension, a):
    t = -1 + (a + 1) * rng.random()
    v = [rng.gauss(0, 1) for _ in range(dimension - 1)]
    norm = math.sqrt(sum(x * x for x in v))
    r = math.sqrt(max(0.0, 1.0 - t * t)) * rng.random() ** (1.0 / (dimension - 1))
    return (t,) + tuple(r * x / norm for x in v)


def check_cap():
    rng = random.Random(221026)
    count = 0
    for d in (2, 3, 5, 12):
        for a in (-0.999, -0.95, -0.5, -0.1, 0.0, 0.25, 0.65, 0.95, 0.999):
            k = alpha(a)
            c = center(a)
            z = (1 + k) * c
            assert -1 < c < a
            assert 0 < k < 1
            assert abs(k * k - a * k - (1 - a) / 2) < 3e-15
            assert abs(z + k - a) < 2e-15
            assert abs((z - k * a) ** 2 + k * k * (1 - a * a) - 1) < 2e-15
            count += 5
            for _ in range(1280):
                x = ball_point(rng, d, a)
                image_t = z - k * x[0]
                image_radius_sq = image_t ** 2 + k * k * sum(t * t for t in x[1:])
                assert image_t <= a + 2e-14, (d, a, x, image_t)
                assert image_radius_sq <= 1 + 3e-14, (d, a, x, image_radius_sq)
                count += 2
            # Every larger parameter violates the necessary rim inequality
            for h in (1e-4, 1e-3, 1e-2):
                test = k + h * (1 - k)
                rim_sq = (a - (1 + a) * test) ** 2 + test * test * (1 - a * a)
                assert rim_sq > 1 + 1e-15, (a, test, rim_sq)
                count += 1
    return count


def check_paraboloid():
    rng = random.Random(190926)
    k = (math.sqrt(5) - 1) / 2
    assert abs(k * k + k - 1) < 1e-14
    count = 1
    for d in (2, 3, 8):
        for _ in range(2400):
            t = rng.random()
            vec = [rng.gauss(0, 1) for _ in range(d - 1)]
            r = math.sqrt(t) * rng.random() ** (1 / (d - 1)) / math.sqrt(sum(v * v for v in vec))
            y2 = sum((r * v) ** 2 for v in vec)
            new_t = 1 - k * t
            assert 0 <= new_t <= 1
            assert k * k * y2 <= new_t + 1e-14
            count += 2
    for a in (-0.9, -0.99, -0.999, -0.9999):
        assert 0 < alpha(a) - k < 0.5 * (a + 1)
        count += 1
    return count


def main():
    cap_checks = check_cap()
    paraboloid_checks = check_paraboloid()
    print('PASS cap algebra, contact equalities, unique-candidate feasibility samples:', cap_checks)
    print('PASS parabolic limit and inclusion samples:', paraboloid_checks)
    print('PASS total checks:', cap_checks + paraboloid_checks)
    for a in (-0.999, -0.5, 0.0, 0.5, 0.999):
        print('a=', a, 'symmetry=', f'{alpha(a):.15f}', 'center=', f'{center(a):.15f}')


if __name__ == '__main__':
    main()
