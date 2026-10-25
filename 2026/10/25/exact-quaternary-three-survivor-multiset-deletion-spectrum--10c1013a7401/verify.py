#!/usr/bin/env python3
"""Independent finite checks for the four-symbol, three-survivor multiset-code theorem.

Run: python verify.py
Requires only Python 3 standard library.
"""
from itertools import combinations


def compositions(n, q=4):
    if q == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for tail in compositions(n - a, q - 1):
                yield (a,) + tail


def intersection(x, y):
    return sum(min(a, b) for a, b in zip(x, y))


def light(x):
    return max(x) <= 2


def corners(n):
    return [tuple(n if i == j else 0 for i in range(4)) for j in range(4)]


def witness(n):
    code = corners(n)
    if n == 5:
        code += [(0, 1, 2, 2), (2, 2, 0, 1)]
    elif n == 6:
        code += [(2, 2, 1, 1)]
    elif n == 7:
        code += [(2, 2, 2, 1)]
    elif n == 8:
        code += [(2, 2, 2, 2)]
    return code


def verify():
    assert sum(1 for _ in compositions(5)) == 56
    for n, expected_light, expected_compatible in [(5, 16, 12), (6, 10, 0), (7, 4, 0), (8, 1, 0), (9, 0, 0)]:
        all_words = list(compositions(n))
        small = [x for x in all_words if light(x)]
        compatible_edges = [(x, y) for x, y in combinations(small, 2) if intersection(x, y) <= 2]
        assert len(small) == expected_light, (n, len(small))
        assert len(compatible_edges) == expected_compatible, (n, len(compatible_edges))
        if n == 5:
            # No triple of light compositions can coexist in a valid code.
            assert not any(intersection(x, y) <= 2 and intersection(x, z) <= 2 and intersection(y, z) <= 2
                           for x, y, z in combinations(small, 3))
            pattern_A = (0, 1, 2, 2)
            nbrs = {y for y in small if y != pattern_A and intersection(pattern_A, y) <= 2}
            assert nbrs == {(2, 2, 0, 1), (2, 2, 1, 0)}, nbrs
            pattern_B = (2, 1, 1, 1)
            assert not any(y != pattern_B and intersection(pattern_B, y) <= 2 for y in small)
        code = witness(n)
        assert len(code) == (6 if n == 5 else 5 if n <= 8 else 4)
        assert all(len(x) == 4 and sum(x) == n and min(x) >= 0 for x in code)
        assert all(intersection(x, y) <= 2 for x, y in combinations(code, 2))
        print(f'n={n}: compositions={len(all_words)}; light={len(small)}; light_edges={len(compatible_edges)}; witness={len(code)}; OK')

    # Independent direct decoding-ball verification: every possible three-token
    # output belongs to the deletion ball of at most one codeword.
    for n in range(5, 21):
        code = witness(n)
        outputs = list(compositions(3))
        for y in outputs:
            parents = [x for x in code if all(y[i] <= x[i] for i in range(4))]
            assert len(parents) <= 1, (n, y, parents)
        assert len(code) == (6 if n == 5 else 5 if n <= 8 else 4)
    print('direct three-survivor decoding balls: n=5..20; OK')
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    verify()
