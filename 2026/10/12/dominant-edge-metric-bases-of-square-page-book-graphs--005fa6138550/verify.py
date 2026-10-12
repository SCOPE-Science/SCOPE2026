from itertools import combinations
from collections import deque

def book_graph(r):
    n = 2 + 2*r
    edges = [(0, 1)]
    for i in range(r):
        a = 2 + 2*i
        b = a + 1
        edges += [(0, a), (a, b), (b, 1)]
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj, edges

def all_distances(adj):
    D = []
    for s in range(len(adj)):
        d = [-1]*len(adj)
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        D.append(d)
    return D

def is_vertex_cover(edges, S):
    S = set(S)
    return all(u in S or v in S for u, v in edges)

def is_edge_resolving(D, edges, S):
    seen = set()
    for u, v in edges:
        sig = tuple(min(D[s][u], D[s][v]) for s in S)
        if sig in seen:
            return False
        seen.add(sig)
    return True

subset_trials = 0
bases_checked = 0

for r in range(2, 10):
    adj, edges = book_graph(r)
    D = all_distances(adj)
    n = len(adj)
    target = r + 1

    for k in range(target):
        for S in combinations(range(n), k):
            subset_trials += 1
            assert not (is_vertex_cover(edges, S) and is_edge_resolving(D, edges, S)), (r, k, S)

    actual = set()
    for S in combinations(range(n), target):
        subset_trials += 1
        if is_vertex_cover(edges, S) and is_edge_resolving(D, edges, S):
            actual.add(frozenset(S))

    expected = {
        frozenset([0] + [3 + 2*i for i in range(r)]),
        frozenset([1] + [2 + 2*i for i in range(r)]),
    }
    assert actual == expected, (r, actual, expected)
    assert len(actual) == 2
    bases_checked += len(actual)

print("VERIFY_OK")
print("book_parameters_checked =", 8)
print("parameters r = 2..9")
print("subset_trials =", subset_trials)
print("minimum_bases_checked =", bases_checked)
print("all smaller sets failed the combined vertex-cover and edge-resolving test")
print("all minimum bases were exactly the two bipartition classes")
