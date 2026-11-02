#!/usr/bin/env python3
"""Direct finite checks for the binary Pascal-row two-sum theorem."""
from collections import Counter
from math import comb


def support(n):
    return [k for k in range(n + 1) if (n & k) == k]


def runs(n):
    sizes = []
    shift = 0
    while n:
        if not n & 1:
            n >>= 1
            shift += 1
            continue
        length = 0
        while n & 1:
            n >>= 1
            length += 1
        sizes.append((shift, length))
        shift += length
    return sizes


def predicted_distribution(n):
    accum = {0: 1}
    for h, ell in runs(n):
        m = 1 << ell
        next_accum = {}
        for total, ways in accum.items():
            for digit in range(2 * m - 1):
                multiplicity = min(digit + 1, 2 * m - 1 - digit)
                k = total + (digit << h)
                assert k not in next_accum, ('nonunique digit representation', n, k)
                next_accum[k] = ways * multiplicity
        accum = next_accum
    return accum


def formula_energy(n):
    value = 1
    for _, ell in runs(n):
        value *= (2 * (8 ** ell) + 2 ** ell) // 3
    return value


def verify():
    parity_tests = 0
    polynomial_tests = 0
    energy_tests = 0
    for n in range(256):
        a = support(n)
        for k in range(n + 1):
            assert ((comb(n, k) & 1) == (k in a)), ('Lucas check', n, k)
            parity_tests += 1
        actual = Counter(x + y for x in a for y in a)
        predicted = predicted_distribution(n)
        assert actual == predicted, ('full convolution spectrum', n)
        polynomial_tests += 1
        assert sum(v*v for v in actual.values()) == formula_energy(n), ('energy', n)
        energy_tests += 1

    total = 0
    f_prev2, f_prev1 = 1, 7
    recurrence_tests = 0
    row_count = 0
    for n in range(1 << 11):
        total += formula_energy(n)
        row_count += 1
        if n + 1 == 1 << ((n + 1).bit_length() - 1):
            r = (n + 1).bit_length() - 1
            if r == 0:
                expected = 1
            elif r == 1:
                expected = 7
            else:
                expected = 11 * f_prev1 - 20 * f_prev2
                f_prev2, f_prev1 = f_prev1, expected
            assert total == expected, ('aggregate', r, total, expected)
            recurrence_tests += 1
    print('PASS Lucas parity identities:', parity_tests)
    print('PASS exact two-sum multiplicity profiles:', polynomial_tests)
    print('PASS row-energy products:', energy_tests)
    print('PASS dyadic aggregate recurrence:', recurrence_tests, 'levels,', row_count, 'rows')
    print('Final dyadic sum:', total)


if __name__ == '__main__':
    verify()
