#!/usr/bin/env python3
from pathlib import Path
from itertools import product, combinations
from collections import Counter
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT / "artifacts" / "certificate.json").read_text(encoding="utf-8"))

ADD = [[a ^ b for b in range(4)] for a in range(4)]
MUL = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
INV = [None,1,3,2]
CONJ = [0,1,3,2]

def add(a,b): return ADD[a][b]
def mul(a,b): return MUL[a][b]

def poly_mul(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] = add(out[i+j], mul(x,y))
    return out

g2 = poly_mul([3,1,1], [1,3,1])
g3 = poly_mul([2,2,1], [1,3,1])
assert g2 == [3,3,1,2,1]
assert g3 == [2,3,2,1,1]

m = 7
g1 = [1] + [0]*6
g2 = g2 + [0]*(m-len(g2))
g3 = g3 + [0]*(m-len(g3))

def shift(v,t):
    out = [0]*m
    for i,x in enumerate(v):
        out[(i+t)%m] = x
    return out

G = [shift(g1,t) + shift(g2,t) + shift(g3,t) for t in range(m)]

def rref(rows, ncols):
    A = [list(r) for r in rows if any(r)]
    piv = 0
    for c in range(ncols):
        q = next((i for i in range(piv,len(A)) if A[i][c]), None)
        if q is None:
            continue
        A[piv], A[q] = A[q], A[piv]
        s = INV[A[piv][c]]
        A[piv] = [mul(s,x) for x in A[piv]]
        for i in range(len(A)):
            if i != piv and A[i][c]:
                a = A[i][c]
                A[i] = [add(A[i][j], mul(a,A[piv][j])) for j in range(ncols)]
        piv += 1
        if piv == len(A):
            break
    return tuple(tuple(r) for r in A[:piv])

assert len(rref(G,21)) == 7

dist = Counter()
for coeff in product(range(4), repeat=7):
    w = [0]*21
    for a,row in zip(coeff,G):
        if a:
            w = [add(x,mul(a,y)) for x,y in zip(w,row)]
    dist[sum(x != 0 for x in w)] += 1
expected_dist = {int(k):v for k,v in cert["ordinary_weight_distribution"].items()}
assert dict(sorted(dist.items())) == expected_dist
assert min(x for x in dist if x) == 11

Gram = []
for a in range(7):
    row = []
    for b in range(7):
        s = 0
        for x,y in zip(G[a],G[b]):
            s = add(s, mul(x, CONJ[y]))
        row.append(s)
    Gram.append(row)
assert len(rref(Gram,7)) == 7

cols = [tuple(G[r][j] for r in range(7)) for j in range(21)]

def rref_vecs(rows):
    return rref(rows,7)

def in_span(v, basis):
    return len(rref_vecs(list(basis)+[v])) == len(basis)

maxima = [0]
counts = [1]
for t in range(1,7):
    spans = set()
    for comb in combinations(range(21), t):
        key = rref_vecs([cols[j] for j in comb])
        if len(key) == t:
            spans.add(key)
    counts.append(len(spans))
    best = max(sum(in_span(v,key) for v in cols) for key in spans)
    maxima.append(best)

assert counts == cert["distinct_column_generated_subspaces_by_dimension"]
assert maxima == cert["column_intersection_maxima_by_subspace_dimension"]

for tstr, data in cert["maximizing_witnesses"].items():
    t = int(tstr)
    key = rref_vecs(data["basis"])
    assert len(key) == t
    got = [j for j,v in enumerate(cols) if in_span(v,key)]
    assert got == data["contained_column_indices"]
    assert len(got) == maxima[t]

ghw = [21 - maxima[7-r] for r in range(1,8)]
assert ghw == cert["generalized_hamming_weights"]
primal = set(ghw)
comp = [u for u in range(1,22) if u not in primal]
dual = sorted(22-u for u in comp)
assert dual == cert["dual_generalized_hamming_weights"]

print("VERIFY_OK")
