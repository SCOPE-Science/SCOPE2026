#!/usr/bin/env python3
"""Exhaustive, integer-only verification of a Heawood higher-independence plateau.

Requires Python 3.10+; no external packages. The graph has point vertices
0,...,6 and line vertices 7,...,13. Line j contains j,j+1,j+3 mod 7.
"""
if not __debug__:
    raise RuntimeError("Run without Python -O: exhaustive assertions must remain enabled")

from collections import Counter, deque
from itertools import combinations

N = 14
VERTICES = range(N)
POINTS = range(7)
LINES = tuple(frozenset(((j + k) % 7) for k in (0, 1, 3)) for j in range(7))
ADJ = [0] * N
for j, line in enumerate(LINES):
    for i in line:
        ADJ[i] |= 1 << (7 + j)
        ADJ[7 + j] |= 1 << i


def connected_component_limit(mask, upper):
    """Direct queue/bitmask traversal of induced connected components."""
    remaining = mask
    while remaining:
        seed = remaining & -remaining
        remaining -= seed
        found = seed
        frontier = seed
        while frontier:
            vbit = frontier & -frontier
            frontier ^= vbit
            v = vbit.bit_length() - 1
            newly = ADJ[v] & remaining
            found |= newly
            remaining ^= newly
            frontier |= newly
            if found.bit_count() > upper:
                return False
    return True


def induced_connected(mask):
    """Independent graph-traversal implementation with Python sets."""
    vertices = {j for j in VERTICES if (mask >> j) & 1}
    if not vertices:
        return False
    reached = {min(vertices)}
    todo = [min(vertices)]
    while todo:
        u = todo.pop()
        for v in vertices - reached:
            if (ADJ[u] >> v) & 1:
                reached.add(v)
                todo.append(v)
    return reached == vertices


def all_faces_by_forbidden(k):
    """A set is admissible iff it avoids all connected induced k-sets."""
    forbidden = []
    for tup in combinations(VERTICES, k):
        mask = sum(1 << j for j in tup)
        if induced_connected(mask):
            forbidden.append(mask)
    faces = set()
    for mask in range(1, 1 << N):
        if all((mask & obstruction) != obstruction for obstruction in forbidden):
            faces.add(mask)
    return faces, len(forbidden)


def toggle_matching(faces, order):
    """Successive element-pivot matching on remaining faces."""
    unmatched = set(faces)
    pairs = []
    for v in order:
        bit = 1 << v
        for lower in sorted(unmatched):
            if lower not in unmatched or lower & bit:
                continue
            upper = lower | bit
            if upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    return pairs, unmatched


def count_acyclic_digraph(faces, pairs):
    """Full cover-incidence cycle check, reversing exactly matched edges."""
    paired = {a: b for a, b in pairs}
    assert len(paired) == len(pairs)
    assert all(a in faces and b in faces and (b ^ a).bit_count() == 1
               and (b & a) == a for a, b in pairs)
    assert 2 * len(pairs) == len({x for ab in pairs for x in ab})
    outgoing = {m: [] for m in faces}
    indegree = {m: 0 for m in faces}
    incidences = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = upper ^ bit
            if lower not in faces:
                continue
            if paired.get(lower) == upper:
                src, dst = lower, upper
            else:
                src, dst = upper, lower
            outgoing[src].append(dst)
            indegree[dst] += 1
            incidences += 1
    queue = deque(m for m, deg in indegree.items() if deg == 0)
    consumed = 0
    while queue:
        x = queue.popleft()
        consumed += 1
        for y in outgoing[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert consumed == len(faces), (consumed, len(faces))
    return incidences


def actual_relative_collapse(base, extended, pairs):
    """Replay each free-face removal in the ambient simplicial complex."""
    assert base < extended
    relative = extended - base
    assert len(relative) == 2 * len(pairs)
    paired_low = {a: b for a, b in pairs}
    assert len(paired_low) == len(pairs)
    assert {x for pair in pairs for x in pair} == relative
    active = set(extended)
    count = 0
    while paired_low:
        chosen = None
        for lower, upper in paired_low.items():
            if upper not in active or lower not in active:
                raise AssertionError('matched cell missing before collapse')
            immediate_superfaces = [lower | (1 << v) for v in VERTICES
                                    if not ((lower >> v) & 1)
                                    and (lower | (1 << v)) in active]
            if immediate_superfaces == [upper]:
                assert not any((upper | (1 << v)) in active
                               for v in VERTICES if not ((upper >> v) & 1))
                chosen = (lower, upper)
                break
        assert chosen is not None, ('no free pair', len(paired_low))
        lower, upper = chosen
        del paired_low[lower]
        active.remove(lower)
        active.remove(upper)
        count += 1
    assert active == base
    return count


def main():
    assert all(len(s) == 3 for s in LINES)
    assert all(sum(i in s for s in LINES) == 3 for i in POINTS)
    assert all(len(LINES[i] & LINES[j]) == 1
               for i in POINTS for j in POINTS if i < j)

    # Compare independent exhaustive predicates at all five consecutive stages.
    direct = {r: {m for m in range(1, 1 << N)
                  if connected_component_limit(m, r)} for r in range(2, 7)}
    expected_counts = {2: 2256, 3: 4622, 4: 6190, 5: 7870, 6: 9683}
    expected_eulers = {2: -12, 3: 2, 4: 2, 5: 2, 6: -19}
    for r in range(2, 7):
        other, connected_count = all_faces_by_forbidden(r + 1)
        assert direct[r] == other, r
        fvec = Counter(m.bit_count() - 1 for m in direct[r])
        chi = sum(((-1) ** dim) * count for dim, count in fvec.items())
        assert len(direct[r]) == expected_counts[r]
        assert chi == expected_eulers[r]
        print('stage', r, 'faces', len(direct[r]),
              'f_vector', dict(sorted(fvec.items())), 'Euler', chi,
              'connected_forbidden', connected_count)
    F3 = direct[3]
    assert all(direct[r] < direct[r + 1] for r in range(2, 6))

    # Complete acyclic Morse matching on Ind_3(H): one 0-cell, one 6-cell.
    order3 = (8, 12, 10, 6, 3, 9, 13, 5, 11, 1, 2, 7, 0, 4)
    whole_pairs, critical = toggle_matching(F3, order3)
    assert len(whole_pairs) == 2310
    assert critical == {1 << 8, 10454}, critical
    assert (10454).bit_count() == 7
    whole_inc = count_acyclic_digraph(F3, whole_pairs)
    print('stage3_matching_pairs', len(whole_pairs),
          'critical_masks', sorted(critical), 'cover_relations', whole_inc)

    # Actual elementary simplicial collapses, not only abstract Morse models.
    for r in (4, 5):
        base, extended = direct[r - 1], direct[r]
        relative = extended - base
        pairs, critical = toggle_matching(relative, tuple(VERTICES))
        assert not critical
        assert len(relative) == (1568 if r == 4 else 1680)
        assert len(pairs) == (784 if r == 4 else 840)
        relative_incidences = count_acyclic_digraph(relative, pairs)
        collapses = actual_relative_collapse(base, extended, pairs)
        assert collapses == len(pairs)
        print('stage', r, 'to', r - 1, 'relative_faces', len(relative),
              'relative_matching_pairs', len(pairs),
              'relative_cover_relations', relative_incidences,
              'actual_free_pair_collapses', collapses)

    print('HEAWOOD_IND3_TO_IND5_PLATEAU_AND_BOUNDARIES_VERIFIED')


if __name__ == '__main__':
    main()
