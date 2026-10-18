#!/usr/bin/env python3
"""Direct graph-level verification of induced and maximal matchings in clique subdivisions."""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, factorial


def stirling2(n, k):
    if n == k == 0:
        return 1
    if k == 0:
        return 0
    a = [[0] * (k + 1) for _ in range(n + 1)]
    a[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            a[i][j] = a[i-1][j-1] + j*a[i-1][j]
    return a[n][k]


def check(n):
    vertices = [('o', i) for i in range(n)] + [('m', i, j) for i, j in combinations(range(n), 2)]
    edges = []
    for i, j in combinations(range(n), 2):
        edges.append((('o', i), ('m', i, j)))
        edges.append((('o', j), ('m', i, j)))
    vertex_set = set(vertices)
    assert all(a in vertex_set and b in vertex_set for a, b in edges)
    # Independent graph-level calculation: a pair of graph edges is in conflict
    # exactly if their four endpoints fail to induce two disjoint graph edges.
    adjacency = defaultdict(set)
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    def compatible(e1, e2):
        endpoints1, endpoints2 = set(e1), set(e2)
        return not (endpoints1 & endpoints2 or any(v in adjacency[u] for u in endpoints1 for v in endpoints2))
    count = len(edges)
    conflicts = [0] * count
    for i, j in combinations(range(count), 2):
        if not compatible(edges[i], edges[j]):
            conflicts[i] |= 1 << j
            conflicts[j] |= 1 << i
    allmask = (1 << count) - 1
    independent = Counter()
    maximal = Counter()
    maximal_records = []
    n_instances = 0

    def enumerate_matchings(chosen, available, blocked):
        nonlocal n_instances
        independent[len(chosen)] += 1
        n_instances += 1
        if blocked == allmask:
            maximal[len(chosen)] += 1
            maximal_records.append(tuple(chosen))
        while available:
            lowbit = available & -available
            i = lowbit.bit_length()-1
            available ^= lowbit
            new_blocked = blocked | conflicts[i] | lowbit
            enumerate_matchings(chosen+(i,), available & ~new_blocked, new_blocked)

    enumerate_matchings((), allmask, 0)
    expected_induced = {k: comb(n,k)*(n-k)**k for k in range(n)}
    expected_max = {
        k: comb(n,k)*factorial(n-k)*stirling2(k,n-k)
        for k in range(1,n)
        if 2*k >= n
    }
    assert dict(independent) == expected_induced, (n, independent, expected_induced)
    assert dict(maximal) == expected_max, (n, maximal, expected_max)
    if n % 2 == 1:
        k = (n + 1)//2
        minima = {frozenset(r) for r in maximal_records if len(r) == k}
        buckets = defaultdict(list)
        for state in minima:
            for dropped in state:
                buckets[state - {dropped}].append(state)
        neighbors = {state: set() for state in minima}
        for bucket in buckets.values():
            for left, right in combinations(bucket, 2):
                neighbors[left].add(right)
                neighbors[right].add(left)
        expected_degree = 3*((n-3)//2)
        assert set(map(len, neighbors.values())) == {expected_degree}, (n, Counter(map(len,neighbors.values())))
        unseen = set(minima)
        components = []
        while unseen:
            start = unseen.pop()
            stack = [start]
            component_size = 1
            while stack:
                state = stack.pop()
                for nxt in neighbors[state] & unseen:
                    unseen.remove(nxt)
                    stack.append(nxt)
                    component_size += 1
            components.append(component_size)
        assert len(components) == (3 if n==3 else 1), (n, components)
        assert sum(components) == len(minima)
    if n % 2 == 0:
        m = n//2
        minima = {frozenset(r) for r in maximal_records if len(r)==m}
        # Build the graph of minimum maximal induced matchings by single-edge swaps.
        components = []
        unseen = set(minima)
        degrees = set()
        while unseen:
            start = unseen.pop()
            todo = [start]
            component = {start}
            while todo:
                v = todo.pop()
                neighbors = set()
                for removed in v:
                    base = v - {removed}
                    for added in range(count):
                        if added not in v:
                            nxt = frozenset(base | {added})
                            if nxt in minima:
                                neighbors.add(nxt)
                degrees.add(len(neighbors))
                for nxt in neighbors:
                    if nxt not in component:
                        component.add(nxt)
                        todo.append(nxt)
                        unseen.discard(nxt)
            components.append(component)
        # Every component is precisely a hypercube on its underlying pairs.
        assert len(components) == factorial(n)//(2**m * factorial(m)), (n, len(components))
        assert all(len(c) == 2**m for c in components), n
        assert degrees == {m}, (n, degrees)
        for component in components:
            pair_signatures = []
            for matching in component:
                sig = frozenset(frozenset((i,j)) for edge_index in matching for _tag, i, j in [edges[edge_index][1]])
                pair_signatures.append(sig)
            assert len(set(pair_signatures)) == 1
    return count, n_instances, dict(sorted(maximal.items())), len(maximal_records)

if __name__ == '__main__':
    grand_total = 0
    for n in range(2,10):
        edge_count, instances, maximal_counts, total_max = check(n)
        grand_total += instances
        print(f'n={n} graph_edges={edge_count} induced_matchings={instances} maximal_by_size={maximal_counts} maximal_total={total_max}')
    print(f'VERIFICATION_OK n=2..9 induced_matchings_checked={grand_total} reconfiguration_orders=2..9')
