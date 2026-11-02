#!/usr/bin/env python3
"""Finite rational and numerical consistency checks for the displayed stationary tail identities.

Requires only Python 3's standard library. Its finite checks do not prove any
infinite-tail limit or the uniqueness of a stationary distribution.
"""
from fractions import Fraction
from itertools import combinations
from math import atan, comb, exp, factorial, pi, prod

CHECKS = 0


def check(condition, description):
    global CHECKS
    assert condition, description
    CHECKS += 1


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def hit_rates(n, weights):
    q = [Fraction(0)]
    for j in range(1, n + 1):
        avoid = sum(
            (weights[m - 1] * Fraction(choose(n - j, m), comb(n, m))
             for m in range(1, n + 1)), Fraction(0)
        )
        q.append(1 - avoid)
    return q


def direct_enumerated_hit_rates(n, weights):
    q = [Fraction(0)]
    for j in range(1, n + 1):
        chosen_labels = set(range(j))
        val = Fraction(0)
        for m in range(1, n + 1):
            count = sum(bool(chosen_labels.intersection(sub))
                        for sub in combinations(range(n), m))
            val += weights[m - 1] * Fraction(count, comb(n, m))
        q.append(val)
    return q


def amplification(q):
    n = len(q) - 1
    return [Fraction(1)] + [
        Fraction(factorial(j)) * q[1] ** j / prod(q[1:j+1])
        for j in range(1, n + 1)
    ]


def reconstruct(H):
    n = len(H) - 1
    q = [Fraction(0)] + [
        Fraction(j) * H[j-1] * H[n] / (n * H[j] * H[n-1])
        for j in range(1, n + 1)
    ]
    b = [1 - v for v in q]
    recovered = [
        Fraction(comb(n, m)) * sum(
            ((-1) ** (m-s) * comb(m, s) * b[n-s]
             for s in range(m+1)), Fraction(0)
        ) for m in range(1, n+1)
    ]
    return q, recovered


def normalized(values):
    total = sum(values)
    return [Fraction(v, total) for v in values]


for n in range(2, 10):
    laws = [
        [int(m == 1) for m in range(1, n+1)],
        [int(m == n) for m in range(1, n+1)],
        [int(m == (n+1)//2) for m in range(1, n+1)],
        [1 for m in range(1, n+1)],
        [m for m in range(1, n+1)],
        [n+1-m for m in range(1, n+1)],
        [m*m + 3*m + 1 for m in range(1, n+1)],
    ]
    for raw in laws:
        p = normalized(raw)
        q = hit_rates(n, p)
        check(q == direct_enumerated_hit_rates(n, p), (n, 'direct subset counting'))
        check(q[n] == 1 and all(v > 0 for v in q[1:]), (n, 'hit rate positivity'))
        H = amplification(q)
        check(all(Fraction(1) <= H[j] <= factorial(j) for j in range(2, n+1)),
              (n, 'sharp amplitude envelope'))
        check(H[1] == 1, (n, 'one-particle normalization'))
        recovered_q, recovered_p = reconstruct(H)
        check(recovered_q == q, (n, 'hit-rate inverse'))
        check(recovered_p == p, (n, 'law inverse'))
        # Stationary generator recursion versus the explicit age moment product.
        moments = [Fraction(1)]
        for j in range(1, n+1):
            moments.append(Fraction(j) * moments[-1] / q[j])
            check(moments[j] == Fraction(factorial(j), 1) / prod(q[1:j+1]),
                  (n, j, 'age-moment recursion'))
        if sum(int(x > 0) for x in p) == 1:
            m = next(i+1 for i, v in enumerate(p) if v)
            check(H[2] == 2 / (2 - Fraction(m-1, n-1)),
                  (n, m, 'pair constant'))
            check(m == 1 + 2*(n-1)*(1 - 1/H[2]),
                  (n, m, 'fixed batch identification'))


def simpson(f, upper=50.0, steps=8000):
    step = upper/steps
    return (step/3) * (f(0) + f(upper) +
        4*sum(f(i*step) for i in range(1, steps, 2)) +
        2*sum(f(i*step) for i in range(2, steps, 2)))


# When every particle shares one reset clock of rate one, the stationary
# common age is Exp(1). At alpha=1, conditional displacements are Cauchy:
# P(|X|>x | age=a) = 2*atan(a/x)/pi for D=1.
x = 1000.0
single = simpson(lambda a: exp(-a)*2*atan(a/x)/pi)
check(abs(x*single - 2/pi) < 0.004, 'Cauchy one-particle tail')
for j in (2, 3, 4):
    joint = simpson(lambda a: exp(-a)*(2*atan(a/x)/pi)**j)
    factor = joint / (single ** j)
    check(abs(factor - factorial(j)) < 0.1, (j, 'Cauchy joint tail factor'))

print('PASS: %d finite exact and numerical consistency checks' % CHECKS)
