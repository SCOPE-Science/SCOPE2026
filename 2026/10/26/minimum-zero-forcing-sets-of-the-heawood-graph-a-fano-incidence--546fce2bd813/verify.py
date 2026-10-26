#!/usr/bin/env python3
"""Exact finite checker for zero-forcing bases of the Fano incidence graph.

Run: python3 heawood_zero_forcing_verify.py
Requires only the Python standard library.
"""
from collections import Counter, deque
from itertools import combinations, permutations

POINTS = tuple(range(1, 8))
LINES = tuple(sorted((frozenset(t) for t in combinations(POINTS, 3)
                      if t[0] ^ t[1] ^ t[2] == 0),
                     key=lambda s: tuple(sorted(s))))
assert len(LINES) == 7 and len(set(LINES)) == 7
N = [set() for _ in range(14)]
for j, line in enumerate(LINES):
    for p in line:
        N[p-1].add(7+j)
        N[7+j].add(p-1)
assert all(len(ns) == 3 for ns in N)
ALL = (1 << 14)-1
NBITS = [sum(1 << j for j in row) for row in N]


def steps_parallel(seed):
    """Simultaneously fire every uniquely available white neighbor."""
    blue = sum(1 << i for i in seed)
    steps = 0
    while True:
        after = blue
        for i in range(14):
            if blue & (1 << i):
                available = NBITS[i] & ~blue
                if available and available & (available-1) == 0:
                    after |= available
        if after == blue:
            return steps if blue == ALL else None
        blue = after
        steps += 1


def succeeds_sequential(seed):
    """Independently replay the standard one-forcing-at-a-time rule."""
    blue = set(seed)
    while True:
        found = False
        for u in sorted(blue):
            white = N[u] - blue
            if len(white) == 1:
                blue.add(next(iter(white)))
                found = True
                break
        if not found:
            return len(blue) == 14


def is_noncollinear(three_points):
    return frozenset(p+1 for p in three_points) not in LINES


def is_nonconcurrent(three_lines):
    return not any(all(p in LINES[j] for j in three_lines) for p in POINTS)


def induced_incidence_count(seed):
    sp = {i for i in seed if i < 7}
    sl = {i for i in seed if i >= 7}
    return sum(j in N[p] for p in sp for j in sl)


def linear_group():
    maps = []
    for images in permutations(POINTS, 3):
        if images[0] ^ images[1] ^ images[2] == 0:
            continue
        def transform(x):
            return ((images[0] if x & 1 else 0) ^
                    (images[1] if x & 2 else 0) ^
                    (images[2] if x & 4 else 0))
        f = {p: transform(p) for p in POINTS}
        imgs = [frozenset(f[p] for p in line) for line in LINES]
        perm = tuple([f[p]-1 for p in POINTS] +
                     [7+LINES.index(line) for line in imgs])
        maps.append(perm)
    assert len(maps) == len(set(maps)) == 168
    polarity = []
    for p in POINTS:
        pline = frozenset(q for q in POINTS if (p & q).bit_count() % 2 == 0)
        polarity.append(7+LINES.index(pline))
    for line in LINES:
        n = [p for p in POINTS if
             frozenset(q for q in POINTS if (p & q).bit_count() % 2 == 0) == line]
        assert len(n) == 1
        polarity.append(n[0]-1)
    group = tuple(maps + [tuple(polarity[i] for i in g) for g in maps])
    assert len(set(group)) == 336
    for perm in group:
        for u in range(14):
            assert {perm[v] for v in N[u]} == N[perm[u]]
    return group


def orbit_partition(states, group):
    states = set(states)
    unseen = set(states)
    orbits = []
    while unseen:
        base = min(unseen)
        orbit = {tuple(sorted(g[i] for i in base)) for g in group}
        assert orbit <= states
        unseen -= orbit
        orbits.append(orbit)
    return orbits


