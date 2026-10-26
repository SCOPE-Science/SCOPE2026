#!/usr/bin/env python3
"""Exact certificate for connected-dominating-set exchanges in two 16-vertex graphs.

Run: python3 verify.py
Only Python standard-library modules are required.
"""
from collections import Counter, deque
from itertools import combinations

N = 16
FULL = (1 << N) - 1


def neighbors(kind):
    a = [0] * N
    for u in range(N):
        x, y = divmod(u, 4)
        for v in range(N):
            X, Y = divmod(v, 4)
            dx, dy = (X - x) % 4, (Y - y) % 4
            if kind == "shrikhande":
                linked = (dx, dy) in ((1, 0), (3, 0), (0, 1),
                                      (0, 3), (1, 1), (3, 3))
            else:
                linked = u != v and (x == X or y == Y)
            if linked:
                a[u] |= 1 << v
    return a


def induced_connected(s, adj):
    if not s:
        return False
    reached = s & -s
    while True:
        next_reached = reached
        t = reached
        while t:
            b = t & -t
            next_reached |= adj[b.bit_length() - 1] & s
            t -= b
        if reached == next_reached:
            return reached == s
        reached = next_reached


def dominates(s, adj):
    reached = s
    t = s
    while t:
        b = t & -t
        reached |= adj[b.bit_length() - 1]
        t -= b
    return reached == FULL


def connected_dominating_sets(adj):
    result = {k: [] for k in (1, 2, 3, 4, 5, 6)}
    for mask in range(1, FULL + 1):
        k = mask.bit_count()
        if k not in result:
            continue
        if dominates(mask, adj) and induced_connected(mask, adj):
            result[k].append(mask)
    return result


def exchange_graph(states):
    lookup = {mask: i for i, mask in enumerate(states)}
    out = [set() for _ in states]
    for i, mask in enumerate(states):
        in_bits = [a for a in range(N) if mask & (1 << a)]
        out_bits = [b for b in range(N) if not mask & (1 << b)]
        for a in in_bits:
            for b in out_bits:
                other = mask ^ (1 << a) ^ (1 << b)
                j = lookup.get(other)
                if j is not None:
                    out[i].add(j)
    assert all(i in out[j] for i, row in enumerate(out) for j in row)
    return out


def component_indices(graph):
    unseen = set(range(len(graph)))
    comps = []
    while unseen:
        origin = min(unseen)
        seen = {origin}
        queue = deque([origin])
        while queue:
            for v in graph[queue.popleft()]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        unseen.difference_update(seen)
        comps.append(seen)
    return comps


def eccentricities(graph):
    ecc = []
    for src in range(len(graph)):
        distances = {src: 0}
        queue = deque([src])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v not in distances:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        ecc.append(max(distances.values()))
    return ecc


def graph_checks(kind):
    adj = neighbors(kind)
    assert all(a.bit_count() == 6 for a in adj)
    assert all((adj[u] >> v) & 1 == (adj[v] >> u) & 1
               for u in range(N) for v in range(N))
    for u, v in combinations(range(N), 2):
        common = (adj[u] & adj[v]).bit_count()
        assert common == (2 if adj[u] & (1 << v) else 2)
    states = connected_dominating_sets(adj)
    assert all(not states[k] for k in (1, 2, 3))
    expected_counts = ((32, 672, 4064) if kind == "shrikhande"
                       else (8, 384, 3744))
    for k, n in zip((4, 5, 6), expected_counts):
        assert len(states[k]) == n, (kind, k, len(states[k]))
    # Exact equality classification of the optimum configurations.
    if kind == "shrikhande":
        claws = set()
        for center in range(N):
            x, y = divmod(center, 4)
            for parity in (0, 1):
                # An open neighborhood is a 6-cycle; take alternating vertices.
                ring = ((x + 1, y), (x + 1, y + 1), (x, y + 1),
                        (x - 1, y), (x - 1, y - 1), (x, y - 1))
                m = 1 << center
                for pos in (parity, parity + 2, parity + 4):
                    X, Y = ring[pos]
                    m |= 1 << (((X % 4) * 4) + Y % 4)
                claws.add(m)
        assert len(claws) == 32
        assert set(states[4]) == claws
    else:
        rows = {sum(1 << (4 * i + j) for j in range(4)) for i in range(4)}
        cols = {sum(1 << (4 * i + j) for i in range(4)) for j in range(4)}
        assert set(states[4]) == rows | cols
        type_count = Counter()
        for mask in states[5]:
            occupied_rows = {v // 4 for v in range(N) if mask & (1 << v)}
            occupied_cols = {v % 4 for v in range(N) if mask & (1 << v)}
            assert (len(occupied_rows), len(occupied_cols)) in ((4, 2), (2, 4))
            type_count["row" if len(occupied_rows) == 4 else "column"] += 1
        assert type_count == {"row": 192, "column": 192}
    for k in (4, 5, 6):
        h = exchange_graph(states[k])
        e = sum(map(len, h)) // 2
        degree = Counter(map(len, h))
        comps = component_indices(h)
        comp_sizes = sorted((len(q) for q in comps), reverse=True)
        exp = {
            "shrikhande": {
                4: (0, [1] * 32, {0: 32}),
                5: (5136, [672], {11: 192, 17: 480}),
                6: (74304, [4064], None),
            },
            "rook": {
                4: (0, [1] * 8, {0: 8}),
                5: (2112, [192, 192], {9: 288, 17: 96}),
                6: (63024, [3744], None),
            },
        }[kind][k]
        assert e == exp[0] and comp_sizes == exp[1], (kind, k, e, comp_sizes)
        if exp[2] is not None:
            assert degree == exp[2], (kind, k, degree)
        if k == 5:
            ecc = Counter(eccentricities(h))
            target = ({5: 672} if kind == "shrikhande" else {6: 96, 7: 288})
            assert ecc == target, (kind, ecc)
            print(kind.upper(), "FIVE_METRIC_OK", "eccentricity_counts", sorted(ecc.items()))
        print(kind.upper(), "EXCHANGE_OK", "size", k, "vertices", len(h),
              "edges", e, "component_sizes", comp_sizes)
    return states


if __name__ == "__main__":
    graph_checks("shrikhande")
    graph_checks("rook")
    print("ALL_VERIFY_OK")
