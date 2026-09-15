"""Consolidated verifier for the emergent claim. Reproduces the atomic two-sided CSS-repair obstruction end to end.
Claim: Q1 = truncate(Q0 tensor P) with Q0=[[4,2,2]], P=[3,2,2] parity complex has n=13,K=4,DX=2,DZ=4
(GF(2) ranks: rank(HX)=6, rank(HZ)=3; row-space sizes 64/8),
baseline dressed radius-1 (rhoX,rhoZ)=(1.0,2.0); every X and Z check heavy; no CSS-safe single-ancilla
bipartition of X-row0 support {0,1,2,3} exists (all 7 unordered bipartitions); every consistent Z-gauge
repair forces a dropped opposite-side syndrome set (partition1: 64 solutions, min added-fix weight 5;
partition2: 64 solutions, min added-fix weight 6), and the repaired code has dressed radius-1 (0,0) with
gauge-inequivalent blind witnesses at dressed distance 1.
Conventions for the (0,0) claim:
  - Stabilizer convention: gauge groups equal stabilizer groups; X-error syndrome map = full repaired HZs,
    Z-error syndrome map = full repaired HXs. Partition1 HZs=[Z0;g] (2x14, rank 2), HXs (8x14, rank 7):
    stabilizer radius-1 (rhoX,rhoZ)=(0.0,2.0). Partition2 HZs=[g] (1x14, rank 1), HXs (8x14, rank 7):
    stabilizer radius-1 (rhoX,rhoZ)=(0.0,2.0).
  - Dressed-subsystem convention: X-gauge GX=row(HXs) (|GX|=128), Z-gauge GZ=row(HZs) (|GZ|=4 for
    partition1, 2 for partition2); measured Z-error syndrome map SX_syn (7x14, rank 6: 6 untouched old X
    rows + c1+c2); measured X-error syndrome map SZ_syn (partition1: 1x14 [Z0], rank 1; partition2: empty
    0x14 set, rank 0). Dressed radius-1 (rhoX,rhoZ)=(0.0,0.0) on both partitions.
"""
import numpy as np


def gf2_rank(M):
    A = M.copy() % 2
    rows, cols = A.shape
    R = 0
    for c in range(cols):
        piv = None
        for i in range(R, rows):
            if A[i, c] == 1:
                piv = i
                break
        if piv is None:
            continue
        A[[R, piv]] = A[[piv, R]]
        for i in range(rows):
            if i != R and A[i, c] == 1:
                A[i] ^= A[R]
        R += 1
        if R == rows:
            break
    return R


def row_space(H):
    r = H.shape[0]
    S = set()
    for mask in range(1 << r):
        v = np.zeros(H.shape[1], dtype=int)
        for i in range(r):
            if mask >> i & 1:
                v ^= H[i]
        S.add(tuple(v.tolist()))
    return S


def min_dist(e, S, n):
    et = tuple(e.tolist())
    best = n + 1
    for c in S:
        w = sum(1 for a, b in zip(et, c) if a != b)
        if w < best:
            best = w
            if best == 0:
                break
    return best


HX0 = np.ones((1, 4), dtype=int)
HZ0 = np.ones((1, 4), dtype=int)
A = HZ0.T.copy()
B = HX0.copy()
H0d = np.ones((1, 3), dtype=int)
I3 = np.eye(3, dtype=int)
I1 = np.eye(1, dtype=int)
I4 = np.eye(4, dtype=int)
d3 = np.vstack([np.kron(I1, H0d) % 2, np.kron(A, I3) % 2])
d2 = np.vstack([np.hstack([np.kron(A, I1) % 2, np.kron(I4, H0d) % 2]),
                np.hstack([np.zeros((3, 1), dtype=int), np.kron(B, I3) % 2])])
assert not (d2.dot(d3) % 2).any(), "not a complex"
HXp = d2 % 2
HZp = (d3.T) % 2
n = 13
assert not (HXp.dot(HZp.T) % 2).any(), "not CSS"
rX = gf2_rank(HXp)
rZ = gf2_rank(HZp)
K = 13 - rX - rZ
print(f"Q1: n=13 K={K} rankHX={rX} rankHZ={rZ} Xw={HXp.sum(1).tolist()} Zw={HZp.sum(1).tolist()}")
assert rX == 6 and rZ == 3, "GF(2) ranks must be 6/3"
assert K == 4, "K must be 4 over GF(2)"
SX0 = row_space(HXp)
SZ0 = row_space(HZp)
print(f"row-space sizes: |rowHX|={len(SX0)} |rowHZ|={len(SZ0)}")
assert len(SX0) == 64 and len(SZ0) == 8, "row-space sizes must be 64/8"
assert int((HXp.sum(1) > 3).sum()) == 7 and int((HZp.sum(1) > 3).sum()) == 3, "not all heavy"


def base_curve(Hsyn, Sgauge, nn):
    S = row_space(Sgauge)
    rho = 1e9
    for mask in range(1, 1 << nn):
        e = np.array([(mask >> i) & 1 for i in range(nn)], dtype=int)
        d = min_dist(e, S, nn)
        if d == 0 or d > 1:
            continue
        sw = int((Hsyn.dot(e) % 2).sum())
        rho = min(rho, sw / d)
    return rho


print("baseline rhoX:", base_curve(HZp, HXp, 13), "rhoZ:", base_curve(HXp, HZp, 13))

# No CSS-safe bipartition over ALL 7 unordered bipartitions of {0,1,2,3} (fix 0 in A).
HZemb = np.hstack([HZp, np.zeros((3, 1), dtype=int)])
supp = [0, 1, 2, 3]
parts = []
for mask in range(1, 1 << 4):
    Aset = tuple(sorted([supp[k] for k in range(4) if mask >> k & 1]))
    Bset = tuple(sorted(set(supp) - set(Aset)))
    if not Aset or not Bset:
        continue
    if 0 not in Aset:
        continue
    parts.append((Aset, Bset))
