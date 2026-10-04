#!/usr/bin/env python3
"""Numerical sanity checks for the four-vertex core used in the proof.

The theorem itself is proved analytically in RESULT.md.  This script only checks
finite-epsilon matrices, the limiting radicals, and the exact lift bookkeeping.
It uses only the Python standard library.
"""
import math


def jacobi_eigh(A, tol=1e-15, max_iter=10000):
    n = len(A)
    A = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_iter):
        p = q = 0
        best = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > best:
                    best = abs(A[i][j]); p, q = i, j
        if best < tol:
            break
        app, aqq, apq = A[p][p], A[q][q], A[p][q]
        phi = 0.5 * math.atan2(2.0 * apq, aqq - app)
        c, s = math.cos(phi), math.sin(phi)
        for k in range(n):
            if k != p and k != q:
                akp, akq = A[k][p], A[k][q]
                A[k][p] = A[p][k] = c * akp - s * akq
                A[k][q] = A[q][k] = s * akp + c * akq
        A[p][p] = c*c*app - 2*c*s*apq + s*s*aqq
        A[q][q] = s*s*app + 2*c*s*apq + c*c*aqq
        A[p][q] = A[q][p] = 0.0
        for k in range(n):
            vkp, vkq = V[k][p], V[k][q]
            V[k][p] = c*vkp - s*vkq
            V[k][q] = s*vkp + c*vkq
    else:
        raise RuntimeError("Jacobi iteration failed")
    vals = [A[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda i: vals[i])
    return [vals[i] for i in order], [[V[r][i] for i in order] for r in range(n)]


def core(eps):
    edges = [(0,1,eps), (0,2,1.0/eps), (0,3,1.0/3.0),
             (1,2,eps), (1,3,1.0), (2,3,eps*eps)]
    W = [[0.0]*4 for _ in range(4)]
    for i,j,w in edges:
        W[i][j] = W[j][i] = w
    d = [sum(row) for row in W]
    S = [[0.0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            S[i][j] = (1.0 if i == j else 0.0) - W[i][j]/math.sqrt(d[i]*d[j])
    vals, V = jacobi_eigh(S)
    x = [0.0, math.sqrt(d[1]), 0.0, 0.0]
    coeff = []
    for k,lam in enumerate(vals):
        dot = sum(V[r][k]*x[r] for r in range(4))
        coeff.append(0.0 if lam < 1e-10 else dot/math.sqrt(lam))
    h = [sum(V[r][k]*coeff[k] for k in range(4)) for r in range(4)]
    g = [h[i]/math.sqrt(d[i]) for i in range(4)]
    out = [g[i]-g[j] for i,j,_ in edges]
    weights = [w for _,_,w in edges]
    ratios = []
    for v in map(abs, out):
        mass = sum(w for w,z in zip(weights, map(abs,out)) if z >= v - 1e-11)
        ratios.append(v*mass/d[1])
    return d, vals, g, out, max(ratios)


def main():
    rt3 = math.sqrt(3.0)
    # Exact limiting 2x2 calculation: (1-r)^(-1/2)=sqrt(3)+1 and
    # (1+r)^(-1/2)=sqrt(3)-1 for r=sqrt(3)/2.
    r = rt3/2.0
    assert abs(1/math.sqrt(1-r) - (rt3+1)) < 2e-14
    assert abs(1/math.sqrt(1+r) - (rt3-1)) < 2e-14
    target_edges = [-rt3, 0.0, -rt3/2, rt3, rt3/2, -rt3/2]
    previous = 0.0
    rows = []
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        d, vals, g, out, ratio = core(eps)
        assert vals[1] > 0.12  # uniform positive spectral gap after the kernel
        err = max(abs(a-b) for a,b in zip(out,target_edges))
        assert ratio > previous
        previous = ratio
        rows.append((eps, ratio, err))
    assert abs(rows[-1][1] - 2/rt3) < 6e-5
    assert rows[-1][2] < 6e-5

    # Exact lift bookkeeping for e_k=2^{-|k|}: sum e_k=3, so sum a_k=6.
    sum_e = 1.0 + 2.0*sum(2.0**(-k) for k in range(1,80))
    A = 2.0*sum_e
    assert abs(sum_e - 3.0) < 1e-14 and abs(A - 6.0) < 2e-14
    tau = 1e-6
    penalty = 1/math.sqrt(1+tau)
    assert 0.999999 < penalty < 1.0

    print("VERIFY_OK")
    print("target_lower_bound=%.15f" % (2/rt3))
    for eps, ratio, err in rows:
        print("eps=%g weak_ratio=%.15f max_edge_limit_error=%.3e" % (eps, ratio, err))
    print("lift_sum_a=%.15f penalty_tau_1e-6=%.15f" % (A, penalty))

if __name__ == "__main__":
    main()
