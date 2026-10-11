#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

RAW = """
123456c 123456d 12345ab 12345ac 12345bd 12346cd 123479a 123479d
12347ad 12348ab 12348ad 12348bd 12349ac 12349cd 12356bc 12356bd
1235abc 1236bcd 12379ad 12389ab 12389ad 12389bd 1239abc 1239bcd
1245678 124567b 1245689 124569a 12456ac 12456bd 1245789 124579a
12457ab 124678b 124689b 12469ac 12469bd 12469cd 124789d 12478ab
12478ad 12489bd 125678c 12567bc 125689a 12568ac 125789a 12578ac
1257abc 12678ab 12678ac 1267abc 12689ab 1269abc 1269bcd 12789ad
1345679 134567d 134569a 13456ac 134579a 13457ad 1345abd 134679c
13467cd 13469ac 13479cd 1348abd 1356789 135678c 13567bc 13567bd
135689a 13568ac 135789c 13579ad 13579bc 13579bd 13589ad 13589bc
13589bd 1358abc 1358abd 136789c 1367bcd 13689ac 1379bcd 1389abc
1456789 14567bd 1457abd 146789c 14678bd 14678cd 14689bc 1468bcd
1469bcd 14789cd 1478abd 1489bcd 15789ad 15789cd 1578acd 1579bcd
157abcd 1589bcd 158abcd 1678abd 1678acd 167abcd 1689abc 168abcd
23456cd 23458bc 23458bd 23458cd 2345abc 23478ab 23478ad 23478bc
23478cd 23479ac 23479cd 2347abc 235678b 235678c 23567bc 235689b
235689d 23568cd 23569bd 23578bc 23589bd 23678ab 23678ad 23678cd
23679ab 23679ad 23679bd 2367bcd 23689ab 23689ad 2379abc 2379bcd
245678b 245689b 24569ac 24569bd 24569cd 245789c 24578bc 24579ac
2457abc 24589bd 24589cd 24789cd 25689ad 2568acd 2569acd 25789ad
25789cd 2578acd 2579acd 2678acd 2679abd 267abcd 269abcd 279abcd
345679a 34567ad 3456acd 3458abc 3458abd 3458acd 346789b 346789c
34678ab 34678ad 34678cd 34679ab 34689ab 34689ac 3468acd 34789bc
3479abc 3489abc 356789b 35679ad 35679bd 35689ad 3568acd 35789bc
456789b 45679ab 4567abd 4569abd 4569acd 45789bc 4579abc 4589bcd
458abcd 459abcd 4678abd 4689abc 468abcd 469abcd 5679abd 579abcd
""".split()

lab = {str(i): i for i in range(1, 10)}
lab.update({"a": 10, "b": 11, "c": 12, "d": 13})
FACETS = {tuple(sorted(lab[ch] for ch in s)) for s in RAW}
V = tuple(range(1, 14))

def faces(k):
    return sorted({tuple(sorted(c)) for f in FACETS for c in combinations(f, k)})

E = faces(2)
T = faces(3)
Q = faces(4)
P = faces(5)
R = faces(6)

assert (len(V), len(E), len(T), len(Q), len(P), len(R), len(FACETS)) == (
    13, 78, 286, 715, 1014, 728, 208
)
assert set(Q) == set(combinations(V, 4))

Ti = {t: i for i, t in enumerate(T)}
Qi = {q: i for i, q in enumerate(Q)}

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

# Boundary map C_3 -> C_2.
d3 = []
for q in Q:
    x = 0
    for t in combinations(q, 3):
        x ^= 1 << Ti[t]
    d3.append(x)
B3 = rref_basis(d3)

# Boundary map C_4 -> C_3.
d4 = []
for p in P:
    x = 0
    for q in combinations(p, 4):
        x ^= 1 << Qi[q]
    d4.append(x)
B4 = rref_basis(d4)

assert (len(B3), len(B4), len(Q) - len(B3) - len(B4)) == (220, 493, 2)

all5 = set(combinations(V, 5))
missing5 = sorted(all5 - set(P))
assert len(missing5) == 273

def sphere_chain(s):
    x = 0
    for q in combinations(s, 4):
        x ^= 1 << Qi[q]
    return x

# Verify each five-set boundary is a 3-cycle.
def boundary3(chain):
    out = 0
    for i, q in enumerate(Q):
        if (chain >> i) & 1:
            for t in combinations(q, 3):
                out ^= 1 << Ti[t]
    return out

classes = {}
for s in missing5:
    z = sphere_chain(s)
    assert boundary3(z) == 0
    c = reduce_mod(z, B4)
    assert c != 0
    classes.setdefault(c, []).append(s)

assert len(classes) == 3
assert sorted(len(v) for v in classes.values()) == [91, 91, 91]

# Present five-sets are 4-simplices, so their boundaries vanish in H_3.
for p in P:
    assert reduce_mod(sphere_chain(p), B4) == 0

# Choose lexicographically first representatives for the three classes.
class_lists = sorted((lst[0], c, lst) for c, lst in classes.items())
reps = [x[0] for x in class_lists]
assert reps == [
    (1, 2, 3, 5, 7),
    (1, 2, 3, 5, 8),
    (1, 2, 3, 7, 8),
]
c1 = class_lists[0][1]
c2 = class_lists[1][1]
c3 = class_lists[2][1]
assert c1 ^ c2 == c3

# Every vertex is present in the same number of minimum supports.
vinc = {v: sum(v in s for s in missing5) for v in V}
assert set(vinc.values()) == {105}

print(
    "VERIFY_OK f=13,78,286,715,1014,728,208 "
    "H3_F2_dim=2 missing5=273 all_missing5_nonzero=yes "
    "class_counts=91,91,91 reps=12357|12358|12378 "
    "class_relation=alpha+beta=gamma carrier_vertex_degree=105"
)
