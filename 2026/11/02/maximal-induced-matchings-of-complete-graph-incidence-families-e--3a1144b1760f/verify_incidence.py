"""Direct graph-level checks of maximal induced matching formulas.
Run: python3 verify_incidence.py
No external dependencies are required.
"""
from collections import Counter
from math import comb, factorial


def stirling(n, k):
    if n == k == 0:
        return 1
    if n < 1 or k < 1 or k > n:
        return 0
    values = [[0] * (k + 1) for _ in range(n + 1)]
    values[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            values[i][j] = values[i - 1][j - 1] + j * values[i - 1][j]
    return values[n][k]


def predicted_bipartite(a, b):
    output = Counter()
    output[a] += b ** a
    output[b] += a ** b
    for p in range(1, a):
        for q in range(1, b):
            term = (comb(a, p) * comb(b, q)
                    * factorial(b - q) * stirling(p, b - q)
                    * factorial(a - p) * stirling(q, a - p))
            output[p + q] += term
    return {k: v for k, v in sorted(output.items()) if v}


def predicted_complete(n):
    return {k: comb(n, k) * factorial(n-k) * stirling(k, n-k)
            for k in range(1, n) if stirling(k, n-k)}


def incidence_edges(N, original_edges):
    """Adjacencies of the incidence graph, constructed from scratch."""
    adjacency = [set() for _ in range(N + len(original_edges))]
    edge_list = []
    for index, (u, v) in enumerate(original_edges):
        w = N + index
        for x in (u, v):
            adjacency[x].add(w)
            adjacency[w].add(x)
            edge_list.append((x, w))
    return adjacency, edge_list


def graph_level_enumeration(adjacency, edges):
    """Enumerate all independent edge subsets using the actual graph adjacency.
    Reject any set that is not inclusion-maximal in the graph.
    """
    E = len(edges)
    clash = []
    for i, (u, v) in enumerate(edges):
        conflicts = 0
        for j, (x, y) in enumerate(edges):
            if i == j or x == u or x == v or y == u or y == v \
                    or x in adjacency[u] or y in adjacency[u] \
                    or x in adjacency[v] or y in adjacency[v]:
                conflicts |= 1 << j
        clash.append(conflicts)
    all_mask = (1 << E) - 1
    result = Counter()
    tested = 0

    def extend(remaining, covered, size):
        nonlocal tested
        tested += 1
        if covered == all_mask:
            result[size] += 1
        candidates = remaining
        while candidates:
            bit = candidates & -candidates
            i = bit.bit_length() - 1
            candidates ^= bit
            extend(candidates & ~clash[i], covered | clash[i], size + 1)
    extend(all_mask, 0, 0)
    return dict(sorted(result.items())), tested


def check_bipartite(a, b):
    original_edges = [(i, a + j) for i in range(a) for j in range(b)]
    adj, edges = incidence_edges(a + b, original_edges)
    actual, calls = graph_level_enumeration(adj, edges)
    wanted = predicted_bipartite(a, b)
    assert actual == wanted, ('K_a,b', a, b, actual, wanted)
    return calls


def check_complete(n):
    original_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    adj, edges = incidence_edges(n, original_edges)
    actual, calls = graph_level_enumeration(adj, edges)
    wanted = predicted_complete(n)
    assert actual == wanted, ('K_n', n, actual, wanted)
    return calls


def main():
    total = 0
    cases = 0
    for a in range(1, 6):
        for b in range(a, 7):
            if a * b > 25:
                continue
            total += check_bipartite(a, b)
            cases += 1
    for n in range(2, 8):
        total += check_complete(n)
        cases += 1
    for a in range(2, 9):
        for b in range(a, 11):
            p = predicted_bipartite(a, b)
            expected = {a} | set(range(b, a + b - 1))
            assert set(p) == expected, (a, b, p, expected)
    for n in range(2, 12):
        assert set(predicted_complete(n)) == set(range((n + 1) // 2, n))
    print('VERIFY_OK', 'graph_instances=' + str(cases),
          'induced_matching_recursions=' + str(total),
          'support_checks=' + str(9 + sum(11 - a for a in range(2, 9))))
    print('EXAMPLES', 'K_2,5=' + str(predicted_bipartite(2, 5)),
          'K_3,3=' + str(predicted_bipartite(3, 3)),
          'K_4=' + str(predicted_complete(4)))

if __name__ == '__main__':
    main()
