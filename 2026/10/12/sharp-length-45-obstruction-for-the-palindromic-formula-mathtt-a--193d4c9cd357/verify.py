#!/usr/bin/env python3
import json
import itertools
from collections import defaultdict
from pathlib import Path

ALPHABET = "012"

def has_square_suffix(w):
    n = len(w)
    for h in range(1, n // 2 + 1):
        if w[n-2*h:n-h] == w[n-h:n]:
            return True
    return False

def contains_square_direct(w):
    n = len(w)
    for i in range(n):
        for h in range(1, (n-i)//2 + 1):
            if w[i:i+h] == w[i+h:i+2*h]:
                return True
    return False

pairs = []
suffix_map = defaultdict(set)
for A in ALPHABET:
    for lb in range(1, 5):
        for lc in range(1, 5):
            if lb + lc > 5:
                continue
            for Bt in itertools.product(ALPHABET, repeat=lb):
                B = "".join(Bt)
                for Ct in itertools.product(ALPHABET, repeat=lc):
                    C = "".join(Ct)
                    x = A + B + C + A
                    y = A + C + B + A
                    pairs.append((x, y))
                    suffix_map[x].add(y)
                    suffix_map[y].add(x)

assert len(pairs) == 3834
assert set(map(len, suffix_map)) == {4,5,6,7}

def creates_restricted_formula_suffix(w):
    for L in (4,5,6,7):
        if L > len(w):
            continue
        s = w[-L:]
        for other in suffix_map.get(s, ()):
            if other in w:
                return True
    return False

def direct_valid(w):
    if contains_square_direct(w):
        return False
    for x, y in pairs:
        if x in w and y in w:
            return False
    return True

def engine_suffix():
    levels = [[""]]
    for _ in range(1,47):
        nxt = []
        for w in levels[-1]:
            for c in ALPHABET:
                q = w + c
                if has_square_suffix(q):
                    continue
                if creates_restricted_formula_suffix(q):
                    continue
                nxt.append(q)
        levels.append(sorted(nxt))
    return levels

def engine_direct():
    levels = [[""]]
    for _ in range(1,47):
        nxt = []
        for w in levels[-1]:
            for c in ALPHABET:
                q = w + c
                if direct_valid(q):
                    nxt.append(q)
        levels.append(sorted(nxt))
    return levels

root = Path(__file__).resolve().parent
cert = json.loads((root / "certificate.json").read_text(encoding="utf-8"))
A = engine_suffix()
B = engine_direct()
expected_counts = cert["survivor_counts_by_length_0_to_46"]
assert [len(x) for x in A] == expected_counts
assert [len(x) for x in B] == expected_counts
assert A == B
assert A[45] == sorted(cert["length_45_extremizers"])
assert len(A[45]) == 18
assert A[46] == []
assert all(direct_valid(w) for w in A[45])

perms = [str.maketrans(dict(zip(ALPHABET,p))) for p in itertools.permutations(ALPHABET)]
def orbit(w):
    out = set()
    for tr in perms:
        q = w.translate(tr)
        out.add(q)
        out.add(q[::-1])
    return out

remaining = set(A[45])
computed = []
while remaining:
    w = min(remaining)
    o = sorted(orbit(w) & set(A[45]))
    computed.append(o)
    remaining -= set(o)
computed = sorted(computed)
assert computed == sorted(sorted(o) for o in cert["symmetry_orbits"])
assert sorted(len(o) for o in computed) == [6,12]

print(
    "VERIFY_OK max=45 count45=18 count46=0 engines=2 assignments=3834 "
    "orbits=2 orbit_sizes=6,12 counts=" + ",".join(str(x) for x in expected_counts)
)
