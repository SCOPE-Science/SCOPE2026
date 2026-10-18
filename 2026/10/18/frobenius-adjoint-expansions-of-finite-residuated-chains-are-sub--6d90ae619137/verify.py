"""Finite sanity checks for subalgebra-rounding Frobenius adjoints.

Run: python3 verify_frobenius_chain.py
The all-size theorems are proved mathematically, not inferred from these tests.
"""
from itertools import product, combinations
from math import prod


def operations(n, kind):
    if kind == 'Lukasiewicz':
        return (lambda a, b: max(0, a+b-(n-1)),
                lambda a, b: min(n-1, n-1-a+b))
    if kind == 'Godel':
        return min, lambda a, b: (n-1 if a <= b else b)
    if kind == 'NilpotentMinimum':
        mul = lambda a, b: (0 if a+b <= n-1 else min(a,b))
        return mul, lambda a,b: max(c for c in range(n) if mul(a,c) <= b)
    if kind == 'Drastic':
        mul = lambda a,b: (b if a==n-1 else (a if b==n-1 else 0))
        return mul, lambda a,b: max(c for c in range(n) if mul(a,c) <= b)
    raise ValueError(kind)


def is_subalgebra(S, n, multiplication, implication):
    return (0 in S and n-1 in S and
            all(multiplication(a, b) in S and implication(a, b) in S
                for a in S for b in S))


def round_pair(S, n):
    return (tuple(max(s for s in S if s <= i) for i in range(n)),
            tuple(min(s for s in S if s >= i) for i in range(n)))


def satisfies(f, g, n, multiplication, implication):
    if any(f[i] > i for i in range(n)):
        return False
    if any((g[i] <= j) != (i <= f[j]) for i in range(n) for j in range(n)):
        return False
    for i in range(n):
        for j in range(n):
            if f[implication(g[i], j)] != implication(g[i], f[j]):
                return False
            if f[max(g[i], j)] != max(g[i], f[j]):
                return False
            if g[min(i, g[j])] != min(g[i], g[j]):
                return False
    return True


def enumerate_by_rounding(n, kind):
    mul, implication = operations(n, kind)
    solutions = set()
    for mask in range(1 << (n-2)):
        S = frozenset([0, n-1] + [i+1 for i in range(n-2) if mask & (1 << i)])
        if is_subalgebra(S, n, mul, implication):
            pair = round_pair(S, n)
            assert satisfies(*pair, n, mul, implication)
            solutions.add(pair)
    return solutions


def enumerate_by_adjoints(n, kind):
    mul, implication = operations(n, kind)
    solutions = set()
    # Any right adjoint must be increasing, and FARL1 makes it contractive.
    for f in product(*[range(i+1) for i in range(n-1)], (n-1,)):
        if any(f[i] > f[i+1] for i in range(n-1)):
            continue
        g = tuple(next(j for j in range(n) if i <= f[j]) for i in range(n))
        if satisfies(f, g, n, mul, implication):
            S = frozenset(f)
            assert S == frozenset(g)
            assert is_subalgebra(S, n, mul, implication)
            assert (f, g) == round_pair(S, n)
            solutions.add((f, g))
    return solutions


def divisor_count(n):
    return sum(n % d == 0 for d in range(1, n+1))


def check():
    counts = {}
    for kind in ('Lukasiewicz', 'Godel'):
        for n in range(2, 11):
            by_subalg = enumerate_by_rounding(n, kind)
            by_adjoints = enumerate_by_adjoints(n, kind)
            assert by_subalg == by_adjoints, (kind, n)
            expected = divisor_count(n-1) if kind == 'Lukasiewicz' else 2**(n-2)
            assert len(by_subalg) == expected, (kind, n)
            counts[(kind, n)] = len(by_subalg)
        # Larger independent closure enumeration without adjoint enumeration.
        for n in range(11, 14):
            by_subalg = enumerate_by_rounding(n, kind)
            expected = divisor_count(n-1) if kind == 'Lukasiewicz' else 2**(n-2)
            assert len(by_subalg) == expected
    # Two further finite t-norm residuated chain families, with genuine non-MV behavior.
    for kind in ('NilpotentMinimum', 'Drastic'):
        for n in range(2, 10):
            assert enumerate_by_rounding(n, kind) == enumerate_by_adjoints(n, kind)
    # Check order inclusion and both pointwise order correspondences.
    for n in range(2, 9):
        pairs = enumerate_by_rounding(n, 'Lukasiewicz')
        indexed = [(frozenset(f), f, g) for f,g in pairs]
        for S, f, g in indexed:
            for T, h, j in indexed:
                assert ((S <= T) == all(a<=b for a,b in zip(f,h)))
                assert ((S <= T) == all(a>=b for a,b in zip(g,j)))
    print('MV_COUNTS_n2_TO_n10', [counts[('Lukasiewicz',n)] for n in range(2,11)])
    print('GODEL_COUNTS_n2_TO_n10', [counts[('Godel',n)] for n in range(2,11)])
    print('FINITE_CHAIN_FROBENIUS_VERIFY_OK')


if __name__ == '__main__':
    check()
