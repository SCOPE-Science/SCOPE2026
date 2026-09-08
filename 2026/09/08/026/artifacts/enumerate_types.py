#!/usr/bin/env python3
"""Step 1: enumerate labeled simple rank-3 line families on [8], reduce to iso types.
Writes representatives JSON + log."""
import json, time, sys

N = 8
pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
P = len(pairs)
pidx = {p: k for k, p in enumerate(pairs)}

cands = []
for em in range(1 << N):
    if bin(em).count("1") >= 3:
        pts = [i for i in range(N) if (em >> i) & 1]
        pm = 0
        for a in range(len(pts)):
            for b in range(a + 1, len(pts)):
                pm |= 1 << pidx[(pts[a], pts[b])]
        cands.append((em, pm))
NC = len(cands)

contain = [0] * P
for c, (em, pm) in enumerate(cands):
    m = pm
    while m:
        lsb = m & (-m)
        p = lsb.bit_length() - 1
        contain[p] |= 1 << c
        m ^= lsb

conflict = [0] * NC
for c, (em, pm) in enumerate(cands):
    s = 0
    m = pm
    while m:
        lsb = m & (-m)
        p = lsb.bit_length() - 1
        s |= contain[p]
        m ^= lsb
    conflict[c] = s

FULL = (1 << N) - 1

def line_data(fam):
    """fam: tuple of emasks. returns key + per-point signatures."""
    degs = [0] * N
    thru = [[] for _ in range(N)]
    for em in fam:
        s = bin(em).count("1")
        m = em
        while m:
            lsb = m & (-m)
            i = lsb.bit_length() - 1
            degs[i] += 1
            thru[i].append(s)
            m ^= lsb
    for i in range(N):
        thru[i].sort()
    sizes = sorted(bin(em).count("1") for em in fam)
    profs = []
    for em in fam:
        d = []
        m = em
        while m:
            lsb = m & (-m)
            i = lsb.bit_length() - 1
            d.append(degs[i])
            m ^= lsb
        profs.append((bin(em).count("1"), tuple(sorted(d))))
    profs.sort()
    pkey = tuple(sorted((degs[i], tuple(thru[i])) for i in range(N)))
    return (tuple(sizes), tuple(sorted(degs)), tuple(profs), pkey), degs, thru

def collinear_triples(fam):
    S = set()
    for em in fam:
        pts = [i for i in range(N) if (em >> i) & 1]
        for a in range(len(pts)):
            for b in range(a + 1, len(pts)):
                for c in range(b + 1, len(pts)):
                    S.add((pts[a], pts[b], pts[c]))
    return S

def iso_test(famF, sigF, famG, sigG):
    """sig = (degs, thru-as-tuples). Backtrack point map preserving collinearity."""
    degsF, thruF = sigF
    degsG, thruG = sigG
    colF = collinear_triples(famF)
    colG = collinear_triples(famG)
    keyF = [(degsF[i], thruF[i]) for i in range(N)]
    keyG = [(degsG[i], thruG[i]) for i in range(N)]
    from collections import defaultdict
    cand = defaultdict(list)
    for j in range(N):
        cand[keyG[j]].append(j)
    order = sorted(range(N), key=lambda i: (len(cand[keyF[i]]), -degsF[i]))
    if any(len(cand[keyF[i]]) == 0 for i in order):
        return False
    img = [-1] * N
    used = [False] * N
    assigned = []
    def ok_partial(i, j):
        for a in assigned:
            for b in assigned:
                if b <= a:
                    continue
                tF = tuple(sorted((i, a, b)))
                tG = tuple(sorted((j, img[a], img[b])))
                if (tF in colF) != (tG in colG):
                    return False
        return True
    def rec(k):
        if k == N:
            return True
        i = order[k]
        for j in cand[keyF[i]]:
            if used[j]:
                continue
            if not ok_partial(i, j):
                continue
            img[i] = j
            used[j] = True
            assigned.append(i)
            if rec(k + 1):
                return True
            assigned.pop()
            used[j] = False
            img[i] = -1
        return False
    return rec(0)

sys.setrecursionlimit(10000)
buckets = {}   # key -> list of [fam, degs, thru, count]
total = rank2 = 0
t0 = time.time()
leaves = 0

# iterative DFS with explicit selected list to build families
stack = [((1 << NC) - 1, 0, [])]  # (rem, used, selected)
while stack:
    rem, used, sel = stack.pop()
    # find first undecided pair
    p = None
    for q in range(P):
        if (used >> q) & 1:
            continue
        if rem & contain[q]:
            p = q
            break
    if p is None:
        leaves += 1
        fam = tuple(sorted(sel))
        if len(fam) == 1 and fam[0] == FULL:
            rank2 += 1
            continue
        total += 1
        key, degs, thru = line_data(fam)
        sig = (tuple(degs), tuple(tuple(t) for t in thru))
        b = buckets.get(key)
        if b is None:
            buckets[key] = [[fam, sig, 1]]
        else:
            found = False
            for rep in b:
                if iso_test(fam, sig, rep[0], rep[1]):
                    rep[2] += 1
                    found = True
                    break
            if not found:
                b.append([fam, sig, 1])
        continue
    stack.append((rem & ~contain[p], used, sel))
    m = rem & contain[p]
    while m:
        lsb = m & (-m)
        c = lsb.bit_length() - 1
        m ^= lsb
        stack.append((rem & ~conflict[c], used | cands[c][1], sel + [cands[c][0]]))

dt = time.time() - t0
ntypes = sum(len(v) for v in buckets.values())
print(f"leaves={leaves} rank2skip={rank2} labeled_simple_rank3={total}", flush=True)
print(f"buckets={len(buckets)} types={ntypes} time={dt:.1f}s", flush=True)
s = sum(rep[2] for v in buckets.values() for rep in v)
print(f"labeled check sum={s} (should equal {total})", flush=True)
assert s == total

reps = []
for key, lst in buckets.items():
    for (fam, sig, cnt) in lst:
        reps.append({"lines": list(fam), "count": cnt})
reps.sort(key=lambda r: (len(r["lines"]), r["lines"]))
with open("output/artifacts/reps.json", "w") as f:
    json.dump({"N": N, "total_labeled": total, "ntypes": len(reps), "reps": reps}, f)
with open("output/artifacts/enum_log.txt", "w") as f:
    f.write(f"leaves={leaves} rank2skip={rank2} labeled={total} buckets={len(buckets)} types={len(reps)} time={dt:.1f}s\n")
print("saved reps:", len(reps), flush=True)
