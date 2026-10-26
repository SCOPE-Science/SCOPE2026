#!/usr/bin/env python3
"""Independent matrix-entry verification for the finite interval-translation monoid."""
from math import comb


def elt_maps(n):
    result = [({}, 0)]
    for length in range(1, n+1):
        for start in range(1, n-length+2):
            for target in range(1, n-length+2):
                image = {i: i + target - start for i in range(start, start+length)}
                result.append((image, target-start))
    return result


def product(f, g):
    # Matrix convention: (fg)(i) = g(f(i)), with absent entries interpreted as zero.
    return {i: g[j] for i, j in f.items() if j in g}


def closed(n):
    elements = elt_maps(n)
    m = len(elements)
    expected_m = 1+n*(n+1)*(2*n+1)//6
    assert m == expected_m
    ordered_both_zero = 0
    ordered_nonzero_equal = 0
    category = {'both_idempotent': 0, 'one_idempotent': 0,
                'both_positive': 0, 'both_negative': 0, 'mixed_sign': 0}
    for (x,sx) in elements:
        for (y,sy) in elements:
            xy = product(x,y)
            yx = product(y,x)
            if not x or not y:
                assert xy == yx == {}
                continue
            if not xy and not yx:
                ordered_both_zero += 1
            if xy and xy == yx:
                ordered_nonzero_equal += 1
                if sx == 0 and sy == 0:
                    category['both_idempotent'] += 1
                elif sx == 0 or sy == 0:
                    category['one_idempotent'] += 1
                elif sx > 0 and sy > 0:
                    category['both_positive'] += 1
                elif sx < 0 and sy < 0:
                    category['both_negative'] += 1
                else:
                    category['mixed_sign'] += 1
    e = n*(n+1)//2
    t = n*(n-1)*(n+1)*(n+2)*(n+3)//60
    expected_category = {
        'both_idempotent': e*e-2*comb(n+2,4),
        'one_idempotent':2*t,
        'both_positive':comb(n+1,4),
        'both_negative':comb(n+1,4),
        'mixed_sign':0
    }
    expected_zz = n*(n-1)*(n+1)*(n+2)*(n*n+n-1)//30
    expected_nz = n*(n+1)*(2*n**3+23*n*n-3*n+8)//60
    expected_all = (2*n**6+8*n**5+25*n**4+50*n**3+63*n*n+32*n+60)//60
    assert category == expected_category, (n,category,expected_category)
    assert ordered_both_zero == expected_zz,(n,ordered_both_zero,expected_zz)
    assert ordered_nonzero_equal == expected_nz,(n,ordered_nonzero_equal,expected_nz)
    assert ordered_both_zero + ordered_nonzero_equal + 2*m-1 == expected_all
    return m*m, expected_all


if __name__ == '__main__':
    pair_total = 0
    for n in range(1,13):
        pairs, commuting = closed(n)
        pair_total += pairs
        print(f'n={n} pairs={pairs} commuting={commuting}')
    print('ALL_CONSECUTIVE_DIAGONAL_COMMUTATION_CHECKS_PASSED',12,pair_total)
