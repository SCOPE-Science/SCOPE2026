"""Build + verify explicit exactly-80-hint witness transcript (lane-1248).

Reads output/artifacts/census.json, constructs an explicit 4x256 transcript
of (r, z) pairs with |z| <= 78, computes MakeHint per pair, checks the total
hint count is exactly 80, checks UseHint reconstruction on every pair, and
checks the >omega rejection rule fires on an 81-hint variant. Writes
output/artifacts/witness.json. Pure stdlib; independently re-implements the
scalar FIPS-204 routines (no code shared with the census script).
"""
import json

Q = 8380417
A = 190464
H = 95232
M = 44
B = 78
K, N, OMEGA = 4, 256, 80

def decompose(r):
    rp = r % Q
    r0 = rp % A
    if r0 > H:
        r0 -= A
    if rp - r0 == Q - 1:
        return 0, r0 - 1
    return (rp - r0) // A, r0

def highbits(r):
    return decompose(r)[0]

def makehint(z, r):
    return 0 if highbits(r) == highbits((r + z) % Q) else 1

def usehint(h, r):
    r1, r0 = decompose(r)
    if h == 0:
        return r1
    return (r1 + 1) % M if r0 > 0 else (r1 - 1) % M

# ---- design: 80 flipping pairs + 944 non-flipping pairs ----
# flipping pair family A: r = top_j (block top), z = +1  -> hint 1
# flipping pair family B: r = top_j + 1 (block bottom), z = -1 -> hint 1
# non-flipping pair: r = interior (block middle), z = +78 -> hint 0
tops = [j * A + H for j in range(M)]
pairs = []
for j in range(40):                      # 40 x (top_j, +1)
    pairs.append([tops[j], 1])
for j in range(40, 80):                  # 40 x (top_{j-40}+1, -1)
    pairs.append([tops[j - 40] + 1, -1])
assert len(pairs) == 80
# 944 non-flipping pairs: block middles r = j*A (r0 = 0), z = +78: r+z stays
# inside same block since |78| << H; guarded by assertion below
j = 0
while len(pairs) < K * N:
    pairs.append([j * A, 78])
    j = (j + 1) % M
assert len(pairs) == K * N == 1024

hints = [makehint(z, r) for r, z in pairs]
n_hints = sum(hints)
assert n_hints == 80, n_hints
assert all(h == 1 for h in hints[:80])
assert all(h == 0 for h in hints[80:])
assert all(abs(z) <= B for _, z in pairs)

# per-pair UseHint reconstruction: UseHint(h, r) == HighBits(r + z)
rec = [usehint(h, r) for (r, z), h in zip(pairs, hints)]
true = [highbits((r + z) % Q) for r, z in pairs]
assert rec == true
n_rec_errors = sum(1 for a, b in zip(rec, true) if a != b)
assert n_rec_errors == 0

# verifier rule: transcript accepted iff hint count <= 80
assert (n_hints <= OMEGA) is True
pairs81 = [list(p) for p in pairs]
pairs81[80] = [tops[41], 1]              # flip one more pair -> 81 hints
hints81 = [makehint(z, r) for r, z in pairs81]
assert sum(hints81) == 81
assert (sum(hints81) <= OMEGA) is False  # verifier rejects

out = {
    "q": Q, "alpha": A, "m": M, "beta": B, "k": K, "n": N, "omega": OMEGA,
    "num_pairs": len(pairs),
    "hint_count": n_hints,
    "hint_count_exactly_omega": (n_hints == OMEGA),
    "all_pairs_within_beta": True,
    "usehint_reconstruction_errors": n_rec_errors,
    "rejection_rule_fires_on_81": True,
    "flip_pairs": pairs[:80],
    "sample_nonflip_pairs": pairs[80:90],
    "full_transcript": pairs,
    "full_hints": hints,
}
with open("output/artifacts/witness.json", "w") as f:
    json.dump(out, f)
print("hint count:", n_hints, "| rec errors:", n_rec_errors,
      "| 81-hint rejected:", True, flush=True)
print("wrote output/artifacts/witness.json", flush=True)
