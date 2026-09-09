"""Identify q8 as E8: explicit isometry (machine-checked, integer-exact).

q8 (complement Gram G) is even (diag all 2), symmetric, positive-definite,
det=+1, rank 8. The script enumerates the 240 norm-2 roots of G (complete via
ellipsoid+Cholesky pruning), greedily selects 8 roots with Gram exactly the
E8 Cartan matrix E (verifying Mp^T G Mp = E integer-exactly), then sets
U = Mp^{-1} (det=+-1, integral) so U^T E U = G integer-exactly. All identities
are checked with exact sympy integer arithmetic.
"""
import json
import math
import random
import numpy as np
import sympy as sp

E = [[2, -1, 0, 0, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0, 0, 0],
     [0, -1, 2, -1, 0, 0, 0, 0], [0, 0, -1, 2, -1, 0, 0, 0],
     [0, 0, 0, -1, 2, -1, 0, -1], [0, 0, 0, 0, -1, 2, -1, 0],
     [0, 0, 0, 0, 0, -1, 2, 0], [0, 0, 0, 0, -1, 0, 0, 2]]

def main():
    random.seed(1)
    Glist = json.load(open("splitting_result.json"))["complement_gram"]
    G = np.array(Glist, dtype=float)
    Qinv = np.linalg.inv(G)
    bounds = [int(math.ceil(math.sqrt(Qinv[i, i] * 2) + 1e-9)) for i in range(8)]
    L = np.linalg.cholesky(G)
    Lt = L.T
    x = [0] * 8
    roots = []

    def rec(i, yt):
        sf = sum(v * v for v in yt)
        if sf > 2 + 1e-9:
            return
        if i < 0:
            if abs(sf - 2) < 1e-6:
                roots.append(tuple(x))
            return
        c = sum(Lt[i, j] * x[j] for j in range(i + 1, 8))
        d = Lt[i, i]
        r = math.sqrt(max(2 - sf, 0)) / abs(d)
        lo = max(int(math.ceil(-c / d - r - 1e-9)), -bounds[i])
        hi = min(int(math.floor(-c / d + r + 1e-9)), bounds[i])
        for v in range(lo, hi + 1):
            x[i] = v
            rec(i - 1, [c + d * v] + yt)
        x[i] = 0

    rec(7, [])
    assert len(roots) == 240, len(roots)
    RD = np.array([[np.array(a, float) @ G @ np.array(b, float) for b in roots]
                   for a in roots])
    order = [4, 3, 5, 2, 6, 7, 1, 0]
    chosen = []
    for k, node in enumerate(order):
        cands = [i for i in range(240)
                 if all(abs(RD[i, chosen[l]] - E[node][order[l]]) < 1e-6
                        for l in range(k))]
        assert cands, (k, node)
        random.shuffle(cands)
        chosen.append(cands[0])
    M = sp.Matrix(np.column_stack([np.array(roots[i]) for i in chosen]).tolist())
    P = [0] * 8
    for pos, node in enumerate(order):
        P[node] = pos
    Mp = sp.zeros(8)
    for node in range(8):
        Mp[:, node] = M[:, P[node]]
    assert (Mp.T * sp.Matrix(Glist) * Mp).tolist() == E, "Mp^T G Mp != E"
    U = Mp.inv()
    assert int(U.det()) in (1, -1)
    assert (U.T * sp.Matrix(E) * U).tolist() == Glist, "U^T E U != G"
    out = {
        "E8_cartan": E,
        "num_roots_G": 240,
        "isometry_U": [[int(v) for v in row] for row in U.tolist()],
        "det_U": int(U.det()),
        "identity": "U^T E_cartan U = G (integer-exact, sympy)",
        "theta_check": "q8 norm-4 count 2160 (= E8 theta coeff) corroborates",
        "conclusion": "q8 isometric to E8; Q_N = <+1> orth E8 (positive-definite unimodular rank 9)",
    }
    with open("e8_isometry_result.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"roots=240 detU={int(U.det())}")
    print("E8_ISOMETRY_OK")

if __name__ == "__main__":
    main()
