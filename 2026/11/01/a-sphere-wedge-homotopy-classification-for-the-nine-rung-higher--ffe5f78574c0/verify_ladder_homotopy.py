#!/usr/bin/env python3
"""Exact finite certificate for the 9-rung ladder two-independence complex.

Requires only Python 3 standard library. Vertices 0..8 are the first rail,
9..17 the second rail. Face masks are positive 18-bit integers.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 9
ORDER = [10, 14, 9, 5, 17, 2, 4, 11, 6, 16, 12, 13, 3, 0, 1, 15, 8, 7]
EXPECTED_5_SUPPORT = [73875, 73878, 74386, 75922]
EXPECTED_7_CRITICAL = [37291, 37801, 69995, 70505]


def direct_edges():
    edges = [(i, i + 1) for i in range(8)]
    edges += [(i + 9, i + 10) for i in range(8)]
    edges += [(i, i + 9) for i in range(9)]
    return edges


def graph_masks():
    adj = [0] * 18
    for a, b in direct_edges():
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return adj


def graph_face(mask, adj):
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        vertex = bit.bit_length() - 1
        if (mask & adj[vertex]).bit_count() > 1:
            return False
    return True


def local_faces():
    """Independent column-based enumeration, without using graph adjacency."""
    collected = []

    def middle_column_ok(before, middle, after):
        if middle & 1 and ((before & 1) != 0) + ((after & 1) != 0) + ((middle & 2) != 0) > 1:
            return False
        if middle & 2 and ((before & 2) != 0) + ((after & 2) != 0) + ((middle & 1) != 0) > 1:
            return False
        return True

    def rec(index, before, middle, mask):
        if index == N:
            if mask and middle_column_ok(before, middle, 0):
                collected.append(mask)
            return
        for after in range(4):
            if middle_column_ok(before, middle, after):
                new_mask = mask | ((after & 1) << index) | ((after & 2) << (N + index - 1))
                rec(index + 1, middle, after, new_mask)

    for first in range(4):
        rec(1, 0, first, (first & 1) | ((first & 2) << (N - 1)))
    return collected


def facets(mask):
    original = mask
    while mask:
        bit = mask & -mask
        yield original ^ bit
        mask -= bit


def main():
    faces = local_faces()
    face_set = set(faces)
    assert len(faces) == len(face_set) == 22692
    adj = graph_masks()
    direct = {mask for mask in range(1, 1 << (2 * N)) if graph_face(mask, adj)}
    assert direct == face_set, 'Two independent face tests disagree'
    print('MEMBERSHIP 262143 nonempty vertex subsets checked; 22692 faces')

    remaining = set(face_set)
    pairs = []
    for vertex in ORDER:
        bit = 1 << vertex
        for lower in faces:
            upper = lower | bit
            if lower in remaining and lower & bit == 0 and upper in remaining:
                remaining.remove(lower)
                remaining.remove(upper)
                pairs.append((lower, upper))
    assert len(pairs) == 11343
    crit = Counter(mask.bit_count() - 1 for mask in remaining)
    assert crit == {0: 1, 5: 1, 7: 4}, crit
    print('MATCHING 11343 pairs; critical cells', dict(sorted(crit.items())))

    lower_to_upper = dict(pairs)
    upper_to_lower = {upper: lower for lower, upper in pairs}
    assert len(lower_to_upper) == len(upper_to_lower) == len(pairs)
    assert len(remaining) + 2 * len(pairs) == len(faces)

    outgoing = {mask: [] for mask in faces}
    indegree = {mask: 0 for mask in faces}
    incidences = 0
    for upper in faces:
        for lower in facets(upper):
            if not lower:
                continue
            incidences += 1
            if lower_to_upper.get(lower) == upper:
                a, b = lower, upper
            else:
                a, b = upper, lower
            outgoing[a].append(b)
            indegree[b] += 1
    ready = deque(mask for mask in faces if indegree[mask] == 0)
    visited = 0
    while ready:
        a = ready.popleft()
        visited += 1
        for b in outgoing[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                ready.append(b)
    assert visited == len(faces), 'Gradient cycle detected'
    print('ACYCLIC', incidences, 'covering incidences,', visited, 'faces sorted')
    del outgoing, indegree

    critical5 = [mask for mask in remaining if mask.bit_count() == 6]
    critical7 = sorted(mask for mask in remaining if mask.bit_count() == 8)
    assert critical5 == [74386] and critical7 == EXPECTED_7_CRITICAL

    @lru_cache(None)
    def cochain5(mask):
        # Mod-2 Morse projection dual for degree-five simplices.
        if mask in remaining:
            return int(mask == critical5[0])
        if mask in upper_to_lower:
            return 0
        upper = lower_to_upper[mask]
        return sum(cochain5(y) for y in facets(upper) if y != mask) % 2

    support5 = sorted(mask for mask in faces if mask.bit_count() == 6 and cochain5(mask))
    assert support5 == EXPECTED_5_SUPPORT, support5
    assert not any(sum(cochain5(y) for y in facets(upper)) % 2
                   for upper in faces if upper.bit_count() == 7)
    core = support5[0]
    for mask in support5:
        core &= mask
    assert core.bit_count() == 5
    assert all((x | y).bit_count() <= 7 for x in support5 for y in support5)
    print('FIVE_COCYCLE', support5, 'shared-five-vertex core', core)

    # Direct evaluation of Medina-Mardones's cup-3 diagonal on 7-simplices.
    # The two tensor factors must each be 5-dimensional.  The formula
    # partitions deleted positions by parity of u_j-j, with j one-based;
    # its interchange of the two factors is immaterial for alpha cup alpha.
    cuts = []
    for selected in combinations(range(8), 4):
        part0 = [u for j, u in enumerate(selected) if (u - (j + 1)) % 2 == 0]
        part1 = [u for j, u in enumerate(selected) if (u - (j + 1)) % 2 != 0]
        if len(part0) == len(part1) == 2:
            cuts.append((part0, part1))
    assert len(cuts) == 18
    squares = 0
    for mask in faces:
        if mask.bit_count() != 8:
            continue
        vertices = [i for i in range(18) if mask & (1 << i)]
        value = 0
        for p0, p1 in cuts:
            left = mask ^ (1 << vertices[p0[0]]) ^ (1 << vertices[p0[1]])
            right = mask ^ (1 << vertices[p1[0]]) ^ (1 << vertices[p1[1]])
            value ^= cochain5(left) & cochain5(right)
        squares += value
    assert squares == 0, 'Square must vanish as a cochain'
    print('STEENROD_SQ2 cochain identically zero (18 cup-3 terms per 7-face)')

    @lru_cache(None)
    def lift_cycle(upper):
        chain = {upper}
        for facet in facets(upper):
            if facet in lower_to_upper and lower_to_upper[facet] != upper:
                chain.symmetric_difference_update(lift_cycle(lower_to_upper[facet]))
        return frozenset(chain)

    def mod2_boundary(chain):
        boundary = set()
        for cell in chain:
            for f in facets(cell):
                if f in boundary:
                    boundary.remove(f)
                else:
                    boundary.add(f)
        return boundary

    generator5 = lift_cycle(critical5[0])
    assert not mod2_boundary(generator5)
    assert sum(cochain5(cell) for cell in generator5) % 2 == 1
    for crit7 in critical7:
        lifted7 = lift_cycle(crit7)
        assert not mod2_boundary(lifted7), crit7
        assert [int(m in lifted7) for m in critical7] == [int(m == crit7) for m in critical7]
    print('CYCLES mod-2 generator in degree 5 and four independent degree-7 cycles verified')
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
