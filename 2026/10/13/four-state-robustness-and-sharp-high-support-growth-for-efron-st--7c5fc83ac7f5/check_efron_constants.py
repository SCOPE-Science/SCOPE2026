#!/usr/bin/env python3
"""Finite reproducibility checks for sharp constants in directed Efron--Stein comparisons.

No finite calculation is used as a proof of the uniform or asymptotic theorem.
"""
import math
from functools import reduce


def spectral_scan(k):
    """Find maximum discrete Fourier ratio over all cycle lengths <= k.

    For a fixed number of active coordinates, retain the smallest energy at
    every sum phase. The stopping certificate uses the universal bound
    numerator <= 1 and energy >= active_count*sin(pi/k)**2.
    """
    period = math.lcm(*range(1, k + 1))
    options = {}
    for m in range(2, k + 1):
        for u in range(1, m):
            residue = (u * period // m) % period
            cost = math.sin(math.pi * u / m) ** 2
            if cost < options.get(residue, math.inf):
                options[residue] = cost
    energy = [math.inf] * period
    energy[0] = 0.0
    sinus = [math.sin(math.pi * j / period) ** 2 for j in range(period)]
    best, best_t = 1.0, 1
    t = 0
    while True:
        t += 1
        next_energy = [math.inf] * period
        for residue, cost in options.items():
            for old, val in enumerate(energy):
                dst = (old + residue) % period
                if val + cost < next_energy[dst]:
                    next_energy[dst] = val + cost
        energy = next_energy
        for j in range(period):
            if energy[j] > 0 and math.isfinite(energy[j]):
                ratio = sinus[j] / energy[j]
                if ratio > best + 1e-13:
                    best, best_t = ratio, t
        # Every larger active-coordinate count has ratio bounded by 1/(t sin^2 alpha).
        if 1.0 / ((t + 1) * math.sin(math.pi / k) ** 2) < best - 1e-12:
            return best, best_t


def direct_cycle_ratio(k, n):
    """Evaluate expectations of cos(2*pi*sum X/k) on deterministic k-cycles."""
    from itertools import product
    top = 0.0
    bottom = 0.0
    for states in product(range(k), repeat=n):
        f = lambda s: math.cos(2 * math.pi * sum(s) / k)
        x = list(states)
        y = [(v + 1) % k for v in x]
        top += (f(x) - f(y)) ** 2
        for j in range(n):
            z = x.copy()
            z[j] = y[j]
            bottom += (f(x) - f(z)) ** 2
    return top / bottom


def main():
    expected = {2: 1.0, 3: 1.0, 4: 1.0,
                5: (3 + math.sqrt(5)) / 4, 6: 1.5}
    for k, target in expected.items():
        value, witness_count = spectral_scan(k)
        assert abs(value - target) < 2e-12, (k, value, target)
        print('k=%s, spectral maximum=%.12f, active count=%d' %
              (k, value, witness_count))
    for k, n in [(3, 1), (4, 2), (5, 2), (6, 2)]:
        observed = direct_cycle_ratio(k, n)
        predicted = math.sin(math.pi * n / k) ** 2 / (
            n * math.sin(math.pi / k) ** 2)
        assert abs(observed - predicted) < 2e-12
    for k in [4, 5, 6, 7, 8, 16, 30, 100]:
        alpha = math.pi / k
        for j in range(1001):
            angle = alpha + (math.pi / 2 - alpha) * j / 1000
            assert math.sin(angle) ** 2 / angle >= (
                math.sin(alpha) ** 2 / alpha) - 1e-12
    tau_lo, tau_hi = 1.0, 1.4
    for _ in range(100):
        tau = (tau_lo + tau_hi) / 2
        if math.tan(tau) > 2 * tau:
            tau_hi = tau
        else:
            tau_lo = tau
    tau = (tau_lo + tau_hi) / 2
    asymptotic = math.sin(tau) ** 2 / (math.pi * tau)
    assert abs(asymptotic - 0.23065095754814657) < 5e-13
    for k in (100, 1000, 10000):
        n = max(1, int(tau * k / math.pi))
        ratio = math.sin(math.pi * n / k) ** 2 / (
            n * math.sin(math.pi / k) ** 2)
        upper = (math.pi / k) * math.sin(tau) ** 2 / (
            tau * math.sin(math.pi / k) ** 2)
        assert ratio <= upper + 1e-10
        print('k=%d: lower/k=%.9f, upper/k=%.9f' %
              (k, ratio / k, upper / k))
    print('Finite checks passed; universal conclusions require the written proof.')


if __name__ == '__main__':
    main()
