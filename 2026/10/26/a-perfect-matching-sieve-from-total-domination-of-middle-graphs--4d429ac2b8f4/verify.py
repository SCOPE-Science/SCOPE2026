"""Reproduce the total-domination-polynomial edge-cover identity for small graphs."""
from itertools import combinations
from math import comb
from collections import Counter


def is_connected(n, edges):
    seen = {0}
    changed = True
    while changed:
        changed = False
        for a, b in edges:
            if (a in seen) != (b in seen):
                seen.add(a)
                seen.add(b)
                changed = True
    return len(seen) == n


def polynomial_by_original_definition(n, edges):
    m = len(edges)
    adj = [0] * (n + m)
    for j, (a, b) in enumerate(edges):
        i = n + j
        adj[a] |= 1 << i
        adj[b] |= 1 << i
        adj[i] |= (1 << a) | (1 << b)
    for i, (a, b) in enumerate(edges):
        for j in range(i + 1, m):
            c, d = edges[j]
            if len({a, b, c, d}) < 4:
                adj[n + i] |= 1 << (n + j)
                adj[n + j] |= 1 << (n + i)
    out = Counter()
    for s in range(1 << (n + m)):
        if all(s & a for a in adj):
            out[s.bit_count()] += 1
    return out


def polynomial_by_edge_covers(n, edges):
    m = len(edges)
    out = Counter()
    for s in range(1 << m):
        degrees = [0] * n
        for j, (a, b) in enumerate(edges):
            if s >> j & 1:
                degrees[a] += 1
                degrees[b] += 1
        if not all(degrees):
            continue
        isolated = sum(
            (degrees[a] == 1 and degrees[b] == 1)
            for j, (a, b) in enumerate(edges)
            if s >> j & 1
        )
        # factor: z^|C| (1+z)^(n-2i) (2z+z^2)^i
        for j in range(n - 2 * isolated + 1):
            for k in range(isolated + 1):
                out[s.bit_count() + j + isolated + k] += (
                    comb(n - 2 * isolated, j) * comb(isolated, k) * 2 ** (isolated-k)
                )
    return out


def signed_edge_monomial_coefficients(n, edges):
    """Sum signs of dominating sets at each edge-selector monomial, directly."""
    m = len(edges)
    adj = [0] * (n + m)
    for j, (a, b) in enumerate(edges):
        i = n + j
        adj[a] |= 1 << i
        adj[b] |= 1 << i
        adj[i] |= (1 << a) | (1 << b)
    for i, (a, b) in enumerate(edges):
        for j in range(i + 1, m):
            c, d = edges[j]
            if len({a, b, c, d}) < 4:
                adj[n + i] |= 1 << (n + j)
                adj[n + j] |= 1 << (n + i)
    out = Counter()
    for s in range(1 << (n + m)):
        if all(s & a for a in adj):
            out[s >> n] += -1 if s.bit_count() % 2 else 1
    return {selector: weight for selector, weight in out.items() if weight}


def perfect_matching_monomials(n, edges):
    out = {}
    for s in range(1 << len(edges)):
        counts = [0] * n
        for j, (a, b) in enumerate(edges):
            if s >> j & 1:
                counts[a] += 1
                counts[b] += 1
        if all(v == 1 for v in counts):
            out[s] = 1
    return out


def number_of_perfect_matchings(n, edges):
    if n % 2:
        return 0
    partners = [set() for _ in range(n)]
    for a, b in edges:
        partners[a].add(b)
        partners[b].add(a)
    def go(remaining):
        if not remaining:
            return 1
        a = min(remaining)
        return sum(go(remaining - {a, b}) for b in partners[a] & remaining)
    return go(set(range(n)))


def check_graph(n, edges):
    direct = polynomial_by_original_definition(n, edges)
    formula = polynomial_by_edge_covers(n, edges)
    assert direct == formula, (n, edges, direct, formula)
    assert sum((-1)**k * count for k, count in direct.items()) == number_of_perfect_matchings(n, edges), (n, edges)
    assert signed_edge_monomial_coefficients(n, edges) == perfect_matching_monomials(n, edges), (n, edges)


def main():
    checked = 0
    total_candidate_sets = 0
    for n in range(2, 6):
        all_edges = list(combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            edges = [e for j, e in enumerate(all_edges) if mask >> j & 1]
            if len(edges) > 7 or not is_connected(n, edges):
                continue
            check_graph(n, edges)
            total_candidate_sets += 1 << (n + len(edges))
            checked += 1
    extra = [
        (6, [(i, (i+1) % 6) for i in range(6)]),
        (6, [(0, i) for i in range(1, 6)]),
        (6, [(i, i+1) for i in range(5)]),
        (6, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(0,3)]),
        (6, [(0,1),(0,2),(1,3),(1,4),(2,5)]),
        (7, [(i,i+1) for i in range(6)]),
    ]
    for n, edges in extra:
        check_graph(n, edges)
        checked += 1
        total_candidate_sets += 1 << (n + len(edges))
    disconnected = [
        (4, [(0,1),(2,3)]),
        (6, [(0,1),(2,3),(4,5)]),
        (6, [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5)]),
        (6, [(0,1),(1,2),(2,0),(3,4),(4,5)]),
    ]
    for n, edges in disconnected:
        check_graph(n, edges)
        checked += 1
        total_candidate_sets += 1 << (n + len(edges))
    # Boundary of the class: isolated original vertices make the polynomial identically zero.
    assert polynomial_by_original_definition(3, [(0, 1)]) == {}
    assert polynomial_by_edge_covers(3, [(0, 1)]) == {}
    print('PASS: independent direct definition versus edge-cover expansion')
    print('Connected labeled test graphs:', checked)
    print('Direct candidate vertex subsets checked:', total_candidate_sets)
    print('PASS: coefficientwise multivariate signed polynomial equals perfect-matching enumerator')
    print('PASS: evaluation at -1 equals independent perfect-matching count')
    print('Boundary test: graph with isolated vertex -> zero polynomial')
    for n, edges in [(2, [(0,1)]), (3, [(0,1),(1,2)]), (3, [(0,1),(1,2),(2,0)])]:
        print('Polynomial sample:', n, edges, sorted(polynomial_by_edge_covers(n,edges).items()))

if __name__ == '__main__':
    main()
