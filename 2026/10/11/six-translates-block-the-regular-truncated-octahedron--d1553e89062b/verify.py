#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations, product, combinations

def vadd(a,b): return tuple(a[i]+b[i] for i in range(3))
def vsub(a,b): return tuple(a[i]-b[i] for i in range(3))
def vscale(q,a): return tuple(q*a[i] for i in range(3))
def l1(a): return sum(abs(x) for x in a)
def d2(a,b): return sum((a[i]-b[i])**2 for i in range(3))

def inside_P(x):
    return all(abs(t) < 1 for t in x) and l1(x) < F(3,2)

def boundary_P(x):
    feasible = all(abs(t) <= 1 for t in x) and l1(x) <= F(3,2)
    active = any(abs(t) == 1 for t in x) or l1(x) == F(3,2)
    return feasible and active

centers = [
    (F(-5,8),F(-7,8),F(0)),
    (F(-1,2),F(1,2),F(-1,2)),
    (F(-1,2),F(1,2),F(1,2)),
    (F(3,8),F(-1,2),F(-5,8)),
    (F(3,8),F(-1,2),F(5,8)),
    (F(7,8),F(5,8),F(0)),
]

assert all(boundary_P(z) for z in centers)
for i,j in combinations(range(6),2):
    assert not inside_P(vsub(centers[i],centers[j]))

base = (F(1),F(1,2),F(0))
vertices = set()
for p in set(permutations(base)):
    for s in product((-1,1),repeat=3):
        vertices.add(tuple(F(s[i])*p[i] for i in range(3)))
assert len(vertices) == 24
assert all(boundary_P(v) for v in vertices)

facets = []
for axis in range(3):
    for sign in (-1,1):
        fv = [v for v in vertices if v[axis] == sign]
        assert len(fv) == 4
        facets.append((f"x{axis+1}={sign}",fv))
for sign in product((-1,1),repeat=3):
    fv = [v for v in vertices
          if sum(F(sign[i])*v[i] for i in range(3)) == F(3,2)]
    assert len(fv) == 6
    facets.append((f"s={sign}",fv))
assert len(facets) == 14

def ordered_cycle(fv):
    adj = {
        v: sorted(w for w in fv if w != v and d2(v,w) == F(1,2))
        for v in fv
    }
    assert all(len(nbrs) == 2 for nbrs in adj.values())
    start = min(fv)
    second = min(adj[start])
    cyc = [start, second]
    prev, cur = start, second
    while True:
        nxt = [w for w in adj[cur] if w != prev][0]
        if nxt == start:
            break
        cyc.append(nxt)
        prev, cur = cur, nxt
    assert len(cyc) == len(fv)
    assert all(d2(cyc[i],cyc[(i+1)%len(cyc)]) == F(1,2)
               for i in range(len(cyc)))
    return cyc

def centroid(points):
    n = F(len(points))
    return tuple(sum(p[i] for p in points)/n for i in range(3))

def shifted_slack(p,z):
    q = vsub(p,z)
    return min(
        F(1)-abs(q[0]),
        F(1)-abs(q[1]),
        F(1)-abs(q[2]),
        F(3,2)-l1(q),
    )

def covered_by(tri,z):
    return all(shifted_slack(p,z) > 0 for p in tri)

leaf_count = 0
max_depth = 0
min_slack = None
facet_counts = {}

def certify_triangle(tri, depth=0):
    global leaf_count, max_depth, min_slack
    for z in centers:
        if covered_by(tri,z):
            slack = min(shifted_slack(p,z) for p in tri)
            min_slack = slack if min_slack is None else min(min_slack,slack)
            leaf_count += 1
            max_depth = max(max_depth,depth)
            return 1
    assert depth < 8
    a,b,c = tri
    ab = vscale(F(1,2),vadd(a,b))
    bc = vscale(F(1,2),vadd(b,c))
    ca = vscale(F(1,2),vadd(c,a))
    children = [
        (a,ab,ca),
        (ab,b,bc),
        (ca,bc,c),
        (ab,bc,ca),
    ]
    return sum(certify_triangle(child,depth+1) for child in children)

for name,fv in facets:
    cyc = ordered_cycle(fv)
    ctr = centroid(fv)
    before = leaf_count
    for i in range(len(cyc)):
        certify_triangle((ctr,cyc[i],cyc[(i+1)%len(cyc)]))
    facet_counts[name] = leaf_count-before

assert leaf_count == 438
assert max_depth == 3
assert min_slack == F(1,16)

expected = {
    "x1=-1":64, "x1=1":22,
    "x2=-1":10, "x2=1":64,
    "x3=-1":52, "x3=1":52,
    "s=(-1, -1, -1)":30, "s=(-1, -1, 1)":30,
    "s=(-1, 1, -1)":6, "s=(-1, 1, 1)":6,
    "s=(1, -1, -1)":6, "s=(1, -1, 1)":6,
    "s=(1, 1, -1)":45, "s=(1, 1, 1)":45,
}
assert facet_counts == expected

print("VERIFY_OK")
print("vertices =",len(vertices))
print("facets =",len(facets))
print("terminal_triangles =",leaf_count)
print("max_subdivision_depth =",max_depth)
print("minimum_exact_slack =",min_slack)
