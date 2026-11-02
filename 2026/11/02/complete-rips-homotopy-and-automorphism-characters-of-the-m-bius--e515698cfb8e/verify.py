#!/usr/bin/env python3
"""Exact integral Morse and full-symmetry checks for graph-metric Rips complexes of GP(8,3).

Python standard library only. Every finite object is rebuilt from the stated graph.
"""
from collections import Counter, deque
from itertools import combinations

N = 16
ADJ = [set() for _ in range(N)]

def edge(a, b):
    ADJ[a].add(b)
    ADJ[b].add(a)

for j in range(8):
    edge(j, (j+1) % 8)
    edge(j, 8+j)
    edge(8+j, 8+(j+3) % 8)
assert all(len(a) == 3 for a in ADJ)
DIST = []
for s in range(N):
    ds = {s: 0}
    todo = deque([s])
    while todo:
        u = todo.popleft()
        for v in ADJ[u]:
            if v not in ds:
                ds[v] = ds[u] + 1
                todo.append(v)
    assert len(ds) == N
    DIST.append(ds)
assert max(max(ds.values()) for ds in DIST) == 4

VERTS = {m: tuple(i for i in range(N) if (m >> i) & 1)
         for m in range(1, 1 << N)}

def faces_at(scale):
    return {m for m, vs in VERTS.items()
            if all(DIST[i][j] <= scale for i, j in combinations(vs, 2))}

F = faces_at(2)
F_BY_DIM = {d: tuple(sorted(m for m in F if m.bit_count() == d+1)) for d in range(4)}
assert tuple(len(F_BY_DIM[d]) for d in range(4)) == (16, 72, 112, 48)
assert len(F) == 248

ORDER = (3, 15, 13, 4, 12, 6, 9, 1, 14, 2, 7, 10, 11, 0, 8, 5)
active = set(F)
pairs = []
for v in ORDER:
    for f in sorted(active, key=lambda m: (m.bit_count(), m)):
        if f not in active or (f >> v) & 1:
            continue
        g = f | (1 << v)
        if g in active:
            active.remove(f)
            active.remove(g)
            pairs.append((f, g))
assert len(pairs) == 118
assert Counter(m.bit_count()-1 for m in active) == {0: 1, 2: 9, 3: 2}

# Forman acyclicity: direct each matched cover upward, all others downward.
matchset = set(pairs)
indegree = {f: 0 for f in F}
arc = {f: [] for f in F}
for g in F:
    if g.bit_count() == 1:
        continue
    for i in VERTS[g]:
        f = g ^ (1 << i)
        a, b = (f, g) if (f, g) in matchset else (g, f)
        arc[a].append(b)
        indegree[b] += 1
