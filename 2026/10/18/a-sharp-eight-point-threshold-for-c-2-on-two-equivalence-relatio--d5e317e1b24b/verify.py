#!/usr/bin/env python3
"""Exact finite census for two named equivalence relations.

No non-standard packages are required. Run: python3 verify.py
A structure is encoded by the nonnegative matrix of intersections of
its two equivalence-class partitions; its elements are the matrix units.
"""
from collections import Counter, defaultdict
from itertools import permutations, product
from hashlib import sha256

EXPECTED_COUNTS = {1: 1, 2: 4, 3: 10, 4: 33, 5: 91,
                   6: 298, 7: 910, 8: 3017}
EXPECTED_COLOR_CLASSES = {1: 1, 2: 4, 3: 10, 4: 33,
                          5: 91, 6: 298, 7: 910, 8: 3016}


def canonical(rows):
    """A unique canonical matrix under independent row/column permutations.

    Fix ascending column-sum order, then consider all permutations within
    equal-sum groups and sort the rows. This is a canonical orbit selector,
    not necessarily the absolute lexicographic minimum over all column orders.
    """
    nr, nc = len(rows), len(rows[0])
    groups = defaultdict(list)
    for j in range(nc):
        groups[sum(rows[i][j] for i in range(nr))].append(j)
    group_perms = [permutations(groups[k]) for k in sorted(groups)]
    best = None
    for block_tuple in product(*group_perms):
        col_perm = tuple(j for block in block_tuple for j in block)
        trial = tuple(sorted(tuple(row[j] for j in col_perm) for row in rows))
        if best is None or trial < best:
            best = trial
    return best


def one_point_extensions(matrix):
    """All outcomes of adjoining a point to one E-class and one F-class.

    Either class can be new; every finite two-equivalence structure admits
    such a deletion, so the recursion loses no isomorphism types.
    """
    nr, nc = len(matrix), len(matrix[0])
    for i in range(nr):
        for j in range(nc):
            a = [list(row) for row in matrix]
            a[i][j] += 1
            yield a
    for i in range(nr):
        a = [list(row) + [0] for row in matrix]
        a[i][nc] = 1
        yield a
    for j in range(nc):
        a = [list(row) for row in matrix] + [[0] * nc]
        a[nr][j] = 1
        yield a
    yield [list(row) + [0] for row in matrix] + [[0] * nc + [1]]


def elements(matrix):
    return tuple((i, j)
                 for i, row in enumerate(matrix)
                 for j, multiplicity in enumerate(row)
                 for _ in range(multiplicity))


def jointly_refined_signatures(matrices):
    """Synchronous color refinement on the disjoint union of the structures.

    Every vertex of a structure denotes one element. Edges have the four
    (E(x,y),F(x,y)) binary relation colors. Color names are assigned
    globally, not independently inside the compared structures.
    """
    point_lists = [elements(m) for m in matrices]
    colors = [[0] * len(p) for p in point_lists]
    for round_number in range(24):
        patterns = []
        for pts, cs in zip(point_lists, colors):
            for u, (i, j) in enumerate(pts):
                relation_counts = Counter(
                    (int(i == p), int(j == q), cs[v])
                    for v, (p, q) in enumerate(pts))
                patterns.append((cs[u], tuple(sorted(relation_counts.items()))))
        palette = {p: k for k, p in enumerate(sorted(set(patterns)))}
        new_flat = [palette[p] for p in patterns]
        new_colors, offset = [], 0
        for pts in point_lists:
            new_colors.append(new_flat[offset:offset + len(pts)])
            offset += len(pts)
        if new_colors == colors:
            break
        colors = new_colors
    else:
        raise AssertionError('Refinement failed to stabilize')
    return [tuple(sorted(Counter(cs).items())) for cs in colors]


def assert_partition_crosscheck():
    """Independent labelled set-partition enumeration at orders <=5."""
    def partitions(n):
        if n == 1:
            yield ((0,),)
            return
        for blocks in partitions(n-1):
            for j in range(len(blocks)):
                a = [tuple(b) for b in blocks]
                a[j] = a[j] + (n-1,)
                yield tuple(a)
            yield blocks + ((n-1,),)
    for n in range(1, 6):
        p = tuple(partitions(n))
        candidates = set()
        for e in p:
            row_for = {x: i for i, row in enumerate(e) for x in row}
            for f in p:
                col_for = {x: j for j, col in enumerate(f) for x in col}
                a = [[0] * len(f) for _ in e]
                for x in range(n):
                    a[row_for[x]][col_for[x]] += 1
                candidates.add(canonical(a))
        assert len(candidates) == EXPECTED_COUNTS[n], (n, len(candidates))


def run():
    assert_partition_crosscheck()
    classes = {((1,),)}
    for n in range(1, 9):
        if n > 1:
            classes = {canonical(a) for m in classes for a in one_point_extensions(m)}
        matrices = sorted(classes)
        assert len(matrices) == EXPECTED_COUNTS[n], (n, len(matrices))
        signatures = jointly_refined_signatures(matrices)
        groups = defaultdict(list)
        for matrix, sig in zip(matrices, signatures):
            groups[sig].append(matrix)
        assert len(groups) == EXPECTED_COLOR_CLASSES[n], (n, len(groups))
        ambiguous = sorted((sorted(v) for v in groups.values() if len(v) > 1),
                           key=str)
        if n < 8:
            assert not ambiguous, (n, ambiguous)
        else:
            assert len(ambiguous) == 1 and len(ambiguous[0]) == 2
            a, b = ambiguous[0]
            expected = [
              ((0, 0, 1, 1), (0, 0, 1, 1),
               (1, 1, 0, 0), (1, 1, 0, 0)),
              ((0, 0, 1, 1), (0, 1, 0, 1),
               (1, 0, 1, 0), (1, 1, 0, 0))]
            assert ambiguous[0] == expected, ambiguous
            assert all(sum(row) == 2 for matrix in (a, b) for row in matrix)
            assert all(sum(row[j] for row in matrix) == 2
                       for matrix in (a, b) for j in range(4))
            assert sum(x for row in a for x in row) == 8
            print('UNIQUE_FIRST_PAIR', a, b)
        print('order', n, 'isomorphism_types', len(matrices),
              'C2_types', len(groups), 'ambiguities', len(ambiguous))
    print('VERIFIED: full sharp C2 threshold and unique first pair')


if __name__ == '__main__':
    run()
