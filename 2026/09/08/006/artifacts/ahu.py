"""AHU canonical invariant for functional digraphs + fast grouping."""
import itertools
from collections import deque

def ahu_code(a):
    n = len(a)
    pre = [[] for _ in range(n)]
    for r in range(n):
        pre[a[r]].append(r)
    # find cycle nodes via indegree pruning
    indeg = [len(pre[q]) for q in range(n)]
    from collections import deque as dq
    q = dq([i for i in range(n) if indeg[i] == 0])
    removed = [False]*n
    while q:
        u = q.popleft()
        removed[u] = True
        v = a[u]
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
    on_cycle = [not r for r in removed]
    # tree codes: process non-cycle nodes bottom-up (order of removal)
    code = [None]*n
    # recompute removal order
    indeg2 = [len(pre[i]) for i in range(n)]
    qq = dq([i for i in range(n) if indeg2[i] == 0])
    order = []
    while qq:
        u = qq.popleft()
        order.append(u)
        v = a[u]
        indeg2[v] -= 1
        if indeg2[v] == 0 and not on_cycle[v]:
            qq.append(v)
    for u in order:
        kids = [code[c] for c in pre[u] if not on_cycle[c]]
        kids.sort()
        code[u] = tuple(kids)
    for c in range(n):
        if on_cycle[c]:
            kids = [code[x] for x in pre[c] if not on_cycle[x]]
            kids.sort()
            code[c] = tuple(kids)
    # components: walk cycles
    seen = [False]*n
    comps = []
    for c in range(n):
        if on_cycle[c] and not seen[c]:
            cyc = []
            u = c
            while not seen[u]:
                seen[u] = True
                cyc.append(u)
                u = a[u]
            # cyc is in a-order; rotate to min tree-code sequence
            seq = [code[u] for u in cyc]
            k = len(seq)
            best = min(tuple(seq[(i+j) % k] for j in range(k)) for i in range(k))
            comps.append((k, best))
    comps.sort()
    return (tuple(comps),)

def canon_a_bruteforce(a):
    n = len(a)
    best = None
    for p in itertools.permutations(range(n)):
        inv = [0]*n
        for qq in range(n):
            inv[p[qq]] = qq
        img = tuple(p[a[inv[i]]] for i in range(n))
        if best is None or img < best:
            best = img
    return best

if __name__ == '__main__':
    import random, time
    # completeness check: random collisions between AHU code and brute-force canon on n=6
    random.seed(0)
    from itertools import product
    n = 5
    groups = {}
    for a in product(range(n), repeat=n):
        c1 = ahu_code(a)
        c2 = canon_a_bruteforce(a)
        if c1 not in groups:
            groups[c1] = set()
        groups[c1].add(c2)
    bad = {k: v for k, v in groups.items() if len(v) > 1}
    print("n=5: AHU groups:", len(groups), "colliding (one AHU -> many brute):", len(bad))
    # reverse: same brute -> same AHU (must hold; soundness)
    rev = {}
    for a in product(range(n), repeat=n):
        c1 = ahu_code(a); c2 = canon_a_bruteforce(a)
        rev.setdefault(c2, set()).add(c1)
    bad2 = {k: v for k, v in rev.items() if len(v) > 1}
    print("n=5: brute groups:", len(rev), "unsound (one brute -> many AHU):", len(bad2))
