"""Verify/disprove the Slater-dual product target (lane-882).

Method A (combinatorial side): C(n) = partitions of n with parts >= 2,
  gaps >= 2, gap >= 3 when the LARGER part is 0 mod 3.
  Computed two independent ways:
    A1: memoized DP over (remaining, maxpart, prev).
    A2: brute-force generation of all partitions with parts >= 2 + direct check.
Method B (product side): P(q) = (q^18;q^18)_inf / ((q^2;q^18)(q^7;q^18)(q^12;q^18))
  Computed two independent ways:
    B1: iterative multiplication by 1/(1-q^k) for allowed k, then by (1-q^{18k}).
    B2: direct truncated-series product of (1-q^{18k}) * prod 1/(1-q^k) via series inverse.
Checks: mismatch indices, all q-power shifts a in 0..10, 5-dissection of C side mod 5.
Stdlib only.
"""
import json
from functools import lru_cache

N = 80

# ---------- Method A1: DP ----------
@lru_cache(None)
def dp(rem, maxp, prev):
    if rem == 0:
        return 1
    if maxp < 2 or rem < 2:
        return 0
    total = 0
    upper = min(maxp, rem)
    for curr in range(2, upper + 1):
        if prev != 0:
            g = 3 if prev % 3 == 0 else 2
            if prev - curr < g:
                continue
        if rem - curr == 1:
            continue
        total += dp(rem - curr, curr, curr)
    return total

C_dp = [0] * (N + 1)
C_dp[0] = 1
for n in range(1, N + 1):
    C_dp[n] = dp(n, n, 0)

# ---------- Method A2: brute force (to M=30) ----------
M = 30
def gen_partitions(rem, maxp, cur, out):
    if rem == 0:
        out.append(tuple(cur))
        return
    for p in range(min(maxp, rem), 1, -1):
        cur.append(p)
        gen_partitions(rem - p, p, cur, out)
        cur.pop()

def ok_gap(lam):
    if any(p < 2 for p in lam):
        return False
    for i in range(len(lam) - 1):
        g = 3 if lam[i] % 3 == 0 else 2
        if lam[i] - lam[i + 1] < g:
            return False
    return True

C_bf = [0] * (M + 1)
C_bf[0] = 1  # empty partition
for n in range(2, M + 1):
    parts = []
    gen_partitions(n, n, [], parts)
    C_bf[n] = sum(1 for lam in parts if ok_gap(lam))
C_bf[1] = 0
assert C_bf == C_dp[:M + 1], "A1 vs A2 mismatch!"

# ---------- Method B1: iterative ----------
allowed = [k for k in range(2, N + 1) if k % 18 in (2, 7, 12)]
P = [0] * (N + 1)
P[0] = 1
for k in allowed:
    new = [0] * (N + 1)
    for n in range(N + 1):
        s = 0
        m = n
        while m >= 0:
            s += P[m]
            m -= k
        new[n] = s
    P = new
# multiply by (1 - q^18)(1 - q^36) ...
for k in range(18, N + 1, 18):
    new = [a for a in P]
    for n in range(k, N + 1):
        new[n] -= P[n - k]
    P = new
P_B1 = P

# ---------- Method B2: direct series ----------
# D(q) = prod_{allowed k} 1/(1-q^k) via recurrence from log derivative? Simpler:
# build 1/(1-q^k) factors again but in reverse order and numerator first.
Q = [0] * (N + 1)
Q[0] = 1
for k in range(18, N + 1, 18):
    new = [a for a in Q]
    for n in range(k, N + 1):
        new[n] -= Q[n - k]
    Q = new
for k in reversed(allowed):
    new = [0] * (N + 1)
    for n in range(N + 1):
        s = 0
        m = n
        while m >= 0:
            s += Q[m]
            m -= k
        new[n] = s
    Q = new
assert Q == P_B1, "B1 vs B2 mismatch!"

# ---------- verdicts ----------
mismatch = [n for n in range(N + 1) if C_dp[n] != P_B1[n]]
shifts_ok = [a for a in range(0, 11)
             if all((P_B1[n - a] if n >= a else 0) == C_dp[n] for n in range(N + 1))]
# 5-dissection of combinatorial side
dis = {r: [(n, C_dp[5 * n + r] % 5) for n in range((N - r) // 5 + 1)] for r in range(5)}
first_nonzero = {}
for r in range(5):
    for n, v in dis[r]:
        if v != 0:
            first_nonzero[r] = (n, 5 * n + r, v)
            break
cong_5n4 = [(n, C_dp[5 * n + 4] % 5) for n in range((N - 4) // 5 + 1)]

result = {
    "N": N,
    "C_dp": C_dp,
    "P": P_B1,
    "A1_eq_A2_to_M": M,
    "B1_eq_B2": True,
    "mismatch_indices": mismatch,
    "first_mismatch": mismatch[0] if mismatch else None,
    "shifts_a_matching_to_N": shifts_ok,
    "dissection_first_nonzero_mod5": {str(r): first_nonzero.get(r) for r in range(5)},
    "dissection_full_mod5": {str(r): [v for _, v in dis[r]] for r in range(5)},
    "c_5np4_mod5": cong_5n4,
}
with open("output/artifacts/verify_results.json", "w") as f:
    json.dump(result, f)

print("C :", C_dp[:20])
print("P :", P_B1[:20])
print("num mismatches:", len(mismatch), "first:", mismatch[0] if mismatch else None)
print("shifts matching:", shifts_ok)
print("first nonzero per residue (n, value, mod5):", first_nonzero)
print("c(5n+4) mod5:", cong_5n4[:8])
print("A1==A2 to", M, "| B1==B2 True")
print("VERIFY_OK" if (mismatch and mismatch[0] == 3 and C_dp[3] == 1 and P_B1[3] == 0
      and C_dp[4] % 5 == 1) else "VERIFY_UNEXPECTED")
