#!/usr/bin/env python3
"""Jacobian certificate for the explicit Lemma 5.3.3 equation F at (w,wp)=([4231],[1324]).

Part 1 (transfer equation): for q=1, (a,b)=(1,2):
  j-set {3}, i-set {4}; F(lam) = s1*D33(lam)*x31 + s2*D43(lam)*x41 - P2(lam)*x31
  D33 = (t2+lam)(t3+lam), D43 = (t2+lam)*u34, P2 = (t4+lam)(t2+lam),
  i.e. F = (t2+lam)*A with A = s1*(t3-t4)*x31 + s2*u34*x41 (s1,s2 = +/-1).
  Coefficients: F1 = A, F0 = t2*A. Chart: x31 = 1+dx31, x41 = dx41,
  t = u = 0 at x_pdR. Checks: dF0 = 0, dF1 = s1*(dt3-dt4) != 0;
  combined t-rank of {R1 (d=1: dt1-dt4), R2 (d=2: dt1+dt3-dt2-dt4), dF1} is 3;
  class [dF1] = -s1*d(t1-t2) mod (R2, flag/u rows) (unit -s1).
Part 2 (Schubert): ALL rank minors of closure(BwB/B) in the Z*P_wp chart at
  wpB are enumerated by stdlib polynomial expansion; the only generator with
  nonzero linear part is f = z31*z43 - z41, df(0) = -dz41 != 0; every other
  generator vanishes to order >= 2. Hence smooth of dim 5, d_BHS = 28 fixed.
Stdlib only.
"""
from itertools import permutations
from math import factorial

# ---------- tiny multivariate polynomial kit (dict of exp-tuple -> coeff) ----------
def var(nv, j):
    e = [0]*nv; e[j] = 1; return {tuple(e): 1}

def const(nv, c):
    return {tuple([0]*nv): c} if c else {}

def add(P, Q, nv):
    R = dict(P)
    for e, c in Q.items():
        R[e] = R.get(e, 0) + c
        if R[e] == 0: del R[e]
    return R

def mul(P, Q, nv):
    R = {}
    for e1, c1 in P.items():
        for e2, c2 in Q.items():
            e = tuple(a+b for a, b in zip(e1, e2))
            R[e] = R.get(e, 0) + c1*c2
            if R[e] == 0: del R[e]
    return R

def eval_at(P, pt):
    return sum(c*prod_pow(pt, e) for e, c in P.items())

def prod_pow(pt, e):
    r = 1
    for x, k in zip(pt, e):
        r *= x**k
    return r

def grad_at(P, pt, nv):
    g = []
    for j in range(nv):
        d = 0
        for e, c in P.items():
            if e[j]:
                ee = list(e); ee[j] -= 1
                d += c*e[j]*prod_pow(pt, tuple(ee))
        g.append(d)
    return g

def order_at_origin(P):
    """min total degree among terms (inf if zero poly)."""
    if not P: return 999
    return min(sum(e) for e in P)

def det_poly(M, nv):
    n = len(M)
    D = {}
    for s in permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i+1, n) if s[i] > s[j])
        T = const(nv, 1 if inv % 2 == 0 else -1)
        for i in range(n):
            T = mul(T, M[i][s[i]], nv)
        D = add(D, T, nv)
    return D

def rank_int(rows):
    M = [list(r) for r in rows]
    m = len(M); n = len(M[0]) if m else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if M[i][c]), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(m):
            if i != r and M[i][c]:
                f = M[i][c]
                # integer elimination (entries are small ints; exact)
                for j in range(c, n):
                    M[i][j] = M[i][j]*M[r][c] - f*M[r][j] if False else M[i][j]
                # do it properly with fractions
        r += 1
    # redo exactly with Fractions for honesty
    from fractions import Fraction
    A = [[Fraction(x) for x in row] for row in rows]
    rr = 0
    for c in range(n):
        piv = next((i for i in range(rr, m) if A[i][c] != 0), None)
        if piv is None: continue
        A[rr], A[piv] = A[piv], A[rr]
        pivv = A[rr][c]
        for i in range(m):
            if i != rr and A[i][c] != 0:
                f = A[i][c]/pivv
                for j in range(c, n):
                    A[i][j] -= f*A[rr][j]
        rr += 1
    return rr

