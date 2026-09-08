"""Independent verifier for the covering-radius census fragment.
Reads census.json (same directory), checks per cell:
 (1) H is r x n binary, rank = r, no zero column;
 (2) exact covering radius by full syndrome BFS over all 2^r syndromes;
 (3) full coset weight distribution sums to 2^r and matches stored cwd/rho;
 (4) sphere-covering lower bound recomputation and gap/optimal flags.
Stdlib + numpy only. Usage: python3 verify.py [census.json]
"""
import json, math, sys, os
import numpy as np
def sph_lb(n, r):
    s = 0
    for i in range(n + 1):
        s += math.comb(n, i)
        if s >= 2 ** r:
            return i
    return n
def rank_gf2(H):
    M = H.copy() % 2; r, n = M.shape; rk = 0; row = 0
    for c in range(n):
        p = -1
        for i in range(row, r):
            if M[i, c]: p = i; break
        if p < 0: continue
        M[[row, p]] = M[[p, row]]
        for i in range(r):
            if i != row and M[i, c]: M[i] ^= M[row]
        row += 1; rk += 1
        if row == r: break
    return rk
def covering_radius(cols, r):
    N = 1 << r; IDX = np.arange(N)
    dist = np.full(N, -1, dtype=np.int32); dist[0] = 0
    frontier = np.zeros(N, dtype=bool); frontier[0] = True
    d = 0; nleft = N - 1; cols = [int(c) for c in cols]
    while nleft > 0:
        d += 1
        newf = np.zeros(N, dtype=bool)
        for c in cols: newf |= frontier[IDX ^ c]
        newf &= (dist < 0)
        cnt = int(newf.sum())
        if cnt == 0: raise ValueError("unreachable syndrome: rank-deficient H")
        dist[newf] = d; frontier = newf; nleft -= cnt
    return int(dist.max()), dist
def main(path):
    d = json.load(open(path))
    cells = d["cells"]; nfail = 0
    for c in cells:
        n, k, r = c["n"], c["k"], c["r"]
        H = np.array(c["H"], dtype=np.int64)
        assert H.shape == (r, n), (n, k, H.shape)
        assert set(np.unique(H)) <= {0, 1}
        rk = rank_gf2(H)
        assert rk == r, (n, k, rk)
        assert (H.sum(axis=0) > 0).all(), (n, k, "zero column")
        cols = []
        for j in range(n):
            v = 0
            for i in range(r):
                if H[i, j]: v |= (1 << i)
            cols.append(v)
        rho, dist = covering_radius(cols, r)
        cwd = [int((dist == w).sum()) for w in range(rho + 1)]
        assert sum(cwd) == 2 ** r, (n, k)
        lb = sph_lb(n, r)
        ok = (rho == c["rho"] and cwd == c["cwd"] and lb == c["sphere_lb"]
              and (rho - lb) == c["gap"] and (rho == lb) == c["optimal"])
        flag = "OPT" if c["optimal"] else f"gap{c['gap']}"
        print(f"[{n},{k}] r={r} rho={rho} sphLB={lb} {flag} cwd={cwd} {'OK' if ok else 'MISMATCH'}")
        if not ok: nfail += 1
    print(f"{len(cells)-nfail}/{len(cells)} cells verified; {sum(1 for c in cells if c['optimal'])} sphere-optimal pins.")
    return 1 if nfail else 0
if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "census.json")
    sys.exit(main(p))
