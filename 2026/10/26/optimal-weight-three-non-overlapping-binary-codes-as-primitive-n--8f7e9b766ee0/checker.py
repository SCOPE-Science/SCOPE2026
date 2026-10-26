"""Independent finite checks for weight-three non-overlapping binary codes.

The all-length theorem is established by its mathematical proof, not by this script.
Uses only the Python standard library.
"""
from itertools import combinations
from math import comb


def construction(n):
    assert n >= 4
    h = (n + 2) // 3
    for j in range(n - h, n - 1):
        for i in range(h - 1, j):
            if i < 1:
                continue
            word = ['0'] * n
            for z in (i, j, n - 1):
                word[z] = '1'
            yield ''.join(word)


def is_nonoverlapping(code):
    words = list(code)
    n = len(words[0])
    for u in words:
        assert len(u) == n and u.count('1') == 3
        for v in words:
            for t in range(1, n):
                if u[:t] == v[-t:]:
                    return False, (u, v, t)
    return True, None


def rotate(word, shift):
    return word[shift:] + word[:shift]


def orbit(s):
    return {rotate(s, k) for k in range(len(s))}


def weight_three_words(n):
    for indices in combinations(range(n), 3):
        word = ['0'] * n
        for i in indices:
            word[i] = '1'
        yield ''.join(word)


def expected(n):
    return (n - 1) * (n - 2) // 6


def check_small(n):
    code = list(construction(n))
    assert len(code) == len(set(code)) == expected(n), n
    ok, clash = is_nonoverlapping(code)
    assert ok, (n, clash)
    selected_orbits = set().union(*(orbit(c) for c in code))
    assert len(selected_orbits) == n * len(code)
    primitive = {s for s in weight_three_words(n) if len(orbit(s)) == n}
    assert selected_orbits == primitive, (n, len(selected_orbits), len(primitive))
    periodic_count = comb(n, 3) - len(primitive)
    assert periodic_count == (n // 3 if n % 3 == 0 else 0)
    return (n, len(code), len(primitive), periodic_count)


def check_general_count(n):
    h = (n + 2) // 3
    formula = (h - 1) * (2 * n - 3 * h) // 2
    assert formula == expected(n)
    return True


if __name__ == '__main__':
    for n in range(4, 17):
        print('n / code / primitive words / periodic words:', *check_small(n))
    for n in range(4, 100001):
        check_general_count(n)
    print('PASS: exhaustive word and overlap checks through n=16; arithmetic count n=4..100000')
