#!/usr/bin/env python3
"""Finite exact-rational consistency tests for a discrete-location costly-voting model.

Not an exhaustive proof over all real platform choices or real cost exponents.
"""
from fractions import Fraction as F
from itertools import product


def share(x, y, locs, weights, q):
    return sum(w * max(abs(p-y)-abs(p-x), F(0))**q for p, w in zip(locs,weights))


def test_three_blocks():
    grid = [F(i, 24) for i in range(25)]
    positions = (F(0), F(1,2), F(1))
    count = 0
    for q in (1, 2, 3, 4):
        critical = F(1, 1+2**q)
        choices = sorted(set((F(1,10), F(1,5), F(1,4),F(1,3),F(2,5),critical)))
        for e in choices:
            weights = (e, 1-2*e, e)
            eligible = set()
            if e <= critical:
                eligible.update(((0,F(1,2)),(F(1,2),0),(F(1,2),1),(1,F(1,2))))
            if e >= critical:
                eligible.update(((0,1),(1,0)))
            if q == 1 and e == critical:
                # The continuum is tested at all grid points in its two intervals.
                eligible.update((F(0),y) for y in grid if y >= F(1,2))
                eligible.update((F(1),y) for y in grid if y <= F(1,2))
                eligible.update((y,F(0)) for y in grid if y >= F(1,2))
                eligible.update((y,F(1)) for y in grid if y <= F(1,2))
            for x, y in product(grid,repeat=2):
                ux=share(x,y,positions,weights,q)
                uy=share(y,x,positions,weights,q)
                brx=max(share(z,y,positions,weights,q) for z in positions)
                bry=max(share(z,x,positions,weights,q) for z in positions)
                iseq=(ux==brx and uy==bry)
                assert iseq == ((x,y) in eligible), (q,e,x,y,ux,uy,brx,bry)
                count += 1
            if e < critical:
                # In each equilibrium class the participation total is constant.
                x,y=F(0),F(1,2)
                turnout=share(x,y,positions,weights,q)+share(y,x,positions,weights,q)
                assert turnout==F(1,2**q)
            if e > critical:
                x,y=F(0),F(1)
                turnout=share(x,y,positions,weights,q)+share(y,x,positions,weights,q)
                assert turnout==2*e
    return count


def test_support_reduction():
    # On every gap between ideal-point locations, payoff is convex for q>=1.
    # Midpoint inequality checked exactly in many atomic profiles.
    pts=[F(0), F(1,6), F(1,3), F(1,2), F(2,3), F(5,6), F(1)]
    count=0
    for q in (1,2,3):
        for locs in ((F(1,4),F(3,4)), (F(0),F(1,2),F(1)), (F(1,6),F(1,3),F(5,6))):
            weights=(F(1,len(locs)),)*len(locs)
            intervals=sorted(set((F(0),F(1),*locs)))
            for y in pts:
                for a,b in zip(intervals,intervals[1:]):
                    m=(a+b)/2
                    lhs=share(m,y,locs,weights,q)
                    rhs=(share(a,y,locs,weights,q)+share(b,y,locs,weights,q))/2
                    assert lhs<=rhs, (q,locs,y,a,b,lhs,rhs)
                    count+=1
    return count


if __name__ == '__main__':
    a=test_three_blocks()
    b=test_support_reduction()
    print('PASS: exact grid Nash classifications:',a)
    print('PASS: exact within-gap convexity inequalities:',b)
    print('LIMIT: grid comparisons are not a proof for arbitrary real strategies or exponents.')
