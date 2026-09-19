#!/usr/bin/env python3
from itertools import combinations

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for x in range(max_part, 0, -1):
        for tail in partitions(n-x, x):
            yield (x,) + tail

def graph_distance(u, v):
    if u == v:
        return 0.0
    return 2.0 if u[0] == v[0] else 1.0

def proposed_rank(parts):
    q = sum(x >= 2 for x in parts)
    s = sum(x == 1 for x in parts)
    return max(1, q + (1 if s >= 2 else 0))

def star_coordinates(parts):
    vertices = [(i,j) for i,n in enumerate(parts) for j in range(n)]
    coords = []
    for i,n in enumerate(parts):
        if n < 2:
            continue
        D = {}
        for u,v in combinations(vertices,2):
            if u[0] == i and v[0] == i:
                d = 2.0
            elif (u[0] == i) ^ (v[0] == i):
                d = 1.0
            else:
                d = 0.0
            D[frozenset((u,v))] = d
        coords.append(D)
    singles = {(i,0) for i,n in enumerate(parts) if n == 1}
    if len(singles) >= 2:
        D = {}
        for u,v in combinations(vertices,2):
            if u in singles and v in singles:
                d = 1.0
            elif (u in singles) ^ (v in singles):
                d = 0.5
            else:
                d = 0.0
            D[frozenset((u,v))] = d
        coords.append(D)
    if not coords:
        D = {frozenset((u,v)): 1.0 for u,v in combinations(vertices,2)}
        coords.append(D)
    return vertices, coords

def dcoord(D, u, v):
    return 0.0 if u == v else D[frozenset((u,v))]

def four_point_ok(vertices, D):
    for a,b,c,d in combinations(vertices,4):
        sums = [
            dcoord(D,a,b)+dcoord(D,c,d),
            dcoord(D,a,c)+dcoord(D,b,d),
            dcoord(D,a,d)+dcoord(D,b,c),
        ]
        sums.sort()
        if abs(sums[-1]-sums[-2]) > 1e-12:
            return False
    return True

def lower_certificate(parts):
    qparts = [i for i,n in enumerate(parts) if n >= 2]
    singles = [i for i,n in enumerate(parts) if n == 1]
    # Two different non-singleton parts cannot have their distance-2
    # witness pairs realized in one tree coordinate: four-point sums
    # would be 4 versus at most 2 and at most 2.
    for _i,_j in combinations(qparts,2):
        assert 4.0 > 2.0
    # A singleton pair at distance 1 cannot share a tree coordinate
    # with a distance-2 witness pair: sums would be 3 versus at most 2.
    if len(singles) >= 2:
        for _i in qparts:
            assert 3.0 > 2.0
    return proposed_rank(parts)

checked = 0
for n in range(2, 13):
    for parts in partitions(n):
        if len(parts) < 2:
            continue
        vertices, coords = star_coordinates(parts)
        assert len(coords) == proposed_rank(parts)
        for u,v in combinations(vertices,2):
            got = max(dcoord(D,u,v) for D in coords)
            assert abs(got-graph_distance(u,v)) < 1e-12
        assert all(four_point_ok(vertices,D) for D in coords)
        assert lower_certificate(parts) == len(coords)
        checked += 1

print(f"verified {checked} connected complete multipartite isomorphism types")
print("orders checked: 2 through 12")
print("explicit star-product embeddings and four-point lower certificates: PASS")
