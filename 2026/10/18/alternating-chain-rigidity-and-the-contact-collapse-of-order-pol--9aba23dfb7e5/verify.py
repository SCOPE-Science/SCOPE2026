#!/usr/bin/env python3
"""Finite exact checks of Euclidean minimum-width normals of poset order polytopes.

This is corroboration only. The arbitrary-size theorem is proved symbolically.
Requires Python >=3.9 and no third-party packages.
"""
from itertools import combinations, product


def all_naturally_labeled_posets(n):
    pairs = list(combinations(range(n), 2))
    seen = set()
    for m in range(1 << len(pairs)):
        gt = [0] * n
        for bit, (i, j) in enumerate(pairs):
            if m >> bit & 1:
                gt[i] |= 1 << j
        for k in reversed(range(n)):
            for j in range(k + 1, n):
                if gt[k] >> j & 1:
                    gt[k] |= gt[j]
        tup = tuple(gt)
        if tup not in seen:
            seen.add(tup)
            yield tup


def upper_sets(gt):
    n = len(gt)
    return [s for s in range(1 << n)
            if all(not (s >> i & 1) or (s & gt[i]) == gt[i]
                   for i in range(n))]


def longest_chains(gt):
    n = len(gt)
    chains = []
    for k in range(1, n + 1):
        for tup in combinations(range(n), k):
            if all(gt[tup[j]] >> tup[j + 1] & 1 for j in range(k - 1)):
                chains.append(tup)
    h = max(map(len, chains))
    return h, [c for c in chains if len(c) == h]


def width(v, upper):
    vals = [sum(vi for i, vi in enumerate(v) if s >> i & 1) for s in upper]
    return max(vals) - min(vals)


def claimed_directions(n, chains):
    target = set()
    for c in chains:
        for sg in (-1, 1):
            v = [0] * n
            for j, i in enumerate(c):
                v[i] = sg * (-1) ** j
            target.add(tuple(v))
    return target


def run():
    total_posets = 0
    total_comparisons = 0
    total_normals = 0
    for n in range(1, 6):
        count = 0
        for gt in all_naturally_labeled_posets(n):
            U = upper_sets(gt)
            h, C = longest_chains(gt)
            expected = claimed_directions(n, C)
            # Exact support profile on the signed longest-chain normals.
            for chain in C:
                for signs in product((-1, 1), repeat=h):
                    v = [0] * n
                    for i, sign in zip(chain, signs):
                        v[i] = sign
                    walk = [0]
                    for sign in reversed(signs):
                        walk.append(walk[-1] + sign)
                    expected_span = max(walk) - min(walk)
                    assert width(v, U) == expected_span, (gt, chain, signs)
                    assert (expected_span == 1) == all(
                        signs[j] != signs[j + 1] for j in range(h - 1)
                    )
            actual = set()
            for v in product((-1, 0, 1), repeat=n):
                if not any(v):
                    continue
                W = width(v, U)
                sq = sum(x * x for x in v)
                assert h * W * W >= sq, (gt, v, h, W)
                if h * W * W == sq:
                    actual.add(v)
                total_comparisons += 1
            assert actual == expected, (gt, actual, expected)
            assert len(expected) == 2 * len(C)
            total_normals += len(expected)
            count += 1
        print(f'n={n}: {count} naturally labeled posets verified')
        total_posets += count
    print(f'PASS: {total_posets} posets, {total_comparisons} directional checks, '
          f'{total_normals} shortest-unit-direction witnesses')


if __name__ == '__main__':
    run()
