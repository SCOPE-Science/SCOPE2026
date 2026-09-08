"""Independent stabilizer cross-check: different branching + closure test."""
import glob
from collections import Counter

def load(f):
    return [int(l.strip(), 2) for l in open(f) if l.strip()]

def aut_group(v, seed_order):
    fams = [frozenset(i for i in range(14) if (x >> (13 - i)) & 1) for x in v]
    famset = set(fams)
    deg = [sum(1 for s in fams if i in s) for i in range(14)]
    # different variable order: sort by deg then by seed-rotated index
    order = sorted(range(14), key=lambda i: (deg[i], (i + seed_order) % 14))
    img = [None]*14
    used = [False]*14
    elts = []
    # triple-intersection signature for stronger pruning
    def sigok(p, q):
        for r in range(14):
            if img[r] is not None:
                c1 = sum(1 for s in fams if p in s and r in s)
                c2 = sum(1 for s in fams if q in s and img[r] in s)
                if c1 != c2:
                    return False
        return True
    def ok():
        for s in fams:
            t = {img[p] for p in s if img[p] is not None}
            if len(t) == 7:
                if frozenset(t) not in famset:
                    return False
            elif t:
                if not any(t <= set(F) for F in fams):
                    return False
        return True
    def dfs(k):
        if k == 14:
            elts.append(tuple(img))
            return
        p = order[k]
        for q in range(14):
            if used[q] or deg[q] != deg[p]:
                continue
            if not sigok(p, q):
                continue
            img[p] = q
            used[q] = True
            if ok():
                dfs(k+1)
            img[p] = None
            used[q] = False
    dfs(0)
    return elts

def compose(a, b):
    return tuple(a[b[i]] for i in range(14))

for f in ['output/artifacts/brouwer42.txt'] + sorted(glob.glob('output/artifacts/clique*.txt')):
    v = load(f)
    e1 = aut_group(v, 0)
    e2 = aut_group(v, 5)
    S1, S2 = set(e1), set(e2)
    assert len(e1) == len(S1) and len(e2) == len(S2)
    assert S1 == S2, (f, len(S1), len(S2))
    # closure + identity + each maps family to itself (re-verify)
    fams = set(frozenset(i for i in range(14) if (x >> (13 - i)) & 1) for x in v)
    assert tuple(range(14)) in S1
    for a in list(S1)[:50]:
        for b in list(S1)[:50]:
            assert compose(a, b) in S1
    print(f"{f}: |Stab|={len(S1)} (two orders agree, closure ok)")
    # point degrees
    deg = sorted(sum(1 for x in v if (x >> (13 - i)) & 1) for i in range(14))
    print("  degrees:", deg)
