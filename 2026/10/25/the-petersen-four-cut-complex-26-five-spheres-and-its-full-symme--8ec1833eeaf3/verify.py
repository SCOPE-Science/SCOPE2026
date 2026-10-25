#!/usr/bin/env python3
"""Exact finite verifier for the 4-cut complex of the Petersen graph.

Uses only the Python standard library. Constructs every face and every
cover relation, certifies a complete acyclic Morse matching, computes
integer signed Lefschetz traces, and decomposes the S5 character.
"""
from collections import defaultdict, Counter, deque
from functools import lru_cache
from itertools import combinations
from math import factorial

LABELS = tuple(combinations(range(5), 2))
N = len(LABELS)
FULL = (1 << N) - 1
assert N == 10
NEIGHBORS = [0] * N
for i, a in enumerate(LABELS):
    for j, b in enumerate(LABELS):
        if i != j and not set(a).intersection(b):
            NEIGHBORS[i] |= 1 << j


def induced_connected(mask):
    visited = mask & -mask
    while True:
        new = visited
        for v in range(N):
            if (visited >> v) & 1:
                new |= NEIGHBORS[v] & mask
        if new == visited:
            return new == mask
        visited = new


FOUR_MASKS = [sum(1 << i for i in t) for t in combinations(range(N), 4)]
assert len(FOUR_MASKS) == 210
FACETS = [FULL ^ a for a in FOUR_MASKS if not induced_connected(a)]
assert len(FACETS) == 140
assert sum(induced_connected(a) for a in FOUR_MASKS) == 70
assert all(f.bit_count() == 6 for f in FACETS)
FACES = set()
for facet in FACETS:
    sub = facet
    while True:
        FACES.add(sub)
        if sub == 0:
            break
        sub = (sub-1) & facet
BY_DIM = defaultdict(list)
for face in sorted(FACES):
    BY_DIM[face.bit_count()-1].append(face)
assert [len(BY_DIM[k]) for k in range(-1, 6)] == [1,10,45,120,210,240,140]

# Finite acyclic matching: keep the vertex 0 as a basepoint, and on all
# other faces successively match face F to F U {i} whenever both remain.
basepoint = 1
remaining = set(FACES) - {0, basepoint}
matched_pairs = set()
for i in range(N):
    bit = 1 << i
    now = {(f, f | bit) for f in remaining if not f & bit and (f | bit) in remaining}
    assert all(a != b and b == a | bit for a,b in now)
    assert len({x for pair in now for x in pair}) == 2*len(now)
    for a,b in now:
        remaining.remove(a)
        remaining.remove(b)
    matched_pairs |= now
assert len(matched_pairs) == 369
assert len(remaining) == 26
assert all(f.bit_count() == 6 for f in remaining)
assert len({x for a,b in matched_pairs for x in (a,b)}) == 738

# Verify every directed Hasse relation; reverse the matched covers.
# The vertex basepoint is not matched and the empty face is excluded.
nonempty = FACES - {0}
adj = {f: [] for f in nonempty}
indegree = {f: 0 for f in nonempty}
num_covers = 0
for hi in nonempty:
    for i in range(N):
        bit = 1 << i
        if not hi & bit:
            continue
        lo = hi ^ bit
        if lo == 0:
            continue
        if (lo,hi) in matched_pairs:
            tail, head = lo,hi
        else:
            tail, head = hi,lo
        adj[tail].append(head)
        indegree[head] += 1
        num_covers += 1
q = deque([f for f in nonempty if indegree[f] == 0])
seen = 0
while q:
    f = q.popleft()
    seen += 1
    for g in adj[f]:
        indegree[g] -= 1
        if indegree[g] == 0:
            q.append(g)
assert seen == len(nonempty) == 765
assert len(nonempty) == 2*len(matched_pairs)+1+26

# Independent exact mod-two boundary-rank cross-check of reduced Betti numbers.
def rank_mod2(k):
    if k < 0:
        return 0
    rowid = {face:i for i,face in enumerate(BY_DIM[k-1])}
    pivots = {}
    for face in BY_DIM[k]:
        col = 0
        for i in range(N):
            if face >> i & 1:
                col ^= 1 << rowid[face ^ (1 << i)]
        while col:
            j = col.bit_length()-1
            if j in pivots:
                col ^= pivots[j]
            else:
                pivots[j] = col
                break
    return len(pivots)
ranks = [rank_mod2(k) for k in range(6)]
assert ranks == [1,9,36,84,126,114], ranks
betti = {k:len(BY_DIM[k])-ranks[k]-(ranks[k+1] if k+1 <=5 else 0) for k in range(6)}
assert betti == {0:0,1:0,2:0,3:0,4:0,5:26}, betti


