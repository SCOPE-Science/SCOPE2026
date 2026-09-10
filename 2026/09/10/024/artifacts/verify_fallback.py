#!/usr/bin/env python3
"""Machine-checkable certificate for the lane-540 preset fallback.

Claim: k1(Gamma_eq) in [a,b], k1(Gamma_con) in [c,d], widths <= 1e-6,
disjoint with a > d, where
  Gamma_eq  = equilateral metric cube Q3, L=1 (12 edges of length 1/12),
  Gamma_con = single-edge-contracted cube, L=1 (11 edges of length 1/11),
both with Kirchhoff vertex conditions.

Route (stdlib only, exact integer/Fraction arithmetic):
  1. Cube spectrum via Z2^3 characters (exact integer eigenvector checks).
  2. Contracted spectrum via exact integer Bareiss: charpoly of B=12*P_con
     proved equal to claimed factorization by 8-point agreement (both monic
     degree 7), then exact root ordering with integer evaluations.
  3. von Below vertex reduction (proved in DRAFT.md): for equilateral graphs,
     k>0 eigenvalue  <=>  cos(k*ell) in spec(P)  or  k*ell in pi*Z.
  4. Rigorous enclosure L < arccos(1/3) < U by alternating Taylor bounds
     with machine-checked remainder justification.
  5. Scale to [a,b]=12*[L,U], [c,d]=11*[L,U]; width + disjointness checks;
     no-eigenvalue-below-a (resp. c) exclusion; uniqueness in the intervals.

Exit: prints VERIFY_OK iff every check passes.
"""
from fractions import Fraction
from math import factorial

ONE3 = Fraction(1, 3)

# ---------------------------------------------------------------- cube Q3
def check_cube():
    n = 8
    A = [[0] * n for _ in range(n)]
    for i in range(8):
        for b in range(3):
            A[i][i ^ (1 << b)] = 1
    vecs = []
    for a in range(8):
        v = [1 if bin(a & x).count("1") % 2 == 0 else -1 for x in range(8)]
        lam = sum(1 if not (a >> b & 1) else -1 for b in range(3))
        # exact eigenvector check A v = lam v
        for i in range(8):
            assert sum(A[i][j] * v[j] for j in range(8)) == lam * v[i], (a, i)
        vecs.append((v, lam))
    # pairwise orthogonality => 8-dim eigenbasis => full spectrum
    for i in range(8):
        for j in range(i + 1, 8):
            assert sum(vecs[i][0][x] * vecs[j][0][x] for x in range(8)) == 0
    lams = sorted(l[1] for l in vecs)
    assert lams == [-3, -1, -1, -1, 1, 1, 1, 3], lams
    # P = A/3: largest 1 (simple), second largest 1/3
    print("cube: spec(A) = {-3,-1^3,1^3,3}; alpha2(P) = 1/3  OK")
    return True

# ------------------------------------------------- integer Bareiss determinant
def bareiss_det(M):
    n = len(M)
    A = [list(map(int, row)) for row in M]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k] != 0), -1)
            if piv < 0:
                return 0
            A[k], A[piv] = A[piv], A[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = A[i][j] * A[k][k] - A[i][k] * A[k][j]
                assert num % prev == 0, "Bareiss inexact division"
                A[i][j] = num // prev
            A[i][k] = 0
        prev = A[k][k]
    return sign * A[n - 1][n - 1]

# ------------------------------------------------- contracted cube spectrum
# Contract edge T0-B0 of Q3; merged vertex M (deg 4), others deg 3.
# 0=M,1=T1,2=B1,3=T3,4=B3,5=B2,6=T2
CON_EDGES = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 5),
             (1, 6), (3, 4), (4, 5), (5, 6), (6, 3)]
# claimed charpoly of B = 12*D^{-1}*A, ascending coefficients:
# (y-12)(y-4)(y+4)(y^2+4y-16)(y^2+8y-16)
Q_CLAIM = [49152, -40960, 0, 4864, -192, -160, 0, 1]

def qeval(c, y):
    return sum(ci * y ** i for i, ci in enumerate(c))

