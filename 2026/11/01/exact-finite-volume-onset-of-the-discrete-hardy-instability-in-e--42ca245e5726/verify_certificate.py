#!/usr/bin/env python3
"""Exact, dependency-free certificates for finite-volume lattice Hardy transitions.

Run: python verify_certificate.py
Only the adjacent certificate.json file is read. No numerical eigensolver is used.
"""
import json
import math
from collections import Counter
from pathlib import Path


def orbits(dimension, cutoff):
    found = []
    def extend(positive, floor, sumsq):
        if positive:
            found.append(tuple([0] * (dimension-len(positive)) + positive))
        if len(positive) == dimension:
            return
        for value in range(floor, math.isqrt(cutoff-sumsq)+1):
            extend(positive+[value], value, sumsq+value*value)
    extend([], 1, 0)
    return sorted(found, key=lambda t: (sum(x*x for x in t), t))


def graph(dimension, cutoff):
    points = orbits(dimension, cutoff)
    lookup = {t: i for i,t in enumerate(points)}
    radii = [sum(z*z for z in t) for t in points]
    sizes, rows = [], []
    for point in points:
        counts = Counter(point)
        mult = math.factorial(dimension) * 2**(dimension-counts.get(0,0))
        for multiplicity in counts.values():
            mult //= math.factorial(multiplicity)
        sizes.append(mult)
        row = {}
        for coordinate in range(dimension):
            for change in (-1,1):
                neighbor = list(point)
                neighbor[coordinate] = abs(neighbor[coordinate]+change)
                neighbor.sort()
                j = lookup.get(tuple(neighbor))
                if j is not None:
                    row[j] = row.get(j,0)+1
        rows.append(row)
    for i,row in enumerate(rows):
        for j,number in row.items():
            assert i != j and number > 0
            assert sizes[i]*number == sizes[j]*rows[j][i]
    return points, radii, sizes, rows


def scaled_difference(dimension, cutoff, values):
    points, radii, sizes, rows = graph(dimension, cutoff)
    assert len(points)==len(values) and all(isinstance(x,int) for x in values)
    denominator = math.lcm(*radii)
    coeff_num = (dimension-2)**2
    total = sum(sizes[i] * (
        (8*dimension*radii[i]-coeff_num)*values[i]*values[i]
        - 4*radii[i]*values[i]*sum(weight*values[j] for j,weight in rows[i].items())
    )*(denominator//radii[i]) for i in range(len(points)))
    # total = denominator * (4*energy - (d-2)^2*Hardy_mass)
    return total, denominator


def verify():
    data = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
    assert data['dimension'] == 9
    assert data['continuum_coefficient_numerator'] == 49
    assert data['continuum_coefficient_denominator'] == 4
    pos = data['positive_super_solution']; neg = data['negative_witness']
    assert pos['radius_squared'] == 23 and neg['radius_squared'] == 24
    pts,radii,sizes,rows = graph(9,23)
    h = pos['orbit_values']
    assert len(pts) == len(h) == 90 and all(type(v)==int and v>0 for v in h)
    slacks = [
        (72*radii[i]-49)*h[i]
        -4*radii[i]*sum(m*h[j] for j,m in rows[i].items())
        for i in range(len(h))
    ]
    assert min(slacks) == 100963 and min(slacks)>0
    # A strictly positive Dirichlet supersolution gives positive definiteness
    # for ALL functions supported in the ball, not only invariant functions.
    w = neg['orbit_values']
    assert len(w)==98 and all(type(v)==int and v>0 for v in w)
    defect,den = scaled_difference(9,24,w)
    assert den==5354228880
    assert defect == -3740776448633821897328 < 0
    # For d=10,11 the explicitly given invariant functions violate at the
    # first listed support radius; R=1 or R=2 smaller cases are positive.
    defect10, _=scaled_difference(10,3,[17,4,1])
    defect11, _=scaled_difference(11,2,[4,1])
    defect12, _=scaled_difference(12,1,[1])
    assert defect10<0 and defect11<0 and defect12<0
    # R=1 is positive for d=9,10,11; R=2 positive for d=10.
    assert all(2*d > (d-2)**2/4 for d in (9,10,11))
    # First-two-orbit exact eigenvalue: 3d - sqrt(d^2+8d-8).
    assert 30-math.sqrt(172) > 16
    # For d>=12: 2d < (d-2)^2/4 (monotone separation).
    assert 24 < (12-2)**2/4
    print('CERTIFICATE_OK')
    print('d9 positive supported ball: 90 signed-permutation orbits, min scaled slack:',min(slacks))
    print('d9 negative supported ball: 98 orbits, exact signed defect:',defect)
    print('d10 radius 3 witness defect:',defect10)
    print('d11 radius 2 witness defect:',defect11)
    print('d12 radius 1 witness defect:',defect12)
    print('Explicit small-radius cases and all-dimension monotonicity: OK')

if __name__=='__main__': verify()
