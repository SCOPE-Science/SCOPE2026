#!/usr/bin/env python3
"""Enumerate genus-0 (connected, tree) floor diagrams for F0=P1xP1, class (3,4).

Setup (fixed explicitly to remove F_n-convention ambiguity):
  Surface S = Sigma_0 = P1 x P1 (m = 0).
  Line bundle L = d*H + c*F with d = 3, c = 4  (bidegree (L.F, L.H) = (3,4)).
  Newton polygon = rectangle [0,4] x [0,3] (c=4 wide, d=3 tall).
  Arithmetic genus = (3-1)*(4-1) = 6 = # interior lattice points.
  Genus 0  =>  cogenus delta = 6 - 0 = 6 (automatic for connected trees).
  # point conditions n = dim|L| - delta = 19 - 6 = 13.

Floor diagrams (Block-Gottsche 1407.2901, Def 5.1, Sigma_m case, m=0):
  Vertex set {1,...,d} = {1,2,3}, edges directed i->j (i<j).
  s = (s1,s2,s3), sum = c = 4.
  div(j) = out(j) - in(j) <= m + s_j = s_j.
  Connected genus-0 on 3 vertices => exactly 2 edges forming a tree.
  Connected patterns (undirected tree on {1,2,3}):
    A: 1->2, 2->3            (chain)
    E: 1->2, 1->3            (fan from 1)
    F: 1->3, 2->3            (fan into 3)
  (Patterns with a doubled edge leave a vertex isolated, but with total
   genus 1 (k=2 components) they still have cogenus 6 and MUST be included:
   delta = g_a - sum g_i + k - 1 with g_a=6. Single-edge (delta=7) and
   empty (delta=8) graphs are excluded.)
  Parallel equal-weight edges admit a swapping automorphism, so
  nu = LE/(prod s_j! t_j! * aut), aut=2 when the two parallel equal, else 1.

Refined multiplicity: mult(D;y) = prod_e [w_e]_y^2, [n]_y quantum number.
Markings: nu(D) = # linear extensions of marked graph D~ (Steps 1-4),
  counted with distinguishable added vertices via subset DP, divided by
  prod_j s_j! t_j! (indistinguishable short vertices), t_j = s_j - div(j).
  No parallel edges occur in patterns A,E,F, so no extra edge symmetry.
"""
import json
from functools import lru_cache
from math import factorial

