"""Exact finite checks for normal-cone angle identities of bipartite graphical zonotopes.

Run: python angular_collision_checker.py
Uses only Python's standard library. Finite tests support, but do not prove,
the all-parameter statements in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def run_factorial_product(word):
    product = 1
    count = 1
    for a, b in zip(word, word[1:]):
        if a == b:
            count += 1
        else:
            product *= factorial(count)
            count = 1
    return product * factorial(count)


def word_sums(p, q):
    n = p + q
    total = 0
    minimum = None
    maximum = 0
    for a_positions in combinations(range(n), p):
        a_positions = set(a_positions)
        word = tuple(0 if k in a_positions else 1 for k in range(n))
        weight = run_factorial_product(word)
        total += weight
        minimum = weight if minimum is None else min(minimum, weight)
        maximum = max(maximum, weight)
    return total, minimum, maximum


def orientation_extension_counts(p, q):
    """Enumerate labeled permutations, independent of block-composition enumeration."""
    n = p + q
    counts = Counter()
    for permutation in permutations(range(n)):
        ranks = [0] * n
        for position, v in enumerate(permutation):
            ranks[v] = position
        signature = tuple(int(ranks[a] < ranks[b]) for a in range(p) for b in range(p, n))
        counts[signature] += 1
    return counts


def factorial_power_coefficients(degree, kmax):
    fac = [factorial(i) for i in range(degree + 1)]
    powers = [[0] * (degree + 1) for _ in range(kmax + 1)]
    powers[0][0] = 1
    for k in range(1, kmax + 1):
        for n in range(1, degree + 1):
            powers[k][n] = sum(fac[j] * powers[k - 1][n - j] for j in range(1, n + 1))
    return powers


def series_collision(p, q):
    """Coefficient of F(x)G(y)(2+F(x)+G(y))/(1-F(x)G(y))."""
    limit = min(p, q) + 1
    aa = factorial_power_coefficients(p, limit)
    bb = factorial_power_coefficients(q, limit)
    weighted = 0
    for k in range(1, limit + 1):
        weighted += (2 * aa[k][p] * bb[k][q]
                     + aa[k][p] * bb[k - 1][q]
                     + aa[k - 1][p] * bb[k][q])
    return Fraction(weighted * factorial(p) * factorial(q), factorial(p + q) ** 2)


def minimum_data(p, q):
    if p < q:
        p, q = q, p
    n = p + q
    if p == q:
        return Fraction(1, factorial(n)), 2 * factorial(p) * factorial(q)
    s, r = divmod(p, q + 1)
    assert s >= 1
    product = factorial(s) ** (q + 1 - r) * factorial(s + 1) ** r
    count = factorial(q) * comb(q + 1, r) * factorial(p) // product
    return Fraction(product, factorial(n)), count


def check():
    total_cases = 0
    checked_orientations = 0
    for p in range(1, 5):
        for q in range(1, 5):
            if p + q > 7:
                continue
            words, smallest, largest = word_sums(p, q)
            counts = orientation_extension_counts(p, q)
            nfac = factorial(p + q)
            assert sum(counts.values()) == nfac
            assert sum(v * v for v in counts.values()) == words * factorial(p) * factorial(q)
            assert series_collision(p, q) == Fraction(sum(v*v for v in counts.values()), nfac*nfac)
            assert Fraction(max(counts.values()), nfac) == Fraction(factorial(p)*factorial(q), nfac)
            min_ang, min_count = minimum_data(p, q)
            assert Fraction(min(counts.values()), nfac) == min_ang
            assert sum(v == min_ang * nfac for v in counts.values()) == min_count
            assert largest == factorial(p)*factorial(q)
            assert smallest == min_ang * nfac
            total_cases += 1
            checked_orientations += len(counts)
    assert series_collision(2, 2) == Fraction(7, 72)
    for q in (1, 2, 3):
        hq = sum(Fraction(1, comb(q, j)) for j in range(q+1))
        limit = factorial(q)**2 * hq
        scaled = []
        for p in (30, 60, 120):
            assert p >= q
            scaled.append(series_collision(p, q) * p**(2*q))
        # Direct checks of approach from below for these parameter samples.
        assert all(scaled[i] < scaled[i+1] < limit for i in range(2))
        print('q=', q, 'limit=', str(limit), 'scaled_p120=', float(scaled[-1]))
    print('PASS; brute pairs:', total_cases, 'orientations:', checked_orientations,
          'and long-strip coefficient comparisons: 9')


if __name__ == '__main__':
    check()
