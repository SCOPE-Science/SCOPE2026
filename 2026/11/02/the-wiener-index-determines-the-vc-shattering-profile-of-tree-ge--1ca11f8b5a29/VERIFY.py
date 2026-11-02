"""Independent finite checks for tree halfspace shattering and distance sums.

Only the Python standard library is required.  Exhaustive over all labelled
Cayley trees through six vertices; larger tests use deterministic sampled trees.
"""
from collections import deque
from itertools import product
from math import comb
import random


def prufer_tree(n, word):
    if n == 1:
        return []
    degree = [1] * n
    for x in word:
        degree[x] += 1
    edges = []
    for x in word:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    a, b = [i for i in range(n) if degree[i] == 1]
    edges.append((a, b))
    return edges


def distances(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    dist = []
    for s in range(n):
        dd = [-1] * n
        dd[s] = 0
        q = deque([s])
        while q:
            a = q.popleft()
            for b in adj[a]:
                if dd[b] == -1:
                    dd[b] = dd[a] + 1
                    q.append(b)
        assert all(x >= 0 for x in dd)
        dist.append(dd)
    return adj, dist


def direct_halfspaces(n, d):
    universe = (1 << n) - 1
    convex = set()
    for mask in range(1 << n):
        vs = [i for i in range(n) if mask >> i & 1]
        if all(not (d[a][b] == d[a][c] + d[c][b]) or (mask >> c & 1)
               for a in vs for b in vs for c in range(n)):
            convex.add(mask)
    return {m for m in convex if (universe ^ m) in convex}


def edge_halfspaces(n, edges, adj):
    universe = (1 << n) - 1
    result = {0, universe}
    for a, b in edges:
        found = {a}
        q = [a]
        for x in q:
            for y in adj[x]:
                if (x == a and y == b) or (x == b and y == a):
                    continue
                if y not in found:
                    found.add(y)
                    q.append(y)
        m = sum(1 << i for i in found)
        result.update([m, universe ^ m])
    return result


def trace_profile(n, family):
    counts = [0] * (n + 1)
    shattered = set()
    for support in range(1 << n):
        k = support.bit_count()
        traces = {h & support for h in family}
        if len(traces) == (1 << k):
            counts[k] += 1
            shattered.add(support)
    return counts, shattered


def check(n, edges, exhaustive=True):
    adj, d = distances(n, edges)
    half = direct_halfspaces(n, d) if exhaustive else edge_halfspaces(n, edges, adj)
    assert half == edge_halfspaces(n, edges, adj), (n, edges, 'halfspace classification')
    assert len(half) == 2 * n
    W = sum(d[i][j] for i in range(n) for j in range(i + 1, n))
    cutW = 0
    for a, b in edges:
        found = {a}
        q = [a]
        for x in q:
            for y in adj[x]:
                if (x == a and y == b) or (x == b and y == a):
                    continue
                if y not in found:
                    found.add(y)
                    q.append(y)
        s = len(found)
        cutW += s * (n - s)
    assert W == cutW
    target = [1, n, comb(n, 2) if n >= 2 else 0,
              (comb(n, 3) if n >= 3 else 0) + comb(n, 2) - W]
    # The theoretical polynomial has no coefficients beyond degree 3.
    target += [0] * max(0, n + 1 - len(target))
    target = target[:n + 1]
    counts, shattered = trace_profile(n, half)
    assert counts == target, (n, edges, counts, target)
    for support in range(1 << n):
        vertices = [i for i in range(n) if support >> i & 1]
        k = len(vertices)
        if k <= 2:
            condition = True
        elif k == 3:
            condition = not any(d[a][b] == d[a][c] + d[c][b]
                                for a in vertices for b in vertices for c in vertices
                                if len({a,b,c}) == 3)
        else:
            condition = False
        assert (support in shattered) == condition, (n,edges,vertices)
    return W, counts[3] if n >= 3 else 0


def main():
    total = 0
    for n in range(1, 7):
        num = 0
        for word in product(range(n), repeat=max(0, n - 2)):
            edges = prufer_tree(n, word)
            check(n, edges)
            num += 1
        total += num
        print(f'EXHAUSTIVE_LABELLED_TREES_PASS n={n} count={num}')
    assert total == 1442, total
    rng = random.Random(923417)
    samples = 0
    for n in range(7, 11):
        for _ in range(30):
            word = [rng.randrange(n) for __ in range(n - 2)]
            edges = prufer_tree(n, word)
            check(n, edges)
            samples += 1
    print(f'DETERMINISTIC_LARGER_TREES_PASS count={samples}')
    for n in range(4, 11):
        star = [(0, v) for v in range(1, n)]
        path = [(v, v + 1) for v in range(n - 1)]
        w_star, triple_star = check(n, star)
        w_path, triple_path = check(n, path)
        assert w_star == (n - 1) ** 2
        assert triple_star == comb(n - 1, 3)
        assert w_path == n * (n * n - 1) // 6
        assert triple_path == 0
    print('EXTREMAL_STAR_PATH_IDENTITIES_PASS')
    print('ALL_TREE_HALFSPACE_WIENER_CHECKS_PASS')


if __name__ == '__main__':
    main()
