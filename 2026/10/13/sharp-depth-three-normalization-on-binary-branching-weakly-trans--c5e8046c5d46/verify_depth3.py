#!/usr/bin/env python3
"""Finite exhaustive certificate for sharp depth-three modal stabilization.

This script uses no third-party packages. Running it proves a finite lemma:
for any two weakly transitive directed graphs with at most three vertices
and outdegree at most two, and any assignment of atomic valuations,
the depth-three and depth-four bisimulation partitions coincide on their
disjoint union. Equality patterns of atomic valuations suffice, because
all logical atoms are compared exclusively for equality of truth vectors.
"""
from collections import Counter
from itertools import permutations


def admissible_labeled(n):
    for bits in range(1 << (n*n)):
        rows = tuple(sum(1 << j for j in range(n) if (bits >> (i*n+j)) & 1)
                     for i in range(n))
        if any(row.bit_count() > 2 for row in rows):
            continue
        # xRy and yRz force xRz or x=z.
        if any(rows[y] & ~(rows[x] | (1 << x))
               for x in range(n) for y in range(n) if (rows[x] >> y) & 1):
            continue
        yield rows


def relabel(rows, permutation):
    n = len(rows)
    # permutation[renamed_vertex] is its old vertex.
    inverse = {old: new for new, old in enumerate(permutation)}
    return tuple(sum(1 << inverse[old_target] for old_target in range(n)
                     if (rows[old_source] >> old_target) & 1)
                 for old_source in permutation)


def canonical_frames(n):
    seen = set()
    perms = tuple(permutations(range(n)))
    for rows in admissible_labeled(n):
        representative = min(relabel(rows, p) for p in perms)
        if representative not in seen:
            seen.add(representative)
            yield representative


def set_partitions(n):
    # Restricted-growth words: 0 <= a_i <= 1+max(a_0,...,a_{i-1}).
    def recurse(prefix, greatest):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            for c in range(greatest + 2):
                yield from recurse(prefix + [c], max(c, greatest))
    if n > 0:
        yield from recurse([0], 0)
    else:
        yield ()


def depth_types(colors, successors, through=4):
    prev = tuple(colors)
    series = [prev]
    for depth in range(1, through + 1):
        signatures = tuple((colors[i], tuple(sorted({prev[j] for j in successors[i]})))
                           for i in range(len(colors)))
        ranks = {signature: index for index, signature in
                 enumerate(sorted(set(signatures)))}
        prev = tuple(ranks[z] for z in signatures)
        series.append(prev)
    return series


def equivalence_is_same(a, b):
    return all((a[i] == a[j]) == (b[i] == b[j])
               for i in range(len(a)) for j in range(i+1, len(a)))


def check_witness():
    # Point a in P: a->b,c; b->c; c has no outgoing edge.
    P = (0b110, 0b100, 0b000)
    # Point a in Q: a->b,c; b->a,c; c has no outgoing edge.
    Q = (0b110, 0b101, 0b000)
    for rows in (P, Q):
        assert rows in set(admissible_labeled(3))
    successors = tuple(tuple(j for j in range(3) if (rows[i] >> j) & 1)
                       for rows in (P,) for i in range(3)) + \
                 tuple(tuple(3+j for j in range(3) if (rows[i] >> j) & 1)
                       for rows in (Q,) for i in range(3))
    types = depth_types((0,)*6, successors, 4)
    assert types[2][0] == types[2][3]
    assert types[3][0] != types[3][3]
    # The length-three reachability distinction is exactly Diamond^3 top.
    def has_path(rows, start, length):
        states = {start}
        for _ in range(length):
            states = {j for i in states for j in range(3) if (rows[i] >> j) & 1}
        return bool(states)
    assert not has_path(P, 0, 3) and has_path(Q, 0, 3)


def main():
    labeled = {n: list(admissible_labeled(n)) for n in range(1,4)}
    assert {n: len(x) for n,x in labeled.items()} == {1:2, 2:16, 3:159}
    canonical = {n: list(canonical_frames(n)) for n in range(1,4)}
    assert {n: len(x) for n,x in canonical.items()} == {1:2, 2:10, 3:37}
    # Verify orbit representatives really cover every labeled graph.
    for n in range(1,4):
        reps = set(canonical[n]); perms=list(permutations(range(n)))
        assert all(min(relabel(rows,p) for p in perms) in reps
                   for rows in labeled[n])
    frames = [(n, rows) for n in range(1,4) for rows in canonical[n]]
    counts = Counter()
    for n, left in frames:
        for m, right in frames:
            N = n+m
            successors = [tuple(j for j in range(n) if left[i] >> j & 1)
                          for i in range(n)]
            successors += [tuple(n+j for j in range(m) if right[i] >> j & 1)
                           for i in range(m)]
            for atom_pattern in set_partitions(N):
                series = depth_types(atom_pattern, successors, through=4)
                counts['cases'] += 1
                for d in range(1,4):
                    if not equivalence_is_same(series[d-1], series[d]):
                        counts[f'refinements_at_{d}'] += 1
                assert equivalence_is_same(series[3], series[4]), (
                    'depth-four distinction found', n, left, m, right, atom_pattern)
    check_witness()
    assert counts == Counter({'cases':320315,
                              'refinements_at_1':291034,
                              'refinements_at_2':27989,
                              'refinements_at_3':68})
    print('PASS: all 320315 paired-frame/atom-partition cases stabilize by depth 3')
    print('Labeled admissible frames: {1: 2, 2: 16, 3: 159}')
    print('Unlabeled representatives: {1: 2, 2: 10, 3: 37}')
    print('Refinements in cases: depth 1 = 291034, depth 2 = 27989, depth 3 = 68')
    print('Sharp witness: depth 2-equivalent but Diamond^3 top separates')

if __name__ == '__main__':
    main()
