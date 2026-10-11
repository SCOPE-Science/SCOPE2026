#!/usr/bin/env python3
"""Standalone exact verification of a graph-metric Rips collapse certificate.

Python 3 standard library only. All graph distances and simplices are
reconstructed independently of the certificate data.
"""
import collections
import itertools
import json
from pathlib import Path


def assert_connected(nodes, edges):
    if not nodes:
        return False
    adjacency = {v: set() for v in nodes}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    visited = {next(iter(nodes))}
    work = list(visited)
    while work:
        u = work.pop()
        for v in adjacency[u] - visited:
            visited.add(v)
            work.append(v)
    return visited == set(nodes)


def main():
    vertices = [(axis, *signs)
                for axis in range(3)
                for signs in itertools.product((-1, 1), repeat=3)]
    assert len(vertices) == 24
    edges = set()
    for i, j in itertools.combinations(range(24), 2):
        axis, *signs = vertices[i]
        other_axis, *other_signs = vertices[j]
        same_axis_edge = (axis == other_axis and
                          signs[axis] == other_signs[axis] and
                          sum(signs[k] != other_signs[k]
                              for k in range(3)) == 1)
        different_axis_edge = axis != other_axis and signs == other_signs
        if same_axis_edge or different_axis_edge:
            edges.add((i, j))
    assert len(edges) == 48
    adjacent = {i: set() for i in range(24)}
    for i, j in edges:
        adjacent[i].add(j)
        adjacent[j].add(i)
    assert {len(adjacent[i]) for i in range(24)} == {4}
    assert assert_connected(set(range(24)), edges)
    distances = {}
    for start in range(24):
        distance = {start: 0}
        queue = collections.deque([start])
        while queue:
            u = queue.popleft()
            for v in adjacent[u]:
                if v not in distance:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        assert len(distance) == 24
        distances[start] = distance
    assert max(max(d.values()) for d in distances.values()) == 5
    triangles = {
        triple for triple in itertools.combinations(range(24), 3)
        if all(pair in edges for pair in itertools.combinations(triple, 2))
    }
    assert len(triangles) == 8
    assert len(set().union(*map(set, triangles))) == 24
    squares = []
    for quad in itertools.combinations(range(24), 4):
        internal = [e for e in itertools.combinations(quad, 2) if e in edges]
        if len(internal) == 4 and all(sum(v in e for e in internal) == 2 for v in quad):
            squares.append(quad)
    assert len(squares) == 18
    target_triangles = set(triangles)
    for square in squares:
        nonedges = [pair for pair in itertools.combinations(square, 2)
                    if pair not in edges]
        assert len(nonedges) == 2
        a, b = min(nonedges)
        for v in square:
            if v not in (a, b):
                target_triangles.add(tuple(sorted((a, b, v))))
    assert len(target_triangles) == 44
    target = {(i,) for i in range(24)} | target_triangles
    for t in target_triangles:
        target.update(itertools.combinations(t, 2))
    assert collections.Counter(map(len, target)) == {1: 24, 2: 66, 3: 44}
    target_edges = {f for f in target if len(f) == 2}
    assert assert_connected(set(range(24)), target_edges)
    edge_incidence = collections.Counter(e for tri in target_triangles
                                          for e in itertools.combinations(tri, 2))
    assert set(edge_incidence) == target_edges
    assert set(edge_incidence.values()) == {2}
    for v in range(24):
        link_edges = {tuple(x for x in t if x != v)
                      for t in target_triangles if v in t}
        link_nodes = {x for e in link_edges for x in e}
        assert link_nodes
        assert assert_connected(link_nodes, link_edges)
        degrees = collections.Counter(x for e in link_edges for x in e)
        assert set(degrees.values()) == {2}
    assert 24 - 66 + 44 == 2

    # Enumerate every simplex of the graph square, not merely maximal ones.
    near = {i: {j for j in range(24) if j != i and distances[i][j] <= 2}
            for i in range(24)}
    faces = set()
    def visit(prefix, choices):
        for pos, v in enumerate(choices):
            face = prefix + (v,)
            faces.add(face)
            visit(face, [w for w in choices[pos+1:] if w in near[v]])
    visit((), list(range(24)))
    assert collections.Counter(map(len, faces)) == {
        1: 24, 2: 132, 3: 248, 4: 186, 5: 48}
    assert len(faces) == 638 and target <= faces

    certificate = json.loads((Path(__file__).parent /
                              'collapse_certificate.json').read_text(encoding='utf-8'))
    assert certificate['schema_version'] == 1
    pairs = certificate['collapse_pairs']
    assert len(pairs) == 252
    for step_index, pair in enumerate(pairs):
        lower, upper = map(tuple, pair)
        assert lower == tuple(sorted(set(lower)))
        assert upper == tuple(sorted(set(upper)))
        assert len(upper) == len(lower) + 1
        assert set(lower) < set(upper)
        assert lower in faces and upper in faces, step_index
        assert lower not in target and upper not in target
        # A free codimension-one face belongs to precisely one simplex of
        # the next dimension; in an abstract simplicial complex this ensures
        # that it has no other coface in any dimension.
        next_cofaces = [f for f in faces
                        if len(f) == len(lower)+1 and set(lower) < set(f)]
        assert next_cofaces == [upper], (step_index, lower, next_cofaces)
        faces.remove(lower)
        faces.remove(upper)
    assert faces == target

    # Scale one: each of the eight vertex-disjoint triangles has a unique
    # edge not in any other triangle, so eight free-face collapses leave a
    # connected graph with 24 vertices and 40 edges, hence cycle rank 17.
    assert len(triangles) == 8 and len(edges) == 48
    assert 48 - 8 - 24 + 1 == 17
    print('VERIFY_OK: 24 vertices, 48 original edges, 18 squares, 8 triangles;'
          ' scale-two face vector (24,132,248,186,48);'
          ' 252 elementary collapses; 24-vertex 2-sphere triangulation;'
          ' scale-one cycle rank 17')

if __name__ == '__main__':
    main()
