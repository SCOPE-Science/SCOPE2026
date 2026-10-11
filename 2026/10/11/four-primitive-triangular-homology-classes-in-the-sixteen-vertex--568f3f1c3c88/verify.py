#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,7),
(1,4,6,8),(1,4,7,8),(1,5,6,8),(1,5,7,8),(2,3,4,9),(2,3,5,10),
(2,3,9,11),(2,3,10,11),(2,4,6,9),(2,5,6,12),(2,5,10,13),(2,5,12,13),
(2,6,9,14),(2,6,12,14),(2,7,10,11),(2,7,10,13),(2,7,11,15),(2,7,13,16),
(2,7,15,16),(2,8,12,13),(2,8,12,14),(2,8,13,16),(2,8,14,15),
(2,8,15,16),(2,9,11,15),(2,9,14,15),(3,4,7,12),(3,4,9,12),(3,5,7,16),
(3,5,10,16),(3,6,10,14),(3,6,10,16),(3,6,13,14),(3,6,13,15),
(3,6,15,16),(3,7,12,15),(3,7,15,16),(3,8,9,11),(3,8,9,12),(3,8,11,13),
(3,8,12,13),(3,10,11,14),(3,11,13,14),(3,12,13,15),(4,5,10,13),
(4,5,10,16),(4,5,13,15),(4,5,14,15),(4,5,14,16),(4,6,8,15),(4,6,9,13),
(4,6,13,15),(4,7,8,14),(4,7,11,12),(4,7,11,14),(4,8,14,15),(4,9,10,12),
(4,9,10,13),(4,10,12,16),(4,11,12,16),(4,11,14,16),(5,6,8,11),
(5,6,11,12),(5,7,8,9),(5,7,9,16),(5,8,9,11),(5,9,11,15),(5,9,14,15),
(5,9,14,16),(5,11,12,15),(5,12,13,15),(6,8,11,16),(6,8,15,16),
(6,9,13,14),(6,10,12,14),(6,10,12,16),(6,11,12,16),(7,8,9,10),
(7,8,10,14),(7,9,10,13),(7,9,13,16),(7,10,11,14),(7,11,12,15),
(8,9,10,12),(8,10,12,14),(8,11,13,16),(9,13,14,16),(11,13,14,16)
}
V = tuple(range(1,17))

def faces(k):
    return sorted({tuple(sorted(c)) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
assert (len(V), len(E), len(T), len(FACETS)) == (16,110,188,94)
ESET = set(E)
TSET = set(T)

TREE = {
(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),
(2,9),(2,10),(2,11),(2,12),(2,13),(2,14),(2,15),(2,16)
}
assert TREE <= ESET
NTE = [e for e in E if e not in TREE]
assert len(NTE) == 95
EI = {e:i for i,e in enumerate(NTE)}

def triangle_relation(t):
    a,b,c = sorted(t)
    row = [0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        e = tuple(sorted(e))
        if e in EI:
            row[EI[e]] += s
    return row

R = [triangle_relation(t) for t in T]

def unit_pivot_reduce(A):
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
assert rank == 93
for i in range(len(RR)):
    for j in range(len(RR[0])):
        expected = 1 if i == j and i < 93 else 0
        assert RR[i][j] == expected
# Hence the relation lattice is a primitive rank-93 direct summand of Z^95.

Y1 = {
(2,7):-1,(2,8):-1,(3,8):-1,(3,15):1,(3,16):1,(4,11):1,(4,14):1,
(4,15):1,(4,16):1,(5,9):1,(5,11):1,(5,14):1,(5,15):1,(5,16):1,
(6,11):1,(6,15):1,(6,16):1,(7,9):1,(7,10):1,(7,11):1,(7,13):1,
(7,14):1,(7,15):1,(7,16):1,(8,9):1,(8,10):1,(8,11):1,(8,12):1,
(8,13):1,(8,14):1,(8,15):1,(8,16):1,(10,16):1,(11,12):-1,
(12,15):1,(12,16):1,(13,15):1
}
Y2 = {
(2,7):-1,(2,8):-1,(3,12):1,(3,13):1,(3,15):1,(3,16):1,(4,5):1,
(4,10):1,(4,11):1,(4,12):1,(4,13):1,(4,14):1,(4,15):1,(4,16):2,
(5,16):1,(6,13):1,(6,15):1,(6,16):1,(7,10):1,(7,11):1,(7,12):1,
(7,13):1,(7,14):1,(7,15):1,(7,16):1,(8,10):1,(8,12):1,(8,13):1,
(8,14):1,(8,15):1,(8,16):1,(9,10):1,(9,12):1,(9,13):1,(9,16):1,
(10,16):1,(11,13):1,(11,16):1,(12,16):1,(13,14):-1,(14,16):1
}
y1 = [Y1.get(e,0) for e in NTE]
y2 = [Y2.get(e,0) for e in NTE]
assert all(sum(a*b for a,b in zip(row,y1)) == 0 for row in R)
assert all(sum(a*b for a,b in zip(row,y2)) == 0 for row in R)

def triangle_cycle(t):
    a,b,c = sorted(t)
    row = [0]*len(NTE)
    for e,s in [((a,b),1),((b,c),1),((a,c),-1)]:
        e = tuple(sorted(e))
        if e in EI:
            row[EI[e]] += s
    return row

def coord(t):
    x = triangle_cycle(t)
    return (
        sum(a*b for a,b in zip(x,y1)),
        sum(a*b for a,b in zip(x,y2))
    )

assert coord((2,5,9)) == (1,0)
assert coord((1,4,5)) == (0,1)
# Since H1 is free rank two and these cocycles give a surjection to Z^2,
# they are exact integral coordinates.

cliques = [
    tuple(c) for c in combinations(V,3)
    if all(tuple(sorted(e)) in ESET for e in combinations(c,2))
]
empty = [c for c in cliques if c not in TSET]
assert len(cliques) == 449
assert len(empty) == 261

def canon(v):
    a,b = v
    if a < 0 or (a == 0 and b < 0):
        return (-a,-b)
    return (a,b)

def gcd(a,b):
    a,b = abs(a),abs(b)
    while b:
        a,b = b,a%b
    return a

counts = Counter(canon(coord(c)) for c in empty)
assert counts == Counter({
    (0,0):43,
    (0,1):86,
    (1,1):66,
    (1,0):65,
    (1,2):1
})
assert [c for c in empty if canon(coord(c)) == (1,2)] == [(2,4,16)]
assert all(gcd(a,b) == 1 for c in empty for a,b in [coord(c)] if (a,b) != (0,0))

print(
    "VERIFY_OK f=16,110,188,94 H1_Z=Z^2 "
    "graph_triangles=449 facial3=188 empty3=261 "
    "null_empty3=43 primitive_systoles=218 "
    "unoriented_class_counts=86,66,65,1 "
    "class_vectors=01|11|10|12 singleton=2,4,16"
)
