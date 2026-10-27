#!/usr/bin/env python3
"""Independent finite checks for one-marker DFA separation.

Public-domain style standalone script, requiring only Python 3 stdlib.
An exhaustive search over every zero-transition map and every possible
one-transition response at the two reached states is exact for each finite
state budget tested. Separate brute-force transition-table tests avoid
relying solely on the symbolic simplification.
"""
from itertools import product
from math import lcm


def nondivisor(d):
    p = 2
    while d % p == 0:
        p += 1
    return p


def formula(n, i, j):
    assert 0 <= i < j < n
    return min(nondivisor(j-i), i+3, n+1-j)


def values(f, length):
    m = len(f)
    powers = [tuple(range(m))]
    for _ in range(length):
        last = powers[-1]
        powers.append(tuple(f[last[s]] for s in range(m)))
    return powers


def exists_for_k(k, n, i, j):
    d = j-i
    r = n-1-j
    for f in product(range(k), repeat=k):
        v = values(f, n)
        q, t = v[i][0], v[j][0]
        if q == t:
            if any(v[r+d][s] != v[r][s] for s in range(k)):
                return True
        else:
            if len(set(v[r+d]) | set(v[r])) > 1:
                return True
    return False


def brute(k, n, i, j):
    x = '0'*i + '1' + '0'*(n-i-1)
    y = '0'*j + '1' + '0'*(n-j-1)
    for f in product(range(k), repeat=k):
        for g in product(range(k), repeat=k):
            def endpoint(word):
                s = 0
                for c in word:
                    s = f[s] if c == '0' else g[s]
                return s
            if endpoint(x) != endpoint(y):
                return True
    return False


def check():
    g_cases = 0
    for n in range(2, 10):
        for i in range(n):
            for j in range(i+1, n):
                z = formula(n, i, j)
                for k in range(1, min(z+1, 4)):
                    assert brute(k,n,i,j) == (k >= z), (n,i,j,k,z)
                    g_cases += 1
    f_cases = 0
    for n in range(2, 29):
        for i in range(n):
            for j in range(i+1, n):
                z = formula(n, i, j)
                for k in range(1, min(z+1, 6)):
                    assert exists_for_k(k,n,i,j) == (k >= z), (n,i,j,k,z)
                    f_cases += 1
    for n in range(2, 201):
        worst = max(formula(n,i,j) for i in range(n) for j in range(i+1,n))
        k = 2
        while n >= lcm(*range(1,k)) + 2*k-4:
            k += 1
        assert worst == k-1, (n,worst,k)
    print('CHECK_OK full_transition_tests',g_cases,'all_zero_transition_tests',f_cases,'sharp_threshold_lengths',199)


if __name__ == '__main__':
    check()
