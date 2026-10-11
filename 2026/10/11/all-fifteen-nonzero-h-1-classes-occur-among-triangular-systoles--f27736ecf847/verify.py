#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque, Counter

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,7),
(1,4,6,8),(1,4,7,9),(1,4,8,9),(1,5,6,10),(1,5,7,11),(1,5,10,11),
(1,6,8,10),(1,7,9,12),(1,7,11,13),(1,7,12,13),(1,8,9,12),(1,8,10,14),
(1,8,12,14),(1,10,11,13),(1,10,13,14),(1,12,13,14),(2,3,4,10),
(2,3,5,13),(2,3,10,15),(2,3,11,13),(2,3,11,15),(2,4,6,16),(2,4,10,16),
(2,5,6,9),(2,5,9,13),(2,6,9,16),(2,9,11,13),(2,9,11,14),(2,9,14,16),
(2,10,15,16),(2,11,14,15),(2,14,15,16),(3,4,7,17),(3,4,10,12),
(3,4,12,17),(3,5,7,16),(3,5,13,16),(3,6,9,15),(3,6,9,16),(3,6,11,15),
(3,6,11,16),(3,7,14,16),(3,7,14,17),(3,9,10,12),(3,9,10,15),
(3,9,12,17),(3,9,14,16),(3,9,14,17),(3,11,13,16),(4,5,9,13),(4,5,9,15),
(4,5,10,11),(4,5,10,12),(4,5,11,14),(4,5,12,15),(4,5,13,14),(4,6,8,13),
(4,6,11,14),(4,6,11,16),(4,6,13,14),(4,7,9,15),(4,7,15,17),(4,8,9,13),
(4,10,11,16),(4,12,15,17),(5,6,9,15),(5,6,10,12),(5,6,12,15),
(5,7,8,11),(5,7,8,16),(5,8,11,17),(5,8,16,17),(5,11,14,17),
(5,13,14,17),(5,13,16,17),(6,7,8,10),(6,7,8,13),(6,7,10,12),
(6,7,12,13),(6,11,14,15),(6,12,13,14),(6,12,14,15),(7,8,10,14),
(7,8,11,13),(7,8,14,16),(7,9,10,12),(7,9,10,15),(7,10,14,17),
(7,10,15,17),(8,9,11,13),(8,9,11,17),(8,9,12,17),(8,12,14,16),
(8,12,16,17),(9,11,14,17),(10,11,13,16),(10,13,14,17),(10,13,16,17),
(10,15,16,17),(12,14,15,16),(12,15,16,17)
}
V = tuple(range(1,18))

def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
assert (len(V),len(E),len(T),len(FACETS)) == (17,124,214,107)
ESET = set(E)
TSET = set(T)

adj = defaultdict(list)
for a,b in E:
    adj[a].append(b)
    adj[b].append(a)
for v in adj:
    adj[v].sort()

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
assert len(NTE) == 108

