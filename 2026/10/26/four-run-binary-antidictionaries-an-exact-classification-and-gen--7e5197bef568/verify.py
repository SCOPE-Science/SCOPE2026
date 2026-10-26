#!/usr/bin/env python3
"""Finite cross-checks for the four-run minimal-absent-factor theorem.

This is a reproducibility check, not a substitute for the all-parameter proof.
"""
from itertools import product


def direct_maws(text):
    factors = {""}
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            factors.add(text[i:j])
    return {x + middle + y for middle in factors for x, y in product('01', repeat=2)
            if x + middle in factors and middle + y in factors
            and x + middle + y not in factors}


def listed_maws(a, b, c, d):
    assert min(a, b, c, d) >= 1
    result = {'0' * (max(a, c) + 1), '1' * (max(b, d) + 1)}
    result.update('0' + '1' * j + '0' for j in range(1, b))
    result.update('1' + '0' * j + '1' for j in range(1, c))
    if a > c:
        result.add('1' + '0' * (c + 1))
    if d > b:
        result.add('1' * (b + 1) + '0')
    if a < c and b > d:
        result.add('0' * (a + 1) + '1' * (d + 1))
    if a > c and d > b:
        result.add('0' * (c + 1) + '1' * (b + 1))
    if c > a and d >= b:
        result.add('0' * (a + 1) + '1' * b + '0')
    if a >= c and b > d:
        result.add('1' + '0' * c + '1' * (d + 1))
    if a >= c and d >= b:
        result.add('1' + '0' * c + '1' * b + '0')
    return result


def exact_count(a, b, c, d):
    return b + c + (1 + (a > c)) * (1 + (d > b))


def compositions4(n):
    for a in range(1, n - 2):
        for b in range(1, n - a - 1):
            for c in range(1, n - a - b):
                yield a, b, c, n - a - b - c


def main():
    cases = 0
    for a, b, c, d in product(range(1, 9), repeat=4):
        word = '0' * a + '1' * b + '0' * c + '1' * d
        measured = direct_maws(word)
        predicted = listed_maws(a, b, c, d)
        assert measured == predicted, (a, b, c, d, measured ^ predicted)
        assert len(predicted) == exact_count(a, b, c, d)
        cases += 1
    check_count = 0
    for n in range(4, 22):
        m = max(exact_count(*p) for p in compositions4(n))
        assert m == (n if n == 6 else n - 1), (n, m)
        check_count += 1
    # Verify the bivariate generating formula via its exact pairwise factorization.
    # F_0 represents pairs (a,c) with a<=c; F_1 pairs with a>c,
    # and analogously the second pair (d,b).
    actual = {}
    for n in range(4, 18):
        for a, b, c, d in compositions4(n):
            key = (n, exact_count(a, b, c, d))
            actual[key] = actual.get(key, 0) + 1
    predicted = {}
    for q, r, extra in ((0, 0, 1), (0, 1, 2), (1, 0, 2), (1, 1, 4)):
        for a in range(1, 18):
            for c in range(1, 18):
                if (a > c) != bool(q):
                    continue
                for d in range(1, 18):
                    for b in range(1, 18):
                        n = a + b + c + d
                        if n >= 18 or (d > b) != bool(r):
                            continue
                        key = (n, b + c + extra)
                        predicted[key] = predicted.get(key, 0) + 1
    assert actual == predicted
    print('VERIFY_OK: exact minimal-absent sets on', cases,
          'parameter quadruples; sharp maxima at', check_count,
          'lengths; full bivariate counts through length 17')


if __name__ == '__main__':
    main()