def partitions(n, maximum=None):
    if n == 0:
        yield ()
    else:
        for a in range(min(n, maximum or n), 0, -1):
            for tail in partitions(n-a, a):
                yield (a,) + tail


def class_representative(lam):
    p = list(range(5))
    start = 0
    for ell in lam:
        xs = list(range(start, start+ell))
        for a,b in zip(xs, xs[1:]+xs[:1]):
            p[a] = b
        start += ell
    return tuple(p)


def induced_vertex_perm(g):
    return tuple(LABELS.index(tuple(sorted((g[a],g[b])))) for a,b in LABELS)


def signed_fixed_face(face, pi):
    domain = [i for i in range(N) if face >> i & 1]
    image = [pi[i] for i in domain]
    if sorted(image) != domain:
        return 0
    inversions = sum(image[i] > image[j] for i in range(len(image)) for j in range(i+1, len(image)))
    return 1 if inversions % 2 == 0 else -1


def top_homology_trace(g):
    pi = induced_vertex_perm(g)
    # Since all reduced homology is in odd degree five,
    # top trace = - reduced Lefschetz number.
    aug_alt_trace = -1  # empty face in degree -1
    for f in nonempty:
        aug_alt_trace += (-1 if f.bit_count() % 2 == 0 else 1) * signed_fixed_face(f,pi)
    return -aug_alt_trace

EXPECTED = {(5,):1, (4,1):0, (3,2):0, (3,1,1):2,
            (2,2,1):-2, (2,1,1,1):6, (1,1,1,1,1):26}
character = {t:top_homology_trace(class_representative(t)) for t in partitions(5)}
assert character == EXPECTED, character

# Independently cross-check that the character is class-invariant on S5.
# This is a finite check of all 120 label relabelings, not an appeal to names.
from itertools import permutations
for g in permutations(range(5)):
    visited = set(); cycle_lengths = []
    for i in range(5):
        if i not in visited:
            cur=i; length=0
            while cur not in visited:
                visited.add(cur); length+=1;cur=g[cur]
            cycle_lengths.append(length)
    t=tuple(sorted(cycle_lengths,reverse=True))
    assert top_homology_trace(g) == EXPECTED[t]

# Murnaghan-Nakayama irreducible characters, implemented independently.
def border_strip_sign(lam, mu, size):
    boxes = {(i,j) for i,r in enumerate(lam) for j in range(r)} - \
            {(i,j) for i,r in enumerate(mu) for j in range(r)}
    if len(boxes) != size:
        return None
    reach = {next(iter(boxes))}
    stack = list(reach)
    while stack:
        i,j = stack.pop()
        for nb in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if nb in boxes and nb not in reach:
                reach.add(nb);stack.append(nb)
    if reach != boxes:
        return None
    if any((i+1,j) in boxes and (i,j+1) in boxes and (i+1,j+1) in boxes for i,j in boxes):
        return None
    return -1 if (len({i for i,j in boxes})-1) % 2 else 1

@lru_cache(None)
def specht_char(lam, cyc):
    if not cyc:
        return int(not lam)
    sz = cyc[0]
    out = 0
    for m in range(sum(lam)+1):
        for sub in partitions(m):
            if all((sub[i] if i<len(sub) else 0)<=lam[i] for i in range(len(lam))):
                sign = border_strip_sign(lam,sub,sz)
                if sign is not None:
                    out += sign*specht_char(sub,cyc[1:])
    return out

def centralizer_size(t):
    res=1
    for size,mult in Counter(t).items():
        res *= size**mult * factorial(mult)
    return res

MULT = {(5,):1,(4,1):2,(3,2):1,(3,1,1):2,
        (2,2,1):0,(2,1,1,1):0,(1,1,1,1,1):0}
for shape in partitions(5):
    num = sum(character[t]*specht_char(shape,t) * (120//centralizer_size(t)) for t in character)
    assert num == 120*MULT[shape], (shape,num)
assert sum(MULT[lam]*specht_char(lam,(1,1,1,1,1)) for lam in MULT) == 26
print('PET_EMPTY_PLUS_BASEPOINT_MORSE_ACYCLIC')
print('f-vector', [len(BY_DIM[k]) for k in range(6)], 'facets',len(FACETS),'cover_relations',num_covers)
print('matching_pairs',len(matched_pairs),'critical_0',1,'critical_5',len(remaining))
print('mod2_boundary_ranks',ranks)
print('S5_top_character',character)
print('Specht_multiplicities',MULT)
print('PETERSEN_FOUR_CUT_HOMOTOPY_AND_CHARACTER_VERIFIED')
