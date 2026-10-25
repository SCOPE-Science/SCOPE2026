#!/usr/bin/env python3
"""Exact finite check for a sharp joint-retention protection threshold.

Uses only the Python standard library.  Zero-based bit j denotes resource j.
Each nonzero integer row mask represents the resources supporting one plant.
"""
from collections import defaultdict
from itertools import combinations_with_replacement
import json
from fractions import Fraction

EXPECTED = {
    (2, 2): 3, (3, 2): 6, (2, 3): 10,
    (4, 2): 10, (3, 3): 44, (2, 4): 33,
    (5, 2): 15, (4, 3): 135, (3, 4): 332, (2, 5): 106,
    (6, 2): 21, (5, 3): 336, (4, 4): 1992, (3, 5): 2476, (2, 6): 333,
    (7, 2): 28, (6, 3): 728, (5, 4): 8880, (4, 5): 30166,
    (3, 6): 18136, (2, 7): 1030,
}

def is_connected(rows, r):
    m = len(rows)
    # BFS on the two vertex classes, starting with plant 0.
    seen_p = {0}
    seen_q = set()
    changed = True
    while changed:
        changed = False
        for a in tuple(seen_p):
            for j in range(r):
                if rows[a] & (1 << j) and j not in seen_q:
                    seen_q.add(j)
                    changed = True
        for i, row in enumerate(rows):
            if i not in seen_p and any(row & (1 << j) for j in seen_q):
                seen_p.add(i)
                changed = True
    return len(seen_p) == m and len(seen_q) == r

def success_coefficients(rows, r):
    # Number of successful k-survivor subsets among the r-1 unprotected species.
    result = []
    for protected in range(r):
        values = [0] * r
        for other in range(1 << r):
            if other & (1 << protected):
                continue
            surviving = other | (1 << protected)
            if all(row & surviving for row in rows):
                values[other.bit_count()] += 1
        result.append(values)
    return result

def universal_coefficient_dominator(coeff):
    r = len(coeff)
    return [i for i in range(r) if all(
        all(coeff[i][k] >= coeff[j][k] for k in range(r))
        for j in range(r))]

def value(c, p):
    q = 1-p
    return sum(Fraction(v)*p**k*q**(len(c)-1-k) for k,v in enumerate(c))


def main():
    rows_count = {}
    for total in range(4, 10):
        for r in range(2, total-1):
            m = total-r
            count=0
            for rows in combinations_with_replacement(range(1, 1 << r), m):
                if not is_connected(rows, r):
                    continue
                count += 1
                c = success_coefficients(rows, r)
                if not universal_coefficient_dominator(c):
                    raise AssertionError(('missing coefficientwise universal choice',m,r,rows,c))
            assert count == EXPECTED[m,r], (m,r,count)
            rows_count[f'{m}x{r}'] = count
    # The cases with one plant or one resource have identical choices or only
    # one choice; their proof is structural and does not use enumeration.
    example = (3,5,14,22,26)
    assert is_connected(example, 5)
    coeff = success_coefficients(example,5)
    assert coeff == [
        [0,1,6,4,1],
        [0,2,5,4,1],
        [0,1,5,4,1],
        [0,0,4,4,1],
        [0,0,4,4,1]
    ],coeff
    for p, expected_winners in [
        (Fraction(1,4),[1]), (Fraction(1,2),[0,1]),
        (Fraction(3,4),[0])
    ]:
        scores=[value(c,p) for c in coeff]
        assert [i for i,x in enumerate(scores) if x==max(scores)]==expected_winners
        # Independently: direct summation over full survival states, with
        # all plant support conditions tested on each original row.
        for i in range(5):
            direct = Fraction(0)
            for bitset in range(1<<5):
                if bitset & (1<<i):continue
                mask=bitset|(1<<i)
                if all(mask & row for row in example):
                    k=bitset.bit_count()
                    direct += p**k*(1-p)**(4-k)
            assert direct == scores[i]
    # Algebraic identity checked at the coefficient level:
    # coeff[1]-coeff[0] = (0,1,-1,0,0), hence
    # R_B - R_A = p(1-p)^2(1-2p).
    assert [a-b for a,b in zip(coeff[1],coeff[0])] == [0,1,-1,0,0]
    assert all(a>=b for a,b in zip(coeff[0],coeff[2]))
    assert all(a>=b for a,b in zip(coeff[0],coeff[3]))
    assert all(a>=b for a,b in zip(coeff[0],coeff[4]))
    print(json.dumps({
        'statement':'Every connected bipartite graph with at most nine total vertices has a coefficientwise universally optimal protected resource. A ten-vertex network has a strict parameter-dependent switch.',
        'enumerated_connected_row_multisets_by_plant_resource_counts':rows_count,
        'enumerated_connected_cases_total':sum(rows_count.values()),
        'no_coefficientwise_dominator_through_nine':0,
        'example_plant_resource_masks':list(example),
        'example_coefficients_resource_0_to_4':coeff,
        'exact_difference_R1_minus_R0':'p*(1-p)^2*(1-2*p)',
        'exact_switch':'p=1/2',
        'spot_checks':{'p=1/4':'resource 1','p=1/2':'resources 0 and 1','p=3/4':'resource 0'},
        'direct_survival_enumeration':'all 5 targets at each of 3 rational p values matched exactly'
    },sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
