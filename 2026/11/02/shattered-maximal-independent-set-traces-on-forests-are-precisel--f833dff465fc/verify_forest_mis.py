"""Independent finite checks for shattering by maximal independent vertex sets.

Standard-library Python 3. No external data required.
Run: python3 forest_mis_verify.py
"""
from itertools import combinations


def adjacency(n, edges):
    a = [0] * n
    for u, v in edges:
        a[u] |= 1 << v
        a[v] |= 1 << u
    return a


def is_forest(n, edges):
    parent = list(range(n))
    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def maximal_independent_sets(n, adj):
    out = []
    for mask in range(1 << n):
        if any((adj[v] & mask) for v in range(n) if mask >> v & 1):
            continue
        if all((mask >> v & 1) or (adj[v] & mask) for v in range(n)):
            out.append(mask)
    return out


def shattered_supports(n, mis):
    results = set()
    for s in range(1 << n):
        if len({x & s for x in mis}) == (1 << s.bit_count()):
            results.add(s)
    return results


def matching_sides(n, edges):
    results = {0}
    for choice in range(1 << len(edges)):
        chosen = [edges[i] for i in range(len(edges)) if choice >> i & 1]
        endpoints = 0
        for u, v in chosen:
            endpoints |= (1 << u) | (1 << v)
        if endpoints.bit_count() != 2 * len(chosen):
            continue
        if sum(1 for u, v in edges if ((endpoints >> u) & 1) and ((endpoints >> v) & 1)) != len(chosen):
            continue
        for side in range(1 << len(chosen)):
            s = 0
            for k, (u, v) in enumerate(chosen):
                s |= 1 << (v if side >> k & 1 else u)
            results.add(s)
    return results


def check(n, edges):
    mis = maximal_independent_sets(n, adjacency(n, edges))
    actual = shattered_supports(n, mis)
    predicted = matching_sides(n, edges)
    assert actual == predicted, (n, edges, sorted(actual ^ predicted))
    return len(actual)


def main():
    total_forests = 0
    total_supports = 0
    total_queries = 0
    for n in range(0, 7):
        potential = list(combinations(range(n), 2))
        count = supports = 0
        for mask in range(1 << len(potential)):
            edges = [potential[j] for j in range(len(potential)) if mask >> j & 1]
            if not is_forest(n, edges):
                continue
            supports += check(n, edges)
            count += 1
            total_queries += 1 << n
        total_forests += count
        total_supports += supports
        print(f'FORESTS_ORDER_{n} {count} SHATTERED_SUPPORTS {supports}')
    # This cyclic obstruction proves the forest hypothesis cannot simply be removed.
    cycle = [(i, (i+1) % 5) for i in range(5)]
    mis = maximal_independent_sets(5, adjacency(5, cycle))
    sh = shattered_supports(5, mis)
    ind = matching_sides(5, cycle)
    assert (1 << 0 | 1 << 2) in sh and (1 << 0 | 1 << 2) not in ind
    assert max(s.bit_count() for s in sh) == 2
    assert max(s.bit_count() for s in ind) == 1
    print(f'TOTAL_FORESTS {total_forests} TOTAL_SUPPORT_QUERIES {total_queries} TOTAL_SHATTERED_SUPPORTS {total_supports}')
    print('C5_OBSTRUCTION VC_2 INDUCED_MATCHING_1')
    print('ALL_FOREST_SHATTERING_CHECKS_PASS')


if __name__ == '__main__':
    main()
