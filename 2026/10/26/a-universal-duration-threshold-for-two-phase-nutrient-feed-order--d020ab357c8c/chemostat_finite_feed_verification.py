"""Numerical checks for finite two-block Monod invasion-growth comparison.

Requires numpy, scipy, mpmath. The exact classification is proved analytically
in RESULT.md; these finite tests are diagnostic, not a proof.
"""
import math
import random

import mpmath as mp
from scipy.integrate import quad


def monod_integral(s0, feed, t, dil, k):
    e = math.exp(dil * t)
    return t - k / (dil * (k + feed)) * math.log1p(
        (k + feed) * (e - 1) / (k + s0)
    )


def gain_difference(s0, high, low, tau, dil, k):
    factor = math.exp(-dil * tau)
    high_state = high + (s0 - high) * factor
    low_state = low + (s0 - low) * factor
    return (monod_integral(s0, high, tau, dil, k)
            + monod_integral(high_state, low, tau, dil, k)
            - monod_integral(s0, low, tau, dil, k)
            - monod_integral(low_state, high, tau, dil, k))


def integral_difference(s0, high, low, tau, dil, k):
    def one_order(a, b):
        sa = a + (s0 - a) * math.exp(-dil * tau)
        def integral_phase(initial, feed):
            return quad(lambda t: (feed + (initial - feed) * math.exp(-dil*t)) /
                        (k + feed + (initial - feed) * math.exp(-dil*t)),
                        0, tau, epsabs=1e-12, epsrel=1e-12)[0]
        return integral_phase(s0, a) + integral_phase(sa, b)
    return one_order(high, low) - one_order(low, high)


def high_precision_gain(s0, high, low, tau, dil, k):
    s0, high, low, tau, dil, k = map(mp.mpf, (s0, high, low, tau, dil, k))
    def one_phase(s, c):
        return tau - k / (dil * (k + c)) * mp.log(
            ((k + c) * mp.exp(dil * tau) + s - c) / (k + s))
    factor = mp.exp(-dil*tau)
    return (one_phase(s0, high)
            + one_phase(high + (s0 - high)*factor, low)
            - one_phase(s0, low)
            - one_phase(low + (s0 - low)*factor, high))


def main():
    random.seed(20261022)
    critical = math.log(1 + math.sqrt(2))
    checked_integrals = 0
    checked_signs = 0
    for _ in range(1000):
        dil = math.exp(random.uniform(-1, 1))
        tau = random.uniform(.1, 1.6) / dil
        k = math.exp(random.uniform(-1, 1))
        low = random.uniform(0, 2)
        high = low + random.uniform(.2, 4)
        s0 = random.uniform(0, 120)
        value = gain_difference(s0, high, low, tau, dil, k)
        quadrature = integral_difference(s0, high, low, tau, dil, k)
        assert abs(value - quadrature) < 6e-11 * (1 + abs(quadrature))
        checked_integrals += 1
        if dil*tau <= critical - .05:
            assert value > -1e-12
            checked_signs += 1

    mp.mp.dps = 70
    d, tau, high, low, k = 1, 1, 4, 1, 1
    root = mp.findroot(lambda s: high_precision_gain(s, high, low, tau, d, k), (40, 70))
    assert abs(root - mp.mpf('53.13409233711023304983361509359370769276880572882296746643146432567')) < mp.mpf('1e-40')
    assert high_precision_gain(0, high, low, tau, d, k) > 0
    assert high_precision_gain(100, high, low, tau, d, k) < 0
    assert high_precision_gain(50, high, low, tau, d, k) > 0
    print('Quadrature comparisons passed:', checked_integrals)
    print('Safe-duration sign comparisons passed:', checked_signs)
    print('Universal dimensionless crossover:', critical)
    print('Example initial nutrient crossover:', mp.nstr(root, 45))
    print('All numerical checks passed.')


if __name__ == '__main__':
    main()
