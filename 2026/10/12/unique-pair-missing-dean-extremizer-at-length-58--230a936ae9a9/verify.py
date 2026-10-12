#!/usr/bin/env python3
import itertools
import json
from pathlib import Path

ALPH = "0123"
INV = {"0":"2","2":"0","1":"3","3":"1"}
FORBIDDEN = "10"

def suffix_square(w):
    n = len(w)
    for h in range(1, n//2+1):
        if w[n-2*h:n-h] == w[n-h:n]:
            return True
    return False

def incremental_levels():
    levels = [[""]]
    for _ in range(1,60):
        nxt = []
        for w in levels[-1]:
            for c in ALPH:
                if w and c == INV[w[-1]]:
                    continue
                q = w+c
                if q.endswith(FORBIDDEN):
                    continue
                if suffix_square(q):
                    continue
                nxt.append(q)
        levels.append(sorted(nxt))
    return levels

def direct_valid(w):
    if FORBIDDEN in w:
        return False
    for i in range(len(w)-1):
        if w[i+1] == INV[w[i]]:
            return False
    n = len(w)
    for i in range(n):
        for h in range(1,(n-i)//2+1):
            if w[i:i+h] == w[i+h:i+2*h]:
                return False
    return True

def direct_levels():
    levels = [[""]]
    for _ in range(1,60):
        nxt = []
        for w in levels[-1]:
            for c in ALPH:
                q = w+c
                if direct_valid(q):
                    nxt.append(q)
        levels.append(sorted(nxt))
    return levels

root = Path(__file__).resolve().parent
cert = json.loads((root/"certificate.json").read_text(encoding="utf-8"))

A = incremental_levels()
B = direct_levels()
expected = cert["fixed_pair_survivor_counts_by_length_0_to_59"]
assert [len(x) for x in A] == expected
assert [len(x) for x in B] == expected
assert A == B
assert len(A[58]) == 1
assert A[58][0] == cert["unique_length_58_fixed_pair_extremizer"]
assert A[59] == []
w = A[58][0]

possible = sorted(a+b for a in ALPH for b in ALPH if b != a and b != INV[a])
assert possible == cert["length_2_dean_factors"]
present = {w[i:i+2] for i in range(len(w)-1)}
assert sorted(set(possible)-present) == ["10"]

maps = []
for p in itertools.permutations(ALPH):
    mp = dict(zip(ALPH,p))
    if all(mp[INV[a]] == INV[mp[a]] for a in ALPH):
        maps.append(mp)
assert len(maps) == 8
assert sorted({mp["1"]+mp["0"] for mp in maps}) == possible

images = sorted({w.translate(str.maketrans(mp)) for mp in maps})
assert images == cert["global_length_58_pair_missing_extremizers"]
assert len(images) == 8
def is_dean_direct(q):
    for i in range(len(q)-1):
        if q[i+1] == INV[q[i]]:
            return False
    n = len(q)
    for i in range(n):
        for h in range(1,(n-i)//2+1):
            if q[i:i+h] == q[i+h:i+2*h]:
                return False
    return True

for q in images:
    assert is_dean_direct(q)
    missing = sorted(set(possible)-{q[i:i+2] for i in range(len(q)-1)})
    assert len(missing) == 1

# Symmetry argument: any length-58 Dean word missing any possible pair can be
# relabeled to a length-58 Dean word missing 10, which is unique.
print(
    "VERIFY_OK fixed_pair=10 max=58 fixed_count58=1 fixed_count59=0 "
    "global_pair_missing_count58=8 symmetry_group=8 missing_each=1 counts="
    + ",".join(str(x) for x in expected)
)
