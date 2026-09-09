"""PRESET FALLBACK: exhaustive shifted C5^(3)-free census on 7 vertices.

Shifted (left-compressed): H on {0..6} with: t in H, j in t, i<j, i not in t
=> shift-down u=(t-{j})u{i} in H. Equivalent to predecessor-closed (order ideal)
in the shift poset; closure under immediate downs implies full shiftedness.

Generator: DFS over triples in nondecreasing-sum order (predecessors decided
before dependents). EXCLUDE k -> force all dependents out; INCLUDE k allowed
iff all immediate predecessors in. Each ideal generated exactly once.
Freeness: brute force over 21 five-sets x 12 tight-C5 patterns (252 masks).
Isomorphism: group labeled C5-free ideals into S7 orbits; representative = lex
smallest shifted member of each class.
Outputs: census.json (representatives + summary), prints summary.
Stdlib + numpy (numpy only for 2^20-free vector ops here? actually stdlib only).
"""
import itertools
import json

n = 7
T = sorted(itertools.combinations(range(n), 3), key=lambda t: (sum(t), t))
idx = {t: k for k, t in enumerate(T)}
m = len(T)  # 35

pred = [[] for _ in range(m)]
for k, t in enumerate(T):
    s = set(t)
    for j in t:
        for i in range(j):
            if i not in s:
                pred[k].append(idx[tuple(sorted((s - {j}) | {i}))])
    pred[k] = sorted(set(pred[k]))
depend = [[] for _ in range(m)]
for k in range(m):
    for u in pred[k]:
        depend[u].append(k)
order = sorted(range(m), key=lambda k: (sum(T[k]), T[k]))

# distinct tight-C5 masks
c5 = []
for verts in itertools.combinations(range(n), 5):
    seen = set()
    for p in itertools.permutations(verts):
        if p[0] != min(p) or p[1] > p[4]:
            continue
        e = frozenset(tuple(sorted((p[k], p[(k + 1) % 5], p[(k + 2) % 5]))) for k in range(5))
        if e in seen:
            continue
        seen.add(e)
        c5.append(sum(1 << idx[t] for t in e))
print("triples=%d C5 patterns=%d" % (m, len(c5)), flush=True)

import sys
sys.setrecursionlimit(10000)
state = [0] * m
ideals = []

def dfs(p):
    if p == m:
        ideals.append(sum(1 << k for k in range(m) if state[k] == 1))
        return
    k = order[p]
    if state[k] != 0:
        dfs(p + 1)
        return
    # OUT
    touched = [k]
    state[k] = -1
    for d_ in depend[k]:
        if state[d_] == 0:
            state[d_] = -1
            touched.append(d_)
    dfs(p + 1)
    for d_ in touched:
        state[d_] = 0
    # IN
    if all(state[u] == 1 for u in pred[k]):
        state[k] = 1
        dfs(p + 1)
        state[k] = 0

dfs(0)
print("labeled shifted ideals: %d" % len(ideals), flush=True)

def pop(x):
    return bin(x).count('1')

free = [h for h in ideals if all((h & c) != c for c in c5)]
print("C5-free labeled shifted: %d" % len(free), flush=True)

# S7 orbits among free ideals
perms = list(itertools.permutations(range(n)))
pmap = []
for q in perms:
    pm = [idx[tuple(sorted(q[v] for v in T[k]))] for k in range(m)]
    pmap.append(pm)

def apply(h, pm):
    out = 0
    hh = h
    k = 0
    while hh:
        if hh & 1:
            out |= 1 << pm[k]
        k += 1
        hh >>= 1
    return out

free_set = set(free)
seen = set()
classes = []
for h in free:
    if h in seen:
        continue
    orb = set()
    for pm in pmap:
        g = apply(h, pm)
        if g in free_set:
            orb.add(g)
    for g in orb:
        seen.add(g)
    rep = min(orb)
    classes.append((rep, len(orb)))
print("isomorphism classes: %d" % len(classes), flush=True)

def edges(h):
    return sorted([list(T[k]) for k in range(m) if (h >> k) & 1])

classes.sort(key=lambda r: (pop(r[0]), r[0]))
mx = max(pop(h) for h in free)
ext = [r for r in classes if pop(r[0]) == mx]
print("max edges in class: %d (#classes at max: %d)" % (mx, len(ext)), flush=True)
by_edges = {}
for (rep, sz) in classes:
    by_edges.setdefault(pop(rep), []).append((rep, sz))
for e in sorted(by_edges):
    print("edges=%d: %d classes" % (e, len(by_edges[e])), flush=True)

out = {
    "n": n,
    "num_triples": m,
    "num_c5_patterns": len(c5),
    "num_labeled_shifted": len(ideals),
    "num_labeled_shifted_c5free": len(free),
    "num_classes": len(classes),
    "max_edges": mx,
    "classes": [
        {"representative_edges_0based": edges(rep), "edges": pop(rep),
         "labeled_orbit_size_within_shifted_free": sz}
        for (rep, sz) in classes
    ],
}
with open('output/artifacts/census.json', 'w') as f:
    json.dump(out, f)
print("wrote output/artifacts/census.json", flush=True)
for (rep, sz) in ext[:10]:
    print("extremal rep:", edges(rep), "x%d" % sz, flush=True)
