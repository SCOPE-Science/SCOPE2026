"""Splitting Q_N = <+1> orth q8 (machine-checked, integer-exact).

v0 = (6,3,4,2,5,4,3,2,1): v0^2=+1 (integer-exact), Q_N v0 = e8 = (0,...,0,1),
so v0 is primitive (gcd of Qv0-coords = 1). The Q-orthogonal complement is
{x : v0^T Q x = 0} = {x : x_8 = 0} = span(e0..e7), with Gram G = QN[:8,:8]:
det(G)=+1 (integer-exact), positive-definite sig=+8 (eigs>0). Hence
Q_N = <+1> orth q8 with q8 unimodular positive-definite rank 8, det=+1.
Characteristic parity: K char iff K_8 odd (diag(QN) = (0,...,0,1) mod 2 ...
verified); the c5-cap sphere pairing K.S_c5 = K_8 is hence odd for every char
K, forcing adjunction RHS>=3+1=4 (margin>=6) uniformly.
"""
import json
import numpy as np
import sympy as sp

def main():
    P = json.load(open("plumbing_result.json"))
    QN = sp.Matrix(P["QN"])
    n = 9
    v0 = sp.Matrix([6, 3, 4, 2, 5, 4, 3, 2, 1])
    v0sq = int((v0.T * QN * v0)[0])
    assert v0sq == 1, v0sq
    w = QN * v0
    wlist = [int(a) for a in w]
    assert wlist == [0] * 8 + [1], wlist
    import math
    g = 0
    for a in wlist:
        g = math.gcd(g, a)
    assert g == 1  # primitive
    G = QN[:8, :8]
    detG = int(G.det())
    assert detG == 1, detG
    evG = np.linalg.eigvalsh(np.array(G.tolist(), dtype=float))
    assert all(x > 1e-9 for x in evG), evG
    diag = [int(QN[i, i]) % 2 for i in range(n)]
    assert diag == [0] * 8 + [1], diag
    out = {
        "v0": [int(a) for a in v0],
        "v0_square": int(v0sq),
        "Qv0": wlist,
        "primitive_gcd": g,
        "complement_basis": "e0..e7 (since v0^T Q x = x_8)",
        "complement_gram": [[int(v) for v in row] for row in G.tolist()],
        "det_complement": detG,
        "eig_complement": [float(x) for x in sorted(evG)],
        "sig_complement": 8,
        "splitting": "Q_N = <+1> orth q8, q8 positive-definite unimodular rank 8 det=+1",
        "char_parity": diag,
        "parity_margin": "every char K has K_8 odd => |K.S_c5|>=1 => adjunction RHS>=4 (LHS=-2): uniform kill",
    }
    with open("splitting_result.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"v0^2={v0sq} Qv0=e8 primitive detG={detG} sig=+8")
    print("SPLITTING_OK")

if __name__ == "__main__":
    main()
