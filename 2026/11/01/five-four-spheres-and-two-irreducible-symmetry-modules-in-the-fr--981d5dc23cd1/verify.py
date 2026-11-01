#!/usr/bin/env python3
"""Standalone finite proof checker for a twelve-vertex cubic graph complex.
No network access, external dependencies, or files required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 12
V = range(N)
EDGE_SET = {tuple(sorted((i, (i+1) % N))) for i in V}
EDGE_SET |= {tuple(sorted((i, (i+(5 if i % 2 == 0 else -5)) % N))) for i in V}
assert len(EDGE_SET) == 18
NB = [set() for _ in V]
for a, b in EDGE_SET:
    NB[a].add(b); NB[b].add(a)
assert all(len(NB[v]) == 3 for v in V)

def is_face_degree(mask):
    for v in V:
        if mask & (1 << v) and sum(bool(mask & (1 << w)) for w in NB[v]) > 1:
            return False
    return True

FORBIDDEN = set()
for v in V:
    for x, y in combinations(NB[v], 2):
        FORBIDDEN.add((1 << v) | (1 << x) | (1 << y))

def is_face_triples(mask):
    return all(mask & t != t for t in FORBIDDEN)

assert all(is_face_degree(mask) == is_face_triples(mask) for mask in range(1 << N))
FACES = tuple(mask for mask in range(1, 1 << N) if is_face_degree(mask))
FSET = set(FACES)
F_VECTOR = tuple(sum(m.bit_count() == j for m in FACES) for j in range(1, 7))
assert F_VECTOR == (12, 66, 184, 264, 168, 28)
assert len(FACES) == 722

# A completely specified sequential element matching; the empty face is omitted.
ORDER = (7, 11, 0, 8, 5, 6, 3, 10, 4, 1, 9, 2)
remaining = set(FACES)
matched = []
for v in ORDER:
    bit = 1 << v
    for f in sorted(remaining):
        if not (f & bit) and f | bit in remaining:
            remaining.remove(f); remaining.remove(f | bit)
            matched.append((f, f | bit))
assert len(matched) == 358
assert len(remaining) == 6
assert Counter(f.bit_count() - 1 for f in remaining) == {0: 1, 4: 5}
assert len({x for ab in matched for x in ab}) == 716
assert all(a | (b ^ a) == b and (b ^ a).bit_count() == 1 for a, b in matched)
MATCH = set(matched)

# Exhaustive directed-Hasse acyclicity certificate: unmatched cover upper -> lower,
# matched cover lower -> upper. Check every cover and all vertices by Kahn's algorithm.
OUT = defaultdict(list)
indegree = {f: 0 for f in FACES}
incidences = 0
for upper in FACES:
    for v in V:
        if upper & (1 << v):
            lower = upper ^ (1 << v)
            if lower == 0:  # ordinary, not augmented face poset
                continue
            assert lower in FSET
            if (lower, upper) in MATCH:
                src, dst = lower, upper
            else:
                src, dst = upper, lower
            OUT[src].append(dst)
            indegree[dst] += 1
            incidences += 1
queue = deque(f for f, deg in indegree.items() if deg == 0)
visited = 0
while queue:
    f = queue.popleft(); visited += 1
    for g in OUT[f]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)
assert visited == len(FACES), 'matched Hasse graph contains directed cycle'

# Enumerate all graph automorphisms by a recursive bijection with adjacency checks.
# Each partial assignment is extended over every unused compatible image.
EDGES = EDGE_SET

def enumerate_automorphisms():
    current = [-1] * N
    unused = set(V)
    result = []
    def feasible(v):
        return [w for w in unused if all(((u in NB[v]) == (current[u] in NB[w]))
                                             for u in V if current[u] >= 0)]
    def backtrack():
        if not unused:
            p = tuple(current)
            assert all(tuple(sorted((p[a], p[b]))) in EDGES for a, b in EDGES)
            result.append(p)
            return
        # MRV (a vertex with minimum remaining available images).
        candidates = [(len(feasible(v)), -sum(current[u] >= 0 for u in NB[v]), v)
                      for v in V if current[v] < 0]
        _, _, v = min(candidates)
        for w in feasible(v):
            current[v] = w
            unused.remove(w)
            backtrack()
            unused.add(w)
            current[v] = -1
    backtrack()
    return sorted(result)

AUT = enumerate_automorphisms()
assert len(AUT) == 48
assert len(set(AUT)) == 48
Z = tuple((i+6)%12 for i in V)
assert Z in AUT

def compose(a,b):
    return tuple(a[b[i]] for i in V)
assert all(compose(p, Z) == compose(Z, p) for p in AUT)
assert all(compose(p, q) in AUT for p in AUT for q in AUT)

def cycles(p):
    lengths = []; unseen = set(V)
    while unseen:
        i = min(unseen); j = i; l = 0
        while j in unseen:
            unseen.remove(j); l += 1; j = p[j]
        assert j == i
        lengths.append(l)
    return tuple(sorted(lengths))

def fixed_simplex_sign(f, p):
    vertices = [v for v in V if f & (1 << v)]
    image = [p[v] for v in vertices]
    if sum(1 << j for j in image) != f: return 0
    inversions = sum(image[i] > image[j]
                     for i in range(len(image)) for j in range(i+1, len(image)))
    return 1 if inversions % 2 == 0 else -1

def fixed_simplex_sign_cycles(f,p):
    image = {p[v] for v in V if f & (1 << v)}
    setv = {v for v in V if f & (1 << v)}
    if image != setv: return 0
    unseen = setv.copy(); num_cycles = 0
    while unseen:
        num_cycles += 1; j = min(unseen)
        while j in unseen:
            unseen.remove(j); j = p[j]
    return (-1) ** (len(setv) - num_cycles)

def character(p):
    lefschetz = 0
    for f in FACES:
        s = fixed_simplex_sign(f,p)
        assert s == fixed_simplex_sign_cycles(f,p)
        lefschetz += (-1)**(f.bit_count()-1) * s
    return lefschetz - 1

chars = {p: character(p) for p in AUT}
assert chars[tuple(V)] == 5
assert chars[Z] == 1
assert Counter(chars.values()) == {1:24, -1:20, -3:3, 5:1}
assert sum(chars.values()) == 0
assert sum(c*c for c in chars.values()) == 96

rows = Counter((cycles(p),chars[p]) for p in AUT)
EXPECTED = {
    ((1,)*12,5): 1,
    ((1,)*8+(2,)*2,-3): 3,
    ((1,)*4+(2,)*4,1): 3,
    ((2,)*6,-1): 12,
    ((2,)*6,1): 1,
    ((2,)*2+(4,)*2,1): 12,
    ((3,)*4,-1): 8,
    ((6,)*2,1): 8,
}
assert rows == EXPECTED, (rows, EXPECTED)
# Since the central involution has trace 1 on a five-dimensional module,
# the + and - eigenspaces have dimensions 3 and 2. Their character norms
# are both 1, hence each is absolutely irreducible.
pos = {g:(chars[g]+chars[compose(g,Z)])/2 for g in AUT}
neg = {g:(chars[g]-chars[compose(g,Z)])/2 for g in AUT}
assert pos[tuple(V)] == 3 and neg[tuple(V)] == 2
assert all(x == int(x) for x in pos.values())
assert all(x == int(x) for x in neg.values())
assert sum(pos[g]*pos[g] for g in AUT) == 48
assert sum(neg[g]*neg[g] for g in AUT) == 48
assert sum(pos[g]*neg[g] for g in AUT) == 0

# Independent degree-by-degree mod-2 boundary ranks. Only a corroboration;
# the integral homotopy conclusion already follows from the acyclic matching.
def rank_mod2(columns):
    pivots = {}
    for c in columns:
        while c:
            b = c.bit_length()-1
            if b in pivots: c ^= pivots[b]
            else:
                pivots[b] = c
                break
    return len(pivots)

by_size = {size:[f for f in FACES if f.bit_count()==size] for size in range(1,7)}
ranks = {}
for j in range(2,7):
    lower = {f:i for i,f in enumerate(by_size[j-1])}
    columns = []
    for upper in by_size[j]:
        c = 0
        for v in V:
            if upper & (1<<v):
                c ^= 1<<lower[upper^(1<<v)]
        columns.append(c)
    ranks[j-1] = rank_mod2(columns)
betti = {d:len(by_size[d+1])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(6)}
assert betti == {0:1,1:0,2:0,3:0,4:5,5:0}

print('GRAPH_VERTICES',N,'GRAPH_EDGES',len(EDGES),'FORBIDDEN_TRIPLES',len(FORBIDDEN))
print('F_VECTOR', F_VECTOR,'NONEMPTY_FACES',len(FACES))
print('MATCHING_ORDER',ORDER,'MATCHED_PAIRS',len(matched),'CRITICAL_DIMENSIONS',sorted(Counter(f.bit_count()-1 for f in remaining).items()))
print('HASSE_INCIDENCES',incidences,'TOPOLOGICAL_SORT_VISITS',visited)
print('AUTOMORPHISMS',len(AUT),'CENTER_HALF_ROTATION',Z,'CHARACTER_DISTRIBUTION',sorted(Counter(chars.values()).items()))
print('CHARACTER_BY_VERTEX_CYCLE_TYPE_AND_VALUE')
for (typ, value), count in sorted(rows.items()):
    print(' ',typ, value, count)
print('INVARIANTS',sum(chars.values())//48,'CHARACTER_NORM_SQUARED',sum(c*c for c in chars.values())//48)
print('CENTRAL_EIGEN_DIMENSIONS',int(pos[tuple(V)]),int(neg[tuple(V)]),'EIGEN_CHARACTER_NORMS',sum(x*x for x in pos.values())//48,sum(x*x for x in neg.values())//48)
print('MOD2_BOUNDARY_RANKS',sorted(ranks.items()),'MOD2_BETTI',sorted(betti.items()))
print('ALL_CHECKS_PASS')
