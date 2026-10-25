#!/usr/bin/env python3
"""Exact integral discrete-Morse certificate for the Hesse cap complex.

The 9 points are elements of F_3^2 in row-major order. Faces are subsets
containing no collinear triple. The program uses only the Python stdlib.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

VERTICES = tuple(range(9))
COORD = {i: (i // 3, i % 3) for i in VERTICES}
ORDER = (5, 7, 1, 3, 4, 2, 8, 6, 0)


def vertices(mask):
    return tuple(i for i in VERTICES if mask & (1 << i))


def boundary(mask):
    return tuple((mask ^ (1 << i), (-1) ** j)
                 for j, i in enumerate(vertices(mask)))


def rank_mod2(columns):
    basis = {}
    for col in columns:
        while col:
            pivot = col.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = col
                break
            col ^= basis[pivot]
    return len(basis)


def verify():
    # Every unordered pair has a unique third point on its affine line.
    line_masks = set()
    for a, b in combinations(VERTICES, 2):
        xa, ya = COORD[a]
        xb, yb = COORD[b]
        target = ((-xa - xb) % 3, (-ya - yb) % 3)
        c = next(i for i in VERTICES if COORD[i] == target)
        assert c not in (a, b)
        line_masks.add((1 << a) | (1 << b) | (1 << c))
    assert len(line_masks) == 12
    for a, b in combinations(VERTICES, 2):
        assert sum((l & (1 << a) != 0) and (l & (1 << b) != 0)
                   for l in line_masks) == 1

    faces = {mask for mask in range(1, 1 << 9)
             if all(mask & line != line for line in line_masks)}
    f_vector = Counter(mask.bit_count() - 1 for mask in faces)
    assert dict(f_vector) == {0: 9, 1: 36, 2: 72, 3: 54}
    assert len(faces) == 171

    # Toggle free vertices in a specified deterministic order.
    available = set(faces)
    pairs = []
    for v in ORDER:
        for lo in sorted(available, key=lambda f: (f.bit_count(), f)):
            if lo not in available or (lo & (1 << v)):
                continue
            hi = lo | (1 << v)
            if hi in available:
                assert hi.bit_count() == lo.bit_count() + 1
                available.remove(lo)
                available.remove(hi)
                pairs.append((lo, hi))

    critical = {d: sorted(f for f in available if f.bit_count() == d + 1)
                for d in range(4)}
    assert critical == {
        0: [32],
        1: [],
        2: [145],
        3: [29, 78, 83, 197, 269, 278, 323, 325, 332, 344, 393],
    }
    assert len(pairs) == 79
    assert len({f for pair in pairs for f in pair}) == 158
    assert len(available) == 13
    assert all(lo in faces and hi in faces for lo, hi in pairs)

    # Forman's acyclicity test: direct every unmatched cover downward,
    # and every matched cover upward. Verify entire finite Hasse graph.
    matched = set(pairs)
    adj = {f: [] for f in faces}
    indeg = {f: 0 for f in faces}
    incidence_count = 0
    for hi in faces:
        if hi.bit_count() < 2:
            continue
        for lo, _sign in boundary(hi):
            assert lo in faces
            incidence_count += 1
            src, dst = (lo, hi) if (lo, hi) in matched else (hi, lo)
            adj[src].append(dst)
            indeg[dst] += 1
    queue = deque(sorted(f for f in faces if indeg[f] == 0))
    topo = []
    while queue:
        a = queue.popleft()
        topo.append(a)
        for b in adj[a]:
            indeg[b] -= 1
            if indeg[b] == 0:
                queue.append(b)
    assert len(topo) == len(faces), 'Morse matching is cyclic'

    upper_of = {lo: hi for lo, hi in pairs}
    lower_of = {hi: lo for lo, hi in pairs}
    critical_triangle = critical[2][0]
    active = set()

    @lru_cache(None)
    def project_triangle(face):
        # Project a triangular chain onto the unique critical triangle
        # using integral elementary cancellations along gradient paths.
        assert face.bit_count() == 3
        if face == critical_triangle:
            return 1
        if face in lower_of:
            assert lower_of[face].bit_count() == 2
            return 0
        assert face in upper_of
        tet = upper_of[face]
        assert tet.bit_count() == 4
        assert face not in active
        active.add(face)
        coefficients = dict(boundary(tet))
        pivot = coefficients.pop(face)
        assert pivot in (-1, 1)
        val = -sum(c * project_triangle(g) for g, c in coefficients.items()) * pivot
        active.remove(face)
        return val

    morse_boundary = []
    for tet in critical[3]:
        morse_boundary.append(sum(c * project_triangle(g)
                                  for g, c in boundary(tet)))
    assert morse_boundary == [0] * 11

    # Independent modular cross-check of unreduced boundary maps.
    chain = {k: sorted(f for f in faces if f.bit_count() == k)
             for k in range(1, 5)}
    ranks = {}
    for k in (2, 3, 4):
        row_index = {f: j for j, f in enumerate(chain[k - 1])}
        columns = [sum(1 << row_index[g] for g, _c in boundary(f))
                   for f in chain[k]]
        ranks[k] = rank_mod2(columns)
    assert ranks == {2: 8, 3: 28, 4: 43}
    assert len(chain[3]) - ranks[3] - ranks[4] == 1
    assert len(chain[4]) - ranks[4] == 11

    # Independent algebraic chain cancellation: eliminate the actual 79
    # unit-incidence pairs, updating integer boundary columns exactly.
    reduced = {face: dict(boundary(face)) if face.bit_count() >= 2 else {}
               for face in faces}
    active_faces = set(faces)
    remaining_pairs = set(pairs)
    unit_steps = 0
    while remaining_pairs:
        options = sorted(
            (a, b, reduced[b][a]) for a, b in remaining_pairs
            if a in reduced[b] and abs(reduced[b][a]) == 1
        )
        assert options, 'No unit cancellation available'
        a, b, pivot = min(options, key=lambda triple:
                          (triple[1].bit_count(), triple[0], triple[1]))
        for c in tuple(active_faces):
            if c != b and c.bit_count() == b.bit_count() and a in reduced[c]:
                multiplier = reduced[c][a] * pivot
                for row, coefficient in reduced[b].items():
                    reduced[c][row] = (reduced[c].get(row, 0)
                                       - multiplier * coefficient)
                    if reduced[c][row] == 0:
                        del reduced[c][row]
        for c in tuple(active_faces):
            if c.bit_count() == b.bit_count() + 1:
                reduced[c].pop(b, None)
        active_faces.remove(a)
        active_faces.remove(b)
        remaining_pairs.remove((a, b))
        unit_steps += 1
    assert unit_steps == 79
    assert active_faces == available
    assert all(not reduced[face] for face in active_faces)

    print('HESSE_CAP_VERIFIED')
    print('face_vector=9,36,72,54')
    print('nonempty_faces=171')
    print('matched_pairs=79')
    print('exact_unit_cancellations=' + str(unit_steps))
    print('hasse_incidences=' + str(incidence_count))
    print('directed_hasse_vertices=' + str(len(topo)))
    print('critical_vector=1,0,1,11')
    print('critical_2_simplex=145')
    print('critical_3_simplices=' + ','.join(map(str, critical[3])))
    print('integral_morse_boundary_3_to_2=' + ','.join(map(str, morse_boundary)))
    print('unreduced_mod2_boundary_ranks=8,28,43')
    print('homotopy=S^2 wedge 11 S^3')


if __name__ == '__main__':
    verify()
