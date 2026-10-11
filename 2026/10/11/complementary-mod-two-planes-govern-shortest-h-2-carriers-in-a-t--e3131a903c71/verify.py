#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from math import gcd

FACETS = {
(1,2,3,4,7),(1,2,3,4,10),(1,2,3,7,10),
(1,2,4,7,8),(1,2,4,8,11),(1,2,4,9,10),
(1,2,4,9,12),(1,2,4,11,12),(1,2,7,8,10),
(1,2,8,9,10),(1,2,8,9,12),(1,2,8,11,12),
(1,3,4,7,11),(1,3,4,10,11),(1,3,7,8,11),
(1,3,7,8,12),(1,3,7,9,10),(1,3,7,9,12),
(1,3,8,11,12),(1,3,9,10,12),(1,3,10,11,12),
(1,4,7,8,11),(1,4,9,10,11),(1,4,9,11,12),
(1,7,8,9,10),(1,7,8,9,12),(1,9,10,11,12),
(2,3,4,6,9),(2,3,4,6,10),(2,3,4,7,12),
(2,3,4,9,12),(2,3,5,7,9),(2,3,5,7,10),
(2,3,5,8,10),(2,3,5,8,11),(2,3,5,9,11),
(2,3,6,9,11),(2,3,6,10,11),(2,3,7,9,12),
(2,3,8,10,11),(2,4,5,7,8),(2,4,5,7,12),
(2,4,5,8,11),(2,4,5,11,12),(2,4,6,9,10),
(2,5,7,8,10),(2,5,7,9,11),(2,5,7,11,12),
(2,6,7,9,11),(2,6,7,9,12),(2,6,7,11,12),
(2,6,8,9,10),(2,6,8,9,12),(2,6,8,10,12),
(2,6,10,11,12),(2,8,10,11,12),(3,4,5,8,9),
(3,4,5,8,12),(3,4,5,9,12),(3,4,6,7,11),
(3,4,6,7,12),(3,4,6,8,9),(3,4,6,8,12),
(3,4,6,10,11),(3,5,7,9,10),(3,5,8,9,11),
(3,5,8,10,12),(3,5,9,10,12),(3,6,7,8,11),
(3,6,7,8,12),(3,6,8,9,11),(3,8,10,11,12),
(4,5,7,8,10),(4,5,7,10,12),(4,5,8,9,11),
(4,5,8,10,12),(4,5,9,11,12),(4,6,7,10,11),
(4,6,7,10,12),(4,6,8,9,10),(4,6,8,10,12),
(4,7,8,9,10),(4,7,8,9,11),(4,7,9,10,11),
(5,7,9,10,11),(5,7,10,11,12),(5,9,10,11,12),
(6,7,8,9,11),(6,7,8,9,12),(6,7,10,11,12)
}
V = tuple(range(1,13))

def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
Q = faces(4)
assert (len(V),len(E),len(T),len(Q),len(FACETS)) == (12,63,192,225,90)

EI = {e:i for i,e in enumerate(E)}
TI = {t:i for i,t in enumerate(T)}

