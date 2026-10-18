#!/usr/bin/env python3
"""Exhaustive finite checks for length-four reverse-complement site collisions."""
from collections import Counter
from fractions import Fraction
from itertools import product

def transform(source, index):
    block = source[index:index + 4]
    return source[:index + 4] + tuple((a ^ 1) for a in reversed(block)) + source[index + 4:]

def local_count(q, displacement):
    return q if displacement in (1, 3) else q * q

def pair_probability(q, displacement):
    return Fraction(local_count(q, displacement), q ** (displacement + 4))

def expected_pairs(q, n):
    return sum(((n - 3 - d) * pair_probability(q, d)
                for d in range(1, n - 3)), Fraction(0))

def check_local():
    for q, maximum in ((2, 10), (4, 5)):
        for d in range(1, maximum + 1):
            count = sum(transform(x, 0) == transform(x, d)
                        for x in product(range(q), repeat=d + 4))
            assert count == local_count(q, d), (q, d, count)

def check_global():
    for n in range(4, 13):
        total = 0
        for w in product((0, 1), repeat=n):
            descendants = [transform(w, i) for i in range(n - 3)]
            counts = Counter(descendants)
            total += sum(m * (m - 1) // 2 for m in counts.values())
        observed = Fraction(total, 2 ** n)
        predicted = expected_pairs(2, n)
        assert observed == predicted, (n, observed, predicted)

if __name__ == "__main__":
    check_local()
    check_global()
    print("PAIR_SPECTRUM_RC4_PASS")
