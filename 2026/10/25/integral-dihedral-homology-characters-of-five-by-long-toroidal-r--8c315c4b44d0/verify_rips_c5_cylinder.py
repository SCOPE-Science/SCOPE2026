#!/usr/bin/env python3
"""Reproduce local elementary collapses for the width-five graph-metric Rips complex.

All calculations use exact finite simplicial complexes and Python's standard library.
The uniform all-width argument is mathematical: every distance-two cross-column
edge has the same three-vertex simplex link when the second circumference is >=7.
"""

from collections import Counter
from itertools import combinations


def faces_of_graph(vertices, distance):
    vertices = tuple(vertices)
    adjacent = {
        i: {j for j in range(i + 1, len(vertices)) if distance(vertices[i], vertices[j]) <= 2}
        for i in range(len(vertices))
    }
    result = set()

    def grow(prefix, choices):
        for j in sorted(choices):
            new = prefix + (j,)
            result.add(new)
            grow(new, choices.intersection(adjacent[j]))

    grow((), set(range(len(vertices))))
    return result


def two_column_faces():
    vertices = tuple((r, c) for r in range(5) for c in range(2))

    def distance(v, w):
        return min((v[0] - w[0]) % 5, (w[0] - v[0]) % 5) + abs(v[1] - w[1])

    return vertices, faces_of_graph(vertices, distance)


def free_pair(complex_faces, lower, upper):
    assert lower in complex_faces and upper in complex_faces
    assert len(upper) == len(lower) + 1 and set(lower) < set(upper)
    N = 1 + max(max(f) for f in complex_faces)
    # A free face is contained in exactly one maximal simplex, which is upper.
    ups = [tuple(sorted(lower + (v,))) for v in range(N) if v not in lower]
    assert [q for q in ups if q in complex_faces] == [upper], (lower, upper)
    assert not any(tuple(sorted(upper + (v,))) in complex_faces
                   for v in range(N) if v not in upper), upper
    complex_faces.remove(lower)
    complex_faces.remove(upper)


def local_octahedron_certificate():
    vertices, faces = two_column_faces()
    assert Counter(map(len, faces)) == {1: 10, 2: 35, 3: 50, 4: 25, 5: 2}
    faces = set(faces)
    moves = 0
    stage_counts = []
    for cutoff in (3, 2, 1):
        while True:
            pair = None
            for upper in sorted((f for f in faces if len(f) > cutoff),
                                key=lambda f: (-len(f), f)):
                if any(tuple(sorted(upper + (v,))) in faces
                       for v in range(10) if v not in upper):
                    continue
                for lower in combinations(upper, len(upper) - 1):
                    supers = [tuple(sorted(lower + (v,)))
                              for v in range(10) if v not in lower]
                    if [q for q in supers if q in faces] == [upper]:
                        pair = lower, upper
                        break
                if pair is not None:
                    break
            if pair is None:
                break
            free_pair(faces, *pair)
            moves += 1
        stage_counts.append((cutoff, moves, dict(Counter(map(len, faces)))))
    assert moves == 48
    assert Counter(map(len, faces)) == {1: 6, 2: 12, 3: 8}
    tri = [f for f in faces if len(f) == 3]
    assert len(tri) == 8
    support = {v for f in faces for v in f}
    opposite = {(u, v) for u, v in combinations(sorted(support), 2)
                if (u, v) not in faces}
    assert len(opposite) == 3
    assert len({v for pair in opposite for v in pair}) == 6
    assert all(len([f for f in tri if e[0] in f and e[1] in f]) == 0
               for e in opposite)
    assert all(len([f for f in tri if e.issubset(set(f))]) == 2
               for e in map(set, (f for f in faces if len(f) == 2)))
    print('TWO-COLUMN BLOCK: 48 valid elementary collapses to octahedral 2-sphere')
    print('Local collapse stages:', stage_counts)
    print('Octahedron opposite vertex pairs:', [(vertices[u], vertices[v]) for u, v in sorted(opposite)])


def full_torus_faces(n):
    vertices = tuple((r, c) for r in range(5) for c in range(n))

    def distance(v, w):
        return (min((v[0] - w[0]) % 5, (w[0] - v[0]) % 5)
                + min((v[1] - w[1]) % n, (w[1] - v[1]) % n))

    return vertices, faces_of_graph(vertices, distance)


def check_uniform_global_collapses(n):
    assert n >= 7
    vertices, full = full_torus_faces(n)
    ix = {v: i for i, v in enumerate(vertices)}
    assert Counter(map(len, full)) == {1: 5*n, 2: 30*n, 3: 55*n, 4: 35*n, 5: 6*n}
    full = set(full)
    move_count = 0
    for center in range(n):
        for r in range(5):
            ends = {ix[r, (center-1) % n], ix[r, (center+1) % n]}
            midpoint = ix[r, center]
            sides = (ix[(r-1) % 5, center], ix[(r+1) % 5, center])
            for size in (2, 1, 0):
                for other in combinations(sides, size):
                    low = tuple(sorted(ends.union(other)))
                    high = tuple(sorted(set(low).union({midpoint})))
                    free_pair(full, low, high)
                    move_count += 1
    assert move_count == 20*n
    # Remaining cliques are precisely supported in one column or two neighboring columns.
    assert all(len({vertices[j][1] for j in f}) <= 2
               and (len({vertices[j][1] for j in f}) == 1
                    or any({vertices[j][1] for j in f} == {c, (c+1) % n}
                           for c in range(n))) for f in full)
    target = set()
    for c in range(n):
        ids = {ix[r, cc] for r in range(5) for cc in (c, (c+1) % n)}
        target.update(f for f in full if set(f) <= ids)
    assert full == target
    assert Counter(map(len, full)) == {1: 5*n, 2: 25*n, 3: 40*n, 4: 20*n, 5: n}
    print(f'C5 x C{n}: {move_count} exact free-face pairs; remaining complex is the necklace of {n} two-column blocks.')


def main():
    local_octahedron_certificate()
    for n in (7, 8, 9, 10, 11, 12):
        check_uniform_global_collapses(n)
    print('All exact finite checks passed. Infinite extension uses the uniform link classification.')


if __name__ == '__main__':
    main()
