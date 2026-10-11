#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque, Counter

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,8),
(1,3,7,8),(1,4,6,9),(1,4,7,9),(1,5,6,10),(1,5,8,10),(1,6,9,11),
(1,6,10,11),(1,7,8,12),(1,7,9,12),(1,8,10,12),(1,9,11,12),(1,10,11,12),
(2,3,4,10),(2,3,5,11),(2,3,9,10),(2,3,9,11),(2,4,6,13),(2,4,10,14),
(2,4,13,14),(2,5,6,15),(2,5,11,15),(2,6,12,13),(2,6,12,15),(2,7,8,12),
(2,7,8,16),(2,7,12,13),(2,7,13,14),(2,7,14,16),(2,8,9,11),(2,8,9,16),
(2,8,11,15),(2,8,12,15),(2,9,10,14),(2,9,14,16),(3,4,7,10),(3,5,8,14),
(3,5,11,17),(3,5,14,17),(3,6,8,14),(3,6,8,16),(3,6,12,13),(3,6,12,17),
(3,6,13,16),(3,6,14,17),(3,7,8,16),(3,7,10,16),(3,9,10,13),(3,9,11,12),
(3,9,12,13),(3,10,13,16),(3,11,12,17),(4,5,7,10),(4,5,7,15),
(4,5,10,14),(4,5,13,14),(4,5,13,15),(4,6,9,16),(4,6,13,16),(4,7,9,15),
(4,9,15,16),(4,13,15,16),(5,6,7,10),(5,6,7,15),(5,8,10,14),
(5,11,13,15),(5,11,13,17),(5,13,14,17),(6,7,10,11),(6,7,11,14),
(6,7,14,17),(6,7,15,17),(6,8,9,11),(6,8,9,16),(6,8,11,14),(6,12,15,17),
(7,9,12,13),(7,9,13,17),(7,9,15,17),(7,10,11,16),(7,11,14,16),
(7,13,14,17),(8,10,12,15),(8,10,14,15),(8,11,14,15),(9,10,13,17),
(9,10,14,15),(9,10,15,17),(9,14,15,16),(10,11,12,17),(10,11,13,16),
(10,11,13,17),(10,12,15,17),(11,13,15,16),(11,14,15,16)
}
V = tuple(range(1,18))

def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
assert (len(V),len(E),len(T),len(FACETS)) == (17,117,200,100)
ESET, TSET = set(E), set(T)

# Contract a deterministic spanning tree of the one-skeleton.
adj = defaultdict(list)
for a,b in E:
    adj[a].append(b)
    adj[b].append(a)
TREE = set()
seen = {1}
q = deque([1])
while q:
    u = q.popleft()
    for v in adj[u]:
        if v not in seen:
            seen.add(v)
            q.append(v)
            TREE.add(tuple(sorted((u,v))))
assert len(TREE) == 16

NTE = [e for e in E if e not in TREE]
EI = {e:i for i,e in enumerate(NTE)}
assert len(NTE) == 101

