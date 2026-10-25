"""Direct mod-two checks of the cotree formula for two-independence complexes.

This script verifies finite examples only; the general homotopy classification
is proved by simplicial-join and graph-edge-attachment arguments.
"""
from itertools import combinations
from random import Random


def construct(kind, left, right):
    n1, e1, p1 = left
    n2, e2, p2 = right
    edges = set(e1) | {(u + n1, v + n1) for u, v in e2}
    if kind == 'join':
        edges.update((u, n1 + v) for u in range(n1) for v in range(n2))
        poly = dict(p1)
        for d, rank in p2.items():
            poly[d] = poly.get(d, 0) + rank
        poly[1] = poly.get(1, 0) + n1 * n2 - 1
    else:
        poly = {}
        for d, a in p1.items():
            for e, b in p2.items():
                poly[d + e + 1] = poly.get(d + e + 1, 0) + a * b
    return n1 + n2, edges, {d: x for d, x in poly.items() if x}


def mod2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)


def homology(n, edges):
    edge_set = set(frozenset(e) for e in edges)
    def admissible(s):
        present = set(s)
        visited = set()
        for v in s:
            if v not in visited:
                seen = {v}
                todo = [v]
                while todo:
                    w = todo.pop()
                    for z in present:
                        if z not in seen and frozenset((w,z)) in edge_set:
                            seen.add(z)
                            todo.append(z)
                if len(seen) > 2:
                    return False
                visited.update(seen)
        return True
    faces = {k: [s for s in combinations(range(n), k+1) if admissible(s)]
             for k in range(n)}
    # Reduced chain groups: augment d_0 onto dimension -1.
    ranks = {-1: 0, 0: 1 if n else 0}
    for k in range(1,n):
        if not faces[k]:
            ranks[k] = 0
            continue
        ix = {s:i for i,s in enumerate(faces[k-1])}
        cols = []
        for face in faces[k]:
            col = 0
            for j in range(len(face)):
                sub = face[:j] + face[j+1:]
                col ^= 1 << ix[sub]
            cols.append(col)
        ranks[k] = mod2_rank(cols)
    ans = {}
    for k in range(n):
        b = len(faces[k]) - ranks[k] - ranks.get(k+1,0)
        if b: ans[k]=b
    return ans


def random_tree(rng, n):
    if n == 1:
        return 1,set(),{}
    m=rng.randrange(1,n)
    a=random_tree(rng,m)
    b=random_tree(rng,n-m)
    return construct(rng.choice(('join','union')),a,b)


def run():
    rng=Random(20261022)
    cases=0
    for n in range(1,11):
        for _ in range(24):
            q=random_tree(rng,n)
            measured=homology(q[0],q[1])
            if measured!=q[2]:
                raise AssertionError((n,q[1],q[2],measured))
            cases+=1
    # Deliberate mixed-dimensional example.
    triangle=construct('join', (1,set(),{}),construct('join',(1,set(),{}),(1,set(),{})))
    two_triangles=construct('union', triangle, triangle)
    mixed=construct('join',two_triangles,triangle)
    assert mixed[2]=={1:18,3:1}
    assert homology(mixed[0],mixed[1])==mixed[2]
    print(f'REPLAY_OK: {cases} cotrees with 1..10 vertices plus a 9-vertex mixed-dimensional example.')

if __name__ == '__main__':
    run()
