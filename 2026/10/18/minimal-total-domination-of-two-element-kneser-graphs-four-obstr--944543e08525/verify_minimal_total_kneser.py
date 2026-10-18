#!/usr/bin/env python3
"""Independent finite checks for minimal total domination of KG(n,2).

No third-party dependencies.  Direct graph-neighborhood testing is distinct from
both the vertex-cover reduction and the structural enumeration in the proof.
"""
from collections import Counter
from itertools import combinations
from math import comb


def predicted(n):
    choose = lambda k: comb(n, k) if n >= k else 0
    return {3: 15 * choose(6), 4: 10 * choose(5),
            5: 12 * choose(5), 6: choose(4)}


def direct_counts(n):
    base_edges = tuple(combinations(range(n), 2))
    size = len(base_edges)
    # In KG(n,2), adjacency is edge-disjointness in K_n.
    neighborhoods = []
    for e in base_edges:
        mask = 0
        for j, f in enumerate(base_edges):
            if not (set(e) & set(f)):
                mask |= 1 << j
        neighborhoods.append(mask)

    def totally_dominates(mask):
        return all(mask & adjacent for adjacent in neighborhoods)

    found = Counter()
    for mask in range(1, 1 << size):
        if not totally_dominates(mask):
            continue
        if all(not totally_dominates(mask ^ (1 << j))
               for j in range(size) if mask & (1 << j)):
            found[mask.bit_count()] += 1

    expected = {k: v for k, v in predicted(n).items() if v}
    assert dict(found) == expected, (n, found, expected)
    return size, dict(sorted(found.items()))


def threshold_checks():
    # Coefficient tests are on the full sequence, with leading zero coefficients.
    for n in range(4, 81):
        p = predicted(n)
        entries = [0, 0, 0] + [p[k] for k in (3, 4, 5, 6)]
        log_concave = all(entries[j] ** 2 >= entries[j-1] * entries[j+1]
                          for j in range(1, len(entries)-1))
        unimodal = any(all(entries[j] <= entries[j+1] for j in range(t))
                       and all(entries[j] >= entries[j+1]
                               for j in range(t, len(entries)-1))
                       for t in range(len(entries)))
        assert log_concave == (n <= 8), (n, 'log-concavity')
        assert unimodal == (n <= 9), (n, 'unimodality')


if __name__ == '__main__':
    total_examined = 0
    for order in range(4, 8):
        count, spectrum = direct_counts(order)
        total_examined += (1 << count) - 1
        print(f'n={order} KG_vertices={count} minimal_total_sets={spectrum}')
    threshold_checks()
    print(f'VERIFICATION_OK nonempty_examined={total_examined} orders=4..7 threshold_orders=4..80')
