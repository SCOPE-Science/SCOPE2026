#!/usr/bin/env python3
"""Exact checks for the ladder fort-support theorem (Python 3 + SymPy).

Run: python3 verify.py
The symbolic identity is exact; finite enumeration is an independent cross-check.
"""
from collections import defaultdict
from math import ceil
import sympy as sp


def flip(x):
    return ((x & 1) << 1) | ((x & 2) >> 1)


def allowed(a, b, c):
    for bit in (1, 2):
        if not b & bit:
            k = int(bool(a & bit)) + int(bool(c & bit)) + int(bool(b & (3 ^ bit)))
            if k == 1:
                return False
    return True


def pop(x):
    return x.bit_count()


def direct(n):
    result = defaultdict(int)
    for mask in range(1 << (2 * n)):
        # Indexing by (column, row), independently checking graph neighbors.
        support = lambda col, row: bool(mask & (1 << (2 * col + row)))
        valid = True
        for col in range(n):
            for row in (0, 1):
                if support(col, row):
                    continue
                count = int(support(col, 1 - row))
                if col:
                    count += int(support(col - 1, row))
                if col < n - 1:
                    count += int(support(col + 1, row))
                if count == 1:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            result[mask.bit_count()] += 1
    return dict(result)


def transfer_count(n):
    if n == 0:
        return {0: 1}
    dp = {(0, 0): 1}  # previous column, cardinality
    for col in range(n):
        if col == 0:
            dp = {(b, pop(b)): 1 for b in range(4)}
            continue
        raise RuntimeError('not used')


def size_profile(n):
    if n == 0:
        return {0: 1}
    dp = defaultdict(int)
    # The first two columns, with a virtual empty predecessor.
    if n == 1:
        return {0: 1, 2: 1}
    for b in range(4):
        for c in range(4):
            if allowed(0, b, c):
                dp[(b, c, pop(b) + pop(c))] += 1
    for _ in range(2, n):
        nxt = defaultdict(int)
        for (a, b, size), qty in dp.items():
            for c in range(4):
                if allowed(a, b, c):
                    nxt[(b, c, size + pop(c))] += qty
        dp = nxt
    ans = defaultdict(int)
    for (a, b, size), qty in dp.items():
        if allowed(a, b, 0):
            ans[size] += qty
    return dict(ans)


def minimum(n):
    d = (2 * (n + 1) + 2) // 3
    if n == 1:
        return d, 1
    k, r = divmod(n, 3)
    count = (2 * k if r == 0 else k * (k + 3) if r == 1 else 2)
    return d, count


def symbolic():
    t, z, q = sp.symbols('t z q')
    P = (1 - t*z - t**2*z**2 + 2*t**2*z**3 - 3*t**3*z**2
         - 2*t**3*z**3 - 4*t**4*z**4 + 4*t**5*z**4)
    Q = (1 - t*z - t*z**2 - 2*t**2*z**2 - t**2*z**3
         - t**3*z**2 + t**3*z**3 - t**3*z**4 + t**5*z**4)
    expected = P / ((1 - t) * Q)

    reps = sorted({min((a, b), (flip(a), flip(b)))
                   for a in range(4) for b in range(4)})
    assert len(reps) == 10
    ix = {pair: i for i, pair in enumerate(reps)}
    M = sp.zeros(10)
    w = sp.zeros(10, 1)
    for (a, b), i in ix.items():
        w[i] = int(allowed(a, b, 0))
        for c in range(4):
            if allowed(a, b, c):
                target = min((b, c), (flip(b), flip(c)))
                M[i, ix[target]] += z**pop(c)
    f = (sp.eye(10) - t*M).inv() * w
    actual = 1 + t * sum(z**pop(b) * f[ix[min((0, b), (0, flip(b)))]]
                         for b in range(4))
    assert sp.cancel(actual - expected) == 0, 'transfer/closed rational identity'

    # Remove the all-zero word, then convert size to nonnegative slack
    # s=3*size-2*(n+1).
    H = sp.cancel((expected.subs({t: t/q**2, z: q**3})
                   - 1/(1-t/q**2))/q**2)
    Hr = t * (2*t + q**2 - 3*q**2*t**3 + 3*q**3*t + q**4*t**2) / (
        1 - t**3 - q*t - 2*q**2*t**2 + q**2*t**5 + q**3*t**3
        - q**4*t - q**5*t**2 - q**6*t**3)
    assert sp.cancel(H-Hr) == 0, 'slack rational identity'
    expected_low = [2*t**2/(1-t**3),
                    2*t**3/(1-t**3)**2,
                    t*(1+t**3+t**6-t**9)/(1-t**3)**3]
    for j in range(3):
        actual_low = sp.diff(H, q, j).subs(q, 0)/sp.factorial(j)
        assert sp.cancel(actual_low - expected_low[j]) == 0, f'slack degree {j}'
    return P, Q


def main():
    P, Q = symbolic()
    examined = 0
    for n in range(1, 9):
        direct_profile = direct(n)
        profile = size_profile(n)
        assert profile == direct_profile, (n, profile, direct_profile)
        examined += 1 << (2*n)
    for n in range(1, 45):
        profile = size_profile(n)
        positive = sorted(size for size, qty in profile.items() if size > 0 and qty > 0)
        d, c = minimum(n)
        assert positive[0] == d and profile[d] == c, (n, positive[0], profile[d], d, c)
    print('VERIFY_OK transfer_states=10 exact_rational_identities=5 '
          f'direct_supports={examined} direct_lengths=1..8 '
          'minimum_profile_lengths=1..44')


if __name__ == '__main__':
    main()
