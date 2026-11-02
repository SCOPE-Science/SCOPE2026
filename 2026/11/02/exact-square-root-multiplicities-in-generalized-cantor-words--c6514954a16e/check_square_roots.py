#!/usr/bin/env python3
"""Finite checks of the generalized Cantor square-root classification.

All tested prefixes and sets are constructed independently from their explicit
string definitions. These checks illustrate the theorem; its infinite proof is
mathematical and does not depend on the tested cutoff.
"""


def substitute(word, base):
    return ''.join(('1' + '0' * (base - 2) + '1') if c == '1'
                   else '0' * base for c in word)


def prefix(base, exponent):
    value = '1'
    for _ in range(exponent):
        value = substitute(value, base)
    return value


def base_digits_indicator(n, base):
    while n:
        digit = n % base
        if digit != 0 and digit != base - 1:
            return '0'
        n //= base
    return '1'


def observed_roots(word, period):
    return {word[i:i + period]
            for i in range(len(word) - 2 * period + 1)
            if '1' in word[i:i + period]
            and word[i:i + period] == word[i + period:i + 2 * period]}


def predicted_roots(base, k):
    m = base ** k
    island = prefix(base, k)
    gap = (base - 2) * m
    return {'0' * a + island + '0' * (gap - a)
            for a in range(gap + 1)}


def check():
    cases = 0
    lengths = []
    for base in range(3, 8):
        for k in range(5):
            word = prefix(base, k + 3)
            if len(word) > 150000:
                continue
            m = base ** k
            period = (base - 1) * m
            assert len(word) >= 2 * period
            # Digit-recursion check is logically independent of the morphism.
            assert all(c == base_digits_indicator(i, base)
                       for i, c in enumerate(word))
            expected = predicted_roots(base, k)
            observed = observed_roots(word, period)
            assert observed == expected, (base, k,
                                          len(observed), len(expected),
                                          observed - expected,
                                          expected - observed)
            assert len(expected) == (base - 2) * m + 1
            assert all(len(root) == period for root in expected)
            cases += 1
            lengths.append((base, k, len(word), period, len(observed)))
    assert cases == 23, cases
    print('VERIFY_OK')
    print('CASES', cases)
    print('CHECKED', lengths)


if __name__ == '__main__':
    check()
