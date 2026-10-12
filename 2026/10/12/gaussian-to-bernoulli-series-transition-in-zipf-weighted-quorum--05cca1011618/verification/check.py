#!/usr/bin/env python3
"""Finite exact checks for weighted first-arrival mass at nested thresholds."""
from fractions import Fraction as Q
from itertools import product
from math import sqrt, log, fsum

checks = 0

def test(ok):
    global checks
    if not ok:
        raise AssertionError(f"identity failed at check {checks + 1}")
    checks += 1

profiles = (
    (1, 1),
    (1, 2, 3),
    (1, 2, 3, 4),
    (1, 3, 4, 8),
    (1, 1, 2, 2, 3),
    (1, 1, 1, 3, 4, 6),
    (1, 2, 2, 3, 4, 6, 7),
)
levels = ((Q(1, 4), Q(2, 3)),
          (Q(1, 3), Q(3, 4)),
          (Q(2, 5), Q(4, 5)),
          (Q(1, 2), Q(7, 8)))

for weights in profiles:
    tot = sum(weights)
    w = [Q(x, tot) for x in weights]
    squares = sum(x * x for x in w)
    for a, b in levels:
        probs = (a, b - a, 1 - b)
        mean_a = mean_b = square_a = square_b = mixed = Q(0)
        for outcome in product(range(3), repeat=len(w)):
            prob = Q(1)
            ma = mb = Q(0)
            for j, digit in enumerate(outcome):
                prob *= probs[digit]
                if digit == 0:
                    ma += w[j]
                    mb += w[j]
                elif digit == 1:
                    mb += w[j]
            mean_a += prob * ma
            mean_b += prob * mb
            square_a += prob * ma * ma
            square_b += prob * mb * mb
            mixed += prob * ma * mb
        test(mean_a == a)
        test(mean_b == b)
        test(square_a - mean_a * mean_a == a * (1 - a) * squares)
        test(square_b - mean_b * mean_b == b * (1 - b) * squares)
        test(mixed - mean_a * mean_b == a * (1 - b) * squares)

# Exact third/fourth Bernoulli cumulants, from two-atom moments.
for t in (Q(1, 4), Q(2, 5), Q(1, 2), Q(3, 4)):
    values = ((1 - t, t), (-t, 1 - t))
    m2 = t * (1 - t) ** 2 + (1 - t) * t ** 2
    m3 = t * (1 - t) ** 3 - (1 - t) * t ** 3
    m4 = t * (1 - t) ** 4 + (1 - t) * t ** 4
    test(m2 == t * (1 - t))
    test(m3 == t * (1 - t) * (1 - 2 * t))
    test(m4 - 3 * m2 * m2 == t * (1 - t) * (1 - 6 * t * (1 - t)))

# Check normalization constants by convergence of independent power sums.
def H(n, t):
    return fsum(i ** (-t) for i in range(1, n + 1))

for s in (0.0, 0.2, 0.45):
    constant = (1 - s) / sqrt(1 - 2 * s)
    deviations = []
    for n in (200, 2000, 20000):
        a = sqrt(H(n, 2 * s)) / H(n, s)
        deviations.append(abs(sqrt(n) * a - constant))
    test(deviations[-1] < deviations[0] if s > 0 else deviations[-1] < 1e-12)
for s in (0.5,):
    deviations = []
    for n in (200, 2000, 20000):
        a = sqrt(H(n, 2 * s)) / H(n, s)
        deviations.append(abs(sqrt(n / log(n)) * a - 0.5))
    test(deviations[-1] < deviations[0])
for s in (0.65, 0.75, 0.9):
    # The product N^(1-s)*sqrt(H_2s)/H_s converges to (1-s)*sqrt(zeta(2s)).
    # Finite partial sums of zeta are sufficient for a monotone convergence check.
    n1, n2, ref = 200, 5000, 200000
    limit_est = (1 - s) * sqrt(H(ref, 2 * s) + ref ** (1 - 2 * s) / (2 * s - 1))
    def fac(n):
        return n ** (1 - s) * sqrt(H(n, 2 * s)) / H(n, s)
    test(abs(fac(n2) - limit_est) < abs(fac(n1) - limit_est))

print(f"PASS: {checks} independent finite exact and asymptotic checks")
