#!/usr/bin/env python3
"""Exact finite certificate for the strong Morse matching complex of a wheel.

Only the Python standard library is needed. The wheel is an unfilled graph:
its triangular circuits are *not* two-dimensional simplices of the input.
"""
import itertools
import collections
import json
from pathlib import Path

N = 6
RIM = 5
UNDIRECTED = tuple(sorted({tuple(sorted((0, i))) for i in range(1, 6)} |
                          {tuple(sorted((i, i % 5 + 1))) for i in range(1, 6)}))
ARCS = tuple(sorted({(u, v) for e in UNDIRECTED for u, v in (e, e[::-1])}))
ARC_ID = {a: i for i, a in enumerate(ARCS)}
ADJ = tuple(frozenset(w for e in UNDIRECTED if v in e for w in e if w != v)
            for v in range(N))


def from_increasing_order(order):
    """Vertex filtration: v is paired exactly if it has one earlier neighbor."""
    earlier = set()
    output = 0
    for vertex in order:
        neighbors = ADJ[vertex] & earlier
        if len(neighbors) == 1:
            target = next(iter(neighbors))
            output |= 1 << ARC_ID[(vertex, target)]
        earlier.add(vertex)
    return output


def independent_order_oracle(order):
    """Separate rank-based implementation, without maintaining a prefix set."""
    rank = {vertex: pos for pos, vertex in enumerate(order)}
    return sum(1 << ARC_ID[(v, next(u for u in ADJ[v] if rank[u] < rank[v]))]
               for v in range(N)
               if sum(rank[u] < rank[v] for u in ADJ[v]) == 1)


def subfaces(mask):
    sub = mask
    while sub:
        yield sub
        sub = (sub - 1) & mask


def face_data():
    masks = set()
    norders = 0
    for p in itertools.permutations(range(N)):
        a = from_increasing_order(p)
        b = independent_order_oracle(p)
        assert a == b, ('generation disagreement', p)
        masks.add(a)
        norders += 1
    assert norders == 720
    assert len(masks) == 81
    maximal = {m for m in masks if not any(m != n and m & n == m for n in masks)}
    assert len(maximal) == 45
    faces = set()
    for m in maximal:
        faces.update(subfaces(m))
    f = collections.Counter(m.bit_count()-1 for m in faces)
    assert dict(f) == {0:20, 1:55, 2:20}, dict(f)
    assert len(faces) == 95
    assert set(masks) - {0} <= faces
    return maximal, faces


def mask(ids):
    result = 0
    for j in ids:
        assert isinstance(j, int) and 0 <= j < len(ARCS)
        assert not (result >> j) & 1
        result |= 1 << j
    return result


def labels(m):
    return [j for j in range(len(ARCS)) if (m >> j) & 1]


def make_collapse_pairs(faces):
    remaining_t = set(f for f in faces if f.bit_count() == 3)
    remaining_e = set(f for f in faces if f.bit_count() == 2)
    certificates = []
    while remaining_t:
        counts = collections.Counter()
        for t in remaining_t:
            counts.update(t ^ (1 << b) for b in labels(t))
        choices = sorted((e, t) for t in remaining_t
                         for e in (t ^ (1 << b) for b in labels(t))
                         if counts[e] == 1 and e in remaining_e)
        assert choices, 'A non-collapsible triangle remains.'
        e, t = choices[0]
        certificates.append({'edge': labels(e), 'triangle': labels(t)})
        remaining_e.remove(e)
        remaining_t.remove(t)
    assert len(certificates) == 20
    assert len(remaining_e) == 35
    return certificates


def check_collapses(faces, witness):
    rem_t = set(f for f in faces if f.bit_count() == 3)
    rem_e = set(f for f in faces if f.bit_count() == 2)
    assert len(witness) == 20
    seen = set()
    for pair in witness:
        assert sorted(pair.keys()) == ['edge', 'triangle']
        edge, tri = mask(pair['edge']), mask(pair['triangle'])
        assert edge.bit_count() == 2 and tri.bit_count() == 3
        assert edge in rem_e and tri in rem_t
        assert edge & tri == edge
        assert sum(edge & q == edge for q in rem_t) == 1
        assert (edge, tri) not in seen
        seen.add((edge, tri))
        rem_e.remove(edge)
        rem_t.remove(tri)
    assert not rem_t
    assert len(rem_e) == 35
    vertices = set(m for m in faces if m.bit_count() == 1)
    assert len(vertices) == 20
    adj = {v: set() for v in vertices}
    for edge in rem_e:
        x, y = (1 << j for j in labels(edge))
        assert x in vertices and y in vertices
        adj[x].add(y)
        adj[y].add(x)
    reached, todo = {next(iter(vertices))}, list(vertices)[:1]
    while todo:
        v = todo.pop()
        for w in adj[v] - reached:
            reached.add(w)
            todo.append(w)
    assert len(reached) == len(vertices)
    rank = len(rem_e) - len(vertices) + 1
    assert rank == 16
    return rank


def signed_trace(faces, vmap):
    arc_perm = [ARC_ID[(vmap[u], vmap[v])] for u, v in ARCS]
    assert sorted(arc_perm) == list(range(len(ARCS)))
    out = [0, 0, 0]
    for simplex in faces:
        original = labels(simplex)
        mapped = [arc_perm[j] for j in original]
        transformed = sum(1 << a for a in mapped)
        assert transformed in faces, ('not invariant', simplex)
        if simplex == transformed:
            inversions = sum(mapped[i] > mapped[j]
                             for i in range(len(mapped))
                             for j in range(i+1, len(mapped)))
            out[len(original)-1] += 1 if inversions % 2 == 0 else -1
    return tuple(out)


def dihedral_table(faces):
    rows = []
    for reflected in (False, True):
        for shift in range(5):
            vmap = {0: 0}
            for i in range(5):
                vmap[i+1] = 1 + ((shift - i if reflected else shift + i) % 5)
            tr = signed_trace(faces, vmap)
            char_H1 = 1 - tr[0] + tr[1] - tr[2]
            expected = (2, -3, 0) if reflected else ((20, 55, 20) if shift == 0 else (0, 0, 0))
            assert tr == expected, (reflected, shift, tr)
            assert char_H1 == (-4 if reflected else (16 if shift == 0 else 1))
            epsilon = -1 if reflected else 1
            rho = 0 if reflected else (4 if shift == 0 else -1)
            assert char_H1 == 4 * epsilon + 3 * rho
            rows.append((('s' if reflected else 'r'), shift, tr, char_H1))
    assert len(rows) == 10
    # The character inner product with the trivial character vanishes.
    assert sum(row[3] for row in rows) == 0
    return rows


def run():
    assert len(UNDIRECTED) == 10 and len(ARCS) == 20
    facets, faces = face_data()
    witness_path = Path(__file__).with_name('collapse_pairs.json')
    witness = json.loads(witness_path.read_text(encoding='utf-8'))
    assert witness['vertices'] == [list(a) for a in ARCS]
    assert witness['pairs'] == make_collapse_pairs(faces)
    beta = check_collapses(faces, witness['pairs'])
    rows = dihedral_table(faces)
    assert collections.Counter(m.bit_count() for m in facets) == {2: 25, 3: 20}
    print('VERIFY_OK: orders=720 matchings=81 facets=45 face_vector=(20,55,20)')
    print('VERIFY_OK: collapses=20 spine=(20 vertices,35 edges) homotopy=vee_16_S1')
    print('VERIFY_OK: dihedral_actions=10 character=(16,1,-4) rational_module=4sign+3fourdim')


if __name__ == '__main__':
    run()
