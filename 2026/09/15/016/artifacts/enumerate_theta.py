#!/usr/bin/env python3
"""lane-20300: verification script for the theta-graph counterexample.

X, X': genus-3 bridgeless stable weighted tropical curves sharing the minimal
model T = theta graph (2 vertices, 4 parallel edges), with edge lengths
  X  : (1,1,1,1)
  X' : (1,1,1,2)
Polarization: canonical universal polarization of degree d=1,
  mu(v) = d*(2*w(v)-2+val(v))/(2g-2) = 1/2 per vertex.

Checks:
  (a) genus 3, bridgeless, stable, biconnected (single block) for both;
  (b) mu is nondegenerate on T (hence PSD = QD by AAP Thm, and P^trop(mu) is a
      well-defined coarsening of the poset computed below);
  (c) the (v0,mu)-quasistable pseudo-divisor poset (Abreu-Pacini Sec.4) depends
      ONLY on combinatorial data (degrees, mu, cut sizes) -- no edge lengths --
      hence is identical for X and X';
  (d) X, X' are NOT isomorphic as weighted metric graphs (length multisets
      differ; Aut(T) permutes parallel edges);
  (e) Jacobian volumes (Kirchhoff: sum over spanning-tree complements of
      length products) differ, so even the pp Jacobians differ.
"""
import json
from itertools import combinations
from collections import Counter
from math import prod

V = [0, 1]
E = [(0, 1)] * 4          # 4 parallel edges
nE = len(E)
g = nE - len(V) + 1       # connected graph genus
assert g == 3, g
print("genus =", g)

# ---- bridges ----
def comps_wo_edges(rem):
    parent = {v: v for v in V}
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for i, (a, b) in enumerate(E):
        if i not in rem:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
    return len({find(v) for v in V})

bridges = [i for i in range(nE) if comps_wo_edges({i}) > 1]
print("bridges =", bridges)
assert bridges == []

# ---- stability: valences (weights all 0) ----
val = {v: sum(1 for (a, b) in E if v in (a, b)) for v in V}
print("valences =", val)
assert all(x >= 3 for x in val.values())

# ---- biconnectivity: no cut vertex ----
def comps_wo_vertex(v):
    rest = [u for u in V if u != v]
    if not rest:
        return 0
    parent = {u: u for u in rest}
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for (a, b) in E:
        if a != v and b != v:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
    return len({find(u) for u in rest})

cuts = [v for v in V if comps_wo_vertex(v) > 1]
print("cut vertices =", cuts)
assert cuts == []          # single biconnected component (block)

# ---- canonical polarization d=1, nondegeneracy ----
d = 1
mu = {v: d * (0 - 2 + val[v]) / (2 * g - 2) for v in V}
print("mu =", mu)
assert all(m == 0.5 for m in mu.values())
# nondegenerate: mu(V) - delta(V)/2 never integral for nonempty proper V
def delta(S):
    S = set(S)
    return sum(1 for (a, b) in E if (a in S) != (b in S))
nondeg = True
for r in range(1, len(V)):
    for S in combinations(V, r):
        q = sum(mu[v] for v in S) - delta(S) / 2
        if abs(q - round(q)) < 1e-9:
            nondeg = False
            print("degenerate at", S, q)
print("mu nondegenerate =", nondeg)
assert nondeg

# ---- (v0,mu)-quasistable pseudo-divisor enumeration (Abreu-Pacini, Sec 4) ----
# Vertices of subdivision Gamma_F: 0,1 + exceptional x_e for e in F.
# Induced polarization mu^F: mu on old vertices, 0 on exceptional vertices.
# D: D(x_e) = -1; D(0)+D(1) = d + |F|.
# beta(V) = deg(D|V) - mu^F(V) + cut_{Gamma_F}(V)/2.
# (v0=0)-quasistable: beta(V) >= 0 for all proper nonempty V, strict if 0 in V.
def quasistable_list(v0=0):
    out = []
    for r in range(nE + 1):
        for F in combinations(range(nE), r):
            F = set(F)
            # F nondisconnecting <=> Gamma minus F connected
            if comps_wo_edges(F) > 1:
                continue
            exc = [('x', e) for e in F]
            verts = V + exc
            adj = []
            for i, (a, b) in enumerate(E):
                if i in F:
                    adj.append((a, ('x', i)))
                    adj.append((('x', i), b))
                else:
                    adj.append((a, b))
            def dlt(S):
                S = set(S)
                return sum(1 for (a, b) in adj if (a in S) != (b in S))
            muF = {0: mu[0], 1: mu[1]}
            for e in F:
                muF[('x', e)] = 0.0
            for D0 in range(-3, 2 + len(F) + 3):
                D1 = (d + len(F)) - D0
                D = {0: D0, 1: D1}
                for e in F:
                    D[('x', e)] = -1
                ok = True
                for rr in range(1, len(verts)):
                    for S in combinations(verts, rr):
                        S = set(S)
                        deg = sum(D[v] for v in S)
                        beta = deg - sum(muF[v] for v in S) + dlt(S) / 2
                        if beta < -1e-9 or (v0 in S and abs(beta) < 1e-9):
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    out.append((tuple(sorted(F)), D0, D1))
    return out

Q = quasistable_list()
print("number of (v0,mu)-quasistable pseudo-divisors =", len(Q))
assert len(Q) > 0
maxrk = max(len(F) for (F, _, _) in Q)
print("maximal rank |F| =", maxrk, "(b1 =", g, ")")
assert maxrk == g  # ranked of length b1, Abreu-Pacini Prop 4.10
print("rank distribution:", dict(sorted(Counter(len(F) for (F, _, _) in Q).items())))
# NOTE: this enumeration uses only (degrees, mu, cut sizes) -- no edge lengths.
# Both X and X' share model T and mu, so their posets (hence, in the
# nondegenerate case, their polystable posets and P^trop_mu polyhedral
# complexes up to the length-parametrized cells below) agree combinatorially.

# ---- metric non-isomorphism of the single blocks ----
L1 = (1, 1, 1, 1)
L2 = (1, 1, 1, 2)
print("length multisets:", sorted(L1), sorted(L2))
# Aut(T) permutes the 4 parallel edges (and may swap vertices), so the sorted
# length tuple is a complete invariant of the weighted metric graph.
assert sorted(L1) != sorted(L2)
print("blocks NOT isomorphic as weighted metric graphs: True")

# ---- Jacobian volumes differ (Kirchhoff matrix-tree for tropical Jac) ----
def jac_vol(L):
    # spanning trees of the 2-vertex 4-edge banana graph = single edges;
    # cell vol = product of complement; total vol = sum over trees.
    trees = [[i] for i in range(nE)]
    return sum(prod(L[e] for e in range(nE) if e not in T) for T in trees)
v1, v2 = jac_vol(L1), jac_vol(L2)
print("Jacobian volumes:", v1, v2)
assert v1 != v2

with open("theta_counterexample.json", "w") as f:
    json.dump({
        "genus": g, "bridges": bridges, "cut_vertices": cuts,
        "valences": val, "mu": mu, "mu_nondegenerate": nondeg,
        "n_quasistable": len(Q), "max_rank": maxrk,
        "rank_distribution": dict(sorted(Counter(len(F) for (F, _, _) in Q).items())),
        "lengths_X": sorted(L1), "lengths_Xp": sorted(L2),
        "blocks_metrically_isomorphic": False,
        "jacobian_volumes": [v1, v2],
    }, f, indent=2)
print("wrote theta_counterexample.json")
