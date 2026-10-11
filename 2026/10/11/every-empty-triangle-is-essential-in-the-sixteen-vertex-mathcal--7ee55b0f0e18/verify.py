#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from math import gcd

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,7),
(1,4,6,8),(1,4,7,8),(1,5,6,9),(1,5,7,10),(1,5,9,10),(1,6,8,11),
(1,6,9,11),(1,7,8,12),(1,7,10,13),(1,7,12,13),(1,8,11,14),(1,8,12,14),
(1,9,10,13),(1,9,11,15),(1,9,13,16),(1,9,15,16),(1,11,14,15),
(1,12,13,16),(1,12,14,15),(1,12,15,16),(2,3,4,9),(2,3,5,16),(2,3,9,10),
(2,3,10,16),(2,4,6,13),(2,4,9,12),(2,4,12,13),(2,5,6,15),(2,5,8,15),
(2,5,8,16),(2,6,7,13),(2,6,7,15),(2,7,8,12),(2,7,8,15),(2,7,12,13),
(2,8,12,14),(2,8,14,16),(2,9,10,12),(2,10,12,14),(2,10,14,16),
(3,4,7,9),(3,5,7,11),(3,5,11,16),(3,6,8,10),(3,6,8,11),(3,6,10,16),
(3,6,11,16),(3,7,9,14),(3,7,11,14),(3,8,9,10),(3,8,9,14),(3,8,11,14),
(4,5,10,11),(4,5,10,14),(4,5,11,16),(4,5,13,14),(4,5,13,16),(4,6,8,10),
(4,6,10,14),(4,6,13,14),(4,7,8,15),(4,7,9,15),(4,8,10,15),(4,9,11,12),
(4,9,11,15),(4,10,11,15),(4,11,12,16),(4,12,13,16),(5,6,9,12),
(5,6,12,15),(5,7,10,11),(5,8,13,15),(5,8,13,16),(5,9,10,12),
(5,10,12,14),(5,12,14,15),(5,13,14,15),(6,7,13,14),(6,7,14,16),
(6,7,15,16),(6,9,11,12),(6,10,14,16),(6,11,12,16),(6,12,15,16),
(7,9,14,16),(7,9,15,16),(7,10,11,13),(7,11,13,14),(8,9,10,13),
(8,9,13,16),(8,9,14,16),(8,10,13,15),(10,11,13,15),(11,13,14,15)
}
V = tuple(range(1,17))

def faces(k):
    return sorted({tuple(sorted(c)) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
assert (len(V),len(E),len(T),len(FACETS)) == (16,116,200,100)
ESET,TSET = set(E),set(T)

TREE = {(1,v) for v in range(2,17)}
assert TREE <= ESET
NTE = [e for e in E if e not in TREE]
assert len(NTE) == 101
EI = {e:i for i,e in enumerate(NTE)}

def triangle_relation(t):
    a,b,c = t
    row = [0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI:
            row[EI[e]] += s
    return row

R = [triangle_relation(t) for t in T]

Y = {
(2,7):1,(2,8):1,(2,12):1,(2,13):1,(2,14):1,(2,15):1,(2,16):1,
(3,16):1,(4,12):1,(4,13):1,(4,14):1,(4,16):1,(5,8):1,(5,12):1,
(5,13):1,(5,14):1,(5,15):1,(5,16):1,(6,7):1,(6,12):1,(6,13):1,
(6,14):1,(6,15):1,(6,16):1,(9,12):1,(10,12):1,(10,14):1,(10,16):1,
(11,12):1,(11,16):1
}
y = [Y.get(e,0) for e in NTE]
assert gcd(*[abs(x) for x in y if x]) == 1
assert all(sum(a*b for a,b in zip(row,y)) == 0 for row in R)

PIVROWS = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,60,61,62,63,64,65,66,67,70,74,76,77,78,79,80,81,82,83,84,86,88,91,92,93,94,95,96,98,100,103,108,109,110,111,112,116,117,120,124,128,134,136,140,142,163]
PIVCOLS = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100]
assert len(PIVROWS) == len(PIVCOLS) == 100

def bareiss_det(A):
    A = [row[:] for row in A]
    n = len(A)
    sign = 1
    prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            j = next((j for j in range(k+1,n) if A[j][k]), None)
            assert j is not None
            A[k],A[j] = A[j],A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j] = (A[i][j]*pivot - A[i][k]*A[k][j]) // prev
        prev = pivot
        for i in range(k+1,n):
            A[i][k] = 0
        for j in range(k+1,n):
            A[k][j] = 0
    return sign*A[-1][-1]

