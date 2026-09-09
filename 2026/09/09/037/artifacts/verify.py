#!/usr/bin/env python3
"""Exact (disc, herdisc, detLB) census for canonical order-8 Sylvester Hadamard S8.
Stdlib only, exact integer arithmetic (Bareiss for determinants).
Reproduces: D=4, H=5, M_k table, detLB=4096^{1/8}=2*sqrt(2), R=5*sqrt(2)/4.
Writes: subset_table.csv, spectrum.json (into same dir as script).
"""
import itertools, json, csv, os

def kron(A, B):
    m, n, p, q = len(A), len(A[0]), len(B), len(B[0])
    C = [[0]*(n*q) for _ in range(m*p)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                for l in range(q):
                    C[i*p+k][j*q+l] = A[i][j]*B[k][l]
    return C

S1 = [[1,1],[1,-1]]
S8 = kron(kron(S1, S1), S1)
assert len(S8) == 8 and all(len(r) == 8 for r in S8)
# Hadamard check
for i in range(8):
    for j in range(8):
        assert sum(S8[i][k]*S8[j][k] for k in range(8)) == (8 if i == j else 0)

def disc_of_cols(M, J):
    k = len(J)
    best, bestx = None, None
    for bits in range(2**k):
        x = [1 if (bits >> j) & 1 else -1 for j in range(k)]
        mx = 0
        brk = False
        for i in range(8):
            s = sum(M[i][J[j]]*x[j] for j in range(k))
            a = abs(s)
            if a > mx:
                mx = a
                if best is not None and mx >= best:
                    brk = True
                    break
        if brk:
            continue
        if best is None or mx < best:
            best, bestx = mx, tuple(x)
    return best, bestx

def bareiss_det(M):
    n = len(M)
    if n == 0:
        return 1
    A = [row[:] for row in M]
    prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            piv = next((i for i in range(k+1, n) if A[i][k] != 0), None)
            if piv is None:
                return 0
            A[k], A[piv] = A[piv], A[k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = (A[i][j]*A[k][k] - A[i][k]*A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
        if prev == 0:
            return 0
    return A[n-1][n-1]

D, xD = disc_of_cols(S8, list(range(8)))

rows = []  # (mask, J, disc, x)
H, HJ, Hx = 0, None, None
for mask in range(1, 256):
    J = [j for j in range(8) if (mask >> j) & 1]
    d, x = disc_of_cols(S8, J)
    rows.append((mask, J, d, x))
    if d > H:
        H, HJ, Hx = d, tuple(J), x

Mk, att = {}, {}
count = 0
for k in range(1, 9):
    best, bestB = 0, None
    for rws in itertools.combinations(range(8), k):
        for cls in itertools.combinations(range(8), k):
            B = [[S8[r][c] for c in cls] for r in rws]
            d = abs(bareiss_det(B))
            count += 1
            if d > best:
                best, bestB = d, (rws, cls)
    Mk[k], att[k] = best, bestB

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "subset_table.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["mask", "columns_J", "disc", "attaining_signing"])
    for mask, J, d, x in rows:
        w.writerow([mask, ";".join(map(str, J)), d, ";".join(map(str, x))])
with open(os.path.join(here, "spectrum.json"), "w") as f:
    json.dump({"M_k": {str(k): Mk[k] for k in Mk},
               "attainers": {str(k): {"rows": list(att[k][0]), "cols": list(att[k][1])} for k in att},
               "submatrices_evaluated": count}, f, indent=1)

print(f"S8 committed matrix row0: {S8[0]}")
print(f"D=disc(S8)={D} attainer={xD}")
print(f"H=herdisc(S8)={H} J*={HJ} x*={Hx}")
print(f"M_k={Mk}")
print(f"submatrices evaluated: {count} (expect 12869 nonempty)")
print(f"detLB = 4096^(1/8) = 2*sqrt(2) ~= {4096**(1/8):.10f}")
print(f"R = 5*sqrt(2)/4 ~= {5*2**0.5/4:.10f}")
print("VERIFY_OK" if (D == 4 and H == 5 and Mk == {1:1,2:2,3:4,4:16,5:32,6:128,7:512,8:4096} and count == 12869) else "VERIFY_FAIL")
