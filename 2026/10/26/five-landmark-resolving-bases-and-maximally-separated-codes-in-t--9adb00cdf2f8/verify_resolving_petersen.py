#!/usr/bin/env python3
"""Exact 2-token Petersen graph resolving-basis census; Python standard library."""
from collections import Counter, deque
from itertools import combinations, permutations
from math import comb


def main():
    base = list(combinations(range(5), 2))
    base_index = {v: i for i, v in enumerate(base)}
    base_edges = [(i, j) for i, j in combinations(range(10), 2)
                  if not set(base[i]).intersection(base[j])]
    assert len(base_edges) == 15
    states = list(combinations(range(10), 2))
    state_index = {s: i for i, s in enumerate(states)}
    adjacency = [set() for _ in states]
    for a, b in base_edges:
        for other in range(10):
            if other not in (a, b):
                p = state_index[tuple(sorted((a, other)))]
                q = state_index[tuple(sorted((b, other)))]
                adjacency[p].add(q)
                adjacency[q].add(p)
    assert len(states) == 45 and sum(map(len, adjacency)) == 240
    assert all(u in adjacency[v] for u in range(45) for v in adjacency[u])
    dist = []
    for root in range(45):
        d = [-1] * 45
        d[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    queue.append(v)
        assert -1 not in d
        dist.append(d)
    assert max(map(max, dist)) == 4
    assert all(dist[u][v] == dist[v][u] for u in range(45) for v in range(45))
    pairs = list(combinations(range(45), 2))
    full = (1 << len(pairs)) - 1
    distinguish = []
    for landmark in range(45):
        bits = 0
        for p, (u, v) in enumerate(pairs):
            if dist[landmark][u] != dist[landmark][v]:
                bits |= 1 << p
        distinguish.append(bits)

    # All four-subsets and five-subsets, not just representatives or samples.
    assert not any((distinguish[a] | distinguish[b] | distinguish[c] |
                    distinguish[d]) == full for a, b, c, d in combinations(range(45), 4))
    bases = set()
    for S in combinations(range(45), 5):
        bits = 0
        for i in S:
            bits |= distinguish[i]
        if bits == full:
            bases.add(S)
    assert len(bases) == 189540
    assert (6, 13, 22, 25, 34) in bases

    # The 120 induced permutations of the ten vertices and of the 45 states.
    actions = []
    for perm in permutations(range(5)):
        action_base = [base_index[tuple(sorted((perm[a], perm[b])))] for a, b in base]
        action = [state_index[tuple(sorted((action_base[a], action_base[b])))]
                  for a, b in states]
        assert all(set(action[j] for j in adjacency[i]) == adjacency[action[i]]
                   for i in range(45))
        actions.append(action)
    assert len({tuple(a) for a in actions}) == 120
    remaining = bases.copy()
    orbit_hist = Counter()
    while remaining:
        S = min(remaining)
        orbit = {tuple(sorted(action[i] for i in S)) for action in actions}
        assert orbit <= remaining
        orbit_hist[len(orbit)] += 1
        remaining.difference_update(orbit)
    assert orbit_hist == {120: 1534, 60: 90, 30: 1, 24: 1, 6: 1}
    assert sum(k * v for k, v in orbit_hist.items()) == len(bases)
    assert sum(orbit_hist.values()) == 1627

    # All pairwise 3-separated code sets; clique enumeration is complete.
    distant = [{j for j in range(45) if dist[i][j] >= 3} for i in range(45)]
    clique_hist = Counter()
    packings = []
    def extend(prefix, candidates):
        if prefix:
            clique_hist[len(prefix)] += 1
        if len(prefix) == 5:
            packings.append(tuple(prefix))
        for index, a in enumerate(candidates):
            extend(prefix + [a], [b for b in candidates[index+1:] if b in distant[a]])
    extend([], list(range(45)))
    assert clique_hist == {1: 45, 2: 480, 3: 1220, 4: 570, 5: 30}
    assert len(packings) == 30
    assert all(S in bases for S in packings)
    assert all(dist[i][j] == 3 for S in packings for i, j in combinations(S, 2))
    orbit_hist_packing = Counter()
    pending = set(packings)
    while pending:
        S = min(pending)
        orbit = {tuple(sorted(action[i] for i in S)) for action in actions}
        assert orbit <= pending
        orbit_hist_packing[len(orbit)] += 1
        pending.difference_update(orbit)
    assert orbit_hist_packing == {6: 1, 24: 1}
    # Independently validate the distance-vector definition for each packed basis.
    for S in packings:
        signatures = {tuple(dist[s][v] for s in S) for v in range(45)}
        assert len(signatures) == 45
    print('VERIFY_OK; 45 states; 120 moves; metric dimension 5; '
          '189540 bases; 1627 S5-orbits; 30 optimal distance-separated bases')


if __name__ == '__main__':
    main()
