#!/usr/bin/env python3
"""Exhaustive exact four-bit-word hitting sets via an eight-vertex overlap digraph."""
import itertools
import json
from collections import Counter

BITS = 4
N = 1 << (1 << BITS)


def maximal_avoider_length(set_mask):
    # A four-bit factor labels an edge from its three-bit prefix to suffix.
    adj = [[] for _ in range(8)]
    indegree = [0] * 8
    for factor in range(16):
        if not (set_mask >> factor) & 1:
            u, v = factor >> 1, factor & 7
            adj[u].append(v)
            indegree[v] += 1
    queue = [u for u in range(8) if indegree[u] == 0]
    order = []
    for u in queue:
        order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    if len(order) < 8:
        return None  # A directed cycle supplies arbitrarily long avoiding words.
    longest_edges = [0] * 8
    for u in order:
        for v in adj[u]:
            longest_edges[v] = max(longest_edges[v], longest_edges[u] + 1)
    return 3 + max(longest_edges)


def necklace_classes():
    found = set()
    groups = []
    for word in range(16):
        if word in found:
            continue
        group = sorted({((word << r) | (word >> (4 - r))) & 15
                        for r in range(4)})
        found.update(group)
        groups.append(group)
    return groups


def main():
    longest = [maximal_avoider_length(s) for s in range(N)]
    optimum = {}
    witness = {}
    for length in range(4, 12):
        good = [s for s, mx in enumerate(longest)
                if mx is not None and mx < length]
        cardinality = min(s.bit_count() for s in good)
        winners = [s for s in good if s.bit_count() == cardinality]
        optimum[length] = (cardinality, len(winners))
        witness[length] = min(winners)
    expected = {4: (16, 1), 5: (10, 2), 6: (9, 50),
                7: (7, 8), 8: (7, 52), 9: (6, 10),
                10: (6, 14), 11: (6, 30)}
    assert optimum == expected, (optimum, expected)
    groups = necklace_classes()
    assert sorted(map(len, groups)) == [1, 1, 2, 4, 4, 4]
    signatures = Counter()
    min_sets = {}
    for choice in itertools.product(*groups):
        s = sum(1 << t for t in choice)
        signatures[longest[s]] += 1
        if longest[s] is not None:
            min_sets[s] = longest[s]
    assert signatures == {None: 98, 8: 10, 9: 4, 10: 16}, signatures
    assert len(min_sets) == 30
    assert sum(s.bit_count() == 6 and longest[s] is not None
               for s in range(N)) == 30
    print(json.dumps({
        'check': 'PASS', 'enumerated_subsets': N,
        'optimal_profiles': {str(l): list(c) for l, c in optimum.items()},
        'necklace_sizes': list(map(len, groups)),
        'six_transversal_max_avoider_histogram':
            {str(k): v for k, v in signatures.items()},
        'six_sets_with_finite_avoider': len(min_sets),
        'witness_masks_hex': {str(l): f'{s:04x}' for l, s in witness.items()}
    }, sort_keys=True))

if __name__ == '__main__':
    main()
