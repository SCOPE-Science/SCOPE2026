#!/usr/bin/env python3
"""Finite consistency check for sharp component-partition Betti envelopes."""
from itertools import combinations_with_replacement

def partition_bound(degrees):
    return 2 + sum((a-1)*(a-2) for a in degrees) + sum(
        a*b for i, a in enumerate(degrees) for b in degrees[i+1:]
    )

def alternate_bound(degrees):
    d = sum(degrees)
    r = len(degrees)
    squares = sum(a*a for a in degrees)
    assert (d*d + squares) % 2 == 0
    return 2 + (d*d + squares)//2 - 3*d + 2*r

def fixed_count_max(d, r):
    return d*d - d*r - 2*d + r*(r+3)//2 + 2

def global_max(d):
    return {1: 2, 2: 3, 3: 5}.get(d, d*d-3*d+4)

def run():
    n = 0
    for d in range(1, 13):
        by_count = {}
        for r in range(1, d+1):
            values = [(partition_bound(p), p)
                      for p in combinations_with_replacement(range(1, d+1), r)
                      if sum(p) == d]
            assert values
            for val, p in values:
                assert val == alternate_bound(p)
            best = max(v for v, _ in values)
            expected = tuple(sorted((d-r+1,) + (1,)*(r-1)))
            assert best == fixed_count_max(d, r)
            assert {p for v, p in values if v == best} == {expected}
            by_count[r] = best
            n += len(values)
        assert max(by_count.values()) == global_max(d)
        if d >= 5:
            assert max(by_count[r] for r in range(2, d+1)) == d*d-4*d+7
            winners = {r for r in range(2, d+1)
                       if by_count[r] == d*d-4*d+7}
            assert winners == ({2, d} if d == 5 else {2})
        if d == 4:
            assert {r for r, v in by_count.items() if v == 8} == {1, 4}
    print('VERIFY_OK', n, 'partition cases')

if __name__ == '__main__':
    run()
