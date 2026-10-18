#!/usr/bin/env python3
"""Exact finite verification for two Heawood matching complexes and their symmetries.

Requires only Python 3.9+ standard library. All arithmetic is integral.
"""
import collections
import itertools
import json
from math import lcm

POINTS = tuple(range(1, 8))
EDGES = tuple((p, l) for p in POINTS for l in POINTS if (p & l).bit_count() % 2 == 0)
INDEX = {e: i for i, e in enumerate(EDGES)}
assert len(EDGES) == 21


def perfect_matchings():
    # A perfect matching is a bijection of points to incident lines.
    ans = []
    for perm in itertools.permutations(POINTS):
        if all((p & l).bit_count() % 2 == 0 for p, l in zip(POINTS, perm)):
            ans.append(sum(1 << INDEX[(p, l)] for p, l in zip(POINTS, perm)))
    assert len(ans) == len(set(ans)) == 24
    return tuple(sorted(ans))


def perfect_faces(facets):
    ans = {0}
    for facet in facets:
        edges = [i for i in range(21) if facet >> i & 1]
        assert len(edges) == 7
        for choice in range(128):
            ans.add(sum(1 << edges[j] for j in range(7) if choice >> j & 1))
    return ans - {0}


def all_matching_faces():
    ans = {0}
    for i, (p, l) in enumerate(EDGES):
        for face in tuple(ans):
            if all(not (EDGES[j][0] == p or EDGES[j][1] == l)
                   for j in range(21) if face >> j & 1):
                ans.add(face | (1 << i))
    return ans - {0}


def cell_histogram(faces):
    return dict(sorted(collections.Counter(x.bit_count()-1 for x in faces).items()))


PERFECT_PIVOTS = (4, 16, 8, 6, 13, 2, 7, 17, 15, 10, 12, 1,
                  20, 19, 14, 3, 11, 9, 0, 18, 5)
ORDINARY_PIVOTS = (6, 17, 9, 11, 7, 4, 5, 3, 15, 20, 16, 10,
                   18, 14, 8, 2, 0, 1, 19, 13, 12)


def morse_verify(faces, pivots, expected_critical):
    assert set(pivots) == set(range(21))
    remain = set(faces)
    pairset = set()
    for i in pivots:
        b = 1 << i
        ps = [(x, x | b) for x in remain if not x & b and x | b in remain]
        for lower, upper in ps:
            assert lower in remain and upper in remain and upper == lower | b
            remain.remove(lower)
            remain.remove(upper)
            pairset.add((lower, upper))
    crit = cell_histogram(remain)
    assert crit == expected_critical, (crit, expected_critical)

    # Construct the COMPLETE directed face-poset Hasse graph. A matched
    # incidence points upward, every other incidence downward.
    incoming = {f: 0 for f in faces}
    outgoing = {f: [] for f in faces}
    incidence_count = 0
    for upper in faces:
        for i in range(21):
            b = 1 << i
            if not upper & b:
                continue
            lower = upper ^ b
            if not lower:  # The empty face is not a Morse cell.
                continue
            assert lower in faces
            a, z = (lower, upper) if (lower, upper) in pairset else (upper, lower)
            outgoing[a].append(z)
            incoming[z] += 1
            incidence_count += 1
    q = collections.deque(x for x, v in incoming.items() if v == 0)
    seen = 0
    while q:
        x = q.popleft()
        seen += 1
        for y in outgoing[x]:
            incoming[y] -= 1
            if incoming[y] == 0:
                q.append(y)
    assert seen == len(faces), (seen, len(faces))
    assert 2 * len(pairset) + len(remain) == len(faces)
    return {'faces': len(faces), 'pairs': len(pairset),
            'critical_by_dimension': crit, 'hasse_incidences': incidence_count,
            'acyclic': True}


def invert_permutation(A):
    inv = [0] * 8
    for x, y in enumerate(A):
        inv[y] = x
    return inv


def dual(A, l):
    inv = invert_permutation(A)
    return sum(((l & inv[1 << j]).bit_count() % 2) << j for j in range(3))


def gl3_2():
    for a, b, c in itertools.product(POINTS, repeat=3):
        table = tuple((a if i & 1 else 0) ^ (b if i & 2 else 0) ^
                      (c if i & 4 else 0) for i in range(8))
        if len(set(table)) == 8:
            yield table


def edge_action(A, swap):
    return tuple(INDEX[(dual(A, l), A[p])] if swap else INDEX[(A[p], dual(A, l))]
                 for p, l in EDGES)


