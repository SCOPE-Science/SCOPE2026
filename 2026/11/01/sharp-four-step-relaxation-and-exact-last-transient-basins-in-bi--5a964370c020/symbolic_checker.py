#!/usr/bin/env python3
"""Exact finite order-type proof for a bipartite bi-threshold network.

All comparisons depend only on the ordering of 0,a,i,a-i,b,j,b-j
and on two threshold cut positions. There are 80 linearisations.
No finite graph-size cutoff is used.
"""
from itertools import permutations

# 0=zero, 1=a, 2=i, 3=a-i, 4=b, 5=j, 6=b-j
COMPLEMENT_A = {0: 1, 1: 0, 2: 3, 3: 2}
COMPLEMENT_B = {0: 4, 4: 0, 5: 6, 6: 5}


def iterate(up, down):
    a, b = 2, 5  # Initial count symbols i and j
    history = [(a, b)]
    for _ in range(6):
        ua, da = up[b], down[b]
        ub, db = up[a], down[a]
        # h(v,s) = (1-v) 1{s>=u} + v 1{s>=d-1}
        next_a = 0 if not ua and not da else 1 if ua and da else a if not ua else COMPLEMENT_A[a]
        next_b = 0 if not ub and not db else 4 if ub and db else b if not ub else COMPLEMENT_B[b]
        a, b = next_a, next_b
        history.append((a, b))
    return history


def main():
    orders = 0
    cases = 0
    exceptions = 0
    types = {'A_larger': 0, 'B_larger': 0}
    for tail in permutations((1, 2, 3, 4, 5, 6)):
        # All admissible numerical orders have a>i,a-i and b>j,b-j,
        # with equalities resolved in favor of this ordering.
        if not (tail.index(1) > tail.index(2) and tail.index(1) > tail.index(3)
                and tail.index(4) > tail.index(5) and tail.index(4) > tail.index(6)):
            continue
        orders += 1
        ordered = (0,) + tail
        position = {symbol: r for r, symbol in enumerate(ordered)}
        for up_cut in range(1, 8):   # u>=1 means 0 < u
            for down_cut in range(8):  # d-1>=0, so down_cut can be 0
                cases += 1
                up = tuple(position[k] >= up_cut for k in range(7))
                down = tuple(position[k] >= down_cut for k in range(7))
                history = iterate(up, down)
                assert history[6] == history[4], (ordered, up_cut, down_cut, history)
                condition = all(up[k] for k in (2, 3, 5, 6)) and (
                    (not down[4] and not down[2] and down[3]) or
                    (not down[1] and not down[5] and down[6]))
                actual = history[5] != history[3]
                assert actual == condition, (ordered, up_cut, down_cut, history)
                if actual:
                    exceptions += 1
                    assert up_cut == 1 and down_cut == 5
                    if down[3]:
                        types['A_larger'] += 1
                        assert position[3] > position[4]
                    else:
                        types['B_larger'] += 1
                        assert position[6] > position[1]
    assert orders == 80 and cases == 4480 and exceptions == 16
    assert types == {'A_larger': 8, 'B_larger': 8}
    print('PASS order types:', orders)
    print('PASS threshold-cut cases:', cases)
    print('PASS global identity: F^6=F^4 (all cases)')
    print('PASS exact T=4 criterion (all cases)')
    print('Exceptional symbolic order/cut cases:', exceptions, types)


if __name__ == '__main__':
    main()
