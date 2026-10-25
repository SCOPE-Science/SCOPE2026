#!/usr/bin/env python3
"""Exact independent enumeration of 2-stable matchings on labeled cycles.

The model uses local ranks 1 (favorite neighbor), 2 (other neighbor),
3 (unmatched), with a pair blocking at threshold 2 only if each endpoint
improves by at least two ranks.  All arithmetic is integral.
"""
from collections import Counter
from math import comb


def matchings(n):
    """All edge masks for matchings in C_n, with edge i=(i,i+1)."""
    for mask in range(1 << n):
        if all(not ((mask >> i) & 1 and (mask >> ((i+1)%n)) & 1)
               for i in range(n)):
            yield mask


def rank(n, preferences, vertex, partner):
    """Preference bit 1 means prefer clockwise neighbor; 0 anticlockwise."""
    if partner is None:
        return 3
    clockwise = (vertex + 1) % n
    assert partner in (clockwise, (vertex - 1) % n)
    preferred_clockwise = (preferences >> vertex) & 1
    return 1 if (partner == clockwise) == bool(preferred_clockwise) else 2


def is_stable(n, preferences, edge_mask):
    partner = [None] * n
    for i in range(n):
        if (edge_mask >> i) & 1:
            j = (i + 1) % n
            assert partner[i] is None and partner[j] is None
            partner[i], partner[j] = j, i
    for i in range(n):
        if (edge_mask >> i) & 1:
            continue
        j = (i + 1) % n
        improvement_i = rank(n, preferences, i, partner[i]) - rank(n, preferences, i, j)
        improvement_j = rank(n, preferences, j, partner[j]) - rank(n, preferences, j, i)
        if improvement_i >= 2 and improvement_j >= 2:
            return False
    return True


def matrix():
    states = [(a,b,o) for a in range(2) for b in range(2)
              for o in range(2) if not (a and b)]
    mats = [[[0,0] for _ in states] for _ in states]
    for i,(a,b,o) in enumerate(states):
        for j,(bb,c,op) in enumerate(states):
            if b == bb and not (a == b == c == 0 and o == 1 and op == 0):
                mats[i][j][c] = 1
    return states,mats


def matmul(A, B):
    m = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(m)] for i in range(m)]


def main():
    states, mats = matrix()
    assert states == [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1)]
    for z in (0,1,2,3,7):
        T = [[entry[0] + z * entry[1] for entry in row] for row in mats]
        A = [[int(i == j) for j in range(6)] for i in range(6)]
        for n in range(1,17):
            A = matmul(A, T)
            transfer_count = sum(A[i][i] for i in range(6))
            direct_formula = 2 * sum(comb(n,2*j) * (4*z)**j
                                      for j in range(n//2+1))
            assert transfer_count == direct_formula, (n,z,transfer_count,direct_formula)
    print('Transfer-matrix polynomial identity checked at z=0,1,2,3,7 and powers 1..16.')
    for n in range(3,12):
        histogram = Counter()
        allowed_matchings = list(matchings(n))
        for preferences in range(1 << n):
            for matching in allowed_matchings:
                if is_stable(n, preferences, matching):
                    histogram[matching.bit_count()] += 1
        predicted = {j: 2 * (4**j) * comb(n,2*j)
                     for j in range(n//2+1)}
        assert dict(histogram) == predicted, (n, histogram, predicted)
        print(f'n={n:2d} profiles={1<<n:6d} matchings={len(allowed_matchings):4d} '
              f'count_by_size={dict(sorted(histogram.items()))} total={sum(histogram.values())}')
    print('PASS: direct rank-difference exhaustive enumerations all agree, n=3..11.')

if __name__ == '__main__':
    main()
