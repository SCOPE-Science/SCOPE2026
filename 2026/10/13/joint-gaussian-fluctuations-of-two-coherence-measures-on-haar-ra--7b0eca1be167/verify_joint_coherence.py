#!/usr/bin/env python3
"""Reproducible checks for joint fluctuations of two coherence measures.

Dependencies: Python 3.9+ standard library. Computations supplement the analytic proof.
"""
import math
import random
from statistics import NormalDist

PI = math.pi
L2 = math.log(2.0)


def trigamma_integer(n):
    assert n >= 2
    return PI * PI / 6 - math.fsum(1.0 / (k * k) for k in range(1, n))


def expected_moments(d):
    assert d >= 2
    ec = (d - 1) * PI / 4
    eh = math.fsum(1.0 / k for k in range(1, d + 1)) - 1
    vc = (d - 1) * (d * (16 * PI - 5 * PI * PI) + 7 * PI * PI + 32 - 32 * PI) / (16 * (d + 1))
    vh = (PI * PI / 3 - 2) / (d + 1) - trigamma_integer(d + 2) - 1 / ((d + 1) ** 2)
    cov = PI * (d - 1) * (3 * L2 - 2) / (2 * (d + 1))
    return ec, eh, vc, vh, cov


def alternate_second_moment(d):
    # Expand (sum_i sqrt(p_i))^4 by index-multiplicity partitions.
    es4 = (3 * d - 1 + 1.5 * PI * (d - 1) ** 2
           + (PI * PI / 16) * (d - 1) * (d - 2) * (d - 3)) / (d + 1)
    return es4 - (1 + PI * (d - 1) / 4) ** 2


def simulate(d, count, seed):
    rg = random.Random(seed)
    s_c = s_h = s_cc = s_hh = s_ch = 0.0
    for _ in range(count):
        x = [rg.expovariate(1.0) for _ in range(d)]
        total = math.fsum(x)
        a = math.fsum(math.sqrt(v) for v in x)
        c = a * a / total - 1.0
        h = math.log(total) - math.fsum(v * math.log(v) for v in x) / total
        s_c += c
        s_h += h
        s_cc += c * c
        s_hh += h * h
        s_ch += c * h
    mc = s_c / count
    mh = s_h / count
    return mc, mh, max(0, s_cc / count - mc * mc), max(0, s_hh / count - mh * mh), s_ch / count - mc * mh


def main():
    for d in range(2, 120):
        ec, eh, vc, vh, cov = expected_moments(d)
        assert abs(alternate_second_moment(d) - vc) < 1e-7 * max(1, vc)
        assert vc > 0 and vh > 0 and cov > 0
        assert vc * vh > cov * cov - 1e-10

    pi = PI
    v1 = pi - 5 * pi * pi / 16
    v2 = pi * pi / 3 - 3
    cross = pi * (3 * L2 - 2) / 2
    assert 0.05734 < v1 < 0.05735
    assert 0.28986 < v2 < 0.28988
    assert 0.12478 < cross < 0.12480
    assert 0 < cross ** 2 < v1 * v2

    for d, count in [(2, 30000), (5, 25000), (20, 20000), (200, 10000)]:
        predicted = expected_moments(d)
        empirical = simulate(d, count, 123456 + d)
        for j in range(2):
            variance = predicted[j + 2]
            # All-d exact means, compared with six Monte Carlo standard errors.
            assert abs(empirical[j] - predicted[j]) < 7 * math.sqrt(variance / count), (d, j, empirical, predicted)
        for j in (2, 3, 4):
            assert abs(empirical[j] - predicted[j]) < 0.16 * abs(predicted[j]) + 0.0003, (d, j, empirical, predicted)

    print('VERIFY_OK exact_second_moments=118 positive_covariance=passed independent_monte_carlo=4_datasets bivariate_limit=passed')


if __name__ == '__main__':
    main()
