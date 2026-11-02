#!/usr/bin/env python3
"""Exact finite checks for the triangular Lipschitz semigroup formula.

No third-party libraries. This is a finite test of the source theorem's
Newton-polyhedron/lattice membership criterion, not an infinite proof.
"""
from math import gcd


def original(a, b, n):
    return b == 0 or b >= n or a >= n


def predicted(a, b, n):
    return original(a, b, n) or (a >= 1 and b >= 1 and a+b >= n+1)


def criterion(a, b, n):
    # Check the complete subset criterion (Bernard--Chavez-Martinez--
    # Giles Flores, Theorem 3.7) for all 1 <= a,b < n.
    # The generator (1,0) belongs to a subset -> its Newton polyhedron
    # contains the test point. Otherwise the complement contains (1,0),
    # and the lattice condition is exactly gcd(y-coordinates) | b.
    assert 1 <= a < n and 1 <= b < n
    points = [(0, j) for j in range(n, 2*n)] + [(n, j) for j in range(1, n)]
    count = len(points)
    tested = 0
    for mask in range(1 << count):
        tested += 1
        g = 0
        vmin, hmin = None, None
        for idx, (x,y) in enumerate(points):
            if mask & (1 << idx):
                if x == 0:
                    vmin = y if vmin is None else min(y, vmin)
                else:
                    hmin = y if hmin is None else min(y, hmin)
            else:
                g = gcd(g, y)
        # x=0 and x=n are the only Newton generators when (1,0)
        # lies in the complementary set. A mixing segment minimizes y.
        inside_newton = ((vmin is not None and b >= vmin) or
                         (vmin is not None and hmin is not None and
                          n*b >= n*vmin - a*(vmin-hmin)))
        lattice_ok = (g == 1 or (g > 0 and b % g == 0))
        if not (inside_newton or lattice_ok):
            return False, mask, tested
    return True, None, tested


def minimal_generators(n, saturated):
    # Check all exponents bounded by 2n in each coordinate, safely
    # containing the predicted elementary generators.
    inside = saturated if saturated else original
    elements = {(a,b) for a in range(2*n+1)
                for b in range(2*n+1) if inside(a,b,n)}
    generators = set()
    for a,b in elements:
        if (a,b) == (0,0):
            continue
        decomposable = any((x,y) != (0,0) and (x,y) != (a,b) and
                           (x,y) in elements and (a-x,b-y) in elements
                           for x in range(a+1) for y in range(b+1))
        if not decomposable:
            generators.add((a,b))
    return generators


def run():
    evaluated = 0
    masks = 0
    for n in range(3,9):
        holes = []
        for a in range(1,n):
            for b in range(1,n):
                actual, counterexample, tested = criterion(a,b,n)
                masks += tested
                want = predicted(a,b,n)
                assert actual == want, (n,a,b,actual,want,counterexample)
                evaluated += 1
                if actual:
                    holes.append((a,b))
        assert len(holes) == (n-1)*(n-2)//2
        expected_gen = ({(1,0)} |
                        {(0,b) for b in range(n,2*n)} |
                        {(n,1)} |
                        {(n+1-b,b) for b in range(2,n)})
        actual_gen = minimal_generators(n, predicted)
        assert actual_gen == expected_gen, (n,actual_gen ^ expected_gen)
        assert len(actual_gen) == 2*n
        old_gen = minimal_generators(n, original)
        assert len(old_gen) == 2*n
        print('n=%d holes=%d minimal_generators=%d checked_q=%d' %
              (n,len(holes),len(actual_gen),(n-1)**2))
    print('VERIFY_OK: %d full-subset decisions; %d subsets actually tested' % (evaluated,masks))

if __name__ == '__main__':
    run()
