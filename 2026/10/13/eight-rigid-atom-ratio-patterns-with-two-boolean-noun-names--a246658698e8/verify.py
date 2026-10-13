#!/usr/bin/env python3
"""Exact exhaustive check for four-atom cardinality-balance ratios.

The domain is fixed: two Boolean predicate letters, four disjoint atoms,
three independent cardinality equalities between Boolean combinations.
Python 3 standard library only. The two enumerations use different traversals.
"""
from itertools import product, combinations, combinations_with_replacement, permutations
from math import gcd
from functools import reduce
from collections import Counter

ROWS = [r for r in product((-1, 0, 1), repeat=4)
        if any(r) and next(a for a in r if a) > 0]
assert len(ROWS) == 40


def determinant3(matrix):
    (a,b,c),(d,e,f),(g,h,i)=matrix
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def kernel_from_three(rows):
    cofactors = [(-1)**j * determinant3(
        [[row[k] for k in range(4) if k != j] for row in rows])
        for j in range(4)]
    if not any(cofactors):
        return None
    if not (all(x > 0 for x in cofactors) or all(x < 0 for x in cofactors)):
        return None
    divisor = reduce(gcd, cofactors)
    return tuple(abs(x // divisor) for x in cofactors)


def rank_over_q(matrix):
    """Exact rank by Fraction-free elimination over the integers."""
    mat = [list(map(int, row)) for row in matrix]
    if not mat:
        return 0
    nrows, ncols = len(mat), len(mat[0]); rank = 0
    for col in range(ncols):
        pivot = next((r for r in range(rank, nrows) if mat[r][col]), None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        for r in range(rank+1,nrows):
            p, q = mat[rank][col], mat[r][col]
            if not q:
                continue
            mat[r] = [p*x-q*y for x,y in zip(mat[r],mat[rank])]
            common = reduce(gcd, mat[r])
            if common > 1:
                mat[r] = [x//common for x in mat[r]]
        rank += 1
        if rank == nrows:
            break
    return rank


def enumerate_by_minors():
    ratios = set()
    witnessed = {}
    rank_three = 0
    for rs in combinations(ROWS, 3):
        k = kernel_from_three(rs)
        if k is not None:
            rank_three += 1
            ratios.add(k)
            witnessed.setdefault(k, rs)
    return ratios, witnessed, rank_three


def enumerate_by_candidates():
    positive = []
    rank_distribution = Counter()
    for v in combinations_with_replacement(range(1, 6),4):
        if reduce(gcd, v) != 1:
            continue
        equations = [row for row in ROWS if sum(a*b for a,b in zip(row,v)) == 0]
        rank = rank_over_q(equations)
        rank_distribution[rank] += 1
        if rank == 3:
            positive.append(v)
    return positive, rank_distribution


def main():
    direct, witnesses, triples = enumerate_by_minors()
    sorted_reps, rank_hist = enumerate_by_candidates()
    reps_from_direct = sorted({tuple(sorted(v)) for v in direct})
    assert sorted_reps == reps_from_direct, (sorted_reps,reps_from_direct)
    expected = [
        (1,1,1,1), (1,1,1,2), (1,1,1,3), (1,1,2,2),
        (1,1,2,3), (1,1,2,4), (1,2,2,3), (1,2,3,4)]
    assert sorted_reps == expected
    assert len(direct) == 75
    assert rank_hist == {1:8, 2:47, 3:8}
    sizes = Counter(map(sum,direct))
    assert sizes == {4:1, 5:4, 6:10, 7:12, 8:24, 10:24}
    for v in direct:
        assert reduce(gcd, v) == 1 and min(v) >= 1
        rows = witnesses[v]
        assert rank_over_q(rows) == 3
        assert all(sum(a*b for a,b in zip(row,v)) == 0 for row in rows)
    print('Ternary row directions:',len(ROWS))
    print('Checked distinct unordered row triples:',len(list(combinations(ROWS,3))))
    print('Row triples with strictly positive 1-dimensional kernel:',triples)
    print('Primitive sorted candidates bounded by Hadamard:',sum(reduce(gcd,v)==1 for v in combinations_with_replacement(range(1,6),4)))
    print('Rank distribution for sorted candidates:',dict(sorted(rank_hist.items())))
    print('Eight orbit representatives:',sorted_reps)
    print('Realizable ordered atom ratios:',len(direct))
    print('Minimal-model-size distribution:',dict(sorted(sizes.items())))
    print('Maximum minimal-model size:',max(sizes),'(attained by',len([v for v in direct if sum(v)==10]),'ordered ratios)')
    print('9 excluded:', 9 not in sizes)
    print('All assertions passed.')

if __name__ == '__main__':
    main()
