#!/usr/bin/env python3
"""Exact finite simplicial-collapse certificate for conjugation-fixed partition-graph complexes.

Usage: python3 verify.py certificate.json
Pure Python standard library. No sampling, dependencies, or network access.
"""
import json
import sys
from itertools import combinations


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for k in range(min(n, maximum), 0, -1):
        for remainder in partitions(n-k, k):
            yield (k,) + remainder


def conjugate(a):
    return tuple(sum(x >= j for x in a) for j in range(1, a[0] + 1)) if a else ()


def row_neighbors(a):
    out = set()
    for i in range(len(a)):
        shrunk = list(a)
        shrunk[i] -= 1
        for j in range(len(a) + 1):
            if i == j:
                continue
            b = list(shrunk)
            if j == len(a):
                b.append(1)
            else:
                b[j] += 1
            b = tuple(sorted((v for v in b if v > 0), reverse=True))
            if b != a:
                out.add(b)
    return out


def conjugate_coordinate_neighbor(a, b):
    x, y = conjugate(a), conjugate(b)
    l = max(len(x), len(y))
    differences = [((y[j] if j < len(y) else 0)-
                    (x[j] if j < len(x) else 0)) for j in range(l)]
    return sorted(d for d in differences if d) == [-1, 1]


def addable_corners(a):
    corners = []
    for i in range(len(a)):
        if i == 0 or a[i-1] > a[i]:
            corners.append((i+1, a[i]+1))
    corners.append((len(a)+1, 1))
    return corners


def add_at(a, i, j):
    b = list(a)
    if i == len(a) + 1:
        assert j == 1
        b.append(1)
    else:
        assert j == b[i-1] + 1
        b[i-1] += 1
    assert all(b[k] >= b[k+1] for k in range(len(b)-1))
    return tuple(b)


def centre_pairs(n):
    result = set()
    for centre in partitions(n-1):
        if centre != conjugate(centre):
            continue
        corners = set(addable_corners(centre))
        for i, j in corners:
            if i != j and (j, i) in corners:
                a, b = add_at(centre, i, j), add_at(centre, j, i)
                result.add(tuple(sorted((a, b))))
    return result


def orbit_graph(n):
    vertices = list(partitions(n))
    neighbors = {v: row_neighbors(v) for v in vertices}
    c = {v: conjugate(v) for v in vertices}
    vertexset = set(vertices)
    assert set(c.values()) == vertexset
    for v in vertices:
        assert v not in neighbors[v]
        for w in neighbors[v]:
            assert w in vertexset
            assert v in neighbors[w]
            assert c[w] in neighbors[c[v]]
            assert conjugate_coordinate_neighbor(v, w)
    singles = {(v,) for v in vertices if c[v] == v}
    doubles = {(v, c[v]) for v in vertices if v < c[v] and c[v] in neighbors[v]}
    assert doubles == centre_pairs(n), (n, doubles ^ centre_pairs(n))
    orbits = sorted(singles | doubles)
    edges = []
    for i in range(len(orbits)):
        for j in range(i+1, len(orbits)):
            if all(y in neighbors[x] for x in orbits[i] for y in orbits[j]):
                edges.append((i, j))
    return orbits, edges


def all_faces(num_vertices, edges):
    neighbors = [set() for _ in range(num_vertices)]
    for i,j in edges:
        neighbors[i].add(j)
        neighbors[j].add(i)
    levels = [[(i,) for i in range(num_vertices)]]
    while levels[-1]:
        higher = []
        for face in levels[-1]:
            for next_vertex in sorted(neighbors[face[-1]]):
                if next_vertex > face[-1] and all(next_vertex in neighbors[i] for i in face[:-1]):
                    higher.append(face + (next_vertex,))
        if not higher:
            break
        levels.append(higher)
    return levels


def connected_components(vertices, edges):
    adjacency = {v: set() for v in vertices}
    for i,j in edges:
        adjacency[i].add(j)
        adjacency[j].add(i)
    comps = []
    unseen = set(vertices)
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        component = {root}
        active = [root]
        while active:
            x = active.pop()
            for y in adjacency[x] & unseen:
                unseen.remove(y)
                component.add(y)
                active.append(y)
        components_edges = [(i,j) for i,j in edges if i in component and j in component]
        comps.append((len(component), len(components_edges)-len(component)+1))
    return sorted(comps)


def is_free_pair(faces, small, large):
    if small not in faces or large not in faces or len(large) != len(small)+1:
        return False
    if not set(small).issubset(large):
        return False
    larger_cofaces = [s for s in faces if len(s) > len(small) and set(small).issubset(s)]
    return larger_cofaces == [large]


