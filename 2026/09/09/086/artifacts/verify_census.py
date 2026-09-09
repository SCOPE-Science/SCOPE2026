#!/usr/bin/env python3
"""Independent stdlib verifier for the n=6 single-C5^3-free census (no numpy).

Loads output/artifacts/census_types.json (or census_types.json in cwd) and:
 (V1) each representative is C5^3-free (independent brute-force definitions:
      own triple list, own injection list, 5 distinct consecutive-triple edges);
 (V2) each representative's stored canon equals the recomputed min-code over
      all 720 perms AND the stored edge count matches (canonicity check);
 (V3) pairwise non-isomorphism: all stored canons distinct AND each rep's
      full 720-orbit has min == stored canon (orbit-consistency), plus
      cross-check that no two reps share an orbit element (hash all 720 codes
      of each rep into a set; sets disjoint);
 (V4) coverage: sum of 720/stabilizer over reps... INDEPENDENT orbit-size
      computation: for each rep, stabilizer = #{p : p(rep)==rep} by direct
      edge-set comparison, orbit = 720/stab; sum orbits == 371229 and
      sum-orbits-per-edge-count == stored edge distribution; ALSO global
      coverage: coverage == 2^20 is verified by re-enumerating all 2^20 masks?
      That is the generator's claim; the verifier independently rechecks the
      C5-test on a deterministic pseudorandom sample + ALL reps' orbits...
      NO — full coverage needs full re-enumeration. Do it: 2^20 masks x 720
      injections in pure stdlib ~ minutes. With early-exit + edge-count prefilter
      (need >=5 edges; skip popcount<5 via bin(x).count) it runs ~2-5 min.
      Compares total free count vs stored 371229 and per-edge distribution.
Exits VERIFY_OK iff all pass.
"""
import itertools
import json
import os
import sys
import time

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "census_types.json")
if not os.path.exists(P):
    P = "census_types.json"
d = json.load(open(P))
TRIPLES = list(itertools.combinations(range(6), 3))
TIDX = {t: i for i, t in enumerate(TRIPLES)}
PERMS = list(itertools.permutations(range(6)))
INJS = list(itertools.permutations(range(6), 5))
assert len(PERMS) == 720 and len(INJS) == 720
# C5 edge-sets per injection (frozenset of triple indices; assert size 5)
C5 = []
for v in INJS:
    es = frozenset(
        TIDX[tuple(sorted((v[k], v[(k + 1) % 5], v[(k + 2) % 5])))]
        for k in range(5))
    assert len(es) == 5, v
    C5.append(es)


def edges_of(rep):
    return frozenset(TIDX[tuple(sorted(e))] for e in rep)


def has_c5(eset):
    for c in C5:
        if c <= eset:
            return True
    return False


def img_of(eset, q):
    out = set()
    for i in eset:
        a, b, c = TRIPLES[i]
        out.add(TIDX[tuple(sorted((q[a], q[b], q[c])))])
    return frozenset(out)


def code_of(eset):
    return sum(1 << i for i in eset)


types = d["types"]
print("loaded %d types" % len(types))

# V1: freeness + edge count
for t in types:
    es = edges_of(t["rep"])
    assert not has_c5(es), t["canon"]
    assert len(es) == t["edges_n"], t["canon"]
print("PASS V1: all %d representatives C5^3-free, edge counts match" % len(types))

# V2: canonicity (min-code over 720 perms == stored canon)
for t in types:
    es = edges_of(t["rep"])
    mc = min(code_of(img_of(es, q)) for q in PERMS)
    assert mc == t["canon"], (t["canon"], mc)
print("PASS V2: all stored canons are the true min-codes")

# V3: disjoint orbits (no two reps isomorphic).
# (Within one rep, the 720 images need not be distinct — stabilizers exist —
# so track per-rep code SETS and require the sets to be pairwise disjoint.)
seen = {}
for t in types:
    es = edges_of(t["rep"])
    my = set()
    for q in PERMS:
        c = code_of(img_of(es, q))
        assert c not in seen, (t["canon"], seen.get(c))
        my.add(c)
    for c in my:
        seen[c] = t["canon"]
    # orbit-stabilizer spot check here too: |orbit| * |stab| == 720
    stab = sum(1 for q in PERMS if img_of(es, q) == es)
    assert len(my) * stab == 720, t["canon"]
print("PASS V3: %d distinct labeled graphs across orbits, pairwise disjoint "
      "(reps pairwise non-isomorphic)" % len(seen))

# V4a: orbit sizes via stabilizers; sum == labeled total; per-edge dist
tot = 0
per_edge = [0] * 21
for t in types:
    es = edges_of(t["rep"])
    stab = sum(1 for q in PERMS if img_of(es, q) == es)
    assert 720 % stab == 0
    orb = 720 // stab
    assert orb == t["count"], (t["canon"], orb, t["count"])
    tot += orb
    per_edge[t["edges_n"]] += orb
assert tot == d["n_labeled_free"] == 371229, tot
assert per_edge == d["edge_dist_free"], per_edge
print("PASS V4a: stabilizer orbit sizes match stored counts; "
      "sum=%d; per-edge distribution matches" % tot)

# V4b: FULL independent re-enumeration coverage == 2^20
t0 = time.time()
free = 0
cnt = [0] * 21
for m in range(1 << 20):
    pc = bin(m).count("1")
    if pc < 5:
        cnt[pc] += 1  # C5 needs 5 edges: all such graphs are C5-free
        free += 1
        continue
    es = frozenset(i for i in range(20) if (m >> i) & 1)
    bad = False
    for c in C5:
        if c <= es:
            bad = True
            break
    if not bad:
        free += 1
        cnt[pc] += 1
    if m and m % 200000 == 0:
        print("  re-enumeration %d/1048576 free=%d %.1fs"
              % (m, free, time.time() - t0), flush=True)
assert free == 371229 == tot, (free, tot)
assert cnt == per_edge, [x for x in zip(cnt, per_edge) if x[0] != x[1]]
print("PASS V4b: independent full re-enumeration: %d C5-free of 1048576 "
      "(coverage exact), edge distribution identical" % free)
print("VERIFY_OK")
