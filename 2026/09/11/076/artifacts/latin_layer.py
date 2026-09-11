#!/usr/bin/env python3
"""Layer 1: count C5-equivariant Latin squares of order 10 (normalised).

sigma(i) = (i+1)%5 + 5*(i//5). Cell-orbit o=(er,ec,d), 20 vars X[o]=(s,b).
sym(r,c) = s*5 + (b + r%5)%5. Row groups must be permutations; columns Latin.
Fix X[(0,0,0)] = 0 (uses symbol-centralizer transitivity).
"""
import sys, time, json

NO = 20
orbits = [(er, ec, d) for er in (0, 1) for ec in (0, 1) for d in range(5)]
oidx = {o: i for i, o in enumerate(orbits)}

def cell_orbit(r, c):
    return (r // 5, c // 5, ((c % 5) - (r % 5)) % 5)

cells_of = [[] for _ in range(NO)]
for r in range(10):
    for c in range(10):
        cells_of[oidx[cell_orbit(r, c)]].append((r, c))
assert all(len(x) == 5 for x in cells_of), [len(x) for x in cells_of]

def sym_of(val, r):
    s, b = divmod(val, 5)
    return s * 5 + (b + r % 5) % 5

grp = [[oidx[(er, ec, d)] for ec in (0, 1) for d in range(5)] for er in (0, 1)]
isingrp0 = [False] * NO
for i in grp[0]:
    isingrp0[i] = True

fix = oidx[(0, 0, 0)]
X = [-1] * NO
X[fix] = 0
used = [set() for _ in range(2)]
used[0].add(0)
col_used = [set() for _ in range(10)]
# for each var, its 5 cells (r,c)
order = [i for i in grp[0] if i != fix] + list(grp[1])

cap = int(sys.argv[1]) if len(sys.argv) > 1 else 10**18
tlimit = float(sys.argv[2]) if len(sys.argv) > 2 else 600.0
count = 0
first = []
t0 = time.time()
stop = False

sys.setrecursionlimit(10000)

def bt(k):
    global count, stop
    if stop:
        return
    if k == len(order):
        count += 1
        if len(first) < 3:
            first.append(tuple(X))
        if count >= cap:
            stop = True
        return
    i = order[k]
    g = 0 if isingrp0[i] else 1
    u = used[g]
    cells = cells_of[i]
    for v in range(10):
        if v in u:
            continue
        ok = True
        touched = []
        for (r, c) in cells:
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
        if stop:
            return

bt(0)
dt = time.time() - t0
print(json.dumps({
    "count_capped": count,
    "cap": cap,
    "exhausted": not stop,
    "seconds": round(dt, 2),
    "first3": [list(f) for f in first],
}))
