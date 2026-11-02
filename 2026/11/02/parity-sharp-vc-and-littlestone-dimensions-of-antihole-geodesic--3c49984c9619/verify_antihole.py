#!/usr/bin/env python3
"""Independent exhaustive checks of antihole geodesic-convexity learning assertions."""
from collections import deque
from functools import lru_cache
from math import comb


def cycle_independent(n):
    return [s for s in range(1 << n)
            if all(not ((s >> i) & 1 and (s >> ((i + 1) % n)) & 1)
                   for i in range(n))]


def shortest_path_convex_sets(n):
    neighbors = [tuple(v for v in range(n)
                       if v != u and (v - u) % n not in (1, n - 1))
                 for u in range(n)]
    distances = []
    for source in range(n):
        dist = [n + 1] * n
        dist[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in neighbors[u]:
                if dist[v] == n + 1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        assert max(dist) == 2
        distances.append(dist)
    intervals = [[sum(1 << x for x in range(n)
                      if distances[u][x] + distances[x][v] == distances[u][v])
                  for v in range(n)] for u in range(n)]
    convex = []
    for mask in range(1 << n):
        verts = [i for i in range(n) if (mask >> i) & 1]
        if all(not (intervals[u][v] & ~mask) for u in verts for v in verts):
            convex.append(mask)
    return convex


def shattered_polynomial(hypotheses, n):
    poly = [0] * (n + 1)
    for support in range(1 << n):
        vertices = [i for i in range(n) if (support >> i) & 1]
        traces = {sum(1 << j for j, v in enumerate(vertices)
                      if (h >> v) & 1) for h in hypotheses}
        if len(traces) == (1 << len(vertices)):
            poly[len(vertices)] += 1
    return poly


def littlestone_dimension(hypotheses, n):
    queries = [sum(1 << j for j, hyp in enumerate(hypotheses)
                   if (hyp >> i) & 1) for i in range(n)]
    @lru_cache(None)
    def solve(version_space):
        if version_space.bit_count() <= 1:
            return 0
        best = 0
        for positives in queries:
            yes = version_space & positives
            no = version_space & ~positives
            if yes and no:
                best = max(best, 1 + min(solve(yes), solve(no)))
        return best
    result = solve((1 << len(hypotheses)) - 1)
    return result, solve.cache_info().currsize


def augmented_path_dimension(m):
    hypotheses = [s for s in range(1 << m)
                  if all(not ((s >> i) & 1 and (s >> (i + 1)) & 1)
                         for i in range(m - 1))]
    hypotheses.append((1 << (m + 1)) - 1)
    return littlestone_dimension(hypotheses, m + 1)[0]


def main():
    for n in range(7, 14):
        independent = cycle_independent(n)
        convex = shortest_path_convex_sets(n)
        assert set(convex) == set(independent) | {(1 << n) - 1}, n
        expected = [0] * (n + 1)
        expected[0] = 1
        for k in range(1, n // 2 + 1):
            expected[k] = n * comb(n - k, k) // (n - k)
        expected[2] += n
        observed = shattered_polynomial(convex, n)
        assert observed == expected, (n, observed, expected)
        print(f'GRAPH_AND_SHATTERING_PASS n={n} hypotheses={len(convex)} '
              f'polynomial={observed[:n // 2 + 1]}')
    for n in range(7, 15):
        hypotheses = cycle_independent(n) + [(1 << n) - 1]
        ld, states = littlestone_dimension(hypotheses, n)
        expected = (n + 1) // 2
        assert ld == expected, (n, ld, expected)
        print(f'ONLINE_PASS n={n} ldim={ld} memo_states={states}')
    for m in range(0, 15):
        ld = augmented_path_dimension(m)
        assert ld == (m // 2) + 1, (m, ld)
    print('AUGMENTED_PATH_LEMMA_CHECK_PASS m=0..14')
    print('ALL_ANTIHOLE_GEODESIC_LEARNING_CHECKS_PASS')


if __name__ == '__main__':
    main()
