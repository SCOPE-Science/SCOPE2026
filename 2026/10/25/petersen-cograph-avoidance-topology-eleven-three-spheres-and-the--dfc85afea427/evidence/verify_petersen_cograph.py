#!/usr/bin/env python3
"""Exact, standard-library verification of Petersen induced-cograph topology and S5 character.

Usage: python3 verify_petersen_cograph.py
No network access, stochastic steps, or third-party dependencies.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from math import factorial, prod

VERTICES = list(combinations(range(5), 2))
N = len(VERTICES)
EDGES = {(i, j) for i in range(N) for j in range(i+1, N)
         if set(VERTICES[i]).isdisjoint(VERTICES[j])}

# List all induced four-vertex paths. Triangle/4-cycle freeness of this graph
# makes these precisely the noninduced four-vertex paths as well.
BAD = set()
for quad in combinations(range(N), 4):
    edges = [(i, j) for i, j in EDGES if i in quad and j in quad]
    deg = sorted(sum(i == a or i == b for a, b in edges) for i in quad)
    if len(edges) == 3 and deg == [1, 1, 2, 2]:
        BAD.add(sum(1 << j for j in quad))
assert len(EDGES) == 15 and len(BAD) == 60

# Independent verification: directly search the paths in each induced subgraph.
def path_present(mask):
    seen = [i for i in range(N) if mask >> i & 1]
    adj = {i: [j for j in seen if (min(i,j), max(i,j)) in EDGES] for i in seen}
    return any(v3 != v1 and v3 != v0 and v2 != v0
               for v0 in seen for v1 in adj[v0] for v2 in adj[v1]
               for v3 in adj[v2])

ALL = {mask for mask in range(1 << N)
       if all(mask & b != b for b in BAD)}
assert len(ALL) == 391
assert all(((mask in ALL) == (not path_present(mask))) for mask in range(1 << N))
FACES = ALL - {0}
D = {mask: mask.bit_count() - 1 for mask in FACES}
F_VECTOR = Counter(D.values())
assert [F_VECTOR[k] for k in range(6)] == [10, 45, 120, 150, 60, 5]
FACETS = [mask for mask in FACES
          if not any((mask | (1 << v)) in ALL
                     for v in range(N) if not (mask >> v & 1))]
assert Counter(D[m] for m in FACETS) == {3:10, 4:30, 5:5}

# Deterministic element matching: process each vertex and match every currently
# unmatched face not containing it to the face obtained by adding the vertex.
remaining = set(FACES)
PAIRS = []
for pivot in range(N):
    stage = [(a, a | (1 << pivot)) for a in sorted(remaining)
             if not (a >> pivot & 1) and (a | (1 << pivot)) in remaining]
    for lower, upper in stage:
        remaining.remove(lower)
        remaining.remove(upper)
    PAIRS.extend(stage)
assert len(PAIRS) == 187
assert Counter(D[m] for m in remaining) == {0: 1, 3: 13, 4: 2}
assert remaining.intersection(a for pair in PAIRS for a in pair) == set()

# Full oriented Hasse graph: downward covers, reversed matched pairs.
MATCHED = set(PAIRS)
indegree = {mask: 0 for mask in FACES}
succ = {mask: [] for mask in FACES}
incidences = 0
for upper in FACES:
    for v in range(N):
        if not (upper >> v & 1):
            continue
        lower = upper ^ (1 << v)
        if lower == 0:
            continue
        incidences += 1
        src, dst = (lower, upper) if (lower, upper) in MATCHED else (upper, lower)
        succ[src].append(dst)
        indegree[dst] += 1
q = deque(x for x in FACES if indegree[x] == 0)
visited = 0
while q:
    a = q.popleft()
    visited += 1
    for b in succ[a]:
        indegree[b] -= 1
        if indegree[b] == 0:
            q.append(b)
assert visited == len(FACES), ('cyclic matching', visited, len(FACES))
assert incidences == sum(mask.bit_count() for mask in FACES if mask.bit_count() > 1)

# Exact chain-level algebraic cancellation of each matched pair. Each
# coefficient is an integer, and every pivot is required to be a unit.
# Ordinary simplicial orientation is ascending vertex order.
columns = {}
for sigma in FACES:
    col = {}
    idx = [v for v in range(N) if sigma >> v & 1]
    if len(idx) > 1:
        for i, v in enumerate(idx):
            col[sigma ^ (1 << v)] = (-1)**i
    columns[sigma] = col
alive = set(FACES)
for a, b in PAIRS:
    assert a in alive and b in alive
    pivot = columns[b].get(a, 0)
    assert abs(pivot) == 1, ('non-unit cancellation', a, b, pivot)
    for other in list(alive):
        if other == b or D[other] != D[b]:
            continue
        coeff = columns[other].get(a, 0)
        if not coeff:
            continue
        for row, val in columns[b].items():
            new = columns[other].get(row, 0) - coeff * val * pivot
            if new:
                columns[other][row] = new
            else:
                columns[other].pop(row, None)
    for other in alive:
        if other != b:
            columns[other].pop(a, None)
    alive.remove(a)
    alive.remove(b)
assert alive == remaining
UP = sorted(m for m in alive if D[m] == 4)
DOWN = sorted(m for m in alive if D[m] == 3)
assert len(UP) == 2 and len(DOWN) == 13
B = [[columns[upper].get(lower, 0) for upper in UP] for lower in DOWN]
assert B == [[0,0],[0,1],[0,0],[1,0],[-1,0],[0,-1],
             [1,1],[0,0],[1,1],[0,1],[-1,-1],[1,0],[0,0]], B
assert B[1][0]*B[3][1] - B[1][1]*B[3][0] == -1
assert all(not columns[m] for m in alive if D[m] in (0,3))

# The Morse 3-skeleton is a wedge of thirteen 3-spheres, and the 2x2
# unimodular minor cancels two 3/4-cell pairs up to homotopy. Hence 11 S^3.

# Orientation-sensitive simplicial Lefschetz trace. Every permutation of five
# labels induces an automorphism of the Petersen graph (on two-subsets).
def cycle_type(p):
    used=set(); lengths=[]
    for i in range(5):
        if i in used:continue
        j=i;count=0
        while j not in used:
            used.add(j);count+=1;j=p[j]
        lengths.append(count)
    return tuple(sorted(lengths, reverse=True))

def sign_of_reordering(a):
    return (-1) ** sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1,len(a)))

TRACES = defaultdict(set)
COUNTS = Counter()
for p in permutations(range(5)):
    c = cycle_type(p)
    COUNTS[c] += 1
    image = [VERTICES.index(tuple(sorted(p[i] for i in pair))) for pair in VERTICES]
    trace = 0
    for face in FACES:
        a = [i for i in range(N) if face >> i & 1]
        mapped = [image[i] for i in a]
        if sorted(mapped) != a:
            continue
        trace += (-1) ** (len(a)-1) * sign_of_reordering(mapped)
    TRACES[c].add(1-trace)
assert sum(COUNTS.values()) == 120 and all(len(ts)==1 for ts in TRACES.values())
characters = {c: next(iter(tr)) for c,tr in TRACES.items()}
assert characters == {
    (1,1,1,1,1):11,
    (2,1,1,1):-3,
    (2,2,1):-1,
    (3,1,1):2,
    (3,2):0,
    (4,1):-1,
    (5,):1,
}

# Irreducible character decomposition via Murnaghan--Nakayama.
def partitions(n, lim=None):
    if lim is None:lim = n
    if n == 0:
        yield ()
    else:
        for first in range(min(n,lim), 0, -1):
            for tail in partitions(n-first, first):yield (first,)+tail

def diagram(lam):
    return {(row,col) for row,length in enumerate(lam) for col in range(length)}
from functools import lru_cache
@lru_cache(None)
def chi(lam, typ):
    if not typ:return int(not lam)
    r=typ[0]; n=sum(lam)
    out=0
    for small in partitions(n-r):
        if len(small)>len(lam) or any(x>y for x,y in zip(small,lam)):
            continue
        strip=diagram(lam)-diagram(small)
        if len(strip)!=r:continue
        if any((i+1,j) in strip and (i,j+1) in strip and (i+1,j+1) in strip
               for i,j in strip):continue
        connected={next(iter(strip))}
        queue=list(connected)
        for i,j in queue:
            for z in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if z in strip and z not in connected:
                    connected.add(z);queue.append(z)
        if len(connected)!=len(strip):continue
        out+=(-1)**(len({i for i,j in strip})-1)*chi(small,typ[1:])
    return out

MULTS = {}
for lam in partitions(5):
    numerator=sum(COUNTS[c]*characters[c]*chi(lam,c) for c in characters)
    assert numerator % 120 == 0
    mult=numerator//120
    assert mult>=0
    if mult:MULTS[lam]=mult
assert MULTS == {(3,1,1):1,(2,1,1,1):1,(1,1,1,1,1):1}
assert sum(chi(lam,(1,1,1,1,1))*m for lam,m in MULTS.items()) == 11

# Independent simplicial boundary ranks over multiple characteristics (without
# using the discrete-Morse matching). Torsion is already excluded by the integral
# unit boundary minor above; these checks guard against enumeration mistakes.
def modular_rank(vectors, modulus):
    pivots = {}
    for vec in vectors:
        vec = {r: x % modulus for r, x in vec.items() if x % modulus}
        while vec:
            r = min(vec)
            if r not in pivots:
                inv = pow(vec[r], -1, modulus)
                pivots[r] = {i: (z*inv) % modulus for i, z in vec.items()}
                break
            factor = vec[r]
            for k, z in pivots[r].items():
                t = (vec.get(k,0) - factor*z) % modulus
                if t:vec[k]=t
                else:vec.pop(k,None)
    return len(pivots)

BOUNDARY_RANKS = {}
for p in (2,3,5,13):
    ranks = []
    for d in range(1,6):
        cols = []
        for upper in FACES:
            if D[upper] != d:continue
            indices = [i for i in range(N) if upper >> i & 1]
            cols.append({upper ^ (1 << v): (-1)**j for j,v in enumerate(indices)})
        ranks.append(modular_rank(cols,p))
    assert ranks == [9,36,84,55,5], (p,ranks)
    BOUNDARY_RANKS[p] = ranks

print('GRAPH_VERTICES=10 GRAPH_EDGES=15 FORBIDDEN_P4=60')
print('FACES_NONEMPTY=390 F_VECTOR=(10,45,120,150,60,5)')
print('FACETS_DIM3=10 FACETS_DIM4=30 FACETS_DIM5=5')
print(f'HASSE_INCIDENCES={incidences} ACYCLIC_KAHN_VISITED={visited}')
print('MORSE_PAIRS=187 CRITICAL_DIMS={0:1,3:13,4:2}')
print('MORSE_BOUNDARY_13x2='+repr(B))
print('UNIMODULAR_MINOR=-1 MORSE_H3_RANK=11')
print('HOMOTOPY=WEDGE_11_S3')
print('S5_H3_CHARACTER='+repr(characters))
print('S5_H3_IRREPS='+repr(MULTS))
print('SIMPLICIAL_BOUNDARY_RANKS='+repr(BOUNDARY_RANKS))
print('VERIFY_OK')
