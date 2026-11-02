#!/usr/bin/env python3
"""Exact polynomial expansion and constructive checks for length-three symmetric non-overlap codes."""
from itertools import product
from math import comb


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def polypow(p, k):
    out = [1]
    for _ in range(k):
        out = multiply(out, p)
    return out


def spectrum(h):
    if h < 1:
        raise ValueError('h must be positive')
    degree = h * h * (h - 1) // 2
    out = [0] * (degree + 1)
    for a in range(h + 1):
        orbits_from_unused_letters = polypow([1, 1], a * a * (h - a))
        # 2 (1+y)^a - 1
        arc_choices = [1] + [2 * comb(a, j) for j in range(1, a + 1)]
        orbit_choices = polypow(arc_choices, comb(a, 2))
        p = multiply(orbits_from_unused_letters, orbit_choices)
        weight = (-1) ** (h - a) * comb(h, a) * (2 ** a)
        for j, x in enumerate(p):
            out[j] += weight * x
    assert min(out) >= 0
    return out  # coefficient index j counts 2j codewords


def maximal_code(h):
    # Complement swaps 0<->1, 2<->3, etc. Take A={0,2,...}.
    a = list(range(0, 2 * h, 2))
    code = set()
    for i in range(h):
        for j in range(i + 1, h):
            v, z = a[i], a[j]
            for u in a:
                code.add((u, v, z ^ 1))
                code.add((z, v ^ 1, u ^ 1))
    return code


def valid(C):
    def rc(w):
        return tuple(x ^ 1 for x in w[::-1])
    if set(map(rc, C)) != C:
        return False
    prefixes = {w[:k] for w in C for k in (1, 2)}
    suffixes = {w[-k:] for w in C for k in (1, 2)}
    return not (prefixes & suffixes)


def main():
    expected = {
        1: [1],
        2: [1, 12, 8],
        3: [1, 60, 726, 3072, 6276, 7344, 5256, 2304, 576, 64],
    }
    for h in range(1, 10):
        p = spectrum(h)
        assert p[-1] == (1 if h == 1 else 2 ** (h + comb(h, 2)))
        if h in expected:
            assert p == expected[h], (h, p)
        C = maximal_code(h)
        assert valid(C), h
        assert len(C) == h * h * (h - 1), (h, len(C))
        assert len(p) - 1 == len(C) // 2
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
