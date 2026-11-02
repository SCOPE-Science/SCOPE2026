#!/usr/bin/env python3
"""Exact finite checks for two leading preference multiplicities in parking functions.

The all-size assertions require the separate mathematical proof; this file
checks their finite consequences through independently constructed counts.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial

checks = 0


def assert_eq(a, b, label):
    global checks
    assert a == b, (label, a, b)
    checks += 1


def parking(seq):
    return all(x <= i for i, x in enumerate(sorted(seq), 1))


def observed_brute(n):
    ans = Counter()
    for seq in product(range(1, n + 1), repeat=n):
        if parking(seq):
            ans[(seq.count(1), seq.count(2))] += 1
    return ans


def predicted(n):
    ans = Counter({(n, 0): 1})
    for k in range(1, n):
        # [v^t](v+k-1)(v+n-1)^(n-k-1).
        m = n - k - 1
        for t in range(m + 2):
            coeff = 0
            if t <= m:
                coeff += (k - 1) * comb(m, t) * (n - 1) ** (m - t)
            if 1 <= t <= m + 1:
                coeff += comb(m, t - 1) * (n - 1) ** (m - t + 1)
            if coeff:
                ans[k, t] += comb(n, k) * coeff
    return ans


def via_multiplicities(n):
    """Separate enumeration over weak compositions, using factorial weights."""
    ans = Counter()
    def visit(i, remaining, counts, accum):
        if i == n:
            if remaining != 0:
                return
            ans[counts[0], counts[1]] += factorial(n) // accum
            return
        for k in range(remaining + 1):
            # Necessary and sufficient ballot inequalities.
            used = n - remaining + k
            if used < i + 1:
                continue
            visit(i + 1, remaining - k, counts + (k,), accum * factorial(k))
    visit(0, n, (), 1)
    return ans


for n in range(2, 7):
    brute = observed_brute(n)
    theory = predicted(n)
    assert_eq(sum(brute.values()), (n + 1) ** (n - 1), ('total', n))
    assert_eq(brute, theory, ('brute vs polynomial', n))
    for k in range(1, n + 1):
        marg = sum(v for (a, b), v in brute.items() if a == k)
        expect = comb(n - 1, k - 1) * n ** (n - k)
        assert_eq(marg, expect, ('first margin', n, k))
        if k == n:
            assert_eq(sum(b * v for (a, b), v in brute.items() if a == k), 0,
                      ('terminal', n))
        else:
            # Conditional probability generating function factorization.
            cond_num = [sum(v for (a, b), v in brute.items() if a == k and b == t)
                        for t in range(n - k + 1)]
            model_num = [theory.get((k, t), 0) for t in range(n - k + 1)]
            assert_eq(cond_num, model_num, ('conditional', n, k))
    ek = Fraction(sum(k * v for (k, t), v in brute.items()), len([0]) and sum(brute.values()))
    et = Fraction(sum(t * v for (k, t), v in brute.items()), sum(brute.values()))
    ekt = Fraction(sum(k * t * v for (k, t), v in brute.items()), sum(brute.values()))
    got_cov = ekt - ek * et
    formula_cov = 2 * Fraction(n, n + 1) ** n - 1 - Fraction(n - 1, (n + 1) ** 2)
    assert_eq(got_cov, formula_cov, ('covariance', n))
    assert got_cov < 0
    checks += 1

for n in range(2, 10):
    theory = predicted(n)
    independent = via_multiplicities(n)
    assert_eq(independent, theory, ('multiplicity independent', n))
    assert_eq(sum(theory.values()), (n + 1) ** (n - 1), ('total theory', n))

# A direct exact check that each conditional expectation is strictly decreasing.
for n in range(2, 101):
    means = [Fraction(1, k) + Fraction(n - k - 1, n) for k in range(1, n)] + [Fraction(0)]
    for a, b in zip(means, means[1:]):
        assert a > b, ('strict regression', n, a, b)
        checks += 1

print('VERIFY_OK', checks)
