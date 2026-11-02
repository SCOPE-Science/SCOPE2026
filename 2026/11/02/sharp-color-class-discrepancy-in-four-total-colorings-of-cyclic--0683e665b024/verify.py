#!/usr/bin/env python3
"""Exact finite sanity checks for four-color total colorings of cyclic prisms.

The general theorem is proved combinatorially in RESULT.md; this script
independently checks the displayed blocks and enumerates cyclic states.
"""
from itertools import product

P3 = ('30102', '23130', '02123')
P4 = ('30102', '21310', '03231', '12023')
P7 = ('30102', '23130', '01213', '32021', '10302', '23130', '02123')
P8 = ('30102', '23130', '01213', '30201', '12320', '01312', '23031', '12023')


def direct_check(blocks):
    seq = tuple(tuple(map(int, x)) for x in blocks)
    n = len(seq)
    assert n >= 3
    # Independently represent the original labelled graph.  At rung i,
    # the tuple is (top vertex, bottom vertex, rung edge,
    #               forward top edge, forward bottom edge).
    for i in range(n):
        a, b, r, t, u = seq[i]
        prev = seq[(i - 1) % n]
        nex = seq[(i + 1) % n]
        assert set((a, r, t, prev[3])) == set(range(4))
        assert set((b, r, u, prev[4])) == set(range(4))
        assert a != b and a != nex[0] and b != nex[1]
    total = [sum(row.count(c) for row in seq) for c in range(4)]
    vertex = [sum((row[0] == c) + (row[1] == c) for row in seq) for c in range(4)]
    assert sum(vertex) == 2*n and sum(total) == 5*n
    assert all(total[c] == n + vertex[c]//2 for c in range(4))
    return vertex, total


def state_graph():
    states = []
    for s in product(range(4), repeat=5):
        a, b, r, t, u = s
        if len({a, b, r}) != 3 or len({a, r, t}) != 3 or len({b, r, u}) != 3:
            continue
        states.append(s)
    follow = []
    for old in states:
        reachable = []
        for j, new in enumerate(states):
            a, b, r, t, u = new
            pa, pb, pr, pt, pu = old
            if a == pa or b == pb:
                continue
            if len({a, r, t, pt}) == 4 and len({b, r, u, pu}) == 4:
                reachable.append(j)
        follow.append(tuple(reachable))
    return states, follow


def max_delta(states, follow, n):
    # Color-name symmetry lets us optimize the difference of any chosen
    # ordered pair of color classes, here 0 and 1.
    wt = [s.count(0) - s.count(1) for s in states]
    optimum = None
    for start in range(len(states)):
        cur = {start: 0}
        for _ in range(n):
            nxt = {}
            for u, value in cur.items():
                for v in follow[u]:
                    z = value + wt[v]
                    if z > nxt.get(v, -10**9):
                        nxt[v] = z
            cur = nxt
        if start in cur:
            optimum = cur[start] if optimum is None else max(optimum, cur[start])
    return optimum


def main():
    for n, block in ((3,P3), (4,P4), (7,P7), (8,P8)):
        v, c = direct_check(block)
        assert (v,c) == {
            3: ([2,0,2,2], [4,3,4,4]),
            4: ([2,2,2,2], [5,5,5,5]),
            7: ([4,2,4,4], [9,8,9,9]),
            8: ([4,4,4,4], [10,10,10,10]),
        }[n]
        print('BASE_ORIGINAL_GRAPH_OK', n, v, c)
    for n in range(6,91):
        k, r = divmod(n,3)
        seq = (P3*k) if r==0 else ((P7 if r==1 else P8) + P3*(k-2))
        assert len(seq)==n
        vertex, total = direct_check(seq)
        assert vertex == [2*k,2*r,2*k,2*k]
        assert max(total)-min(total)==k-r
    print('ALL_BLOCK_CONCATENATIONS_DIRECTLY_CHECKED', 6,90)
    states, follow = state_graph()
    assert len(states)==96 and sum(map(len,follow))==168
    for n in range(3,25):
        actual = max_delta(states,follow,n)
        k, r = divmod(n,3)
        expected = None if n==5 else k-r
        assert actual == expected, (n, actual, expected)
        print('INDEPENDENT_EXHAUSTIVE_TRANSFER_OK',n,actual)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
