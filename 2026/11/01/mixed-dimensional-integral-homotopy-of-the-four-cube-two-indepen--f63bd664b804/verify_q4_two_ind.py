#!/usr/bin/env python3
"""Reproducible exhaustive certificate for the 2-independence complex of Q4.

No third-party modules are required. Vertices are 0,...,15, encoded in binary.
All graph and simplicial-complex arithmetic is exact.
"""
from collections import Counter, defaultdict, deque

D = 4
N = 1 << D
PIVOTS = [15, 0, 4, 3, 8, 11, 10, 13, 9, 14, 2, 7, 6, 1, 5, 12]
EXPECTED_VECTOR = [1, 16, 120, 464, 964, 960, 440, 80, 10]
EXPECTED_CRITICAL_3 = [408, 960, 1440, 2328, 2640, 3120, 4488, 6168,
                       8772, 9252, 10260, 12300, 16962, 17442, 18450, 20490]
EXPECTED_CRITICAL_4 = [6800]

NEIGH = [sum(1 << v for v in range(N) if (u ^ v).bit_count() == 1)
         for u in range(N)]


def permitted(mask):
    # Graph components must have at most two vertices. This is equivalently
    # the absence of a vertex with two selected neighbors.
    return all((NEIGH[v] & mask).bit_count() <= 1
               for v in range(N) if (mask >> v) & 1)


def independently_permitted(mask):
    # Separate breadth-first connected-component criterion.
    remaining = mask
    while remaining:
        start = remaining & -remaining
        frontier = start
        component = 0
        while frontier:
            bit = frontier & -frontier
            frontier -= bit
            if component & bit:
                continue
            component |= bit
            if component.bit_count() > 2:
                return False
            vertex = bit.bit_length() - 1
            frontier |= NEIGH[vertex] & mask & ~component
        remaining &= ~component
    return True


def boundary(mask):
    """List of (codimension-one face, integral incidence sign)."""
    ans = []
    bits = mask
    i = 0
    while bits:
        bit = bits & -bits
        bits -= bit
        ans.append((mask ^ bit, -1 if i & 1 else 1))
        i += 1
    return ans


def topo_sort(nodes, edges):
    degrees = {v: 0 for v in nodes}
    for v, targets in edges.items():
        for w in targets:
            degrees[w] += 1
    queue = deque(v for v in nodes if degrees[v] == 0)
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for w in edges[v]:
            degrees[w] -= 1
            if degrees[w] == 0:
                queue.append(w)
    assert len(order) == len(nodes), 'a directed cycle was detected'
    return order


def gf2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            highest = col.bit_length() - 1
            if highest in pivots:
                col ^= pivots[highest]
            else:
                pivots[highest] = col
                break
    return len(pivots)


