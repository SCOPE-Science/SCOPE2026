"""Standalone exhaustive certificate for the Heawood Hamiltonian-containment complex.
Requires Python 3.9+ and standard library only. Run: python heawood_hamilton_verify.py
"""
from collections import Counter, deque
from itertools import permutations


def verify():
    # Points 0,...,6, lines 7,...,13; difference-set coordinates of the Fano plane.
    lines = [{j, (j + 1) % 7, (j + 3) % 7} for j in range(7)]
    assert len({frozenset(x) for x in lines}) == 7
    assert all(sum(p in L and q in L for L in lines) == 1
               for p in range(7) for q in range(p + 1, 7))
    edges = [(p, 7 + j) for j, L in enumerate(lines) for p in sorted(L)]
    assert len(edges) == 21
    adjacency = [set() for _ in range(14)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    assert all(len(n) == 3 for n in adjacency)
    edge_number = {e: i for i, e in enumerate(edges)}

    # Exhaustive 14-vertex Hamiltonian cycles, normalized to start at vertex zero
    # and to use a single orientation.
    cycles = set()
    def search(path, used):
        last = path[-1]
        if len(path) == 14:
            if 0 in adjacency[last] and path[1] < last:
                m = 0
                for a, b in zip(path, path[1:] + [0]):
                    m |= 1 << edge_number[tuple(sorted((a, b)))]
                assert m.bit_count() == 14
                cycles.add(m)
            return
        for nxt in sorted(adjacency[last]):
            if not (used >> nxt & 1):
                search(path + [nxt], used | (1 << nxt))
    search([0], 1)
    assert len(cycles) == 24
    assert len({((1 << 21) - 1) ^ c for c in cycles}) == 24

    # Independent enumeration of perfect matchings in bipartite graph.
    matchings = set()
    def matching(point, taken, mask):
        if point == 7:
            assert taken == (1 << 7) - 1
            matchings.add(mask)
            return
        for line in range(7):
            if point in lines[line] and not (taken >> line & 1):
                matching(point + 1, taken | (1 << line),
                         mask | (1 << edge_number[(point, line + 7)]))
    matching(0, 0, 0)
    assert len(matchings) == 24
    assert {((1 << 21) - 1) ^ m for m in matchings} == cycles

    # All faces are precisely subsets of the twenty-four maximal 14-edge facets.
    faces = {0}
    for facet in cycles:
        s = facet
        while s:
            faces.add(s)
            s = (s - 1) & facet
    assert len(faces) == 252903
    f_vector = [sum(f.bit_count() == k for f in faces) for k in range(1, 15)]
    assert f_vector == [21, 210, 1316, 5691, 17346, 37072, 55380,
                        58170, 43400, 23100, 8652, 2184, 336, 24]

    # Elementary toggles in sorted edge order. Reserve empty face and vertex 0
    # as unpaired. Every remaining face is paired at the first feasible stage.
    active = set(faces)
    partner = {}
    for e in range(21):
        bit = 1 << e
        pairs = [(f, f | bit) for f in active
                 if f not in (0, 1) and not f & bit and (f | bit) in active]
        for lo, hi in pairs:
            assert lo in active and hi in active
            assert lo not in partner and hi not in partner
            assert hi.bit_count() == lo.bit_count() + 1
            partner[lo] = hi
            partner[hi] = lo
        for lo, hi in pairs:
            active.remove(lo)
            active.remove(hi)
    assert len(partner) == len(faces) - 3
    assert active == {0, 1, 674086}
    assert (674086).bit_count() == 8

    # Full directed Hasse diagram: upper -> lower on unmatched incidences,
    # lower -> upper on matched incidences. A topological order proves acyclicity.
    # Empty face is excluded from the ordinary nonempty face poset.
    indeg = {f: 0 for f in faces if f}
    incidents = 0
    for upper in indeg:
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = upper ^ bit
            if lower == 0:
                continue
            if partner.get(lower) == upper:
                indeg[upper] += 1
            else:
                indeg[lower] += 1
            incidents += 1
    assert incidents == 1936998
    queue = deque(f for f, d in indeg.items() if d == 0)
    visited = 0
    while queue:
        face = queue.popleft()
        visited += 1
        up = partner.get(face)
        if up is not None and up.bit_count() == face.bit_count() + 1:
            indeg[up] -= 1
            if indeg[up] == 0:
                queue.append(up)
        bits = face
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = face ^ bit
            if not lower or partner.get(lower) == face:
                continue
            indeg[lower] -= 1
            if indeg[lower] == 0:
                queue.append(lower)
    assert visited == len(faces) - 1
    assert not any(indeg.values())
    # One critical vertex and one critical 7-simplex imply a CW model S^7.
    print('graph_vertices=14 graph_edges=21')
    print('hamiltonian_cycles=24 perfect_matchings=24 complements_equal=True')
    print('nonempty_faces=252902')
    print('f_vector=' + ','.join(map(str, f_vector)))
    print('morse_pairs=126450')
    print('critical_nonempty=1 vertex, 1 seven_simplex')
    print('directed_face_incidences=1936998')
    print('topological_sort_visited=252902')
    print('homotopy_type=S7')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
