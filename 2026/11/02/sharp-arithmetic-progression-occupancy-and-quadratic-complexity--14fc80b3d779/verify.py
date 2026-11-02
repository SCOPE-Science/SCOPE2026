"""Finite stress tests of power-indicator arithmetic-progression factors.

The infinite theorem is proved in RESULT.md; these tests are corroborative only.
"""
from math import gcd
from itertools import combinations


def geom_sum(base, count):
    assert count >= 1
    return (base ** (count - 1) - 1) // (base - 1)


def envelope(base, length):
    r = 1
    while geom_sum(base, r + 1) < length:
        r += 1
    return r


def power_mark(base, index):
    x = index + 1
    while x % base == 0:
        x //= base
    return x == 1


def pattern(base, start, step, length):
    return ''.join('1' if power_mark(base, start + j * step) else '0'
                   for j in range(length))


def polynomial_bound(base, length):
    from math import comb
    if length == 1:
        return 2
    L = 0
    while base ** (L + 1) <= length - 1:
        L += 1
    return 1 + length + comb(length, 2) + sum(
        (j + base ** f - 1) // (base ** f)
        for f in range(1, L + 1)
        for j in range(1, length))


checks = 0
for base in range(2, 7):
    for length in range(1, 31):
        r = envelope(base, length)
        assert geom_sum(base, r) < length <= geom_sum(base, r + 1)
        witness = pattern(base, 0, base - 1, length)
        assert witness.count('1') == r
        checks += 3
        if length == geom_sum(base, r) + 1:
            expected = ''.join('1' if j in {geom_sum(base, t) for t in range(1, r + 1)} else '0'
                               for j in range(length))
            assert witness == expected
            checks += 1

for base in range(2, 6):
    for length in range(1, 24):
        words = set()
        top_words = set()
        r = envelope(base, length)
        for start in range(0, 130):
            for step in range(1, 54):
                w = pattern(base, start, step, length)
                words.add(w)
                assert w.count('1') <= r
                checks += 1
                if w.count('1') == r:
                    top_words.add(w)
        assert len(words) <= polynomial_bound(base, length)
        checks += 1
        if length == geom_sum(base, r) + 1:
            expected = pattern(base, 0, base - 1, length)
            assert top_words == {expected}
            checks += 1

for base in range(2, 9):
    for exps in combinations(range(0, 12), 3):
        a, b, c = exps
        g = gcd(b - a, c - a)
        exact_gcd = gcd(base ** b - base ** a,
                        base ** c - base ** a)
        assert exact_gcd == base ** a * (base ** g - 1)
        span = (base ** c - base ** a) // exact_gcd
        assert span >= geom_sum(base, 3)
        assert span >= base ** (b - a)
        checks += 3

print(f'VERIFY_OK {checks} assertions; finite tests only')
