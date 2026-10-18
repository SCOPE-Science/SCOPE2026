#!/usr/bin/env python3
"""Finite, independent checks for a dyadic valuation lattice language.

Only Python's standard library is required. Exhaustive checks below concern
small windows; the all-size result uses the separate analytical proof.
"""
from itertools import product


def valuation2(z):
    if z == 0:
        return 10**7
    z = abs(z)
    return (z & -z).bit_length() - 1


def expected(n, m):
    if n == m:
        return 5 * 4 ** (n - 1)
    return 2 ** (n + m + 1) - 4 ** min(n, m)


def exact_shift_count(n, m):
    rows, cols = 2 ** n, 2 ** m
    level = 2 ** max(n, m)
    patterns = set()
    for x, y in product(range(level), repeat=2):
        for hole_bit in (0, 1):
            bits = bytearray()
            for i in range(rows):
                for j in range(cols):
                    xx, yy = (x + i) % level, (y + j) % level
                    if xx == 0 and yy == 0:
                        bits.append(hole_bit)
                    else:
                        bits.append(min(valuation2(xx), valuation2(yy)) % 2)
            patterns.add(bytes(bits))
    return len(patterns)


def truncated_words(k):
    words = set()
    modulus = 2 ** (k + 2)
    for t in range(1, k + 4):
        for a in range(modulus):
            words.add(bytes(min(valuation2(a + j), t) % 2
                            for j in range(2 ** k)))
    return words


def main():
    comparisons = 0
    for n in range(1, 6):
        for m in range(1, 6):
            assert exact_shift_count(n, m) == expected(n, m), (n, m)
            comparisons += 1
    expected_first = {b'\x00\x00', b'\x00\x01', b'\x01\x00'}
    assert truncated_words(1) == expected_first
    assert truncated_words(2) == {
        bytes(int(c) for c in s)
        for s in ('0001', '0010', '0100', '0101', '1000', '1010')
    }
    for k in range(2, 7):
        assert len(truncated_words(k)) == 2 ** (k + 1) - 2
        comparisons += 1
    for n in range(2, 14):
        for m in range(2, 14):
            assert expected(n, m) == 4 * expected(n - 1, m - 1)
            comparisons += 1
    print('PASS:', comparisons, 'finite pattern/count/recurrence checks;')
    print('       all-parameter assertion established in RESULT.md, not by enumeration.')


if __name__ == '__main__':
    main()
