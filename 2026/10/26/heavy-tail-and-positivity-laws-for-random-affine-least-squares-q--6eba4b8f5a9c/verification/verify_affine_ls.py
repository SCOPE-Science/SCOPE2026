#!/usr/bin/env python3
"""Reproducibility checks for uniform-node affine least-squares quadrature.

Only the Python standard library is needed. Numerical checks do not replace
proofs of the stated all-sample and asymptotic results.
"""
import math
import random


def quadrature_weights(nodes):
    m = len(nodes)
    assert m >= 2
    center = sum(nodes) / m
    v = [x - center for x in nodes]
    s = sum(a * a for a in v)
    assert s > 0
    return [1 / m - center * a / s for a in v]


def cond_number(nodes):
    return sum(abs(w) for w in quadrature_weights(nodes))


def check_exact_reproduction():
    rng = random.Random(51022)
    cases = 0
    for m in (2, 3, 4, 5, 7, 12):
        for _ in range(500):
            nodes = [rng.uniform(-1, 1) for __ in range(m)]
            w = quadrature_weights(nodes)
            center = sum(nodes) / m
            s = sum((x - center) ** 2 for x in nodes)
            assert abs(sum(w) - 1) < 2e-9
            assert abs(sum(x * a for x, a in zip(nodes, w))) < 2e-9
            assert abs(sum(a * a for a in w) - (1 / m + center ** 2 / s)) < 2e-8
            assert abs(cond_number(nodes) - 1) < 1e-8 or min(w) < 0
            cases += 1
    return cases


def check_three_sample_positive_probability():
    rng = random.Random(7259)
    n = 350000
    positives = 0
    for _ in range(n):
        x = [rng.uniform(-1, 1) for __ in range(3)]
        positives += min(quadrature_weights(x)) > 0
    rate = positives / n
    exact = (14 - math.pi) / 16
    assert abs(rate - exact) < 0.005, (rate, exact)
    return rate, exact


def centered_direction(theta):
    return [math.sqrt(2 / 3) * math.cos(theta + 2 * math.pi * j / 3) for j in range(3)]


def angular_moment(n=7200):
    angle_sum = 0
    for j in range(n):
        theta = 2 * math.pi * (j + .5) / n
        omega = centered_direction(theta)
        assert abs(sum(omega)) < 1e-13
        assert abs(sum(a*a for a in omega) - 1) < 1e-13
        angle_sum += sum(abs(a) for a in omega) ** 2
    return 2 * math.pi * angle_sum / n


def check_three_sample_tail_constant():
    integr = angular_moment()
    exact_integr = 8 * math.pi / 3 + 4 * math.sqrt(3)
    assert abs(integr - exact_integr) < 2e-5
    c = math.sqrt(3) * integr / 24
    expected = .5 + math.pi / (3 * math.sqrt(3))
    assert abs(c - expected) < 2e-6

    # An independent finite-threshold integration over the sample cube:
    # with t=sample mean >=0 and direction omega, q solves
    # sum(abs(1/3-q*omega_i))=u.  The radial cutoff is t/q, or the
    # nearest face of the cube, whichever is smaller. For u>=10 the
    # negative-face cube boundary is never active. The t integral is
    # alpha^2/[3(1+alpha*max_positive(omega))^2], alpha=1/q.
    n_angles = 900
    results = []
    for u in (30, 100, 300):
        total = 0.0
        for j in range(n_angles):
            omega = centered_direction(2 * math.pi * (j + .5) / n_angles)
            lo = 0.0
            hi = u * 4.0
            for _ in range(44):
                mid = (lo + hi) / 2
                if sum(abs(1 / 3 - mid * a) for a in omega) > u:
                    hi = mid
                else:
                    lo = mid
            alpha = 1 / hi
            a = max(omega)
            total += alpha ** 2 / (3 * (1 + alpha * a) ** 2)
        prob = (math.sqrt(3) / 8) * (2 * math.pi / n_angles) * total
        scaled = u*u*prob
        results.append((u, prob, scaled))
    assert 1.02 < results[0][2] < 1.05
    assert 1.07 < results[1][2] < 1.09
    assert 1.09 < results[2][2] < 1.105
    return integr, expected, results


def check_collisions():
    theta = .5
    omega = centered_direction(theta)
    t = .35
    ell = sum(abs(z) for z in omega)
    for radius in (1e-2, 1e-3, 1e-4):
        x = [t + radius * z for z in omega]
        assert abs(radius * cond_number(x) / t - ell) < radius / t + 1e-9


if __name__ == '__main__':
    count = check_exact_reproduction()
    rate, exact = check_three_sample_positive_probability()
    integral, constant, tail = check_three_sample_tail_constant()
    check_collisions()
    print(f'PASS: {count} independent sample moment/weight tests')
    print(f'PASS: positivity Monte Carlo={rate:.8f}, theorem={exact:.8f}')
    print(f'PASS: angular integral={integral:.10f}, tail constant={constant:.10f}')
    print('PASS: finite-threshold radial integrals', tail)
    print('PASS: clustered-node scaling')
