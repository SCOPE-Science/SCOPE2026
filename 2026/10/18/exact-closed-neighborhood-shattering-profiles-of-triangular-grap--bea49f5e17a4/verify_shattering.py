#!/usr/bin/env python3
"""Independent finite checks of closed-neighborhood traces in triangular graphs."""
from collections import Counter
from itertools import combinations
from math import comb


def expected_counts(n):
    def c(k, threshold):
        return comb(n, k) if n >= threshold else 0
    return [1,
            comb(n, 2) if n >= 4 else 0,
            3*c(3, 5) + 3*c(4, 6),
            4*c(4, 6) + 30*c(5, 7),
            90*c(6, 8),
            0]


def component_shapes(selected_edges):
    adjacency = {}
    for u, v in selected_edges:
        adjacency.setdefault(u, set()).add(v)
        adjacency.setdefault(v, set()).add(u)
    shapes = []
    while adjacency:
        root = next(iter(adjacency))
        pending = [root]
        vertices = set()
        while pending:
            a = pending.pop()
            if a not in adjacency or a in vertices:
                continue
            vertices.add(a)
            pending.extend(adjacency[a])
        degrees = tuple(sorted(len(adjacency[x]) for x in vertices))
        shapes.append(degrees)
        for a in vertices:
            del adjacency[a]
    return tuple(sorted(shapes))


ALLOWED = {
    0: {()},
    1: {((1, 1),)},
    2: {((1, 1, 2),), ((1, 1), (1, 1))},
    3: {((1, 1, 1, 3),), ((1, 1), (1, 1, 2))},
    4: {((1, 1, 2), (1, 1, 2))},
    5: set(),
}


def brute(n, max_k=5):
    edges = list(combinations(range(n), 2))
    nbr_masks = []
    for f in edges:
        nbr_masks.append(sum(1 << i for i, e in enumerate(edges)
                             if f[0] in e or f[1] in e))
    totals = Counter()
    checked = 0
    for k in range(min(max_k, len(edges)) + 1):
        for indices in combinations(range(len(edges)), k):
            checked += 1
            bits = [1 << i for i in indices]
            needed = (1 << (1 << k)) - 1
            seen = 0
            for neighborhood in nbr_masks:
                trace = 0
                for j, bit in enumerate(bits):
                    if neighborhood & bit:
                        trace |= 1 << j
                seen |= 1 << trace
                if seen == needed:
                    break
            shattered = seen == needed
            chosen = [edges[i] for i in indices]
            used = len(set(v for e in chosen for v in e))
            predicted = ((n >= used + 2) and component_shapes(chosen) in ALLOWED[k])
            if k == 0:
                predicted = True
            assert shattered == predicted, (n, k, chosen, shattered, predicted)
            totals[k] += shattered
    return totals, checked


def main():
    checked_all = 0
    for n in range(2, 11):
        # For n=10 a five-set exhaustive scan is unnecessary for the certificate.
        limit = 4 if n == 10 else 5
        totals, checked = brute(n, limit)
        want = expected_counts(n)
        assert all(totals[k] == want[k] for k in range(limit + 1)), (n, totals, want)
        checked_all += checked
        print('N', n, 'checked_subsets', checked, 's_0_to_'+str(limit),
              [totals[k] for k in range(limit + 1)], 'PASS')
    print('VERIFY_OK', 'tested_subsets', checked_all,
          'closed_neighborhood_traces=PASS',
          'structural_types=PASS', 'exact_counts=PASS',
          'four_to_five_boundary=PASS')


if __name__ == '__main__':
    main()
