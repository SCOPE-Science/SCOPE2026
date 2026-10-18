"""Independent small-case test of fixed-point census for Takasaki quandle good involutions.

Only Python standard library. Run: python check_good_involutions.py
"""
from collections import Counter
from itertools import permutations, product
from math import comb, factorial, prod


def predicted(orders):
    n = prod(orders)
    d = sum(t % 2 == 0 for t in orders)
    e = sum(t % 2 == 0 and t % 4 != 0 for t in orders)
    K, L, b, h = 2 ** (d - e), 2 ** e, 2 ** (d - e), n // (2 ** d)
    # Polynomial multiplication by combinatorial convolution.
    def mul(p, q):
        r = Counter()
        for i, a in p.items():
            for j, c in q.items():
                r[i + j] += a * c
        return r
    unit = {0: 1}
    monomer = {0: K - 1, h: 1} if K > 1 else {h: 1}
    block = Counter()
    for pairs in range(L // 2 + 1):
        matchings = factorial(L) // (2 ** pairs * factorial(pairs) * factorial(L - 2 * pairs))
        term = unit
        for _ in range(L - 2 * pairs):
            term = mul(term, monomer)
        for degree, coef in term.items():
            block[degree] += matchings * K ** pairs * coef
    result = unit
    for _ in range(b):
        result = mul(result, block)
    return {i: count for i, count in result.items() if count}


def brute(orders):
    elems = list(product(*[range(x) for x in orders]))
    n = len(elems)
    idx = {v: i for i, v in enumerate(elems)}
    op = [[idx[tuple((2 * y[j] - x[j]) % orders[j] for j in range(len(orders)))]
           for y in elems] for x in elems]
    # direct permutation test against quandle good-involution identities
    distribution = Counter()
    for f in permutations(range(n)):
        if any(f[f[i]] != i for i in range(n)):
            continue
        # involutory kei's good property: x triangle f(y) == x triangle y
        if any(op[x][f[y]] != op[x][y] for x in range(n) for y in range(n)):
            continue
        # good condition: f(x triangle y) == f(x) triangle y
        if any(f[op[x][y]] != op[f[x]][y] for x in range(n) for y in range(n)):
            continue
        distribution[sum(f[i] == i for i in range(n))] += 1
    return dict(distribution)


def main():
    families = [(1,), (3,), (4,), (5,), (6,), (7,), (8,), (2, 2), (2, 4), (2, 2, 2), (2, 3)]
    for orders in families:
        actual = brute(orders)
        forecast = predicted(orders)
        assert forecast == actual, (orders, forecast, actual)
        print(f'{orders}: {forecast}  total={sum(forecast.values())}')
    assert predicted((2, 4)) == {0: 9, 2: 12, 4: 10, 6: 4, 8: 1}
    assert predicted((2, 2, 2)) == {8: 1, 6: 28, 4: 210, 2: 420, 0: 105}
    print('CHECKER_OK')

if __name__ == '__main__':
    main()
