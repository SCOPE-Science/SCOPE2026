#!/usr/bin/env python3
"""Recompute the exact triadic 2-binomial Cantor-word weight spectrum.

No third-party libraries are used.  The finite tests supplement a proof
valid for arbitrary nonnegative levels.
"""
from collections import defaultdict


def cantor_positions(k):
    p = [0]
    for j in range(k):
        p = p + [x + 2 * 3**j for x in p]
    return p


def exact_spectrum(k):
    n = 3**k
    p = cantor_positions(k)
    m = 2**k
    spectrum = {0: 1, m: 1}
    overlap = {}
    u = 0
    for w in range(1, m):
        u += p[w - 1]
        a, b = p[w - 1] + 1, p[w]
        numerator = (n + 1) * w + 2 * u
        intersection = 0
        if numerator % w == 0:
            c = numerator // w
            intersection = max(0, min(b, c - a) - max(a, c - b) + 1)
        assert 0 <= intersection <= b - a + 1
        spectrum[w] = 2 * (b - a + 1) - intersection
        if intersection:
            overlap[w] = intersection
    return spectrum, overlap


def cantor_block(k):
    b = bytearray([1])
    for _ in range(k):
        b = bytearray(y for x in b for y in ((1, 0, 1) if x else (0, 0, 0)))
    return b


def two_arms(k):
    n = 3**k
    b = cantor_block(k)
    families = defaultdict(set)
    families[0].add(0)
    for t in range(n + 1):
        prefix = b[:t]
        weight = sum(prefix)
        moment = sum(i * x for i, x in enumerate(prefix))
        s = (n - t) * weight + moment
        families[weight].add(s)
        families[weight].add(weight * (n - 1) - s)
    return families


def checked_prefix_factors(k):
    n = 3**k
    word = cantor_block(k + 3)
    weight = sum(word[:n])
    moment = sum(i * word[i] for i in range(n))
    profiles = defaultdict(set)
    profiles[weight].add(moment)
    for i in range(len(word) - n):
        old, new = word[i], word[i + n]
        moment += -weight + old + (n - 1) * new
        weight += new - old
        profiles[weight].add(moment)
    return profiles


def main():
    expected = (2, 5, 17, 50, 154, 466, 1402, 4210, 12634, 37906, 113722, 341170)
    for k in range(12):
        spectrum, overlap = exact_spectrum(k)
        count = sum(spectrum.values())
        assert count == expected[k], (k, count, expected[k])
        assert set(spectrum) == set(range(2**k + 1))
        if k <= 7:
            arm = two_arms(k)
            finite = checked_prefix_factors(k)
            assert {w: len(s) for w, s in arm.items()} == spectrum
            assert finite == arm, k
        if k <= 4:
            print(f'k={k}, n={3**k}, classes={count}, overlaps={overlap}')
    print('VERIFY_OK: exact arithmetic k=0..11; two-arm / rolling-window sets k=0..7')


if __name__ == '__main__':
    main()
