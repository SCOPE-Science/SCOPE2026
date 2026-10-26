"""Exact checks of the conditional cycle-count law at marked permutation records.
This script is standalone and needs only the Python standard library.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb, factorial


def cycles(p):
    n = len(p)
    seen = [False] * n
    c = 0
    for start in range(n):
        if seen[start]:
            continue
        c += 1
        j = start
        while not seen[j]:
            seen[j] = True
            j = p[j] - 1
    return c


def poly_mul(a, b):
    z = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            z[i+j] += u*v
    return z


@lru_cache(None)
def cycle_pgf(n):
    f = [Fraction(1)]
    for m in range(1,n+1):
        f = poly_mul(f, [Fraction(m-1,m), Fraction(1,m)])
    return tuple(f)


@lru_cache(None)
def expected_conditional(n, i):
    g = cycle_pgf(n)
    t = poly_mul(cycle_pgf(i-1), cycle_pgf(n-i))
    eps = Fraction(i-1, i*comb(n,i))
    delta = poly_mul(t, [Fraction(-1), Fraction(1)])
    return tuple(g[j] + eps*(delta[j] if j < len(delta) else 0)
            for j in range(n+1))


def test_exhaustive(n):
    total = Counter()
    rec = [Counter() for _ in range(n)]
    rec_count = [0] * n
    for p in permutations(range(1,n+1)):
        k = cycles(p)
        total[k] += 1
        maximum = 0
        for i, x in enumerate(p):
            if x > maximum:
                maximum = x
                rec[i][k] += 1
                rec_count[i] += 1
    N = factorial(n)
    assert sum(total.values()) == N
    G = cycle_pgf(n)
    assert all(G[k] == Fraction(total[k],N) for k in range(n+1))
    for i in range(1,n+1):
        assert rec_count[i-1] == N//i
        exact = expected_conditional(n,i)
        assert all(exact[k] == Fraction(rec[i-1][k], rec_count[i-1])
                   for k in range(n+1)), (n,i,exact,rec[i-1])
        eps = Fraction(i-1,i*comb(n,i))
        distribution_T = poly_mul(cycle_pgf(i-1), cycle_pgf(n-i))
        for k in range(n+2):
            tail_diff = sum(exact[j]-G[j] for j in range(k,n+1))
            rhs = eps*(distribution_T[k-1] if 0 <= k-1<len(distribution_T) else 0)
            assert tail_diff == rhs, (n,i,k,tail_diff,rhs)
        expected_cov = Fraction(i-1,i*i*comb(n,i))
        mu_C = sum(k*G[k] for k in range(n+1))
        mu_RecC = sum(k*Fraction(rec[i-1][k],N) for k in range(n+1))
        assert mu_RecC - mu_C/Fraction(i) == expected_cov
    print(f'EXHAUSTIVE_PASS n={n} permutations={N} marked_positions={n}')


def test_recurrence(limit):
    for n in range(1,limit+1):
        G_n = cycle_pgf(n)
        assert sum(G_n) == 1
        for i in range(1,n+1):
            a = expected_conditional(n,i)
            assert all(x>=0 for x in a)
            assert sum(a) == 1
            if i == n:
                assert a == (Fraction(0),) + cycle_pgf(n-1)
            else:
                old = expected_conditional(n-1,i)
                predicted = [Fraction(0)]*(n+1)
                for k in range(n+1):
                    old_k = old[k] if k < len(old) else 0
                    old_prev = old[k-1] if 0<=k-1<len(old) else 0
                    predicted[k] = Fraction(i,n)*cycle_pgf(n-1)[k] if k < n else Fraction(0)
                    predicted[k] += Fraction(n-i-1,n)*old_k + Fraction(1,n)*old_prev
                assert tuple(predicted) == a, (n,i)
    print(f'EXACT_PGF_RECURRENCE_PASS n<= {limit}')


if __name__ == '__main__':
    for n in range(1,9):
        test_exhaustive(n)
    test_recurrence(35)
    print('VERIFY_OK')
