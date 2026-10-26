"""Reproduce the exact descent-conditioned record boundary, without simulations."""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial


def enumerate_counts(n):
    totals = [0] * n
    marks = [[0] * n for _ in range(n)]
    for p in permutations(range(n)):
        d = sum(p[k] > p[k+1] for k in range(n-1))
        totals[d] += 1
        maximum = -1
        for j, v in enumerate(p):
            if v > maximum:
                maximum = v
                marks[j][d] += 1
    assert sum(totals) == factorial(n)
    return totals, marks


def subset_dp_counts(n, mark_position):
    # Key: used-value subset, last element, descents, flag (record at target).
    curr = {(1 << v, v, 0, int(mark_position == 1)): 1 for v in range(n)}
    for length in range(1, n):
        nxt = defaultdict(int)
        for (mask, last, d, record), count in curr.items():
            for v in range(n):
                if mask & (1 << v):
                    continue
                rec = int(v > mask.bit_length()-1) if length + 1 == mark_position else record
                nxt[mask | (1 << v), v, d + int(last > v), rec] += count
        curr = nxt
    totals = [0] * n
    marks = [0] * n
    for (_, _, d, rec), count in curr.items():
        totals[d] += count
        marks[d] += count * rec
    return totals, marks


def verify():
    violations = []
    for n in range(2, 9):
        totals, records = enumerate_counts(n)
        for j in range(2, n + 1):
            dptotals, dprecords = subset_dp_counts(n, j)
            assert dptotals == totals and dprecords == records[j-1], (n, j)
            for d in range(n-2):
                left = records[j-1][d+1] * totals[d]
                right = records[j-1][d] * totals[d+1]
                if left > right:
                    violations.append((n, j, d, left-right))
    assert violations == [(8, 5, 5, 3043)], violations
    print('All n=2,...,8 verified by two independent enumerations.')
    print('First and only violation: n=8, j=5, d=5 to 6, determinant=3043.')
    print('P(R_5=1|D=5) =',Fraction(596,4293))
    print('P(R_5=1|D=6) =',Fraction(35,247))
    print('Difference =',Fraction(35,247)-Fraction(596,4293))

if __name__ == '__main__':
    verify()
