#!/usr/bin/env python3
"""Independent finite checks of circular and conjugate square formulas for Zimin words."""
from collections import Counter


def recursive_zimin(n):
    w = (1,)
    for letter in range(2, n + 1):
        w = w + (letter,) + w
    return w


def ruler_zimin(n):
    return tuple((i & -i).bit_length() for i in range(1, 1 << n))


def cyclic_squares(w):
    size = len(w)
    twice = w + w
    return {(start, period)
            for period in range(1, size // 2 + 1)
            for start in range(size)
            if twice[start:start + period] == twice[start + period:start + 2 * period]}


def direct_linear_squares(w):
    size = len(w)
    return sum(w[start:start + period] == w[start + period:start + 2 * period]
               for period in range(1, size // 2 + 1)
               for start in range(size - 2 * period + 1))


def expected_squares(n):
    size = (1 << n) - 1
    return {(size - ((1 << k) - 1), (1 << k) - 1) for k in range(1, n)}


def predicted_hist(n):
    if n == 1:
        return {0: 1}
    return {0: 1, **{k: (1 << (k + 1)) for k in range(1, n - 1)}, n - 1: 2}


def check():
    direct_square_count = 0
    direct_rotation_count = 0
    for n in range(1, 12):
        w = recursive_zimin(n)
        assert w == ruler_zimin(n), n
        assert len(w) == (1 << n) - 1
        sq = cyclic_squares(w)
        assert sq == expected_squares(n), (n, sq ^ expected_squares(n))
        direct_square_count += len(sq)
        size = len(w)
        doubled = w + w
        for start, period in sq:
            assert 2 * period <= size
            assert doubled[start:start + period] == doubled[start + period:start + 2 * period]
            # No square extends to a circular power of exponent greater than 2.
            if 2 * period < size:
                assert doubled[start] != doubled[start + 2 * period]
        if n <= 8:
            hist = Counter()
            for shift in range(size):
                rotated = w[shift:] + w[:shift]
                hist[direct_linear_squares(rotated)] += 1
                direct_rotation_count += 1
            assert dict(hist) == predicted_hist(n), (n, hist, predicted_hist(n))
    print('VERIFY_OK cyclic_square_levels=1..11'
          f' cyclic_square_occurrences={direct_square_count}'
          f' independently_scanned_conjugates_levels=1..8_count={direct_rotation_count}'
          ' linear_square_histogram_exact=1..8'
          ' no_proper_circular_power_above_exponent_2=1..11'
          ' recursive_equals_ruler=1..11')

if __name__ == '__main__':
    check()
