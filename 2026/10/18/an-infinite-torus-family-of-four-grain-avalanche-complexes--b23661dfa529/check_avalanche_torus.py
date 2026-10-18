"""Finite reproducibility checks for cyclic four-chip avalanche complexes.

The mathematical proof for all admissible parameters is geometric; these finite
checks independently rebuild the dynamics, verify each elementary collapse,
and test the resulting surface triangulations.
"""
from collections import defaultdict, deque
from itertools import combinations


def close_facets(facets):
    faces = set()
    for face in facets:
        vertices = tuple(sorted(face))
        for k in range(1, len(vertices) + 1):
            faces.update(frozenset(v) for v in combinations(vertices, k))
    return faces


def avalanche_facets(n, d):
    state = [int(i in (0, 1, d, d + 1)) for i in range(n)]
    seen = []
    for t in range(n):
        active = frozenset(i for i, val in enumerate(state) if val >= 1)
        assert len(active) == 4
        seen.append(active)
        # For the oriented cycle i -> i+1, synchronous firing shifts bits.
        next_state = [state[(i - 1) % n] for i in range(n)]
        state = next_state
    assert state == [int(i in (0, 1, d, d + 1)) for i in range(n)]
    assert len(set(seen)) == n
    return set(seen)


def perform_collapse(faces, low, high):
    assert low in faces and high in faces
    assert len(high) == len(low) + 1 and low < high
    # Codimension one free face of the unique maximal coface.
    containing = [x for x in faces if len(x) > len(low) and low <= x]
    assert containing == [high], (low, containing)
    faces.remove(low)
    faces.remove(high)


def test(n, d):
    assert d >= 3 and n >= 2 * d + 5
    fs = avalanche_facets(n, d)
    faces = close_facets(fs)
    assert [sum(len(x) == k for x in faces) for k in range(1, 5)] == [n, 4*n, 4*n, n]
    for i in range(n):
        tet = frozenset((i, i+1, i+d, i+d+1)[j] % n for j in range(4))
        forbidden_triangle = frozenset({i%n, (i+1)%n, (i+d+1)%n})
        perform_collapse(faces, forbidden_triangle, tet)
    for i in range(n):
        forbidden_edge = frozenset({i%n, (i+d+1)%n})
        removable_triangle = frozenset({i%n, (i+d)%n, (i+d+1)%n})
        perform_collapse(faces, forbidden_edge, removable_triangle)
    predicted_triangles=set()
    for i in range(n):
        predicted_triangles.add(frozenset({i%n,(i+1)%n,(i+d)%n}))
        predicted_triangles.add(frozenset({(i+1)%n,(i+d)%n,(i+d+1)%n}))
    assert faces == close_facets(predicted_triangles)
    assert [sum(len(x) == k for x in faces) for k in range(1, 5)] == [n,3*n,2*n,0]
    assert len(predicted_triangles)==2*n
    edges = [x for x in faces if len(x)==2]
    tris = [x for x in faces if len(x)==3]
    incidence=defaultdict(list)
    for t in tris:
        for e in combinations(t,2):incidence[frozenset(e)].append(t)
    assert all(len(incidence[e])==2 for e in edges)
    # Each vertex link must be a single six-cycle.
    for v in range(n):
        le=[frozenset(t-{v}) for t in tris if v in t]
        link_vertices=set().union(*le)
        assert len(link_vertices)==6 and len(le)==6
        neighbor=defaultdict(set)
        for e in le:
            a,b=tuple(e);neighbor[a].add(b);neighbor[b].add(a)
        assert all(len(neighbor[a])==2 for a in link_vertices)
        reached={next(iter(link_vertices))};todo=list(reached)
        while todo:
            for a in neighbor[todo.pop()]:
                if a not in reached: reached.add(a);todo.append(a)
        assert len(reached)==6
    # Test orientability without relying on lattice quotient.
    def induced_edge_sign(triangle,edge):
        v=sorted(triangle)
        target=sorted(edge)
        for j in range(3):
            s=[v[z] for z in range(3) if z!=j]
            if set(s)==set(target):
                return (-1 if j%2 else 1)
        raise AssertionError
    tri_index={t:i for i,t in enumerate(tris)}
    orientation={0:1};todo=deque([tris[0]])
    while todo:
        t=todo.popleft();ori=orientation[tri_index[t]]
        for e in combinations(t,2):
            edge=frozenset(e)
            other=next(u for u in incidence[edge] if u!=t)
            wanted=-ori*induced_edge_sign(t,edge)*induced_edge_sign(other,edge)
            oi=tri_index[other]
            if oi not in orientation:
                orientation[oi]=wanted;todo.append(other)
            else: assert orientation[oi]==wanted
    assert len(orientation)==2*n
    assert n-3*n+2*n==0
    return True


def main():
    cases=0
    for d in range(3,13):
        for n in range(2*d+5, min(2*d+24,61)):
            assert test(n,d);cases+=1
    print('OK: %d (n,d) pairs; all 2n prescribed collapses, torus links, and orientation checked.'%cases)

if __name__=='__main__':
    main()
