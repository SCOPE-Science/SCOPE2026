"""Exhaustive STS(13) census with canonical prefix + iso classification (lane-300).

Prefix F (fixed wlog): six blocks through 0 with pairs
  {1,2},{3,4},{5,6},{7,8},{9,10},{11,12}, plus block {1,3,5}.
Lemma (uses only STS axioms): every STS(13) contains a labeled copy of F:
  pick any point p, take its 6 pencil blocks, pick any block B not through p
  (exists since 26>6); B meets 3 distinct pencil blocks, so (pencil,B) ~= F.
Hence every iso type appears among completions of F, and testing each
completion against representatives proves the type census.
"""
import sys, time, json
sys.path.insert(0, "artifacts")
from sts_lib import *
from dlxsolve import solve_all

V = 13
FIXED = [(0, 1, 2), (0, 3, 4), (0, 5, 6), (0, 7, 8), (0, 9, 10), (0, 11, 12),
         (1, 3, 5)]

covered = set()
for B in FIXED:
    a, b, c = B
    covered |= {(a, b), (a, c), (b, c)}

def pkey(x, y):
    return (x, y) if x < y else (y, x)

pairs = [pkey(x, y) for x in range(V) for y in range(x + 1, V)]
pidx = {p: i for i, p in enumerate(pairs)}
NCOLS = len(pairs)  # 78
uncovered_mask = 0
for p in pairs:
    if p not in covered:
        uncovered_mask |= 1 << pidx[p]

rows = []       # (mask, block)
for x in range(V):
    for y in range(x + 1, V):
        for z in range(y + 1, V):
            if pkey(x, y) in covered or pkey(x, z) in covered or pkey(y, z) in covered:
                continue
            m = (1 << pidx[pkey(x, y)]) | (1 << pidx[pkey(x, z)]) | (1 << pidx[pkey(y, z)])
            rows.append((m, (x, y, z)))
print("candidate rows:", len(rows), "uncovered pairs:", bin(uncovered_mask).count("1"),
      flush=True)

masks = [m for m, _ in rows]
blocks_of = [b for _, b in rows]

C13 = cyclic_sts(13, [(0, 1, 4), (0, 2, 7)])
reps = [("C13", C13)]
counts = {"C13": 0}
pasch_seen = {}
t0 = time.time()
nsol = [0]

def callback(chosen):
    sys_blocks = list(FIXED) + [blocks_of[i] for i in chosen]
    nsol[0] += 1
    # classify
    for name, R in reps:
        if find_iso(sys_blocks, R, V, limit=1):
            counts[name] += 1
            p = pasch_fast(sys_blocks, V)
            pasch_seen.setdefault(name, set()).add(p)
            return
    # new type?
    ok, msg = verify_sts(sys_blocks, V)
    assert ok, msg
    p = pasch_fast(sys_blocks, V)
    assert p == pasch_bruteforce(sys_blocks), "counter mismatch"
    name = "T%d" % (len(reps) + 1)
    reps.append((name, [tuple(sorted(b)) for b in sys_blocks]))
    counts[name] = 1
    pasch_seen.setdefault(name, set()).add(p)
    print("  NEW TYPE %s pasch=%d aut=%d" % (name, p, aut_order(sys_blocks, V)), flush=True)

# restrict columns to uncovered pairs only: remap to 0..56
cols = [i for i in range(NCOLS) if (uncovered_mask >> i) & 1]
remap = {c: k for k, c in enumerate(cols)}
masks2 = []
for m in masks:
    m2 = 0
    mm = m
    while mm:
        b = mm & (-mm)
        m2 |= 1 << remap[b.bit_length() - 1]
        mm ^= b
    masks2.append(m2)

n = solve_all(len(cols), masks2, callback)
dt = time.time() - t0
print("solutions:", n, "time: %.1fs" % dt)
print("types:", [(nm, counts[nm], sorted(pasch_seen[nm])) for nm, _ in reps])
for nm, R in reps:
    print(nm, "nblocks:", len(R), "pasch:", pasch_fast(R, V), pasch_bruteforce(R),
          "aut:", aut_order(R, V), "sha:", sha_of_system(R))
json.dump({"solutions": n, "time_s": dt,
           "types": [{"name": nm, "count": counts[nm],
                      "pasch": pasch_fast(R, V), "aut": aut_order(R, V),
                      "sha": sha_of_system(R), "blocks": [list(b) for b in canon_system(R)]}
                     for nm, R in reps]},
          open("artifacts/census13.json", "w"), indent=1)
print("wrote artifacts/census13.json")
