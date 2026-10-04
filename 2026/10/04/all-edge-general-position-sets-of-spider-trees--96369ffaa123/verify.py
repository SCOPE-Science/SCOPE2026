from itertools import combinations, product
from collections import deque
from math import comb

def spider_graph(lengths):
    edges = []
    next_vertex = 1
    arm_edges = []
    for length in lengths:
        prev = 0
        arm = []
        for _ in range(length):
            cur = next_vertex
            next_vertex += 1
            arm.append(len(edges))
            edges.append((prev, cur))
            prev = cur
        arm_edges.append(arm)
    return next_vertex, edges, arm_edges

def geodesic_edge_sets(n, edges):
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    paths = []
    for source in range(n):
        parent = [None] * n
        parent_edge = [None] * n
        parent[source] = source
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, e in adj[u]:
                if parent[v] is None:
                    parent[v] = u
                    parent_edge[v] = e
                    queue.append(v)
        for target in range(source + 1, n):
            cur = target
            p = set()
            while cur != source:
                p.add(parent_edge[cur])
                cur = parent[cur]
            paths.append(p)
    return paths

def is_edge_gp(mask, paths):
    return all(sum((mask >> e) & 1 for e in path) <= 2 for path in paths)

def predicted_coefficients(lengths):
    k = len(lengths)
    coeff = [0] * (k + 1)
    coeff[0] = 1
    for length in lengths:
        for r in range(k, 0, -1):
            coeff[r] += length * coeff[r - 1]
    coeff[2] += sum(comb(length, 2) for length in lengths)
    return coeff

checked = 0
checked_subsets = 0
for k in range(3, 6):
    for lengths in product(range(1, 5), repeat=k):
        if sum(lengths) > 10:
            continue
        n, edges, arms = spider_graph(lengths)
        paths = geodesic_edge_sets(n, edges)
        m = len(edges)
        actual = [0] * (m + 1)
        valid = []
        for mask in range(1 << m):
            checked_subsets += 1
            if is_edge_gp(mask, paths):
                actual[mask.bit_count()] += 1
                valid.append(mask)
        expected = predicted_coefficients(lengths)
        expected += [0] * (m + 1 - len(expected))
        assert actual == expected, (lengths, actual, expected)
        maximal = []
        for mask in valid:
            if all(((mask >> e) & 1) or not is_edge_gp(mask | (1 << e), paths) for e in range(m)):
                maximal.append(mask)
        predicted_maximal = []
        for choices in product(*arms):
            mask = 0
            for e in choices:
                mask |= 1 << e
            predicted_maximal.append(mask)
        for arm in arms:
            for e, f in combinations(arm, 2):
                predicted_maximal.append((1 << e) | (1 << f))
        assert set(maximal) == set(predicted_maximal), (lengths, maximal, predicted_maximal)
        checked += 1

print("VERIFY_OK")
print("spider_types_checked =", checked)
print("edge_subsets_checked =", checked_subsets)
print("arm_lengths = 1..4, total_edges <= 10, number_of_arms = 3..5")
