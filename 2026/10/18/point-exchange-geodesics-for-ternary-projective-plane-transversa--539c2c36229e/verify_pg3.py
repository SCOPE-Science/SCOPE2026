#!/usr/bin/env python3
"""Exhaustive finite certificate for the point-exchange graph of PG(2,3).

Run with Python 3.9+ only: python verify_pg3.py. No external data or libraries.
"""
from collections import Counter, deque
from itertools import combinations, product
import json

Q = 3
N = 13
ALL = (1 << N) - 1


def normalize(v):
    pivot = next(x for x in v if x)
    return tuple((x * pow(pivot, -1, Q)) % Q for x in v)


def projective_geometry():
    # Homogeneous-coordinate dot-product incidence, normalized independently.
    vectors = sorted({normalize(v) for v in product(range(Q), repeat=3)
                      if any(v)})
    assert len(vectors) == N
    line_masks = [sum(1 << i for i, p in enumerate(vectors)
                      if sum(a*b for a, b in zip(row, p)) % Q == 0)
                  for row in vectors]
    return vectors, line_masks


def affine_geometry():
    # Different construction: 9 affine points + 4 directions at infinity.
    pts = [(x, y) for x in range(Q) for y in range(Q)]
    pts += [('infinity', m) for m in range(Q)] + [('infinity', 'vertical')]
    p_index = {p: i for i, p in enumerate(pts)}
    line_sets = []
    for slope in range(Q):
        for intercept in range(Q):
            arr = [(x, (slope*x + intercept) % Q) for x in range(Q)]
            arr.append(('infinity', slope))
            line_sets.append(sum(1 << p_index[p] for p in arr))
    for c in range(Q):
        arr = [(c, y) for y in range(Q)] + [('infinity', 'vertical')]
        line_sets.append(sum(1 << p_index[p] for p in arr))
    line_sets.append(sum(1 << p_index[p] for p in pts if p[0] == 'infinity'))
    assert len(pts) == len(line_sets) == N
    return pts, line_sets


def incidence_axioms(lines):
    assert len(set(lines)) == N
    assert all(l.bit_count() == 4 for l in lines)
    assert all(sum(bool(l & (1 << p)) for l in lines) == 4 for p in range(N))
    assert all((a & b).bit_count() == 1 for a,b in combinations(lines, 2))
    assert all(sum(bool((l >> a)&1 and (l >> b)&1) for l in lines) == 1
               for a,b in combinations(range(N),2))


def is_hit(mask, lines):
    return all(mask & l for l in lines)


def move_neighbors(mask, allowed):
    outside = ALL ^ mask
    for a in range(N):
        if not mask & (1 << a):
            continue
        for b in range(N):
            if outside & (1 << b):
                nxt = mask ^ (1 << a) ^ (1 << b)
                if nxt in allowed:
                    yield nxt


def components(allowed, adjacency):
    unseen = set(allowed)
    out = []
    while unseen:
        root = unseen.pop()
        component = {root}
        stack = [root]
        while stack:
            a = stack.pop()
            for b in adjacency[a]:
                if b in unseen:
                    unseen.remove(b)
                    component.add(b)
                    stack.append(b)
        out.append(component)
    return out


def geodesic_exchange_certificate(arr, allowed):
    # A finite universal test for the *directed* increasing-intersection exchange axiom.
    # Each successful swap reduces the Johnson distance to any specified target by one.
    tested = 0
    for a in arr:
        for b in arr:
            if a == b:
                continue
            tested += 1
            out = a & ~b
            want = b & ~a
            found = False
            while out and not found:
                bit_a = out & -out
                out -= bit_a
                opts = want
                while opts:
                    bit_b = opts & -opts
                    opts -= bit_b
                    if a ^ bit_a ^ bit_b in allowed:
                        found = True
                        break
            assert found, ('geodesic exchange missing', a, b)
    assert tested == len(arr)*(len(arr)-1)
    return tested


def bfs_distances(root, adjacency):
    dist = {root: 0}
    todo = deque([root])
    while todo:
        x = todo.popleft()
        for y in adjacency[x]:
            if y not in dist:
                dist[y] = dist[x]+1
                todo.append(y)
    return dist