minor = [[R[i][j] for j in PIVCOLS] for i in PIVROWS]
assert bareiss_det(minor) == -4

def rref_basis_mod2(rows):
    B = {}
    for row in rows:
        x = sum((a&1)<<i for i,a in enumerate(row))
        for p in sorted(B, reverse=True):
            if (x>>p)&1:
                x ^= B[p]
        if not x:
            continue
        p = x.bit_length()-1
        for q in list(B):
            if (B[q]>>p)&1:
                B[q] ^= x
        B[p] = x
    return dict(sorted(B.items(), reverse=True))

B = rref_basis_mod2(R)
assert len(B) == 98
NONP = [i for i in range(101) if i not in B]
assert NONP == [4,6,12]
assert [NTE[i] for i in NONP] == [(2,7),(2,9),(2,16)]
assert [y[i]&1 for i in NONP] == [1,0,1]

def cycle_vec(t):
    a,b,c = sorted(t)
    row = [0]*len(NTE)
    for e,s in [((a,b),1),((b,c),1),((a,c),-1)]:
        if e in EI:
            row[EI[e]] += s
    return row

def mod2_coords(row):
    x = sum((a&1)<<i for i,a in enumerate(row))
    for p,b in B.items():
        if (x>>p)&1:
            x ^= b
    c = tuple((x>>i)&1 for i in NONP)
    return c

def class_coord(t):
    z = cycle_vec(t)
    n = sum(a*b for a,b in zip(z,y))
    c0,c1,c2 = mod2_coords(z)
    assert (n&1) == (c0^c2)
    return (n,c1,c2)

cliques = [
    t for t in combinations(V,3)
    if all(tuple(sorted(e)) in ESET for e in combinations(t,2))
]
empty = [t for t in cliques if t not in TSET]
assert len(cliques) == 507
assert len(empty) == 307

oriented = Counter(class_coord(t) for t in empty)
assert (0,0,0) not in oriented
assert set(n for n,_,_ in oriented) <= {-1,0,1}

def unoriented(c):
    n,a,b = c
    return (-n,a,b) if n < 0 else c

classes = Counter(unoriented(class_coord(t)) for t in empty)
assert classes == Counter({
    (0,1,1):55,
    (0,1,0):53,
    (0,0,1):49,
    (1,1,0):38,
    (1,1,1):38,
    (1,0,0):37,
    (1,0,1):37
})
assert sum(v for (n,_,_),v in classes.items() if n==0) == 157
assert sum(v for (n,_,_),v in classes.items() if n==1) == 150

# Interpretation:
# a 100x100 minor of determinant 4 gives rank at least 100; y gives rank at most 100.
# Mod-2 rank 98 means exactly two Smith factors are even. Since their product divides 4
# and is divisible by 4, the torsion is (Z/2)^2. The primitive y gives the Z coordinate.
# On the mod-2 quotient, the nonpivot coordinates are (c0,c1,c2) with free parity c0+c2.
# Hence, at fixed free coordinate, (c1,c2) gives exact torsion coordinates.

print(
    "VERIFY_OK f=16,116,200,100 H1_Z=Z+Z2+Z2 "
    "maximal_minor_det=-4 rank_mod2=98 "
    "graph_triangles=507 facial3=200 empty3=307 all_empty3_nonzero=yes "
    "torsion_systoles=157 torsion_counts=55,53,49 "
    "primitive_infinite_systoles=150 lift_counts=38,38,37,37"
)
