#!/usr/bin/env python3
"""Independent replay: recompute orbits from scratch (pow-iteration path),
decide each of the 325 unions by TRANSLATION INTERSECTION numbers
|S cap (S+g)| == 1 for all g != 0 (set-operation code path, not differences),
and cross-check byte-identical survivor list + per-set stats vs census.json.
Exit 0 iff everything matches. Stdlib only."""
import json, os, sys, itertools

HERE = os.path.dirname(os.path.abspath(__file__))
V = 157
T = 13

# independent orbit build: iterate x -> 13x with pow, canonical min representative
orbits = {}
for a in range(V):
    if a not in orbits:
        o = set()
        y = a
        while y not in o:
            o.add(y)
            y = (y * T) % V
        rep = min(o)
        for z in o:
            orbits[z] = rep
groups = {}
for z, r in orbits.items():
    groups.setdefault(r, []).append(z)
assert len(groups) == 27, len(groups)
assert sorted(len(v) for v in groups.values()) == [1] + [6] * 26
sext_reps = sorted(r for r, v in groups.items() if len(v) == 6)
assert len(sext_reps) == 26
sext = [sorted(groups[r]) for r in sext_reps]

# cross-check orbit definitions vs primary
prim = json.load(open(os.path.join(HERE, "orbits.json")))
assert prim["representatives"] == sext_reps, "orbit representative mismatch"
assert prim["sextuple_orbits"] == sext, "orbit content mismatch"

census = json.load(open(os.path.join(HERE, "census.json")))
n_surv = 0
survivors = []
mismatch = 0
for idx, (i, j) in enumerate(itertools.combinations(range(26), 2)):
    S = set([0] + sext[i] + sext[j])
    assert len(S) == 13
    # intersection numbers with all nontrivial translates
    bad = 0
    minter = 99
    maxter = -1
    for g in range(1, V):
        Sg = {(x + g) % V for x in S}
        t = len(S & Sg)
        minter = min(minter, t)
        maxter = max(maxter, t)
        if t != 1:
            bad += 1
    is_ds = (bad == 0)
    if is_ds:
        n_surv += 1
        survivors.append([i, j])
    rec = census["results"][idx]
    assert rec["pair"] == [i, j]
    # cross-check: missing residues == #translates with intersection 0? No:
    # difference value d has multiplicity |S cap (S+d)|. So max_mult==maxter,
    # and (#d with mult 0) == (#g with intersection 0). Check consistency:
    if rec["max_mult"] != maxter:
        print("MAX MISMATCH", i, j, rec["max_mult"], maxter)
        mismatch += 1
    n0_replay = sum(1 for g in range(1, V)
                    if len(S & {(x + g) % V for x in S}) == 0)
    if rec["missing"] != n0_replay:
        print("MISSING MISMATCH", i, j, rec["missing"], n0_replay)
        mismatch += 1
    if rec["is_ds"] != is_ds:
        print("VERDICT MISMATCH", i, j)
        mismatch += 1

assert census["n_survivors"] == n_surv, (census["n_survivors"], n_surv)
assert census["survivors"] == survivors, "survivor list mismatch"

with open(os.path.join(HERE, "REPLAY_SURVIVORS.txt"), "w") as f:
    f.write("survivors=%d\n" % len(survivors))
    for p in survivors:
        f.write("%s\n" % (p,))

a = open(os.path.join(HERE, "SURVIVORS.txt"), "rb").read()
b = open(os.path.join(HERE, "REPLAY_SURVIVORS.txt"), "rb").read()
assert a == b, "survivor files not byte-identical"

print("REPLAY_OK: 325 sets re-decided via intersection numbers,",
      "survivors=%d, mismatches=%d, survivor files byte-identical" % (n_surv, mismatch))
sys.exit(1 if mismatch else 0)
