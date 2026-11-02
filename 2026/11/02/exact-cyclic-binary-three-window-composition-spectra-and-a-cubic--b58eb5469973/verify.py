#!/usr/bin/env python3
"""Independent finite tests for cyclic binary three-window composition spectra."""
from itertools import product


def spectrum(word):
    n = len(word)
    out = [0, 0, 0, 0]
    for i in range(n):
        out[word[i] + word[(i + 1) % n] + word[(i + 2) % n]] += 1
    return tuple(out)


def predicted(n):
    if n < 3:
        raise ValueError('Only lengths at least three are covered')
    ans = {(n, 0, 0, 0), (0, 0, 0, n)}
    for c1 in range(n + 1):
        for c2 in range(n - c1 + 1):
            if (c1 - c2) % 3 or not (c1 or c2):
                continue
            r = n - c1 - c2
            for c0 in range(r + 1):
                c3 = r - c0
                if (c0 == 0 or c1 >= 2) and (c3 == 0 or c2 >= 2):
                    ans.add((c0, c1, c2, c3))
    return ans


def witness(counts):
    c0, c1, c2, c3 = counts
    n = sum(counts)
    if c1 + c2 == 0:
        assert (c0 == n and c3 == 0) or (c3 == n and c0 == 0)
        return (0,) * n if c0 else (1,) * n
    a = (2 * c1 + c2) // 3
    b = (c1 + 2 * c2) // 3
    t = (max(a, b) + 1) // 2
    assert t <= min(a - (c0 > 0), b - (c3 > 0))
    ua, ub = 2 * t - a, 2 * t - b
    def lengths(singleton, count0):
        result = [1] * singleton + [2] * (t - singleton)
        if count0:
            assert len(result) > singleton
            result[singleton] += count0
        return result
    aa = lengths(ua, c0)
    bb = lengths(ub, c3)
    word = []
    for p, q in zip(aa, bb):
        word.extend([0] * p + [1] * q)
    assert len(word) == n and spectrum(word) == counts
    return tuple(word)


def closed_formula(n):
    if n % 3 == 0:
        return (n ** 3 - 6 * n ** 2 + 39 * n - 18) // 18
    if n % 3 == 1:
        return ((n - 1) * (n ** 2 - 5 * n + 34)) // 18
    return (n ** 3 - 6 * n ** 2 + 39 * n - 26) // 18


def run():
    checked = 0
    for n in range(3, 19):
        actual = set()
        for bits in product((0, 1), repeat=n):
            actual.add(spectrum(bits))
            checked += 1
        target = predicted(n)
        assert actual == target, (n, sorted(actual ^ target)[:10])
        assert len(actual) == closed_formula(n), (n, len(actual), closed_formula(n))
    print('EXHAUSTIVE_OK lengths=3..18 words=', checked)
    profiles = 0
    for n in range(3, 46):
        expected = predicted(n)
        assert len(expected) == closed_formula(n)
        for p in expected:
            assert spectrum(witness(p)) == p
            profiles += 1
    print('CONSTRUCTIONS_OK n=3..45 profiles=', profiles)


if __name__ == '__main__':
    run()
