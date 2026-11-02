#!/usr/bin/env python3
"""Exact-rational consistency checks for seasonal Beverton--Holt comparison.

The general parameter theorem is proved algebraically in RESULT.md;
finite rational checks serve as independent regression tests, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import permutations

TESTS = 0

def test(statement):
    global TESTS
    TESTS += 1
    assert statement, 'failed assertion %d' % TESTS


def four_cycle(r, capacities):
    assert len(capacities) == 4 and r > 1 and all(k > 0 for k in capacities)
    gamma = [(r - 1) / k for k in capacities]
    initial = sum(r ** i * gamma[i] for i in range(4)) / (r ** 4 - 1)
    ys = [initial]
    for i in range(3):
        ys.append((ys[-1] + gamma[i]) / r)
    test((ys[-1] + gamma[3]) / r == ys[0])
    xs = [1 / y for y in ys]
    for i in range(4):
        test(xs[(i + 1) % 4] == r * capacities[i] * xs[i] /
             (capacities[i] + (r - 1) * xs[i]))
    return ys, xs


def assert_case(r, low, high):
    g_y, g_x = four_cycle(r, [low, low, high, high])
    a_y, a_x = four_cycle(r, [low, high, low, high])
    test(sum(g_y) == sum(a_y))
    test(sum(g_y) / 4 == (1 / low + 1 / high) / 2)
    test(sum(g_x) > sum(a_x))
    test(min(g_x) < min(a_x))
    test(max(g_x) > max(a_x))
    gs, aas = sorted(g_y, reverse=True), sorted(a_y, reverse=True)
    for m in (1, 2, 3):
        test(sum(gs[:m]) > sum(aas[:m]))
    test(sum(gs) == sum(aas))
    test(sum(y*y for y in g_y) > sum(y*y for y in a_y))
    test(sum(y*y*y for y in g_y) > sum(y*y*y for y in a_y))
    test(sorted(g_y) == sorted(set(g_y)))
    test(len(set(a_y)) == 2)
    for schedule in set(permutations([low,low,high,high])):
        yy, xx = four_cycle(r, schedule)
        class_group = any(schedule == tuple([low, low, high, high][j:] + [low, low, high, high][:j]) for j in range(4))
        if class_group:
            test(sorted(yy) == sorted(g_y))
            test(sorted(xx) == sorted(g_x))
        else:
            test(sorted(yy) == sorted(a_y))
            test(sorted(xx) == sorted(a_x))


def main():
    r_values = [F(101,100), F(11,10), F(6,5), F(4,3), F(3,2), F(2),
                F(5,2), F(3), F(5), F(9)]
    lows = [F(1,7), F(1,4), F(1,3), F(1,2), F(2,3), F(3,4), F(1), F(4,3)]
    factors = [F(101,100), F(6,5), F(3,2), F(2), F(7,3), F(3), F(10), F(100)]
    for r in r_values:
        for low in lows:
            for factor in factors:
                assert_case(r, low, low*factor)
    gy, gx = four_cycle(F(2), [F(1,3), F(1,3), F(1), F(1)])
    ay, ax = four_cycle(F(2), [F(1,3), F(1), F(1,3), F(1)])
    test(sorted(gx, reverse=True) == [F(5,7),F(5,9),F(5,11),F(5,13)])
    test(sorted(ax, reverse=True) == [F(3,5),F(3,5),F(3,7),F(3,7)])
    test(sum(gx)/4 == F(4750,9009))
    test(sum(ax)/4 == F(18,35))
    test(sum(gx)/4 - sum(ax)/4 == F(584,45045))
    print('%d exact-rational assertions passed across %d parameter triples.' %
          (TESTS, len(r_values)*len(lows)*len(factors)))

if __name__ == '__main__':
    main()
