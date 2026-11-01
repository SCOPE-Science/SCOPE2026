#!/usr/bin/env python3
"""Exact orbit-cell verification for two unordered points on complete graphs.

The program uses only the Python standard library.  Its finite checks complement
an explicit, uniform, continuous deformation defined in the accompanying proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
import json


def even(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 == 0


def cell_action(p, c):
    kind, data = c
    if kind == 0:
        return (0, tuple(sorted(p[x] for x in data)))
    if kind == 1:
        vertex, edge = data
        return (1, (p[vertex], tuple(sorted(p[x] for x in edge))))
    return (2, tuple(sorted(tuple(sorted(p[x] for x in e)) for e in data)))


def generate(n):
    E = list(combinations(range(n), 2))
    zero = [(0, pair) for pair in E]
    one = [(1, (vertex, e)) for vertex in range(n) for e in E if vertex not in e]
    two = [(2, tuple(sorted((e, f)))) for e, f in combinations(E, 2) if not set(e).intersection(f)]
    pairs = set()
    triangles = set()
    for _, (v, (a, b)) in one:
        e = (1, (v, (a, b)))
        pairs.add(((0, tuple(sorted((v, a)))), e))
        pairs.add(((0, tuple(sorted((v, b)))), e))
    for square in two:
        e, f = square[1]
        for a in e:
            for b in f:
                corner = (0, tuple(sorted((a, b))))
                for side in ((1, (a, f)), (1, (b, e))):
                    tri = (corner, side, square)
                    triangles.add(tri)
                    pairs.update([(corner, square), (side, square)])
    return [zero, one, two], list(pairs), list(triangles)


def calculate(n, alternating):
    cells, edges, triangles = generate(n)
    perms = [p for p in permutations(range(n)) if not alternating or even(p)]
    def orbit(face):
        return min(tuple(cell_action(p, c) for c in face) for p in perms)
    vertices = [(c,) for part in cells for c in part]
    faces = [vertices, edges, triangles]
    canonical = [{orbit(face) for face in part} for part in faces]
    id_maps = [{c: idx for idx, c in enumerate(sorted(part))} for part in canonical]
    def idx(face):
        k = len(face) - 1
        return id_maps[k][orbit(face)]
    endpoint = {}
    for rep, i in id_maps[1].items():
        endpoint[i] = (idx((rep[0],)), idx((rep[1],)))
        assert endpoint[i][0] != endpoint[i][1], 'inverted quotient edge'
    incidence = {}
    for rep, i in id_maps[2].items():
        incidence[i] = tuple(idx((rep[j], rep[k])) for j, k in ((0, 1), (0, 2), (1, 2)))
        assert len(set(incidence[i])) == 3
    # Every triangle has distinct vertex types, hence no inversions or folded faces.
    C = [len(part) for part in canonical]
    assert all(len(t) == 3 for t in incidence.values())
    assert all(len(endpoint[e]) == 2 for e in endpoint)
    # Boundary incidence signs with global 0/1/2 orderings.
    boundary = {(t, e): s for t, tri in incidence.items() for e, s in zip(tri, (1, -1, 1))}
    for t, tri in incidence.items():
        d1d2 = Counter()
        for e in tri:
            v0, v1 = endpoint[e]
            sign = boundary[(t, e)]
            d1d2[v0] -= sign
            d1d2[v1] += sign
        assert all(z == 0 for z in d1d2.values()), 'boundary squared is nonzero'
    # Rank over Q by explicit rational elimination, without a computer algebra package.
    def rank(matrix):
        if not matrix or not matrix[0]:
            return 0
        arr = [[Fraction(z) for z in row] for row in matrix]
        h, w = len(arr), len(arr[0])
        row = 0
        for col in range(w):
            pivot = next((i for i in range(row, h) if arr[i][col]), None)
            if pivot is None:
                continue
            arr[row], arr[pivot] = arr[pivot], arr[row]
            z = arr[row][col]
            arr[row] = [v / z for v in arr[row]]
            for i in range(row + 1, h):
                z = arr[i][col]
                if z:
                    arr[i] = [a - z * b for a, b in zip(arr[i], arr[row])]
            row += 1
            if row == h:
                break
        return row
    d1 = [[0] * C[1] for _ in range(C[0])]
    for e, (a, b) in endpoint.items():
        d1[a][e] = -1
        d1[b][e] = 1
    d2 = [[0] * C[2] for _ in range(C[1])]
    for (t, e), s in boundary.items():
        d2[e][t] = s
    r1, r2 = rank(d1), rank(d2)
    betti = (C[0] - r1, C[1] - r1 - r2, C[2] - r2)
    # Explicit free-face collapses of the orbit delta-complex.
    alive_edges = set(endpoint)
    alive_tris = set(incidence)
    collapses = []
    while alive_tris:
        multiplicity = Counter(e for t in alive_tris for e in incidence[t])
        options = sorted((t, e) for t in alive_tris for e in incidence[t] if multiplicity[e] == 1)
        if not options:
            break
        t, e = options[0]
        alive_tris.remove(t)
        alive_edges.remove(e)
        collapses.append(('triangle_edge', t, e))
    alive_vertices = set(range(C[0]))
    while True:
        valency = Counter(v for e in alive_edges for v in endpoint[e])
        options = sorted((v, e) for e in alive_edges for v in endpoint[e] if valency[v] == 1)
        if not options:
            break
        v, e = options[0]
        alive_edges.remove(e)
        alive_vertices.remove(v)
        collapses.append(('edge_vertex', e, v))
    residue = {'vertices': len(alive_vertices), 'edges': len(alive_edges), 'triangles': len(alive_tris)}
    assert not alive_tris
    result = {'n': n, 'group': 'A' if alternating else 'S', 'order': len(perms),
              'cell_counts': C, 'betti_over_Q': betti, 'euler': C[0]-C[1]+C[2],
              'edge_to_vertices': {str(k): list(v) for k, v in sorted(endpoint.items())},
              'triangle_to_edges': {str(k): list(v) for k, v in sorted(incidence.items())},
              'collapses': collapses, 'residual': residue}
    assert betti[0] == 1
    if (alternating and n in (3, 4)):
        assert betti == (1, 1, 0)
        assert residue['edges'] == residue['vertices'] and residue['triangles'] == 0
    else:
        assert betti == (1, 0, 0)
        assert residue == {'vertices': 1, 'edges': 0, 'triangles': 0}
    return result



def check_homotopy_equivariance():
    """Sample exact rational configurations; the general proof is symbolic."""
    def point(e, x):
        x = Fraction(x)
        if x == 0:
            return ('v', e[0])
        if x == 1:
            return ('v', e[1])
        assert 0 < x < 1
        return ('e', e, x)
    def action(p, q):
        if q[0] == 'v':
            return ('v', p[q[1]])
        a, b = q[1]
        x = q[2] if p[a] < p[b] else 1 - q[2]
        return point(tuple(sorted((p[a], p[b]))), x)
    def coord_from(q, v):
        assert q[0] == 'e' and v in q[1]
        return q[2] if q[1][0] == v else 1 - q[2]
    def from_coord(e, v, x):
        return point(e, x if e[0] == v else 1 - x)
    def h(pair, u):
        p, q = pair
        if p[0] == q[0] == 'v':
            return frozenset(pair)
        if p[0] == 'v' or q[0] == 'v':
            vertex = p if p[0] == 'v' else q
            moving = q if p[0] == 'v' else p
            v = vertex[1]
            if v not in moving[1]:
                return frozenset(pair)
            t = coord_from(moving, v)
            return frozenset((vertex, from_coord(moving[1], v, (1-u)*t+u)))
        if p[1] == q[1]:
            x, y = sorted([p[2], q[2]])
            return frozenset((point(p[1], (1-u)*x), point(p[1], (1-u)*y+u)))
        common = set(p[1]).intersection(q[1])
        if not common:
            return frozenset(pair)
        v = next(iter(common))
        x, y = coord_from(p, v), coord_from(q, v)
        factor = 1-u+u/max(x, y)
        return frozenset((from_coord(p[1], v, factor*x), from_coord(q[1], v, factor*y)))
    for n in (3, 4, 5):
        E = list(combinations(range(n), 2))
        pts = [('v', i) for i in range(n)] + [point(e, Fraction(j, 4)) for e in E for j in (1, 2, 3)]
        ps = list(permutations(range(n)))
        for pair in combinations(pts, 2):
            for u in (Fraction(0), Fraction(1, 2), Fraction(1)):
                image = h(pair, u)
                assert len(image) == 2, 'collision'
                if u == 0:
                    assert image == frozenset(pair)
                if u == 1:
                    carriers = [set((q[1],)) if q[0] == 'v' else set(q[1]) for q in image]
                    assert not carriers[0].intersection(carriers[1]), 'outside discrete complex'
                for perm in ps:
                    lhs = frozenset(action(perm, v) for v in image)
                    rhs = h(tuple(action(perm, v) for v in pair), u)
                    assert lhs == rhs, 'not equivariant'
    print('RATIONAL_SAMPLE_EQUIVARIANCE_OK')


def main():
    all_results = [calculate(n, alt) for n in range(2, 7) for alt in (False, True)]
    assert {tuple(r['cell_counts']) for r in all_results if r['n'] >= 4 and r['group'] == 'S'} == {(3, 3, 1)}
    assert [r['cell_counts'] for r in all_results if r['group'] == 'A' and r['n'] >= 4] == [
        [3, 5, 2], [3, 4, 2], [3, 3, 1]]
    assert [r['cell_counts'] for r in all_results if r['group'] == 'A' and r['n'] == 3] == [[2, 2, 0]]
    for result in all_results:
        print(result['group'], result['n'], 'f-vector', result['cell_counts'],
              'Betti', result['betti_over_Q'], 'residual', result['residual'])
    with open('orbit_certificate.json', 'w', encoding='utf8') as out:
        json.dump({'model': 'barycentrically triangulated Abrams two-point cubical complex',
                   'range_verified': [2, 6], 'results': all_results}, out, indent=2)
        out.write('\n')
    check_homotopy_equivariance()
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
