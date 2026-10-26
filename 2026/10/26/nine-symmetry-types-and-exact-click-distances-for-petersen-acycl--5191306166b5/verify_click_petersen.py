#!/usr/bin/env python3
"""Exhaustive certificate for click reconfiguration of Petersen acyclic orientations.

Runs with the Python 3 standard library. No input files are needed.
Vertices are 2-subsets of {0,1,2,3,4} ordered lexicographically;
edges join disjoint pairs. Bit k of an orientation mask reverses edge k.
"""
from collections import Counter, deque
from itertools import combinations, permutations

VERTICES = list(combinations(range(5), 2))
EDGES = [(u, v) for u in range(10) for v in range(u + 1, 10)
         if set(VERTICES[u]).isdisjoint(VERTICES[v])]
assert len(EDGES) == 15
INC = [[] for _ in range(10)]
FLIP = [0] * 10
for k, (u, v) in enumerate(EDGES):
    INC[u].append((k, 0))
    INC[v].append((k, 1))
    FLIP[u] |= 1 << k
    FLIP[v] |= 1 << k
assert all(len(x) == 3 for x in INC)


def oriented_edges(mask):
    for k, (u, v) in enumerate(EDGES):
        yield (v, u) if mask & (1 << k) else (u, v)


def acyclic_kahn(mask):
    indeg = [0] * 10
    targets = [[] for _ in range(10)]
    for u, v in oriented_edges(mask):
        indeg[v] += 1
        targets[u].append(v)
    queue = [i for i in range(10) if indeg[i] == 0]
    visited = 0
    while queue:
        u = queue.pop()
        visited += 1
        for v in targets[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    return visited == 10


def acyclic_dfs(mask):
    # Independently test for directed cycles using depth-first 3-coloring.
    out = [[] for _ in range(10)]
    for a, b in oriented_edges(mask):
        out[a].append(b)
    color = [0] * 10

    def visit(u):
        color[u] = 1
        for v in out[u]:
            if color[v] == 1 or (color[v] == 0 and not visit(v)):
                return False
        color[u] = 2
        return True

    return all(color[u] != 0 or visit(u) for u in range(10))


def sources(mask):
    return [v for v in range(10)
            if all(((mask >> k) & 1) == endpoint for k, endpoint in INC[v])]


def sinks(mask):
    return [v for v in range(10)
            if all(((mask >> k) & 1) != endpoint for k, endpoint in INC[v])]


ALL = [mask for mask in range(1 << 15) if acyclic_kahn(mask)]
assert len(ALL) == 16680
assert all(acyclic_dfs(mask) == (mask in set(ALL)) for mask in range(1 << 15))
# The independent fixed-unique-source count agrees with Tutte evaluation T(1,0).
assert sum(sources(mask) == [0] for mask in ALL) == 704
# Known chromatic polynomial of Petersen evaluated at -1 gives 16680.
t = -1
poly = t * (t - 1) * (t - 2) * (t**7 - 12*t**6 + 67*t**5
        - 230*t**4 + 529*t**3 - 814*t**2 + 775*t - 352)
assert poly == 16680

neighbors = {}
for mask in ALL:
    # A sink flip is the inverse of a source-to-sink click at the same vertex.
    neighbors[mask] = tuple(sorted({mask ^ FLIP[v] for v in sources(mask) + sinks(mask)}))
    assert len(neighbors[mask]) == len(sources(mask)) + len(sinks(mask))
    for next_mask in neighbors[mask]:
        assert acyclic_kahn(next_mask)
assert all(mask in neighbors[next_mask] for mask in ALL for next_mask in neighbors[mask])

components = []
component_id = {}
for mask in ALL:
    if mask in component_id:
        continue
    cid = len(components)
    q = [mask]
    component_id[mask] = cid
    for u in q:
        for v in neighbors[u]:
            if v not in component_id:
                component_id[v] = cid
                q.append(v)
    components.append(q)
assert len(components) == 704
assert len(component_id) == 16680
size_hist = Counter(map(len, components))
assert dict(size_hist) == {12: 120, 16: 120, 21: 120, 22: 120,
                          28: 120, 38: 60, 50: 24, 66: 20}

# An independent pairwise-distance calculation from the published median-potential
# formula for acyclic source/sink orientation flips.
def potential_distance(initial, final):
    arcs = [[] for _ in range(10)]
    for k, (u, v) in enumerate(EDGES):
        if (initial >> k) & 1:
            u, v = v, u
        step = (initial ^ final) >> k & 1
        arcs[u].append((v, -step))
        arcs[v].append((u, step))
    potential = [None] * 10
    potential[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v, delta in arcs[u]:
            proposed = potential[u] + delta
            if potential[v] is None:
                potential[v] = proposed
                q.append(v)
            else:
                assert potential[v] == proposed
    assert None not in potential
    med = sorted(potential)[5]
    return sum(abs(z - med) for z in potential)

# All-pairs BFS in every connected component: no sampling or diameter heuristic.
component_diam = {}
component_ecc = {}
pair_hist = Counter()
for cid, comp in enumerate(components):
    cc = set(comp)
    eh = Counter()
    for start in comp:
        dist = {start: 0}
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in neighbors[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        assert set(dist) == cc
        for target, shortest in dist.items():
            assert potential_distance(start, target) == shortest
        eh[max(dist.values())] += 1
        # Ordered pairs are counted here; divide once after all traversals.
        pair_hist.update(dist.values())
    component_diam[cid] = max(eh)
    component_ecc[cid] = eh
assert all(v % 2 == 0 for k, v in pair_hist.items() if k)
for k in list(pair_hist):
    if k:
        pair_hist[k] //= 2
assert dict(pair_hist) == {0: 16680, 1: 28140, 2: 50400,
                           3: 63040, 4: 60960, 5: 30500, 6: 2040}
assert sum(v for k, v in pair_hist.items() if k) == sum(
    len(c) * (len(c) - 1) // 2 for c in components)
assert Counter((len(c), component_diam[i]) for i, c in enumerate(components)) == {
    (12, 5): 120, (16, 5): 120, (21, 5): 120, (22, 5): 120,
    (28, 6): 120, (38, 6): 60, (50, 6): 24, (66, 6): 20}

EDGE_IDS = {edge: k for k, edge in enumerate(EDGES)}
V_IDS = {vertex: i for i, vertex in enumerate(VERTICES)}

def automorphism_action(mask, vertex_perm):
    answer = 0
    for k, (u, v) in enumerate(EDGES):
        a, b = vertex_perm[u], vertex_perm[v]
        if (mask >> k) & 1:
            a, b = b, a
        j = EDGE_IDS[tuple(sorted((a, b)))]
        if a > b:
            answer |= 1 << j
    return answer

aut = []
for p in permutations(range(5)):
    vp = tuple(V_IDS[tuple(sorted((p[a], p[b])))] for a, b in VERTICES)
    assert {tuple(sorted((vp[a], vp[b]))) for a, b in EDGES} == set(EDGES)
    aut.append(vp)
assert len(set(aut)) == 120

# Independent published check: Cameron counted 168 S5-orbits on individual
# acyclic Petersen orientations, distinct from orbits of click components.
unseen_orientations = set(ALL)
orientation_orbit_count = 0
while unseen_orientations:
    seed = min(unseen_orientations)
    images = {automorphism_action(seed, a) for a in aut}
    assert images <= unseen_orientations
    unseen_orientations -= images
    orientation_orbit_count += 1
assert orientation_orbit_count == 168

remaining = set(range(704))
orbits = []
component_orbit = {}
while remaining:
    cid = min(remaining)
    seed = min(components[cid])
    orbit = {component_id[automorphism_action(seed, a)] for a in aut}
    assert orbit <= remaining
    for j in orbit:
        assert len(components[j]) == len(components[cid])
        assert component_diam[j] == component_diam[cid]
        component_orbit[j] = len(orbits)
    remaining -= orbit
    orbits.append((seed, orbit, len(components[cid]), component_diam[cid],
                   tuple(sorted(component_ecc[cid].items()))))
assert len(orbits) == 9
actual = Counter((len(orbit), size, diam, ecc) for _, orbit, size, diam, ecc in orbits)
expected = Counter([
    (120, 12, 5, ((5, 12),)),
    (120, 16, 5, ((5, 16),)),
    (60, 21, 5, ((5, 21),)),
    (60, 21, 5, ((5, 21),)),
    (120, 22, 5, ((5, 22),)),
    (120, 28, 6, ((5, 24), (6, 4))),
    (60, 38, 6, ((5, 26), (6, 12))),
    (24, 50, 6, ((5, 20), (6, 30))),
    (20, 66, 6, ((5, 22), (6, 44))),
])
assert actual == expected

# Reversing every arrow interchanges the two 21-state symmetry types,
# but fixes each of the seven other symmetry types.
reverse_map = {}
for idx, (seed, orb, size, dia, ec) in enumerate(orbits):
    reverse_map[idx] = component_orbit[component_id[seed ^ ((1 << 15) - 1)]]
assert all(orbits[reverse_map[k]][2] == data[2] for k, data in enumerate(orbits))
assert sum(i != j for i, j in reverse_map.items()) == 2
assert all(orbits[i][2] == 21 for i, j in reverse_map.items() if i != j)

print('ACYCLIC_ORIENTATIONS', len(ALL))
print('CLASSES', len(components))
print('CLASS_SIZE_MULTIPLICITIES', sorted(size_hist.items()))
print('CLASS_SYMMETRY_ORBITS', len(orbits))
print('REPRESENTATIVES (mask, component_count_in_orbit, class_size, diameter, eccentricities):')
for seed, orb, size, dia, ec in sorted(orbits, key=lambda x: (x[2], x[0])):
    print(seed, len(orb), size, dia, ec)
print('UNORDERED_PAIR_DISTANCE_HISTOGRAM', sorted(pair_hist.items()))
print('REVERSAL_SWAPS_EXACTLY_TWO_21_STATE_ORBITS', True)
print('VERIFY_OK')