todo = deque(k for k, v in indegree.items() if v == 0)
visited = 0
while todo:
    v = todo.popleft()
    visited += 1
    for w in arc[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            todo.append(w)
assert visited == len(F)

# Signed simplicial differential and exact integral cancellation.
BDRY = {g: {} for g in F}
for g in F:
    if g.bit_count() > 1:
        for i, v in enumerate(VERTS[g]):
            BDRY[g][g ^ (1 << v)] = (-1)**i

differentials = {f: dict(BDRY[f]) for f in F}
survive = set(F)
for f, g in pairs:
    pivot = differentials[g].get(f, 0)
    assert abs(pivot) == 1, (f, g, pivot)
    for h in tuple(survive):
        if h == g or h.bit_count() != g.bit_count():
            continue
        coef = differentials[h].get(f, 0)
        if not coef:
            continue
        for target, val in differentials[g].items():
            new_val = differentials[h].get(target, 0) - (coef // pivot)*val
            if new_val:
                differentials[h][target] = new_val
            else:
                differentials[h].pop(target, None)
    survive.remove(f)
    survive.remove(g)
    del differentials[f]
    del differentials[g]
    for h in survive:
        differentials[h].pop(f, None)
        differentials[h].pop(g, None)
assert survive == active
assert all(not bd for bd in differentials.values())

# At the next scale the only absent edges are eight antipodal pairs.
far_pairs = [(a, b) for a in range(N) for b in range(a+1, N)
             if DIST[a][b] == 4]
assert len(far_pairs) == 8
assert Counter(x for p in far_pairs for x in p) == {i: 1 for i in range(N)}
assert all(DIST[i][j] <= 3 for i in range(N) for j in range(i+1, N)
           if (i, j) not in far_pairs)
# Therefore the scale-three complex is the 8-fold join of S^0, i.e. S^7.

# Two explicit primitive integral 3-cycles (tetrahedron-mask, coefficient).
Z0 = dict(((1290,1),(1320,1),(1410,-1),(1440,1),(5130,1),
           (5160,1),(5250,-1),(5280,1),(16650,-1),(16680,-1),
           (16770,1),(16800,-1),(20490,1),(20520,1),(20610,-1),(20640,1)))
Z1 = dict(((2565,1),(2580,1),(2625,-1),(2640,1),(10245,1),
           (10260,1),(10305,-1),(10320,1),(33285,-1),(33300,-1),
           (33345,1),(33360,-1),(40965,1),(40980,1),(41025,-1),(41040,1)))
assert set(Z0).issubset(F_BY_DIM[3]) and set(Z1).issubset(F_BY_DIM[3])
for cycle in (Z0, Z1):
    b = Counter()
    for g, coeff in cycle.items():
        for f, delta in BDRY[g].items():
            b[f] += coeff*delta
    assert not any(b.values())
assert (Z0.get(1290,0), Z1.get(1290,0), Z0.get(2565,0), Z1.get(2565,0)) == (1,0,0,1)

# Enumerate all graph automorphisms by exact adjacency-preserving backtracking.
def automorphisms():
    result = []
    def rec(mapping, used):
        if len(mapping) == N:
            result.append(tuple(mapping[i] for i in range(N)))
            return
        best = None
        for v in range(N):
            if v in mapping:
                continue
            candidates = [w for w in range(N) if w not in used and all(
                ((u in ADJ[v]) == (mapping[u] in ADJ[w])) for u in mapping)]
            key = (len(candidates), -sum(u in ADJ[v] for u in mapping), v)
            if best is None or key < best[0]:
                best = (key, v, candidates)
        _, v, candidates = best
        for w in candidates:
            mapping[v] = w
            used.add(w)
            rec(mapping, used)
            used.remove(w)
            del mapping[v]
    rec({}, set())
    return result

AUT = automorphisms()
assert len(AUT) == 96
assert len(set(AUT)) == 96

def map_mask(mask, perm):
    originals = VERTS[mask]
    mapped = [perm[v] for v in originals]
    inversions = sum(mapped[i] > mapped[j]
                     for i in range(len(mapped)) for j in range(i+1, len(mapped)))
    return sum(1 << j for j in mapped), (-1)**inversions

bipartition = {i: (i % 2) for i in range(8)}
bipartition.update({8+i: 1 - (i % 2) for i in range(8)})
assert all(bipartition[a] != bipartition[b] for a in range(N) for b in ADJ[a])
far_index = {a: i for i, (a,b) in enumerate(far_pairs) for a in (a,b)}
character1, character2, character3, character7 = [], [], [], []
for perm in AUT:
    lefschetz = 0
    lefschetz_graph = 0
    for k, faces in F_BY_DIM.items():
        fixed_signed = sum(sgn for mask in faces for new, sgn in [map_mask(mask, perm)]
                           if new == mask)
        lefschetz += (-1)**k * fixed_signed
        if k <= 1:
            lefschetz_graph += (-1)**k * fixed_signed
    projected = []
    for cycle in (Z0, Z1):
        image = Counter()
        for m, coeff in cycle.items():
            new, sgn = map_mask(m, perm)
            image[new] += coeff*sgn
        c0, c1 = image[1290], image[2565]
        assert all(image[m] == c0*Z0.get(m,0) + c1*Z1.get(m,0)
                   for m in F_BY_DIM[3])
        projected.append((c0,c1))
    tr3 = projected[0][0] + projected[1][1]
    bip_sign = 1 if bipartition[perm[0]] == bipartition[0] else -1
    assert tr3 == 1 + bip_sign
    tr1 = 1 - lefschetz_graph
    character1.append(tr1)
    tr2 = lefschetz - 1 + tr3
    character2.append(tr2)
    character3.append(tr3)
    paired_perm = [far_index[perm[a]] for a,b in far_pairs]
    inv = sum(paired_perm[i] > paired_perm[j] for i in range(8) for j in range(i+1,8))
    swap_sign = 1
    for a,b in far_pairs:
        swap_sign *= 1 if perm[a] < perm[b] else -1
    chi7 = ((-1)**inv) * swap_sign
    character7.append(chi7)

assert Counter(character2) == {-3:8, -1:42, 1:39, 3:6, 9:1}
assert Counter(character3) == {0:48, 2:48}
assert Counter(character7) == {1:96}
assert sum(character1) == 0
assert sum(character2) == 0
assert sum(character3) == 96
assert sum(character7) == 96

print('MOBIUS_KANTOR_RIPS_EXACT_MORSE_96_CHARACTER_OK')
print('scale2 face vector: (16,72,112,48)')
print('Morse pairs: 118; critical cells: (1,0,9,2); signed Morse differential: zero')
print('scale3: crosspolytope boundary S^7; aut order: 96')
print('scale1 character invariant dimension:', sum(character1)//96)
print('character2 distribution:', sorted(Counter(character2).items()))
print('character3 distribution:', sorted(Counter(character3).items()))
print('character7 distribution:', sorted(Counter(character7).items()))
