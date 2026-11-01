#!/usr/bin/env python3
"""Exact finite verification of the Pappus graph independence homology character.

Uses only the Python 3 standard library. All graph, simplex, symmetry, and
Lefschetz computations are reconstructed from the defining LCF presentation.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations

N = 18
OFFSETS = (5, 7, -7, 7, -7, -5)
VERTICES = tuple(range(N))
EDGES = set()
for i in VERTICES:
    for j in ((i + 1) % N, (i + OFFSETS[i % 6]) % N):
        EDGES.add(tuple(sorted((i, j))))
EDGES = tuple(sorted(EDGES))
assert len(EDGES) == 27
ADJ = [0] * N
for i, j in EDGES:
    ADJ[i] |= 1 << j
    ADJ[j] |= 1 << i
assert set(x.bit_count() for x in ADJ) == {3}

# Exhaustive enumeration with canonical increasing vertex choices.
FACES = []
def enumerate_faces(mask, remaining):
    if mask:
        FACES.append(mask)
    while remaining:
        b = remaining & -remaining
        remaining -= b
        enumerate_faces(mask | b, remaining & ~ADJ[b.bit_length() - 1])
enumerate_faces(0, (1 << N) - 1)
FACES = tuple(sorted(FACES))
FCOUNT = Counter(s.bit_count() - 1 for s in FACES)
assert tuple(FCOUNT[i] for i in range(9)) == (18,126,438,801,756,348,90,18,2)
assert len(FACES) == 2597

# Construct an acyclic Forman matching on the entire nonempty face poset.
ORDER = (4,7,16,15,12,2,14,13,6,10,5,8,11,1,17,9,3,0)
remaining = set(FACES)
matching = {}
for v in ORDER:
    bit = 1 << v
    pairs = [(s, s | bit) for s in sorted(remaining) if not (s & bit) and (s | bit) in remaining]
    for s, t in pairs:
        assert s in remaining and t in remaining
        remaining.remove(s)
        remaining.remove(t)
        matching[(s, t)] = True
assert len(matching) == 1293
assert Counter(s.bit_count() - 1 for s in remaining) == {0:1, 4:10}

# Orient all proper Hasse covers downward, except reverse matched covers.
indegree = dict.fromkeys(FACES, 0)
outgoing = defaultdict(list)
hasse = 0
for t in FACES:
    if t.bit_count() == 1:
        continue
    bits = t
    while bits:
        b = bits & -bits
        bits -= b
        s = t ^ b
        if (s, t) in matching:
            tail, head = s, t
        else:
            tail, head = t, s
        outgoing[tail].append(head)
        indegree[head] += 1
        hasse += 1
assert hasse == 11430
q = deque(sorted(s for s in FACES if not indegree[s]))
visited = 0
while q:
    s = q.popleft()
    visited += 1
    for t in outgoing[s]:
        indegree[t] -= 1
        if not indegree[t]:
            q.append(t)
assert visited == len(FACES), 'Matching not acyclic'

# All-pairs distances, giving a particularly fast exhaustive automorphism test.
DIST = [[N] * N for _ in range(N)]
for i in VERTICES:
    DIST[i][i] = 0
    q = deque([i])
    while q:
        u = q.popleft()
        for v in VERTICES:
            if (ADJ[u] >> v) & 1 and DIST[i][v] == N:
                DIST[i][v] = DIST[i][u] + 1
                q.append(v)
assert max(map(max, DIST)) == 4

def all_automorphisms():
    mapping = [-1] * N
    used = [False] * N
    def rec(left):
        if not left:
            yield tuple(mapping)
            return
        # Distances to already assigned vertices specify exact constraints.
        best_v, best_targets = None, None
        for v in left:
            possible = []
            for w in VERTICES:
                if used[w]:
                    continue
                if all(mapping[u] < 0 or DIST[v][u] == DIST[w][mapping[u]] for u in VERTICES):
                    possible.append(w)
            if best_targets is None or len(possible) < len(best_targets):
                best_v, best_targets = v, possible
                if not possible:
                    break
        for w in best_targets:
            mapping[best_v] = w
            used[w] = True
            yield from rec(left - {best_v})
            used[w] = False
            mapping[best_v] = -1
    yield from rec(set(VERTICES))

AUTOS = tuple(sorted(all_automorphisms()))
assert len(AUTOS) == 216 and len(set(AUTOS)) == 216
assert all({tuple(sorted((g[u],g[v]))) for u,v in EDGES} == set(EDGES) for g in AUTOS)

# Two independent implementations of the reduced simplicial Lefschetz trace.
def direct_signed_trace(g):
    total = -1  # the augmentation chain in degree -1
    for mask in FACES:
        old = [i for i in VERTICES if mask >> i & 1]
        new = [g[i] for i in old]
        if sum(1 << j for j in new) != mask:
            continue
        inversions = sum(new[i] > new[j] for i in range(len(new)) for j in range(i+1,len(new)))
        total += (-1) ** (len(new) - 1 + inversions)
    return total

def orbit_independence_trace(g):
    orbits = []
    unseen = set(VERTICES)
    while unseen:
        start = min(unseen)
        u = start
        orbit = []
        while u in unseen:
            unseen.remove(u)
            orbit.append(u)
            u = g[u]
        assert u == start
        orbits.append(sum(1 << x for x in orbit))
    allowed = []
    for mask in orbits:
        if all((ADJ[v] & mask) == 0 for v in VERTICES if mask >> v & 1):
            allowed.append(mask)
    # Independence polynomial at -1 of the orbit conflict graph.
    evaluations = [0]
    def rec(k, selected, parity):
        if k == len(allowed):
            evaluations[0] += parity
            return
        rec(k + 1, selected, parity)
        block = allowed[k]
        if all((ADJ[v] & selected) == 0 for v in VERTICES if block >> v & 1):
            rec(k+1, selected|block, -parity)
    rec(0,0,1)
    return -evaluations[0]

CHAR = {}
for g in AUTOS:
    a = direct_signed_trace(g)
    b = orbit_independence_trace(g)
    assert a == b, (g,a,b)
    CHAR[g] = a

# Cycle partitions; the order-three fixed-point-free elements require centralizers.
def cycle_type(g):
    seen = set()
    lengths = []
    for v in VERTICES:
        if v not in seen:
            u = v
            size = 0
            while u not in seen:
                seen.add(u)
                size += 1
                u = g[u]
            lengths.append(size)
    return tuple(sorted(lengths,reverse=True))

def commute(g,h):
    return all(g[h[i]] == h[g[i]] for i in VERTICES)

TABLE = defaultdict(Counter)
for g in AUTOS:
    cycle = cycle_type(g)
    cent = sum(commute(g,h) for h in AUTOS) if cycle == (3,)*6 else 0
    TABLE[(cycle,cent)][CHAR[g]] += 1
assert len(TABLE) == 12
assert sum(sum(c.values()) for c in TABLE.values()) == 216
assert sum(CHAR.values()) == 0
# Exhaust every conjugacy class, not merely vertex-permutation cycle types.
def compose(g, h):
    return tuple(g[h[i]] for i in VERTICES)
def invert(g):
    result = [None] * N
    for i, j in enumerate(g):
        result[j] = i
    return tuple(result)
unseen = set(AUTOS)
CONJUGACY = []
while unseen:
    g = min(unseen)
    orbit = {compose(compose(h,g),invert(h)) for h in AUTOS}
    assert orbit <= unseen
    assert len({CHAR[x] for x in orbit}) == 1
    CONJUGACY.append(orbit)
    unseen -= orbit
assert len(CONJUGACY) == 13
assert sum(c*c for c in CHAR.values()) == 2*len(AUTOS) # character squared norm exactly two
# The two fixed-point-free order-three types have identical vertex and edge
# cycle partitions yet different homology traces.
def edge_cycle_type(g):
    positions = {e:i for i,e in enumerate(EDGES)}
    h = [positions[tuple(sorted((g[u],g[v])))] for u,v in EDGES]
    seen = set()
    sizes = []
    for i in range(len(EDGES)):
        if i not in seen:
            j = i
            count = 0
            while j not in seen:
                seen.add(j)
                count += 1
                j = h[j]
            sizes.append(count)
    return tuple(sorted(sizes,reverse=True))
for g in AUTOS:
    if cycle_type(g) == (3,)*6:
        assert edge_cycle_type(g) == (3,)*9
r = tuple((i+6)%N for i in VERTICES)
assert r in CHAR and CHAR[r] == -2
assert CHAR[tuple((i+12)%N for i in VERTICES)] == -2

# The graph's unique bipartition (up to exchange) defines the index-two group.
color = [-1] * N
color[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for w in VERTICES:
        if (ADJ[v] >> w) & 1:
            if color[w] == -1:
                color[w] = 1 - color[v]
                q.append(w)
            assert color[w] != color[v]
G_PLUS = [g for g in AUTOS if all(color[g[i]] == color[i] for i in VERTICES)]
assert len(G_PLUS) == 108
assert sum(CHAR[g] for g in G_PLUS) == 0

print('graph: vertices=18 edges=27 diameter=4 automorphisms=216')
print('independence f-vector:', tuple(FCOUNT[i] for i in range(9)))
print('Morse: pairs=1293 critical=', sorted(Counter(s.bit_count()-1 for s in remaining).items()), 'Hasse=11430 acyclic=True')
print('topology: integral wedge of ten 4-spheres')
print(f'conjugacy classes: {len(CONJUGACY)}, all exhaustively partition 216 automorphisms')
print('full character classes:')
for (cyc,cent), hist in sorted(TABLE.items()):
    print('  cycle=',cyc,' centralizer=',cent or 'not needed',' histogram=',dict(sorted(hist.items())))
print('rational invariants: full=0 index-two-bipartition-preserving=0; character norm squared=2')
print('all 216 signed traces equal orbit-independent-set traces: True')
