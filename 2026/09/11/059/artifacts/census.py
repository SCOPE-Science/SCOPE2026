#!/usr/bin/env python3
"""Exact elliptic (genus-1) marked floor-diagram census: F0, beta = 3*D0 + 4*F.

Fixed conventions (verbatim, also in WORKLOG.md):
  X = F0 = P1 x P1, (h,d) = (3,4): 3 floors, 4 incoming + 4 outgoing
  unbounded edges (weight 1). v_l = (-1,0)x3, v_r = (1,0)x3, so the
  divergence condition is bounded_in - bounded_out = b_V - a_V at each vertex.
  n = 14 points; g_{Delta,n} = 14+1-14 = 1; bounded edges = 3.
  m_BG(D;q) = prod_{bounded E} [w_E]_q^2 (unbounded contribute [1]^2 = 1).
  #markings per class = #linear_extensions(rep) / |Aut(rep)| (free action;
  integrality asserted). G(q) = sum over marked iso classes of m_BG.

Weight solving is EXACT: incidence nullspace + congruence stepping over the
finite t-interval (finiteness asserted via mixed-sign null vector). No WMAX.
"""
import itertools
import json
from fractions import Fraction
from collections import Counter
from math import gcd, factorial

H = 3
DD = 4


def comps(n, k):
    if k == 1:
        yield (n,)
        return
    for i in range(n + 1):
        for r in comps(n - i, k - 1):
            yield (i,) + r


AC = list(comps(DD, H))
BC = list(comps(DD, H))

PAIRS = [(u, v) for u in range(H) for v in range(H) if u != v]


def gen_ms(items, k, start=0, cur=None):
    if cur is None:
        cur = []
    if k == 0:
        yield tuple(cur)
        return
    for i in range(start, len(items)):
        cur.append(items[i])
        yield from gen_ms(items, k - 1, i, cur)
        cur.pop()


def connected(ori):
    adj = [set() for _ in range(H)]
    for u, v in ori:
        adj[u].add(v)
        adj[v].add(u)
    seen = {0}
    st = [0]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                st.append(y)
    return len(seen) == H


def acyclic(ori):
    reach = [[False] * H for _ in range(H)]
    for u, v in ori:
        reach[u][v] = True
    for k in range(H):
        for i in range(H):
            for j in range(H):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True
    return not any(reach[i][i] for i in range(H))


ORI = [ms for ms in gen_ms(PAIRS, 3) if connected(ms) and acyclic(ms)]
print(f"labeled acyclic connected orientations (3 edges): {len(ORI)}", flush=True)


