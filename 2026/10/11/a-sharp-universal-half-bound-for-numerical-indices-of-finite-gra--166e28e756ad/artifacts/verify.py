"""Finite exact checks for the unit-edge graph numerical-index half bound.

Proof of the infinite graph-family claim is analytic; these are corroborative cases.
"""
from itertools import combinations, product
from collections import deque


def graph_connected(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    q = deque([0])
    while q:
        for v in adj[q.popleft()]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen) == n


def directed_distance(n, edges, h, start):
    # Each arc (s,t) costs 1+min(0,h[t]-h[s]) in {0,1}.
    # Bellman-Ford is exact, dependency-free, and avoids any heuristic search.
    g = [n + 1] * n
    g[start] = 0
    for _ in range(n - 1):
        changed = False
        for a, b in edges:
            ca = 1 + min(0, h[b] - h[a])
            cb = 1 + min(0, h[a] - h[b])
            if g[b] > g[a] + ca:
                g[b] = g[a] + ca
                changed = True
            if g[a] > g[b] + cb:
                g[a] = g[b] + cb
                changed = True
        if not changed:
            break
    return g


def verify_potential(n, edges, h):
    if any(abs(h[a] - h[b]) > 1 for a, b in edges):
        return 0
    count = 0
    for a, b in edges:
        if h[a] != h[b]:
            continue
        g = directed_distance(n, edges, h, b)
        assert g[a] == 1 and g[b] == 0, (n, edges, h, a, b, g)
        assert all(abs(g[s] - g[t]) <= 1 for s, t in edges), (n, edges, h, g)
        assert all(abs((h[s]-g[s]) - (h[t]-g[t])) <= 1 for s, t in edges), (n, edges, h, g)
        count += 1
    return count


def exhaustive():
    graphs = potentials = equal_edges = 0
    for n in range(2, 6):
        pairs = list(combinations(range(n), 2))
        for mask in range(1, 1 << len(pairs)):
            edges = [e for i,e in enumerate(pairs) if mask & (1 << i)]
            if not graph_connected(n, edges):
                continue
            graphs += 1
            for htail in product(range(-(n-1), n), repeat=n-1):
                h=(0,)+htail
                if any(abs(h[a]-h[b])>1 for a,b in edges):
                    continue
                potentials += 1
                equal_edges += verify_potential(n, edges, h)
    print('VERIFY_OK', 'connected_labeled_graphs=', graphs,
          'integer_potentials=', potentials,
          'equal_edge_decompositions=', equal_edges, 'n=2..5')

if __name__=='__main__':
    exhaustive()
