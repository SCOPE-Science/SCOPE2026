"""Direct geodesic-enumeration check for general-position counts of L(K_n).

No nonstandard packages are required. Execute: python3 verify_triangular_gp.py
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def recurrent(nmax):
    polys = [[1]]
    for n in range(1, nmax + 1):
        counts = [0] * (n * (n - 1) // 2 + 1)
        for s in range(1, n + 1):
            c = {1: [(0, 1)], 2: [(1, 1)], 3: [(2, 3), (3, 1)]}.get(s)
            if c is None:
                c = [(s-1, s)]
            for degree, coef in c:
                for d, v in enumerate(polys[n-s]):
                    counts[degree + d] += comb(n-1, s-1) * coef * v
        while counts and counts[-1] == 0:
            counts.pop()
        polys.append(counts)
    return polys


def geodesic_enumeration(n):
    edges = list(combinations(range(n), 2))
    N = len(edges)
    # The distance in a line graph of a clique is one for intersecting
    # pairs of edges, and two for disjoint pairs. This is checked here
    # directly from shortest paths in the actual line graph.
    neighborhoods = [set() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and set(edges[i]) & set(edges[j]):
                neighborhoods[i].add(j)
    distances = []
    for start in range(N):
        dist = [-1] * N
        dist[start] = 0
        frontier = [start]
        for u in frontier:
            for v in neighborhoods[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    frontier.append(v)
        distances.append(dist)
    forbidden_pairs_with_new = [[] for _ in range(N)]
    for a, b, c in combinations(range(N), 3):
        dab, dac, dbc = distances[a][b], distances[a][c], distances[b][c]
        if dab + dbc == dac or dab + dac == dbc or dac + dbc == dab:
            forbidden_pairs_with_new[c].append((1 << a) | (1 << b))
    counts = Counter()
    visited = 0
    def recurse(next_edge, chosen, size):
        nonlocal visited
        visited += 1
        if next_edge == N:
            counts[size] += 1
            return
        recurse(next_edge + 1, chosen, size)
        if not any((chosen & pair) == pair for pair in forbidden_pairs_with_new[next_edge]):
            recurse(next_edge + 1, chosen | (1 << next_edge), size + 1)
    recurse(0, 0, 0)
    return [counts[i] for i in range(max(counts) + 1)], visited


def main():
    polys = recurrent(20)
    total = 0
    for n in range(8):
        actual, visited = geodesic_enumeration(n)
        total += visited
        assert actual == polys[n], (n, actual, polys[n])
        print(f'n={n} vertices={comb(n,2)} configurations_visited={visited} polynomial_coefficients={actual}')
    for n in range(3, 21):
        expected_degree = n if n % 3 == 0 else n-1
        assert len(polys[n])-1 == expected_degree, (n, polys[n])
        if n % 3 == 0:
            assert polys[n][-1] == factorial(n) // (6 ** (n//3) * factorial(n//3))
    print('maximum degree and multiplicity identities verified for 3<=n<=20')
    print(f'total recursive geodesic test nodes: {total}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
