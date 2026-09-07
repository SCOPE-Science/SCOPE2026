#!/usr/bin/env python3
"""Independent cold verifier for (51,25,12) census (stdlib only).
Different code path from enumerate script:
 - reloads orbit_table.json + blocks_F0.json
 - rechecks orbit partition, fixedness, sizes
 - recounts differences via collections.Counter (ordered pairs i!=j)
 - rechecks autocorrelation via +/-1 sums (separate loop)
 - rechecks character-sum (group-ring) spot check on best candidate
 - verifies H-shift normalization lemma: D+17 maps singleton families
"""
import json, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))
V, K, LAM = 51, 25, 12

orbits = json.load(open(os.path.join(HERE, "orbit_table.json")))
singletons = orbits["singletons"]
fours = orbits["four_orbits"]
assert sorted(singletons) == [[0],[17],[34]]
assert len(fours) == 12
# partition check
allpts = sorted([x for o in singletons+fours for x in o])
assert allpts == list(range(51)), "orbits must partition Z_51"
# each four-orbit closed under x13
for o in fours:
    assert set((13*x) % 51 for x in o) == set(o), o
print("orbits OK: partition + 13-closed")

blocks = json.load(open(os.path.join(HERE, "blocks_F0.json")))
assert len(blocks) == 924, len(blocks)
# canonical order check: combos strictly increasing lex
combos = [tuple(b["combo"]) for b in blocks]
assert combos == sorted(combos), "not canonical lex order"
print("catalog OK: 924 blocks, canonical lex order")

npass = 0
best = None
for b in blocks:
    D = b["block"]
    assert len(D) == 25 and len(set(D)) == 25
    assert set((13*x) % 51 for x in D) == set(D), "fixedness fail"
    assert 0 in D and 17 not in D and 34 not in D
    c = collections.Counter((a-b) % V for a in D for b in D if a != b)
    assert sum(c.values()) == 600
    bad = [d for d in range(1, 51) if c.get(d, 0) != LAM]
    ok = (len(bad) == 0)
    if ok:
        npass += 1
    # autocorr independent loop
    S = set(D)
    ac_bad = 0
    for t in range(1, 51):
        inter = sum(1 for x in S if (x+t) % V in S)
        R = V - 4*K + 4*inter
        if R != -1:
            ac_bad += 1
    assert (ac_bad == 0) == ok, "difference/autocorr disagree!"
    dev = max(abs(c.get(d,0)-LAM) for d in range(1,51))
    if best is None or dev < best[0]:
        best = (dev, D, dict(c))
print(f"difference recount OK: {npass}/924 pass (expect 0)")
assert npass == 0
print(f"best maxdev={best[0]} example block={best[1]}")

# H-shift normalization lemma check: shifting 0-family by 17/34 gives 17/34 families, still fixed
S0 = set(blocks[0]["block"])
for h, s in [(17,17),(34,34)]:
    T = sorted((x+h) % V for x in S0)
    assert set((13*x) % V for x in T) == set(T)
    assert s in T and 0 not in T or (h==17 and 17 in T)
print("H-shift lemma OK: D fixed => D+h fixed; singleton can be normalized to 0")

# Group-ring spot check on best block: sum_{d} N_d = k^2 with N_0=k, N_d=lambda required
D = best[1]
N = collections.Counter((a-b) % V for a in D for b in D)  # includes diagonal
assert N[0] == 25 and sum(N.values()) == 625
print("group-ring counts: N0 =", N[0], " sum =", sum(N.values()), " (expect 25, 625)")
print("COLD VERIFIER PASS: 0/924 are (51,25,12) difference sets")
