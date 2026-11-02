#!/usr/bin/env python3
"""Exact-rational checks for two common-order anchored ballot record counts.

Only the Python standard library is required. Finite checks complement, but do
not replace, the mathematical proof for arbitrary ballot sizes.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial
import random


def records(order, display):
    position = {x: i for i, x in enumerate(order)}
    minimum = len(order)
    count = 0
    for x in display:
        if position[x] < minimum:
            count += 1
            minimum = position[x]
    return count


def covariance_brute(p, q):
    n = len(p)
    rp = []
    rq = []
    for display in permutations(p):
        rp.append(records(p, display))
        rq.append(records(q, display))
    k = factorial(n)
    return Fraction(sum(x * y for x, y in zip(rp, rq)), k) - \
        Fraction(sum(rp) * sum(rq), k * k)


def covariance_pair_formula(p, q):
    # Pairwise record-indicator calculation using independent uniform clocks.
    n = len(p)
    P = {p[i]: set(p[:i + 1]) for i in range(n)}
    Q = {q[i]: set(q[:i + 1]) for i in range(n)}
    value = Fraction(0)
    for x in p:
        for y in q:
            A, B = P[x], Q[y]
            a, b = len(A), len(B)
            u = len(A | B)
            if x == y:
                joint = Fraction(1, u)
            elif x in B and y in A:
                joint = Fraction(0)
            elif x in B:
                joint = Fraction(1, a * u)
            elif y in A:
                joint = Fraction(1, b * u)
            else:
                joint = Fraction(a + b, a * b * u)
            value += joint - Fraction(1, a * b)
    return value


def expected_increment(p, q, i):
    # q[i], q[i+1] currently occur in p in the same order.
    a, b = q[i], q[i + 1]
    assert p.index(a) < p.index(b)
    S = set(q[:i])
    A = set(p[:p.index(a)])
    r = 1 + len(S | A)
    return Fraction(1, r * (r + 1))


def run():
    n_brute = n_cov = n_swap = 0
    for n in range(2, 7):
        p = tuple(range(n))
        values = {}
        for q in permutations(p):
            c = covariance_pair_formula(p, q)
            values[q] = c
            n_cov += 1
            if n <= 5:
                assert covariance_brute(p, q) == c, ('brute', n, q)
                n_brute += 1
        h = sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))
        h2 = sum((Fraction(1, k * k) for k in range(1, n + 1)), Fraction(0))
        assert values[p] == h - h2
        assert values[p[::-1]] == 1 - h2
        assert sum(x == h - h2 for x in values.values()) == 1
        assert sum(x == 1 - h2 for x in values.values()) == 1
        for q in values:
            for i in range(n - 1):
                if p.index(q[i]) < p.index(q[i + 1]):
                    qq = list(q)
                    qq[i], qq[i + 1] = qq[i + 1], qq[i]
                    got = values[q] - values[tuple(qq)]
                    predicted = expected_increment(p, q, i)
                    assert got == predicted, ('swap', n, q, i, got, predicted)
                    n_swap += 1
    rng = random.Random(20261031)
    for _ in range(200):
        n = 7
        p = list(range(n))
        rng.shuffle(p)
        q = list(range(n))
        rng.shuffle(q)
        candidates = [i for i in range(n - 1) if p.index(q[i]) < p.index(q[i + 1])]
        if not candidates:
            continue
        i = rng.choice(candidates)
        qq = q.copy()
        qq[i], qq[i + 1] = qq[i + 1], qq[i]
        assert covariance_pair_formula(tuple(p), tuple(q)) - covariance_pair_formula(tuple(p), tuple(qq)) == expected_increment(p, q, i)
        n_swap += 1
    print('PASS: exact direct-enumeration comparisons:', n_brute)
    print('PASS: exact pair-indicator covariances:', n_cov)
    print('PASS: exact adjacent-swap increments:', n_swap)
    print('PASS: sharp endpoints and unique equality profiles for n=2,...,6')
    print('PASS: independently relabeled randomized n=7 profiles')


if __name__ == '__main__':
    run()
