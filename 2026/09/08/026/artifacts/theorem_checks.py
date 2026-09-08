#!/usr/bin/env python3
"""Step 4: uniform-matroid maximizer theorem checks + Fano cert + replay traces."""
import json
from itertools import combinations

N = 8
rows = json.load(open("output/artifacts/tutte_table.json"))
rs = sorted(rows, key=lambda d: (-d["t20"], d["type"]))
W, R = rs[0], rs[1]

def rank_of_masks(lines):
    r = [0] * (1 << N)
    for s in range(1, 1 << N):
        pc = bin(s).count("1")
        if pc <= 2:
            r[s] = pc
        else:
            r[s] = 2 if any((s & ~ln) == 0 for ln in lines) else 3
    return r

# (a) Closed form T_{U(3,8)} by basis-activity counting: all 56 triples are bases.
# Verify against computed poly of W.
pw = {(i, j): c for (i, j, c) in [tuple(t) for t in W["poly"]]}
print("W poly terms:", sorted(pw.items()))
# check x-only: T(2,0)=58
print("W T(2,0) =", sum(c * 2**i for (i, j), c in pw.items() if j == 0))

# (b) Strict-decrease lemma check: for every non-uniform type, T(2,0) < 58
print("runner-up:", R["type"], R["t20"], "gap:", W["t20"] - R["t20"])
print("all others < 58:", all(d["t20"] < 58 for d in rs[1:]))

# (c) Fano cert for type-66: verify Fano axioms on points {0,1,2,3,5,6,7} with the 7 lines.
F = [[1,2,5],[0,3,5],[0,2,6],[1,3,6],[0,1,7],[2,3,7],[5,6,7]]
pts = [0,1,2,3,5,6,7]
ok_lines = all(len(L) == 3 for L in F)
pairs_covered = {}
ok = True
for L in F:
    for a in range(3):
        for b in range(a+1, 3):
            p = (min(L[a],L[b]), max(L[a],L[b]))
            if p in pairs_covered:
                ok = False
                print("pair twice:", p)
            pairs_covered[p] = tuple(L)
print("7 lines x C(3,2) =", 7*3, "= C(7,2) =", 21, "; pairwise-disjoint-pair cover:", ok and len(pairs_covered) == 21)
# Pasch/Fano: check isomorphic to standard Fano by finding an explicit bijection
import itertools
STD = [{0,1,3},{1,2,4},{2,0,5},{0,4,6},{1,5,6},{2,6,3},{3,4,5}]  # another Fano labeling
S = set()
for L in F:
    for a in range(3):
        for b in range(a+1,3):
            for c in range(b+1,3):
                pass
T = set(tuple(sorted(L)) for L in F)
found = None
for perm in itertools.permutations(pts):
    m = dict(zip([0,1,2,3,4,5,6], perm))
    img = set(tuple(sorted(m[x] for x in L)) for L in STD)
    if img == T:
        found = perm
        break
print("explicit Fano iso (std 0..6 -> pts):", found)

# (d) deletion-contraction replay trace for W and R (record decision sequence + states)
from functools import lru_cache
def trace(lines, label):
    r = rank_of_masks(lines)
    def rk(cset, sub):
        return r[sub | cset] - r[cset]
    seq = []
    memo = {}
    def T(rem, cset):
        key = (rem, cset)
        if key in memo:
            return memo[key]
        if not rem:
            memo[key] = {(0,0):1}; return memo[key]
        remset = 0
        for e in rem: remset |= 1 << e
        e = rem[0]; rest = rem[1:]
        restset = remset ^ (1<<e)
        re_ = rk(cset, 1<<e); rall = rk(cset, remset); rrest = rk(cset, restset)
        if re_ == 0:
            seq.append((label, "loop", e)); sub = T(rest, cset)
            out = {}
            for (i,j),c in sub.items(): out[(i,j+1)] = out.get((i,j+1),0)+c
        elif rrest < rall:
            seq.append((label, "coloop", e)); sub = T(rest, cset | (1<<e))
            out = {}
            for (i,j),c in sub.items(): out[(i+1,j)] = out.get((i+1,j),0)+c
        else:
            seq.append((label, "split", e)); d = T(rest, cset); c = T(rest, cset | (1<<e))
            out = dict(d)
            for k,cc in c.items(): out[k] = out.get(k,0)+cc
        memo[key] = out
        return out
    poly = T(tuple(range(N)), 0)
    v = sum(c*2**i for (i,j),c in poly.items() if j == 0)
    json.dump({"label": label, "lines": lines, "T20": v,
               "nsteps": len(seq), "nstates": len(memo),
               "steps": [[a,b,c] for (a,b,c) in seq],
               "poly": sorted([[i,j,c] for (i,j),c in poly.items()] )},
              open(f"output/artifacts/replay_{label}.json", "w"))
    print(label, "T(2,0) =", v, "steps =", len(seq), "states =", len(memo))

trace(W["lines"], "W")
trace(R["lines"], "runnerup")
print("distinct T20 values:", sorted(set(d['t20'] for d in rows), reverse=True))
print("type counts: ntypes=68; table rows:", len(rows))