def main():
    faces = [m for m in range(1 << N) if permitted(m)]
    assert all(permitted(m) == independently_permitted(m) for m in range(1 << N))
    face_set = set(faces)
    assert all((mask ^ (1 << v)) in face_set
               for mask in faces for v in range(N) if (mask >> v) & 1)
    assert [sum(m.bit_count() == k for m in faces) for k in range(9)] == EXPECTED_VECTOR
    assert len(faces) == 3055
    facet_dim = Counter(mask.bit_count() - 1 for mask in faces
                        if not any((mask | (1 << v)) in face_set
                                   for v in range(N) if not ((mask >> v) & 1)))
    assert facet_dim == {3: 16, 5: 160, 7: 10}, facet_dim

    # Iterated element toggling: a face and its coface are removed together.
    # The resulting partial matching is independently checked for acyclicity.
    unmatched = set(faces)
    matching = {}
    for vertex in PIVOTS:
        assert len(unmatched) % 2 == (len(faces) % 2)
        for lower in sorted(unmatched):
            if (lower >> vertex) & 1:
                continue
            upper = lower | (1 << vertex)
            if upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                matching[lower] = upper
    critical = sorted(unmatched)
    assert 0 in matching, 'empty simplex must be paired'
    assert len(matching) == 1519
    assert sorted(v for v in critical if v.bit_count() == 4) == EXPECTED_CRITICAL_3
    assert sorted(v for v in critical if v.bit_count() == 5) == EXPECTED_CRITICAL_4
    assert len(critical) == 17
    assert Counter(v.bit_count() - 1 for v in critical) == {3: 16, 4: 1}

    # Every cover incidence in the full augmented face poset is oriented:
    # matched arcs from lower to higher; all other arcs higher to lower.
    oriented = {m: [] for m in faces}
    incidences = 0
    for upper in faces:
        for lower, _ in boundary(upper):
            incidences += 1
            if matching.get(lower) == upper:
                oriented[lower].append(upper)
            else:
                oriented[upper].append(lower)
    assert incidences == 13584, incidences
    topo_sort(faces, oriented)

    # Exact signed Morse differential from the unique critical dimension-4
    # face to all sixteen critical dimension-3 faces. Every integral gradient
    # propagation is performed explicitly, rather than inferred from mod 2.
    threefaces = [f for f in faces if f.bit_count() == 4]
    paths = {f: [] for f in threefaces}
    graph = {f: [] for f in threefaces}
    for lower, upper in matching.items():
        if lower.bit_count() != 4:
            continue
        incidents = dict(boundary(upper))
        pivot_sign = incidents[lower]
        for other, sign in incidents.items():
            if other != lower:
                graph[lower].append(other)
                paths[lower].append((other, -pivot_sign * sign))
    dim_order = topo_sort(threefaces, graph)
    alpha = EXPECTED_CRITICAL_4[0]
    coefficients = defaultdict(int)
    for face, sign in boundary(alpha):
        coefficients[face] += sign
    for face in dim_order:
        amount = coefficients[face]
        if face in matching:
            if amount:
                for other, multiplier in paths[face]:
                    coefficients[other] += amount * multiplier
            coefficients[face] = 0
    critical_boundary = {f: coefficients[f] for f in EXPECTED_CRITICAL_3}
    assert all(value == 0 for value in critical_boundary.values()), critical_boundary
    assert all(coefficients[f] == 0 for f in threefaces), 'nonzero residual'

    # Independent mod-two chain calculation on original full complex, not
    # the collapsed model, including the augmented empty face in degree -1.
    by_size = [[f for f in faces if f.bit_count() == size] for size in range(9)]
    ranks = {}
    for size in range(1, 9):
        index = {face: i for i, face in enumerate(by_size[size - 1])}
        columns = [sum(1 << index[lower] for lower, _ in boundary(upper))
                   for upper in by_size[size]]
        ranks[size] = gf2_rank(columns)
    ranks[0] = 0
    ranks[9] = 0
    betti = {size - 1: len(by_size[size]) - ranks[size] - ranks[size + 1]
             for size in range(9)}
    assert betti == {-1: 0, 0: 0, 1: 0, 2: 0, 3: 16, 4: 1,
                     5: 0, 6: 0, 7: 0}, betti
    reduced_euler = sum((-1) ** (size - 1) * len(by_size[size])
                        for size in range(9))
    assert reduced_euler == -15

    print('Q4_TWO_INDEPENDENCE_INTEGRAL_MORSE_OK')
    print('vertices=16 edges=32')
    print('f_vector_including_empty=' + str(EXPECTED_VECTOR))
    print('faces=3055 cover_incidences=13584 matched_pairs=1519')
    print('facet_count_by_dimension=' + str(dict(sorted(facet_dim.items()))))
    print('critical_cells={3:16, 4:1}; empty_face=paired')
    print('critical_three_faces=' + str(EXPECTED_CRITICAL_3))
    print('critical_four_face=' + str(EXPECTED_CRITICAL_4))
    print('exact_integer_Morse_boundary_4_to_3=' + str(list(critical_boundary.values())))
    print('reduced_GF2_betti=' + str(betti))
    print('reduced_euler_characteristic=-15')
    print('certificate: exhaustive enumeration, full acyclicity, exact signed Morse boundary, independent GF2 ranks')


if __name__ == '__main__':
    main()
