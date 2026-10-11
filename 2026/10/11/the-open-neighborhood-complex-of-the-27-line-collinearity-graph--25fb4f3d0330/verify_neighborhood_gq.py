#!/usr/bin/env python3
"""Complete discrete Morse certificate for the open-neighborhood complex
of the 27-line intersection graph of a smooth cubic surface.
Standard library only; all incidences checked, no external data required.
"""
from collections import Counter, deque
from itertools import combinations


def lines_on_cubic():
    # Each divisor class is (a,b_1,...,b_6) with square a^2-sum b_i^2.
    classes = []
    for i in range(6):
        b = [0] * 6
        b[i] = 1
        classes.append((0, tuple(b)))    # E_i
    for i, j in combinations(range(6), 2):
        b = [0] * 6
        b[i] = b[j] = -1
        classes.append((1, tuple(b)))    # L-E_i-E_j
    for i in range(6):
        b = [-1] * 6
        b[i] = 0
        classes.append((2, tuple(b)))    # 2L-sum_{j != i} E_j
    assert len(classes) == 27
    return classes


def main():
    classes = lines_on_cubic()
    near = [0] * 27
    for i, j in combinations(range(27), 2):
        a, b = classes[i]
        c, d = classes[j]
        intersection = a * c - sum(x * y for x, y in zip(b, d))
        assert intersection in (0, 1), (i, j, intersection)
        if intersection == 1:
            near[i] |= 1 << j
            near[j] |= 1 << i
    assert {x.bit_count() for x in near} == {10}
    assert sum(x.bit_count() for x in near) // 2 == 135
    for i, j in combinations(range(27), 2):
        n_common = (near[i] & near[j]).bit_count()
        is_edge = (near[i] >> j) & 1
        assert n_common == (1 if is_edge else 5)

    # Definition of the ordinary Lovasz open-neighborhood complex:
    # every nonempty subset of any open vertex neighborhood is a simplex.
    faces = set()
    for neighborhood in near:
        subset = neighborhood
        while subset:
            faces.add(subset)
            subset = (subset - 1) & neighborhood
    by_dimension = Counter(face.bit_count() - 1 for face in faces)
    expected = (27, 351, 1800, 4590, 6588, 5670, 3240, 1215, 270, 27)
    assert tuple(by_dimension[d] for d in range(10)) == expected
    assert len(faces) == 23778

    # Deterministic 27-step pivot-toggle matching (nonempty simplices only).
    remaining = set(faces)
    matched_lower_to_upper = {}
    for pivot in range(27):
        singleton = 1 << pivot
        for lower in sorted(remaining, key=lambda f: (f.bit_count(), f)):
            upper = lower | singleton
            if not (lower & singleton) and upper in remaining:
                assert upper.bit_count() == lower.bit_count() + 1
                remaining.remove(lower)
                remaining.remove(upper)
                matched_lower_to_upper[lower] = upper
    assert len(matched_lower_to_upper) == 11853
    assert Counter(face.bit_count() - 1 for face in remaining) == {0: 1, 4: 71}

    # Full Hasse diagram: point every codimension-1 incidence upwards,
    # except that precisely the matched pairs point downwards.
    incoming = {face: 0 for face in faces}
    outgoing = {face: [] for face in faces}
    arrows = 0
    for upper in faces:
        peel = upper
        while peel:
            singleton = peel & -peel
            peel ^= singleton
            lower = upper ^ singleton
            if lower not in faces:  # the empty face is deliberately excluded
                continue
            source, destination = ((upper, lower) if
                matched_lower_to_upper.get(lower) == upper else (lower, upper))
            outgoing[source].append(destination)
            incoming[destination] += 1
            arrows += 1
    assert arrows == 126522
    queue = deque(face for face in faces if incoming[face] == 0)
    visited = 0
    while queue:
        source = queue.popleft()
        visited += 1
        for destination in outgoing[source]:
            incoming[destination] -= 1
            if incoming[destination] == 0:
                queue.append(destination)
    assert visited == len(faces), f'directed cycle; processed {visited} of {len(faces)}'
    assert sum((-1)**dimension * count for dimension, count in enumerate(expected)) == 72
    print('PASS geometry: (27,10,1,5) collinearity graph on 27 exceptional curves')
    print('PASS complex: 23778 nonempty faces, f-vector =', expected)
    print('PASS Morse: 11853 pairs, one critical 0-cell and 71 critical 4-cells')
    print('PASS acyclicity: 126522 directed Hasse edges, 23778/23778 vertices sorted')
    print('THEOREM: open-neighborhood complex is a wedge of 71 four-spheres')


if __name__ == '__main__':
    main()
