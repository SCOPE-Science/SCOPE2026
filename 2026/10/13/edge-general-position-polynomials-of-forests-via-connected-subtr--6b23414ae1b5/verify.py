"""Independent checks for edge-general-position polynomial on forests.

Python 3 standard library only. Execute: python verify_edge_gp_forests.py
"""
from collections import deque
from itertools import product
from math import comb, prod
import random


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i + j] += x * y
    return c


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    return c


def polynomial(n, edges):
    """Fast theorem evaluation for any forest, including isolated vertices."""
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    visited = set()
    result = [1]
    for root in range(n):
        if root in visited:
            continue
        visited.add(root)
        parents = {root: -1}
        order = [root]
        for v in order:
            for w in g[v]:
                if w not in parents:
                    parents[w] = v
                    visited.add(w)
                    order.append(w)
        B = {}
        for v in reversed(order):
            p = [1]
            for w in g[v]:
                if parents.get(w) == v:
                    p = mul(p, add([0, 1], B[w]))
            B[v] = p
        C = B[root][:]
        for v in order[1:]:
            C = add(C, [0] + B[v])
        m = len(order) - 1
        Q = [0] * (m + 1)
        for k in range(3, len(C)):
            Q[k] += C[k]
        Q[0] = 1
        if m >= 1: Q[1] = m
        if m >= 2: Q[2] = comb(m, 2)
        result = mul(result, Q)
    return result


def brute(n, edges):
    """Literal all-geodesics test, without relying on cut characterization."""
    m = len(edges)
    g = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        g[u].append((v, i))
        g[v].append((u, i))
    paths = set()
    for s in range(n):
        visited = {s: 0}
        q = deque([s])
        while q:
            v = q.popleft()
            for w, e in g[v]:
                if w not in visited:
                    visited[w] = visited[v] | (1 << e)
                    q.append(w)
        paths.update(visited.values())
    counts = [0] * (m + 1)
    for S in range(1 << m):
        if all((S & p).bit_count() < 3 for p in paths):
            counts[S.bit_count()] += 1
    return counts, 1 << m


def prufer_tree(n, seq):
    if n == 1: return []
    if n == 2: return [(0, 1)]
    deg = [1] * n
    for x in seq: deg[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i, d in enumerate(deg) if d == 1)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    a, b = (i for i in range(n) if deg[i] == 1)
    edges.append((a, b))
    return edges


def connected_cut_counts(n, edges):
    """Third check: enumerate all vertex subsets directly by connectedness."""
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    c = [0] * (n + 1)
    for mask in range(1, 1 << n):
        start = (mask & -mask).bit_length() - 1
        seen = {start}
        stack = [start]
        while stack:
            v = stack.pop()
            for w in g[v]:
                if mask >> w & 1 and w not in seen:
                    seen.add(w)
                    stack.append(w)
        if len(seen) == mask.bit_count():
            boundary = sum(bool((mask >> u & 1) != (mask >> v & 1)) for u, v in edges)
            c[boundary] += 1
    return c


def extremal_count(n, edges):
    """Leaf-arm product for a nonpath tree; None otherwise."""
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    branches = {v for v in range(n) if len(g[v]) >= 3}
    if not branches:
        return None
    lengths = []
    for v in range(n):
        if len(g[v]) != 1: continue
        prev, cur, length = -1, v, 0
        while cur not in branches:
            neigh = [w for w in g[cur] if w != prev]
            assert len(neigh) == 1
            prev, cur = cur, neigh[0]
            length += 1
        lengths.append(length)
    return len(lengths), prod(lengths)


def main():
    total_sets = total_trees = cut_checks = extremal_checks = 0
    rng = random.Random(273190)
    for n in range(1, 12):
        if n <= 7:
            seqs = product(range(n), repeat=max(n - 2, 0)) if n >= 2 else [()]
        else:
            sample_count = {8: 400, 9: 350, 10: 180, 11: 75}[n]
            seqs = (tuple(rng.randrange(n) for _ in range(n - 2)) for _ in range(sample_count))
        for j, seq in enumerate(seqs):
            edges = prufer_tree(n, seq)
            fast = polynomial(n, edges)
            direct, tested = brute(n, edges)
            assert fast == direct, (n, edges, fast, direct)
            total_trees += 1
            total_sets += tested
            if n <= 9 and (n <= 6 or j % 11 == 0):
                c = connected_cut_counts(n, edges)
                c[1] -= n - 1
                assert fast == c[:n], (n, edges, fast, c)
                cut_checks += 1
            if n >= 4:
                lead = extremal_count(n, edges)
                if lead is not None:
                    leaves, product_count = lead
                    assert len(fast) - 1 >= leaves
                    assert fast[leaves] == product_count
                    assert not any(fast[leaves+1:])
                    extremal_checks += 1
                elif n >= 3:
                    assert fast[2] == comb(n - 1, 2)
    # Component multiplicativity and disconnected boundary samples.
    assert polynomial(0, []) == [1]
    assert polynomial(4, []) == [1]
    assert polynomial(6, [(0, 1), (1, 2), (3, 4), (4, 5)]) == mul(polynomial(3, [(0, 1), (1, 2)]), polynomial(3, [(0, 1), (1, 2)]))
    print('PASS exhaustive/sample labelled trees:', total_trees)
    print('PASS geodesic edge-subset checks:', total_sets)
    print('PASS independent connected-cut enumerations:', cut_checks)
    print('PASS extremal arm-product identities:', extremal_checks)
    print('PASS disconnected forests and isolated-vertex cases')
    for n in [5, 7, 9]:
        edges = [(0, i) for i in range(1, n)]
        print('star', n, polynomial(n, edges))
    for n in [4, 7, 10]:
        edges = [(i, i + 1) for i in range(n - 1)]
        print('path', n, polynomial(n, edges))

if __name__ == '__main__':
    main()
