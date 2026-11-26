"""Finite exact verification of maximal geodesic general-position counts."""
from collections import Counter
from itertools import combinations
from math import comb


def geodesic_census(n):
    d = [[0 if i == j else n+1 for j in range(n)] for i in range(n)]
    for i, j in combinations(range(n), 2):
        if j-i not in (1, n-1):
            d[i][j] = d[j][i] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])

    bad = [[0]*n for _ in range(n)]
    for i, j, k in combinations(range(n), 3):
        a, b, c = sorted((d[i][j], d[j][k], d[i][k]))
        if a+b == c:
            bad[i][j] |= 1 << k
            bad[i][k] |= 1 << j
            bad[j][k] |= 1 << i

    census = Counter()
    all_vertices = (1 << n)-1

    def visit(chosen, mask, forbidden):
        additions = all_vertices & ~(mask | forbidden)
        if additions == 0:
            census[len(chosen)] += 1
            return
        # Order the recursion only after testing maximality without a label restriction.
        if chosen:
            additions &= ~((1 << (chosen[-1]+1))-1)
        while additions:
            bit = additions & -additions
            additions ^= bit
            w = bit.bit_length()-1
            new_forbidden = forbidden
            for i in chosen:
                new_forbidden |= bad[i][w]
            visit(chosen+(w,), mask|bit, new_forbidden)

    visit((), 0, 0)
    return census


def predicted(n):
    if n == 5:
        return Counter({3: 5})
    if n == 6:
        return Counter({2: 3, 3: 8})
    outcome = Counter({3: n})
    for k in range((n+2)//3, n//2+1):
        term, remainder = divmod(n*comb(k, n-2*k), k)
        assert remainder == 0
        outcome[k] += term
    return outcome


if __name__ == '__main__':
    for n in range(5, 17):
        observed = geodesic_census(n)
        assert observed == predicted(n), (n, observed)
        print(n, sorted(observed.items()))
    print('MAXIMAL_CENSUS_CHECK_OK n=5..16')
