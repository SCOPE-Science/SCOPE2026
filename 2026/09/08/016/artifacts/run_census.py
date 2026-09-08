"""Exhaustive conditioned census: P* (published-optimal E=26 anchor) fixed,
Q over all 2^20 sign patterns with q0=+1 (global-sign quotient; lossless for
S(Q)=E(Q)+X(P*,Q) since both E and X are invariant under Q -> -Q).
Exact integer arithmetic (chunked numpy int). Writes census_top.json."""
import numpy as np, json, time

P = np.array([-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,1,-1], dtype=np.int8)
N = 21

def auto_E(A):
    n = A.shape[1]
    E = np.zeros(A.shape[0], dtype=np.int64)
    for k in range(1, n):
        c = (A[:, :n-k].astype(np.int16) * A[:, k:].astype(np.int16)).sum(axis=1).astype(np.int64)
        E += c * c
    return E

def cross_X(A, P):
    n = A.shape[1]
    X = np.zeros(A.shape[0], dtype=np.int64)
    Ai = A.astype(np.int16)
    Pi = P.astype(np.int16)
    for k in range(-(n-1), n):
        if k >= 0:
            d = (Pi[:n-k] * Ai[:, k:]).sum(axis=1).astype(np.int64)
        else:
            d = (Pi[-k:] * Ai[:, :n+k]).sum(axis=1).astype(np.int64)
        X += d * d
    return X

# sanity: E(P*)==26 and X identity X = N^2 + 2<C^P,C^Q> on random sample
assert int(auto_E(P[None, :])[0]) == 26
rng = np.random.default_rng(0)
T = rng.choice([-1, 1], size=(500, N)).astype(np.int8)
Cp = np.array([(P[:N-k] * P[k:]).sum() for k in range(1, N)])
for q in T[:20]:
    Cq = np.array([(q[:N-k] * q[k:]).sum() for k in range(1, N)])
    assert int(cross_X(q[None, :], P)[0]) == N * N + 2 * int((Cp * Cq).sum())
print("sanity OK: E(P*)=26, X-identity holds", flush=True)

B = 1 << 17
TOTAL = 1 << 20
shifts = np.arange(0, 20, dtype=np.int64)  # positions 1..20 <- bits 0..19
TOPK = 512
top = []
t0 = time.time()
done = 0
for off in range(0, TOTAL, B):
    b = min(B, TOTAL - off)
    idx = np.arange(off, off + b, dtype=np.int64)
    A = np.where(((idx[:, None] >> shifts) & 1) == 1, 1, -1).astype(np.int8)
    A = np.concatenate([np.ones((b, 1), dtype=np.int8), A], axis=1)
    E = auto_E(A)
    X = cross_X(A, P)
    S = E + X
    k = min(TOPK, b)
    part = np.argpartition(S, k - 1)[:k]
    for j in part:
        top.append((int(S[j]), int(off + j)))
    top.sort()
    top = top[:TOPK]
    done += b
    print(f"chunk {off//B+1}/{TOTAL//B}: done={done} minS={top[0][0]} t={time.time()-t0:.1f}s", flush=True)

assert done == TOTAL == 1048576

def bits_of(i):
    return [1] + [1 if (i >> s) & 1 else -1 for s in range(0, 20)]

out = {"P*": [int(v) for v in P.tolist()], "E_P": 26, "total_enumerated": done,
       "quotient": "q0=+1 (global-sign quotient, lossless for S)",
       "top": [{"S": s, "Q": bits_of(i), "idx": i} for s, i in top[:64]]}
with open("output/artifacts/census_top.json", "w") as f:
    json.dump(out, f)
from collections import Counter
print("S-histogram over kept top512:", dict(sorted(Counter(s for s, _ in top).items())), flush=True)
print("TOTAL_ENUMERATED:", done, flush=True)
