#!/usr/bin/env python3
"""Reproducible checks for the complete-multipartite geodesic-packing theorem."""
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from random import Random


def formula(parts):
    assert len(parts) >= 2 and min(parts) >= 1
    n = sum(parts)
    if max(parts) == 1:
        return n // 2, n // 2
    singles = sum(x == 1 for x in parts)
    q = sum(x // 2 for x in parts)
    a = max(parts)
    scored = [
        (min((n + e) // 3, n - a - e, q + e), e)
        for e in range(singles // 2 + 1)
    ]
    return max(scored)


def from_graph(parts):
    """Enumerate all maximal shortest paths from adjacency, then exact packing."""
    partof = [i for i, s in enumerate(parts) for _ in range(s)]
    n = len(partof)
    adj = [[u != v and partof[u] != partof[v] for v in range(n)] for u in range(n)]
    paths = set()
    for u, v in combinations(range(n), 2):
        if adj[u][v]:
            extends = any(
                (adj[u][w] and not adj[w][v]) or
                (adj[v][w] and not adj[w][u])
                for w in range(n) if w not in (u, v)
            )
            if not extends:
                paths.add((1 << u) | (1 << v))
        else:
            for w in range(n):
                if adj[u][w] and adj[w][v]:
                    paths.add((1 << u) | (1 << w) | (1 << v))
    by_vertex = [[] for _ in range(n)]
    for path in paths:
        for v in range(n):
            if (path >> v) & 1:
                by_vertex[v].append(path)

    @lru_cache(None)
    def solve(mask):
        if mask == 0:
            return 0
        bit = mask & -mask
        v = bit.bit_length() - 1
        best = solve(mask ^ bit)
        for path in by_vertex[v]:
            if path & mask == path:
                best = max(best, 1 + solve(mask ^ path))
        return best
    return solve((1 << n) - 1), len(paths), solve.cache_info().currsize


def witness(parts):
    """Construct optimum geodesics via pair allocation and a Hall matching."""
    value, e = formula(parts)
    vertices = [[(i, j) for j in range(x)] for i, x in enumerate(parts)]
    singleton = [i for i, x in enumerate(parts) if x == 1]
    paths = []
    for a, b in zip(singleton[: 2 * e : 2], singleton[1 : 2 * e : 2]):
        paths.append((vertices[a].pop(), vertices[b].pop()))
    ns = [len(x) for x in vertices]
    N = sum(ns)
    t = min(N // 3, N - max(ns), sum(x // 2 for x in ns))
    assert t + e == value
    if not t:
        return paths
    lower = [max(0, x - (N - 2 * t)) for x in ns]
    alloc = lower[:]
    assert sum(alloc) <= t
    remaining = t - sum(alloc)
    for i, x in enumerate(ns):
        add = min(remaining, x // 2 - alloc[i])
        alloc[i] += add
        remaining -= add
    assert remaining == 0 and sum(alloc) == t
    paired = []
    for i, count in enumerate(alloc):
        for _ in range(count):
            paired.append((i, vertices[i].pop(), vertices[i].pop()))
    center_vertices = [v for part in vertices for v in part]
    owner = {v: i for i, part in enumerate(vertices) for v in part}
    matched_to = {}

    def augment(pair_index, used):
        i = paired[pair_index][0]
        for v in center_vertices:
            if v in used or owner[v] == i:
                continue
            used.add(v)
            if v not in matched_to or augment(matched_to[v], used):
                matched_to[v] = pair_index
                return True
        return False

    for idx in range(t):
        assert augment(idx, set()), (parts, t, idx)
    centers = {idx: v for v, idx in matched_to.items()}
    assert len(centers) == t
    for j, (i, a, b) in enumerate(paired):
        paths.append((a, centers[j], b))
    seen = set()
    for path in paths:
        assert len(set(path)) == len(path)
        for v in path:
            assert v not in seen
            seen.add(v)
        if len(path) == 2:
            assert parts[path[0][0]] == parts[path[1][0]] == 1
        else:
            assert path[0][0] == path[2][0] != path[1][0]
    assert len(paths) == value
    return paths


def main():
    cases = states = paths_count = 0
    for n in range(2, 14):
        for k in range(2, n + 1):
            for parts in combinations_with_replacement(range(1, n + 1), k):
                if sum(parts) != n:
                    continue
                target = formula(parts)[0]
                actual, pcount, state_count = from_graph(parts)
                assert actual == target, (parts, actual, target)
                assert len(witness(parts)) == target
                cases += 1
                states += state_count
                paths_count += pcount
    print('exhaustive_partitions=%d, dynamic_programming_states=%d, enumerated_geodesics=%d, orders=2..13: PASS' % (cases, states, paths_count))
    rng = Random(173552)
    for k in range(2, 35):
        for j in range(30):
            parts = [rng.randint(1, 30) for _ in range(k)]
            w = witness(parts)
            assert len(w) == formula(parts)[0]
    print('constructive_random_witnesses=%d, parts_per_instance=2..34: PASS' % (33*30))
    for parts, expected in [((2, 2),1),((3,3),2),((2,1,1,1,1,1),3),((5,1,1,1,1),3),((100,1,1,1,1),4),((1,)*12,6)]:
        assert formula(parts)[0] == expected
    print('targeted_boundary_instances=6: PASS')

if __name__ == '__main__':
    main()
