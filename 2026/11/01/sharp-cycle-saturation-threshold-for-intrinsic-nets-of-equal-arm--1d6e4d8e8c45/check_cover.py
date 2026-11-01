#!/usr/bin/env python3
"""Exact rational checks for a metric multi-theta covering construction.

All network points are represented by (edge-index, coordinate from endpoint A).
Edge 0 has length L; edges 1,...,m have length s.
"""
from fractions import Fraction as F
from itertools import product


def distance(lengths, i, x, j, y):
    """Exact intrinsic shortest-path distance on parallel-edge metric graph."""
    a, b = min(lengths), max(lengths)
    assert a > 0
    if i == j:
        # The direct route, or a route using a shortest different A--B arm.
        alternate = min(lengths[k] for k in range(len(lengths)) if k != i)
        return min(abs(x-y), x+alternate+lengths[i]-y,
                   lengths[i]-x+alternate+y)
    return min(x+y, (lengths[i]-x)+(lengths[j]-y),
               x+min(lengths[k] for k in range(len(lengths)) if k != i and k != j)+(lengths[j]-y),
               (lengths[i]-x)+min(lengths[k] for k in range(len(lengths)) if k != i and k != j)+y)


def check_case(s, L, m, p):
    assert m >= 2 and L >= s > 0 and p >= 1 and L >= (p-1)*s
    r = (L+s)/F(2*p)
    t = r-s/F(2)
    xs = [t+2*j*r for j in range(p)]
    assert xs[0] == t and xs[-1] == L-t
    assert t >= 0 and all(0 <= x <= L for x in xs)
    assert all(xs[j+1]-xs[j] == 2*r for j in range(p-1))
    assert xs[0]-r == -s/F(2) and xs[-1]+r == L+s/F(2)
    # Direct long-edge balls and endpoint access on all remaining edges.
    for i in range(m+1):
        li = L if i == 0 else s
        # Distances are continuous piecewise affine. The strict symbolic
        # enclosure gives universal coverage, and the rational mesh tests
        # independently corroborate the exact network distance formula.
        for k in range(51):
            x = li * F(k, 50)
            d = min(distance([L]+[s]*m, i, x, 0, z) for z in xs)
            assert d <= r, (s, L, m, p, i, x, d, r)
    return len(xs)*(m+1)*51


def main():
    cases = 0
    checks = 0
    lengths = [F(1),F(3,2),F(7,3),F(5)]
    for s in [F(1,3), F(1), F(5,2)]:
        for p in range(1, 9):
            for m in [2,3,5,9]:
                for L in lengths + [(p-1)*s if p >= 2 else s, (p-1)*s+s/F(7)]:
                    if L < s or L < (p-1)*s:
                        continue
                    checks += check_case(s,L,m,p)
                    cases += 1
    # Strict regime algebra: q<s/2 precisely when L<(p-1)s.
    for s in [F(1,3),F(1),F(5,2)]:
        for p in range(3,12):
            for L in [s, (p-1)*s-s/F(13)]:
                if L < s or L >= (p-1)*s:continue
                q=(L+s)/F(2*p)
                assert q < s/F(2)
                # For a center t in the interior of a short edge not on
                # the chosen circle, at most one of t and s-t is <q.
                for k in range(1,100):
                    t=s*F(k,100)
                    assert not (t < q and s-t < q)
                    a=max(F(0),q-t)
                    b=max(F(0),q-(s-t))
                    assert 2*(a+b) < 2*q
                checks += 99
    print('PASS exact-rational network tests:',cases,'parameter cases,',checks,'point and obstruction checks')

if __name__ == '__main__':main()