def permutation_order(perm):
    visited = set()
    ans = 1
    for i in range(len(perm)):
        if i in visited:
            continue
        j, length = i, 0
        while j not in visited:
            visited.add(j)
            length += 1
            j = perm[j]
        ans = lcm(ans, length)
    return ans


def signed_face_trace(faces, perm):
    trace = -1  # subtract H_0 in the reduced Lefschetz number
    for mask in faces:
        indices = [i for i in range(21) if mask >> i & 1]
        destinations = [perm[i] for i in indices]
        if sum(1 << j for j in destinations) != mask:
            continue
        inversions = sum(destinations[i] > destinations[j]
                         for i in range(len(indices)) for j in range(i+1, len(indices)))
        trace += (-1 if ((len(indices) - 1 + inversions) % 2) else 1)
    return trace


def cycle_trace_by_feasibility(perm, valid):
    # Independent alternate calculation: a fixed face is a union of edge
    # permutation cycles. Its contribution to reduced homology trace is
    # negative (-1)^(number of selected cycles), including the empty union.
    seen, cycles = set(), []
    for i in range(21):
        if i in seen:
            continue
        j, m = i, 0
        while j not in seen:
            seen.add(j)
            m |= 1 << j
            j = perm[j]
        cycles.append(m)
    def dfs(k, mask, sign):
        if not valid(mask):
            return 0  # every extension of an invalid face remains invalid
        if k == len(cycles):
            return sign
        return dfs(k+1, mask, sign) + dfs(k+1, mask | cycles[k], -sign)
    return -dfs(0, 0, 1)


def main():
    facets = perfect_matchings()
    perfect = perfect_faces(facets)
    ordinary = all_matching_faces()
    assert len(perfect) == 2201 and len(ordinary) == 3461
    assert perfect < ordinary
    assert cell_histogram(perfect) == {0: 21, 1: 168, 2: 560,
                                       3: 756, 4: 504, 5: 168, 6: 24}
    pm = morse_verify(perfect, PERFECT_PIVOTS, {0: 1, 2: 16})
    om = morse_verify(ordinary, ORDINARY_PIVOTS, {0: 1, 4: 16})
    mat = list(gl3_2())
    assert len(mat) == 168
    group = [(A, swap) for A in mat for swap in (0, 1)]
    assert len(group) == 336
    perms = [edge_action(A, swap) for A, swap in group]
    assert len(set(perms)) == 336 and all(len(set(p)) == 21 for p in perms)

    pf_valid = lambda mask: not mask or any(mask & ~f == 0 for f in facets)
    om_valid = lambda mask: not mask or all(
        not ((mask >> i & 1) and (mask >> j & 1)) or
        (EDGES[i][0] != EDGES[j][0] and EDGES[i][1] != EDGES[j][1])
        for i in range(21) for j in range(i+1, 21))
    assert all(pf_valid(f) for f in perfect)
    assert all(om_valid(f) for f in ordinary)

    summary = collections.Counter()
    for (A, swap), perm in zip(group, perms):
        char_p = signed_face_trace(perfect, perm)
        char_o = signed_face_trace(ordinary, perm)
        assert char_p == cycle_trace_by_feasibility(perm, pf_valid)
        assert char_o == cycle_trace_by_feasibility(perm, om_valid)
        assert char_p == ((-1) if swap else 1) * char_o
        summary[(swap, permutation_order(perm), char_p, char_o)] += 1
    predicted = {
        (0,1,16,16):1, (0,2,0,0):21, (0,3,1,1):56,
        (0,4,0,0):42, (0,7,2,2):48,
        (1,2,-4,4):28, (1,6,-1,1):56, (1,8,0,0):84
    }
    assert dict(summary) == predicted, (summary, predicted)
    assert sum(count * (e[2]) for e, count in summary.items()) == 0
    assert sum(count * (e[3]) for e, count in summary.items()) == 336
    assert sum(count * e[2] for e, count in summary.items() if not e[0]) == 168
    print(json.dumps({
        'perfect_matching_count': len(facets),
        'perfect_matching_complex': pm,
        'ordinary_matching_complex': om,
        'group_order': len(group),
        'characters_by_side_switch_order_perfect_ordinary': [
            {'swaps_bipartition': bool(sw), 'order': o,
             'perfect_H2_trace': tp, 'ordinary_H4_trace': to, 'class_size': count}
            for (sw, o, tp, to), count in sorted(summary.items())],
        'character_relation': 'perfect_H2 = bipartition_sign_tensor_ordinary_H4',
        'invariant_ranks': {'perfect_full':0, 'ordinary_full':1,
                            'perfect_side_preserving':1},
        'all_336_independent_cycle_trace_crosschecks': True
    }, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