def compute_collapses(face_levels):
    faces = set(sum(face_levels, []))
    pairs = []
    while any(len(f) >= 3 for f in faces):
        success = False
        for large in sorted((f for f in faces if len(f)>=3), key=lambda f:(-len(f), f)):
            for small in combinations(large, len(large)-1):
                if is_free_pair(faces, small, large):
                    pairs.append([list(small),list(large)])
                    faces.remove(small);faces.remove(large)
                    success=True
                    break
            if success: break
        if not success:
            raise AssertionError('No available collapse removing a high-dimensional simplex')
    high_pairs = len(pairs)
    while True:
        edges = sorted(f for f in faces if len(f)==2)
        counts = {v[0]:0 for v in faces if len(v)==1}
        for a,b in edges:
            counts[a]+=1;counts[b]+=1
        leaves = sorted(v for v,degree in counts.items() if degree==1)
        if not leaves: break
        leaf=leaves[0]
        edge=next(e for e in edges if leaf in e)
        assert is_free_pair(faces,(leaf,),edge)
        pairs.append([[leaf],list(edge)])
        faces.remove((leaf,));faces.remove(edge)
    return pairs,high_pairs,faces


def rank_mod_two(columns):
    pivots={}
    for column in columns:
        while column:
            idx=column.bit_length()-1
            if idx in pivots:
                column ^= pivots[idx]
            else:
                pivots[idx]=column
                break
    return len(pivots)


def bettis(face_levels):
    ranks = [0]
    for k in range(1,len(face_levels)):
        index = {face:i for i,face in enumerate(face_levels[k-1])}
        boundaries=[]
        for f in face_levels[k]:
            value=0
            for j in range(len(f)):
                value ^= (1 << index[f[:j]+f[j+1:]])
            boundaries.append(value)
        ranks.append(rank_mod_two(boundaries))
    return [len(face_levels[k])-ranks[k]-(ranks[k+1] if k+1<len(ranks) else 0)
            for k in range(len(face_levels))]


def build_row(n):
    orbits, edges = orbit_graph(n)
    levels=all_faces(len(orbits),edges)
    pairs,high_pairs,remaining=compute_collapses(levels)
    dims=[len(k) for k in levels]
    original_betti=bettis(levels)
    before_comps=connected_components(range(len(orbits)),edges)
    after_edges=sorted(k for k in remaining if len(k)==2)
    after_vertices=sorted(v[0] for v in remaining if len(v)==1)
    after_comps=connected_components(after_vertices,after_edges)
    assert len(after_comps)==len(before_comps)
    assert original_betti[0]==len(after_comps)
    assert (original_betti[1] if len(original_betti)>1 else 0) == sum(b for _,b in after_comps)
    assert all(v==0 for v in original_betti[2:])
    return dict(n=n, orbits=[[list(v) for v in orbit] for orbit in orbits],
                face_counts=dims, collapses=pairs, high_collapse_count=high_pairs,
                remaining_vertices=after_vertices,
                remaining_edges=[list(e) for e in after_edges],
                components=[list(x) for x in after_comps],
                mod2_betti=original_betti)


def verify_row(row):
    n=row['n']
    orbits,edges=orbit_graph(n)
    assert row['orbits']==[[list(v) for v in orbit] for orbit in orbits]
    levels=all_faces(len(orbits),edges)
    assert row['face_counts']==[len(k) for k in levels]
    original_betti=bettis(levels)
    assert row['mod2_betti']==original_betti
    allcells=set(sum(levels,[]))
    for i, (little,big) in enumerate(row['collapses']):
        a,b=tuple(little),tuple(big)
        assert is_free_pair(allcells,a,b), ('bad collapse',n,i,a,b)
        if i<row['high_collapse_count']:
            assert len(b)>=3
        else:
            assert len(b)==2
        allcells.remove(a);allcells.remove(b)
    assert all(len(f)<=2 for f in allcells)
    remaining_vertices=sorted(v[0] for v in allcells if len(v)==1)
    remaining_edges=sorted(v for v in allcells if len(v)==2)
    assert remaining_vertices==row['remaining_vertices']
    assert [list(v) for v in remaining_edges]==row['remaining_edges']
    components=connected_components(remaining_vertices,remaining_edges)
    assert [list(x) for x in components]==row['components']
    assert len(components)==original_betti[0]
    assert sum(b for _,b in components)==(original_betti[1] if len(original_betti)>1 else 0)
    assert all(b==0 for b in original_betti[2:])
    return (n, row['face_counts'], components)


def main():
    with open(sys.argv[1],encoding='utf-8') as f:
        certificate=json.load(f)
    assert [r['n'] for r in certificate['cases']]==list(range(1,23))
    results=[verify_row(r) for r in certificate['cases']]
    h1={n:sum(b for _,b in comps) for n,_,comps in results}
    assert all(h1[n]==0 for n in range(1,18))
    assert h1[18]==1 and h1[20]==1 and h1[22]==2
    assert results[17][2]==[(1,0),(8,1)]
    assert results[21][2]==[(1,0),(15,2)]
    print('ALL_CERTIFICATES_VALID')
    for n,counts,components in results:
        print('%2d: faces=%-16s graph_core_components=%s' %(n,counts,components))
    print('FIRST_FIXED_H1_NONZERO=18; H1_RANK_AT_18=1; H1_RANK_AT_22=2')

if __name__=='__main__':
    main()
