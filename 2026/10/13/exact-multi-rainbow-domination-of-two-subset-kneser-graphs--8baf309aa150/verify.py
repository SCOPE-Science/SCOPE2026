#!/usr/bin/env python3
"""Independent finite checks of rainbow-domination constructions and small boundaries.

Vertex labels are subsets of the color palette, represented as integer bit masks.
All computations use only the Python standard library.
"""
from itertools import combinations
from math import comb


def vertices(n):
    return list(combinations(range(n), 2))


def neighbors(n):
    es = vertices(n)
    return [tuple(j for j, f in enumerate(es) if set(e).isdisjoint(f))
            for e in es]


def rainbow_valid(n, k, labels):
    assert len(labels) == comb(n, 2)
    full = (1 << k) - 1
    if any(t < 0 or t > full for t in labels):
        return False
    for i, adj in enumerate(neighbors(n)):
        if labels[i]:
            continue
        union = 0
        for j in adj:
            union |= labels[j]
        if union != full:
            return False
    return True


def general_witness(n, k):
    assert k >= 3 and n >= 4
    groups = [0, 0, 0]
    for c in range(k):
        groups[c % 3] |= 1 << c
    matching_index = {
        frozenset(((0, 1), (2, 3))): 0,
        frozenset(((0, 2), (1, 3))): 1,
        frozenset(((0, 3), (1, 2))): 2,
    }
    color_of_edge = {}
    for pair, c in matching_index.items():
        for e in pair:
            color_of_edge[e] = groups[c]
    return [color_of_edge.get(e, 0) for e in vertices(n)]


def exhaustive_reject_below(n, k, target):
    es = vertices(n)
    adj = neighbors(n)
    # Positions correspond to independent color incidences (e,c).
    width = len(es) * k
    target_full = (1 << k) - 1
    tested = 0
    for weight in range(target):
        for chosen in combinations(range(width), weight):
            tested += 1
            labels = [0] * len(es)
            for bit in chosen:
                e, c = divmod(bit, k)
                labels[e] |= 1 << c
            # This loop deliberately uses adjacency, not the structural theorem.
            good = True
            for i, mask in enumerate(labels):
                if mask:
                    continue
                got = 0
                for j in adj[i]:
                    got |= labels[j]
                if got != target_full:
                    good = False
                    break
            if good:
                raise AssertionError((n, k, target, chosen))
    expected = sum(comb(width, j) for j in range(target))
    assert tested == expected
    return tested


def main():
    total_constructed = 0
    for n in range(4, 16):
        for k in range(3, n):
            labels = general_witness(n, k)
            assert rainbow_valid(n, k, labels)
            assert sum(x.bit_count() for x in labels) == 2 * k
            total_constructed += 1
    checked = 0
    for n, k, minimum in [(4, 3, 6), (5, 3, 6)]:
        count = exhaustive_reject_below(n, k, minimum)
        print(f'exhaustive {n=} {k=} minimum={minimum} rejected_below={count}')
        checked += count
    print(f'construction_checks={total_constructed} exhaustive_rejected={checked}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
