from itertools import combinations
from collections import deque

def book_graph(r):
    # spine x=0, y=1; page i has a_i=2+2i, b_i=3+2i
    n = 2 + 2*r
    adj = [set() for _ in range(n)]
    adj[0].add(1)
    adj[1].add(0)
    for i in range(r):
        a = 2 + 2*i
        b = a + 1
        for u, v in ((0, a), (a, b), (b, 1)):
            adj[u].add(v)
            adj[v].add(u)
    return adj

def all_distances(adj):
    n = len(adj)
    D = []
    for s in range(n):
        d = [10**9] * n
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] == 10**9:
                    d[v] = d[u] + 1
                    q.append(v)
        D.append(d)
    return D

def x_positionable(D, X, u, v):
    # A selected vertex z is internal to some u-v geodesic iff
    # d(u,z)+d(z,v)=d(u,v).
    for z in X:
        if z != u and z != v and D[u][z] + D[z][v] == D[u][v]:
            return False
    return True

def is_dual_general_position(D, mask):
    n = len(D)
    X = {v for v in range(n) if (mask >> v) & 1}
    C = set(range(n)) - X
    for group in (X, C):
        for u, v in combinations(group, 2):
            if not x_positionable(D, X, u, v):
                return False
    return True

def predicted_nonempty_sets(r):
    return {
        (1 << (2 + 2*i)) | (1 << (3 + 2*i))
        for i in range(r)
    }

graphs = 0
subsets = 0
dual_sets = 0

for r in range(2, 10):
    adj = book_graph(r)
    D = all_distances(adj)
    actual_nonempty = set()
    n = len(adj)

    for mask in range(1 << n):
        subsets += 1
        if is_dual_general_position(D, mask):
            dual_sets += 1
            if mask:
                actual_nonempty.add(mask)

    expected = predicted_nonempty_sets(r)
    assert actual_nonempty == expected, (r, len(actual_nonempty), len(expected))
    assert max(mask.bit_count() for mask in actual_nonempty) == 2
    assert len(actual_nonempty) == r
    graphs += 1

print("VERIFY_OK")
print("book_parameters_checked =", graphs)
print("vertex_subsets_checked =", subsets)
print("dual_general_position_sets_checked =", dual_sets)
print("parameters r = 2..9")
print("all nonempty dual general-position sets are exactly the internal page pairs")
print("all dual general-position numbers equal 2")
print("all maximum-set counts equal r")
