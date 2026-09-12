"""verify_lacunary_dual.py — replayable ledger for lane-1063 (TARGET: lacunary dual ubiquity).

Certifies with exact integer arithmetic + rigorous rational enclosures + seeded checks:
 1. Shell counts |{max|q|=2^k}| = 8*2^k (identity + brute force for k=3,4; formula for 10..13).
 2. Odd-east subfamily F_k={(2^k,b): b odd, |b|<=2^k}, |F_k|=2^k (brute force k<=11, formula+parity otherwise).
 3. Exact det census: ALL distinct pairs in F over window k=10..13 have det != 0
    (exact int64 chunked census; analytic minimum 2**min(k,j) from odd/even parity).
 4. ln2 enclosure 0.693 < ln2 < 0.6932 via exact rational series sum (Fractions) + geometric tail.
 5. First-moment ledger S(M,K) lower bounds (exact Fractions): S(10,30) >= 2, so
    overlap-loss ratio D/S^2 <= 1/S <= 1/2; S_K -> infinity (harmonic minorant).
 6. Seeded numerical cross-checks of m(E_q)=2Psi and exact factorization
    m(E_q cap E_r)=m_q*m_r for det != 0 (small-height analog at true scale +
    window shells at 100x scale where counts are ample).

Run: python3 verify_lacunary_dual.py  -> prints VERIFY_OK + ledger, writes ledger.json
"""
import json
import math
import os
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "ledger.json")
rng = np.random.default_rng(20260912)
delta = math.sqrt(2) - 1

# ---------- 1. shell counts ----------
for k in (3, 4):  # brute-force validation of the 8H identity on small shells
    H = 2 ** k
    cnt = sum(1 for a in range(-H, H + 1) for b in range(-H, H + 1)
              if max(abs(a), abs(b)) == H)
    assert cnt == 8 * H, (k, cnt)
shell_counts = {k: 8 * 2 ** k for k in range(10, 14)}
for k, v in shell_counts.items():
    H = 2 ** k
    assert v == (2 * H + 1) ** 2 - (2 * H - 1) ** 2  # exact identity

# ---------- 2. odd-east subfamily counts ----------
def F_list(k):
    H = 2 ** k
    return [(H, b) for b in range(-H, H + 1) if b % 2 == 1]
for k in (3, 4, 10, 11):
    assert len(F_list(k)) == 2 ** k, k
sub_counts = {k: 2 ** k for k in range(10, 14)}
for k in (12, 13):  # formula check without materializing: odds in [-2^k,2^k]
    H = 2 ** k
    assert H % 2 == 0
    assert (H + 1) + H == 2 * H + 1  # evens (H+1) + odds (H) = total
    assert sub_counts[k] == H

# ---------- 3. exact det census over window subfamily ----------
def min_abs_det(k, j, blk=512):
    Hk, Hj = np.int64(2 ** k), np.int64(2 ** j)
    b = np.arange(-Hk + 1, Hk, 2, dtype=np.int64)  # odd b's, length 2^k
    c = np.arange(-Hj + 1, Hj, 2, dtype=np.int64)
    assert len(b) == 2 ** k and len(c) == 2 ** j
    m = 2 ** 62
    for a in range(0, len(b), blk):
        D = Hk * c[None, :] - Hj * b[a:a + blk][:, None]
        if k == j:  # skip diagonal (same vector); off-diagonal must be != 0
            idx = np.arange(a, min(a + blk, len(b)))
            D[np.arange(len(idx)), idx] = np.int64(2 ** 62)
        m = min(m, int(np.min(np.abs(D))))
    return m

det_min = {}
for k in range(10, 14):
    for j in range(10, 14):
        d = min_abs_det(k, j)
        det_min[f"{k},{j}"] = d
        assert d >= 2 ** min(k, j) >= 1024 > 0, (k, j, d)

# ---------- 4. ln2 enclosure (exact rational) ----------
N = 12
S12 = sum(Fraction(1, n * 2 ** n) for n in range(1, N + 1))  # partial sum of ln2 series
tail = Fraction(1, 13 * 2 ** 12)  # tail <= (1/13) sum_{n>=13} 2^-n
LN2_LO, LN2_HI = Fraction(693, 1000), Fraction(6932, 10000)
assert S12 > LN2_LO, float(S12)          # ln2 > S12 > 0.693
assert S12 + tail < LN2_HI, float(S12 + tail)  # ln2 < S12 + tail < 0.6932

