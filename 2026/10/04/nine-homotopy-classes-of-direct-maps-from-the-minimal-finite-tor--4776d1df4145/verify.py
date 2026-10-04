#!/usr/bin/env python3
from collections import Counter, deque
from itertools import product

# C is the four-point minimal circle: 0,1 are minimal and 2,3 maximal.
C = range(4)
def cle(a, b):
    return a == b or (a < 2 and b >= 2)

# T = C x C with coordinatewise order.
pts = [(i, j) for i in C for j in C]
index = {p: k for k, p in enumerate(pts)}
N = len(pts)
def tle(p, q):
    return cle(p[0], q[0]) and cle(p[1], q[1])

pred = {k: [j for j in range(N) if j != k and tle(pts[j], pts[k])] for k in range(N)}
rank = lambda p: int(p[0] >= 2) + int(p[1] >= 2)
order = sorted(range(N), key=lambda k: rank(pts[k]))

# Exhaustive enumeration of all monotone maps T -> C.
maps = []
a = [None] * N
def rec(t):
    if t == N:
        maps.append(tuple(a))
        return
    k = order[t]
    for v in C:
        if all(a[j] is None or cle(a[j], v) for j in pred[k]):
            a[k] = v
            rec(t + 1)
            a[k] = None
rec(0)
assert len(maps) == 2836
mindex = {m: i for i, m in enumerate(maps)}
assert len(mindex) == len(maps)

# Independent exact count via order ideals D=f^{-1}({0,1}).
# On each comparability component of D (and of its complement), the map must be constant.
comp_adj = [[j for j in range(N) if j != i and (tle(pts[i], pts[j]) or tle(pts[j], pts[i]))] for i in range(N)]
def ncomp(vertices):
    s = set(vertices)
    c = 0
    while s:
        c += 1
        q = [s.pop()]
        while q:
            u = q.pop()
            for v in comp_adj[u]:
                if v in s:
                    s.remove(v)
                    q.append(v)
    return c

hist = Counter()
weighted = 0
ideals = 0
for mask in range(1 << N):
    ok = True
    for x in range(N):
        if (mask >> x) & 1:
            for y in pred[x]:
                if not ((mask >> y) & 1):
                    ok = False
                    break
        if not ok:
            break
    if not ok:
        continue
    ideals += 1
    D = [i for i in range(N) if (mask >> i) & 1]
    U = [i for i in range(N) if not ((mask >> i) & 1)]
    cd = ncomp(D) if D else 0
    cu = ncomp(U) if U else 0
    hist[(cd, cu)] += 1
    weighted += 2 ** (cd + cu)
assert ideals == 430
assert weighted == 2836
assert hist == Counter({
    (0,1):1, (1,0):1, (1,1):228, (1,2):82, (1,3):16, (1,4):1,
    (2,1):82, (2,2):2, (3,1):16, (4,1):1
})

# Comparable maps are connected by single-coordinate raises: for f<=g, raise a
# maximal domain point among coordinates where f and g differ, then iterate.
# Thus the undirected graph below has exactly the mapping-poset components.
adj = [[] for _ in maps]
for i, m in enumerate(maps):
    mm = list(m)
    for k, v in enumerate(m):
        if v < 2:
            for w in (2, 3):
                mm[k] = w
                g = tuple(mm)
                j = mindex.get(g)
                if j is not None:
                    adj[i].append(j)
                    adj[j].append(i)
            mm[k] = v

seen = [False] * len(maps)
components = []
for s in range(len(maps)):
    if seen[s]:
        continue
    seen[s] = True
    q = [s]
    comp = []
    while q:
        u = q.pop()
        comp.append(u)
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                q.append(v)
    components.append(comp)
csizes = sorted((len(c) for c in components), reverse=True)
assert csizes == [2828] + [1] * 8
big = next(c for c in components if len(c) == 2828)
bigset = {maps[i] for i in big}
assert all(tuple([v] * N) in bigset for v in C)

# Integral degree on C: evaluate the cocycle supported on the edge 0<2
# against the standard 1-cycle (0,2)-(1,2)+(1,3)-(0,3).
def eval_edge(a, b):
    if a == b:
        return 0
    assert a < 2 and b >= 2
    return 1 if (a, b) == (0, 2) else 0

def degree_on_slice(values):
    a0, b0, a1, b1 = values
    return eval_edge(a0,b0) - eval_edge(a1,b0) + eval_edge(a1,b1) - eval_edge(a0,b1)

def degree_pair(m):
    first = [m[index[(0,0)]], m[index[(2,0)]], m[index[(1,0)]], m[index[(3,0)]]]
    second = [m[index[(0,0)]], m[index[(0,2)]], m[index[(0,1)]], m[index[(0,3)]]]
    return degree_on_slice(first), degree_on_slice(second)

profile = Counter(degree_pair(m) for m in maps)
assert profile == Counter({(0,0):2828, (1,0):2, (-1,0):2, (0,1):2, (0,-1):2})

# The eight singleton components are exactly automorphisms of C after a projection.
autos = []
for pm in ((0,1),(1,0)):
    for px in ((2,3),(3,2)):
        perm = {0:pm[0], 1:pm[1], 2:px[0], 3:px[1]}
        autos.append(perm)
proj_maps = set()
for perm in autos:
    proj_maps.add(tuple(perm[x] for x,y in pts))
    proj_maps.add(tuple(perm[y] for x,y in pts))
assert len(proj_maps) == 8
isolated = {maps[c[0]] for c in components if len(c) == 1}
assert isolated == proj_maps
assert all(degree_pair(m) != (0,0) for m in isolated)
assert all(degree_pair(m) == (0,0) for c in components if len(c) > 1 for m in (maps[c[0]],))

print('VERIFY_OK maps=2836 ideals=430 components=2828+8x1 degree_profile=2828,2,2,2,2 isolated=8_projections')