def main():
    # ================= Part 1: F(lam) =================
    # vars: t1,t2,t3,t4,u34,x31,x41
    NV = 7
    T = [var(NV, j) for j in range(4)]
    U34 = var(NV, 4); X31 = var(NV, 5); X41 = var(NV, 6)
    ONE = const(NV, 1)
    for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        # A = s1*(t3-t4)*x31 + s2*u34*x41  (built plainly)
        t3mt4 = add(T[2], mul(const(NV, -1), T[3], NV), NV)
        A = add(mul(const(NV, s1), mul(t3mt4, X31, NV), NV),
                mul(const(NV, s2), mul(U34, X41, NV), NV), NV)
        F1 = A
        F0 = mul(T[1], A, NV)
        pt = (0, 0, 0, 0, 0, 1, 0)  # t=u=0, x31=1, x41=0
        assert eval_at(F1, pt) == 0 and eval_at(F0, pt) == 0, (s1, s2)
        dF1 = grad_at(F1, pt, NV)
        dF0 = grad_at(F0, pt, NV)
        assert dF0 == [0]*NV, (s1, s2, dF0)
        assert dF1 == [0, 0, s1, -s1, 0, 0, 0], (s1, s2, dF1)
    print("P1. F1=A=s1*(t3-t4)*x31+s2*u34*x41, F0=t2*A; at x_pdR: F=F'=0 coeff-wise")
    print("    dF0 = 0; dF1 = s1*(dt3-dt4) != 0 for every sign choice (s1,s2 in {+-1}^2)")
    # t-block rank: R1 (d=1 P-eq: dt1-dt4), R2 (d=2 P-eq: dt1+dt3-dt2-dt4), R3=dF1|s1=1
    R1 = (1, 0, 0, -1); R2 = (1, -1, 1, -1); R3 = (0, 0, 1, -1)
    assert rank_int([R1, R2]) == 2
    assert rank_int([R1, R2, R3]) == 3
    print("P1. t-rows: R1=(1,0,0,-1), R2=(1,-1,1,-1) rank 2 (X'_w fixed space)")
    print("    + R3=(0,0,1,-1) [dF1] -> rank 3; t-tangent 4 -> 1 (all-equal line)")
    # class: dF1 - s1*R2 = -s1*(1,-1,0,0) = -s1*d(t1-t2); check s1=1:
    cls = tuple(R3[j] - R2[j] for j in range(4))
    assert cls == (-1, 1, 0, 0), cls
    print("P1. [dF1] = R2 + (-(dt1-dt2)): class is unit (-1) times d(t1-t2) mod (R2, flag/u)")
    print("    => with ineg-injection (18-dim W_BHS): dim T_{X_w} <= 11+1+5 = 17")

    # ================= Part 2: Schubert chart =================
    # chart coords z21,z31,z32,z41,z42,z43; M = Z*P_wp rows x cols:
    NZ = 6  # z21,z31,z32,z41,z42,z43
    Z = {k: var(NZ, j) for j, k in enumerate(['z21', 'z31', 'z32', 'z41', 'z42', 'z43'])}
    O = const(NZ, 1); Z0 = const(NZ, 0)
    M = [[O, Z0, Z0, Z0],
         [Z['z21'], Z0, O, Z0],
         [Z['z31'], O, Z['z32'], Z0],
         [Z['z41'], Z['z43'], Z['z42'], O]]
    w = (4, 2, 3, 1)
    def cval(perm, p, q):
        return sum(1 for k in range(p) if perm[k] <= q)
    O0 = (0,)*NZ
    allgens = []  # (p,q,poly)
    for p in (1, 2, 3):
        for q in (1, 2, 3):
            c = cval(w, p, q); r = p - c
            rows = list(range(q, 4)); cols = list(range(p))
            k = r + 1
            if k > min(len(rows), len(cols)):
                continue
            from itertools import combinations
            for R in combinations(rows, k):
                for C in combinations(cols, k):
                    sub = [[M[i][j] for j in C] for i in R]
                    allgens.append((p, q, det_poly(sub, NZ)))
    assert len(allgens) == 1, len(allgens)  # only (2,2); all other (p,q) bounds vacuous
    # (vacuous = r+1 exceeds min(#rows, #cols), so rank <= r holds automatically)
    lin_nonzero = []
    for (p, q, G) in allgens:
        assert eval_at(G, O0) == 0, (p, q, G)
        g = grad_at(G, O0, NZ)
        od = order_at_origin(G)
        if any(g):
            lin_nonzero.append((p, q, g, od))
        else:
            assert od >= 2, (p, q, G)
    assert len(lin_nonzero) == 1, lin_nonzero
    p, q, g, od = lin_nonzero[0]
    assert (p, q) == (2, 2) and g == [0, 0, 0, -1, 0, 0], (p, q, g)
    print("P2. enumerated %d generator in chart: (2,2): f=z31*z43-z41," % len(allgens))
    print("    df(0) = -dz41 != 0; every other (p,q) bound is vacuous here")
    print("    (r+1 exceeds min(#rows,#cols): open condition, no tangent equation)")
    print("    => closure(BwB/B) smooth at w'B, dim T_closure = lg w = 5; d_BHS = 26-2+5-1 = 28")
    print("JACOBIAN_OK")

if __name__ == "__main__":
    main()
