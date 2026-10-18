#!/usr/bin/env python3
"""Direct finite geodesic-cover checks for Hamming products."""
from itertools import product, permutations
from collections import Counter


def shortest_paths(u, v):
    differing = [i for i in range(len(u)) if u[i] != v[i]]
    for order in permutations(differing):
        cur = list(u)
        path = [u]
        for i in order:
            cur[i] = v[i]
            path.append(tuple(cur))
        yield tuple(path)


def path_cover_number(vertices, rooted_paths):
    index = {v: i for i, v in enumerate(vertices)}
    full = (1 << len(index)) - 1
    masks = set()
    for path in rooted_paths:
        mask = 0
        for v in path:
            i = index.get(v)
            if i is not None:
                mask |= 1 << i
        if mask:
            masks.add(mask)
    # A geodesic only contributes its vertex intersection. The subset DP
    # explores every collection of rooted paths, not just consecutive blocks.
    best = [999] * (1 << len(index))
    best[0] = 0
    for mask in sorted(masks):
        for state in range(full, -1, -1):
            nxt = state | mask
            if best[state] + 1 < best[nxt]:
                best[nxt] = best[state] + 1
    return best[full]


def main():
    cases = [(2, d) for d in range(1, 6)] + [(3, d) for d in range(1, 4)] + [(4, d) for d in range(1, 3)]
    total = 0
    for q, d in cases:
        points = list(product(range(q), repeat=d))
        root = tuple([0] * d)
        root_paths = list(path for endpoint in points for path in shortest_paths(root, endpoint))
        unique_geodesics = {}
        for u in points:
            for v in points:
                if u > v:
                    continue
                for path in shortest_paths(u, v):
                    key = frozenset(path)
                    unique_geodesics.setdefault(key, tuple(path))
        distribution = Counter()
        maximum = 0
        for path in unique_geodesics.values():
            minimum = path_cover_number(path, root_paths)
            maximum = max(maximum, minimum)
            distribution[minimum] += 1
            total += 1
        expect = (d + 2) // 2 if q == 2 else d + 1
        assert maximum == expect, (q, d, maximum, expect)
        print(f'q={q} d={d} vertices={len(points)} rooted={len(root_paths)} distinct_geodesics={len(unique_geodesics)} ipco_at_zero={maximum} histogram={sorted(distribution.items())}')
    print(f'GEODESICS_TESTED={total}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
