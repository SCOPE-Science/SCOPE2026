"""Exhaustive small-order and witness checks for the derangement swap graph."""
from collections import deque
from itertools import combinations, permutations


def graph(n):
    vertices = [p for p in permutations(range(1, n + 1))
                if all(j != x for j, x in enumerate(p, 1))]
    admissible = set(vertices)
    adj = {p: [] for p in vertices}
    for p in vertices:
        for j in range(n - 1):
            swapped = p[:j] + (p[j+1], p[j]) + p[j+2:]
            if swapped in admissible:
                adj[p].append(swapped)
    return adj


def distances(adj, source):
    d = {source: 0}
    queue = deque([source])
    while queue:
        p = queue.popleft()
        for q in adj[p]:
            if q not in d:
                d[q] = d[p] + 1
                queue.append(q)
    return d


def kendall(a, b):
    rank = {x: j for j, x in enumerate(b)}
    return sum(rank[x] > rank[y] for x, y in combinations(a, 2))


def run():
    for n, size, count in [(2, 1, 0), (3, 2, 0), (4, 9, 11), (5, 44, 188)]:
        adj = graph(n)
        pairs = bad = 0
        for a in adj:
            for b, d in distances(adj, a).items():
                if a < b:
                    pairs += 1
                    bad += d != kendall(a, b)
        print(n, len(adj), pairs, bad)
        assert (len(adj), pairs, bad) == (size, count, 0)
    words = "31256 31526 35126 35216 35261 35621 36521 36251".split()
    path = [tuple(map(int, w))+(4,) for w in words]
    adj = graph(6)
    assert all(b in adj[a] for a, b in zip(path, path[1:]))
    a, b = path[0], path[-1]
    assert (distances(adj, a)[b], kendall(a, b)) == (7, 5)
    print("order-six intrinsic and unrestricted distances: 7 5")


if __name__ == "__main__":
    run()
