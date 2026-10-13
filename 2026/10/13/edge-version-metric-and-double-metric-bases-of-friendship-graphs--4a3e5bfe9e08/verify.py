from itertools import combinations
from collections import deque

def friendship_edges(r):
    # Page i consists of two spokes and one rim edge, in that order.
    edges = []
    center = 0
    for i in range(r):
        a = 1 + 2*i
        b = a + 1
        edges.extend([(center, a), (center, b), (a, b)])
    return edges

def line_graph_distances(edges):
    m = len(edges)
    adj = [set() for _ in range(m)]
    for i in range(m):
        ei = set(edges[i])
        for j in range(i + 1, m):
            if ei.intersection(edges[j]):
                adj[i].add(j)
                adj[j].add(i)

    D = []
    for s in range(m):
        dist = [10**9] * m
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == 10**9:
                    dist[v] = dist[u] + 1
                    q.append(v)
        D.append(dist)
    return D

def is_edge_version_resolving(D, S):
    S = tuple(S)
    seen = set()
    for u in range(len(D)):
        sig = tuple(D[u][s] for s in S)
        if sig in seen:
            return False
        seen.add(sig)
    return True

def is_edge_version_doubly_resolving(D, S):
    S = tuple(S)
    if len(S) < 2:
        return False
    for u in range(len(D)):
        for v in range(u + 1, len(D)):
            first = D[u][S[0]] - D[v][S[0]]
            if all(D[u][s] - D[v][s] == first for s in S[1:]):
                return False
    return True

def predicted_metric_basis(r, S):
    S = set(S)
    counts = [sum((3*i + j) in S for j in range(3)) for i in range(r)]
    if counts.count(1) != 1 or counts.count(2) != r - 1:
        return False
    i = counts.index(1)
    # In the exceptional page, the single selected edge must be a spoke.
    return (3*i in S) ^ (3*i + 1 in S)

def predicted_double_basis(r, S):
    S = set(S)
    return all(sum((3*i + j) in S for j in range(3)) == 2 for i in range(r))

total_subset_trials = 0
metric_bases = 0
double_bases = 0

for r in range(2, 7):
    D = line_graph_distances(friendship_edges(r))
    m = 3*r

    metric_target = 2*r - 1
    for k in range(metric_target):
        for S in combinations(range(m), k):
            total_subset_trials += 1
            assert not is_edge_version_resolving(D, S), (r, "metric", k, S)

    actual_metric = set()
    for S in combinations(range(m), metric_target):
        total_subset_trials += 1
        good = is_edge_version_resolving(D, S)
        pred = predicted_metric_basis(r, S)
        assert good == pred, (r, "metric classification", S, good, pred)
        if good:
            actual_metric.add(S)

    assert len(actual_metric) == 2*r*(3**(r-1))
    metric_bases += len(actual_metric)

    double_target = 2*r
    for k in range(double_target):
        for S in combinations(range(m), k):
            total_subset_trials += 1
            assert not is_edge_version_doubly_resolving(D, S), (r, "double", k, S)

    actual_double = set()
    for S in combinations(range(m), double_target):
        total_subset_trials += 1
        good = is_edge_version_doubly_resolving(D, S)
        pred = predicted_double_basis(r, S)
        assert good == pred, (r, "double classification", S, good, pred)
        if good:
            actual_double.add(S)

    assert len(actual_double) == 3**r
    double_bases += len(actual_double)

print("VERIFY_OK")
print("friendship_parameters_checked =", 5)
print("parameters r = 2..6")
print("subset_trials =", total_subset_trials)
print("metric_bases_checked =", metric_bases)
print("doubly_resolving_bases_checked =", double_bases)
print("all metric dimensions matched 2r-1")
print("all double metric dimensions matched 2r")
print("all minimum sets matched the structural classifications")
