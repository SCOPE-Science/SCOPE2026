#!/usr/bin/env python3
"""Recompute local obstructions and small cases for total visibility in Fibonacci cubes.

Only Python standard-library modules are needed. No precomputed tables or files.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations


def vertices(n):
    return tuple(x for x in range(1 << n) if not (x & (x << 1)))


def adjacency(n, vs):
    st = set(vs)
    return {x: tuple(x ^ (1 << i) for i in range(n)
                     if x ^ (1 << i) in st) for x in vs}


def no_bad_zero_pair(n, x):
    moves = []
    for i in range(n):
        if (x >> i) & 1:
            continue
        y = x ^ (1 << i)
        if not (y & (y << 1)):
            moves.append(i)
    return all(j != i + 1 for i, j in zip(moves, moves[1:]))


def no_long_zero_run(n, x):
    if x == 0:
        return False
    ones = [i for i in range(n) if (x >> i) & 1]
    gaps = [ones[0], n - 1 - ones[-1]]
    internal = [b - a - 1 for a, b in zip(ones, ones[1:])]
    return max(gaps) <= 2 and all(1 <= t <= 3 for t in internal)


def candidate_graph(n):
    vs = vertices(n)
    nn = adjacency(n, vs)
    eligible = tuple(x for x in vs if no_bad_zero_pair(n, x))
    edges = set()
    for ia, a in enumerate(eligible):
        for ib in range(ia):
            b = eligible[ib]
            if (a ^ b).bit_count() != 2:
                continue
            common = set(nn[a]).intersection(nn[b])
            if len(common) == 2:
                edges.add((ib, ia))
    return vs, nn, eligible, edges


def recurrence(n):
    a = [0] * (max(n, 5) + 1)
    a[1:6] = [1, 2, 4, 5, 8]
    for j in range(6, n + 1):
        a[j] = a[j - 2] + a[j - 3] + a[j - 4]
    return a[n]


def distance(nn, root):
    d = {root: 0}
    q = deque([root])
    while q:
        x = q.popleft()
        for y in nn[x]:
            if y not in d:
                d[y] = d[x] + 1
                q.append(y)
    return d


def actually_total_visible(vs, nn, blocked, distances):
    """Independent global all-pairs shortest-path test."""
    for src in vs:
        d = distances[src]
        for dest in vs:
            if d[dest] <= 1:
                continue
            q = deque([src])
            reached = {src}
            while q and dest not in reached:
                x = q.popleft()
                for y in nn[x]:
                    if (y not in blocked or y == dest) and y not in reached \
                            and d[y] == d[x] + 1:
                        reached.add(y)
                        q.append(y)
            if dest not in reached:
                return False
    return True


def local_condition(eligible, edges, selection):
    return all(not (selection >> a & 1 and selection >> b & 1)
               for a, b in edges)


def brute_small():
    for n in range(2, 7):
        vs, nn, eligible, edges = candidate_graph(n)
        dist = {u: distance(nn, u) for u in vs}
        # Verify no midpoint obstruction has been overlooked.
        for x in vs:
            admissible_singleton = all(
                len(set(nn[u]).intersection(nn[v]) - {x}) >= 1
                for u, v in combinations(nn[x], 2)
            )
            assert admissible_singleton == (x in eligible)
            if n >= 2:
                assert no_long_zero_run(n, x) == (x in eligible)
        for mask in range(1 << len(eligible)):
            blocked = {eligible[i] for i in range(len(eligible)) if mask >> i & 1}
            global_check = actually_total_visible(vs, nn, blocked, dist)
            assert global_check == local_condition(eligible, edges, mask), \
                (n, blocked, global_check)
        print('direct_geodesics', n, 'candidates', 1 << len(eligible), 'OK')


def polynomial_components(n):
    vs, nn, eligible, edges = candidate_graph(n)
    nbr = [0] * len(eligible)
    for a, b in edges:
        nbr[a] |= 1 << b
        nbr[b] |= 1 << a

    seen = set()
    components = []
    for i in range(len(eligible)):
        if i in seen:
            continue
        stack = [i]
        seen.add(i)
        component = []
        while stack:
            v = stack.pop()
            component.append(v)
            for w in range(len(eligible)):
                if ((nbr[v] >> w) & 1) and w not in seen:
                    seen.add(w)
                    stack.append(w)
        components.append(component)

    coeff = (1,)
    for comp in components:
        local = [sum((1 << j) for j, w in enumerate(comp)
                     if (nbr[v] >> w) & 1) for v in comp]

        @lru_cache(None)
        def poly(mask):
            if not mask:
                return (1,)
            bit = mask & -mask
            i = bit.bit_length() - 1
            p0 = poly(mask ^ bit)
            p1 = poly((mask ^ bit) & ~local[i])
            result = [0] * max(len(p0), len(p1) + 1)
            for j, count in enumerate(p0):
                result[j] += count
            for j, count in enumerate(p1):
                result[j + 1] += count
            return tuple(result)

        q = poly((1 << len(comp)) - 1)
        product = [0] * (len(coeff) + len(q) - 1)
        for i, a in enumerate(coeff):
            for j, b in enumerate(q):
                product[i + j] += a * b
        coeff = tuple(product)
    degree = len(coeff) - 1
    assert recurrence(n) == len(eligible)
    assert all(no_long_zero_run(n, x) for x in eligible)
    # Independent construction of all rank-two midpoint obstructions.
    expected = set()
    for u, v in combinations(vs, 2):
        middles = list(set(nn[u]).intersection(nn[v]))
        assert len(middles) <= 2
        if len(middles) == 2 and all(x in eligible for x in middles):
            pair = tuple(sorted(eligible.index(x) for x in middles))
            expected.add(pair)
    assert edges == expected
    assert 0 < degree <= len(eligible)
    assert (1 + n * (n - 1) // 2) * degree >= len(eligible)
    return len(vs), len(eligible), len(edges), degree, coeff[-1], sum(coeff)


def main():
    brute_small()
    for n in range(2, 15):
        row = polynomial_components(n)
        print('dimension,vertices,eligible,conflicts,max,total_max_sets,total_sets',
              n, *row)
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