def triangle_relation(t):
    a,b,c = sorted(t)
    row = [0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI:
            row[EI[e]] += s
    return row

R = [triangle_relation(t) for t in T]

def unit_reduce(A):
    # Integral row/column operations only: swaps, sign changes, and
    # addition of integer multiples.
    A = [row[:] for row in A]
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
                qv = A[i][k]
                A[i] = [x-qv*y for x,y in zip(A[i],A[k])]
        for j in range(n):
            if j != k and A[k][j]:
                qv = A[k][j]
                for i in range(m):
                    A[i][j] -= qv*A[i][k]
        k += 1
    return k,A

r1, RR = unit_reduce(R)
assert r1 == 99
for i in range(len(RR)):
    for j in range(len(RR[0])):
        if i < 99 or j < 99:
            assert RR[i][j] == (1 if i == j and i < 99 else 0)

residual = [row[99:] for row in RR[99:]]
assert all(x % 3 == 0 for row in residual for x in row)
r2, BB = unit_reduce([[x//3 for x in row] for row in residual])
assert r2 == 1
for i in range(len(BB)):
    for j in range(len(BB[0])):
        assert BB[i][j] == (1 if i == j and i < 1 else 0)
# Hence the Smith form is diag(1^99,3,0), so H_1 = Z + Z/3.

Y = {
(2,10):-1,(3,10):-1,(3,14):1,(4,5):-1,(4,10):-1,(4,15):-1,
(5,7):1,(5,13):1,(5,14):1,(6,7):1,(6,14):1,(7,10):-1,
(7,11):-1,(7,15):-1,(7,17):-1,(8,14):1,(9,10):-1,(9,15):-1,
(9,17):-1,(10,13):1,(10,14):1,(10,16):1,(11,13):1,(11,14):1,
(11,16):1,(13,15):-1,(13,17):-1,(14,15):-1,(14,17):-1,(15,16):1
}
W = {
(2,7):2,(2,8):2,(2,9):1,(2,11):1,(2,12):2,(3,6):2,(3,9):1,
(3,11):1,(3,12):1,(3,13):2,(3,16):1,(4,16):2,(5,11):1,(6,8):1,
(6,12):2,(6,14):1,(6,16):2,(6,17):1,(7,13):1,(7,14):1,(7,16):1,
(7,17):1,(8,9):2,(8,11):2,(8,15):1,(8,16):1,(9,10):2,(9,13):1,
(9,14):2,(9,16):2,(9,17):1,(10,13):2,(10,15):1,(10,16):1,
(10,17):2,(11,13):2,(11,14):1,(11,15):2,(11,16):1,(11,17):2,
(12,13):1,(12,15):1,(12,17):2,(13,16):2,(14,15):1,(15,16):2,
(15,17):1
}
y = [Y.get(e,0) for e in NTE]
w = [W.get(e,0) for e in NTE]
assert all(sum(a*b for a,b in zip(row,y)) == 0 for row in R)
assert all(sum((a%3)*b for a,b in zip(row,w)) % 3 == 0 for row in R)

def triangle_cycle(t):
    a,b,c = sorted(t)
    row = [0]*len(NTE)
    for e,s in [((a,b),1),((b,c),1),((a,c),-1)]:
        if e in EI:
            row[EI[e]] += s
    return row

def coord(t):
    x = triangle_cycle(t)
    return (
        sum(a*b for a,b in zip(x,y)),
        sum((a%3)*b for a,b in zip(x,w)) % 3
    )

# These two cycles prove surjectivity onto Z + Z/3.
assert coord((1,5,7)) == (1,0)
assert coord((1,2,9)) == (0,1)
# Since H_1 is already proved to be Z + Z/3, these are exact coordinates.

cliques = [
    c for c in combinations(V,3)
    if all(tuple(sorted(e)) in ESET for e in combinations(c,2))
]
empty = [c for c in cliques if c not in TSET]
assert len(cliques) == 439
assert len(empty) == 239

signed = Counter(coord(c) for c in empty)
assert signed == Counter({
    (0,1):70,(0,2):60,
    (1,0):20,(-1,0):21,
    (1,1):16,(-1,2):18,
    (1,2):23,(-1,1):11
})

def unoriented(v):
    n,t = v
    if n > 0:
        return (n,t)
    if n < 0:
        return (-n,(-t)%3)
    if t:
        return (0,1)
    return (0,0)

counts = Counter(unoriented(coord(c)) for c in empty)
assert counts == Counter({
    (0,1):130,
    (1,0):41,
    (1,1):34,
    (1,2):34
})
assert all(coord(c) != (0,0) for c in empty)
assert all(abs(coord(c)[0]) <= 1 for c in empty)

print(
    "VERIFY_OK f=17,117,200,100 H1_Z=Z+Z/3 "
    "graph_triangles=439 facial3=200 empty3=239 "
    "all_empty3_nonzero=yes pure_order3=130 "
    "primitive_free_types=41,34,34 "
    "unoriented_types=t|g|g+t|g+2t "
    "smith=1^99,3,0"
)
