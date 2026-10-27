#!/usr/bin/env python3
"""Exact finite-state checks for the three-cell Poisson stopping-set example.

The analytic obstruction to exploration is proved in RESULT.md; enumerations
here check only the finite decision table and its stopping-set implication.
"""
from itertools import product

# Indices are 0,1,2 for the three disjoint intervals.
TABLE = {
    (0, 0, 0): (1, 2),
    (0, 0, 1): (0, 1, 2),
    (0, 1, 0): (0, 1),
    (0, 1, 1): (0, 1),
    (1, 0, 0): (1, 2),
    (1, 0, 1): (0, 2),
    (1, 1, 0): (0, 1, 2),
    (1, 1, 1): (0, 2),
}


def test_binary_cylinders():
    outcomes = list(product((0, 1), repeat=3))
    assert set(TABLE) == set(outcomes)
    for bits in outcomes:
        chosen = TABLE[bits]
        assert len(chosen) == len(set(chosen))
        assert sum(bits[i] for i in chosen) <= 2
        for other in outcomes:
            # This is precisely the stability condition behind stopping.
            if all(other[i] == bits[i] for i in chosen):
                assert TABLE[other] == chosen
    for i in range(3):
        assert any(i not in TABLE[bits] for bits in outcomes)
    assert TABLE[(0, 0, 0)] == (1, 2)
    assert TABLE[(1, 0, 1)] == (0, 2)
    assert TABLE[(0, 1, 0)] == (0, 1)


def first_hit_prefix(points, a, b):
    inside = tuple(sorted(x for x in points if a <= x <= b))
    return (a, inside[0] if inside else b)


def test_configuration_stability():
    # This is a finite family of point measures, not an infinite proof.
    sites = [(.2, .4), (2.2, 2.4), (4.2, 4.4)]
    options = [(), (0,), (1,), (0, 1)]
    for choice in product(options, repeat=3):
        points = [tuple(sites[i][j] for j in choice[i]) for i in range(3)]
        bits = tuple(int(bool(p)) for p in points)
        chosen = TABLE[bits]
        for i in chosen:
            # The prefix includes its first point, when there is one.
            seg = first_hit_prefix(points[i], 2*i, 2*i+1)
            assert sum(seg[0] <= x <= seg[1] for x in points[i]) <= 1
        assert sum(bits[i] for i in chosen) <= 2
        for alt in product(options, repeat=3):
            other = [tuple(sites[i][j] for j in alt[i]) for i in range(3)]
            if all(first_hit_prefix(other[i],2*i,2*i+1) == first_hit_prefix(points[i],2*i,2*i+1)
                   and tuple(x for x in other[i] if 2*i <= x <= first_hit_prefix(points[i],2*i,2*i+1)[1])
                       == tuple(x for x in points[i] if 2*i <= x <= first_hit_prefix(points[i],2*i,2*i+1)[1])
                   for i in chosen):
                other_bits = tuple(int(bool(p)) for p in other)
                assert TABLE[other_bits] == chosen


def test_first_exploration_obstructions():
    # If the deterministic initial region U hits cell 2 or cell 3, the
    # named positive-probability occupancy patterns omit that cell.
    assert 1 not in TABLE[(1, 0, 1)]
    assert 2 not in TABLE[(0, 1, 0)]
    assert set(TABLE[(0, 0, 0)]) == {1, 2}


if __name__ == '__main__':
    test_binary_cylinders()
    test_configuration_stability()
    test_first_exploration_obstructions()
    print('PASS: 8 outcome cylinders; 64 simple point-configurations and their finite comparisons; first-exploration exclusions.')
    print('Analytic CTDT obstruction and the continuum model require the written proof.')
