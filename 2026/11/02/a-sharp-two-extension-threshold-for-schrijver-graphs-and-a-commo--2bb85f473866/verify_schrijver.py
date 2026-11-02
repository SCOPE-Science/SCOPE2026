"""Exhaustive two-point extension test for stable Kneser graphs.

The graph has cyclically nonconsecutive r-subsets of {0,...,n-1} as
vertices, adjacent exactly when they are disjoint. This program checks
all four adjacency profiles outside every pair of distinct vertices.
"""
from itertools import combinations


def vertices(n, r):
    return [sum(1 << i for i in s)
            for s in combinations(range(n), r)
            if all((i + 1) % n not in s for i in s)]


def exhaustive_check(n, r):
    v = vertices(n, r)
    m = len(v)
    full = (1 << m) - 1
    neighborhoods = []
    for a in v:
        q = 0
        for j, b in enumerate(v):
            if a & b == 0:
                q |= 1 << j
        neighborhoods.append(q)
    all_good = True
    counterexample = None
    for i in range(m):
        ai = neighborhoods[i]
        for j in range(i+1, m):
            remain = full ^ (1 << i) ^ (1 << j)
            x = ai & remain
            y = neighborhoods[j] & remain
            has = (bool(x & y), bool(x & (remain ^ y)),
                   bool((remain ^ x) & y),
                   bool((remain ^ x) & (remain ^ y)))
            if not all(has):
                all_good = False
                counterexample = (i, j, has)
                break
        if not all_good:
            break
    return m, all_good, counterexample


def run():
    passed = 0
    total_pairs = 0
    for r, low, high in ((2,5,12), (3,7,17), (4,9,20), (5,16,20)):
        for n in range(low, high+1):
            if n < 2*r+1:
                continue
            count, ok, witness = exhaustive_check(n, r)
            expected = (n >= 4*r-1)
            assert ok == expected, (r,n,count,witness)
            passed += 1
            total_pairs += count*(count-1)//2 if ok else 0
        print(f'r={r}: checked n={max(2*r+1,low)}..{high}; predicted threshold={4*r-1}')
    print(f'PASS: {passed} finite graph instances, >= {total_pairs} fully examined vertex pairs')


if __name__ == '__main__':
    run()
