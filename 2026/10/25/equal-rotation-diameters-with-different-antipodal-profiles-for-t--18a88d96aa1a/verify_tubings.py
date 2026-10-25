#!/usr/bin/env python3
"""Exact finite verification of rotation metrics for two cubic graphs on eight vertices.

Usage: python3 verify_cube_wagner_tubings.py
Requires only Python's standard library.
"""
from functools import lru_cache
from itertools import permutations, product
from collections import Counter, deque

TARGET = {
    'cube': {
        'size': 16752, 'edges': 58632, 'automorphisms': 48,
        'orbit_sizes': {24: 12, 48: 343},
        'ecc': {17: 1368, 18: 8280, 19: 6336, 20: 768},
        'pairs': [0, 58632, 230712, 653904, 1488696, 2890800, 4967280,
                  7701408, 10887384, 14100984, 16745640, 18179424,
                  17940888, 15963096, 12638352, 8638488, 4806864,
                  1941288, 437856, 34056, 624]
    },
    'wagner': {
        'size': 17568, 'edges': 61488, 'automorphisms': 16,
        'orbit_sizes': {16: 1098},
        'ecc': {17: 976, 18: 5536, 19: 10800, 20: 256},
        'pairs': [0, 61488, 241824, 685152, 1559056, 3028464, 5207440,
                  8089664, 11479368, 14957024, 17918640, 19692096,
                  19737008, 17885520, 14472144, 10188936, 5908024,
                  2528288, 620288, 47936, 168]
    }
}


