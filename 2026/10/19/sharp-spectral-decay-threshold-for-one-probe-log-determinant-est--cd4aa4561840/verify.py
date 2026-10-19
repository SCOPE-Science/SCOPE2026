#!/usr/bin/env python3
"""Reproduce finite checks for spectral-ratio budget-allocation formulas.

Run with Python 3: python verify.py
These numerical checks support, but do not prove, the infinite and universal statements.
"""
import math
import random
from fractions import Fraction


def tail_sums(a, k):
    return sum((t * t for t in a[k:]), Fraction(0))


def mse(a, budget, probe_cost, probes):
    return 2 * tail_sums(a, budget - probe_cost * probes) / probes


def exact_spectral_checks():
    rng = random.Random(413)
    tests = 0
    for _ in range(1100):
        c = rng.randrange(1, 6)
        budget = rng.randrange(c, c * 7 + 1)
        d = rng.randrange(budget - c + 2, budget - c + 30)
        q = Fraction(rng.randrange(1, 9), 10)  # includes values above and below criticality
        a = [Fraction(rng.randrange(1, 9), 1)]
        for j in range(1, d):
            a.append(a[-1] * Fraction(rng.randrange(0, 11), 10) * q)
        S1 = mse(a, budget, c, 1)
        r = q ** (2 * c)
        for probes in range(2, budget // c + 1):
            Sn = mse(a, budget, c, probes)
            assert S1 <= probes * (r ** (probes - 1)) * Sn
            tests += 1
            if r <= Fraction(1, 2):
                assert S1 <= Sn
                tests += 1
    return tests


def sharpness_checks():
    tests = 0
    for c in range(1, 7):
        r_min = 2 ** (-1.0 / (2 * c))
        for q in [r_min + (1 - r_min) * z / 7 for z in (1, 2, 4, 6)]:
            assert 0 < q < 1
            d = c + 4
            while True:
                a = [q ** j for j in range(d)]
                one = 2 * sum(t * t for t in a[c:])
                two = sum(t * t for t in a)
                if one > two:
                    break
                d += 1
                assert d < 50000
            assert one / two > 1
            tests += 1
    return tests


def geometric_optimizers():
    tests = 0
    for c in range(1, 6):
        for B in range(c, 12 * c + 1):
            nmax = B // c
            for q in (0.35, 0.55, 0.7, 0.85, 0.95, 0.99):
                r = q ** (2 * c)
                h = r / (1-r)
                scores = [q ** (2 * (B - c*n)) / n for n in range(1, nmax+1)]
                k = min(nmax, max(1, math.ceil(h)))
                assert scores[k-1] <= min(scores) * (1+1e-10)
                tests += 1
    return tests


def powerlaw_checks():
    tests = 0
    for c in (1, 3):
        for p in (1.25, 1.5, 2.0, 3.0):
            for B in (400, 800, 1600, 3200):
                # Hurwitz-zeta tail via Euler-Maclaurin through six Bernoulli terms.
                def spectral_tail(k):
                    x = float(k + 1)
                    s = 2*p
                    return (x**(1-s)/(s-1) + x**(-s)/2 +
                            s*x**(-s-1)/12 - s*(s+1)*(s+2)*x**(-s-3)/720 +
                            s*(s+1)*(s+2)*(s+3)*(s+4)*x**(-s-5)/30240)
                scores = [2*spectral_tail(B-c*n)/n for n in range(1,B//c+1)]
                nstar = min(range(1,B//c+1), key=lambda n:scores[n-1])
                target_fraction = 1/(2*p*c)
                assert abs(nstar/B-target_fraction) < 0.01
                tests += 1
    return tests


def gaussian_variance_checks():
    rng = random.Random(883)
    tests = 0
    c, B, d, q = 2, 12, 22, 0.63
    a = [q ** i for i in range(d)]
    for n in (1, 2, 3, 4):
        k = B-c*n
        exact = 2 * sum(z*z for z in a[k:]) / n
        total = 0.0
        repeats = 35000
        for _ in range(repeats):
            value = sum( z*(rng.gauss(0,1)**2-1) for _ in range(n) for z in a[k:])/n
            total += value*value
        estimated = total/repeats
        assert abs(estimated-exact)/exact < 0.08, (n, estimated, exact)
        tests += 1
    return tests


if __name__ == '__main__':
    counts = dict(finite_exact=exact_spectral_checks(),
                  strict_threshold_witnesses=sharpness_checks(),
                  geometric_optimizer=geometric_optimizers(),
                  power_law_asymptotics=powerlaw_checks(),
                  gaussian_second_moments=gaussian_variance_checks())
    print('CHECKS PASSED:', counts, 'total:', sum(counts.values()))
