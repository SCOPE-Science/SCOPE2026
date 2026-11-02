#!/usr/bin/env python3
"""Exact finite support-cohort certificate for four-color cyclic contact dynamics on complete split graphs.

No external packages. A cohort represents all vertices in one of the four initially
occupied colors within either vertex class. Identical initial class/color means
identical neighbors of every successor color, hence identical future states.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb

K = 4
SUBSETS = tuple(mask for mask in range(1, 1 << K))
EXPECTED = {
    (0, 1): ((8, 4, 0, 0), (4, 2, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
    (0, 4): ((0, 0, 0, 0), (0, 2, 0, 0), (4, 8, 4, 0), (4, 6, 4, 1)),
    (1, 1): ((8, 8, 4, 0), (8, 4, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
    (1, 4): ((0, 0, 0, 0), (0, 0, 4, 2), (0, 4, 8, 4), (0, 0, 0, 0)),
    (2, 1): ((0, 8, 4, 0), (12, 20, 8, 0), (12, 12, 4, 0), (0, 0, 0, 0)),
    (3, 1): ((0, 4, 8, 4), (0, 8, 12, 4), (0, 0, 0, 0), (0, 0, 0, 0)),
}

def state_for_masks(cmask, imask):
    return (tuple(k if (cmask >> k) & 1 else -1 for k in range(K)),
            tuple(k if (imask >> k) & 1 else -1 for k in range(K)))

def cohort_update(state):
    c, i = state
    present_c = {x for x in c if x >= 0}
    present_i = {x for x in i if x >= 0}
    c1 = tuple((x + 1) % K if x >= 0 and ((x + 1) % K in present_c or
                                                  (x + 1) % K in present_i) else x for x in c)
    i1 = tuple((x + 1) % K if x >= 0 and (x + 1) % K in present_c else x for x in i)
    return c1, i1

def first_entry(cmask, imask):
    s = state_for_masks(cmask, imask)
    seen = {}
    for t in range(32):
        if s in seen:
            return seen[s], t - seen[s]
        seen[s] = t
        s = cohort_update(s)
    raise AssertionError('unclosed orbit')

def surjections(j, n):
    return sum((-1)**(j-r)*comb(j, r)*r**n for r in range(j+1))

def fourcycle_criterion(c, i):
    count = c.bit_count()
    if count == 4:
        return True
    if count == 3:
        return (i & (~c & 15)) != 0
    if count == 2 and c in (0b0101, 0b1010):
        return (i & (~c & 15)) == (~c & 15)
    return False

def predicted_fourcycle_basin(m, n):
    w2 = surjections(2, m)
    w3 = surjections(3, m)
    w4 = surjections(4, m)
    return (w4*4**n + 4*w3*(4**n-3**n)
            + 2*w2*(4**n-2*3**n+2**n))

def predicted_third_layer(m, n):
    return (4*(4**n-2*3**n+2**n)
            + 4*(2**m-2)*(4**n-3**n-2**n+1))

def six_closed_formulas(m, n):
    w2 = surjections(2, m)
    w3 = surjections(3, m)
    w4 = surjections(4, m)
    return {
        (0, 1): 2**(m+n+1),
        (1, 1): 4*(2**(m+n)-3*2**n+3**n+1),
        (2, 1): 4*((3**m-2**m)*3**n-(2**m-1)*(2**n+1)),
        (3, 1): 4*(4**n-2*3**n+2**n)+4*(2**m-2)*(4**n-3**n-2**n+1),
        (0, 4): w4*4**n+4*w3*(3**n-2**n)+2*w2*(2**n-2),
        (1, 4): 4*w3*(4**n-2*3**n+2**n)+2*w2*(4**n-2*3**n+2),
    }

def main():
    observed = defaultdict(lambda: [[0]*4 for _ in range(4)])
    classes = {}
    for c, i in product(SUBSETS, repeat=2):
        t, p = first_entry(c, i)
        assert p == (4 if fourcycle_criterion(c, i) else 1), (c,i,t,p)
        assert t <= 3
        observed[(t, p)][c.bit_count()-1][i.bit_count()-1] += 1
        classes[c,i] = (t,p)
    normalized = {key: tuple(tuple(row) for row in val) for key, val in observed.items()}
    assert normalized == EXPECTED, (normalized, EXPECTED)
    assert len(classes) == 225
    for m, n in product(range(1, 13), repeat=2):
        by_layer = Counter()
        for (c,i), (t,p) in classes.items():
            by_layer[t,p] += surjections(c.bit_count(),m)*surjections(i.bit_count(),n)
        assert sum(by_layer.values()) == 4**(m+n)
        assert all(by_layer[key] == value for key, value in six_closed_formulas(m,n).items())
        assert by_layer[3,1] == predicted_third_layer(m,n)
        assert by_layer[0,4] + by_layer[1,4] == predicted_fourcycle_basin(m,n)
        assert by_layer[0,1] == 2**(m+n+1)
    print('225/225 support pairs verified, cohort dynamics, period criterion, and full 6-layer coefficient table.')
    print('144 parameter pairs checked for all six closed-form layers and the exact all-size surjection identities.')
    print('Maximum first-entry time: 3; only least periods: 1 and 4.')
    print('Four-cycle support criterion: complete clique palette, missing-color exposure for three colors, or complementary pair exposure for antipodal two-color cliques.')
    for key in sorted(EXPECTED):
        print('first entry, least period:',key, 'support matrix:', EXPECTED[key])

if __name__ == '__main__':
    main()
