#!/usr/bin/env python3
"""Reproduce the complete binary-weight-four parameter classification on a finite test grid.

The unrestricted assertion is proved separately by elementary carry analysis.
"""

def predicted(u, v, w):
    return ((u == v == 1 and w >= 4)
            or (u == v and u >= 3 and w == u + 1)
            or (u == v and u >= 2 and w == 2*u)
            or (u == w and u >= 3 and v == 1)
            or (u == 1 and v >= 2 and w == v + 1))


def weight(u, v, w):
    return ((1 << u) + 1).__mul__(1 + (1 << v) + (1 << w)).bit_count()


def main():
    totals = {2:0, 3:0, 4:0, 5:0, 6:0}
    exceptions = []
    checked = 0
    for u in range(1, 81):
        for v in range(1, 80):
            for w in range(v+1, 81):
                actual = weight(u,v,w)
                assert 2 <= actual <= 6, (u,v,w,actual)
                assert (actual == 4) == predicted(u,v,w), (u,v,w,actual)
                totals[actual] += 1
                checked += 1
                if actual <= 3:
                    exceptions.append((u,v,w,actual))
    assert sorted(exceptions) == sorted([
        (1,1,2,3), (1,1,3,2), (2,1,2,3), (2,2,3,2)
    ]), exceptions
    for u,v,w in [(1,1,4),(3,3,4),(2,2,4),(3,1,3),(1,2,3),(25,25,26),(60,1,60)]:
        assert predicted(u,v,w) and weight(u,v,w) == 4
    print('VERIFIED',checked,'triples',totals,'low-weight exceptions',exceptions)

if __name__ == '__main__':
    main()
