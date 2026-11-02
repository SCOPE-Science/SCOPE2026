#!/usr/bin/env python3
"""Exact finite tests for joint excluded-middle / double-negation probabilities.

This checker enumerates all transitively closed relations consistent with a
fixed linear extension on up to six vertices, computes the Heyting operations
on all order ideals, and verifies the stated counting and sharpness assertions.
The infinite statements in RESULT.md have independent structural proofs.
"""
from itertools import combinations


def poset_from_upper_mask(n, bits):
    pairs = list(combinations(range(n), 2))
    down = [1 << i for i in range(n)]
    for k, (i, j) in enumerate(pairs):
        if bits & (1 << k):
            down[j] |= 1 << i
    for j in range(n):
        for i in range(j):
            if down[j] & (1 << i):
                if down[i] & ~down[j]:
                    return None
    return down


def ideals(down):
    n = len(down)
    return [s for s in range(1 << n) if all(not s & (1 << j) or down[j] & s == down[j] for j in range(n))]


def negation(s, down):
    return sum(1 << j for j, d in enumerate(down) if not (d & s))


def component_minima(down):
    n = len(down)
    p = list(range(n))

    def root(x):
        while p[x] != x:
            x = p[x]
        return x

    for j, d in enumerate(down):
        for i in range(n):
            if i != j and d & (1 << i):
                p[root(j)] = root(i)
    c = len({root(i) for i in range(n)})
    m = sum(d.bit_count() == 1 for d in down)
    return c, m


def star_with_top_chain(t, r):
    # t incomparable minima and r ordered vertices above all of them
    assert t >= 2 and r >= 1
    down = [1 << i for i in range(t)]
    for j in range(r):
        down.append(((1 << t) - 1) | (((1 << (j + 1)) - 1) << t))
    return down


def is_equality_shape(down):
    # The unique nontrivial component is one top over t>=2 minima;
    # all other elements are isolated.
    n = len(down)
    nonminimal = [j for j, d in enumerate(down) if d.bit_count() > 1]
    if len(nonminimal) != 1:
        return False
    top = nonminimal[0]
    support = down[top]
    if support.bit_count() < 3:
        return False
    return all(down[j] == (1 << j) for j in range(n) if j != top)


def audit_poset(down):
    n = len(down)
    universe = (1 << n) - 1
    J = ideals(down)
    center = 0
    regular = 0
    for s in J:
        ns = negation(s, down)
        nns = negation(ns, down)
        assert ns in J and nns in J
        if s | ns == universe:
            center += 1
        if nns == s:
            regular += 1
    c, m = component_minima(down)
    assert center == 2 ** c, (down, center, c)
    assert regular == 2 ** m, (down, regular, m)
    k = m - c
    assert k >= 0
    assert regular == 2 ** k * center
    if k > 0:
        assert len(J) >= (2 ** (c - 1)) * (2 ** (k + 1) + 1)
        sharp = len(J) == (2 ** (c - 1)) * (2 ** (k + 1) + 1)
        assert sharp == is_equality_shape(down), (down, k, sharp)
    return k, len(J), center, regular


def main():
    total = 0
    eq_counts = {}
    for n in range(1, 7):
        good = 0
        for bits in range(1 << (n * (n - 1) // 2)):
            down = poset_from_upper_mask(n, bits)
            if down is None:
                continue
            k, size, center, regular = audit_poset(down)
            good += 1
            total += 1
            if k > 0 and size == (center // 2) * (2 ** (k + 1) + 1):
                eq_counts[k] = eq_counts.get(k, 0) + 1
        print(f'NATURAL_POSETS_PASS n={n} count={good}')
    assert total == 5231, total
    for t in range(2, 6):
        for r in range(1, 5):
            down = star_with_top_chain(t, r)
            k, size, center, regular = audit_poset(down)
            assert k == t - 1 and center == 2 and regular == 2 ** t
            assert size == 2 ** t + r
            assert (size == 2 ** t + 1) == is_equality_shape(down)
            print(f'CONNECTED_SPECTRUM_PASS minima={t} ideals={size} pair=2/{size},{2**t}/{size}')
    print(f'JOINT_HEYTING_ALL_CHECKS_PASS enumerated={total} equality_counts={eq_counts}')


if __name__ == '__main__':
    main()