def reduce_units(A, track_qinv=False, track_p=False):
    # Uses only unimodular integral row and column operations.
    A = [row[:] for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    Qinv = [[int(i == j) for j in range(n)] for i in range(n)] if track_qinv else None
    P = [[int(i == j) for j in range(m)] for i in range(m)] if track_p else None
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
        if i != k:
            A[k],A[i] = A[i],A[k]
            if P is not None:
                P[k],P[i] = P[i],P[k]
        if j != k:
            for row in A:
                row[k],row[j] = row[j],row[k]
            if Qinv is not None:
                Qinv[k],Qinv[j] = Qinv[j],Qinv[k]
        if A[k][k] == -1:
            A[k] = [-x for x in A[k]]
            if P is not None:
                P[k] = [-x for x in P[k]]
        for i2 in range(m):
            if i2 != k and A[i2][k]:
                q = A[i2][k]
                A[i2] = [x-q*y for x,y in zip(A[i2],A[k])]
                if P is not None:
                    P[i2] = [x-q*y for x,y in zip(P[i2],P[k])]
        for j2 in range(n):
            if j2 != k and A[k][j2]:
                q = A[k][j2]
                for i2 in range(m):
                    A[i2][j2] -= q*A[i2][k]
                if Qinv is not None:
                    Qinv[k] = [x+q*y for x,y in zip(Qinv[k],Qinv[j2])]
        k += 1
    return k,A,Qinv,P

def matvec(M,x):
    return [sum(a*b for a,b in zip(row,x)) for row in M]

# Integral boundary d2: C2 -> C1.
d2 = [[0]*len(T) for _ in E]
for j,(a,b,c) in enumerate(T):
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        d2[EI[e]][j] = s

r2,D2,Qinv,_ = reduce_units(d2,track_qinv=True)
assert r2 == 52
assert all(
    D2[i][j] == (1 if i == j and i < r2 else 0)
    for i in range(len(D2)) for j in range(len(D2[0]))
)
# Hence ker(d2) is an explicit primitive Z-basis of rank 140.

# Express d3: C3 -> ker(d2) in that basis.
d3cols = []
for a,b,c,d in Q:
    x = [0]*len(T)
    for t,s in [((b,c,d),1),((a,c,d),-1),((a,b,d),1),((a,b,c),-1)]:
        x[TI[t]] = s
    y = matvec(Qinv,x)
    assert all(v == 0 for v in y[:r2])
    d3cols.append(y[r2:])

cycle_rank = len(T)-r2
H = [[d3cols[j][i] for j in range(len(Q))] for i in range(cycle_rank)]
r3,D3,_,P = reduce_units(H,track_p=True)
assert (cycle_rank,r3) == (140,136)
assert all(
    D3[i][j] == (1 if i == j and i < r3 else 0)
    for i in range(len(D3)) for j in range(len(D3[0]))
)
# Therefore H2 is torsion-free of rank four.

def h2coords(x):
    y = matvec(Qinv,x)
    assert all(v == 0 for v in y[:r2])
    z = matvec(P,y[r2:])
    return tuple(z[r3:])

def tetra_boundary(S):
    a,b,c,d = S
    x = [0]*len(T)
    for t,s in [((b,c,d),1),((a,c,d),-1),((a,b,d),1),((a,b,c),-1)]:
        x[TI[t]] = s
    return x

def canon(v):
    for x in v:
        if x < 0:
            return tuple(-z for z in v)
        if x > 0:
            return tuple(v)
    return tuple(v)

TSET = set(T)
QSET = set(Q)
carriers = []
for S in combinations(V,4):
    tris = list(combinations(S,3))
    if not all(t in TSET for t in tris):
        continue
    co = h2coords(tetra_boundary(S))
    if S in QSET:
        assert co == (0,0,0,0)
    else:
        carriers.append((S,co))

assert len(carriers) == 153
assert all(c != (0,0,0,0) for _,c in carriers)
assert all(gcd(gcd(abs(c[0]),abs(c[1])),gcd(abs(c[2]),abs(c[3]))) == 1
           for _,c in carriers)

integral_counts = Counter(canon(c) for _,c in carriers)
assert len(integral_counts) == 12
assert sorted(integral_counts.values()) == [3,3,3] + [16]*9

# Fix a displayed integral basis by four actual minimum carriers.
representatives = {}
for S,c in carriers:
    representatives.setdefault(canon(c),S)
assert representatives[(1,0,0,0)] == (1,7,11,12)
assert representatives[(0,1,0,0)] == (1,2,3,9)
assert representatives[(0,0,1,0)] == (1,2,3,8)
assert representatives[(0,0,0,1)] == (1,4,7,9)

mod2_counts = Counter(tuple(x % 2 for x in c) for _,c in carriers)
assert len(mod2_counts) == 12
assert sorted(mod2_counts.values()) == [3,3,3] + [16]*9

ZERO = (0,0,0,0)
def add2(a,b):
    return tuple(x^y for x,y in zip(a,b))
def span2(gens):
    out = {ZERO}
    for g in gens:
        out |= {add2(x,g) for x in tuple(out)}
    return out

# With e1,e2,e3,e4 the basis above:
# U=<e2+e3,e2+e4>, W=<e2+e3+e4,e1+e3>.
U = span2([(0,1,1,0),(0,1,0,1)])
W = span2([(0,1,1,1),(1,0,1,0)])
assert len(U) == len(W) == 4 and U.intersection(W) == {ZERO}
for u in U-{ZERO}:
    assert mod2_counts[u] == 3
for w in W-{ZERO}:
    assert mod2_counts[w] == 0
for u in U-{ZERO}:
    for w in W-{ZERO}:
        assert mod2_counts[add2(u,w)] == 16

# Each represented mod-two class has exactly one integral sign-class
# among the minimum carriers.
lift_sets = {}
for c in integral_counts:
    lift_sets.setdefault(tuple(x%2 for x in c),set()).add(c)
assert set(lift_sets) == set(mod2_counts)
assert all(len(s) == 1 for s in lift_sets.values())

print(
    "VERIFY_OK f=12,63,192,225,90 H2_Z=Z^4 "
    "min_vertex_support=4 carriers4=153 all_primitive=yes "
    "integral_classes_up_to_sign=12 integral_multiplicities=16x9+3x3 "
    "mod2_carried_classes=12 mod2_missing_classes=3 "
    "planes=U+W_direct_sum=yes "
    "multiplicity_rule=U_nonzero:3|W_nonzero:0|mixed:16"
)