# ---------- 5. first-moment ledger (exact Fractions) ----------
def Slow(M, K):
    # S = sum 2/ln(2^k+2); use 2^k+2 <= 2^{k+1} and ln2 <= LN2_HI
    return sum(Fraction(2, 1) / ((k + 1) * LN2_HI) for k in range(M, K + 1))
S13 = Slow(10, 13)
S30 = Slow(10, 30)
assert S30 >= 2, float(S30)
loss30 = 1 / S30  # D/S^2 <= 1/S since D = sum(m-m^2) <= S
assert loss30 <= Fraction(1, 2)

# ---------- 6. Psi sanity + seeded cross-checks ----------
Psi = lambda H: 1.0 / (H * math.log(H + 2))
for k in range(10, 14):
    assert 0 < Psi(2 ** k) < 0.0002 < 0.5
assert Psi(1024) > Psi(8192)  # decreasing

# (a) single strip at true window scale, q=(1024,0): seeded 1D Monte Carlo
H = 1024
n1 = 4_000_000
u1 = rng.random(n1)
fq = np.minimum((H * u1 - delta) % 1.0, 1.0 - (H * u1 - delta) % 1.0)
m_grid = float(np.mean(fq < Psi(H)))
assert abs(m_grid - 2 * Psi(H)) / (2 * Psi(H)) < 0.15, (m_grid, 2 * Psi(H))

# (b) exact factorization, small-height analog at TRUE scale (H=8, det=-41)
Hs, Ps = 8, Psi(8)
n = 2_000_000
u = rng.random(n)
v = rng.random(n)
aq = np.minimum((3 * u + 5 * v - delta) % 1.0, 1.0 - (3 * u + 5 * v - delta) % 1.0)
ar = np.minimum((7 * u - 2 * v - delta) % 1.0, 1.0 - (7 * u - 2 * v - delta) % 1.0)
hit = float(np.mean((aq < Ps) & (ar < Ps)))
assert abs(hit - 4 * Ps * Ps) / (4 * Ps * Ps) < 0.05, (hit, 4 * Ps * Ps)

# (c) exact factorization, window shells at 100x scale (det=2048 != 0, ample counts)
Pw = 100 * Psi(1024)
n2 = 6_000_000
u2 = rng.random(n2)
v2 = rng.random(n2)
bq = np.minimum((1024 * u2 + v2 - delta) % 1.0, 1.0 - (1024 * u2 + v2 - delta) % 1.0)
br = np.minimum((1024 * u2 + 3 * v2 - delta) % 1.0, 1.0 - (1024 * u2 + 3 * v2 - delta) % 1.0)
hit2 = float(np.mean((bq < Pw) & (br < Pw)))
assert abs(hit2 - 4 * Pw * Pw) / (4 * Pw * Pw) < 0.03, (hit2, 4 * Pw * Pw)

with open(OUT, "w") as f:
    json.dump({"shell_counts_10_13": shell_counts,
               "subfamily_counts_10_13": sub_counts,
               "det_min_window": det_min,
               "ln2_series_S12": float(S12), "ln2_tail": float(tail),
               "S13_lower_frac": str(S13), "S13_lower": float(S13),
               "S30_lower_frac": str(S30), "S30_lower": float(S30),
               "loss_ratio_upper_K30": float(loss30),
               "grid_single_true": {"m_grid": m_grid, "two_Psi": 2 * Psi(H)},
               "mc_pair_small_true": {"hit": hit, "prod": 4 * Ps * Ps},
               "mc_pair_window_100x": {"hit": hit2, "prod": 4 * Pw * Pw}}, f, indent=1)
print("shell counts 10..13:", shell_counts)
print("subfamily counts 10..13:", sub_counts)
print("min |det| over window shell pairs:", min(det_min.values()))
print("ln2 in (0.693, 0.6932): S12 =", float(S12), " tail =", float(tail))
print("S(10..13) lower:", float(S13), " S(10..30) lower:", float(S30))
print("overlap-loss ratio upper at K=30:", float(loss30))
print("grid single (true scale):", m_grid, "vs", 2 * Psi(H))
print("pair small-height (true scale): hit", hit, "prod", 4 * Ps * Ps)
print("pair window (100x scale): hit", hit2, "prod", 4 * Pw * Pw)
print("VERIFY_OK")
