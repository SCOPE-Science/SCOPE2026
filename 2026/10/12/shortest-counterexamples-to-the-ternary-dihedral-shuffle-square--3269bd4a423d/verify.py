#!/usr/bin/env python3
import itertools, json
from collections import Counter
from pathlib import Path

ALPHABET = "012"

def dihedral_orbit(s):
    n = len(s)
    out = set()
    for t in (s, s[::-1]):
        for r in range(n):
            out.add(t[r:] + t[:r])
    return out

def is_dihedral_shuffle(w):
    n = len(w) // 2
    positions = tuple(range(len(w)))
    for chosen in itertools.combinations(positions, n):
        A = set(chosen)
        u = "".join(w[i] for i in positions if i in A)
        v = "".join(w[i] for i in positions if i not in A)
        if v in dihedral_orbit(u):
            return True
    return False

def even_words(N):
    for tup in itertools.product(ALPHABET, repeat=N):
        w = "".join(tup)
        c = Counter(w)
        if all(c[a] % 2 == 0 for a in ALPHABET):
            yield w

def symmetry_orbit(w):
    out = set()
    for p in itertools.permutations(ALPHABET):
        mp = dict(zip(ALPHABET, p))
        v = "".join(mp[c] for c in w)
        out.add(v)
        out.add(v[::-1])
    return out

root = Path(__file__).resolve().parent
cert = json.loads((root / "certificate.json").read_text(encoding="utf-8"))

stats = {}
bad8 = []
for N in (2, 4, 6, 8):
    ew = list(even_words(N))
    bad = [w for w in ew if not is_dihedral_shuffle(w)]
    stats[N] = (len(ew), len(bad))
    if N == 8:
        bad8 = bad

assert stats == {2:(3,0), 4:(21,0), 6:(183,0), 8:(1641,48)}
assert bad8 == cert["bad_words"]

unseen = set(bad8)
classes = []
while unseen:
    rep = min(unseen)
    cls = sorted(unseen & symmetry_orbit(rep))
    classes.append((rep, cls))
    unseen -= set(cls)

expected_reps = ["00011022","00110220","00111221","01112210"]
assert [r for r,_ in classes] == expected_reps
assert [len(c) for _,c in classes] == [12,12,12,12]
assert [{"representative":r,"members":c} for r,c in classes] == cert["symmetry_classes"]

w = "00011022"
balanced_oriented = []
pairs = set()
positions = tuple(range(8))
for chosen in itertools.combinations(positions, 4):
    A = set(chosen)
    u = "".join(w[i] for i in positions if i in A)
    v = "".join(w[i] for i in positions if i not in A)
    if sorted(u) == sorted(v):
        balanced_oriented.append((u,v))
        pairs.add(tuple(sorted((u,v))))

assert len(balanced_oriented) == 24
assert pairs == {("0012","0102")}
orbit = dihedral_orbit("0012")
assert orbit == {"0012","0120","1200","2001","2100","1002","0021","0210"}
assert "0102" not in orbit
assert not is_dihedral_shuffle(w)

print(
    "VERIFY_OK "
    "even_counts=2:3,4:21,6:183,8:1641 "
    "bad_counts=2:0,4:0,6:0,8:48 "
    "classes8=00011022:12,00110220:12,00111221:12,01112210:12 "
    "witness_pair=0012|0102"
)
