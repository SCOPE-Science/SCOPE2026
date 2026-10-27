#!/usr/bin/env python3
"""Reproduce the binary linear length-two read-multispectrum extremum.

Only Python standard library is required. The finite checks corroborate,
not replace, the all-length proof in RESULT.md.
"""
from collections import defaultdict
from itertools import product
from math import comb


def profile(word):
    c = [0, 0, 0, 0]
    for x, y in zip(word, word[1:]):
        c[2*x + y] += 1
    return tuple(c)


def count_formula(c):
    a, up, down, b = c
    if up == down == 0:
        return 2 if (a == 0 and b == 0) else int((a == 0) != (b == 0))
    if abs(up - down) > 1:
        return 0
    if up == down:
        r = up
        return ((a + b + 2*r) * comb(a + r - 1, r - 1)
                * comb(b + r - 1, r - 1)) // r
    r = max(up, down)
    return comb(a + r - 1, r - 1) * comb(b + r - 1, r - 1)


def sharp_value(n):
    if n == 1:
        return 2
    if n == 2:
        return 1
    if n % 4 == 1:
        m = (n - 1) // 4
        return comb(2*m, m)**2
    if n % 4 == 3:
        m = (n - 3) // 4
        return (4*m + 2) * comb(2*m, m)**2 // (m + 1)
    if n % 4 == 0:
        m = n // 4
        return (4*m - 1) * comb(2*m - 2, m - 1) * comb(2*m - 1, m - 1) // m
    m = (n - 2) // 4
    return ((4*m + 1) * comb(2*m - 1, m - 1)
            * comb(2*m, m - 1) // m)


def expected_max_profiles(n):
    if n < 7:
        return None
    if n % 4 == 1:
        m = (n - 1) // 4
        pairs = [(m, m, m)]
    elif n % 4 == 3:
        m = (n - 3) // 4
        pairs = [(m, m + 1, m)]
    elif n % 4 == 0:
        m = n // 4
        pairs = [(m - 1, m, m), (m, m, m - 1)]
    else:
        m = (n - 2) // 4
        pairs = [(m, m, m + 1), (m + 1, m, m),
                 (m - 1, m + 1, m), (m, m + 1, m - 1)]
    return {(a, r, r, b) for a, r, b in pairs}


def inspect_all_profiles(n):
    entries = {}
    if n == 1:
        return {(0, 0, 0, 0): 2}
    entries[(n - 1, 0, 0, 0)] = 1
    entries[(0, 0, 0, n - 1)] = 1
    for r in range(1, (n-1)//2 + 1):
        s = n - 1 - 2*r
        for a in range(s + 1):
            b = s - a
            c = (a, r, r, b)
            entries[c] = count_formula(c)
    for r in range(1, n//2 + 1):
        s = n - 2*r
        for a in range(s + 1):
            b = s - a
            for up, down in ((r, r - 1), (r - 1, r)):
                c = (a, up, down, b)
                entries[c] = count_formula(c)
    return entries


def run_checks():
    seen_words = 0
    seen_profiles = 0
    for n in range(1, 17):
        actual = defaultdict(int)
        for word in product((0, 1), repeat=n):
            actual[profile(word)] += 1
            seen_words += 1
        expected = inspect_all_profiles(n)
        assert dict(actual) == expected, (n, 'profile class sizes disagree')
        assert max(actual.values()) == sharp_value(n), (n, 'max disagrees')
        if n >= 7:
            winners = {c for c, count in actual.items() if count == sharp_value(n)}
            assert winners == expected_max_profiles(n), (n, 'maximizers disagree', winners)
        seen_profiles += len(actual)
    param_instances = 0
    for n in range(17, 201):
        f = inspect_all_profiles(n)
        assert max(f.values()) == sharp_value(n), n
        winners = {c for c, count in f.items() if count == sharp_value(n)}
        assert winners == expected_max_profiles(n), (n, 'maximizers')
        param_instances += len(f)
    print('VERIFY_OK')
    print('exhaustive_binary_words', seen_words)
    print('exhaustive_profile_instances', seen_profiles)
    print('additional_parameter_profile_instances', param_instances)
    print('checked_n_range', '1..200')
    print('M_n_1_to_16', [sharp_value(n) for n in range(1, 17)])


if __name__ == '__main__':
    run_checks()
