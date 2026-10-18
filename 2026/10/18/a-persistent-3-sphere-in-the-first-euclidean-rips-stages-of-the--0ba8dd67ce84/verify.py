#!/usr/bin/env python3
"""Exact finite checker of a relative elementary-collapse certificate for F4 roots.
Run next to collapse_pairs.txt with Python 3.10 or later; no external packages.
"""
from itertools import combinations, product
from pathlib import Path
from collections import Counter


def roots_scaled_by_two():
    a = []
    for i in range(4):
        for sign in (-1, 1):
            v = [0] * 4
            v[i] = 2 * sign
            a.append(tuple(v))
    a.extend(product((-1, 1), repeat=4))
    for i, j in combinations(range(4), 2):
        for si, sj in product((-1, 1), repeat=2):
            v = [0] * 4
            v[i], v[j] = 2 * si, 2 * sj
            a.append(tuple(v))
    assert len(a) == len(set(a)) == 48
    return a


def graph_adjacency(roots, max_squared_scaled):
    a = [0] * 48
    for i, j in combinations(range(48), 2):
        d = sum((x - y) ** 2 for x, y in zip(roots[i], roots[j]))
        if d <= max_squared_scaled:
            a[i] |= 1 << j
            a[j] |= 1 << i
    return a


def all_nonempty_cliques(adj):
    faces = set()
    stack = [(0, (1 << 48) - 1)]
    while stack:
        face, candidates = stack.pop()
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            u = bit.bit_length() - 1
            new_face = face | bit
            assert new_face not in faces
            faces.add(new_face)
            smaller = candidates & adj[u]
            if smaller:
                stack.append((new_face, smaller))
    return faces


def check():
    vertices = roots_scaled_by_two()
    squared = Counter(sum((x-y)**2 for x,y in zip(a,b)) for a,b in combinations(vertices,2))
    assert dict(sorted(squared.items())) == {4:240, 8:168, 12:384, 16:84, 20:144, 24:96, 32:12}
    small = all_nonempty_cliques(graph_adjacency(vertices, 4))
    big = all_nonempty_cliques(graph_adjacency(vertices, 8))
    fv = lambda ff: tuple(Counter(m.bit_count() for m in ff)[j] for j in range(1,8))
    assert fv(small) == (48,240,384,192,0,0,0)
    assert fv(big) == (48,408,1224,1560,840,168,24)
    assert small <= big
    assert len(big - small) == 3408
    # The 24 short roots form a 24-cell; 24 long roots index its facets.
    short = set(range(24)); long = set(range(24,48))
    sfaces = {f for f in small if f >> 24 == 0}
    assert tuple(Counter(f.bit_count() for f in sfaces)[k] for k in (1,2,3,4)) == (24,96,96,0)
    adjsmall = graph_adjacency(vertices,4)
    triangles = {f for f in sfaces if f.bit_count()==3}
    triangle_membership = Counter()
    for i in long:
        neighbors = {j for j in short if (adjsmall[i]>>j)&1}
        supported = {j for j in short if sum(x*y for x,y in zip(vertices[i],vertices[j]))==4}
        assert neighbors == supported and len(neighbors)==6
        induced = [t for t in triangles if (t & ~sum(1<<j for j in neighbors))==0]
        assert len(induced)==8
        induced_edges = [u for u in sfaces if u.bit_count()==2 and all(((u>>j)&1)==0 for j in short-neighbors)]
        assert len(induced_edges)==12
        for t in induced:
            triangle_membership[t]+=1
    assert set(triangle_membership)==triangles and set(triangle_membership.values())=={2}
    # For each remaining free face u the unique immediate coface is v.
    immediate = {f: set() for f in big}
    for face in big:
        if face.bit_count()>=2:
            b=face
            while b:
                bit=b & -b;b^=bit
                immediate[face ^ bit].add(face)
    current=set(big)
    lines=(Path(__file__).with_name('collapse_pairs.txt')).read_text(encoding='ascii').splitlines()
    assert len(lines)==1704
    sizes = Counter()
    for line in lines:
        terms=line.split()
        assert len(terms)==2
        u,v=(int(t,16) for t in terms)
        assert u not in small and v not in small
        assert u in current and v in current
        assert v.bit_count()==u.bit_count()+1 and (u&v)==u
        assert {w for w in immediate[u] if w in current} == {v}
        sizes[u.bit_count()]+=1
        current.remove(u);current.remove(v)
    assert current == small
    assert sum(sizes.values()) == 1704
    print('VERIFY_OK', 'f_1',fv(small),'f_sqrt2',fv(big),
          'pairs',sum(sizes.values()), 'protected',len(current),
          'pair_dimensions',dict(sorted(sizes.items())))

if __name__=='__main__':check()
