"""Save certified cocycle reps + d2-boundary analysis for (3,50) and (5,51)-window.
Run: python3 save_cell.py  (writes cell_3_50.json)
"""
import sys, json
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-705/output/artifacts')
from ext_cobar import *
import numpy as np
mo = Comod('moore')

def dense(s0, t):
    A0 = cobar_basis(mo, s0, t); A1 = cobar_basis(mo, s0+1, t)
    q = {b: k for k, b in enumerate(A1)}
    M = np.zeros((len(A1), len(A0)), dtype=int)
    for col, (tup, c) in enumerate(A0):
        if s0 == 0:
            for (gp, cpp), v in mo.nubar[c].items():
                r = q.get(((gp,), cpp))
                if r is not None:
                    M[r, col] = (M[r, col]+v) % 5
        else:
            for j in range(s0):
                sgn = -1 if (j & 1) else 1
                for (a, b_), v in PSIBAR[tup[j]].items():
                    r = q.get((tup[:j]+(a, b_)+tup[j+1:], c))
                    if r is not None:
                        M[r, col] = (M[r, col]+sgn*v) % 5
            sgn = -1 if (s0 & 1) else 1
            for (gp, cpp), v in mo.nubar[c].items():
                r = q.get((tup+(gp,), cpp))
                if r is not None:
                    M[r, col] = (M[r, col]+sgn*v) % 5
    return A0, A1, M % 5

def gf_rref_rank(M):
    R = M.copy() % 5
    m, n = R.shape
    piv = {}
    rr = 0
    for c in range(n):
        p = None
        for i in range(rr, m):
            if R[i, c] % 5:
                p = i; break
        if p is None:
            continue
        R[[rr, p]] = R[[p, rr]]
        R[rr] = R[rr]*pow(int(R[rr, c]), 3, 5) % 5
        for i in range(m):
            if i != rr and R[i, c] % 5:
                R[i] = (R[i]-R[i, c]*R[rr]) % 5
        piv[c] = rr; rr += 1
    return R, piv, rr

def fmt_elt(tup, c):
    return {"gammas": [[int(x) for x in mons[g][:5]] + [mons[g][5]] for g in tup],
            "gam_degs": [mons[g][5] for g in tup], "cls": mo.cls[c][1], "cls_deg": mo.cls[c][0]}

out = {"prime": 5, "object": "P^3(5) Moore comodule", "convention": "simplicial-sign cobar, validated d^2=0 on 34 products"}
for (s, t) in [(3, 50), (2, 50), (4, 51), (3, 51), (5, 51)]:
    A0, A1, M = dense(s, t)
    R, piv, rk = gf_rref_rank(M)
    n = M.shape[1]
    free = [c for c in range(n) if c not in piv]
    K = []
    for f in free:
        v = np.zeros(n, dtype=int); v[f] = 1
        for c, rr in piv.items():
            v[c] = (-R[rr, f]) % 5
        K.append([int(x) for x in v])
    out["C(%d,%d)" % (s, t)] = {
        "dim_domain": int(M.shape[1]), "dim_target": int(M.shape[0]),
        "rank_d": int(rk), "ker_dim": int(n-rk),
        "domain_basis": [fmt_elt(tup, c) for (tup, c) in A0],
        "kernel_basis": K}
# image membership for (3,50) kernel vecs in im(d: C^2->C^3)
_, _, Dp = dense(2, 50)
_, _, Dn = dense(3, 50)
R0, p0, rk0 = gf_rref_rank(Dp)
K = out["C(3,50)"]["kernel_basis"]
mem = []
for v in K:
    Aug = np.concatenate([Dp, np.array(v).reshape(-1, 1)], axis=1)
    _, _, rka = gf_rref_rank(Aug)
    mem.append(bool(rka == rk0))
out["C(3,50)"]["in_image_of_d2prev"] = mem
with open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-705/output/artifacts/cell_3_50.json', 'w') as f:
    json.dump(out, f, indent=1)
print("wrote cell_3_50.json; mem:", mem)
