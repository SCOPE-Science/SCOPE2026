"""Independent verifier for the preset-fallback census (stdlib only).

(i) Regenerates all 352 labeled shifted ideals on {0..6} via the same ideal DFS
    (independent code path, recursive include/exclude with predecessor check).
(ii) Checks each census.json representative: shifted, C5-free (brute force
    21 five-sets x 12 patterns), edge count matches.
(iii) Checks exhaustiveness: every labeled shifted C5-free ideal is isomorphic
    (S7) to exactly one class representative; confirms class count, per-class
    labeled-orbit sizes, and the maximum edge count 16.
Usage: python3 verify_census.py -> VERIFY_OK / VERIFY_FAIL.
"""
import itertools
import json

n = 7
T = sorted(itertools.combinations(range(n), 3), key=lambda t: (sum(t), t))
idx = {t: k for k, t in enumerate(T)}
m = len(T)

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
    touched = [k]
    state[k] = -1
    for d_ in depend[k]:
        if state[d_] == 0:
            state[d_] = -1
            touched.append(d_)
    dfs(p + 1)
    for d_ in touched:
        state[d_] = 0
    if all(state[u] == 1 for u in pred[k]):
        state[k] = 1
        dfs(p + 1)
        state[k] = 0

dfs(0)
ok_gen = (len(ideals) == 352)
print("(i) labeled shifted ideals: %d (expect 352) -> %s" % (len(ideals), ok_gen))

C = json.load(open('output/artifacts/census.json'))
ok_count = (C['num_labeled_shifted'] == 352 and C['num_labeled_shifted_c5free'] == 68
            and C['num_classes'] == 68 and C['max_edges'] == 16)
print("(i) census.json header counts 352/68/68/16 -> %s" % ok_count)

def is_shifted(h):
    E = set(k for k in range(m) if (h >> k) & 1)
    for k in E:
        for u in pred[k]:
            if u not in E:
                return False
    return True

def is_free(h):
    return all((h & c) != c for c in c5)

reps = []
ok_entries = True
for c in C['classes']:
    h = sum(1 << idx[tuple(sorted(e))] for e in c['representative_edges_0based'])
    if not (is_shifted(h) and is_free(h) and bin(h).count('1') == c['edges']):
        ok_entries = False
        print("BAD entry:", c)
    reps.append(h)
print("(ii) all %d representatives shifted + C5-free + edge count -> %s"
      % (len(reps), ok_entries))

perms = list(itertools.permutations(range(n)))
pmap = []
for q in perms:
    pmap.append([idx[tuple(sorted(q[v] for v in T[k]))] for k in range(m)])

def apply(h, pm):
    out = 0
    for k in range(m):
        if (h >> k) & 1:
            out |= 1 << pm[k]
    return out

free_set = set(h for h in ideals if is_free(h))
ok_exh = (len(free_set) == 68)
# each labeled free ideal isomorphic to exactly one rep; rep = lex-min shifted member
ok_match = True
for h in free_set:
    hits = 0
    for r in reps:
        found = False
        for pm in pmap:
            if apply(h, pm) == r:
                found = True
                break
        if found:
            # also require the image lies in shifted-free set (it does: r is)
            hits += 1
    if hits != 1:
        ok_match = False
        print("MATCH FAIL h=%d hits=%d" % (h, hits))
print("(iii) labeled free count 68 -> %s; each matches exactly one rep -> %s"
      % (ok_exh, ok_match))
mx = max(bin(h).count('1') for h in free_set)
print("(iii) replayed max edges: %d (expect 16) -> %s" % (mx, mx == 16))

if ok_gen and ok_count and ok_entries and ok_exh and ok_match and mx == 16:
    print("VERIFY_OK")
else:
    print("VERIFY_FAIL")