def triangle_relation(t):
    a,b,c = t
    row = [0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI:
            row[EI[e]] += s
    return row

R = [triangle_relation(t) for t in T]

def reduce_with_Q(A):
    # Only unimodular integral row and column operations are used.
    # Q records the complete column basis change: transformed rows are r*Q.
    A = [r[:] for r in A]
    m,n = len(A),len(A[0])
    Q = [[int(i == j) for j in range(n)] for i in range(n)]
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
        if j != k:
            for row in A:
                row[k],row[j] = row[j],row[k]
            for row in Q:
                row[k],row[j] = row[j],row[k]
        if A[k][k] == -1:
            A[k] = [-x for x in A[k]]
        for i2 in range(m):
            if i2 != k and A[i2][k]:
                qv = A[i2][k]
                A[i2] = [x-qv*y for x,y in zip(A[i2],A[k])]
        for j2 in range(n):
            if j2 != k and A[k][j2]:
                qv = A[k][j2]
                for i2 in range(m):
                    A[i2][j2] -= qv*A[i2][k]
                for i2 in range(n):
                    Q[i2][j2] -= qv*Q[i2][k]
        k += 1
    return k,A,Q

def unit_reduce(A):
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
        if j != k:
            for row in A:
                row[k],row[j] = row[j],row[k]
        if A[k][k] == -1:
            A[k] = [-x for x in A[k]]
        for i2 in range(m):
            if i2 != k and A[i2][k]:
                qv = A[i2][k]
                A[i2] = [x-qv*y for x,y in zip(A[i2],A[k])]
        for j2 in range(n):
            if j2 != k and A[k][j2]:
                qv = A[k][j2]
                for i2 in range(m):
                    A[i2][j2] -= qv*A[i2][k]
        k += 1
    return k,A

rank, RR, Q = reduce_with_Q(R)
assert rank == 106
for i in range(len(RR)):
    for j in range(len(RR[0])):
        if i < 106 or j < 106:
            assert RR[i][j] == (1 if i == j and i < 106 else 0)

residual = [row[106:] for row in RR[106:]]
assert all(x % 4 == 0 for row in residual for x in row)
r2, BB = unit_reduce([[x//4 for x in row] for row in residual])
assert r2 == 2
for i in range(len(BB)):
    for j in range(len(BB[0])):
        assert BB[i][j] == (1 if i == j and i < 2 else 0)
# Smith form: diag(1^106,4,4), so H_1 is (Z/4)^2.

Y1 = [Q[i][106] for i in range(108)]
Y2 = [Q[i][107] for i in range(108)]
assert all(sum(a*b for a,b in zip(row,Y1)) % 4 == 0 for row in R)
assert all(sum(a*b for a,b in zip(row,Y2)) % 4 == 0 for row in R)

def triangle_cycle(t):
    a,b,c = t
    row = [0]*len(NTE)
    for e,s in [((a,b),1),((b,c),1),((a,c),-1)]:
        if e in EI:
            row[EI[e]] += s
    return row

def coord(t):
    x = triangle_cycle(t)
    return (
        sum(a*b for a,b in zip(x,Y1)) % 4,
        sum(a*b for a,b in zip(x,Y2)) % 4
    )

cliques = [
    c for c in combinations(V,3)
    if all(tuple(sorted(e)) in ESET for e in combinations(c,2))
]
empty = [c for c in cliques if c not in TSET]
assert len(cliques) == 519
assert len(empty) == 305

oriented = Counter(coord(c) for c in empty)
assert oriented == Counter({
    (1,0):34,(0,3):30,(2,1):30,(3,2):26,(3,3):25,
    (1,2):25,(3,1):23,(2,3):21,(1,1):20,(3,0):18,
    (0,1):18,(1,3):15,(2,0):13,(0,2):5,(2,2):2
})
assert (0,0) not in oriented
assert len(oriented) == 15

def canon(v):
    a,b = v
    neg = ((-a)%4,(-b)%4)
    return min(v,neg)

unoriented = Counter(canon(coord(c)) for c in empty)
order2 = sorted(v for v in unoriented if v != (0,0) and tuple((2*x)%4 for x in v) == (0,0))
order4 = sorted(v for v in unoriented if tuple((2*x)%4 for x in v) != (0,0))
assert sorted(unoriented[v] for v in order4) == [38,45,48,51,51,52]
assert sorted(unoriented[v] for v in order2) == [2,5,13]
assert len(order4) == 6 and len(order2) == 3

# Concrete basis representatives for reproducibility.
assert coord((2,4,11)) == (1,0)
assert coord((1,3,9)) == (0,1)

print(
    "VERIFY_OK f=17,124,214,107 H1_Z=Z4+Z4 "
    "graph_triangles=519 facial3=214 empty3=305 "
    "all_empty3_nonzero=yes all_15_nonzero_classes=yes "
    "order4_inverse_pair_counts=52,51,51,48,45,38 "
    "order2_counts=13,5,2 smith=1^106,4,4"
)
