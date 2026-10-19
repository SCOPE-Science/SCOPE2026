#!/usr/bin/env python3
"""Exact GF(2) rank tests for folded-cube adjacency matrices."""
def rank_binary(rows):
    pivots = {}
    for row in rows:
        while row:
            col = row.bit_length() - 1
            if col not in pivots:
                pivots[col] = row
                break
            row ^= pivots[col]
    return len(pivots)

def check():
    for d in range(2, 11):
        n = 1 << d
        steps = [1 << i for i in range(d)] + [n - 1]
        rows = []
        for x in range(n):
            row = 0
            for s in steps:
                row ^= 1 << (x ^ s)
            rows.append(row)
        actual = rank_binary(rows)
        expected = n if d % 2 == 0 else n//2 - (1 << ((d-1)//2))
        assert actual == expected, (d, actual, expected)
        print('d=', d, 'rank=', actual, 'dim(E2)=', expected, 'PASS')
    print('ALL 9 FOLDED-CUBE RANK TESTS PASS')

if __name__ == '__main__':
    check()
