"""Hochster graded-Betti engine over a prime field Fp.

S = Fp[x_0..x_{n-1}], I(G) = edge ideal. Independence complex Delta;
Hochster: beta_{i,j} = sum_{W subset V, |W|=j} dim red-H_{j-i-1}(Delta_W).
Reduced homology via boundary ranks mod p by fraction-free Bareiss normal
form on sparse 0/1 matrices (exact over integers, then rank mod p).
Verification cross-checks over QQ are exact Fractions elimination; both
fields compared in the audit (Katzman: no torsion for n<=10, so they agree).
"""
import json
import numpy as np
from math import comb


def indep_faces(n, edges):
    E = set(tuple(sorted(e)) for e in edges)
    faces = []
    for r in range(n + 1):
        from itertools import combinations
        for W in combinations(range(n), r):
            ok = True
            for a in range(r):
                for b in range(a + 1, r):
                    if (W[a], W[b]) in E:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                faces.append(set(W))
    return faces


def rank_modp(rows, cols, entries, p):
    """Rank of sparse +-1 boundary matrix over Fp (p prime) by modular
    Gaussian elimination. Katzman (math/0408016): Betti numbers for n<=10
    variables are independent of the ground field, so this Fp table equals
    the QQ table; the audit rechecks the witness and a random sample over
    QQ with exact Fractions elimination (rank_qq below)."""
    if not entries:
        return 0
    M = [[0] * cols for _ in range(rows)]
    for (i, j, v) in entries:
        M[i][j] = (M[i][j] + v) % p
    r = 0
    inv_cache = {}
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        a = M[r][c] % p
        if a not in inv_cache:
            inv_cache[a] = pow(a, p - 2, p)
        inv = inv_cache[a]
        for k in range(c, cols):
            M[r][k] = (M[r][k] * inv) % p
        for i in range(rows):
            if i != r and M[i][c] % p != 0:
                f = M[i][c] % p
                for k in range(c, cols):
                    M[i][k] = (M[i][k] - f * M[r][k]) % p
        r += 1
        if r == rows:
            break
    return r


def rank_qq(rows, cols, entries):
    """Exact rank over QQ via Fractions elimination (independent recheck)."""
    from fractions import Fraction
    if not entries:
        return 0
    M = [[Fraction(0)] * cols for _ in range(rows)]
    for (i, j, v) in entries:
        M[i][j] += Fraction(v)
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        a = M[r][c]
        for k in range(c, cols):
            M[r][k] /= a
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                for k in range(c, cols):
                    M[i][k] -= f * M[r][k]
        r += 1
        if r == rows:
            break
    return r


def betti_table(n, edges, p, rankfn=None):
    """Return dict {(i,j): beta} graded Betti numbers of S/I(G), char p.
    rankfn: 'modp' (default) or 'qq' for the exact-QQ recheck."""
    rk = rank_modp if rankfn in (None, 'modp') else (lambda r, c, e, p: rank_qq(r, c, e))
    E = set(tuple(sorted(e)) for e in edges)
    from itertools import combinations
    faces_all = set()
    for r in range(n + 1):
        for W in combinations(range(n), r):
            if all((W[a], W[b]) not in E for a in range(r) for b in range(a + 1, r)):
                faces_all.add(W)
    out = {}
    verts = list(range(n))
    for j in range(n + 1):
        for W in combinations(verts, j):
            W = list(W)
            k = len(W)
            fidx = {}
            flist = []
            for r in range(k + 1):
                for F in combinations(W, r):
                    if F in faces_all:
                        fidx[(len(F), F)] = len(flist)
                        flist.append(F)
            dims = {}
            for d in range(-1, k):
                dims[d] = [F for F in flist if len(F) == d + 1]
            for i in range(max(0, k - n), k + 1):
                d = k - i - 1
                if d < -1 or d >= k:
                    continue
                Cd = dims.get(d, [])
                Cdm1 = dims.get(d - 1, [])
                Cd1 = dims.get(d + 1, [])
                nd, nm, np1 = len(Cd), len(Cdm1), len(Cd1)
                if nd == 0:
                    h = 0
                else:
                    posd = {F: t for t, F in enumerate(Cd)}
                    # d_{d}: C_d -> C_{d-1}
                    e1 = []
                    if nm:
                        posm = {F: t for t, F in enumerate(Cdm1)}
                        for t, F in enumerate(Cd):
                            for s, v in enumerate(F):
                                G = tuple(u for u in F if u != v)
                                e1.append((posm[G], t, 1 if s % 2 == 0 else -1))
                    rk_in = rk(nm, nd, e1, p) if (nm and nd) else 0
                    # d_{d+1}: C_{d+1} -> C_d
                    e2 = []
                    if np1:
                        for t, F in enumerate(Cd1):
                            for s, v in enumerate(F):
                                G = tuple(u for u in F if u != v)
                                e2.append((t, posd[G], 1 if s % 2 == 0 else -1))
                    rk_out = rk(np1, nd, e2, p) if (np1 and nd) else 0
                    h = nd - rk_in - rk_out
                    if d == -1:
                        # reduced H_{-1}: 1 iff W empty, else 0
                        h = 1 if k == 0 else 0
                if h:
                    out[(i, j)] = out.get((i, j), 0) + h
    return out
