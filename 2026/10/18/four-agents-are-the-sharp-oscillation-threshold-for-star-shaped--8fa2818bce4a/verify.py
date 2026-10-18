"""Exact auxiliary checks for the three-agent star-shaped-confidence cutoff.

Uses only Python's standard library; finite checks support, but do not
replace, the proof applying to all dimensions and all star-shaped sets.
"""
from fractions import Fraction as F


def update_mobile(s, a, b):
    return (s + b) / (1 + a + b)


def check_ordering():
    # A(s) may only drop; B(s) may only rise as s increases.
    count = 0
    grid = [F(i, 24) for i in range(25)]
    for s in grid:
        for t in grid:
            if s > t:
                continue
            for a_s in (0, 1):
                for b_s in (0, 1):
                    for a_t in (0, 1):
                        for b_t in (0, 1):
                            if a_t > a_s or b_t < b_s:
                                continue
                            assert update_mobile(s, a_s, b_s) <= update_mobile(t, a_t, b_t)
                            count += 1
    return count


def in_star_confidence(v):
    x, y = v
    # Unit closed disk plus positive horizontal and two negative diagonal rays.
    return (x*x+y*y <= 1 or
            (x > 0 and y == 0) or
            (x < 0 and (y == x/5 or y == -x/5)))


def add(p, q):
    return tuple(a+b for a, b in zip(p, q))


def sub(p, q):
    return tuple(a-b for a, b in zip(p, q))


def hk_update(points, conf):
    nxt=[]
    neighbors=[]
    for i, p in enumerate(points):
        idx = [j for j,q in enumerate(points) if conf(sub(q,p))]
        assert i in idx
        neighbors.append(idx)
        nxt.append(tuple(sum((points[j][c] for j in idx), F(0))/len(idx)
                         for c in range(len(p))))
    return nxt, neighbors


def check_sharp_witness():
    # X moves, the remaining three agents stay at the stated anchor opinions.
    a,b,c=(F(-3),F(1)),(F(-3),F(-1)),(F(4),F(0))
    x0,x1=(F(0),F(0)),(F(2),F(0))
    p0=[x0,a,b,c]
    p1, neighbors0=hk_update(p0,in_star_confidence)
    p2, neighbors1=hk_update(p1,in_star_confidence)
    assert p1 == [x1,a,b,c], (p1,neighbors0)
    assert p2 == p0, (p2,neighbors1)
    assert neighbors0 == [[0,3],[1],[2],[3]], neighbors0
    assert neighbors1 == [[0,1,2,3],[1],[2],[3]], neighbors1
    assert not in_star_confidence((F(-2),F(0)))
    assert in_star_confidence((F(-5),F(1)))
    return neighbors0,neighbors1


def check_nonstar_three_agent_contrast():
    # Reproduces the SOURCE's non-star-shaped, no-stubborn 3-agent cycle.
    banned={F(z) for z in (-5,-4,-3,-2,-1,1,3,5,6)}
    conf=lambda v: -7 < v[0] < 7 and v[0] not in banned
    p0=[(F(0),),(F(6),),(F(7),)]
    path=[p0]
    for _ in range(3):
        nxt,_=hk_update(path[-1],conf)
        path.append(nxt)
    assert path[1][1] == (F(3),) and path[2][1] == (F(5),)
    assert path[3] == p0
    # The interval between 0 and the accepted direction -6 is not all accepted:
    assert conf((F(-6),)) and not conf((F(-5),))
    return [int(p[1][0]) for p in path]


if __name__ == '__main__':
    print('Ordered secant-table comparisons:',check_ordering())
    print('Four-agent period-two neighbor sets:',check_sharp_witness())
    print('Non-star-shaped three-agent contrast:',check_nonstar_three_agent_contrast())
    print('All exact arithmetic checks passed.')
