#!/usr/bin/env python3
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "collapse_cert.json"
V = tuple(range(9))

def permutation(cycles):
    p = list(range(9))
    for cyc1 in cycles:
        cyc = [x - 1 for x in cyc1]
        for i, x in enumerate(cyc):
            p[x] = cyc[(i + 1) % len(cyc)]
    return tuple(p)

def compose(p, q):
    return tuple(p[q[i]] for i in range(9))

def mask(s):
    return sum(1 << i for i in s)

def from_mask(m):
    return frozenset(i for i in V if (m >> i) & 1)

a = permutation([(1, 4, 7), (2, 5, 8), (3, 6, 9)])
b = permutation([(1, 2, 3), (4, 6, 5)])
g = permutation([(1, 2), (4, 5), (7, 8)])
identity = tuple(range(9))
group = {identity}
frontier = [identity]
for x in frontier:
    for y in (a, b, g):
        z = compose(y, x)
        if z not in group:
            group.add(z)
            frontier.append(z)
assert len(group) == 54

facets = set()
for seed in ({0, 1, 3, 4, 5}, {0, 1, 3, 4, 8}):
    for p in group:
        facets.add(frozenset(p[i] for i in seed))
assert len(facets) == 36

faces = set()
face_by_dim = {d: set() for d in range(5)}
for F in facets:
    for r in range(1, 6):
        for q in combinations(F, r):
            f = frozenset(q)
            faces.add(f)
            face_by_dim[r - 1].add(f)
assert tuple(len(face_by_dim[d]) for d in range(5)) == (9, 36, 84, 90, 36)

# Complementarity on every nontrivial bipartition of the nine vertices.
full = frozenset(V)
for r in range(1, 9):
    for S0 in combinations(V, r):
        S = frozenset(S0)
        T = full - S
        assert (S in faces) != (T in faces)

with CERT.open("r", encoding="utf-8") as f:
    cert = json.load(f)
assert cert == json.loads(CERT.read_text(encoding="utf-8"))
assert cert["schema_version"] == 1 and cert["vertices"] == 9
entries = cert["entries"]

def induced_faces(S):
    return {f for f in faces if f <= S}

def maximal_faces(FS):
    return [f for f in FS if not any(f < h for h in FS)]

def tetrahedral_boundary_support(FS):
    fac = maximal_faces(FS)
    U = set().union(*fac) if fac else set()
    if len(U) != 4 or len(fac) != 4 or any(len(f) != 3 for f in fac):
        return None
    expected = {frozenset(U - {u}) for u in U}
    return frozenset(U) if set(fac) == expected else None

proper_faces = Counter()
nonfaces = Counter()
lengths = Counter()
seen_nonfaces = set()
for r in range(1, 9):
    for S0 in combinations(V, r):
        S = frozenset(S0)
        if S in faces:
            proper_faces[r] += 1
            # If S is a simplex, its induced complex is exactly the full simplex on S.
            expected = {frozenset(q) for k in range(1, r + 1) for q in combinations(S, k)}
            assert induced_faces(S) == expected
            continue

        nonfaces[r] += 1
        key = str(mask(S))
        assert key in entries
        seen_nonfaces.add(key)
        row = entries[key]
        assert row["subset"] == [i + 1 for i in sorted(S)]
        FS = induced_faces(S)
        initial_face_count = len(FS)
        pairs = row["pairs"]
        for tau_m, sig_m in pairs:
            tau, sig = from_mask(tau_m), from_mask(sig_m)
            assert tau in FS and sig in FS
            assert tau < sig and len(sig) == len(tau) + 1
            fac = maximal_faces(FS)
            assert sig in fac
            containing = [h for h in fac if tau <= h]
            assert containing == [sig]
            FS.remove(tau)
            FS.remove(sig)
        target = tetrahedral_boundary_support(FS)
        assert target is not None
        assert [i + 1 for i in sorted(target)] == row["target"]
        assert len(FS) == 14
        assert 2 * len(pairs) == initial_face_count - 14
        lengths[(r, len(pairs))] += 1

assert seen_nonfaces == set(entries)
assert sum(proper_faces.values()) == 255
assert sum(nonfaces.values()) == 255
assert dict(nonfaces) == {4: 36, 5: 90, 6: 84, 7: 36, 8: 9}
assert lengths == Counter({(4, 0): 36, (5, 7): 90, (6, 18): 9,
                           (6, 19): 27, (6, 20): 27, (6, 21): 21,
                           (7, 40): 36, (8, 72): 9})

print("VERIFY_OK facets=36 face_vector=9,36,84,90,36 proper_faces=255 proper_nonfaces=255 "
      "nonfaces=4:36,5:90,6:84,7:36,8:9 "
      "collapse_lengths=4:0x36;5:7x90;6:18x9,19x27,20x27,21x21;7:40x36;8:72x9")
