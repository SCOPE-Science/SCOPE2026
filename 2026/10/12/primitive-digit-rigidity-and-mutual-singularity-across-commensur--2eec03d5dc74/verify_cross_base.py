#!/usr/bin/env python3
"""Exact finite-word diagnostics for commensurable-base Bernoulli laws."""
from fractions import Fraction
from itertools import product
from math import gcd


def integer_of_word(word, base):
    ans = 0
    for a in word:
        ans = ans * base + a
    return ans


def law_of_blocks(word, weights, width, base):
    mass = Fraction(1)
    for k in range(0, len(word), width):
        mass *= weights[integer_of_word(word[k:k + width], base)]
    return mass


def product_weights(base, width, digit_weights):
    result = []
    for word in product(range(base), repeat=width):
        mass = Fraction(1)
        for a in word:
            mass *= digit_weights[a]
        result.append(mass)
    assert sum(result) == 1
    return tuple(result)


def rational_rank(rows):
    rows = [list(map(Fraction, row)) for row in rows]
    height, width = len(rows), len(rows[0])
    current = 0
    for c in range(width):
        pivot = next((r for r in range(current, height) if rows[r][c]), None)
        if pivot is None:
            continue
        rows[current], rows[pivot] = rows[pivot], rows[current]
        coeff = rows[current][c]
        for j in range(c, width):
            rows[current][j] /= coeff
        for r in range(current + 1, height):
            factor = rows[r][c]
            if factor:
                for j in range(c, width):
                    rows[r][j] -= factor * rows[current][j]
        current += 1
        if current == height:
            break
    return current


def check_combinations(base, m, n):
    assert gcd(m, n) == 1 and base >= 2
    w = tuple(Fraction(j + 1, base * (base + 1) // 2) for j in range(base))
    p = product_weights(base, m, w)
    t = product_weights(base, n, w)
    L = m * n
    total = 0
    for digits in product(range(base), repeat=L):
        assert law_of_blocks(digits, p, m, base) == law_of_blocks(digits, t, n, base)
        total += 1
    assert total == base ** L
    if m != n:
        unif_t = (Fraction(1, base ** n),) * (base ** n)
        allzero = (0,) * L
        assert law_of_blocks(allzero, p, m, base) != law_of_blocks(allzero, unif_t, n, base)
    return total


def check_two_three_rank():
    base, m, n, length = 2, 2, 3, 6
    rows = []
    for digits in product(range(base), repeat=length):
        row = [0] * (base ** m + base ** n)
        for k in range(0, length, m):
            row[integer_of_word(digits[k:k + m], base)] += 1
        for k in range(0, length, n):
            row[base ** m + integer_of_word(digits[k:k + n], base)] -= 1
        rows.append(row)
    assert rational_rank(rows) == 10
    # Twelve log-probabilities satisfy ten independent linear constraints,
    # leaving exactly two primitive digit log parameters before normalization.
    return len(rows)


def main():
    counts = [check_combinations(*spec) for spec in
              ((2, 1, 3), (2, 2, 3), (2, 3, 4), (3, 2, 3), (4, 2, 3))]
    assert check_two_three_rank() == 64
    print('EXACT_CHECKS_OK; compatible word counts:', counts,
          '; 4-versus-8 log compatibility rank: 10 of 12')
    print('NOTE: The all-length classification requires the analytic proof.')


if __name__ == '__main__':
    main()
