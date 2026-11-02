"""Finite checks for the real sup-norm mutual Birkhoff--James orthograph.

Standard library only; analytical proofs in RESULT.md cover arbitrary n.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb


def canonical(x):
    x = tuple(x)
    if not any(x):
        raise ValueError('zero vector')
    if next(v for v in x if v) < 0:
        return tuple(-v for v in x)
    return x


def active_round(x):
    a = max(map(abs, x))
    return canonical((1 if v == a else -1 if v == -a else 0) for v in x)


def bj(x, y):
    a = max(map(abs, x))
    z = [x[i] * y[i] for i in range(len(x)) if abs(x[i]) == a]
    return min(z) <= 0 <= max(z)


def mutual(x, y):
    return bj(x, y) and bj(y, x)


def subset_compatible(x, y):
    # Signed partial x is projectively compatible with a restriction of y.
    inds = [i for i, v in enumerate(x) if v]
    if not all(y[i] for i in inds):
        return False
    values = {x[i]*y[i] for i in inds}
    return len(values) == 1  # either all plus or all minus


def comparable(x, y):
    return subset_compatible(x, y) or subset_compatible(y, x)


def vectors(n, alphabet):
    out = []
    for v in product(alphabet, repeat=n):
        if any(v) and next(q for q in v if q) > 0:
            out.append(v)
    return out


def check():
    tests = 0
    for n in range(1, 7):
        ternary = vectors(n, (-1, 0, 1))
        ranks = Counter(sum(bool(z) for z in v) for v in ternary)
        expect = {k: comb(n, k)*2**(k-1) for k in range(1, n+1)}
        assert dict(ranks) == expect, (n, ranks, expect)
        for x, y in combinations(ternary, 2):
            assert mutual(x, y) == (not comparable(x, y)), (n, x, y)
            tests += 1
    print('ternary pair/order tests:', tests)
    tests = 0
    for n in range(1, 5):
        grid = vectors(n, (-2, -1, 0, 1, 2))
        for x, y in combinations(grid, 2):
            if mutual(x, y):
                a, b = active_round(x), active_round(y)
                assert a != b and mutual(a, b) and not comparable(a, b), (n, x, y)
                tests += 1
    print('rounding edge tests:', tests)
    tests = 0
    for n in range(1, 5):
        full = vectors(n, (-1, 1))
        counts = Counter()
        for f in full:
            for pi in permutations(range(n)):
                for k in range(1, n+1):
                    v = [0]*n
                    for i in pi[:k]:v[i] = f[i]
                    counts[(k, canonical(v))] += 1
        # All signed partial objects at a rank occur equally often.
        for k in range(1, n+1):
            counts_k = {counts[(k, x)] for x in vectors(n,(-1,0,1)) if sum(z!=0 for z in x)==k}
            assert len(counts_k)==1, (n,k,counts_k)
        tests += 1
    print('uniform-chain checks:', tests)
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
