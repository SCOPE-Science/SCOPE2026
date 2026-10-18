#!/usr/bin/env python3
"""Independent small-size checks for a Bernoulli-incidence concept-count theorem.

Counts concept intents by explicit double-derivation for every binary matrix;
compares with a separately evaluated closed-pair probability sum.
"""
from fractions import Fraction
from math import comb


def intent_count_from_bits(r, m, bits):
    rows = [(bits >> (i * m)) & ((1 << m) - 1) for i in range(r)]
    total = 0
    for intent in range(1 << m):
        extent = [i for i in range(r) if rows[i] & intent == intent]
        common = (1 << m) - 1
        for i in extent:
            common &= rows[i]
        if common == intent:
            total += 1
    return total


def expectation_by_closed_pair_formula(r, m, q):
    ans = Fraction(0)
    for a in range(r + 1):
        for b in range(m + 1):
            ans += (comb(r, a) * comb(m, b) * q ** (a * b)
                    * (1 - q ** a) ** (m - b)
                    * (1 - q ** b) ** (r - a))
    return ans


def direct_expectation(r, m, q):
    total = Fraction(0)
    for x in range(1 << (r * m)):
        edges = x.bit_count()
        weight = q ** edges * (1 - q) ** (r * m - edges)
        total += weight * intent_count_from_bits(r, m, x)
    return total


def run():
    tests = [(r, m, q)
             for r in range(1, 5) for m in range(1, 5)
             for q in ((Fraction(1, 2),) if r * m > 9 else
                       (Fraction(1, 2), Fraction(1, 3), Fraction(2, 3)))
             if r * m <= 16]
    results = []
    for r, m, q in tests:
        brute = direct_expectation(r, m, q)
        analytic = expectation_by_closed_pair_formula(r, m, q)
        assert brute == analytic, (r, m, q, brute, analytic)
        assert analytic == expectation_by_closed_pair_formula(m, r, q)
        results.append((r, m, str(q), str(brute)))
    # Check concrete structural assertion: every formal concept has unique extent
    # and intent, and each enumerated intent satisfies the two closure equalities.
    # Edge configurations include the empty and universal incidence relations.
    for r, m in ((2, 3), (3, 3)):
        for x in range(1 << (r * m)):
            rows = [(x >> (i * m)) & ((1 << m) - 1) for i in range(r)]
            extent_images = set()
            intent_images = set()
            for b in range(1 << m):
                e = tuple(i for i in range(r) if rows[i] & b == b)
                a_prime = (1 << m) - 1
                for i in e:
                    a_prime &= rows[i]
                if a_prime == b:
                    assert e not in extent_images
                    extent_images.add(e)
                    intent_images.add(b)
            assert len(extent_images) == len(intent_images)
            assert len(intent_images) == intent_count_from_bits(r, m, x)
    print('VERIFY_OK', len(results), 'exact weighted exhaustive cases')
    for row in results:
        if (row[0],row[1],row[2]) in ((2,2,'1/2'),(3,3,'1/2'),(4,4,'1/2')):
            print('E',*row)

if __name__ == '__main__':
    run()
