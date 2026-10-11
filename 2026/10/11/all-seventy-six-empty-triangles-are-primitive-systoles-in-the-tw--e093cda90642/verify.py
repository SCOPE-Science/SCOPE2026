#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

FACETS = {
(1,2,4,5,10),(1,2,4,5,11),(1,2,4,10,11),(1,2,5,10,11),
(1,3,6,7,8),(1,3,6,7,9),(1,3,6,8,9),(1,3,7,8,9),
(1,4,5,10,12),(1,4,5,11,12),(1,4,6,10,11),(1,4,6,10,12),
(1,4,6,11,12),(1,5,7,10,11),(1,5,7,10,12),(1,5,7,11,12),
(1,6,7,8,11),(1,6,7,9,10),(1,6,7,10,11),(1,6,8,9,12),
(1,6,8,11,12),(1,6,9,10,12),(1,7,8,9,12),(1,7,8,11,12),
(1,7,9,10,12),(2,3,4,7,8),(2,3,4,7,9),(2,3,4,8,10),
(2,3,4,9,11),(2,3,4,10,11),(2,3,5,6,8),(2,3,5,6,9),
(2,3,5,8,10),(2,3,5,9,11),(2,3,5,10,11),(2,3,6,7,8),
(2,3,6,7,9),(2,4,5,8,9),(2,4,5,8,10),(2,4,5,9,11),
(2,4,7,8,9),(2,5,6,8,9),(2,6,7,8,12),(2,6,7,9,12),
(2,6,8,9,12),(2,7,8,9,12),(3,4,5,8,9),(3,4,5,8,10),
(3,4,5,9,11),(3,4,5,10,12),(3,4,5,11,12),(3,4,7,8,9),
(3,4,10,11,12),(3,5,6,8,9),(3,5,10,11,12),(4,6,10,11,12),
(5,7,10,11,12),(6,7,8,11,12),(6,7,9,10,12),(6,7,10,11,12)
}
V = tuple(range(1,13))

