#!/usr/bin/env python3
from collections import deque


def vertices(d, a, b):
    return [m for m in range(1 << d) if a <= m.bit_count() <= b]


def adjacent(x, y, a, b):
    px, py = x.bit_count(), y.bit_count()
    if abs(px - py) == 1:
        lo, hi = (x, y) if px < py else (y, x)
        return (lo & hi) == lo and (lo ^ hi).bit_count() == 1
    if px == py and px in (a, b):
        return (x ^ y).bit_count() == 2
    return False


def claimed_distance(x, y, a, b):
    p, q = x.bit_count(), y.bit_count()
    r = (x & y).bit_count()
    h = p + q - 2 * r
    lower = p + q - a - min(a, r)
    upper = 2 * b - p - q + max(0, p + q - r - b)
    return min(h, lower, upper)


def check(max_d=8):
    intervals = 0
    ordered_pairs = 0
    for d in range(2, max_d + 1):
        for a in range(d + 1):
            for b in range(a + 1, d + 1):
                vs = vertices(d, a, b)
                graph = {v: [] for v in vs}
                for i, v in enumerate(vs):
                    for w in vs[i + 1:]:
                        if adjacent(v, w, a, b):
                            graph[v].append(w)
                            graph[w].append(v)
                diameter = 0
                for s in vs:
                    dist = {s: 0}
                    queue = deque([s])
                    while queue:
                        v = queue.popleft()
                        for w in graph[v]:
                            if w not in dist:
                                dist[w] = dist[v] + 1
                                queue.append(w)
                    assert len(dist) == len(vs), ("disconnected", d, a, b)
                    for t, actual in dist.items():
                        expected = claimed_distance(s, t, a, b)
                        assert actual == expected, ("distance", d, a, b, s, t, actual, expected)
                    ordered_pairs += len(vs)
                    diameter = max(diameter, max(dist.values()))
                assert diameter == min(b, d - a), ("diameter", d, a, b, diameter)
                intervals += 1
    print(f"VERIFY_OK consecutive-layer S-hypersimplex metric intervals={intervals} ordered_pairs={ordered_pairs} max_d={max_d}")


if __name__ == "__main__":
    check()
