"""Exhaustive verification of optimal pebbling placements on the Fano incidence graph.
No external dependencies; run: python3 verify_bfs.py
"""
from collections import Counter, deque
from itertools import combinations_with_replacement
from math import comb
import hashlib, json, time

POINTS = list(range(1, 8))
LINES = sorted({tuple(sorted((a, b, a ^ b))) for a in POINTS for b in POINTS if a != b})
assert len(LINES) == 7
ADJ = [set() for _ in range(14)]
for li, line in enumerate(LINES, 7):
    for x in line:
        ADJ[x - 1].add(li)
        ADJ[li].add(x - 1)
assert all(len(neighbors) == 3 for neighbors in ADJ)


def reach_mask(distribution):
    """Explore every pebbling state by a literal breadth-first search."""
    todo = deque([distribution])
    seen = {distribution}
    targets = 0
    while todo:
        state = todo.popleft()
        for u, count in enumerate(state):
            if count > 0:
                targets |= 1 << u
            if count < 2:
                continue
            for v in ADJ[u]:
                change = list(state)
                change[u] -= 2
                change[v] += 1
                child = tuple(change)
                if child not in seen:
                    seen.add(child)
                    todo.append(child)
    return targets


def all_distributions(k):
    for positions in combinations_with_replacement(range(14), k):
        d = [0] * 14
        for p in positions:
            d[p] += 1
        yield tuple(d)


def vertex_distance(u, v):
    todo = deque([(u, 0)])
    seen = {u}
    while todo:
        x, depth = todo.popleft()
        if x == v:
            return depth
        for y in ADJ[x]:
            if y not in seen:
                seen.add(y)
                todo.append((y, depth + 1))
    raise AssertionError("disconnected")


def belongs_to_structural_family(d):
    occupied = [(i, count) for i, count in enumerate(d) if count]
    counts = sorted((count for _, count in occupied), reverse=True)
    if counts == [4, 2]:
        u = next(v for v, c in occupied if c == 4)
        w = next(v for v, c in occupied if c == 2)
        return vertex_distance(u, w) in (1, 3)
    if counts == [3, 3]:
        return vertex_distance(occupied[0][0], occupied[1][0]) == 1
    if counts == [4, 1, 1]:
        heavy = next(v for v, c in occupied if c == 4)
        ones = [v for v, c in occupied if c == 1]
        # For points, a three-point projective line; for line-vertices, a triple of concurrent lines.
        if all(x < 7 for x in (heavy, *ones)):
            return tuple(sorted(x + 1 for x in (heavy, *ones))) in LINES
        if all(x >= 7 for x in (heavy, *ones)):
            return len(set(LINES[heavy - 7]) & set(LINES[ones[0] - 7]) & set(LINES[ones[1] - 7])) == 1
    return False


def main():
    t0 = time.monotonic()
    counts = {}
    opt = []
    for k in range(7):
        solutions = [d for d in all_distributions(k) if reach_mask(d) == (1 << 14) - 1]
        counts[str(k)] = {'candidates': comb(13 + k, k), 'solvable': len(solutions)}
        if k == 6:
            opt = solutions
    assert len(opt) == 161
    assert all(belongs_to_structural_family(d) for d in opt)
    # Conversely, every configuration described geometrically occurs.
    family = {d for d in all_distributions(6) if belongs_to_structural_family(d)}
    assert family == set(opt)
    assert len(family) == 161
    assert Counter(tuple(sorted((x for x in d if x), reverse=True)) for d in opt) == {
        (4, 2): 98, (3, 3): 21, (4, 1, 1): 42
    }
    index = {d: i for i, d in enumerate(opt)}
    edges = set()
    arbitrary_edges = set()
    for i, d in enumerate(opt):
        for u, x in enumerate(d):
            if not x:
                continue
            for v in range(14):
                if u == v:
                    continue
                b = list(d)
                b[u] -= 1
                b[v] += 1
                j = index.get(tuple(b))
                if j is not None and i < j:
                    arbitrary_edges.add((i, j))
                    if v in ADJ[u]:
                        edges.add((i, j))
    assert edges == arbitrary_edges
    assert len(edges) == 42
    N = [set() for _ in opt]
    for i, j in edges:
        N[i].add(j)
        N[j].add(i)
    assert Counter(map(len, N)) == {0: 98, 1: 42, 2: 21}
    unseen = set(range(len(opt)))
    components = []
    while unseen:
        v = min(unseen)
        unseen.remove(v)
        todo = [v]
        component = {v}
        for u in todo:
            for w in N[u]:
                if w in unseen:
                    unseen.remove(w)
                    component.add(w)
                    todo.append(w)
        components.append(component)
    assert Counter(map(len, components)) == {1: 98, 3: 21}
    for c in components:
        if len(c) == 3:
            assert sorted(len(N[x]) for x in c) == [1, 1, 2]
    print(json.dumps({'graph': 'Fano incidence graph via binary XOR',
                      'distribution_summary': counts,
                      'types': {'4+2': 98, '3+3': 21, '4+1+1': 42},
                      'reconfiguration': {'edges': 42, 'isolated': 98, 'three_vertex_paths': 21,
                                          'same_when_nonlocal_moves_allowed': True},
                      'certificate_method': 'literal BFS for each initial placement'}, sort_keys=True))

if __name__ == '__main__':
    main()
