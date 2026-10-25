"""Exact finite checks for a non-monotone binary network public-goods game.

Run with Python 3.9+; standard library only.  The general theorem is proved
analytically in RESULT.md; this script checks finite boundary statements.
"""
from itertools import combinations


def bits(n):
    return range(1 << n)


def edges_of_mask(n, mask):
    all_edges = list(combinations(range(n), 2))
    return [edge for i, edge in enumerate(all_edges) if (mask >> i) & 1]


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def connected(adj):
    if not adj:
        return True
    seen = {0}
    stack = [0]
    while stack:
        for w in adj[stack.pop()]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == len(adj)


def paths_capped_at_two(adj, a, b, forbidden):
    """Count simple a--b paths avoiding one undirected edge, capped at 2."""
    found = 0
    stack = [(a, 1 << a)]
    while stack:
        v, seen = stack.pop()
        if v == b:
            found += 1
            if found == 2:
                return 2
            continue
        for w in adj[v]:
            if (v, w) == forbidden or (w, v) == forbidden:
                continue
            if not (seen >> w) & 1:
                stack.append((w, seen | (1 << w)))
    return found


def cactus(adj, edges):
    return all(paths_capped_at_two(adj, u, v, (u, v)) <= 1
               for u, v in edges)


def is_equilibrium(adj, x, response):
    return all(((x >> i) & 1) == response(sum((x >> j) & 1 for j in adj[i]))
               for i in range(len(adj)))


def solve_odd_domination(adj):
    """Solve (I+A)x=1 over F2, or return None if inconsistent."""
    n = len(adj)
    rows = [1 << i | sum(1 << j for j in adj[i]) | (1 << n)
            for i in range(n)]
    pivots = []
    k = 0
    for col in range(n):
        p = next((j for j in range(k, n) if (rows[j] >> col) & 1), None)
        if p is None:
            continue
        rows[k], rows[p] = rows[p], rows[k]
        for j in range(n):
            if j != k and ((rows[j] >> col) & 1):
                rows[j] ^= rows[k]
        pivots.append(col)
        k += 1
    assert all((row & ((1 << n) - 1)) or not ((row >> n) & 1) for row in rows)
    x = 0
    for j, col in enumerate(pivots):
        if (rows[j] >> n) & 1:
            x |= 1 << col
    assert all((sum((x >> v) & 1 for v in adj[u]) + ((x >> u) & 1)) % 2 == 1
               for u in range(n))
    return x


def verify():
    T = lambda k: int(k in (0, 2))
    checked_cactus = 0
    checked_cactus_odd_cert = 0
    checked_no_bad_cactus = 0
    for n in range(1, 7):
        m = n * (n - 1) // 2
        for em in range(1 << m):
            es = edges_of_mask(n, em)
            adj = adjacency(n, es)
            if not connected(adj) or not cactus(adj, es):
                continue
            checked_cactus += 1
            cert = solve_odd_domination(adj)
            assert is_equilibrium(adj, cert, T), (n, es)
            checked_cactus_odd_cert += 1
            assert any(is_equilibrium(adj, x, T) for x in bits(n))
            checked_no_bad_cactus += 1
    # Two triangles sharing a vertex, and one leaf on a peripheral vertex of each.
    edges7 = [(0, 1), (0, 2), (1, 2), (2, 3),
              (0, 4), (0, 5), (4, 5), (5, 6)]
    adj7 = adjacency(7, edges7)
    assert cactus(adj7, edges7) and connected(adj7)
    assert not any(is_equilibrium(adj7, x, T) for x in bits(7))
    print('PASS: all connected labelled cactus graphs on n<=6')
    print('graphs_checked=', checked_cactus,
          'parity_certificates=', checked_cactus_odd_cert,
          'direct_equilibrium_checks=', checked_no_bad_cactus)
    print('PASS: exact 7-vertex two-triangle cactus has no equilibrium')




def verify_seven_vertex_cactus_census():
    """Exhaust all labelled connected seven-vertex cacti and group failures."""
    from itertools import combinations
    n = 7
    all_edges = list(combinations(range(n), 2))

    def connected_cactus(edge_subset):
        a = [[] for _ in range(n)]
        for u, v in edge_subset:
            a[u].append(v)
            a[v].append(u)
        seen = {0}
        stack = [0]
        while stack:
            for v in a[stack.pop()]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        if len(seen) != n:
            return None
        disc = [-1] * n
        low = [0] * n
        edge_stack = []
        clock = 0

        def dfs(u, parent):
            nonlocal clock
            disc[u] = low[u] = clock
            clock += 1
            for v in a[u]:
                if v == parent:
                    continue
                if disc[v] < 0:
                    edge_stack.append((u, v))
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] >= disc[u]:
                        block = []
                        while True:
                            edge = edge_stack.pop()
                            block.append(edge)
                            if edge == (u, v):
                                break
                        if len(block) > 1:
                            vertices = set()
                            for p, q in block:
                                vertices.add(p)
                                vertices.add(q)
                            if len(block) != len(vertices):
                                raise ValueError('non-cycle block')
                elif disc[v] < disc[u]:
                    edge_stack.append((u, v))
                    low[u] = min(low[u], disc[v])
        try:
            dfs(0, -1)
        except ValueError:
            return None
        return a

    def isomorphic(a, b):
        if sorted(map(len, a)) != sorted(map(len, b)):
            return False
        allowed = {u: [v for v in range(n) if len(a[u]) == len(b[v])]
                   for u in range(n)}
        order = sorted(range(n), key=lambda u: (len(allowed[u]), -len(a[u])))
        used = set()
        match = {}

        def extend(k):
            if k == n:
                return True
            u = order[k]
            for v in allowed[u]:
                if v in used:
                    continue
                if all((w in a[u]) == (match[w] in b[v]) for w in match):
                    match[u] = v
                    used.add(v)
                    if extend(k + 1):
                        return True
                    used.remove(v)
                    del match[u]
            return False
        return extend(0)

    checked = 0
    failing = 0
    classes = []
    # In a connected cactus on 7 vertices, each cycle requires at least
    # two vertices beyond the block-attachment vertex: cycle rank <=3.
    # Hence the number of edges is between 6 and 9 inclusive.
    for m in range(6, 10):
        for es in combinations(all_edges, m):
            adj = connected_cactus(es)
            if adj is None:
                continue
            checked += 1
            if not any(is_equilibrium(adj, x, lambda k: int(k in (0, 2)))
                       for x in bits(7)):
                failing += 1
                if not any(isomorphic(adj, previous) for previous in classes):
                    classes.append(adj)
    assert (checked, failing, len(classes)) == (111982, 3150, 2), (
        checked, failing, len(classes))
    shapes = sorted(sorted(len(x) for x in c) for c in classes)
    assert shapes == [[1, 1, 2, 2, 3, 3, 4], [2, 2, 2, 2, 2, 2, 4]], shapes
    print('PASS: seven-vertex cactus census, exact labelled counts and two obstruction classes')
    print('seven_vertex_labelled_cacti=', checked,
          'no_equilibrium=', failing, 'isomorphism_classes=', len(classes))


if __name__ == '__main__':
    verify()
    verify_seven_vertex_cactus_census()
