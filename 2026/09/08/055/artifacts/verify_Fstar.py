"""Verifier for lane-205: F* = x0*u^3 + x1*v^3 + x2*(u+v)^3 + w^4 over Q.
Replays: (1) catalecticant ranks -> Hilbert vector (1,6,7,6,1);
(2) Hessian determinant identically zero (symbolic);
(3) WLP: L*=sum of vars gives full-rank A1->A2 (6) and A2->A3 (6) + nonzero minors;
(4) graded Betti table via Koszul-Tor with Euler checks.
Requires: sympy only. Runtime ~seconds.
"""
from itertools import combinations

import sympy as sp

N = 6  # variables (x0,x1,x2,u,v,w)


def monoms(k):
    res = []
    def rec(i, rem, cur):
        if i == N - 1:
            res.append(tuple(cur + [rem]))
            return
        for e in range(rem + 1):
            rec(i + 1, rem - e, cur + [e])
    rec(0, k, [])
    return res


def add_exp(a, b):
    return tuple(x + y for x, y in zip(a, b))


def unit(i):
    return tuple(1 if k == i else 0 for k in range(N))


F = {(1, 0, 0, 3, 0, 0): 1, (0, 1, 0, 0, 3, 0): 1, (0, 0, 1, 3, 0, 0): 1,
     (0, 0, 1, 2, 1, 0): 3, (0, 0, 1, 1, 2, 0): 3, (0, 0, 1, 0, 3, 0): 1,
     (0, 0, 0, 0, 0, 4): 1}


def deriv(m):
    out = {}
    for ex, c in F.items():
        if any(ex[i] < m[i] for i in range(N)):
            continue
        f = 1
        ne = []
        for i in range(N):
            for j in range(m[i]):
                f *= (ex[i] - j)
            ne.append(ex[i] - m[i])
        t = tuple(ne)
        out[t] = out.get(t, 0) + c * f
    return {k: v for k, v in out.items() if v != 0}


def catmat(k):
    Rk = monoms(k)
    Sk = monoms(4 - k)
    idx = {s: i for i, s in enumerate(Sk)}
    M = [[0] * len(Rk) for _ in Sk]
    for j, m in enumerate(Rk):
        for ex, c in deriv(m).items():
            M[idx[ex]][j] = c
    return Rk, sp.Matrix(M)


