#!/usr/bin/env python3
"""Recompute stationary fractional-gyrator signed-area calibrations and cusp signs."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma


def noise_factor(alpha):
    return 2 * gamma(1 + alpha) * math.sin(math.pi * alpha / 2)


def damping_denominator(omega, coupling):
    return (omega * omega + (1 - coupling) ** 2) * (omega * omega + (1 + coupling) ** 2)


def F(coupling, alpha):
    return (1 + coupling) ** (2 - alpha) - (1 - coupling) ** (2 - alpha)


def exact_current(coupling, alpha, temperature):
    return -temperature * gamma(1 + alpha) * F(coupling, alpha) / 2


def integral_current(coupling, alpha, temperature):
    integral = quad(lambda w: w ** (3 - alpha) / damping_denominator(w, coupling),
                    0, np.inf, epsabs=1e-10, limit=300)[0]
    return -2 * coupling * temperature * noise_factor(alpha) * integral / math.pi


def temperature_ratio(coupling, ax, ay):
    return gamma(1 + ax) * F(coupling, ax) / (gamma(1 + ay) * F(coupling, ay))


def sine_minus_linear(z):
    if z < .02:
        return z ** 3 * (-1 / 6 + z * z / 120 - z ** 4 / 5040)
    return math.sin(z) - z


def fractional_remainder(coupling, alpha, temperature, t):
    a2 = ((1 - coupling) * t) ** 2
    b2 = ((1 + coupling) * t) ** 2
    def positive_weight(z):
        return z ** (2 - alpha) / ((z * z + a2) * (z * z + b2))
    # Beyond 40, isolate the nonoscillating negative linear tail, and
    # perform the absolutely convergent sine tail separately.
    small = quad(lambda z: positive_weight(z) * sine_minus_linear(z),
                 0, 40, epsabs=4e-10, epsrel=2e-9, limit=250)[0]
    linear_tail = quad(lambda z: -z * positive_weight(z),
                       40, np.inf, epsabs=1e-11, limit=250)[0]
    sine_tail = quad(positive_weight, 40, np.inf, weight='sin', wvar=1,
                     epsabs=2e-10, limit=250)[0]
    return -2 * coupling * temperature * noise_factor(alpha) * (t ** (1 + alpha)) * (small + linear_tail + sine_tail) / math.pi


def run():
    tests = [(0.3, 0.6, 1.4, 0.9), (0.6, 1.3, 0.55, 2.1),
             (0.1, 1.1, 1.75, 1.5), (0.5, 1.0, 1.65, 1.7)]
    checks = 0
    for u, ax, ay, tx in tests:
        ty = tx * temperature_ratio(u, ax, ay)
        assert ty > 0
        checks += 1
        for a, temp in [(ax, tx), (ay, ty)]:
            assert abs(integral_current(u, a, temp) - exact_current(u, a, temp)) < 3e-8
            checks += 1
        assert abs(exact_current(u, ax, tx) - exact_current(u, ay, ty)) < 2e-12
        checks += 1
        amin = min(ax, ay)
        predicted = 2 * u * (tx if ax < ay else -ty) / (1 + amin)
        values = []
        for t in [0.1, 0.05, 0.015, 0.005]:
            lag_asym = fractional_remainder(u, ax, tx, t) - fractional_remainder(u, ay, ty, t)
            ratio = lag_asym / (predicted * t ** (1 + amin))
            values.append(abs(ratio - 1))
            assert lag_asym * predicted > 0
            assert abs(ratio - 1) < .35
            checks += 3
        assert values[-1] < values[0]
        checks += 1
    print(f'Passed {checks} deterministic spectral/cusp comparisons.')

if __name__ == '__main__':
    run()
