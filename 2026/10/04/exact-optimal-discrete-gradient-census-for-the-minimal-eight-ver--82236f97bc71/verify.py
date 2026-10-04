#!/usr/bin/env python3
from collections import Counter, deque

FACETS = [
    (1,2,4),(1,2,7),(1,2,8),(1,3,4),(1,3,5),(1,3,6),
    (1,5,6),(1,7,8),(2,3,5),(2,3,7),(2,3,8),(2,4,5),
    (3,4,8),(3,6,7),(4,5,6),(4,6,8),(6,7,8),
]
N = len(FACETS)
EDGES = sorted({tuple(sorted((a,b))) for F in FACETS for a,b in ((F[0],F[1]),(F[0],F[2]),(F[1],F[2]))})
EINDEX = {e:i for i,e in enumerate(EDGES)}
F_EDGES = [[EINDEX[tuple(sorted((F[a],F[b])))] for a,b in ((0,1),(0,2),(1,2))] for F in FACETS]
EDGE_FACETS = [[] for _ in EDGES]
for t, es in enumerate(F_EDGES):
    for e in es:
        EDGE_FACETS[e].append(t)
ARROWS = [[u for u in EDGE_FACETS[e] if u != t] for t in range(N) for e in []]  # documentation-only shape
OPTIONS = [[(e, tuple(u for u in EDGE_FACETS[e] if u != t)) for e in F_EDGES[t]] for t in range(N)]
ALL_EDGE_MASK = (1 << len(EDGES)) - 1

assert N == 17 and len(EDGES) == 24
assert Counter(map(len, EDGE_FACETS)) == Counter({2:21, 3:3})

def extend_reach(reach, u, targets):
    """Return a new transitive-closure list after adding u->targets, or None on a cycle."""
    newbits = 0
    for v in targets:
        if v == u or ((reach[v] >> u) & 1):
            return None
        newbits |= (1 << v) | reach[v]
    # u has not previously received outgoing arcs in this search ordering.
    nr = reach.copy()
    nr[u] |= newbits
    ub = 1 << u
    # Any predecessor of u now reaches everything newly reachable from u.
    for p in range(N):
        if p != u and (nr[p] & ub):
            nr[p] |= nr[u]
    # Transitive closure can propagate through predecessors in one sweep because
    # every predecessor already reached u before this insertion.
    return nr

cycle_cache = {}
def residual_cycle_length(used_mask):
    residual_mask = ALL_EDGE_MASK ^ used_mask
    if residual_mask in cycle_cache:
        return cycle_cache[residual_mask]
    redges = [EDGES[i] for i in range(len(EDGES)) if (residual_mask >> i) & 1]
    if len(redges) != 8:
        cycle_cache[residual_mask] = 0
        return 0
    adj = {v:set() for v in range(1,9)}
    for a,b in redges:
        adj[a].add(b); adj[b].add(a)
    # connectedness
    seen={1}; stack=[1]
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); stack.append(w)
    if len(seen) != 8:
        cycle_cache[residual_mask] = 0
        return 0
    # peel leaves; a connected 8-edge graph on 8 vertices is unicyclic,
    # and the unpeeled vertices are exactly its unique cycle.
    deg={v:len(adj[v]) for v in adj}
    q=deque(v for v in adj if deg[v] <= 1)
    removed=set()
    while q:
        v=q.popleft()
        if v in removed:
            continue
        removed.add(v)
        for w in adj[v]:
            if w not in removed:
                deg[w]-=1
                if deg[w] == 1:
                    q.append(w)
    ell=8-len(removed)
    if ell < 3:
        ell=0
    cycle_cache[residual_mask]=ell
    return ell

def enumerate_one_critical_triangle():
    hist=Counter(); total=0; bad_residual=0
    for critical in range(N):
        order=[t for t in range(N) if t != critical]
        # Most constrained first: prioritize triangles incident to degree-3 edges,
        # then deterministic index order. This only changes traversal order.
        order.sort(key=lambda t:(-sum(len(EDGE_FACETS[e]) for e in F_EDGES[t]), t))
        def rec(k, used, reach):
            nonlocal total, bad_residual
            if k == len(order):
                total += 1
                ell=residual_cycle_length(used)
                if not ell:
                    bad_residual += 1
                else:
                    hist[ell] += 1
                return
            t=order[k]
            for e, targets in OPTIONS[t]:
                bit=1<<e
                if used & bit:
                    continue
                nr=extend_reach(reach,t,targets)
                if nr is not None:
                    rec(k+1, used|bit, nr)
        rec(0,0,[0]*N)
    return total,hist,bad_residual

def enumerate_no_critical_triangle():
    order=list(range(N))
    order.sort(key=lambda t:(-sum(len(EDGE_FACETS[e]) for e in F_EDGES[t]), t))
    count=0
    def rec(k,used,reach):
        nonlocal count
        if k==len(order):
            count += 1
            return
        t=order[k]
        for e,targets in OPTIONS[t]:
            bit=1<<e
            if used & bit:
                continue
            nr=extend_reach(reach,t,targets)
            if nr is not None:
                rec(k+1,used|bit,nr)
    rec(0,0,[0]*N)
    return count

total,hist,bad=enumerate_one_critical_triangle()
full12=enumerate_no_critical_triangle()
expected={3:754080,4:706489,5:365173,6:131021,7:31621,8:3839}
assert total == 1992223, (total,hist)
assert dict(sorted(hist.items())) == expected, hist
assert bad == 0, bad
assert full12 == 0, full12
weighted=sum(k*v for k,v in hist.items())
assert weighted == 7952246, weighted
optimal=8*weighted
assert optimal == 63617968, optimal
print("VERIFY_OK facets=17 edges=24 full12=0 acyclic16=1992223 "
      "cycle_hist=3:754080,4:706489,5:365173,6:131021,7:31621,8:3839 "
      "weighted=7952246 optimal_fields=63617968")
