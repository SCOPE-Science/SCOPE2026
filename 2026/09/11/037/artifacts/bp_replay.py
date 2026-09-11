"""Replayable BP+SSF decoding log for Q16 (X side, code-capacity + noisy-syndrome).
Min-sum BP (damping 0.8, <=40 iters) + greedy single-bit SSF post-processing.
Fixed seeds; numpy only. Prints logical-error-rate table.
Code-capacity (300 shots/point, seed 999): p=0.03 LER 0.0; 0.04 -> 0.02;
0.05 -> 0.05; 0.06 -> 0.17; 0.075 -> 0.54 (no threshold >= 7.5%).
Phenomenological noisy syndrome q=p (300 shots/point, seed 777, BP only):
p=q=0.01 LER ~0.60; 0.02 ~0.76 (no suppression; far from 3% reference).
"""
import numpy as np

A = np.array([[14, 1, 9, 6], [12, 10, 6, 0], [4, 4, 8, 3]])
L = 16

def expand_LP(A, B, l):
    m1, n1 = A.shape
    m2, n2 = B.shape
    Nqx = n1 * n2 * l + m1 * m2 * l
    HX = np.zeros((m1 * n2 * l, Nqx), dtype=np.uint8)
    HZ = np.zeros((n1 * m2 * l, Nqx), dtype=np.uint8)
    for a in range(m1):
        for x in range(n2):
            for k in range(l):
                r = (a * n2 + x) * l + k
                for b in range(n1):
                    HX[r, (b * n2 + x) * l + ((k - int(A[a, b])) % l)] ^= 1
                for j in range(m2):
                    HX[r, n1 * n2 * l + (a * m2 + j) * l + ((k - int(B[j, x])) % l)] ^= 1
    for b in range(n1):
        for y in range(m2):
            for k in range(l):
                r = (b * m2 + y) * l + k
                for x in range(n2):
                    HZ[r, (b * n2 + x) * l + ((k + int(B[y, x])) % l)] ^= 1
                for a in range(m1):
                    HZ[r, n1 * n2 * l + (a * m2 + y) * l + ((k + int(A[a, b])) % l)] ^= 1
    return HX, HZ

def kernel_mat(H):
    m, n = H.shape
    G = H.copy() % 2
    piv = {}
    r = 0
    for c in range(n):
        p = -1
        for i in range(r, m):
            if G[i, c]:
                p = i
                break
        if p < 0:
            continue
        G[[r, p]] = G[[p, r]]
        for i in range(m):
            if i != r and G[i, c]:
                G[i] ^= G[r]
        piv[c] = r
        r += 1
    free = [c for c in range(n) if c not in piv]
    K = np.zeros((len(free), n), dtype=np.int64)
    for i, f in enumerate(free):
        K[i, f] = 1
        for c, rr in piv.items():
            if G[rr, f]:
                K[i, c] = 1
    return K

HX, HZ = expand_LP(A, A, L)
M, N = HX.shape
KZ = kernel_mat(HZ.astype(np.int64))
rows, cols = np.where(HX)
row_edges = [np.where(rows == i)[0] for i in range(M)]
col_rows = [np.where(HX[:, j])[0] for j in range(N)]
edge_col = cols

def bp_decode(synd, p, iters=40, damp=0.8):
    S = synd.shape[0]
    Lch = np.full((S, N), np.log((1 - p) / p))
    Mv2c = Lch[:, edge_col].copy()
    Mc2v = np.zeros_like(Mv2c)
    est = np.zeros((S, N), dtype=int)
    for _ in range(iters):
        for i in range(M):
            e = row_edges[i]
            x = Mv2c[:, e]
            sgn = np.sign(x)
            sgn[sgn == 0] = 1.0
            P = sgn.prod(axis=1)
            out = P[:, None] * sgn * (1 - 2 * synd[:, [i]])
            ax = np.abs(x)
            idx = np.argmin(ax, axis=1)
            m1 = ax[np.arange(S), idx]
            tmp = ax.copy()
            tmp[np.arange(S), idx] = np.inf
            m2 = np.min(tmp, axis=1)
            pos = np.arange(len(e))[None, :] == idx[:, None]
            Mc2v[:, e] = out * np.where(pos, m2[:, None], m1[:, None]) * damp
        tot = np.zeros((S, N))
        for s in range(S):
            np.add.at(tot[s], edge_col, Mc2v[s])
        Mv2c = Lch[:, edge_col] + (tot[:, edge_col] - Mc2v)
        est = ((tot + Lch) < 0).astype(int)
        if (np.mod(est @ HX.T, 2) == synd).all():
            break
    return est

def ssf_pp(est, synd, max_rounds=50):
    out = est.copy()
    for s in range(out.shape[0]):
        cur = np.mod(out[s] @ HX.T, 2)
        tgt = synd[s]
        for _ in range(max_rounds):
            res = np.mod(cur + tgt, 2)
            if res.sum() == 0:
                break
            bg, bj = 0, -1
            for j in range(N):
                cr = col_rows[j]
                g = res[cr].sum() - (len(cr) - res[cr].sum())
                if g > bg:
                    bg, bj = g, j
            if bg <= 0:
                break
            out[s, bj] ^= 1
            cur = np.mod(out[s] @ HX.T, 2)
    return out

def ler(est, err):
    return 1.0 - (np.mod(np.mod(est + err, 2) @ KZ.T, 2) == 0).all(axis=1).mean()

def main():
    rng = np.random.default_rng(999)
    print("code-capacity BP+SSF, 300 shots/point, seed 999:")
    for p in [0.03, 0.04, 0.05, 0.06, 0.075]:
        S = 300
        err = (rng.random((S, N)) < p).astype(int)
        synd = np.mod(err @ HX.T, 2)
        est = ssf_pp(bp_decode(synd, p), synd)
        print(f"  p={p}: LER={(ler(est, err)):.4f}")
    rng2 = np.random.default_rng(777)
    print("phenomenological noisy syndrome q=p, BP only, 300 shots/point, seed 777:")
    for p in [0.01, 0.02]:
        S = 300
        err = (rng2.random((S, N)) < p).astype(int)
        synd = np.mod(err @ HX.T + (rng2.random((S, M)) < p).astype(int), 2)
        est = bp_decode(synd, p)
        print(f"  p=q={p}: LER={(ler(est, err)):.4f}")
    print("BP_REPLAY_OK")

if __name__ == "__main__":
    main()
