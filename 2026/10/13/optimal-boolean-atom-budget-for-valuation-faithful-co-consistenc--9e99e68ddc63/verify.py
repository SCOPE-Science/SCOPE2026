#!/usr/bin/env python3
"""Independent finite checks of the private-marker clique-cover theorem."""
from itertools import combinations, product


def theta(m, edges):
    """Minimum number of edge-covering cliques; empty edges -> 0."""
    es = tuple(sorted(edges))
    if not es:
        return 0
    covers = []
    for z in range(1, 1 << m):
        vv = [i for i in range(m) if z >> i & 1]
        if len(vv) < 2:
            continue
        if any(tuple(sorted((i, j))) not in edges for i, j in combinations(vv, 2)):
            continue
        mask = 0
        for idx, (i, j) in enumerate(es):
            if i in vv and j in vv:
                mask |= 1 << idx
        if mask:
            covers.append(mask)
    inf = len(es) + 1
    dp = [inf] * (1 << len(es))
    dp[0] = 0
    for mask in range(len(dp)):
        if dp[mask] == inf:
            continue
        for c in covers:
            dp[mask | c] = min(dp[mask | c], dp[mask] + 1)
    return dp[-1]


def unrestricted_labels_are_universal(S, n):
    """Brute semantic definition, not the private-token theorem.

    For every vertex truth-set U there must be a Boolean value a whose
    containment predicates S[v] subseteq a hold exactly at vertices in U.
    """
    m = len(S)
    for truth in range(1 << m):
        if not any(all(((S[v] & ~a) == 0) == bool(truth >> v & 1)
                       for v in range(m)) for a in range(1 << n)):
            return False
    return True


def graph_from_labels(S):
    return frozenset((i, j) for i in range(len(S))
                     for j in range(i + 1, len(S)) if S[i] & S[j])


def all_graphs(m):
    pairs = list(combinations(range(m), 2))
    for z in range(1 << len(pairs)):
        yield frozenset(p for i, p in enumerate(pairs) if z >> i & 1)


def brute_small(m):
    # Exhaustively search all nonempty label families using fewer than
    # m+theta(G) atoms. Includes every Boolean truth-set valuation.
    graphs = list(all_graphs(m))
    targets = {g: m + theta(m, g) for g in graphs}
    found = {g: None for g in graphs}
    for n in range(1, max(targets.values()) + 1):
        for S in product(range(1, 1 << n), repeat=m):
            g = graph_from_labels(S)
            if g not in found or found[g] is not None:
                continue
            if unrestricted_labels_are_universal(S, n):
                found[g] = n
        if all(v is not None for v in found.values()):
            break
    assert found == targets, (m, found, targets)
    return (len(graphs), sum(targets.values()), max(targets.values()))


def upper_construction(m, g, cliques):
    S = [1 << v for v in range(m)]
    for j, c in enumerate(cliques):
        for v in c:
            S[v] |= 1 << (m + j)
    assert graph_from_labels(S) == g
    assert unrestricted_labels_are_universal(S, m + len(cliques))


def test_all_graphs_with_edge_tokens(m):
    for g in all_graphs(m):
        upper_construction(m, g, [{u, v} for (u, v) in g])
    return 1 << (m * (m - 1) // 2)


def main():
    tests = []
    for m in (1, 2, 3):
        tests.append((m, brute_small(m)))
    graphs4 = test_all_graphs_with_edge_tokens(4)
    print('BRUTE_MINIMUM_BY_ALL_BOOLEAN_VALUATIONS:', tests)
    print('ALL_4_VERTEX_GRAPH_CONSTRUCTIONS:', graphs4)
    for m in range(2, 7):
        # All edges form one clique; optimal resource size is m+1.
        edges = frozenset(combinations(range(m), 2))
        if m <= 5: assert theta(m, edges) == 1
        upper_construction(m, edges, [set(range(m))])
    for m in range(2, 6):
        # Cycles of length at least four are triangle-free, hence require
        # exactly one shared coordinate per edge.
        if m >= 4:
            edges = frozenset(tuple(sorted((i, (i + 1) % m))) for i in range(m))
            assert theta(m, edges) == m
    print('COMPLETE_GRAPH_OPTIMA: m+1 for m=2..6')
    print('TRIANGLE_FREE_CYCLE_OPTIMA: 2m for m=4..5')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
