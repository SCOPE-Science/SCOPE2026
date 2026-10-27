#!/usr/bin/env python3
"""Exact first-order rank-four types of connected half-graphs.

A type at rank zero records *all* atomic formulas on an ordered tuple.
At rank r>0 it also records the set of rank-(r-1) types obtained
by extending the tuple with one arbitrary vertex. For finite relational
structures this recursion is exactly the complete quantifier-rank type.
No random search, approximations, or graph-size extrapolation is used.
"""
from functools import lru_cache


def verify():
    ids = {}

    def intern(v):
        if v not in ids:
            ids[v] = len(ids)
        return ids[v]

    def type_of(n, r, colored):
        """Rank r type of H_n, with optional unary bipartition predicate."""
        def edge(x, y):
            if x < n <= y:
                return x <= y - n
            if y < n <= x:
                return y <= x - n
            return False

        @lru_cache(None)
        def tp(depth, xs):
            atomic = (
                tuple(x < n for x in xs) if colored else (),
                tuple((xs[i] == xs[j], edge(xs[i], xs[j]))
                      for i in range(len(xs)) for j in range(i + 1, len(xs))),
            )
            if depth == 0:
                return intern((0, len(xs), atomic))
            successors = frozenset(tp(depth - 1, xs + (v,))
                                   for v in range(2 * n))
            return intern((depth, len(xs), atomic, successors))

        ans = tp(r, ())
        return ans, tp.cache_info().currsize

    # Uncolored H_1 through H_8: seven types, last pair equivalent.
    unc = [type_of(n, 4, False) for n in range(1, 9)]
    assert len({t for t, states in unc}) == 7, unc
    assert len({t for t, states in unc[:7]}) == 7, unc
    assert unc[6][0] == unc[7][0], unc

    # In the bipartition-labelled language H_8 and H_9 are equivalent.
    col = [type_of(n, 4, True) for n in range(7, 10)]
    assert col[0][0] != col[1][0], col
    assert col[1][0] == col[2][0], col

    # Lower ranks provide consistency checks on separate configurations.
    low = {}
    for q in (1, 2, 3):
        low[q] = [type_of(n, q, False)[0] for n in range(1, 10)]
    assert len(set(low[1])) == 1
    assert len(set(low[2])) == 2
    assert len(set(low[3])) == 3
    assert all(low[3][i] == low[3][2] for i in range(2, 9))

    print('rank-four uncolored type partition: {1},{2},{3},{4},{5},{6},{7,8}')
    print('rank-four colored H_7 differs from H_8: True')
    print('rank-four colored H_8 equals colored H_9: True')
    print('rank-one, two, three uncolored class counts on n=1..9: 1,2,3')
    print('rank-four finite computations: exact finite successor-type recursion')
    print('largest uncolored tuple-state count:', max(x[1] for x in unc))
    print('largest colored tuple-state count:', max(x[1] for x in col))
    print('PASS')


if __name__ == '__main__':
    verify()
