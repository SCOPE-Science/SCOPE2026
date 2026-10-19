#!/usr/bin/env python3
"""Exhaustive finite check of Abelian-square counts in double-occurrence words.

Independent of the asymptotic argument. Uses only the standard library.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def double_factorial_odd(n):
    result = 1
    for x in range(1, n + 1, 2):
        result *= x
    return result


def normalized_words(q):
    """Enumerate pairings, assigning labels in order of first occurrence."""
    word = [-1] * (2 * q)

    def visit(open_positions, next_label):
        if not open_positions:
            yield tuple(word)
            return
        i = open_positions[0]
        for idx in range(1, len(open_positions)):
            j = open_positions[idx]
            word[i] = word[j] = next_label
            yield from visit(open_positions[1:idx] + open_positions[idx + 1:], next_label + 1)
        word[i] = -1

    yield from visit(tuple(range(2 * q)), 0)


def abelian_squares_by_half_length(word):
    n = len(word)
    output = [0] * (n // 2 + 1)
    for k in range(1, n // 2 + 1):
        for start in range(n - 2 * k + 1):
            left = Counter(word[start:start + k])
            right = Counter(word[start + k:start + 2 * k])
            if left == right:
                output[k] += 1
    return output


def check(q):
    n = double_factorial_odd(2 * q - 1)
    hist = Counter()
    moments = [0] * (q + 1)
    by_length = [0] * (q + 1)
    free = 0
    actual = 0
    for word in normalized_words(q):
        actual += 1
        squared = abelian_squares_by_half_length(word)
        adjacent = sum(word[i] == word[i + 1] for i in range(2 * q - 1))
        assert adjacent == squared[1], (q, word)
        if sum(squared[1:]) == 0:
            free += 1
        for k in range(1, q + 1):
            by_length[k] += squared[k]
        hist[adjacent] += 1
        for r in range(q + 1):
            if r <= adjacent:
                moments[r] += comb(adjacent, r)
    assert actual == n, ('pairing count', q, actual, n)
    for k in range(1, q + 1):
        expected = Fraction(
            factorial(k) * double_factorial_odd(2 * q - 2 * k + 1),
            double_factorial_odd(2 * q - 1),
        )
        assert Fraction(by_length[k], n) == expected, ('length mean', q, k)
    for r in range(q + 1):
        expected = Fraction(comb(2 * q - r, r), 1)
        for j in range(r):
            expected /= (2 * q - 2 * j - 1)
        assert Fraction(moments[r], n) == expected, ('binomial moment', q, r)
    exact_no_adjacent = sum(
        (-1)**r * Fraction(
            comb(2 * q - r, r) * double_factorial_odd(2 * q - 2 * r - 1),
            n,
        )
        for r in range(q + 1)
    )
    assert Fraction(hist[0], n) == exact_no_adjacent, ('inclusion exclusion', q)
    return free, hist


def main():
    reference = (0, 0, 1, 15, 195, 2630, 38519)
    total = 0
    for q in range(1, 8):
        no_square, hist = check(q)
        assert no_square == reference[q - 1], ('free count', q, no_square)
        total += double_factorial_odd(2 * q - 1)
        print('q=', q, 'matching_count=', double_factorial_odd(2 * q - 1),
              'Abelian_square_free=', no_square, 'adjacent_histogram=', sorted(hist.items()))
    assert total == 146599
    print('DOUBLE_OCCURRENCE_ABELIAN_POISSON_FINITE_PASS matchings=', total)


if __name__ == '__main__':
    main()
