"""Exhaustive check: no uniform (S_N x Z)-invariant graph on N x Z satisfies the 2-2 witness.

Model: vertices (i,m). Invariance under S_N (permute i) + Z (shift m) forces
adjacency of distinct vertices ((i,m),(j,n)) to depend only on (1_{i=j}, n-m).
Variables: S_inter, S_intra subsets of differences {-2..2} (window check).
Witness family: U={(0,0),(1,0)}, V={(2,0),(3,0)}; candidate witnesses
(k,w), k in {0,1,2,3,4(new)}, w in {0,1,2}.
Result: 0/1024 patterns admit a witness. The proof generalizes to all of Z
(see DRAFT.md): a new-orbit witness sees all four points equally; an old-orbit
witness sees the three cross-fiber points equally.
"""
import itertools

diffs = [-2, -1, 0, 1, 2]
U = {(0, 0), (1, 0)}
V = {(2, 0), (3, 0)}
ORBITS = [0, 1, 2, 3]
NEW = 4
POS = [0, 1, 2]


def witness_exists(S_inter, S_intra):
    for k in ORBITS + [NEW]:
        for w in POS:
            ok = True
            for (i, v) in U:
                d = w - v
                adj = (d in S_intra) if (k == i and d != 0) else ((d in S_inter) if k != i else False)
                if k == i and d == 0:
                    adj = False
                if not adj:
                    ok = False
                    break
            if not ok:
                continue
            for (i, v) in V:
                d = w - v
                adj = (d in S_intra) if (k == i and d != 0) else ((d in S_inter) if k != i else False)
                if k == i and d == 0:
                    adj = False
                if adj:
                    ok = False
                    break
            if ok:
                return True
    return False


success = 0
total = 0
for mask1 in range(32):
    S_inter = {d for j, d in enumerate(diffs) if (mask1 >> j) & 1}
    for mask2 in range(32):
        S_intra = {d for j, d in enumerate(diffs) if (mask2 >> j) & 1}
        total += 1
        if witness_exists(S_inter, S_intra):
            success += 1
print(f"uniform patterns with witness: {success}/{total}")
assert success == 0
print("OBSTRUCTION CONFIRMED: uniform 2-2 witness impossible.")