def run(kind):
    n = 8
    full = (1 << n) - 1
    adj = [0] * n
    for a in range(n):
        for b in range(a):
            if (kind == 'cube' and (a ^ b).bit_count() == 1) or (
                kind == 'wagner' and ((a - b) % 8 in (1, 4, 7))
            ):
                adj[a] |= 1 << b
                adj[b] |= 1 << a

    @lru_cache(None)
    def components(mask):
        ans = []
        rem = mask
        while rem:
            front = rem & -rem
            comp = 0
            while front:
                bit = front & -front
                front -= bit
                v = bit.bit_length() - 1
                comp |= bit
                front |= adj[v] & rem & ~comp
            rem &= ~comp
            ans.append(comp)
        return tuple(ans)

    @lru_cache(None)
    def enumerate_tubings(mask):
        if not mask:
            return ((),)
        ans = []
        for root in range(n):
            if not (mask & (1 << root)):
                continue
            parts = components(mask & ~(1 << root))
            options = [[(p,) + t for t in enumerate_tubings(p)] for p in parts]
            for children in product(*options):
                ans.append(tuple(sorted(t for child in children for t in child)))
        assert len(ans) == len(set(ans))
        return tuple(ans)

    tubings = enumerate_tubings(full)
    index = {t: i for i, t in enumerate(tubings)}
    count = len(tubings)
    goal = TARGET[kind]
    assert count == goal['size'] and len(index) == count
    assert all(len(t) == n - 1 for t in tubings)

    # A ridge is a common collection of six tubes. Each has two completions.
    ridge = {}
    flip = [set() for _ in tubings]
    for i, tubing in enumerate(tubings):
        for j in range(n - 1):
            key = tubing[:j] + tubing[j + 1:]
            if key in ridge:
                other = ridge.pop(key)
                flip[i].add(other)
                flip[other].add(i)
            else:
                ridge[key] = i
    assert not ridge
    assert all(len(a) == n - 1 for a in flip)
    assert sum(map(len, flip)) // 2 == goal['edges']

    # A completely different neighborhood construction rotates parent-child
    # edges in the corresponding rooted elimination trees.
    def parents(tubing):
        all_tubes = tubing + (full,)
        label = {}
        for t in all_tubes:
            used = 0
            for s in all_tubes:
                if s != t and (s & t) == s:
                    used |= s
            remaining = t & ~used
            assert remaining.bit_count() == 1
            label[t] = remaining.bit_length() - 1
        parent = [-2] * n
        for t in all_tubes:
            v = label[t]
            if t == full:
                parent[v] = -1
            else:
                bigger = [s for s in all_tubes if t != s and (t & s) == t]
                immediate = min(bigger, key=int.bit_count)
                parent[v] = label[immediate]
        assert -2 not in parent
        return tuple(parent)

    def to_tubing(parent):
        children = [[] for _ in range(n)]
        roots = []
        for v, p in enumerate(parent):
            if p == -1:
                roots.append(v)
            else:
                children[p].append(v)
        assert len(roots) == 1
        descendants = [0] * n
        def visit(v):
            mask = 1 << v
            for w in children[v]:
                mask |= visit(w)
            descendants[v] = mask
            return mask
        assert visit(roots[0]) == full
        return tuple(sorted(descendants[v] for v in range(n) if v != roots[0])), descendants

    for i, tubing in enumerate(tubings):
        original = parents(tubing)
        recovered, subs = to_tubing(original)
        assert recovered == tubing
        adjacent = set()
        for y, x in enumerate(original):
            if x == -1:
                continue
            nxt = list(original)
            nxt[y] = original[x]
            nxt[x] = y
            for z in range(n):
                if original[z] == y and (adj[x] & subs[z]):
                    nxt[z] = x
            after, _ = to_tubing(tuple(nxt))
            assert after in index
            adjacent.add(index[after])
        assert adjacent == flip[i], ('rotation discrepancy', kind, i)

    # Test every vertex permutation rather than presuming the automorphism group.
    original_edges = {(i, j) for i in range(n) for j in range(i + 1, n)
                      if adj[i] & (1 << j)}
    autos = []
    for perm in permutations(range(n)):
        if {(min(perm[i], perm[j]), max(perm[i], perm[j]))
            for i, j in original_edges} == original_edges:
            autos.append(perm)
    assert len(autos) == goal['automorphisms']

    seen = set()
    representatives = []
    size_profile = Counter()
    for i, t in enumerate(tubings):
        if i in seen:
            continue
        orbit = set()
        for p in autos:
            mapped = tuple(sorted(sum(1 << p[v] for v in range(n)
                                      if mask & (1 << v)) for mask in t))
            orbit.add(index[mapped])
        assert i in orbit and not (seen & orbit)
        seen.update(orbit)
        representatives.append((i, len(orbit)))
        size_profile[len(orbit)] += 1
    assert len(seen) == count
    assert dict(size_profile) == goal['orbit_sizes']

    # Shortest-path counts are accumulated once per symmetry orbit with
    # multiplicity equal to the orbit size; unordered pairs counted twice.
    ordered = Counter()
    ecc_profile = Counter()
    ecc_orbits = Counter()
    for source, weight in representatives:
        q = deque([source])
        dist = [-1] * count
        dist[source] = 0
        while q:
            u = q.popleft()
            for v in flip[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    q.append(v)
        assert min(dist) == 0
        e = max(dist)
        ecc_profile[e] += weight
        ecc_orbits[e] += 1
        for d in dist:
            ordered[d] += weight
    assert dict(ecc_profile) == goal['ecc']
    assert ecc_orbits[20] == 16
    assert ordered[0] == count
    pairs = [0] + [ordered[d] // 2 for d in range(1, 21)]
    assert all(ordered[d] % 2 == 0 for d in range(1, 21))
    assert pairs == goal['pairs']
    assert sum(pairs) == count * (count - 1) // 2
    assert min(ecc_profile) == 17 and max(ecc_profile) == 20
    print(f'{kind}: {count} tubings, {goal["edges"]} flips, '
          f'{len(representatives)} symmetry orbits, eccentricities {dict(ecc_profile)}, '
          f'distance-20 pairs {pairs[20]}')


if __name__ == '__main__':
    run('cube')
    run('wagner')
    print('VERIFY_OK')
