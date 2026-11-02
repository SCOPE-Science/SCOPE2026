"""Reproduce the exact descent--leaf laws for uniform tree permutations.

Requires only the Python standard library. All checks use exact integer or
rational arithmetic; finite enumeration supplements, not replaces, proof.
"""
import itertools
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def construct(bits):
    p = [2, 1]
    for value, b in enumerate(bits, 3):
        if b:
            p.insert(-1, value)
        else:
            p = [value if t == value - 1 else t for t in p] + [value - 1]
    return tuple(p)


def summary(p):
    n = len(p)
    descents = sum(p[i] > p[i + 1] for i in range(n - 1))
    degree = [0] * n
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                degree[i] += 1
                degree[j] += 1
                edges.append((i, j))
    return descents, sum(d == 1 for d in degree), edges


def is_tree(p):
    n = len(p)
    _, _, edges = summary(p)
    if len(edges) != n - 1:
        return False
    group = list(range(n))

    def root(x):
        while group[x] != x:
            x = group[x]
        return x

    for i, j in edges:
        group[root(i)] = root(j)
    return len({root(i) for i in range(n)}) == 1


def expected_pair_counts(n):
    m = n - 2
    expected = Counter()
    for t in range(m):
        ways = comb(m - 1, t)
        leaves = n - 1 - t
        if t % 2 == 0:
            expected[(1 + t // 2, leaves)] += 2 * ways
        else:
            expected[(1 + t // 2, leaves)] += ways
            expected[(2 + t // 2, leaves)] += ways
    return expected


def verify():
    checks = 0
    exhaustive_trees = 0
    coded_permutations = 0
    for n in range(3, 14):
        pair_counts = Counter()
        m = n - 2
        for bits in itertools.product((0, 1), repeat=m):
            p = construct(bits)
            d, l, _ = summary(p)
            transition_count = sum(bits[j - 1] != bits[j] for j in range(1, m))
            transitions_01 = sum(bits[j - 1] == 0 and bits[j] == 1 for j in range(1, m))
            assert l == n - 1 - transition_count
            checks += 1
            assert d == 1 + transitions_01
            checks += 1
            assert 2 * d + l - n - 1 == bits[-1] - bits[0]
            checks += 1
            assert is_tree(p)
            checks += 1
            pair_counts[(d, l)] += 1
            coded_permutations += 1
        assert pair_counts == expected_pair_counts(n)
        checks += 1
        assert sum(pair_counts.values()) == 2**m
        checks += 1
        for d in set(a for a, _ in pair_counts):
            assert sum(c for (a, _), c in pair_counts.items() if a == d) == comb(n-1, 2*d-1)
            checks += 1
        N = 2**m
        E_D = sum(Fraction(a*c, N) for (a, b), c in pair_counts.items())
        E_L = sum(Fraction(b*c, N) for (a, b), c in pair_counts.items())
        assert E_D == Fraction(n+1, 4)
        assert E_L == Fraction(n+1, 2)
        checks += 2
        Var_L = sum(Fraction((b-E_L)**2 * c, N) for (a,b),c in pair_counts.items())
        cov = sum(Fraction((a-E_D)*(b-E_L)*c,N) for (a,b),c in pair_counts.items())
        assert Var_L == Fraction(n-3,4)
        assert cov == Fraction(-(n-3),8)
        checks += 2
        if n >= 4:
            Var_D = sum(Fraction((a-E_D)**2*c,N) for (a,b),c in pair_counts.items())
            assert Var_D == Fraction(n-1,16)
            checks += 1
        # Independent brute-force check of tree-permutation membership.
        if n <= 8:
            brute = {p for p in itertools.permutations(range(1,n+1)) if is_tree(p)}
            generated = {construct(b) for b in itertools.product((0,1), repeat=m)}
            assert brute == generated
            checks += 1
            exhaustive_trees += len(brute)
    print('PASS',checks,'exact assertions;',coded_permutations,'coded trees;',
          exhaustive_trees,'independently brute-classified trees')


if __name__ == '__main__':
    verify()
