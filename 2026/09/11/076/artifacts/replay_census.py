#!/usr/bin/env python3
"""Independent replay of the normalized C5-equivariant Latin census.

Differences from work/census_bg.py: different variable order (group-1 block
first, reversed within groups), values tried descending, iterative checksum
(sum of FNV-1a hashes mod 2^64) over all solutions. Must reproduce count
2,082,000 if the census is correct.
"""
import sys, time, json
sys.path.insert(0, "work")
from pair_layer import cells_of, oidx, sym_of, NO

orbits = [(er, ec, d) for er in (0, 1) for ec in (0, 1) for d in range(5)]
O = {o: i for i, o in enumerate(orbits)}
g0 = [O[(0, ec, d)] for ec in (0, 1) for d in range(5)]
g1 = [O[(1, ec, d)] for ec in (0, 1) for d in range(5)]
is0 = [False] * NO
for i in g0:
    is0[i] = True
fix = O[(0, 0, 0)]
# DIFFERENT ORDER: group-1 block first, then group-0 non-fix, reversed
order = list(reversed(g1)) + [i for i in reversed(g0) if i != fix]
assert len(order) == 19 and fix not in order

X = [-1] * NO
X[fix] = 0
used = [set() for _ in range(2)]
used[0].add(0)
col_used = [set() for _ in range(10)]
count = [0]
chk = [0]
nodes = [0]
t0 = time.time()
LOG = open("output/artifacts/latin_census_replay.log", "a", buffering=1)
sys.setrecursionlimit(10000)
M = (1 << 64) - 1
FNV = 1469598103934665603

def h_update():
    h = FNV
    for v in X:
        h ^= (v + 1)
        h = (h * 1099511628211) & M
    chk[0] = (chk[0] + h) & M

def bt(k):
    nodes[0] += 1
    if nodes[0] % 2000000 == 0:
        LOG.write(json.dumps({"nodes": nodes[0], "count": count[0],
                              "t": round(time.time() - t0, 1)}) + "\n")
    if k == len(order):
        count[0] += 1
        h_update()
        return
    i = order[k]
    u = used[0 if is0[i] else 1]
    for v in (9, 8, 7, 6, 5, 4, 3, 2, 1, 0):  # DESCENDING values
        if v in u:
            continue
        ok = True
        touched = []
        for (r, c) in cells_of[i]:
            s = sym_of(v, r)
            if s in col_used[c]:
                ok = False
                break
            touched.append((c, s))
        if not ok:
            continue
        X[i] = v
        u.add(v)
        for (c, s) in touched:
            col_used[c].add(s)
        bt(k + 1)
        for (c, s) in touched:
            col_used[c].discard(s)
        u.discard(v)
        X[i] = -1

bt(0)
LOG.write(json.dumps({"DONE": True, "count": count[0],
                      "checksum": chk[0], "nodes": nodes[0],
                      "t": round(time.time() - t0, 1)}) + "\n")
print(json.dumps({"count": count[0], "checksum": chk[0], "nodes": nodes[0],
                  "t": round(time.time() - t0, 1)}))
