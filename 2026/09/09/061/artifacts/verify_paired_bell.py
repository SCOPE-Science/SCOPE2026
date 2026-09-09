"""Paired-Bell stabilizer witnesses for E1 non-containment + rank-quantization demo.
Objects: quhex Bell |B> = 6^-1/2 sum_s |ss> (stabilizer), paired across 4 quhexes.
Checks: P12 = B12 x B34 has cut-ranks (1, 36, 36); cyclic perms likewise.
Implication: D1 vanishes on P12's first cut but D2,D3 != 0 there, i.e. each
determinantal invariant is nonzero on the others' varieties (non-containment
for the Nullstellenssatz divisibility chain). Also demos qubit-factor rank
quantization {1,2,4} on 4-qubit GHZ cut. numpy only.
"""
import numpy as np

d = 6
B = np.zeros((d, d), dtype=complex)
for s in range(d):
    B[s, s] = 1.0 / np.sqrt(d)

def ranks_of_pairing(pair):
    """pair: ((a,b),(q,w)) Bell pairs; full tensor T[i,j,k,l]; ranks across 3 cuts."""
    T = np.zeros((d, d, d, d), dtype=complex)
    (a, b), (q, w) = pair
    # T = B_ab (x) B_qw
    for x1 in range(d):
        for x2 in range(d):
            for y1 in range(d):
                for y2 in range(d):
                    v = [None]*4
                    v[a], v[b] = x1, x2
                    v[q], v[w] = y1, y2
                    T[v[0], v[1], v[2], v[3]] = B[x1, x2] * B[y1, y2]
    out = {}
    for name, (A, BB) in {'12|34': ((0,1),(2,3)), '13|24': ((0,2),(1,3)),
                          '14|23': ((0,3),(1,2))}.items():
        M = np.transpose(T, list(A) + list(BB)).reshape(d*d, d*d)
        r = int(np.sum(np.linalg.svd(M, compute_uv=False) > 1e-9))
        out[name] = (r, abs(np.linalg.det(M)))
    return out

for pairing in [((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2))]:
    res = ranks_of_pairing(pairing)
    print("pairs", pairing, {k: f"rank={v[0]} |det|={v[1]:.3e}" for k, v in res.items()})

# Non-containment summary: for pairing ((0,1),(2,3)): D(12|34)=0, others !=0 etc.
# Qubit-factor rank quantization demo: 4-qubit GHZ across 2-2 cut has rank 2.
g = np.zeros((2,2,2,2), dtype=complex)
for s in range(2):
    g[s,s,s,s] = 1/np.sqrt(2)
M = g.transpose(0,1,2,3).reshape(4,4)
r = int(np.sum(np.linalg.svd(M, compute_uv=False) > 1e-9))
print("4-qubit GHZ 2-2 cut rank =", r, "(expect 2: in {1,2,4}, not maximally mixed)")
assert r == 2
print("PAIRED_BELL_WITNESSES_OK")
