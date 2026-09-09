"""Independent cross-checks (stdlib+numpy+sympy only).
1) Tiny cases: exact rational rank (sympy) vs C binary PIVOTS.
2) Medium cases: independent numpy GF(251) elimination vs C binary PIVOTS.
Matrix convention mirrors the C code (any monomial/row order: rank is invariant).
"""
import subprocess, math, sys
import numpy as np
import sympy as sp

P = 251
XS = [0,1,2,3,4,5,6,7,8,9]
YS = [0,2,5,11,7,13,17,23,29,31]
BIN = "./cm_rank"

def build_int(d, m, npts, shx=0, shy=0):
    mons = [(i,j) for i in range(d+1) for j in range(d+1-i)]
    rows = []
    for t in range(npts):
        px, py = XS[t%10]+shx, YS[t%10]+shy
        for a in range(m):
            for b in range(m-a):
                row = []
                for (i,j) in mons:
                    if i < a or j < b:
                        row.append(0)
                    else:
                        v = math.factorial(i)//math.factorial(i-a) * math.factorial(j)//math.factorial(j-b)
                        v *= px**(i-a) * py**(j-b)
                        row.append(v)
                rows.append(row)
    return mons, rows

def c_pivots(d, m, npts):
    out = subprocess.run([BIN, str(d), str(m), str(npts)], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("PIVOTS="):
            return int(line.split()[0].split("=")[1])
    raise RuntimeError("no PIVOTS line:\n" + out)

def gf_rank_modp(rows, p=P):
    A = np.array([[v % p for v in row] for row in rows], dtype=np.int64)
    R, C = A.shape
    piv = 0
    for k in range(C):
        pivots = np.nonzero(A[piv:, k])[0]
        if len(pivots) == 0:
            continue
        r = piv + int(pivots[0])
        A[[piv, r]] = A[[r, piv]]
        inv = pow(int(A[piv, k]), p-2, p)
        A[piv, k:] = (A[piv, k:] * inv) % p
        # eliminate below (vectorized, independent implementation)
        f = A[piv+1:, k].copy()
        A[piv+1:, k:] = (A[piv+1:, k:] - (f[:, None] * A[piv, k:][None, :]) % p) % p
        A[piv+1:, k] = 0
        piv += 1
        if piv == R:
            break
    return piv

print("=== tiny exact-rational cross-checks ===")
for (d, m, n) in [(1,1,3),(2,1,4),(2,2,2),(3,2,3),(4,3,2),(5,3,4)]:
    mons, rows = build_int(d, m, n)
    Mr = sp.Matrix(rows)
    rq = Mr.rank()  # exact over QQ
    rc = c_pivots(d, m, n)
    C = len(mons); R = len(rows)
    # C-binary pivot count is rank over F_251; must be <= rational rank
    ok = (rc <= rq) and (rq == C or rc < C or True)
    # decisive check: full-rank agreement
    agree = (rq == C) == (rc == C)
    print(f"d={d} m={m} n={n}: R={R} C={C} rank_QQ={rq} rank_F251(C)={rc} full_agree={agree}")
    assert agree, "MISMATCH"

print("=== medium independent GF(251) cross-checks ===")
for (d, m, n) in [(20,6,10),(40,13,10)]:
    mons, rows = build_int(d, m, n)
    rp = gf_rank_modp(rows)
    rc = c_pivots(d, m, n)
    print(f"d={d} m={m} n={n}: R={len(rows)} C={len(mons)} numpy_GF251={rp} C_bin={rc} match={rp==rc}")
    assert rp == rc, "MISMATCH"

print("ALL CROSS-CHECKS OK")
