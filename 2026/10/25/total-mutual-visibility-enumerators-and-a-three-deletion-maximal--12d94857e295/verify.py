#!/usr/bin/env python3
"""Direct finite verification of total mutual-visibility enumerators.

Uses actual shortest paths; never assumes the proposed omission criterion.
"""
from collections import Counter, deque
from math import comb


def graph(p, q, t):
    adj = [set() for _ in range(p + q)]
    for a in range(p):
        for b in range(q):
            if a == b and a < t:
                continue
            adj[a].add(p + b)
            adj[p + b].add(a)
    return adj


def shortest_path_interiors(adj):
    n = len(adj)
    distances = []
    for root in range(n):
        d = [10**8] * n
        d[root] = 0
        que = deque([root])
        while que:
            x = que.popleft()
            for y in adj[x]:
                if d[y] > d[x] + 1:
                    d[y] = d[x] + 1
                    que.append(y)
        assert all(z < 10**8 for z in d)
        distances.append(d)
    pairs = []
    for root in range(n):
        for target in range(root + 1, n):
            interiors = []
            def grow(x, path):
                if x == target:
                    interiors.append(sum(1 << w for w in path[1:-1]))
                    return
                for y in adj[x]:
                    if (distances[root][y] == distances[root][x] + 1
                            and distances[root][y] + distances[y][target]
                            == distances[root][target]):
                        grow(y, path + [y])
            grow(root, [root])
            assert interiors
            pairs.append(interiors)
    return pairs


def derived_allowed(mask, p, q, t):
    left = {i for i in range(p) if not ((mask >> i) & 1)}
    right = {j for j in range(q) if not ((mask >> (p + j)) & 1)}
    return (bool(any(i >= t for i in left) or len(left) >= 3)
            and bool(any(j >= t for j in right) or len(right) >= 3))


def direct_trial(p, q, t):
    n = p + q
    interiors = shortest_path_interiors(graph(p, q, t))
    valid = set()
    all_coefficients = Counter()
    for mask in range(1 << n):
        is_valid = all(any((middle & mask) == 0 for middle in paths)
                       for paths in interiors)
        assert is_valid == derived_allowed(mask, p, q, t), (p, q, t, mask)
        if is_valid:
            valid.add(mask)
            a = sum((mask >> j) & 1 for j in range(p))
            b = sum((mask >> (p + j)) & 1 for j in range(q))
            all_coefficients[a, b] += 1
    maximal = Counter()
    for mask in valid:
        if all((mask | (1 << j)) not in valid
               for j in range(n) if not ((mask >> j) & 1)):
            a = sum((mask >> j) & 1 for j in range(p))
            b = sum((mask >> (p + j)) & 1 for j in range(q))
            maximal[a, b] += 1

    def part_coefficients(r):
        out = {}
        for k in range(r + 1):
            out[k] = comb(r, k) - (
                comb(t, r - k) if 0 <= r - k <= min(2, t) else 0
            )
        return out
    fa, fb = part_coefficients(p), part_coefficients(q)
    expected_all = Counter()
    for i, ai in fa.items():
        for j, bj in fb.items():
            if ai * bj:
                expected_all[i, j] = ai * bj
    assert all_coefficients == expected_all, (p, q, t)
    u, v, c = p - t, q - t, comb(t, 3) if t >= 3 else 0
    left_max = Counter({p - 1: u})
    right_max = Counter({q - 1: v})
    if c:
        left_max[p - 3] += c
        right_max[q - 3] += c
    expected_maximal = Counter()
    for i, ai in left_max.items():
        for j, bj in right_max.items():
            expected_maximal[i, j] += ai * bj
    assert maximal == expected_maximal, (p, q, t)
    if 1 <= t < min(p, q):
        assert sum(all_coefficients.values()) == (
            (2**p - 1 - t - comb(t, 2))
            * (2**q - 1 - t - comb(t, 2))
        )
    return (p, q, t)


def main():
    trials = [direct_trial(p, q, t)
              for p in range(3, 6)
              for q in range(3, 6)
              for t in range(min(p, q) + 1)]
    print("PASS: %d exhaustive parameter instances" % len(trials))


if __name__ == '__main__':
    main()
