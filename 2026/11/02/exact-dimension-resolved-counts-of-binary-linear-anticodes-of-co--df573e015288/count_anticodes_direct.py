#!/usr/bin/env python3
"""Direct subspace weight enumeration independent of the parity-check formula.
Each row-reduced echelon basis represents one labeled subspace.
This checker intentionally tests codeword weights, not column sums.
"""
from itertools import combinations
from count_anticodes import theoretical

def codes(n, k):
    for pivots in combinations(range(n), k):
        free = [(i, j) for i in range(k) for j in range(pivots[i]+1, n) if j not in pivots]
        for bits in range(1 << len(free)):
            rows = [1 << p for p in pivots]
            for b, (i,j) in enumerate(free):
                if (bits >> b) & 1:
                    rows[i] ^= 1 << j
            yield rows

def count_by_weights(n, r):
    total=0
    for rows in codes(n,n-r):
        codewords=[0]
        for row in rows:
            codewords.extend([v ^ row for v in codewords[:]])
        if all(x.bit_count() <= n-2 for x in codewords):
            total += 1
    return total

if __name__ == '__main__':
    for n in range(2,8):
        for r in range(1,n+1):
            direct = count_by_weights(n,r)
            expected = theoretical(n,r)
            assert direct == expected, (n,r,direct,expected)
            print(f'({n},{r}) direct={direct} formula={expected}')
    print('DIRECT WEIGHT CHECKS PASS')
