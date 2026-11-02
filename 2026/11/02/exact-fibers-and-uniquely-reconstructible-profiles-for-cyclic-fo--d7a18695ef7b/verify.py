#!/usr/bin/env python3
"""Finite cross-checks for cyclic 4-gram read profiles with forbidden cyclic 11.

Run: python3 verify.py. Uses only Python's standard library.
The infinite assertions are proved in RESULT.md, not by this finite check.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial, gcd

GRAMS = ('0000', '0001', '0010', '0100', '0101', '1000', '1001', '1010')


def canon(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def admissible(word):
    return '11' not in word + word[:1]


def profile(word):
    length = len(word)
    seen = Counter(''.join(word[(i+j) % length] for j in range(4))
                   for i in range(length))
    assert not any(('11' in gram) for gram in seen)
    return tuple(seen[gram] for gram in GRAMS)


def totient(d):
    return sum(gcd(t, d) == 1 for t in range(1, d+1))


def multiplicity(a, b, g, e):
    if b == 0:
        if a > 0:
            return int(g == 0 and e == 0)
        t = g + e
        if t == 0:
            return 0
        return sum(totient(d) * comb(t//d, g//d)
                   for d in range(1, t+1)
                   if g % d == e % d == 0 and t % d == 0) // t
    t = b + g + e
    total = 0
    for d in range(1, t+1):
        if any(v % d for v in (a, b, g, e)):
            continue
        types = factorial(t//d) // (
            factorial(b//d) * factorial(g//d) * factorial(e//d))
        extras = comb(a//d + b//d-1, b//d-1)
        total += totient(d) * types * extras
    assert total % t == 0
    return total // t


def is_singleton(a, b, g, e):
    if b == 0:
        return (a > 0 and g == e == 0) or (
            a == 0 and g+e > 0 and min(g, e) <= 1)
    if b == 1:
        return g == 0 or e == 0
    if a == 0:
        return (g == 0 and e <= 1) or (e == 0 and g <= 1)
    return a == 1 and g == e == 0


def attainable(n):
    for a in range(n+1):
        for b in range(n//4+1):
            for g in range(n//3+1):
                rem = n-a-4*b-3*g
                if rem < 0 or rem % 2:
                    continue
                e = rem//2
                if b > 0 or (a == 0 and g+e > 0) or (
                        a > 0 and b == g == e == 0):
                    yield a, b, g, e


def counts(n):
    items = list(attainable(n))
    return len(items), sum(is_singleton(*v) for v in items)


def series_counts(limit):
    # Coefficients of the four positive formal-power-series summands
    # making up the profile generating function, without symbolic software.
    c = [0] * (limit+1)
    s = [0] * (limit+1)
    for n in range(1, limit+1):
        c[n] = sum(1 for _ in attainable(n))
        s[n] = sum(is_singleton(*v) for v in attainable(n))
    return c, s


def test():
    brute_necklaces = 0
    checked_profiles = 0
    first_ambiguous = None
    c, s = series_counts(60)
    for n in range(1, 21):
        indexed = {}
        for letters in product('01', repeat=n):
            word = ''.join(letters)
            if admissible(word):
                indexed[canon(word)] = profile(word)
        by_profile = Counter(indexed.values())
        brute_necklaces += len(indexed)
        checked_profiles += len(by_profile)
        assert len(by_profile) == c[n], ('capacity', n)
        assert sum(v == 1 for v in by_profile.values()) == s[n], ('singleton', n)
        assert sum(by_profile.values()) == len(indexed)
        for observed, frequency in by_profile.items():
            a, b, c1, c2, e, f, g, h = observed
            assert b == f and c1 == c2 == b+g and e == h
            assert a+4*b+3*g+2*e == n
            assert multiplicity(a, b, g, e) == frequency, ('multiplicity', n, observed)
            assert is_singleton(a, b, g, e) == (frequency == 1)
            if frequency != 1 and first_ambiguous is None:
                first_ambiguous = n
    assert first_ambiguous == 9
    assert (c[9], s[9]) == (9, 8)
    assert (c[12], s[12]) == (19, 11)
    assert (c[20], s[20]) == (69, 18)
    # The divisor formula is compared with actual orbits, not merely with
    # the generating functions, for all permitted profiles up to length 20.
    print('VERIFY_OK exhaustive_lengths=1..20',
          'necklaces=', brute_necklaces, 'profiles=', checked_profiles,
          'formal_coefficients=1..60', 'first_ambiguous=9',
          'n20=(69,18)')


if __name__ == '__main__':
    test()
