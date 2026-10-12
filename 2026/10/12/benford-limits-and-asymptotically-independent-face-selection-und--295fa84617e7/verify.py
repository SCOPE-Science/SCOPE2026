"""Exact finite cross-checks of the subset-product gap in RESULT.md.

Standard-library arithmetic only. Enumeration is not an infinite proof.
"""
from itertools import combinations, product
from fractions import Fraction
from math import comb


def check_case(scores, d):
    m = len(scores)
    ranked = sorted(range(m), key=lambda i: (-scores[i], i))
    winners = frozenset(ranked[:d])
    g = scores[ranked[d - 1]] - scores[ranked[d]] if d < m else None
    maximum = 2 ** sum(scores[i] for i in winners)
    sum_products = 0
    for indices in combinations(range(m), d):
        value = 2 ** sum(scores[i] for i in indices)
        sum_products += value
        if frozenset(indices) != winners and g is not None:
            assert Fraction(value, maximum) <= Fraction(1, 2 ** g)
    ratio = Fraction(sum_products, maximum)
    if d < m:
        assert ratio <= 1 + Fraction(comb(m, d) - 1, 2 ** g)
    else:
        assert ratio == 1
    return True


def main():
    count = 0
    # Distinct nonnegative exact binary logarithmic side lengths.
    for m in range(1, 7):
        for scores in combinations(range(1, 11), m):
            for d in range(1, m + 1):
                assert check_case(scores, d)
                assert check_case(tuple(reversed(scores)), d)
                count += 2
    # Tied side lengths are allowed: their gap is zero, so the inequality is non-strict.
    for m in range(2, 5):
        for scores in product((0, 1, 2), repeat=m):
            for d in range(1, m + 1):
                assert check_case(scores, d)
                count += 1
    print(f"PASS: {count} exact winner-gap and subset-product comparisons")


if __name__ == "__main__":
    main()
