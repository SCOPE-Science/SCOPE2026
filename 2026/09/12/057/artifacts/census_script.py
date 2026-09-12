"""Exhaustive per-coefficient hint census for ML-DSA-44 (lane-1248).

Exact FIPS-204 Decompose/HighBits/LowBits/MakeHint/UseHint with
q=8380417, gamma2=95232, alpha=190464, m=44, beta=tau*eta=78.
Full vectorized census over all r in Z_q and all shifts |z|<=78.
"""
import json
import time
import numpy as np

Q = 8380417
G2 = (Q - 1) // 88
A = 2 * G2
H = A // 2
M = (Q - 1) // A
TAU, ETA = 39, 2
B = TAU * ETA
assert (Q - 1) == 88 * G2 and (Q - 1) == 44 * A
assert (G2, A, H, M, B) == (95232, 190464, 95232, 44, 78)

t_start = time.time()
r = np.arange(Q, dtype=np.int32)

# --- exact Decompose, vectorized ---
t = (r % A).astype(np.int32)          # r >= 0 so C-style mod == math mod
t[t > H] -= A                          # centered: r0 in (-H, H]
e = (r - t) == (Q - 1)                 # the q-1 fold
r1 = ((r - t) // A).astype(np.int32)
r1[e] = 0
r0 = t.copy()
r0[e] -= 1
del t
assert int(r1.min()) == 0 and int(r1.max()) == M - 1
assert int(r0.min()) >= -H and int(r0.max()) <= H
# the fold point: Decompose(q-1) must be (0,-1)
assert (int(r1[Q - 1]), int(r0[Q - 1])) == (0, -1)
assert (int(r1[0]), int(r0[0])) == (0, 0)

hist = np.bincount(r1, minlength=M)
assert int(hist.sum()) == Q

# block transitions in linear scan order (r1[q-1]==r1[0]==0 so no wrap artifact)
chg = np.nonzero(np.diff(r1) != 0)[0] + 1
trans = [(int(c), int(r1[c - 1]), int(r1[c])) for c in chg]
assert len(trans) == M
# block j (1..43) is [j*A-H+1 ... ] ; tops c_j = j*A+H, j=0..43 -> transitions at c_j+1
tops = [j * A + H for j in range(M)]
assert sorted(c - 1 for c, _, _ in trans) == tops
for c, a, b in trans:
    assert b == (a + 1) % M

# UseHint(r,1) precompute
uh1 = np.where(r0 > 0, (r1 + 1) % M, (r1 - 1) % M).astype(np.int32)

# --- exhaustive flip + correctness census over z = +-1..+-78 ---
flippable_any = np.zeros(Q, dtype=bool)
total_flip_pairs = 0
per_z_counts = {}
errors = []
for z in list(range(1, B + 1)) + list(range(-1, -B - 1, -1)):
    idx = (r + np.int32(z)) % np.int32(Q)
    flip = r1[idx] != r1
    flippable_any |= flip
    c = int(flip.sum())
    per_z_counts[str(z)] = c
    total_flip_pairs += c
    bad = np.nonzero(flip & (uh1 != r1[idx]))[0]
    for rr in bad.tolist():
        errors.append([int(rr), z, int(uh1[rr]), int(r1[(rr + z) % Q])])
    del idx, flip

nflip = int(flippable_any.sum())
print("flippable r values:", nflip, flush=True)
print("total (r,z) flip pairs:", total_flip_pairs, flush=True)
print("UseHint correctness errors:", len(errors), flush=True)

# --- analytic characterization cross-check ---
# Exact census identity (verified cell below by set equality): the flippable set
# equals the disjoint union over block tops c_j of [c_j-77, c_j+78] (156 pts each).
tops_arr = np.array(tops)
outside = [x for x in np.nonzero(flippable_any)[0].tolist()
           if min(abs(x - tt) for tt in tops) > B]
hyp = set()
for tt in tops:
    hyp.update(range(tt - (B - 1), tt + B + 1))
flipset = set(np.nonzero(flippable_any)[0].tolist())
print("flippable outside boundary neighborhoods:", len(outside), flush=True)
print("exact identity vs union of [c_j-77, c_j+78]:", flipset == hyp,
      len(flipset), len(hyp), flush=True)
assert len(outside) == 0 and flipset == hyp
assert nflip == M * 2 * B  # 44 * 156 = 6864

out = {
    "q": Q, "gamma2": G2, "alpha": A, "m": M,
    "tau": TAU, "eta": ETA, "beta": B, "k": 4, "n": 256, "omega": 80,
    "block_histogram": [int(v) for v in hist],
    "transitions": trans,
    "block_tops": tops,
    "num_flippable_r": nflip,
    "flippable_r": sorted(flipset),
    "total_flip_pairs": total_flip_pairs,
    "per_z_flip_counts": per_z_counts,
    "correctness_errors": errors,
    "neighborhood_characterization_exact": True,
    "elapsed_s": round(time.time() - t_start, 2),
}
with open("output/artifacts/census.json", "w") as f:
    json.dump(out, f)
print("wrote output/artifacts/census.json in %.1fs" % (time.time() - t_start), flush=True)
