"""Exact standalone verification of a cube strong-Morse-matching homotopy calculation.

Run with Python 3.10 or later; uses only the standard library.
The certificate checks a complete vertex-order census, free-face collapses,
a spanning-tree/triangle certificate for simple connectivity, and mod-two ranks.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations


def bit_indices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def submasks(mask):
    value = mask
    while value:
        yield value
        value = (value - 1) & mask


def gf2_rank(columns):
    pivots = {}
    for value in columns:
        while value:
            key = value.bit_length() - 1
            if key not in pivots:
                pivots[key] = value
                break
            value ^= pivots[key]
    return len(pivots)


def verify():
    # Vertices of the original graph are the three-bit strings 0,...,7.
    # Vertices of the matching complex are oriented incidences (v, vw).
    incidences = [(v, u) for v in range(8) for u in range(8)
                  if (v ^ u).bit_count() == 1]
    assert len(incidences) == 24
    number = {pair: i for i, pair in enumerate(incidences)}
    gradients = set()
    for ordering in permutations(range(8)):
        visited = set()
        gradient = 0
        for v in ordering:
            predecessors = [u for u in visited if (u ^ v).bit_count() == 1]
            if len(predecessors) == 1:
                gradient |= 1 << number[v, predecessors[0]]
            visited.add(v)
        if gradient:
            gradients.add(gradient)
    assert len(gradients) == 584
    maximal = sorted(f for f in gradients if not any(
        f != g and f & g == f for g in gradients))
    assert len(maximal) == 216
    assert all(f.bit_count() == 4 for f in maximal)
    faces = {0}
    for f in maximal:
        faces.update(submasks(f))
    levels = {k: sorted(f for f in faces if f.bit_count() == k + 1)
              for k in range(4)}
    assert tuple(map(len, levels.values())) == (24, 168, 392, 216)
    assert len(faces) == 801

    # Exact sequence of simplicial elementary collapses of all tetrahedra.
    cofaces = defaultdict(set)
    for tetra in maximal:
        for v in bit_indices(tetra):
            cofaces[tetra ^ (1 << v)].add(tetra)
    live = set(maximal)
    discarded_triangles = set()
    collapse_pairs = []
    while live:
        choices = [(tri, next(iter(s))) for tri, s in cofaces.items()
                   if len(s) == 1]
        assert choices, 'No free triangle remains before all tetrahedra are removed'
        tri, tetra = min(choices)
        assert tri not in discarded_triangles and tetra in live
        discarded_triangles.add(tri)
        live.remove(tetra)
        collapse_pairs.append((tri, tetra))
        for v in bit_indices(tetra):
            cofaces[tetra ^ (1 << v)].remove(tetra)
    assert len(collapse_pairs) == 216
    triangles = sorted(set(levels[2]) - discarded_triangles)
    assert len(triangles) == 176

    # Kill pi_1 explicitly: contract a spanning tree, then use only triangle
    # relations containing two already trivialized edge generators.
    edges = set(levels[1])
    adjacency = defaultdict(list)
    for edge in edges:
        a, b = tuple(bit_indices(edge))
        adjacency[a].append((b, edge))
        adjacency[b].append((a, edge))
    discovered = {0}
    tree = []
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for w, edge in sorted(adjacency[v]):
            if w not in discovered:
                discovered.add(w)
                tree.append(edge)
                queue.append(w)
    assert len(discovered) == 24 and len(tree) == 23
    known = set(tree)
    triangle_relations = []
    while True:
        progress = False
        for triangle in triangles:
            boundary = [triangle ^ (1 << v) for v in bit_indices(triangle)]
            unknown = [edge for edge in boundary if edge not in known]
            if len(unknown) == 1:
                known.add(unknown[0])
                triangle_relations.append((triangle, unknown[0]))
                progress = True
        if not progress:
            break
    assert known == edges, 'Some fundamental-group generators survive'
    assert len(triangle_relations) == 145

    # Independent chain calculation over F_2 verifies homology ranks.
    ranks = {}
    for degree in (1, 2, 3):
        row_number = {f: i for i, f in enumerate(levels[degree - 1])}
        columns = []
        for f in levels[degree]:
            boundary = 0
            for v in bit_indices(f):
                boundary ^= 1 << row_number[f ^ (1 << v)]
            columns.append(boundary)
        ranks[degree] = gf2_rank(columns)
    assert ranks == {1: 23, 2: 145, 3: 216}
    assert 24 - 168 + 392 - 216 == 32
    assert 24 - 168 + 176 == 32
    print('PASS: 40320 vertex orders; 584 distinct gradients; 216 tetrahedral facets')
    print('PASS: full f-vector (24, 168, 392, 216); 801 faces including empty')
    print('PASS: 216 legal elementary collapses; residual 176 triangles')
    print('PASS: 23 tree edges and 145 triangle relations kill all 168 edges')
    print('PASS: mod-2 boundary ranks (23, 145, 216); Euler characteristic 32')
    print('Consequent integral homotopy type: wedge of 31 copies of S^2')
    return collapse_pairs, tree, triangle_relations


if __name__ == '__main__':
    verify()
