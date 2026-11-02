#!/usr/bin/env python3
"""Finite checks for an exact substitution-scale Parikh law.

Only scientific definitions and tests are included. Execute with Python 3.10+.
"""
from collections import defaultdict
from fractions import Fraction


def formula(B, m):
    assert B >= 2 and m >= 2 and B % m == 0
    origin = (0,) * m
    distribution = defaultdict(Fraction)
    distribution[origin] += Fraction(1, m)
    def prefix(a, r):
        result = [0] * m
        for j in range(r):
            result[(a + j) % m] += 1
        return result
    for r in range(1, m):
        for a in range(m):
            before = prefix(a, r)
            for c in range(m):
                after = prefix((a + c + 1) % m, r)
                v = tuple(after[k] - before[k] for k in range(m))
                q = Fraction((B - 1) * B ** (m - 1 - c), B ** m - 1)
                distribution[v] += q / (m * m)
    return dict(distribution)


def morphism_word(B, m, length):
    """Directly apply the uniform substitution, without digital-sum arithmetic."""
    word = [0]
    while len(word) < length:
        word = [(a + r) % m for a in word for r in range(B)]
    return word[:length]


def observed(B, m, e, K):
    """Exact finite frequencies in B**K consecutive complete aligned B-blocks."""
    J = B ** K
    L = B ** (e + 1)
    word = morphism_word(B, m, B * J + L)
    counts = [0] * m
    for letter in word[:L]:
        counts[letter] += 1
    center = L // m
    freq = defaultdict(int)
    for i in range(B * J):
        key = tuple(x - center for x in counts)
        freq[key] += 1
        if i + 1 < B * J:
            counts[word[i]] -= 1
            counts[word[i + L]] += 1
    return {v: Fraction(x, B * J) for v, x in freq.items()}


def exact_joint_digits(B, m, e, c):
    """Enumerate exactly a representative residue block and check carry/letter independence."""
    total = B ** (e + c + 2)
    goal = B ** (e + c + 1)
    # Use the highest free digit, and enumerate lower fixed combinations.
    # A full block is practical only for small B,e,c.
    counts = [0] * m
    for j in range(total):
        x = j // (B ** e)
        run = 0
        while x % B == B - 1:
            run += 1
            x //= B
        if run == c:
            y = j
            residue = 0
            while y:
                residue += y % B
                y //= B
            counts[residue % m] += 1
    expected = total * Fraction(B - 1, B ** (c + 1) * m)
    assert all(Fraction(value) == expected for value in counts), (B, m, e, c, counts, expected)


def run():
    ntests = 0
    for B, m in ((2, 2), (3, 3), (4, 4), (5, 5), (6, 3), (4, 2), (8, 4), (9, 3)):
        dist = formula(B, m)
        assert sum(dist.values()) == 1
        assert dist[(0,) * m] > 0
        assert all(val > 0 for val in dist.values())
        assert all(sum(v) == 0 and all(abs(x) <= 1 for x in v) for v in dist)
        assert all(dist[v] == dist[tuple(-x for x in v)] for v in dist)
        assert all(dist[v] == dist[v[1:] + v[:1]] for v in dist)
        zero_formula = Fraction(1, m) + Fraction((m - 1) * (B - 1), m * (B ** m - 1))
        assert dist[(0,) * m] == zero_formula
        q_sum = sum((Fraction((B - 1) * B ** (m - c - 1), B ** m - 1)
                     for c in range(m)), Fraction(0))
        assert q_sum == 1
        ntests += 8 + len(dist)
    # Exact symbolic reference instances.
    assert formula(2, 2)[(0, 0)] == Fraction(2, 3)
    assert formula(2, 2)[(-1, 1)] == Fraction(1, 6)
    assert formula(3, 3)[(0, 0, 0)] == Fraction(5, 13)
    assert all(v == (0, 0, 0) or formula(3, 3)[v] == Fraction(4, 39) for v in formula(3, 3))
    ntests += 4
    for B, m, K, emax in ((2, 2, 13, 4), (3, 3, 8, 4), (4, 4, 6, 3), (6, 3, 5, 3), (4, 2, 6, 3)):
        expected = formula(B, m)
        for e in range(emax):
            empirical = observed(B, m, e, K)
            # Discrepancy from the limiting law is controlled by finite-prefix effects.
            max_err = max(abs(empirical.get(v, 0) - p) for v, p in expected.items())
            assert max_err < Fraction(1, 20), (B, m, K, e, max_err)
            assert set(empirical).issubset(set(expected)), (B, m, e)
            ntests += 2
    for B, m, e, c in ((2, 2, 0, 0), (3, 3, 0, 1), (3, 3, 1, 0), (4, 2, 0, 2), (4, 4, 0, 1)):
        exact_joint_digits(B, m, e, c)
        ntests += 1
    print('VERIFY_OK', 'checks=', ntests)
    for B, m in ((2, 2), (3, 3), (4, 4), (6, 3)):
        dist = formula(B, m)
        scalar = defaultdict(Fraction)
        for vec, p in dist.items():
            scalar[sum(j * vec[j] for j in range(m))] += p
        print('B=', B, 'm=', m, 'Parikh_classes=', len(dist),
              'zero_mass=', str(dist[(0,) * m]),
              'weighted_marginal=', [(k, str(v)) for k, v in sorted(scalar.items())])


if __name__ == '__main__':
    run()
