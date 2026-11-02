#!/usr/bin/env python3
"""Independent finite checks for three-square exceptions among binary partitions."""
from collections import Counter
from fractions import Fraction

GAPS = (6, 8, 10, 16, 18, 24)
WEIGHTS = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 16),
           Fraction(3, 16), Fraction(3, 16), Fraction(1, 16))


def tm(n):
    return -1 if n.bit_count() % 2 else 1


def chi(n):
    if not n:
        return False
    valuation = (n & -n).bit_length() - 1
    if not valuation % 2:
        return False
    odd = n >> valuation
    return odd % 4 == 1 and tm((odd - 1) // 4) == -1


def type_block(n):
    offsets = tuple(r for r in range(16) if chi(16 * n + r))
    a = chi(n)
    t = (1 - tm(n)) // 2
    expected = ((0, 10) if a else (10,) if t == 0
                else (2, 8) if n % 2 == 0 else (2,))
    assert offsets == expected, (n, offsets, expected)
    return ('A' if a else 'B' if t == 0 else 'C' if n % 2 == 0 else 'D')


def no_three_squares(m):
    while m and m % 4 == 0:
        m //= 4
    return m % 8 == 7


def main():
    # Recompute b(m) by an unrelated integer recurrence.
    limit = 12000
    b = [0] * (2 * limit + 1)
    b[0] = 1
    for n in range(1, len(b)):
        b[n] = b[n - 1] + (b[n // 2] if n % 2 == 0 else 0)
    for n in range(limit):
        assert chi(n) == no_three_squares(b[2 * n]), n
        assert chi(2 * n + 1) is False
        assert chi(4 * n) == chi(n)
        assert chi(8 * n + 2) == (tm(n) == -1)
        assert chi(8 * n + 6) is False
    nblocks = 1 << 16
    blocks = [type_block(i) for i in range(nblocks + 1)]
    transitions = Counter(zip(blocks, blocks[1:]))
    allowed = {('A', 'D'), ('B', 'D'), ('B', 'A'), ('B', 'B'),
               ('B', 'C'), ('C', 'B'), ('D', 'C'), ('D', 'B')}
    assert set(transitions) == allowed, transitions
    f = [n for n in range(16 * nblocks + 1) if chi(n)]
    gapcounts = Counter(y - x for x, y in zip(f, f[1:]))
    assert set(gapcounts) == set(GAPS)
    assert sum(gapcounts.values()) == len(f) - 1
    # Compare all finite-prefix counts with their exact limiting predictions.
    for cutoff in (1 << e for e in range(8, 17)):
        ff = [n for n in f if n < cutoff]
        actual = Counter(y - x for x, y in zip(ff, ff[1:]))
        for g, w in zip(GAPS, WEIGHTS):
            assert abs(Fraction(actual[g]) - w * sum(actual.values())) < 160
    mean = sum(Fraction(g) * w for g, w in zip(GAPS, WEIGHTS))
    variance = sum(Fraction(g * g) * w for g, w in zip(GAPS, WEIGHTS)) - mean * mean
    assert (mean, variance) == (12, 32)
    print('VERIFY_OK')
    print('direct_binary_partition_three_square_checks=', limit)
    print('block_pattern_checks=', nblocks + 1)
    print('gap_count_total=', sum(gapcounts.values()))
    print('gap_counts=', [(g, gapcounts[g]) for g in GAPS])
    print('transitions=', sorted(((a, b, v) for (a, b), v in transitions.items())))
    print('mean=', mean, 'variance=', variance)
    print('finite_checks_do_not_replace_infinite_proof=true')


if __name__ == '__main__':
    main()
