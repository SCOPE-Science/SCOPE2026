#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

RAW = """
12346a 12346b 123478 12347b 12348a 12357b 12357c 12359b
12359c 1236ab 12378c 1238ac 1239ab 1239ac 124678 12467b
124689 12469a 12489a 1257bc 1259bc 12678c 1267bc 12689c
1269ab 1269bc 1289ac 134678 13467b 13468a 13579b 13579c
13678c 1367bc 1368ac 136abc 1379ab 1379ac 137abc 145689
14568a 14569a 14589c 1458ac 1459ac 1489ac 15689b 1568ab
1569ab 1579ab 1579ac 157abc 1589bc 158abc 1689bc 168abc
23456a 23456c 23458a 23458b 2345bc 2346bc 23478b 235678
23567c 23568a 23578b 2359bc 23678c 2368ac 236abc 239abc
24567a 24567c 24578a 24578b 2457bc 246789 24679a 2467bc
24789a 25678a 26789a 2689ac 269abc 345679 34567c 345689
34568a 34579c 34589b 3459bc 346789 3467bc 34789b 3479bc
356789 35789b 379abc 45679a 4578ab 4579ac 457abc 4589bc
458abc 4789ab 479abc 489abc 56789a 5689ab 5789ab 689abc
""".split()

lab = {str(i): i for i in range(1, 10)}
lab.update({"a": 10, "b": 11, "c": 12})
FACETS = {tuple(sorted(lab[ch] for ch in s)) for s in RAW}
V = tuple(range(1, 13))

def faces(k):
    return {tuple(sorted(c)) for f in FACETS for c in combinations(f, k)}

E = sorted(faces(2))
T = sorted(faces(3))
Q = sorted(faces(4))
P = sorted(faces(5))
assert (len(V), len(E), len(T), len(Q), len(P), len(FACETS)) == (12, 66, 220, 390, 336, 112)
assert set(E) == set(combinations(V, 2))
assert set(T) == set(combinations(V, 3))

Ei = {e: i for i, e in enumerate(E)}
Ti = {t: i for i, t in enumerate(T)}

def rref_basis(rows):
    B = {}
    for x in rows:
        y = x
        for p in sorted(B, reverse=True):
            if (y >> p) & 1:
                y ^= B[p]
        if not y:
            continue
        p = y.bit_length() - 1
        for q in list(B):
            if (B[q] >> p) & 1:
                B[q] ^= y
        B[p] = y
    return dict(sorted(B.items(), reverse=True))

def reduce_mod(x, B):
    y = x
    for p, row in B.items():
        if (y >> p) & 1:
            y ^= row
    return y

d2 = []
for t in T:
    x = 0
    for e in combinations(t, 2):
        x ^= 1 << Ei[e]
    d2.append(x)

d3 = []
for q in Q:
    x = 0
    for t in combinations(q, 3):
        x ^= 1 << Ti[t]
    d3.append(x)

B2 = rref_basis(d2)
B3 = rref_basis(d3)
assert (len(B2), len(B3), len(T) - len(B2) - len(B3)) == (55, 164, 1)

all4 = set(combinations(V, 4))
missing = sorted(all4 - set(Q))
assert len(missing) == 105

def tet_mod2(q):
    x = 0
    for t in combinations(q, 3):
        x ^= 1 << Ti[t]
    return reduce_mod(x, B3)

assert all(tet_mod2(q) == 0 for q in Q)
miss_classes = [tet_mod2(q) for q in missing]
assert all(x != 0 for x in miss_classes)
assert len(set(miss_classes)) == 1

WPOS = {
    (1,4,6),(1,4,7),(1,4,11),(1,5,6),(2,8,11),
    (3,6,9),(3,8,9),(3,8,11),(4,6,8),(4,6,9),
    (4,6,10),(4,7,8),(5,6,8),(5,6,9),(5,6,10),
    (5,6,11),(5,7,8),(7,8,9),(7,8,10),(7,8,11)
}
WNEG = {
    (1,2,4),(1,3,4),(2,4,8),(2,4,9),(2,4,10),
    (2,5,8),(2,5,10),(2,7,9),(2,7,10),(3,4,8),
    (3,4,10),(3,5,8),(3,5,10),(6,7,9),(6,7,10)
}

def w(t):
    t = tuple(sorted(t))
    return 1 if t in WPOS else (-1 if t in WNEG else 0)

def boundary_eval(q):
    q = tuple(sorted(q))
    return sum(((-1) ** i) * w(q[:i] + q[i+1:]) for i in range(4))

assert all(boundary_eval(q) == 0 for q in Q)
ev = Counter(boundary_eval(q) for q in missing)
assert ev == Counter({1: 57, -1: 48})

vinc = {v: sum(v in q for q in missing) for v in V}
assert set(vinc.values()) == {35}

print(
    "VERIFY_OK f=12,66,220,390,336,112 "
    "H2_F2_dim=1 missing4=105 all_missing4_mod2_nonzero=yes "
    "integral_cocycle_support=35 primitive_pairings=+1:57,-1:48 "
    "carrier_vertex_degree=35"
)
