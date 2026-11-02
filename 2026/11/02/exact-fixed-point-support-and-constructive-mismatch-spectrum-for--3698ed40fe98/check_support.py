#!/usr/bin/env python3
"""Standalone exact checks for fixed-point-support of multiset permutations.
Uses only Python standard library; finite checks do not constitute the proof.
"""
from functools import lru_cache
from itertools import combinations
from math import factorial, prod


def compositions(n):
    for mask in range(1 << (n - 1)):
        starts = [0] + [i + 1 for i in range(n - 1) if mask & (1 << i)] + [n]
        yield tuple(starts[i + 1] - starts[i] for i in range(len(starts) - 1))


def exact_counts(a):
    n = sum(a)
    reference = tuple(i for i, m in enumerate(a) for _ in range(m))
    zero = (0,) * (n + 1)
    @lru_cache(None)
    def recurse(rem):
        pos = n - sum(rem)
        if pos == n:
            return (1,) + (0,) * n
        accum = [0] * (n + 1)
        for c, x in enumerate(rem):
            if x == 0:
                continue
            nxt = list(rem)
            nxt[c] -= 1
            sub = recurse(tuple(nxt))
            shift = int(c == reference[pos])
            for j in range(0, n + 1 - shift):
                accum[j + shift] += sub[j]
        return tuple(accum)
    return recurse(tuple(a))


def predicted_support(a):
    n = sum(a)
    k = len(a)
    if k == 1:
        return {n}
    if k == 2:
        return {n - 2 * j for j in range(min(a) + 1)}
    m = min(n, 2 * (n - max(a)))
    return {n} | {n - j for j in range(2, m + 1)}


def criterion_support(a):
    n = sum(a)
    return {n - j for j in range(n + 1)
            if j == 0 or (j >= 2 and sum(min(x, j // 2) for x in a) >= j)}


def construct(a, m):
    """Construct an arrangement with exactly m mismatches when feasible."""
    n = sum(a)
    if m == 0:
        return tuple(i for i, v in enumerate(a) for _ in range(v))
    assert m >= 2
    cap = m // 2
    assert sum(min(x, cap) for x in a) >= m
    rem = m
    d = []
    for x in a:
        v = min(rem, x, cap)
        d.append(v)
        rem -= v
    assert rem == 0
    colors = [i for i, count in enumerate(d) for _ in range(count)]
    moved = [colors[(j + cap) % m] for j in range(m)]
    assert all(colors[j] != moved[j] for j in range(m))
    out = []
    cursor = 0
    for i, x in enumerate(a):
        out.extend(moved[cursor:cursor+d[i]])
        cursor += d[i]
        out.extend([i] * (x-d[i]))
    assert len(out) == n
    assert all(out.count(i) == a[i] for i in range(len(a)))
    assert sum(out[j] != i for i, x in enumerate(a)
               for j in range(sum(a[:i]), sum(a[:i])+x)) == m
    return tuple(out)


def main():
    exact_profiles = exact_supports = constructed = 0
    # All ordered positive compositions through size 11: 2^11 - 1 = 2047 profiles.
    for n in range(1, 12):
        for a in compositions(n):
            vec = exact_counts(a)
            predicted = predicted_support(a)
            actual = {j for j in range(n + 1) if vec[j] > 0}
            assert actual == predicted == criterion_support(a), (a, actual, predicted)
            assert sum(vec) == factorial(n) // prod(factorial(x) for x in a)
            exact_profiles += 1
            exact_supports += len(actual)
            for fixed in actual:
                perm = construct(a, n - fixed)
                assert sum(perm[j] == i for i, x in enumerate(a)
                           for j in range(sum(a[:i]), sum(a[:i])+x)) == fixed
                constructed += 1
    print('exact_composition_profiles', exact_profiles)
    print('exact_positive_support_cells', exact_supports)
    print('explicit_constructions', constructed)
    print('status PASS')


if __name__ == '__main__':
    main()