def main():
    # Every set of size at most five fails. Check all 3,003 six-sets.
    for k in range(6):
        for seed in combinations(range(14), k):
            assert steps_parallel(seed) is None
    bases = {seed for seed in combinations(range(14), 6)
             if steps_parallel(seed) is not None}
    assert len(bases) == 700
    assert all(succeeds_sequential(s) for s in bases)
    assert all(not succeeds_sequential(s) for s in combinations(range(14), 6)
               if s not in bases)

    # Exact geometric criterion: balanced triangle/dual-triangle pairs
    # with at least three incidences, excluding just one boundary orbit.
    triangles = [t for t in combinations(range(7), 3) if is_noncollinear(t)]
    dual_triangles = [t for t in combinations(range(7), 3) if is_nonconcurrent(t)]
    assert len(triangles) == len(dual_triangles) == 28
    predicted = set()
    rejected = set()
    for a in triangles:
        for b in dual_triangles:
            seed = tuple(sorted(a + tuple(j+7 for j in b)))
            if induced_incidence_count(seed) >= 3:
                predicted.add(seed)
            else:
                assert induced_incidence_count(seed) == 2
                rejected.add(seed)
    assert len(predicted) == 700 and len(rejected) == 84
    assert predicted == bases

    # Full 336-element Fano point-line incidence symmetry group.
    group = linear_group()
    orbits = orbit_partition(bases, group)
    assert len(orbits) == 5
    orbit_rows = sorted((len(o), induced_incidence_count(next(iter(o))),
                         steps_parallel(next(iter(o)))) for o in orbits)
    assert (28,6,2) in orbit_rows and (168,5,2) in orbit_rows
    assert orbit_rows.count((168,4,3)) == 2
    assert orbit_rows.count((168,3,3)) == 1
    assert sorted((len(o) for o in orbit_partition(rejected, group))) == [84]
    times = Counter(steps_parallel(seed) for seed in bases)
    assert times == {2: 196, 3: 504}

    # Classification of the six induced configurations, including failure.
    shape = Counter()
    for set_family, tag in ((bases, 'success'), (rejected, 'failure')):
        for s in set_family:
            dg = tuple(sorted(len(N[u].intersection(s)) for u in s))
            shape[(tag, dg)] += 1
    assert shape == {
        ('success',(2,2,2,2,2,2)): 28,       # C6
        ('success',(1,1,2,2,2,2)): 168,      # P6
        ('success',(0,1,1,2,2,2)): 168,      # P5 + K1
        ('success',(1,1,1,1,2,2)): 168,      # 2 P3
        ('success',(0,0,1,1,2,2)): 168,      # P4 + 2 K1
        ('failure',(0,0,1,1,1,1)): 84,       # 2 K2 + 2 K1
    }

    # Vertex-exchange graph on all optimal forcing sets: complete census.
    ordered = sorted(bases)
    lookup = {x:i for i,x in enumerate(ordered)}
    neighbors = [set() for _ in ordered]
    for i,s in enumerate(ordered):
        chosen = set(s)
        for removed in s:
            for added in range(14):
                if added not in chosen:
                    target = tuple(sorted((chosen-{removed})|{added}))
                    j = lookup.get(target)
                    if j is not None:
                        neighbors[i].add(j)
    assert all(i in neighbors[j] for i,vv in enumerate(neighbors) for j in vv)
    deg = Counter(len(ns) for ns in neighbors)
    assert deg == {18:196,17:168,16:168,14:168}
    assert sum(map(len, neighbors)) == 2*5712

    distances = Counter()
    for i in range(len(ordered)):
        q = deque([i]);d={i:0}
        while q:
            u=q.popleft()
            for v in neighbors[u]:
                if v not in d:
                    d[v]=d[u]+1;q.append(v)
        assert len(d) == 700
        distances.update(d.values())
    assert distances[0] == 700
    hist = {k:v//2 for k,v in distances.items() if k>0}
    assert hist == {1:5712,2:34524,3:86184,4:87192,5:28056,6:2982}
    assert sum(hist.values()) == 700*699//2
    print('VERIFY_OK: 700 six-vertex zero-forcing bases; 5 symmetry orbits;')
    print('784 triangle/dual-triangle pairs, 84 excluded; propagation 2:196, 3:504;')
    print('exchange graph connected, 700 vertices, 5712 edges, diameter 6')

if __name__ == '__main__':
    main()
