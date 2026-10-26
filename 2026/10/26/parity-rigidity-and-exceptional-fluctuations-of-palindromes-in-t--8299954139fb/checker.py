#!/usr/bin/env python3
"""Finite checks for circular palindromic-factor counts of two-marker words.

Run: python3 checker.py
No external dependencies or data files are required.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def direct_palindromes(w):
    n = len(w)
    doubled = w + w
    return {
        doubled[i:i + k]
        for i in range(n)
        for k in range(1, n + 1)
        if doubled[i:i + k] == doubled[i:i + k][::-1]
    }


def predicted_count(a, b):
    assert a >= 0 and b >= 0
    z = max(a, b)
    one = min(a, b) + 1
    two = (a // 2 + 1) if a == b else (a // 2 + b // 2 + 2)
    return z + one + two


def predicted_spectrum(n):
    assert n >= 2
    if n & 1:
        return {(3 * n - 1) // 2: (n - 1) // 2}
    m = n // 2
    a = m // 2
    b = (m + 1) // 2 - 1
    d = m // 2 + 1
    h = 3 * m
    ell = h - d
    result = Counter()
    result[h] += a
    result[h - 1] += b
    result[ell] += 1
    return {k: v for k, v in result.items() if v}


def predicted_linear_distribution(n):
    assert n >= 2
    if n & 1:
        return {(3 * n - 1) // 2: comb(n, 2)}
    m = n // 2
    A = m // 2
    B = (m + 1) // 2 - 1
    D = m // 2 + 1
    H = 3 * m
    answer = Counter()
    answer[H] += n * A
    answer[H - 1] += n * B
    answer[H - D] += n // 2
    return {k: v for k, v in answer.items() if v}


def predicted_moments(n):
    counts = predicted_linear_distribution(n)
    total = comb(n, 2)
    mu = Fraction(sum(k * v for k, v in counts.items()), total)
    var = Fraction(sum(v * k * k for k, v in counts.items()), total) - mu * mu
    return mu, var


def check():
    gap_tests = 0
    for n in range(2, 56):
        for a in range(n - 1):
            b = n - 2 - a
            word = '1' + '0' * a + '1' + '0' * b
            got = len(direct_palindromes(word))
            target = predicted_count(a, b)
            assert got == target, ('factor count', n, a, b, got, target)
            gap_tests += 1

    distribution_tests = 0
    for n in range(2, 46):
        necklace_dist = Counter()
        for a in range((n - 2) // 2 + 1):
            b = n - 2 - a
            necklace_dist[predicted_count(a, b)] += 1
        assert dict(necklace_dist) == predicted_spectrum(n), ('necklaces', n)
        word_dist = Counter()
        for i in range(n):
            for j in range(i + 1, n):
                a = j - i - 1
                b = n - j + i - 1
                word_dist[predicted_count(a, b)] += 1
        assert dict(word_dist) == predicted_linear_distribution(n), ('linear', n)
        exact_mean = Fraction(sum(c * k for k, c in word_dist.items()), comb(n, 2))
        exact_second = Fraction(sum(c * k * k for k, c in word_dist.items()), comb(n, 2))
        mu, variance = predicted_moments(n)
        assert mu == exact_mean and variance == exact_second - mu * mu
        distribution_tests += 1

    for n in (57, 88, 139, 200, 301):
        for a in (0, 1, 2, (n - 2) // 2, n - 2):
            b = n - 2 - a
            got = len(direct_palindromes('1' + '0' * a + '1' + '0' * b))
            assert got == predicted_count(a, b), ('large', n, a, b)

    print('PASS: direct distinct-palindrome comparisons:', gap_tests + 25)
    print('PASS: exact necklace and labeled-word distributions:', distribution_tests)
    print('PASS: exact first/second moments:', distribution_tests)
    print('PASS: all stated formulas and parity boundaries.')


if __name__ == '__main__':
    check()