assert len(parts) == 7, "must be 7 unordered bipartitions"
for Aset, Bset in parts:
    c1 = np.zeros(14, dtype=int)
    c2 = np.zeros(14, dtype=int)
    for j in Aset:
        c1[j] = 1
    c1[13] = 1
    for j in Bset:
        c2[j] = 1
    c2[13] = 1
    safe = all(int(c1.dot(r) % 2) == 0 for r in HZemb) and all(int(c2.dot(r) % 2) == 0 for r in HZemb)
    print(tuple(Aset), tuple(Bset), "CSS-safe:", safe)
    assert not safe, f"{Aset}|{Bset} unexpectedly safe"


def check_partition(name, Aset, Bset, exp_minw, exp_keep):
    c1 = np.zeros(14, dtype=int)
    c2 = np.zeros(14, dtype=int)
    for j in Aset:
        c1[j] = 1
    c1[13] = 1
    for j in Bset:
        c2[j] = 1
    c2[13] = 1
    HXs = np.vstack([np.hstack([HXp, np.zeros((7, 1), dtype=int)])[1:], c1, c2])
    M = HXs[:, :13] % 2
    b = HXs[:, 13] % 2
    sols = [np.array([(m >> i) & 1 for i in range(13)], dtype=int) for m in range(1 << 13)
            if ((M.dot(np.array([(m >> i) & 1 for i in range(13)], dtype=int)) % 2) == b).all()]
    minw = min(int(t.sum()) + 1 for t in sols)
    print(f"{name}: consistent g count: {len(sols)} min w(g): {minw} rankHXs={gf2_rank(HXs)}")
    assert len(sols) == 64 and minw == exp_minw, f"{name} fix count/weight mismatch"
    t = min(sols, key=lambda v: int(v.sum()))
    g = np.append(t, [1])
    clash = [j for j in range(3) if int(c1.dot(HZemb[j]) % 2) or int(c2.dot(HZemb[j]) % 2)]
    keep = [j for j in range(3) if j not in clash]
    print(f"{name}: clashing: {clash} keep: {keep}")
    assert keep == exp_keep, f"{name} keep-set mismatch"
    SX_syn = np.vstack([np.hstack([HXp, np.zeros((7, 1), dtype=int)])[1:], (c1 + c2) % 2])
    SZ_syn = HZemb[keep] if keep else np.zeros((0, 14), dtype=int)
    HZs = np.vstack([HZemb[keep], g]) if keep else g.reshape(1, 14)
    assert not (HXs.dot(HZs.T) % 2).any(), f"{name} repair not CSS"
    print(f"{name}: HXs {HXs.shape} r={gf2_rank(HXs)} HZs {HZs.shape} r={gf2_rank(HZs)} "
          f"SX_syn {SX_syn.shape} r={gf2_rank(SX_syn)} "
          f"SZ_syn {SZ_syn.shape} r={gf2_rank(SZ_syn) if SZ_syn.shape[0] > 0 else 0} "
          f"|GX|={len(row_space(HXs))} |GZ|={len(row_space(HZs))}")
    # Dressed convention: distance mod full gauge rows, syndrome from measured stabilizers only.
    GX = row_space(HXs)
    GZ = row_space(HZs)
    rhox = 1e9
    rhoz = 1e9
    wx = None
    wz = None
    for mask in range(1, 1 << 14):
        e = np.array([(mask >> i) & 1 for i in range(14)], dtype=int)
        dx = min_dist(e, GX, 14)
        if dx == 1:
            sw = int((SZ_syn.dot(e) % 2).sum()) if SZ_syn.shape[0] > 0 else 0
            if sw / dx < rhox:
                rhox = sw / dx
                wx = e.copy()
        dz = min_dist(e, GZ, 14)
        if dz == 1:
            sw = int((SX_syn.dot(e) % 2).sum())
            if sw / dz < rhoz:
                rhoz = sw / dz
                wz = e.copy()
    print(f"{name}: dressed radius-1 rhoX: {rhox} witness: {wx} rhoZ: {rhoz} witness: {wz}")
    assert rhox == 0.0 and rhoz == 0.0, f"{name} no dressed collapse"
    assert tuple(wx.tolist()) not in GX and tuple(wz.tolist()) not in GZ, f"{name} witnesses must be gauge-inequivalent"
    # Stabilizer convention: distance mod full row spaces, syndrome from full HXs/HZs.
    SX = row_space(HXs)
    SZ = row_space(HZs)
    srhox = 1e9
    srhoz = 1e9
    for mask in range(1, 1 << 14):
        e = np.array([(mask >> i) & 1 for i in range(14)], dtype=int)
        dx = min_dist(e, SX, 14)
        if dx == 1:
            sw = int((HZs.dot(e) % 2).sum())
            srhox = min(srhox, sw / dx)
        dz = min_dist(e, SZ, 14)
        if dz == 1:
            sw = int((HXs.dot(e) % 2).sum())
            srhoz = min(srhoz, sw / dz)
    print(f"{name}: stabilizer radius-1 rhoX: {srhox} rhoZ: {srhoz}")
    assert srhox == 0.0 and srhoz == 2.0, f"{name} stabilizer values mismatch"
    return wx, wz


check_partition("p1 {0,1}|{2,3}", {0, 1}, {2, 3}, 5, [0])
check_partition("p2 {0}|{1,2,3}", {0}, {1, 2, 3}, 6, [])
print("ALL EMERGENT-CHECKS PASSED")
