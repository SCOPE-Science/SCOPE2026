#!/usr/bin/env python3
"""Layer 2: given an equivariant Latin square L1 (20-tuple X), find all
equivariant orthogonal mates L2 (20-tuple Y) with Y[fix]=0.

Constraints on Y: row-group perms, column Latin, and orthogonality:
cell-orbit o -> symbol pair-orbit class must be injective (hence bijective).
Pair-orbit class of (a,b): (block_a, block_b, (a-b) mod 5).
"""
import sys, json

orbits = [(er, ec, d) for er in (0, 1) for ec in (0, 1) for d in range(5)]
oidx = {o: i for i, o in enumerate(orbits)}
NO = 20

def cell_orbit(r, c):
    return (r // 5, c // 5, ((c % 5) - (r % 5)) % 5)

cells_of = [[] for _ in range(NO)]
for r in range(10):
    for c in range(10):
        cells_of[oidx[cell_orbit(r, c)]].append((r, c))

def sym_of(val, r):
    s, b = divmod(val, 5)
    return s * 5 + (b + r % 5) % 5

def pair_class(a, b):
    return (a // 5, b // 5, ((a % 5) - (b % 5)) % 5)

def mate_count(X, cap=50, tlimit=120.0, yfix=0):
    import time
    t0 = time.time()
    # precompute L1 symbols per cell orbit representative cells
    # full L1 grid
    L1 = [[0]*10 for _ in range(10)]
    for i in range(NO):
        for (r, c) in cells_of[i]:
            L1[r][c] = sym_of(X[i], r)
    grp0 = [oidx[(0, ec, d)] for ec in (0, 1) for d in range(5)]
    grp1 = [oidx[(1, ec, d)] for ec in (0, 1) for d in range(5)]
    fix = oidx[(0, 0, 0)]
    order = [i for i in grp0 if i != fix] + list(grp1)
    Y = [-1]*NO
    Y[fix] = yfix
    used = [set() for _ in range(2)]
    used[0].add(yfix)
    col_used = [set() for _ in range(10)]
    # occupy fix cells
    for (r, c) in cells_of[fix]:
        col_used[c].add(sym_of(yfix, r))
    # pair classes used by fix orbit: class of (L1 cell sym, Y cell sym) per cell
    # invariant per orbit: compute from first cell
    pc_used = set()
    (r0, c0) = cells_of[fix][0]
    pc_used.add(pair_class(L1[r0][c0], sym_of(yfix, r0)))
    L1cell = {}  # orbit -> list of L1 syms per cell
    for i in range(NO):
        L1cell[i] = [L1[r][c] for (r, c) in cells_of[i]]
    count = 0
    sols = []
    sys.setrecursionlimit(10000)
    stop = False
    def bt(k):
        nonlocal count, stop
        if stop:
            return
        if (k & 63) == 0 and time.time() - t0 > tlimit:
            stop = True
            return
        if k == len(order):
            count += 1
            if len(sols) < 3:
                sols.append(tuple(Y))
            if count >= cap:
                stop = True
            return
        i = order[k]
        g = 0 if i in grp0 else 1
        # wait: grp0/grp1 by row-block er; build membership
        u = used[g]
        l1s = L1cell[i]
        for v in range(10):
            if v in u:
                continue
            ok = True
            touched = []
            for j, (r, c) in enumerate(cells_of[i]):
                s = sym_of(v, r)
                if s in col_used[c]:
                    ok = False
                    break
                touched.append((c, s))
            if not ok:
                continue
            pc = pair_class(l1s[0], sym_of(v, cells_of[i][0][0]))
            if pc in pc_used:
                continue
            Y[i] = v
            u.add(v)
            for (c, s) in touched:
                col_used[c].add(s)
            pc_used.add(pc)
            bt(k + 1)
            pc_used.discard(pc)
            for (c, s) in touched:
                col_used[c].discard(s)
            u.discard(v)
            Y[i] = -1
            if stop:
                return
    GRP0 = set(grp0)
    # fix closure issue: use GRP0
    def bt2(k):
        nonlocal count, stop
        if stop:
            return
        if (k & 63) == 0 and time.time() - t0 > tlimit:
            stop = True
            return
        if k == len(order):
            count += 1
            if len(sols) < 3:
                sols.append(tuple(Y))
            if count >= cap:
                stop = True
            return
        i = order[k]
        u = used[0 if i in GRP0 else 1]
        l1s = L1cell[i]
        for v in range(10):
            if v in u:
                continue
            ok = True
            touched = []
            for j, (r, c) in enumerate(cells_of[i]):
                s = sym_of(v, r)
                if s in col_used[c]:
                    ok = False
                    break
                touched.append((c, s))
            if not ok:
                continue
            pc = pair_class(l1s[0], sym_of(v, cells_of[i][0][0]))
            if pc in pc_used:
                continue
            Y[i] = v
            u.add(v)
            for (c, s) in touched:
                col_used[c].add(s)
            pc_used.add(pc)
            bt2(k + 1)
            pc_used.discard(pc)
            for (c, s) in touched:
                col_used[c].discard(s)
            u.discard(v)
            Y[i] = -1
            if stop:
                return
    bt2(0)
    return count, sols, time.time() - t0

if __name__ == "__main__":
    # read L1 solutions from latin_layer output embedded here or argv
    X = [0, 2, 1, 5, 7, 3, 6, 4, 9, 8, 2, 4, 6, 8, 5, 1, 0, 9, 3, 7]
    if len(sys.argv) > 1:
        X = json.loads(sys.argv[1])
    c, s, dt = mate_count(X)
    print(json.dumps({"mates_capped": c, "seconds": round(dt, 2),
                      "first": [list(x) for x in s]}))
