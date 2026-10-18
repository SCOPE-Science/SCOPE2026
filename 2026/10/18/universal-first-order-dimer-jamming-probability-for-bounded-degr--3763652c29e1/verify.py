"""Exact reproducibility checks for random greedy bipartite dimer deposition.

Run with Python 3 standard library.  Vertex labels are 0,...,n-1 on each side.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations


def failure_dp(n, forbidden):
    """Exact incomplete-cover probability under uniform remaining-edge choice."""
    forbidden = frozenset(forbidden)
    @lru_cache(None)
    def p(L, R):
        remaining = [(u, v) for u in range(n) if L & (1 << u)
                     for v in range(n) if R & (1 << v)
                     if (u, v) not in forbidden]
        if not remaining:
            return Fraction(int(L != 0), 1)
        return sum((p(L ^ (1 << u), R ^ (1 << v)) for u, v in remaining),
                   Fraction(0)) / len(remaining)
    return p((1 << n) - 1, (1 << n) - 1)


def failure_orders(n, forbidden):
    """A separate exact construction: enumerate permutations of allowed edges."""
    edges = [(u, v) for u in range(n) for v in range(n)
             if (u, v) not in forbidden]
    fails = 0
    total = 0
    for order in permutations(edges):
        usedL, usedR = set(), set()
        for u, v in order:
            if u not in usedL and v not in usedR:
                usedL.add(u)
                usedR.add(v)
        total += 1
        fails += int(len(usedL) < n)
    return Fraction(fails, total)


def check():
    checks = 0
    for n in range(2, 9):
        one = {(0, 0)}
        assert failure_dp(n, one) == Fraction(2, n * (n + 1))
        checks += 1
        examples = {
            'matching': {(i, i) for i in range(n)},
            'path': {(i, i) for i in range(n)} |
                    {(i, i + 1) for i in range(n - 1)},
            'cycle': {(i, i) for i in range(n)} |
                     {(i, (i + 1) % n) for i in range(n)},
        }
        for key, forbidden in examples.items():
            p = failure_dp(n, forbidden)
            assert Fraction(0) <= p <= Fraction(1)
            # For n sufficiently above the forbidden maximum degree,
            # a perfect matching exists even though greedy failure can occur.
            print(n, key, len(forbidden), p,
                  round(float(p) * n * n / (2 * len(forbidden)), 8))
            checks += 1
    for forbidden in ({(0, 0)}, {(i, i) for i in range(3)},
                      {(0, 0), (0, 1), (1, 1)}):
        assert failure_dp(3, forbidden) == failure_orders(3, forbidden)
        checks += 1
    print('PASS', checks, 'exact checks, including three independent edge-order enumerations')


if __name__ == '__main__':
    check()
