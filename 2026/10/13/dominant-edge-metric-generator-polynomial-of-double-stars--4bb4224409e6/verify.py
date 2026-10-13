from itertools import combinations
from collections import Counter, deque

def double_star(p, q):
    # centers u=0, v=1; A-leaves 2..p+1; B-leaves p+2..p+q+1
    N = p + q + 2
    adj = [set() for _ in range(N)]
    edges = []
    def add(a, b):
        adj[a].add(b); adj[b].add(a); edges.append((a, b))
    add(0, 1)
    for i in range(p):
        add(0, 2+i)
    for j in range(q):
        add(1, 2+p+j)
    return adj, edges

def distances(adj):
    N = len(adj)
    D = []
    for s in range(N):
        d = [10**9] * N
        d[s] = 0
        Q = deque([s])
        while Q:
            u = Q.popleft()
            for v in adj[u]:
                if d[v] == 10**9:
                    d[v] = d[u] + 1
                    Q.append(v)
        D.append(d)
    return D

def is_vertex_cover(edges, S):
    S = set(S)
    return all(u in S or v in S for u, v in edges)

def is_edge_resolving(D, edges, S):
    S = tuple(S)
    reps = []
    for u, v in edges:
        reps.append(tuple(min(D[s][u], D[s][v]) for s in S))
    return len(reps) == len(set(reps))

def structural_condition(p, q, S):
    S = set(S)
    A = set(range(2, 2+p))
    B = set(range(2+p, 2+p+q))
    u, v = 0, 1
    if len(A - S) > 1 or len(B - S) > 1:
        return False
    if u not in S and (A - S):
        return False
    if v not in S and (B - S):
        return False
    if u not in S and v not in S:
        return False
    return True

print("VERIFY_OK")
total_subsets = 0
for p in range(1, 6):
    for q in range(1, 6):
        adj, edges = double_star(p, q)
        D = distances(adj)
        N = len(adj)
        actual = set()
        predicted = set()
        for mask in range(1 << N):
            total_subsets += 1
            S = frozenset(v for v in range(N) if (mask >> v) & 1)
            feasible = is_vertex_cover(edges, S) and is_edge_resolving(D, edges, S)
            structural = structural_condition(p, q, S)
            assert feasible == structural, (p, q, sorted(S), feasible, structural)
            if feasible:
                actual.add(S)
            if structural:
                predicted.add(S)

        assert actual == predicted
        counts = Counter(map(len, actual))
        expected = {
            p+q: p*q + p + q,
            p+q+1: p + q + 2,
            p+q+2: 1,
        }
        assert counts == expected, (p, q, counts, expected)
        assert min(counts) == p+q
        print(f"p={p}, q={q}: Ddim_e={p+q}, profile={dict(sorted(counts.items()))}")

print("subsets_checked =", total_subsets)
print("all feasible sets matched the structural characterization and polynomial")
