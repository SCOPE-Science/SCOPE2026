from itertools import combinations
from collections import deque

def book_graph(r):
    n = 2 + 2*r
    adj = [set() for _ in range(n)]
    adj[0].add(1); adj[1].add(0)
    for i in range(r):
        a = 2 + 2*i
        b = a + 1
        for u,v in ((0,a),(a,b),(b,1)):
            adj[u].add(v); adj[v].add(u)
    return adj

def distances(adj):
    D = []
    for s in range(len(adj)):
        d = [-1]*len(adj)
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        D.append(d)
    return D

def geodesic_internal_masks(adj, D, s, t):
    target = D[s][t]
    out = set()
    def dfs(u, path):
        if len(path)-1 > target:
            return
        if u == t:
            if len(path)-1 == target:
                mask = 0
                for z in path[1:-1]:
                    mask |= 1 << z
                out.add(mask)
            return
        for v in adj[u]:
            if v in path:
                continue
            if D[s][v] != D[s][u] + 1:
                continue
            if D[s][v] + D[v][t] != target:
                continue
            dfs(v, path + [v])
    dfs(s, [s])
    assert out
    return tuple(sorted(out))

def all_pair_geodesics(adj, D):
    pair_masks = {}
    for u,v in combinations(range(len(adj)),2):
        pair_masks[(u,v)] = geodesic_internal_masks(adj,D,u,v)
    return pair_masks

def visible(pair_masks, Xmask, u, v):
    if u > v:
        u,v = v,u
    return any((m & Xmask) == 0 for m in pair_masks[(u,v)])

def is_variant(adj, pair_masks, Xmask, kind):
    n = len(adj)
    for u,v in combinations(range(n),2):
        xu = (Xmask >> u) & 1
        xv = (Xmask >> v) & 1
        required = (
            kind == "total" or
            (kind == "mutual" and xu and xv) or
            (kind == "outer" and (xu or xv)) or
            (kind == "dual" and (xu == xv))
        )
        if required and not visible(pair_masks,Xmask,u,v):
            return False
    return True

def is_independent(adj, Xmask):
    for u in range(len(adj)):
        if (Xmask >> u) & 1:
            if any((Xmask >> v) & 1 for v in adj[u]):
                return False
    return True

parameters = 0
subsets = 0
variant_checks = 0

for r in range(2,8):
    adj = book_graph(r)
    D = distances(adj)
    pair_masks = all_pair_geodesics(adj,D)
    n = len(adj)
    internal_mask = sum(1 << v for v in range(2,n))
    indep_expected = {
        (1 << 1) | sum(1 << (2+2*i) for i in range(r)),
        (1 << 0) | sum(1 << (3+2*i) for i in range(r)),
    }

    for kind in ("mutual","outer","dual","total"):
        best = -1
        maxima = set()
        for Xmask in range(1 << n):
            subsets += 1
            variant_checks += 1
            k = Xmask.bit_count()
            if k < best:
                continue
            if is_variant(adj,pair_masks,Xmask,kind):
                if k > best:
                    best = k
                    maxima = set()
                maxima.add(Xmask)
        assert best == 2*r, (r,kind,best)
        assert maxima == {internal_mask}, (r,kind,maxima)

    best_i = -1
    maxima_i = set()
    for Xmask in range(1 << n):
        subsets += 1
        k = Xmask.bit_count()
        if k < best_i or not is_independent(adj,Xmask):
            continue
        if is_variant(adj,pair_masks,Xmask,"mutual"):
            if k > best_i:
                best_i = k
                maxima_i = set()
            maxima_i.add(Xmask)
    assert best_i == r+1, (r,best_i)
    assert maxima_i == indep_expected, (r,maxima_i,indep_expected)
    parameters += 1

print("VERIFY_OK")
print("book_parameters_checked =", parameters)
print("subset_variant_trials =", subsets)
print("pair_visibility_variant_checks =", variant_checks)
print("parameters r = 2..7")
print("all four visibility numbers equal 2r")
print("the common maximum set is unique and equals the 2r internal page vertices")
print("all independent mutual-visibility numbers equal r+1")
print("the two maximum independent sets match the theorem")