def main():
    vectors, dual = projective_geometry()
    affine_pts, affine_lines = affine_geometry()
    incidence_axioms(dual)
    incidence_axioms(affine_lines)

    # An explicit point bijection proves the two independently created planes coincide.
    pmap = {}
    for i,(x,y,z) in enumerate(vectors):
        if z != 0:
            image = (x * pow(z,-1,Q) % Q, y * pow(z,-1,Q) % Q)
        elif x != 0:
            image = ('infinity', y * pow(x,-1,Q) % Q)
        else:
            image = ('infinity','vertical')
        pmap[i] = affine_pts.index(image)
    assert len(set(pmap.values())) == N
    remap_lines = {sum(1 << pmap[i] for i in range(N) if l & (1 << i))
                   for l in dual}
    assert remap_lines == set(affine_lines)

    # First classifier: homogeneous-coordinate masks, all 8192 subsets.
    P = {k: [x for x in range(1<<N) if x.bit_count()==k and is_hit(x,dual)]
         for k in range(N+1)}
    # Second classifier: independent affine construction, combinations rather than masks.
    A = {k: {sum(1<<i for i in inds) for inds in combinations(range(N),k)
             if is_hit(sum(1<<i for i in inds), affine_lines)}
         for k in range(N+1)}
    for k in range(N+1):
        image = {sum(1<<pmap[i] for i in range(N) if mask & (1<<i))
                 for mask in P[k]}
        assert image == A[k], ('plane disagreement',k)

    census = {str(k):len(P[k]) for k in range(N+1)}
    assert [len(P[k]) for k in range(4,14)] == [13,117,702,1248,1170,702,286,78,13,1]
    assert all(not P[k] for k in range(4))
    assert set(P[4]) == set(dual)

    # Every five-point transversal consists of a line and an external point.
    lines_inside = lambda s:sum((s&l)==l for l in dual)
    assert all(lines_inside(s)==1 for s in P[5])
    assert len(P[5]) == 13*9
    adj5 = {s:set(move_neighbors(s,set(P[5]))) for s in P[5]}
    comps5 = components(P[5],adj5)
    assert Counter(map(len,comps5))==Counter({9:13})
    assert all(all(len(adj5[s])==8 for s in comp) for comp in comps5)
    assert sum(map(len,adj5.values()))//2 == 468

    # Six-point transversal geometry: one line + two points, or triangle interiors.
    classify6 = Counter(lines_inside(s) for s in P[6])
    assert classify6 == Counter({1:468, 0:234})
    triangles = set()
    for a,b,c in combinations(dual,3):
        ab,ac,bc = a&b, a&c, b&c
        if len({ab,ac,bc})<3:
            continue
        triangle = (a|b|c) & ~(ab|ac|bc)
        assert triangle.bit_count() == 6
        triangles.add(triangle)
    assert len(triangles)==234
    assert triangles == {s for s in P[6] if lines_inside(s)==0}

    # The six-transversal family is not a matroid basis family: the stronger
    # basis-exchange requirement fails for this explicitly checked triple.
    first, second, removed = 63, 1182, 0
    assert first in P[6] and second in P[6]
    assert first & (1 << removed) and not second & (1 << removed)
    assert all((first ^ (1 << removed) ^ (1 << b)) not in set(P[6])
               for b in range(N) if second & (1 << b) and not first & (1 << b))

    # One pairwise exchange witness for EVERY directed pair and EVERY k >= 6.
    tested = {}
    for k in range(6,N+1):
        arr=P[k]
        allowed=set(arr)
        tested[str(k)] = geodesic_exchange_certificate(arr,allowed)

    # Separate shortest-path check, with independently constructed adjacency.
    # Runs BFS from all 702 vertices (not relying on the greedy-check routine).
    allowed6=set(P[6])
    adj6={s:set(move_neighbors(s,allowed6)) for s in P[6]}
    assert all(s in adj6[t] for s,ns in adj6.items() for t in ns)
    assert len(components(P[6],adj6))==1
    classes={s:'line' if lines_inside(s) else 'triangle' for s in P[6]}
    degree_hist=Counter(len(adj6[s]) for s in P[6])
    assert degree_hist==Counter({23:468,18:234})
    edge_types=Counter(tuple(sorted((classes[s],classes[t]))) for s in P[6]
                       for t in adj6[s] if s<t)
    assert edge_types==Counter({('line','line'):3978,('line','triangle'):2808,
                               ('triangle','triangle'):702})
    eccentricity=Counter()
    for s in P[6]:
        d=bfs_distances(s,adj6)
        assert len(d)==702
        assert all(dist==6-(s&t).bit_count() for t,dist in d.items())
        eccentricity[(classes[s],max(d.values()))]+=1
    assert eccentricity==Counter({('line',5):468,('triangle',6):234})

    # The direct Johnson-metric maxima give exact radii/diameters at every k>=6.
    metrics={}
    for k in range(6,N+1):
        ecc=[max(k-(s&t).bit_count() for t in P[k]) for s in P[k]]
        metrics[str(k)]={'radius':min(ecc),'diameter':max(ecc)}
    assert metrics == {
      '6':{'radius':5,'diameter':6},'7':{'radius':6,'diameter':6},
      '8':{'radius':5,'diameter':5},'9':{'radius':4,'diameter':4},
      '10':{'radius':3,'diameter':3},'11':{'radius':2,'diameter':2},
      '12':{'radius':1,'diameter':1},'13':{'radius':0,'diameter':0}}

    print(json.dumps({
        'universe_points':N,'lines':len(dual),'census':census,
        'k5_components':{'count':len(comps5),'size':9,'edges':468},
        'k6_classification':dict(classify6),
        'k6_degree_hist':dict(degree_hist),
        'k6_edge_types':{'%s/%s'%t:n for t,n in sorted(edge_types.items())},
        'k6_eccentricities':{'%s/%s'%t:n for t,n in sorted(eccentricity.items())},
        'ordered_pairs_checked':tested,'radius_diameter':metrics,
        'certificate':'all targeted exchanges exist; all BFS distances agree with Johnson distance'
    },sort_keys=True,indent=2))

if __name__=='__main__':
    main()