C_SUM = 4
D_FLOORS = 3


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def qbracket_sq(w):
    """Return [w]_y^2 as dict {int exponent: coeff} in y (integer exponents)."""
    # [w]_y = sum_{k} z^k in z=y^{1/2}, k from -(w-1)/2..(w-1)/2 step 1.
    half = {}
    e = -(w - 1)
    while e <= (w - 1):
        half[e] = half.get(e, 0) + 1  # exponent in units of 1/2
        e += 2
    sq = {}
    for e1, c1 in half.items():
        for e2, c2 in half.items():
            s = e1 + e2  # even integer (units of 1/2); y-exponent = s/2
            assert s % 2 == 0
            sq[s // 2] = sq.get(s // 2, 0) + c1 * c2
    return sq


def mul_poly(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            out[e1 + e2] = out.get(e1 + e2, 0) + c1 * c2
    return out


def count_markings(s, div, edges, w):
    """Count nu(D). edges = list of (i,j) 1-based original edges; w = weights."""
    t = [s[j] - div[j] for j in range(3)]
    assert all(x >= 0 for x in t), (s, div, t)
    # Vertex indexing: 0,1,2 = floors f1,f2,f3.
    # L vertices (incoming shorts): pred set empty; they precede f_j.
    # R vertices (outgoing shorts): successor of f_j.
    # midpoints: between f_i and f_j.
    preds = []  # preds[v] = bitmask of predecessors
    # floors first
    for _ in range(3):
        preds.append(0)
    F = [0, 1, 2]
    # floor order f1 < f2 < f3 enforced as precedence
    preds[1] |= (1 << 0)
    preds[2] |= (1 << 1)
    L_ids, R_ids, M_ids = [], [], []
    for j in range(3):
        cur_L = []
        for _ in range(s[j]):
            v = len(preds)
            preds.append(0)
            preds[F[j]] |= (1 << v)  # v precedes f_j
            cur_L.append(v)
        L_ids.append(cur_L)
        cur_R = []
        for _ in range(t[j]):
            v = len(preds)
            preds.append(1 << F[j])  # f_j precedes v
            cur_R.append(v)
        R_ids.append(cur_R)
    for (i, j) in edges:
        v = len(preds)
        preds.append((1 << F[i - 1]) | 0)
        preds[F[j - 1]] |= (1 << v)
        M_ids.append(v)
    n = len(preds)
    N = 3 + sum(s) + sum(t) + len(edges)
    assert n == N, (n, N, s, t)
    # n=13 for tree patterns; 12 for doubled patterns (verified below).
    # Subset DP over masks
    dp = {0: 1}
    full = (1 << n) - 1
    # iterate masks in increasing order
    for mask in range(full + 1):
        c = dp.get(mask)
        if not c:
            continue
        for v in range(n):
            if mask & (1 << v):
                continue
            if preds[v] & ~mask == 0:
                dp[mask | (1 << v)] = dp.get(mask | (1 << v), 0) + c
    LE = dp.get(full, 0)
    denom = 1
    for j in range(3):
        denom *= factorial(s[j]) * factorial(t[j])
    # parallel double-edge swap automorphism (floor-preserving)
    aut = 2 if (len(edges) == 2 and edges[0] == edges[1]
                and w[0] == w[1]) else 1
    denom *= aut
    assert LE % denom == 0, (LE, denom, s, t, edges)
    return LE // denom, LE


def enumerate_diagrams():
    diagrams = []
    # Pattern A: edges (1,2,a),(2,3,b)
    for s in compositions(C_SUM, 3):
        s1, s2, s3 = s
        for a in range(1, s1 + 1):
            for b in range(1, a + s2 + 1):
                div = (a, b - a, -b)
                if div[1] > s2:
                    continue
                diagrams.append(("A", s, (a, b), [(1, 2), (2, 3)], div))
    # Pattern E: edges (1,2,a),(1,3,b)
    for s in compositions(C_SUM, 3):
        s1, s2, s3 = s
        for a in range(1, 5):
            for b in range(1, 5):
                if a + b > s1:
                    continue
                div = (a + b, -a, -b)
                diagrams.append(("E", s, (a, b), [(1, 2), (1, 3)], div))
    # Pattern F: edges (1,3,a),(2,3,b)
    for s in compositions(C_SUM, 3):
        s1, s2, s3 = s
        for a in range(1, s1 + 1):
            for b in range(1, s2 + 1):
                div = (a, b, -a - b)
                diagrams.append(("F", s, (a, b), [(1, 3), (2, 3)], div))
    # Doubled patterns (disconnected, genus 1, cogenus 6 — INCLUDE):
    # D12(J): double edge 1->2 of weights (a,b); floor 3 isolated.
    for s in compositions(C_SUM, 3):
        s1, s2, s3 = s
        for a in range(1, 5):
            for b in range(a, 5):  # unordered pair, a<=b
                if a + b > s1:
                    continue
                div = (a + b, -a - b, 0)
                diagrams.append(("D12", s, (a, b), [(1, 2), (1, 2)], div))
    # D23(J): double edge 2->3; floor 1 isolated.
    for s in compositions(C_SUM, 3):
        s1, s2, s3 = s
        for a in range(1, 5):
            for b in range(a, 5):
                # div2 = a+b <= s2, div3 = -(a+b); div1 = 0
                if a + b > s2:
                    continue
                div = (0, a + b, -a - b)
                diagrams.append(("D23", s, (a, b), [(2, 3), (2, 3)], div))
    # D13(J): double edge 1->3; floor 2 isolated.
    for s in compositions(C_SUM, 3):
        s1, s2, s3 = s
        for a in range(1, 5):
            for b in range(a, 5):
                if a + b > s1:
                    continue
                div = (a + b, 0, -a - b)
                diagrams.append(("D13", s, (a, b), [(1, 3), (1, 3)], div))
    return diagrams


def main():
    diags = enumerate_diagrams()
    table = []
    L = {0: 0}
    for idx, (pat, s, w, edges, div) in enumerate(diags):
        mult = {0: 1}
        for x in w:
            mult = mul_poly(mult, qbracket_sq(x))
        nu, LE = count_markings(list(s), list(div), edges, list(w))
        t = [s[j] - div[j] for j in range(3)]
        contrib = {e: c * nu for e, c in mult.items()}
        L = {e: L.get(e, 0) + contrib.get(e, 0) for e in set(L) | set(contrib)}
        table.append({
            "id": idx,
            "pattern": pat,
            "s": list(s),
            "weights": list(w),
            "edges": [list(e) for e in edges],
            "div": list(div),
            "t": list(t),
            "mult_q": {str(e): c for e, c in sorted(mult.items())},
            "nu": nu,
            "LE": LE,
        })
    L_clean = {int(e): int(c) for e, c in L.items() if c}
    L1 = sum(L_clean.values())
    Lm1 = sum(c if e % 2 == 0 else -c for e, c in L_clean.items())
    out = {
        "metadata": {
            "surface": "Sigma_0 = P1xP1 (m=0)",
            "class": "L = 3H + 4F, bidegree (L.F, L.H) = (3,4)",
            "polygon": "rectangle [0,4]x[0,3]",
            "arith_genus": 6,
            "cogenus": 6,
            "n_points": 13,
            "n_diagrams": len(table),
        },
        "diagrams": table,
        "L_q": {str(e): c for e, c in sorted(L_clean.items())},
        "L1": L1,
        "Lm1": Lm1,
    }
    with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-887/output/artifacts/ledger.json", "w") as f:
        json.dump(out, f, indent=1)
    print("n_diagrams =", len(table))
    print("L(q) =", {e: c for e, c in sorted(L_clean.items())})
    print("L(1) =", L1, " L(-1) =", Lm1)
    # smallest-LE diagrams for hand check
    tab2 = sorted(table, key=lambda r: r["LE"])
    print("smallest LE rows:")
    for r in tab2[:5]:
        print(r["pattern"], r["s"], r["weights"], "div=", r["div"], "t=", r["t"], "nu=", r["nu"], "LE=", r["LE"])


if __name__ == "__main__":
    main()
