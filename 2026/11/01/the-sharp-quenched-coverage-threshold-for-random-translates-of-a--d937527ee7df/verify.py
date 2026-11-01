"""Reproducible finite checks for random translated-cube coverage.

Only Python standard library. Diagnostics are not an infinite proof.
"""
from fractions import Fraction
from math import comb, exp, factorial, lgamma, log, sqrt, erf, pi
from random import Random

GAMMA = 0.5772156649015328606


def mean_fraction_exact(d, m):
    return sum(((-1) ** (k + 1)) * Fraction(comb(m, k), (k + 1) ** d)
               for k in range(1, m + 1))


def mean_fraction_harmonic(d, m):
    r = d - 1
    h = [Fraction(1)] + [Fraction(0)] * r
    for j in range(1, m + 2):
        for k in range(1, r + 1):
            h[k] += h[k - 1] / j
    return Fraction(1) - h[r] / (m + 1)


def box_union_fraction(boxes, d):
    # Each translated box is [u_j,u_j+1] in each coordinate.
    # Inclusion-exclusion is exact on rational coordinates.
    total = Fraction(0)
    for mask in range(1, 1 << len(boxes)):
        selected = [boxes[j] for j in range(len(boxes)) if mask & (1 << j)]
        length = Fraction(1)
        for i in range(d):
            left = max(row[i] for row in selected)
            right = min(row[i] + 1 for row in selected)
            length *= max(Fraction(0), right - left)
        total += (1 if len(selected) % 2 else -1) * length
    return total / (2 ** d)


def gamma_cdf_integer(d, t):
    if t <= 0:
        return 0.0
    a = [k * log(t) - lgamma(k + 1) for k in range(d)]
    mx = max(a)
    poisson_prefix = exp(mx - t) * sum(exp(v - mx) for v in a)
    return max(0.0, min(1.0, 1.0 - poisson_prefix))


def integrate_gumbel_limit(d, logm, steps=4096):
    # For astronomically large m, max-of-m exponentials has Gumbel limit.
    # Numerically integrate E[F_Gamma(d,1)(logm-log(Z))], Z~Exp(1).
    # Finite-m difference is O(1/m). Uniform midpoint rule on [0,32].
    step = 32.0 / steps
    acc = 0.0
    for i in range(steps):
        z = (i + 0.5) * step
        acc += gamma_cdf_integer(d, logm - log(z)) * exp(-z)
    return acc * step


def translated_box_test():
    # Exact nontrivial overlapping planar rational translates.
    b = [(Fraction(0), Fraction(0)),
         (Fraction(1, 4), Fraction(1, 2)),
         (Fraction(3, 4), Fraction(1, 3))]
    expected = (Fraction(3) - Fraction(3, 8) - Fraction(1, 6)
                - Fraction(5, 12) + Fraction(1, 8)) / 4
    assert box_union_fraction(b, 2) == expected


def run():
    cases = 0
    for d in range(1, 9):
        for m in range(1, 13):
            v = mean_fraction_exact(d, m)
            assert v == mean_fraction_harmonic(d, m)
            assert 0 < v < 1
            cases += 1
        assert mean_fraction_exact(d, 1) == Fraction(1, 2 ** d)
        cases += 1
    translated_box_test()
    cases += 1
    for d in (40, 80, 160):
        for s in (-1.0, 0.0, 1.0):
            a = d + s * sqrt(d)
            numerical = integrate_gumbel_limit(d, a)
            phi = exp(-s * s / 2) / sqrt(2 * pi)
            Phi = (1.0 + erf(s / sqrt(2))) / 2
            predicted = Phi + phi * (GAMMA + (1 - s * s) / 3) / sqrt(d)
            assert abs(numerical - predicted) < 1.5 / d, (d, s, numerical, predicted)
            cases += 1
    for d, tol in [(40, 0.006), (80, 0.003), (160, 0.002)]:
        observed = integrate_gumbel_limit(d, d - GAMMA - Fraction(1, 3).__float__())
        assert abs(observed - 0.5) < tol
        cases += 1
    # Independent finite Monte Carlo on small dimensions and small m.
    rng = Random(261019)
    for d, m in [(2, 3), (3, 3), (2, 4)]:
        reps = 4000
        mc = 0.0
        for _ in range(reps):
            boxes = [tuple(Fraction(rng.randrange(256), 256) for j in range(d))
                     for i in range(m)]
            mc += float(box_union_fraction(boxes, d)) / reps
        target = float(mean_fraction_exact(d, m))
        assert abs(mc - target) < 0.018, (d, m, mc, target)
        cases += 1
    print('PASS:', cases, 'deterministic assertions/cases')


if __name__ == '__main__':
    run()
