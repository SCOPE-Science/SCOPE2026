"""Exact integral chain reduction and symmetry character for a hexagonal prism.

Only Python's standard library is required. Run with Python 3.10 or later.
"""
from collections import Counter, defaultdict
from itertools import combinations

N = 6


def graph_and_faces():
    """Generate graph edges, all perfect matchings, and their down-closed faces."""
    edges = set()
    for layer in range(2):
        for i in range(N):
            edges.add(tuple(sorted((layer * N + i, layer * N + (i + 1) % N))))
    for i in range(N):
        edges.add((i, N + i))
    edges = sorted(edges)
    adjacent = [[] for _ in range(2 * N)]
    for j, (v, w) in enumerate(edges):
        adjacent[v].append((w, j))
        adjacent[w].append((v, j))

    def perfect_matchings(unmatched):
        if not unmatched:
            yield ()
            return
        v = min(unmatched)
        for w, index in adjacent[v]:
            if w in unmatched:
                for rest in perfect_matchings(unmatched - {v, w}):
                    yield tuple(sorted((index,) + rest))

    facets = sorted(set(perfect_matchings(frozenset(range(2 * N)))))
    faces = {()}
    for facet in facets:
        for k in range(1, N + 1):
            faces.update(combinations(facet, k))
    faces = sorted(faces, key=lambda f: (len(f), f))
    assert len(edges) == 18 and len(facets) == 20 and len(faces) == 822
    assert Counter(map(len, faces)) == {0: 1, 1: 18, 2: 117, 3: 276, 4: 270, 5: 120, 6: 20}
    return edges, facets, faces


def initial_boundary(faces):
    return {face: {face[:j] + face[j + 1:]: (-1) ** j
                   for j in range(len(face))} for face in faces}


def verify_chain(boundary):
    """Check all augmented chain identities, including the empty face."""
    for face, d in boundary.items():
        dd = defaultdict(int)
        for subface, a in d.items():
            for target, b in boundary[subface].items():
                dd[target] += a * b
        assert all(v == 0 for v in dd.values()), face


def unit_reduction(initial):
    """Integral cancellation of adjacent generators with unit incidence.

    For a pivot p = [d(c):r] = +1 or -1, replace every other d(x)
    meeting row r by d(x)-[d(x):r]/p*d(c), then discard r and c.
    This is an integral elementary chain-homotopy cancellation.
    """
    boundary = {c: dict(d) for c, d in initial.items()}
    row_columns = defaultdict(set)
    for c, d in boundary.items():
        for r in d:
            row_columns[r].add(c)
    pivots = 0
    while True:
        best = None
        for c, d in boundary.items():
            for r, value in d.items():
                if abs(value) != 1:
                    continue
                score = ((len(row_columns[r]) - 1) * (len(d) - 1),
                         len(d), len(row_columns[r]), len(c), c, r)
                if best is None or score < best[0]:
                    best = (score, r, c, value)
        if best is None:
            break
        _, r, c, pivot = best
        old = boundary[c].copy()
        for x in list(row_columns[r]):
            if x == c:
                continue
            factor = boundary[x][r] // pivot
            assert factor * pivot == boundary[x][r]
            for y, a in old.items():
                new = boundary[x].get(y, 0) - factor * a
                if new:
                    boundary[x][y] = new
                    row_columns[y].add(x)
                else:
                    boundary[x].pop(y, None)
                    row_columns[y].discard(x)
            assert r not in boundary[x]
        for y in boundary[r]:
            row_columns[y].discard(r)
        for y in boundary[c]:
            row_columns[y].discard(c)
        for x in list(row_columns[c]):
            boundary[x].pop(c, None)
        row_columns.pop(c, None)
        row_columns.pop(r, None)
        del boundary[r]
        del boundary[c]
        pivots += 1
        if pivots % 25 == 0:
            verify_chain(boundary)
            assert all(row_columns[y] == {x for x, d in boundary.items() if y in d}
                       for y in row_columns)
    verify_chain(boundary)
    assert pivots == 408
    assert len(boundary) == 6
    assert all(len(c) == 3 and not d for c, d in boundary.items())
    return pivots


def parity(sequence):
    return -1 if sum(sequence[i] > sequence[j]
                     for i in range(len(sequence))
                     for j in range(i + 1, len(sequence))) % 2 else 1


def action_on_edges(edges, rotation, reflection, layer_swap):
    edge_number = {e: i for i, e in enumerate(edges)}

    def vertex(v):
        layer, column = divmod(v, N)
        column = ((-column if reflection else column) + rotation) % N
        return ((layer + layer_swap) % 2) * N + column

    result = [edge_number[tuple(sorted((vertex(v), vertex(w))))]
              for v, w in edges]
    assert len(set(result)) == len(edges)
    return result


def reduced_lefschetz(faces, edge_permutation):
    """Signed simplicial trace minus the augmented degree-minus-one trace."""
    total = -1
    for face in faces:
        if not face:
            continue
        image = [edge_permutation[e] for e in face]
        if set(image) == set(face):
            total += ((-1) ** (len(face) - 1)) * parity(image)
    return total


def predicted_character(a, b, c):
    two_dimensional_frequency_one = (2, 1, -1, -2, -1, 1)
    two_dimensional_frequency_two = (2, -1, -1, 2, -1, -1)
    if b:
        return -1 + (-1) ** a
    return (1 + (-1) ** a + two_dimensional_frequency_one[a]
            + (-1) ** c * two_dimensional_frequency_two[a])


def main():
    edges, facets, faces = graph_and_faces()
    boundary = initial_boundary(faces)
    verify_chain(boundary)
    pivots = unit_reduction(boundary)
    print('edges', len(edges), 'perfect_matchings', len(facets),
          'faces_including_empty', len(faces), 'unit_pivots', pivots)
    table = {}
    for b in range(2):
        for c in range(2):
            traces = []
            for a in range(N):
                permutation = action_on_edges(edges, a, b, c)
                trace = reduced_lefschetz(faces, permutation)
                assert trace == predicted_character(a, b, c), (a, b, c, trace)
                traces.append(trace)
            table[(b, c)] = tuple(traces)
    assert table == {
        (0, 0): (6, 0, 0, 0, 0, 0),
        (0, 1): (2, 2, 2, -4, 2, 2),
        (1, 0): (0, -2, 0, -2, 0, -2),
        (1, 1): (0, -2, 0, -2, 0, -2),
    }
    for (b, c), values in sorted(table.items()):
        print('reflection', b, 'layer_swap', c, 'rotation_a_0_to_5', values)
    print('PASS: integral reduction and all 24 action-character values')


if __name__ == '__main__':
    main()
