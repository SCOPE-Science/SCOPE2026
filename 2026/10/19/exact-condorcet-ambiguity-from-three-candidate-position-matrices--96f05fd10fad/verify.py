"""Exact finite checks for three-alternative position matrices.

All statements for arbitrary electorates are proved algebraically in RESULT.md.
The checks below enumerate small electorates and are not substitutes for that proof.
"""
from itertools import product
from math import factorial

VOTES = ('ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA')


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for x in range(n + 1):
            for tail in compositions(n - x, k - 1):
                yield (x,) + tail


def position_matrix(counts):
    return tuple(tuple(sum(q for q, vote in zip(counts, VOTES) if vote[p] == c)
                       for p in range(3)) for c in 'ABC')


def winner(counts):
    n = sum(counts)
    eligible = []
    for c in 'ABC':
        if all(2 * sum(q for q, vote in zip(counts, VOTES)
                       if vote.index(c) < vote.index(d)) > n
               for d in 'ABC' if d != c):
            eligible.append(c)
    assert len(eligible) <= 1
    return eligible[0] if eligible else None


def fiber(matrix):
    fa, ma, la = matrix[0]
    fb, mb, lb = matrix[1]
    fc, mc, lc = matrix[2]
    n = sum(matrix[0])
    assert all(sum(matrix[i][j] for i in range(3)) == n for j in range(3))
    lower = max(0, lc - fb, fa - lb)
    upper = min(fa, mb, lc)
    result = []
    for t in range(lower, upper + 1):
        counts = (t, fa - t, lc - t, fb - lc + t, lb - fa + t, mb - t)
        assert all(x >= 0 for x in counts)
        assert position_matrix(counts) == matrix
        awin = (2 * (lb + t) > n and 2 * (fa + lc - t) > n)
        bwin = (2 * (lb + t) < n and 2 * (fb + t) > n)
        cwin = (2 * (fa + lc - t) < n and 2 * (fb + t) < n)
        expected = 'A' if awin else 'B' if bwin else 'C' if cwin else None
        assert winner(counts) == expected
        result.append((counts, expected))
    return result


def label_multiplicity(counts):
    n = sum(counts)
    product_factorial = 1
    for x in counts:
        product_factorial *= factorial(x)
    return factorial(n) // product_factorial


def run():
    matrices = 0
    comparisons = 0
    for n in range(1, 11):
        seen = {}
        for counts in compositions(n, 6):
            matrix = position_matrix(counts)
            seen.setdefault(matrix, []).append((counts, winner(counts)))
        ambiguous = []
        for matrix, truth in seen.items():
            computed = fiber(matrix)
            assert set(computed) == set(truth), (matrix, computed, truth)
            # The exact-rank fiber weight is strictly log-concave if >=3 points.
            weights = [label_multiplicity(x) for x, _ in computed]
            for j in range(1, len(weights) - 1):
                assert weights[j] ** 2 > weights[j - 1] * weights[j + 1]
            possible_winners = {w for _, w in truth if w is not None}
            assert len(possible_winners) <= 2
            if len(possible_winners) == 2:
                ambiguous.append((matrix, truth, weights))
            comparisons += len(truth)
        if n <= 4:
            assert len(ambiguous) == 0
            for vals in seen.values():
                if len(vals) >= 2:
                    assert all(w is None for _, w in vals)
        if n == 5:
            assert len(ambiguous) == 3
            wanted = ((2, 2, 1), (2, 2, 1), (1, 1, 3))
            for matrix, truth, weights in ambiguous:
                assert sorted(matrix) == sorted(wanted)
                assert weights == [60, 60] or weights == [60, 60][::-1]
                assert len(truth) == 2
        if n == 10:
            assert len(ambiguous) == 3
            wanted_even = ((4, 4, 2), (4, 4, 2), (2, 2, 6))
            for matrix, truth, weights in ambiguous:
                assert sorted(matrix) == sorted(wanted_even)
                assert len(truth) == 3
                assert weights == [18900, 100800, 18900] or weights == [18900, 100800, 18900][::-1]
                assert len({w for _, w in truth if w is not None}) == 2
                assert sum(w is None for _, w in truth) == 1
        matrices += len(seen)
        print(f'n={n}: {len(seen)} distinct matrices; {len(ambiguous)} with two possible Condorcet winners')
    print(f'PASS: {matrices} distinct matrices, {comparisons} anonymous electorates verified; odd first ambiguity n=5, even first ambiguity n=10, three candidate-labeled matrices in each first layer.')


if __name__ == '__main__':
    run()