def faces(k):
    return sorted({tuple(sorted(c)) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
Q = faces(4)
assert (len(V),len(E),len(T),len(Q),len(FACETS)) == (12,66,144,150,60)
ESET, TSET = set(E), set(T)

# Contract a fixed spanning tree. The remaining 55 edges generate the graph cycle lattice.
TREE = {(1,v) for v in range(2,13)}
assert TREE <= ESET
NTE = [e for e in E if e not in TREE]
EI = {e:i for i,e in enumerate(NTE)}
assert len(NTE) == 55

def triangle_relation(t):
    a,b,c = sorted(t)
    row = [0]*len(NTE)
    # Oriented boundary [b,c]-[a,c]+[a,b].
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI:
            row[EI[e]] += s
    return row

R = [triangle_relation(t) for t in T]

def unit_pivot_reduce(A):
    # Integral row/column operations only: swaps, sign changes, and adding
    # integer multiples. A completed identity block is therefore Smith data.
    A = [r[:] for r in A]
    m,n = len(A),len(A[0])
    k = 0
    while k < min(m,n):
        pos = None
        for i in range(k,m):
            for j in range(k,n):
                if abs(A[i][j]) == 1:
                    pos = (i,j)
                    break
            if pos is not None:
                break
        if pos is None:
            break
        i,j = pos
        A[k],A[i] = A[i],A[k]
        for r in range(m):
            A[r][k],A[r][j] = A[r][j],A[r][k]
        if A[k][k] == -1:
            A[k] = [-x for x in A[k]]
        for i in range(m):
            if i != k and A[i][k]:
                q = A[i][k]
                A[i] = [x-q*y for x,y in zip(A[i],A[k])]
        for j in range(n):
            if j != k and A[k][j]:
                q = A[k][j]
                for i in range(m):
                    A[i][j] -= q*A[i][k]
        k += 1
    return k,A

rank, RR = unit_pivot_reduce(R)
assert rank == 54
for i in range(len(RR)):
    for j in range(len(RR[0])):
        assert RR[i][j] == (1 if i == j and i < 54 else 0)
# Therefore H_1 = Z^55 / <facial triangle relations> is Z.

# An explicit primitive integral cocycle on the contracted graph.
Y = {
(2,3):-1,(2,6):-1,(2,7):-1,(2,8):-1,(2,9):-1,(2,12):-1,
(3,4):1,(3,5):1,(3,10):1,(3,11):1,(3,12):1,
(4,7):-1,(4,8):-1,(4,9):-1,
(5,6):-1,(5,8):-1,(5,9):-1,
(8,10):1,(9,11):1
}
y = [Y.get(e,0) for e in NTE]
assert all(sum(a*b for a,b in zip(row,y)) == 0 for row in R)

def oriented_cycle(seq):
    row = [0]*len(NTE)
    for a,b in zip(seq, seq[1:]+seq[:1]):
        if a < b:
            e,s = (a,b),1
        else:
            e,s = (b,a),-1
        if e in EI:
            row[EI[e]] += s
    return row

def pairing_oriented(seq):
    x = oriented_cycle(list(seq))
    return sum(a*b for a,b in zip(x,y))

# Surjectivity: the cocycle evaluates to a unit on a cycle.
assert abs(pairing_oriented((1,2,3))) == 1

ALL_TRI = list(combinations(V,3))
EMPTY = [t for t in ALL_TRI if t not in TSET]
assert len(ALL_TRI) == 220 and len(EMPTY) == 76
pair_counts = Counter(pairing_oriented(t) for t in EMPTY)
assert pair_counts == Counter({-1:46, 1:30})
# Since the coordinate H_1 -> Z is an isomorphism, every empty triangle
# is a primitive generator.

# Exhaust the full simplicial automorphism group. Any automorphism preserves
# triangular-face membership, so use that necessary condition during
# backtracking and verify the complete facet set at leaves.
def enumerate_automorphisms():
    autos = []
    order = list(V)
    used = set()
    mp = {}
    def rec(i):
        if i == len(order):
            img = {tuple(sorted(mp[x] for x in f)) for f in FACETS}
            if img == FACETS:
                autos.append(tuple(mp[v] for v in V))
            return
        v = order[i]
        for w in V:
            if w in used:
                continue
            mp[v] = w
            used.add(w)
            ok = True
            if i >= 2:
                for a,b in combinations(order[:i],2):
                    src = tuple(sorted((a,b,v))) in TSET
                    dst = tuple(sorted((mp[a],mp[b],w))) in TSET
                    if src != dst:
                        ok = False
                        break
            if ok:
                rec(i+1)
            used.remove(w)
            del mp[v]
    rec(0)
    return autos

AUT = enumerate_automorphisms()
assert len(AUT) == 96

def image_set(t,p):
    return tuple(sorted(p[v-1] for v in t))

remaining = set(EMPTY)
orbits = []
while remaining:
    rep = min(remaining)
    orb = {image_set(rep,p) for p in AUT}
    orbits.append((rep,len(orb)))
    remaining -= orb
assert orbits == [((1,2,3),12),((1,2,6),48),((1,4,8),16)]

# Exact induced action on H_1: apply each permutation to an oriented
# generator cycle, preserving its cyclic order.
rep = (1,2,3)
base = pairing_oriented(rep)
action_counts = Counter()
for p in AUT:
    image_cycle = tuple(p[v-1] for v in rep)
    val = pairing_oriented(image_cycle)
    assert val in (-1,1)
    action_counts[val//base] += 1
assert action_counts == Counter({1:48,-1:48})

print(
    "VERIFY_OK f=12,66,144,150,60 H1_Z=Z "
    "all_triangles=220 facial3=144 empty3=76 "
    "all_empty3_primitive=yes oriented_pairings=+1:30,-1:46 "
    "aut=96 carrier_orbits=12,48,16 reps=123|126|148 "
    "H1_action=+1:48,-1:48"
)
