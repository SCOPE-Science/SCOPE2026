"""verify_replay.py — clean-room replay of the headline claim from stored artifacts only.

Reads trees_free.json + census.json, recomputes charpolys (own Faddeev-LeVerrier code),
walk determinants (own Bareiss), AHU canonical forms, and checks:
 (a) enumeration counts vs A000055 partial table,
 (b) adjacency non-DS counts vs A006610,
 (c) generalized grouping: only nontrivial class is n=12 {421,498},
 (d) stored spec/cspec/walkdet fields match recomputation,
 (e) witness pair non-isomorphic via AHU keys, same stored spec+cspec.
Usage: python3 verify_replay.py  -> prints VERIFY_OK or raises.
"""
import json
from collections import defaultdict

def adj_of(n, edges):
    A = [[0]*n for _ in range(n)]
    for u, v in edges:
        A[u][v] += 1; A[v][u] += 1
    return A

def mat_mul(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik = A[i][k]
            if aik:
                for j in range(n):
                    C[i][j] += aik*B[k][j]
    return C

def charpoly(A):
    n = len(A)
    if n == 1: return [-A[0][0], 1]
    M = [[0]*n for _ in range(n)]
    c = [0]*(n+1); c[n] = 1
    for k in range(1, n+1):
        Mn = [[M[i][j] + (c[n-k+1] if i == j else 0) for j in range(n)] for i in range(n)]
        M = mat_mul(A, Mn)
        t = sum(M[i][i] for i in range(n))
        assert t % k == 0, "LeVerrier divisibility"
        c[n-k] = -t//k
    return c

def bareiss(M):
    n = len(M)
    if n == 1: return M[0][0]
    B = [r[:] for r in M]
    prev = 1
    for k in range(n-1):
        if B[k][k] == 0:
            piv = next((i for i in range(k+1, n) if B[i][k] != 0), None)
            if piv is None: return 0
            B[k], B[piv] = B[piv], B[k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                B[i][j] = (B[i][j]*B[k][k]-B[i][k]*B[k][j])//prev
            B[i][k] = 0
        prev = B[k][k]
    return B[n-1][n-1]

def walk_det(n, edges):
    A = adj_of(n, edges)
    cols = [[1]*n]; v = [1]*n
    for _ in range(1, n):
        v = [sum(A[i][j]*v[j] for j in range(n)) for i in range(n)]
        cols.append(v)
    return bareiss([[cols[j][i] for j in range(n)] for i in range(n)])

def ahu(n, edges):
    adj = {i: [] for i in range(n)}
    for u, v in edges: adj[u].append(v); adj[v].append(u)
    if n == 1: return "()"
    deg = {i: len(adj[i]) for i in range(n)}
    leaves = [i for i in range(n) if deg[i] <= 1]
    rem = set(); left = n
    while True:
        if left <= 2:
            cen = [i for i in range(n) if i not in rem]; break
        nl = []
        for u in leaves:
            rem.add(u); left -= 1
            for w in adj[u]:
                if w not in rem:
                    deg[w] -= 1
                    if deg[w] == 1: nl.append(w)
        leaves = nl
    def enc(u, p):
        return "(" + "".join(sorted(enc(w, u) for w in adj[u] if w != p)) + ")"
    if len(cen) == 1: return enc(cen[0], -1)
    x, y = sorted([enc(cen[0], cen[1]), enc(cen[1], cen[0])])
    return "(" + x + y + ")"

def ps(c): return "(" + ",".join(str(int(x)) for x in c) + ")"

trees = json.load(open("trees_free.json"))
recs = json.load(open("census.json"))
assert len(recs) == 987, len(recs)
A55 = {"1":1,"2":1,"3":1,"4":2,"5":3,"6":6,"7":11,"8":23,"9":47,"10":106,"11":235,"12":551}
for n, e in A55.items():
    assert len(trees[n]) == e, (n, len(trees[n]))

# AHU uniqueness per n (enumeration is duplicate-free)
for n in map(str, range(1, 13)):
    keys = [ahu(int(n), [tuple(e) for e in es]) for es in trees[n]]
    assert len(set(keys)) == len(keys) == int(A55[n]), n

by_n = defaultdict(list)
for r in recs: by_n[r["n"]].append(r)
# recompute every spec/cspec/walkdet from trees_free.json edges
err = 0
for n in range(1, 13):
    E = {r["idx"]: r for r in by_n[n]}
    assert len(E) == len(trees[str(n)])
    for i, es in enumerate(trees[str(n)]):
        r = E[i]
        assert sorted(map(sorted, r["edges"])) == sorted(map(sorted, es)), (n, i)
        A = adj_of(n, es)
        C = [[(0 if a == b else 1)-A[a][b] for b in range(n)] for a in range(n)]
        if ps(charpoly(A)) != r["spec"] or ps(charpoly(C)) != r["cspec"]:
            err += 1; print("poly mismatch", n, i)
        if walk_det(n, es) != r["walkdet"]:
            err += 1; print("walkdet mismatch", n, i)
assert err == 0, err

# adjacency non-DS counts vs A006610
exp_adj = {8:2, 9:10, 10:8, 11:60, 12:119}
for n, e in exp_adj.items():
    adj = defaultdict(list)
    for r in by_n[n]: adj[r["spec"]].append(r["idx"])
    got = sum(len(v) for v in adj.values() if len(v) > 1)
    assert got == e, (n, got, e)

# generalized grouping over full stored census
gen = defaultdict(list)
for r in recs: gen[(r["n"], r["spec"], r["cspec"])].append(r["idx"])
nontriv = {k: v for k, v in gen.items() if len(v) > 1}
assert (len(nontriv) == 1 and list(nontriv)[0][0] == 12
    and sorted(list(nontriv.values())[0]) == [421, 498]), nontriv

A = next(r for r in by_n[12] if r["idx"] == 421)
B = next(r for r in by_n[12] if r["idx"] == 498)
assert A["spec"] == B["spec"] and A["cspec"] == B["cspec"]
assert ahu(12, [tuple(e) for e in A["edges"]]) != ahu(12, [tuple(e) for e in B["edges"]])
print("VERIFY_OK: 987 trees; adjacency non-DS = A006610; "
      "sole generalized-cospectral class n=12 {421,498}; all stored polys/walkdets recomputed.")
