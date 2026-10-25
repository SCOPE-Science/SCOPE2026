"""Exhaustive independent checks of the clique-bouquet zero-forcing theorem.
Run: python3 verify.py (Python >=3.8, standard library only).
"""
from collections import Counter, deque
from itertools import product
from math import prod


def graph(sizes):
    # Vertex 0 is the hub, the other vertices are grouped in disjoint blades.
    parts = []
    idx = 1
    for m in sizes:
        parts.append(tuple(range(idx, idx + m)))
        idx += m
    neighbors = [set() for _ in range(idx)]
    for part in parts:
        vertices = (0,) + part
        for i, v in enumerate(vertices):
            for w in vertices[i + 1:]:
                neighbors[v].add(w)
                neighbors[w].add(v)
    return parts, neighbors


def forceable(blue_mask, neighbors):
    n = len(neighbors)
    blue = {i for i in range(n) if blue_mask >> i & 1}
    while True:
        new = set()
        for v in blue:
            white = neighbors[v] - blue
            if len(white) == 1:
                new.update(white)
        if not new:
            return len(blue) == n
        blue.update(new)


def independent(white_mask, parts):
    if any(sum((white_mask >> v) & 1 for v in part) > 1 for part in parts):
        return False
    return (white_mask.bit_count() <= len(parts))


def verify(sizes):
    parts, neighbors = graph(sizes)
    n, k = len(neighbors), len(parts)
    full = (1 << n) - 1
    computed = Counter()
    base = []
    for x in range(1 << n):
        brute = forceable(x, neighbors)
        predicted = independent(full ^ x, parts)
        assert brute == predicted, (sizes, x, brute, predicted)
        if brute:
            computed[x.bit_count()] += 1
            if x.bit_count() == n - k:
                base.append(full ^ x)
    # Independent-set generating polynomial, computed by direct combinatorial convolution.
    poly = [1]
    for m in sizes:
        new = [0] * (len(poly) + 1)
        for d, a in enumerate(poly):
            new[d] += a
            new[d + 1] += m * a
        poly = new
    before = [0] * (len(poly) + 1)
    for i, a in enumerate(poly):
        before[i] += a
        before[i + 1] += a
    before[-1] -= prod(sizes)
    assert all(computed[n - j] == a for j, a in enumerate(before)), sizes
    p = prod(sizes)
    assert len(base) == p + sum(p // m for m in sizes)
    adj = {b: [c for c in base if (b ^ c).bit_count() == 2] for b in base}
    # Derive all-pairs distances by breadth-first search, not via matroid theory.
    max_distance = 0
    for b in base:
        dist = {b: 0}
        queue = deque([b])
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        assert len(dist) == len(base), sizes
        for c, distance in dist.items():
            assert distance == (b ^ c).bit_count() // 2, (sizes, b, c)
            max_distance = max(max_distance, distance)
        if b & 1:
            missing = [i for i, part in enumerate(parts) if not any(b >> v & 1 for v in part)]
            assert len(missing) == 1
            i = missing[0]
            predicted_degree = sum(sizes[j] - 1 for j in range(k) if j != i) + k * sizes[i]
        else:
            predicted_degree = sum(sizes)
        assert len(adj[b]) == predicted_degree, (sizes, b, len(adj[b]), predicted_degree)
    assert max_distance == k
    return (sizes, n, len(base), max_distance, sum(map(len, adj.values())) // 2)


if __name__ == '__main__':
    for sizes in [(2, 2), (2, 3), (3, 3), (2, 2, 2), (2, 3, 2),
                  (3, 2, 3), (2, 2, 2, 2), (3, 3, 2, 2)]:
        print('OK sizes={} vertices={} minimum_sets={} diameter={} edges={}'.format(*verify(sizes)))
    print('VERIFICATION_OK')
