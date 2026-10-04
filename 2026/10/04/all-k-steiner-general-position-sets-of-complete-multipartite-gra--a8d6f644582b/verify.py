from itertools import combinations
from math import comb
from collections import deque


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def make_graph(part_sizes):
    labels = []
    for i, size in enumerate(part_sizes):
        labels.extend([i] * size)
    n = len(labels)
    adj = [set() for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if labels[u] != labels[v]:
                adj[u].add(v)
                adj[v].add(u)
    return labels, adj


def induced_connected(mask, adj):
    verts = [v for v in range(len(adj)) if (mask >> v) & 1]
    if len(verts) <= 1:
        return True
    seen = {verts[0]}
    q = deque([verts[0]])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if ((mask >> v) & 1) and v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen) == len(verts)


def steiner_edge_count(Bmask, adj):
    n = len(adj)
    best = n + 1
    for U in range(1 << n):
        if (U & Bmask) != Bmask:
            continue
        if induced_connected(U, adj):
            best = min(best, U.bit_count() - 1)
    return best


def actual_ksgp(Amask, k, adj):
    n = len(adj)
    A = [v for v in range(n) if (Amask >> v) & 1]
    if len(A) < k:
        return True
    for Btuple in combinations(A, k):
        Bmask = sum(1 << v for v in Btuple)
        d = steiner_edge_count(Bmask, adj)
        for x in A:
            if (Bmask >> x) & 1:
                continue
            for U in range(1 << n):
                if (U & Bmask) != Bmask or not ((U >> x) & 1):
                    continue
                if U.bit_count() - 1 == d and induced_connected(U, adj):
                    return False
    return True


def predicted_ksgp(Amask, k, labels):
    r = max(labels) + 1
    counts = [0] * r
    for v, part in enumerate(labels):
        if (Amask >> v) & 1:
            counts[part] += 1
    support = sum(c > 0 for c in counts)
    return support <= 1 or max(counts, default=0) <= k - 1


def predicted_coefficients(part_sizes, k):
    N = sum(part_sizes)
    coeff = [0] * (N + 1)
    current = [1]
    for n_i in part_sizes:
        cap = min(n_i, k - 1)
        factor = [comb(n_i, j) for j in range(cap + 1)]
        nxt = [0] * (len(current) + len(factor) - 1)
        for a, ca in enumerate(current):
            for b, cb in enumerate(factor):
                nxt[a + b] += ca * cb
        current = nxt
    for j, c in enumerate(current):
        coeff[j] += c
    for n_i in part_sizes:
        for j in range(k, n_i + 1):
            coeff[j] += comb(n_i, j)
    return coeff


instances = 0
subset_checks = 0
for N in range(2, 9):
    for part_sizes in partitions(N):
        if len(part_sizes) < 2:
            continue
        labels, adj = make_graph(part_sizes)
        for k in range(2, N):
            observed = [0] * (N + 1)
            for A in range(1 << N):
                subset_checks += 1
                actual = actual_ksgp(A, k, adj)
                predicted = predicted_ksgp(A, k, labels)
                assert actual == predicted, (part_sizes, k, A, actual, predicted)
                if actual:
                    observed[A.bit_count()] += 1
            expected = predicted_coefficients(part_sizes, k)
            assert observed == expected, (part_sizes, k, observed, expected)
            M = max(part_sizes)
            S = sum(min(n_i, k - 1) for n_i in part_sizes)
            assert max(i for i, c in enumerate(observed) if c) == max(M, S)
            instances += 1

print('VERIFY_OK')
print('multipartite_k_instances =', instances)
print('vertex_subset_checks =', subset_checks)
print('orders = 2..8; all k = 2..N-1')
