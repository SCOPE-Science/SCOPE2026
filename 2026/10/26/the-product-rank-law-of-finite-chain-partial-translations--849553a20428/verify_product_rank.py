"""Independent finite checks for the product-rank distribution of chain partial translations.

Run: python verify_product_rank.py
Only standard-library modules are used.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def transformations(n):
    out = [dict()]
    for displacement in range(1 - n, n):
        positions = [x for x in range(n) if 0 <= x + displacement < n]
        for bits in range(1, 1 << len(positions)):
            out.append({x: x + displacement for j, x in enumerate(positions)
                        if bits & (1 << j)})
    return out


def direct_product_ranks(n):
    elements = transformations(n)
    result = Counter()
    for f in elements:
        for g in elements:
            result[sum(y in g for y in f.values())] += 1
    return result


def compact_formula(n):
    assert n >= 1
    result = Counter()
    for rank in range(n + 1):
        result[rank] = comb(n, rank) * 3 ** (n - rank)
        for j in range(1, n):
            if n - j >= rank:
                coefficient = 2 ** (j + 1) * (j + 3) - 6
                result[rank] += (coefficient * comb(n - j, rank)
                                 * 3 ** (n - j - rank))
    result[0] += (4 - 8 * n) * 2 ** n + 4 * n * n + 8 * n - 4
    return result


def displacement_formula(n):
    """Separate two-displacement derivation of all coefficients."""
    result = Counter()
    for first in range(1 - n, n):
        for second in range(1 - n, n):
            first_slots = n - abs(first)
            second_slots = n - abs(second)
            width = max(0, first, first + second) - min(0, first, first + second)
            length = max(0, n - width)
            free = 2 ** (first_slots + second_slots - 2 * length)
            for rank in range(length + 1):
                result[rank] += free * comb(length, rank) * 3 ** (length - rank)
    extra_zero_labels = 2 * n - 2
    size = 3 * 2 ** n - 2 * (n + 1)
    result[0] -= 2 * extra_zero_labels * size + extra_zero_labels ** 2
    return result


def check():
    for n in range(1, 8):
        direct = direct_product_ranks(n)
        compact = compact_formula(n)
        shift = displacement_formula(n)
        assert direct == compact == shift, (n, direct, compact, shift)
        size = len(transformations(n))
        assert size == 3 * 2 ** n - 2 * (n + 1)
        assert sum(compact.values()) == size * size
        assert compact[n] == 1
        if n >= 2:
            assert compact[n - 1] == 3 * n + 10
        print('exhaustive', n, 'elements', size,
              'product_ranks', [direct[i] for i in range(n + 1)])
    for n in range(8, 41):
        compact = compact_formula(n)
        assert compact == displacement_formula(n), n
        assert sum(compact.values()) == (3 * 2 ** n - 2 * (n + 1)) ** 2
    # Exact limiting displacement moments (symmetric two-sided geometric law).
    assert 2 * sum(Fraction(j, 3 * 2 ** j) for j in range(1, 101)) < Fraction(4, 3)
    # Closed geometric-series identities give E|A|=4/3 and E|A+B|=56/27.
    assert Fraction(2, 27) * (3 * 6 + 5 * 2) == Fraction(56, 27)
    assert (2 * Fraction(4, 3) + Fraction(56, 27)) / 2 == Fraction(64, 27)
    for n in (20, 30, 40):
        counts = compact_formula(n)
        size = 3 * 2 ** n - 2 * (n + 1)
        mean = Fraction(sum(rank * count for rank, count in counts.items()), size ** 2)
        target = Fraction(n, 4) - Fraction(16, 27)
        assert abs(mean - target) < Fraction(5 * n * n, 2 ** n)
    print('VERIFY_OK_PARTIAL_TRANSLATION_PRODUCT_RANK')


if __name__ == '__main__':
    check()
