"""Exact finite verification of power domination on the icosahedral and dodecahedral graphs.

Run: python3 power_dual_verify.py (Python 3.9+; no third-party packages).
All graph labels and simultaneous observation steps are defined in this file.
"""
from itertools import combinations
from collections import Counter, deque


def graph(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert u != v and 0 <= u < n and 0 <= v < n
        adj[u].add(v)
        adj[v].add(u)
    assert sum(map(len, adj)) == 2 * len(set(tuple(sorted(e)) for e in edges))
    return tuple(tuple(sorted(row)) for row in adj)


def dodecahedron():
    e = []
    for i in range(10):
        e += [(i, (i + 1) % 10), (i, i + 10), (i + 10, (i + 2) % 10 + 10)]
    return graph(20, e)


def icosahedron():
    # Vertices: north pole 0; upper ring 1..5; lower ring 6..10; south pole 11.
    e = []
    for i in range(5):
        a, b = 1 + i, 6 + i
        e += [(0, a), (11, b), (a, 1 + (i + 1) % 5),
              (b, 6 + (i + 1) % 5), (a, b), (a, 6 + (i - 1) % 5)]
    return graph(12, e)


def bfs_distances(adj, source):
    d = [-1] * len(adj)
    d[source] = 0
    q = deque([source])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                q.append(v)
    assert min(d) >= 0
    return d


def propagation_sets(adj, seeds):
    seen = set(seeds)
    for u in seeds:
        seen.update(adj[u])
    sizes = [len(seen)]
    while True:
        new = set()
        for u in seen:
            remaining = set(adj[u]) - seen
            if len(remaining) == 1:
                new.update(remaining)
        if not new:
            break
        seen.update(new)
        sizes.append(len(seen))
    return tuple(sizes)


def propagation_bits(adj, seeds):
    masks = [sum(1 << u for u in nbrs) for nbrs in adj]
    selected = sum(1 << u for u in seeds)
    mask = selected
    for u in seeds:
        mask |= masks[u]
    sizes = [mask.bit_count()]
    limit = (1 << len(adj)) - 1
    while True:
        new = 0
        for u in range(len(adj)):
            if mask >> u & 1:
                outside = masks[u] & (limit ^ mask)
                if outside and outside & (outside - 1) == 0:
                    new |= outside
        if not (new & (limit ^ mask)):
            break
        mask |= new
        sizes.append(mask.bit_count())
    return tuple(sizes)


def exchange_distance_distribution(sets):
    sets = tuple(sorted(sets, key=lambda s: tuple(sorted(s))))
    n = len(sets)
    where = {s: k for k, s in enumerate(sets)}
    sizes = {len(s) for s in sets}
    assert len(sizes) == 1 and next(iter(sizes)) == 2
    nbrs = [[] for _ in sets]
    for i, a in enumerate(sets):
        for v in range(len({x for s in sets for x in s})):
            if v not in a:
                for u in a:
                    b = frozenset((a - {u}) | {v})
                    j = where.get(b)
                    if j is not None and j != i:
                        nbrs[i].append(j)
        nbrs[i] = sorted(set(nbrs[i]))
    assert all(i in nbrs[j] for i, row in enumerate(nbrs) for j in row)
    distances = Counter()
    for i in range(n):
        ds = [-1] * n
        ds[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in nbrs[u]:
                if ds[v] < 0:
                    ds[v] = ds[u] + 1
                    q.append(v)
        assert min(ds) >= 0
        for j in range(i + 1, n):
            distances[ds[j]] += 1
    return (Counter(map(len, nbrs)), dict(sorted(distances.items())))


def verify(adj, expected, count, degree, exchange, label):
    n = len(adj)
    assert len({tuple(sorted((u, v))) for u in range(n) for v in adj[u] if u < v}) == count
    assert set(map(len, adj)) == {degree}
    assert all(all(u in adj[v] for v in adj[u]) for u in range(n))
    assert all(propagation_sets(adj, [u])[-1] < n for u in range(n))
    table = Counter()
    good = []
    ds = [bfs_distances(adj, u) for u in range(n)]
    for u, v in combinations(range(n), 2):
        sizes = propagation_sets(adj, (u, v))
        assert sizes == propagation_bits(adj, (u, v))
        table[ds[u][v], sizes] += 1
        if sizes[-1] == n:
            good.append(frozenset((u, v)))
    assert table == Counter(expected)
    assert set(map(frozenset, good)) == set(
        frozenset((u, v)) for u, v in combinations(range(n), 2)
        if ds[u][v] == (3 if label == 'D' else ds[u][v]))
    degree_dist, distances = exchange_distance_distribution(good)
    assert (len(good), degree_dist, distances) == exchange
    if label == 'D':
        J = [[v for v in range(n) if ds[u][v] == 3] for u in range(n)]
        assert set(map(len, J)) == {6} and sum(map(len, J)) == 120
        assert max(max(bfs_distances(J, u)) for u in range(n)) == 3
    print(f'{label}: {n} vertices, {count} edges, {len(good)} optimal pairs, distances {distances}')


def main():
    verify(
        dodecahedron(),
        { (1, (6,)): 30,
          (2, (7, 10)): 60,
          (3, (8, 10, 14, 18, 20)): 60,
          (4, (8,)): 30,
          (5, (8,)): 10 },
        30, 3,
        (60, Counter({10: 60}), {1: 300, 2: 870, 3: 600}), 'D')
    verify(
        icosahedron(),
        { (1, (8, 10, 12)): 30,
          (2, (10, 12)): 30,
          (3, (12,)): 6 },
        30, 5,
        (66, Counter({20: 66}), {1: 660, 2: 1485}), 'I')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
