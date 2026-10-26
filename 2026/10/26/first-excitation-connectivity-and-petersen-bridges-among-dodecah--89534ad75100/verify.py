#!/usr/bin/env python3
"""Finite verification of balanced-cut exchange geometry of GP(10,2).

Requires Python >=3.9, standard library only. Run: python3 verify.py
Every partition is represented exactly once by its side containing vertex 0.
"""
from collections import Counter, deque
from itertools import combinations

N = 20
FULL = (1 << N) - 1

def edges():
    e = set()
    for i in range(10):
        for a, b in ((i, (i + 1) % 10), (i, 10 + i),
                     (10 + i, 10 + (i + 2) % 10)):
            e.add(tuple(sorted((a, b))))
    return sorted(e)

E = edges()
assert len(E) == 30
NB = [0] * N
for a, b in E:
    NB[a] |= 1 << b
    NB[b] |= 1 << a
assert all(x.bit_count() == 3 for x in NB)

def canonical(x):
    return x if x & 1 else x ^ FULL

def direct_boundary(x):
    return sum(bool(x & (1 << a)) != bool(x & (1 << b)) for a, b in E)

def internal_boundary(x):
    # Every included vertex contributes degree three; internal edges are double counted.
    return 3 * x.bit_count() - sum((NB[i] & x).bit_count()
                                  for i in range(N) if x & (1 << i))

def all_bisections():
    for tail in combinations(range(1, N), 9):
        yield 1 | sum(1 << x for x in tail)

def swaps(x):
    selected = [i for i in range(N) if (x >> i) & 1]
    missing = [i for i in range(N) if not ((x >> i) & 1)]
    for i in selected:
        for j in missing:
            yield canonical(x ^ (1 << i) ^ (1 << j))

def distances_from(root, adj):
    dist = {root: 0}
    todo = deque([root])
    while todo:
        v = todo.popleft()
        for w in adj[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                todo.append(w)
    return dist

# First exhaustive enumeration: precisely binomial(19,9) complement classes.
hist = Counter()
sub = {}
for x in all_bisections():
    b = direct_boundary(x)
    hist[b] += 1
    if b <= 8:
        sub[x] = b
assert sum(hist.values()) == 92378
assert dict(sorted(hist.items())) == {
    6: 10, 8: 330, 10: 2232, 12: 10560, 14: 22680,
    16: 27330, 18: 18760, 20: 8166, 22: 2190, 24: 120
}

# Independent enumeration: every one of 2^20 bit patterns, restricted to weight 10;
# derive the boundary from induced degrees rather than testing crossing edges.
hist2 = Counter()
for x in range(1 << N):
    if x.bit_count() == 10:
        hist2[internal_boundary(x)] += 1
assert hist2 == Counter({key: 2 * val for key, val in hist.items()})

# All candidate hemispheres from graph-distance-two balls.
verts = list(range(N))
metric = {}
for u in verts:
    ds = {u: 0}
    todo = deque([u])
    while todo:
        z = todo.popleft()
        for y in verts:
            if ((NB[z] >> y) & 1) and y not in ds:
                ds[y] = ds[z] + 1
                todo.append(y)
    assert len(ds) == N
    metric[u] = ds
assert all(Counter(metric[u].values()) == Counter({0: 1, 1: 3, 2: 6, 3: 6, 4: 3, 5: 1})
           for u in verts)
hemispheres = {canonical(sum(1 << y for y in verts if metric[u][y] <= 2))
               for u in verts}
minima = sorted(x for x, b in sub.items() if b == 6)
assert len(minima) == 10 and hemispheres == set(minima)
assert all(direct_boundary(x) == 6 for x in hemispheres)
center_pair = {
    x: [u for u in verts if canonical(sum(
        1 << y for y in verts if metric[u][y] <= 2)) == x]
    for x in minima
}
assert all(len(centers) == 2 and metric[centers[0]][centers[1]] == 5
           for centers in center_pair.values())

# First transition graph construction: single exchange of one vertex from each side.
adj = {x: {y for y in swaps(x) if y in sub} for x in sub}
assert all(x not in nbrs for x, nbrs in adj.items())
assert all(x in adj[y] for x, nbrs in adj.items() for y in nbrs)
assert all(len(nbrs) == len(set(nbrs)) for nbrs in adj.values())

# Second transition graph construction: direct pairwise symmetric-difference test,
# with complement identification. This is independent of swaps() enumeration.
ordered = sorted(sub)
for i, x in enumerate(ordered):
    for y in ordered[i + 1:]:
        d = (x ^ y).bit_count()
        assert (y in adj[x]) == (d == 2 or d == 18)
assert len(sub) == 340
assert sum(map(len, adj.values())) // 2 == 2520
assert Counter(len(adj[x]) for x in adj) == Counter({11: 60, 12: 30, 14: 120,
                                                     16: 60, 18: 60, 30: 10})
assert Counter(tuple(sorted((sub[x], sub[y])))
               for x in adj for y in adj[x] if x < y) == Counter({(8, 8): 2220, (6, 8): 300})
assert all(not (set(adj[x]) & set(minima)) for x in minima)

# All shortest paths, not a single-source estimate.
all_dist = {x: distances_from(x, adj) for x in adj}
assert all(len(d) == 340 for d in all_dist.values())
ecc = Counter(max(d.values()) for d in all_dist.values())
assert ecc == Counter({5: 280, 6: 60})
assert min(ecc) == 5 and max(ecc) == 6
assert Counter(all_dist[a][b] for i, a in enumerate(minima)
               for b in minima[i + 1:]) == Counter({2: 15, 4: 30})

# Exact two-step minimum-to-minimum graph. Each edge has four distinct
# cut-eight intermediates; nonedges have none.
bridges = {}
for i, a in enumerate(minima):
    for j in range(i + 1, len(minima)):
        b = minima[j]
        mids = adj[a] & adj[b]
        bridges[i, j] = len(mids)
assert Counter(bridges.values()) == Counter({4: 15, 0: 30})

# Explicit isomorphism to the disjointness graph on 2-subsets of a 5-set.
labels = [(0, 1), (2, 3), (0, 4), (1, 2), (2, 4),
          (0, 3), (1, 4), (1, 3), (0, 2), (3, 4)]
assert len(set(labels)) == 10
for (i, j), p in bridges.items():
    disjoint = not (set(labels[i]) & set(labels[j]))
    assert (p == 4) == disjoint

# Every minimum is frozen at cut 6; cut 8 is the first feasible energy excursion
# and its 340-state graph is connected.
print('VERIFY_OK')
print('bisections=92378; exact_cut_histogram=' + str(dict(sorted(hist.items()))))
print('optimum_cut=6; minima=10; radius_two_hemispheres=10')
print('cut_le_8_states=340; level_eight=330; edges=2520; radius=5; diameter=6')
print('two_swap_optimum_graph=Petersen; edges=15; distinct_middle_states_per_edge=4')
print('minimum_to_minimum_distances={2:15,4:30}; minimum_required_cut_slack=2')