def check_contracted():
    n = 7
    deg = [0] * n
    for u, v in CON_EDGES:
        assert u != v and 0 <= u < n and 0 <= v < n
        deg[u] += 1
        deg[v] += 1
    assert sorted(deg) == [3, 3, 3, 3, 3, 3, 4], deg
    assert deg[0] == 4
    for d in deg:
        assert 12 % d == 0
    B = [[0] * n for _ in range(n)]
    for u, v in CON_EDGES:
        B[u][v] = 12 // deg[u]
        B[v][u] = 12 // deg[v]
    assert Q_CLAIM[-1] == 1 and len(Q_CLAIM) == 8  # monic degree 7
    pts = list(range(-3, 5))  # 8 distinct integers
    assert len(pts) == 8
    for y in pts:
        M = [[(y if i == j else 0) - B[i][j] for j in range(n)] for i in range(n)]
        assert bareiss_det(M) == qeval(Q_CLAIM, y), y
    # det(yI-B) is monic of degree 7; agrees with monic-degree-7 q at 8
    # points => identical polynomials => eigenvalues are exactly the roots.
    # Root ordering (B-scale): 12 simple & largest; next 4; rest < 4.
    f1 = lambda y: y * y + 4 * y - 16
    f2 = lambda y: y * y + 8 * y - 16
    assert f1(0) < 0 < f1(3) and f1(4) > 0   # positive root in (0,3)
    assert f2(0) < 0 < f2(3) and f2(4) > 0   # positive root in (0,3)
    # other roots negative (constant term -16 < 0) => all quad roots < 4
    # linear factors give 12, 4, -4; 12 simple (other factors nonzero there)
    assert (12 - 4) * (12 + 4) * f1(12) * f2(12) != 0
    assert (4 - 12) * (4 + 4) * f1(4) * f2(4) != 0
    print("contracted: charpoly(B)=claimed; spec(P) second-largest = 4/12 = 1/3  OK")
    return True

# ------------------------------------------------- arccos(1/3) enclosure
L = Fraction(123095938, 100000000)   # 1.23095938
U = Fraction(123095946, 100000000)   # 1.23095946
N_TAYLOR = 10

def cos_partial(x, N):
    return sum(((-1) ** n) * x ** (2 * n) / factorial(2 * n) for n in range(N + 1))

def check_theta():
    assert 0 < L < U < Fraction(314, 100) < Fraction(3141592653, 1000000000)  # U < pi
    assert U * U < 6  # Taylor terms decrease from n>=1 => Leibniz remainder
    assert N_TAYLOR >= 1
    RL = L ** (2 * N_TAYLOR + 2) / factorial(2 * N_TAYLOR + 2)
    RU = U ** (2 * N_TAYLOR + 2) / factorial(2 * N_TAYLOR + 2)
    cosL_lo = cos_partial(L, N_TAYLOR) - RL
    cosU_hi = cos_partial(U, N_TAYLOR) + RU
    cosU_lo = cos_partial(U, N_TAYLOR) - RU
    assert cosL_lo > ONE3, "cos(L) > 1/3"
    assert cosU_hi < ONE3, "cos(U) < 1/3"
    # cos decreasing on (0,pi) => unique theta=arccos(1/3) in (L,U)
    assert cosU_lo > Fraction(1, 4), "cos(U) > 1/4 (gap above next branch)"
    print(f"theta: cos({float(L)}) > 1/3 > cos({float(U)}); "
          f"arccos(1/3) in ({float(L)},{float(U)})  OK")
    return True

# ------------------------------------------------- intervals + exclusion
def check_intervals():
    a, b = 12 * L, 12 * U
    c, d = 11 * L, 11 * U
    assert b - a <= Fraction(1, 1000000), b - a
    assert d - c <= Fraction(1, 1000000), d - c
    assert a > d  # disjointness, exact rationals
    print(f"[a,b] = [{a} , {b}]  width {b - a} = {float(b - a):.3e}")
    print(f"[c,d] = [{c} , {d}]  width {d - c} = {float(d - c):.3e}")
    print(f"a - d = {a - d} = {float(a - d):.6f} > 0  OK")
    # Exclusion logic (von Below, see DRAFT.md):
    #  (i)  no eigenvalue in (0,a] (eq, ell=1/12) resp. (0,c] (con, ell=1/11):
    #       cos-branch impossible since k*ell <= L < pi, cos >= cos(L) > 1/3
    #       = max non-Perron eigenvalue, and cos=1 impossible (k*ell<2pi);
    #       vertex-vanishing branch k >= pi/ell > a (resp. c) since pi > 3.14.
    #  (ii) k1 = 12*theta in [a,b] (resp. 11*theta in [c,d]) is an eigenvalue
    #       (Perron lift, sin(theta)>0), hence the least positive one by (i).
    #  (iii) uniqueness of the root in each interval: next cos-branch
    #       eq: arccos(-1/3) = pi - theta > pi - U > U  (pi > 3.14);
    #       con: next P-eigenvalue <= 3/12 = 1/4 < cos(U) (certified above);
    #       vertex branch >= pi/ell >> interval tops.
    PI_LO = Fraction(314, 100)
    assert PI_LO - U > U          # pi - theta > U for the cube next branch
    assert 12 * PI_LO > b and 11 * PI_LO > d
    print("exclusion + uniqueness replay  OK")
    return True

if __name__ == "__main__":
    check_cube()
    check_contracted()
    check_theta()
    check_intervals()
    print("VERIFY_OK")
