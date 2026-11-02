"""Independent finite checks for maximal dissociation sets of edge-subdivision graphs.

Uses only the Python standard library. All graph-level tests enumerate vertex
subsets directly; finite tests corroborate rather than prove the general theorem.
"""
from collections import Counter
from itertools import combinations, product
from math import comb
from random import Random


def edges_of_graph(n, mask):
    return [(u, v) for j, (u, v) in enumerate(combinations(range(n), 2))
            if (mask >> j) & 1]


def subdivision_adjacencies(n, edges):
    adj = [0] * (n + len(edges))
    for j, (u, v) in enumerate(edges):
        w = n + j
        adj[u] |= 1 << w
        adj[v] |= 1 << w
        adj[w] |= (1 << u) | (1 << v)
    return adj


def direct_maximal_sets(n, edges):
    """Check induced maximum degree <=1 and every one-vertex extension."""
    adj = subdivision_adjacencies(n, edges)
    N = len(adj)
    ans = set()
    for mask in range(1 << N):
        degrees = [(mask & adj[v]).bit_count() for v in range(N)]
        if any(degrees[v] > 1 for v in range(N) if mask & (1 << v)):
            continue
        can_extend = False
        for v in range(N):
            if mask & (1 << v):
                continue
            selected_neighbors = mask & adj[v]
            if selected_neighbors.bit_count() == 0:
                can_extend = True
                break
            if (selected_neighbors.bit_count() == 1 and
                    degrees[selected_neighbors.bit_length() - 1] == 0):
                can_extend = True
                break
        if not can_extend:
            ans.add(mask)
    return ans


def constructed_maximal_sets(n, edges):
    """Enumerate the proposed outside-set/partial-function characterization."""
    E = set(edges)
    answer = set()
    for orig in range(1 << n):
        A = [v for v in range(n) if orig & (1 << v)]
        C = [v for v in range(n) if not (orig & (1 << v))]
        neighbors = {a: [c for c in C if (min(a, c), max(a, c)) in E]
                     for a in A}
        boundary_A = [a for a in A if neighbors[a]]
        for target_tuple in product(*(neighbors[a] for a in boundary_A)):
            f = dict(zip(boundary_A, target_tuple))
            if any(sum(1 for x in C if x != c and
                       (min(x, c), max(x, c)) in E) < 2 and
                   c not in f.values() for c in C):
                continue
            selected_edges = 0
            for j, (u, v) in enumerate(edges):
                if ((u in C and v in C) or f.get(u) == v or f.get(v) == u):
                    selected_edges |= 1 << (n + j)
            answer.add(orig | selected_edges)
    return answer


def onto_maps(p, t):
    """Count surjections from a p-set to a t-set by inclusion-exclusion."""
    if t == 0:
        return int(p == 0)
    return sum((-1) ** j * comb(t, j) * (t - j) ** p
               for j in range(t + 1))


def complete_bipartite_edges(a, b):
    return [(u, a + v) for u in range(a) for v in range(b)]


def master_biclique_polynomial(a, b):
    """Exact coefficient sum from the all-graph structural criterion."""
    res = Counter()
    for s in range(a + 1):
        for t in range(b + 1):
            p, q = a - s, b - t
            # Selected first-shore vertices map into t outside vertices.
            Fu = 1 if t == 0 else (t ** p if s >= 2 else onto_maps(p, t))
            # Selected second-shore vertices map into s outside vertices.
            Fv = 1 if s == 0 else (s ** q if t >= 2 else onto_maps(q, s))
            count = comb(a, s) * comb(b, t) * Fu * Fv
            degree = p + q + s * t + (p if t else 0) + (q if s else 0)
            if count:
                res[degree] += count
    return +res


def four_term_polynomial(b):
    assert b >= 2
    result = Counter()
    result[b + 2] += b*b - b + 1
    result[b + 3] += b
    result[2*b] += 3**b - 2*b - 2
    result[2*b + 1] += 2*b + 2
    return +result


def complete_graph_polynomial(n):
    assert n >= 3
    P = Counter({n: 1})
    P[2*n-2] += n
    if n >= 4:
        P[2*n-3] += comb(n, 2) * (2**(n-2) - 2)
    for c in range(3, n+1):
        P[2*(n-c) + comb(c,2)] += comb(n,c)*c**(n-c)
    return +P


def check():
    cases = 0
    inspected = 0
    # Every labelled graph of order at most four.
    for n in range(1, 5):
        for edge_mask in range(1 << comb(n, 2)):
            E = edges_of_graph(n, edge_mask)
            got = direct_maximal_sets(n, E)
            want = constructed_maximal_sets(n, E)
            assert got == want, ('general', n, edge_mask)
            cases += 1
            inspected += 1 << (n + len(E))
    rng = Random(71821)
    for n, repetitions in ((5, 70), (6, 12)):
        for _ in range(repetitions):
            E = edges_of_graph(n, rng.getrandbits(comb(n, 2)))
            if n + len(E) > 19:
                continue
            assert direct_maximal_sets(n, E) == constructed_maximal_sets(n, E)
            cases += 1
            inspected += 1 << (n + len(E))
    biclique_cases = 0
    for a, bmax in ((1, 6), (2, 6), (3, 4), (4, 3)):
        for b in range(max(a,2), bmax + 1):
            E = complete_bipartite_edges(a, b)
            direct = Counter(m.bit_count() for m in direct_maximal_sets(a+b, E))
            predicted = master_biclique_polynomial(a, b)
            assert +direct == predicted, ('bipartite', a, b, direct, predicted)
            if a == 2:
                assert predicted == four_term_polynomial(b)
            biclique_cases += 1
            inspected += 1 << (a + b + len(E))
    clique_cases = 0
    for n in range(3, 6):
        E = list(combinations(range(n), 2))
        direct = Counter(m.bit_count() for m in direct_maximal_sets(n, E))
        assert +direct == complete_graph_polynomial(n), (n, direct)
        clique_cases += 1
        inspected += 1 << (n + len(E))
    for b in range(2, 51):
        assert master_biclique_polynomial(2, b) == four_term_polynomial(b), b
    print('VERIFY_OK', 'general_graphs', cases, 'bicliques', biclique_cases,
          'cliques', clique_cases, 'tested_subsets', inspected,
          'arithmetic_bicliques', 49)

if __name__ == '__main__':
    check()