def main():
    # (1) Hilbert vector
    R, C = {}, {}
    h = []
    for k in range(5):
        R[k], C[k] = catmat(k)
        r = C[k].rank()
        h.append(r)
    print("Hilbert vector:", h)
    assert h == [1, 6, 7, 6, 1], h

    # (2) Hessian vanishes identically
    x0, x1, x2, u, v, w = sp.symbols('x0 x1 x2 u v w')
    Fp = x0 * u**3 + x1 * v**3 + x2 * (u + v)**3 + w**4
    det = sp.hessian(Fp, [x0, x1, x2, u, v, w]).det()
    print("Hessian det:", sp.expand(det))
    assert sp.expand(det) == 0

    # quotient bases + projectors
    piv, E, Ginv, prows, rimap = {}, {}, {}, {}, {}
    for k in range(5):
        _, p = C[k].rref()
        p = list(p)
        piv[k] = p
        E[k] = [R[k][i] for i in p]
        G = C[k].extract(list(range(C[k].rows)), p)
        pr = list(G.T.rref()[1])
        prows[k] = pr
        Ginv[k] = G.extract(list(pr), list(range(len(p)))).inv()
        rimap[k] = {m: i for i, m in enumerate(R[k])}
    assert [len(E[k]) for k in range(5)] == [1, 6, 7, 6, 1]

    def mulmat(k, L):
        cols = []
        for m in E[k]:
            qv = sp.zeros(len(R[k + 1]), 1)
            for i in range(N):
                qv[rimap[k + 1][add_exp(m, unit(i))]] += sp.Rational(L[i])
            b = (C[k + 1] * qv).extract(list(prows[k + 1]), [0])
            cols.append(list(Ginv[k + 1] * b))
        return sp.Matrix(cols).T

    # (3) WLP: L* full rank both mid maps + nonzero minor witnesses
    L = [1] * 6
    M12, M23 = mulmat(1, L), mulmat(2, L)
    print("rank A1->A2:", M12.rank(), "rank A2->A3:", M23.rank())
    assert M12.rank() == 6 and M23.rank() == 6
    d12 = M12.extract([0, 1, 2, 4, 5, 6], list(range(6))).det()
    d23 = M23.extract(list(range(6)), [0, 1, 2, 3, 4, 5]).det()
    print("witness minors:", d12, d23)
    assert d12 == 2 and d23 == 4

    # (4) Betti table via Koszul-Tor + Euler checks
    hh = {k: len(E[k]) for k in range(5)}
    mult = {}
    for k in range(4):
        for vi in range(N):
            cols = []
            for m in E[k]:
                qv = sp.zeros(len(R[k + 1]), 1)
                qv[rimap[k + 1][add_exp(m, unit(vi))]] = sp.Rational(1)
                b = (C[k + 1] * qv).extract(list(prows[k + 1]), [0])
                cols.append(list(Ginv[k + 1] * b))
            mult[(k, vi)] = sp.Matrix(cols).T
    # commutativity spot-check
    for k in (0, 1, 2):
        for i in range(N):
            for j in range(i + 1, N):
                assert (mult[(k + 1, j)] * mult[(k, i)]
                        - mult[(k + 1, i)] * mult[(k, j)]).is_zero_matrix
    from math import comb
    Hilb = [1, 6, 7, 6, 1]
    EXPECT = {0: [1, 0, 0, 0, 0, 0, 0], 1: [0] * 7,
              2: [0, 14, 0, 0, 0, 0, 0], 3: [0, 2, 36, 0, 0, 0, 0],
              4: [0, 4, 8, 39, 0, 0, 0], 5: [0, 0, 20, 12, 20, 0, 0],
              6: [0, 0, 0, 39, 8, 4, 0], 7: [0, 0, 0, 0, 36, 2, 0],
              8: [0, 0, 0, 0, 0, 14, 0], 9: [0] * 7, 10: [0, 0, 0, 0, 0, 0, 1]}

    def kdiff(i, t):
        Si = list(combinations(range(N), i))
        Sj = list(combinations(range(N), i - 1))
        pos = {s: r for r, s in enumerate(Sj)}
        hi, hj = hh.get(t - i, 0), hh.get(t - i + 1, 0)
        M = sp.zeros(len(Sj) * hj, len(Si) * hi)
        if hi == 0 or hj == 0:
            return M
        for c, s in enumerate(Si):
            for jp, vv in enumerate(s):
                T = tuple(x for x in s if x != vv)
                X = mult[(t - i, vv)]
                r = pos[T]
                for a in range(hi):
                    for b in range(hj):
                        M[r * hj + b, c * hi + a] += (-1) ** jp * X[b, a]
        return M

    for t in range(11):
        row = []
        for i in range(7):
            di = comb(6, i) * hh.get(t - i, 0)
            r_out = kdiff(i, t).rank() if i >= 1 and 0 <= t - i + 1 <= 4 else 0
            r_in = kdiff(i + 1, t).rank() if 0 <= t - i - 1 <= 4 else 0
            row.append(di - r_out - r_in)
        assert row == EXPECT[t], (t, row)
        e = sum((1 if i % 2 == 0 else -1) * row[i] for i in range(7))
        s = sum((1 if j % 2 == 0 else -1) * comb(6, j)
                * (Hilb[t - j] if 0 <= t - j <= 4 else 0) for j in range(7))
        assert e == s, (t, e, s)
        print(f"t={t}: {row} euler={e} OK")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
