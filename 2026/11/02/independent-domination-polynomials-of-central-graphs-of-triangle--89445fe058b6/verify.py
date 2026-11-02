#!/usr/bin/env python3
"""Independent verification of the independent-domination polynomial."""
from itertools import combinations
from collections import Counter


def predicted(n, edges):
    m = len(edges)
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    return Counter([m] + [m - deg[v] + 1 for v in range(n)]
                   + [m - deg[u] - deg[v] + 3 for u, v in edges])


def direct(n, edges):
    m = len(edges)
    total = n + m
    neighbors = [0] * total
    original_edges = set(edges)
    for u, v in combinations(range(n), 2):
        if (u, v) not in original_edges:
            neighbors[u] |= 1 << v
            neighbors[v] |= 1 << u
    for k, (u, v) in enumerate(edges):
        s = n + k
        neighbors[s] |= (1 << u) | (1 << v)
        neighbors[u] |= 1 << s
        neighbors[v] |= 1 << s
    output = Counter()
    for chosen in range(1 << total):
        if any(chosen & (1 << v) and chosen & neighbors[v]
               for v in range(total)):
            continue
        if any(not (chosen & (1 << v) or chosen & neighbors[v])
               for v in range(total)):
            continue
        output[chosen.bit_count()] += 1
    return output


def triangle_free(n, edges):
    E = set(edges)
    return all(not ((a,b) in E and (b,c) in E and (a,c) in E)
               for a,b,c in combinations(range(n), 3))


def small_graph_census():
    checked = 0
    for n in range(4, 7):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [edge for j, edge in enumerate(possible) if mask >> j & 1]
            if any(sum(v in e for e in edges) < 2 for v in range(n)):
                continue
            if not triangle_free(n, edges):
                continue
            expected = predicted(n, edges)
            actual = direct(n, edges)
            assert expected == actual, (n, edges, expected, actual)
            assert sum(expected.values()) == 1 + n + len(edges)
            checked += 1
    assert checked == 560, checked
    print("LABELED_TRIANGLE_FREE_MIN_DEGREE_TWO_OK", checked)


def degree_sequence_examples():
    E1 = [(0,1),(0,3),(0,5),(1,2),(2,3),(3,4),(4,5)]
    E2 = [(0,1),(0,4),(0,5),(1,2),(2,3),(3,4),(3,5)]
    P1 = Counter({7: 1, 6: 6, 5: 6, 4: 1})
    P2 = Counter({7: 1, 6: 5, 5: 8})
    assert predicted(6, E1) == direct(6, E1) == P1
    assert predicted(6, E2) == direct(6, E2) == P2
    assert min(P1) == 4 and P1[4] == 1
    assert min(P2) == 5 and P2[5] == 8
    print("SAME_DEGREE_DIFFERENT_POLYNOMIAL_EXAMPLES_OK")


if __name__ == "__main__":
    small_graph_census()
    degree_sequence_examples()
    print("VERIFY_OK")