# ---------- exact rational nullspace of 3x3 incidence (no sympy needed) ------
def null_int(A):
    """Primitive integer null vector of 3x3 incidence A (rank 2)."""
    # null = cross product of two independent rows
    rows = A
    for i, j in ((0, 1), (0, 2), (1, 2)):
        r1, r2 = rows[i], rows[j]
        c = (r1[1] * r2[2] - r1[2] * r2[1],
             r1[2] * r2[0] - r1[0] * r2[2],
             r1[0] * r2[1] - r1[1] * r2[0])
        if any(c):
            g = 0
            for x in c:
                g = gcd(g, x)
            return tuple(x // g for x in c)
    raise AssertionError("rank < 2")


def particular(A, d):
    """Rational particular solution of A w = d using two independent rows."""
    for i, j in ((0, 1), (0, 2), (1, 2)):
        # solve rows i,j (2x3, rank 2): w = B' (B B')^{-1} rhs, rational
        B = [A[i], A[j]]
        rhs = [d[i], d[j]]
        # G = B B' (2x2), invert over Fractions
        G = [[sum(B[a][e] * B[b][e] for e in range(3)) for b in range(2)]
             for a in range(2)]
        det = G[0][0] * G[1][1] - G[0][1] * G[1][0]
        if det == 0:
            continue
        Ginv = [[Fraction(G[1][1], det), Fraction(-G[0][1], det)],
                [Fraction(-G[1][0], det), Fraction(G[0][0], det)]]
        y = [Ginv[a][0] * rhs[0] + Ginv[a][1] * rhs[1] for a in range(2)]
        w = [Fraction(B[0][e]) * y[0] + Fraction(B[1][e]) * y[1]
             for e in range(3)]
        if all(sum(Fraction(A[v][e]) * w[e] for e in range(3)) == d[v]
               for v in range(H)):
            return w
    raise AssertionError("d not in column space")


def ceil_frac(f):
    return -((-f.numerator) // f.denominator)


def floor_frac(f):
    return f.numerator // f.denominator


def solve_weights(ori, d):
    """All w in Z_{>=1}^3 with A(ori) w = d. Exact; asserts finiteness."""
    A = [[0] * 3 for _ in range(H)]
    for e, (u, v) in enumerate(ori):
        A[u][e] -= 1
        A[v][e] += 1
    n = null_int(A)
    assert any(x > 0 for x in n) and any(x < 0 for x in n), \
        f"null not mixed-sign: {ori} {n}"
    wp = particular(A, d)
    L = 1
    for x in wp:
        L = L * x.denominator // gcd(L, x.denominator)
    p = [int(x * L) for x in wp]
    # congruences s*n_e = -p_e (mod L); bounds from positivity
    s0, mod = 0, 1
    lo = None
    hi = None
    for e in range(3):
        ne = n[e]
        if ne == 0:
            if p[e] % L != 0 or p[e] // L < 1:
                return []
            continue
        g = gcd(abs(ne), L)
        if (-p[e]) % g != 0 and (p[e] % g) != 0:
            return []
        if p[e] % g != 0:
            return []
        Lp = L // g
        rhs = ((-p[e]) // g) % Lp
        inv = pow((ne // g) % Lp, -1, Lp)
        se = (rhs * inv) % Lp
        # merge s = s0 (mod) with s = se (mod Lp)
        g2 = gcd(mod, Lp)
        if (se - s0) % g2 != 0:
            return []
        l = mod // g2 * Lp
        s0 = (s0 + mod * ((((se - s0) // g2) *
                           pow((mod // g2) % (Lp // g2), -1, Lp // g2)) % (Lp // g2))) % l
        mod = l
        bnd = Fraction(L - p[e], ne)
        if ne > 0:
            c = ceil_frac(bnd)
            lo = c if lo is None else max(lo, c)
        else:
            c = floor_frac(bnd)
            hi = c if hi is None else min(hi, c)
    if lo is None:
        raise AssertionError("t unbounded below")
    if hi is None:
        raise AssertionError("t unbounded above")
    if lo > hi:
        return []
    k0 = ceil_frac(Fraction(lo - s0, mod))
    k1 = floor_frac(Fraction(hi - s0, mod))
    sols = []
    seen = set()
    for k in range(k0, k1 + 1):
        s = s0 + k * mod
        w = tuple((p[e] + s * n[e]) // L for e in range(3))
        assert all(x >= 1 for x in w)
        assert all(sum(A[v][e] * w[e] for e in range(3)) == d[v]
                   for v in range(H))
        # canonical wrt permuting weights among identical parallel pairs
        groups = {}
        for e, pr in enumerate(ori):
            groups.setdefault(pr, []).append(w[e])
        key = tuple(sorted((pr, tuple(sorted(ws)))
                           for pr, ws in groups.items()))
        if key in seen:
            continue
        seen.add(key)
        sols.append(w)
    return sols


# ---------- divergence triples ----------
dset = set()
ab_of_d = {}
for a in AC:
    for b in BC:
        d = tuple(b[i] - a[i] for i in range(H))
        assert sum(d) == 0
        dset.add(d)
        ab_of_d.setdefault(d, []).append((a, b))
print(f"distinct divergence triples: {len(dset)}", flush=True)

# ---------- S3-canonical iso classes ----------
PERMS = list(itertools.permutations(range(H)))


def signature(ori, w, a, b):
    ew = sorted((u, v, ww) for (u, v), ww in zip(ori, w))
    best = None
    for s in PERMS:
        inv = [0] * H
        for q in range(H):
            inv[s[q]] = q
        na = tuple(a[inv[i]] for i in range(H))
        nb = tuple(b[inv[i]] for i in range(H))
        new = tuple(sorted((s[u], s[v], ww) for (u, v, ww) in ew))
        key = (new, na, nb)
        if best is None or key < best:
            best = key
    return best


reps = {}
for ori in ORI:
    for d in dset:
        for w in solve_weights(ori, d):
            for (a, b) in ab_of_d[d]:
                sig = signature(ori, w, a, b)
                if sig not in reps:
                    reps[sig] = (ori, w, a, b)
print(f"iso classes: {len(reps)}", flush=True)


# ---------- markings: linear-extension DP ----------
def count_linext(ori, a, b):
    N = 3 + 3 + sum(a) + sum(b)
    assert N == 14, N
    pred = [0] * N
    for e, (u, v) in enumerate(ori):
        be = 3 + e
        pred[be] |= (1 << u)
        pred[v] |= (1 << be)
    idx = 6
    for V in range(H):
        for _ in range(a[V]):
            pred[V] |= (1 << idx)
            idx += 1
        for _ in range(b[V]):
            pred[idx] |= (1 << V)
            idx += 1
    FULL = (1 << N) - 1
    dp = {0: 1}
    for _ in range(N):
        ndp = {}
        for mask, c in dp.items():
            for x in range(N):
                if (mask >> x) & 1:
                    continue
                if pred[x] & ~mask == 0:
                    nm = mask | (1 << x)
                    ndp[nm] = ndp.get(nm, 0) + c
        dp = ndp
    return dp.get(FULL, 0)


def aut_order(ori, w, a, b):
    nvp = 0
    ew = sorted((u, v, ww) for (u, v), ww in zip(ori, w))
    for s in PERMS:
        inv = [0] * H
        for q in range(H):
            inv[s[q]] = q
        if tuple(a[inv[i]] for i in range(H)) != a:
            continue
        if tuple(b[inv[i]] for i in range(H)) != b:
            continue
        if tuple(sorted((s[u], s[v], ww) for (u, v, ww) in ew)) != tuple(ew):
            continue
        nvp += 1
    assert nvp >= 1
    groups = Counter((u, v, ww) for (u, v), ww in zip(ori, w))
    eperm = 1
    for m in groups.values():
        eperm *= factorial(m)
    for V in range(H):
        eperm *= factorial(a[V]) * factorial(b[V])
    return nvp * eperm


# ---------- refined weights ----------
def qint2(w):
    exps = [Fraction(-(w - 1), 2) + j for j in range(w)]
    c = Counter()
    for i in exps:
        for j in exps:
            c[int(i + j)] += 1
    return dict(c)


Q2 = {w: qint2(w) for w in range(1, 30)}


def mulpoly(p, q):
    r = Counter()
    for x, cx in p.items():
        for y, cy in q.items():
            r[x + y] += cx * cy
    return dict(r)


G = Counter()
classes = []
for sig, (ori, w, a, b) in reps.items():
    nl = count_linext(ori, a, b)
    ao = aut_order(ori, w, a, b)
    assert nl % ao == 0, (ori, w, a, b, nl, ao)
    nm = nl // ao
    for ww in w:
        assert ww in Q2, f"weight {ww} outside table"
    p = {0: 1}
    for ww in w:
        p = mulpoly(p, Q2[ww])
    for k, v in p.items():
        G[k] += nm * v
    classes.append({"ori": list(ori), "w": list(w), "a": list(a),
                    "b": list(b), "nlinext": nl, "aut": ao, "nmark": nm,
                    "poly": {str(k): v for k, v in p.items()}})

G1 = sum(G.values())
assert all(G.get(k, 0) == G.get(-k, 0) for k in G), "G not symmetric"
mxw = max(max(w) for (_, w, _, _) in reps.values())
print(f"max bounded-edge weight seen: {mxw}")
print(f"G(1) = {G1}")
print(f"G symmetric: True; support: {sorted(G)}")
print("exponent : coeff")
for k in sorted(G):
    print(f"  {k:4d} : {G[k]}")

with open("output/artifacts/ledger.json", "w") as f:
    json.dump({"G": {str(k): G[k] for k in sorted(G)}, "G1": G1,
               "nclasses": len(classes), "classes": classes}, f, indent=1)
print("saved output/artifacts/ledger.json")
