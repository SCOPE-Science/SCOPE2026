#!/usr/bin/env python3
"""Exact rational arrangement certificate for a four-bit skew-torus process.

Only Python's standard library is used.  All quantities are rational.  The
line-arrangement enumeration proves that the area sum is quadratic between the
reported exceptional parameters, so checking three values per interval is
an infinite-parameter symbolic proof, not an inference from sampled floats.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import comb

BINOMIAL = (0, 0, 1, 3)


def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1],
            u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])


def dot(u, v):
    return sum(x*y for x, y in zip(u, v))


def exceptional_parameters():
    # Each threshold line is j*x+y+binom(j,2)*a = k/2.
    # Include both edges of the square and all relevant level lines.
    lines = [((1, 0, 0), Q(0)), ((1, 0, 0), Q(1)),
             ((0, 1, 0), Q(0)), ((0, 1, 0), Q(1))]
    for j, max_k in enumerate((2, 4, 7, 10)):
        lines += [((j, 1, BINOMIAL[j]), Q(k, 2))
                  for k in range(max_k + 1)]
    assert len(lines) == 31
    critical = {Q(0), Q(1, 4)}
    interior_count = 0
    for L1, L2, L3 in combinations(lines, 3):
        u, v, w = (L1[0], L2[0], L3[0])
        rhs = (L1[1], L2[1], L3[1])
        det = dot(u, cross(v, w))
        if det == 0:
            continue
        x = dot(rhs, cross(v, w)) / det
        y = dot(u, cross(rhs, w)) / det
        a = dot(u, cross(v, rhs)) / det
        if Q(0) < a < Q(1, 4) and Q(0) <= x <= Q(1) and Q(0) <= y <= Q(1):
            critical.add(a)
            interior_count += 1
    assert critical == {Q(0), Q(1, 6), Q(1, 4)}, sorted(critical)
    return len(lines), interior_count


def clip_polygon(poly, a, b, c):
    # Intersect the current convex polygon with a*x+b*y<=c.
    if not poly:
        return []
    result = []
    old = poly[-1]
    old_val = a*old[0] + b*old[1] - c
    for new in poly:
        new_val = a*new[0] + b*new[1] - c
        if (old_val < 0 < new_val) or (new_val < 0 < old_val):
            point = (old[0] + old_val*(new[0]-old[0])/(old_val-new_val),
                     old[1] + old_val*(new[1]-old[1])/(old_val-new_val))
            result.append(point)
        if new_val <= 0:
            result.append(new)
        old, old_val = new, new_val
    return result


def polygon_area(poly):
    if len(poly) < 3:
        return Q(0)
    total = sum(p[0]*q[1]-p[1]*q[0]
                for p,q in zip(poly, poly[1:] + poly[:1]))
    return abs(total)/2


def correlation_exact(a):
    a = Q(a)
    assert 0 <= a <= Q(1,4)
    signed_area = Q(0)
    covered_area = Q(0)
    n_positive = 0
    square = [(Q(0),Q(0)), (Q(1),Q(0)), (Q(1),Q(1)), (Q(0),Q(1))]
    for ks in product(range(2), range(4), range(7), range(10)):
        poly = square
        for j,k in enumerate(ks):
            poly = clip_polygon(poly, Q(j), Q(1), Q(k+1,2)-BINOMIAL[j]*a)
            poly = clip_polygon(poly, Q(-j), Q(-1), BINOMIAL[j]*a-Q(k,2))
            if not poly:
                break
        piece = polygon_area(poly)
        if piece:
            n_positive += 1
            covered_area += piece
            signed_area += (-piece if sum(ks)%2 else piece)
    assert covered_area == 1, covered_area
    return signed_area, n_positive


def formula(a):
    a = Q(a)
    return Q(1,3)-16*a*a if a <= Q(1,6) else -Q(1,3)+32*(Q(1,4)-a)**2


def main():
    n_lines, n_concurrences = exceptional_parameters()
    # Three evaluations per polynomial piece certify the quadratic identities.
    left = (Q(0),Q(1,12),Q(1,6))
    right = (Q(1,6),Q(5,24),Q(1,4))
    certified_values = {}
    for a in set(left+right):
        v, positive = correlation_exact(a)
        assert v == formula(a), (a,v,formula(a))
        certified_values[str(a)] = str(v)
    # Extra exact verification at generic parameters without extra assumptions.
    for a in (Q(1,20),Q(1,10),Q(1,8),Q(3,20),Q(17,100),Q(1,5),Q(11,50)):
        v, _ = correlation_exact(a)
        assert v == formula(a)
    print('VERIFY_OK: 31 arrangement lines; %d interior triple intersections;' % n_concurrences,
          'only breakpoint 1/6; 5 interpolation nodes; 7 extra exact polygon-area checks;'
          'all 560 cells partition the square exactly')
    print('EXACT_VALUES', certified_values)

if __name__ == '__main__':
    main()
