#!/usr/bin/env python3
"""Exact checks for gcd-subset deficits and the least-nondivisor spectrum.
No third-party packages. All integers exact.
"""
from math import gcd, lcm, comb


def relatively_prime_counts(N):
    f = [0] * (N + 1)
    for t in range(1, N + 1):
        f[t] = (1 << t) - 1 - sum(f[t // g] for g in range(2, t + 1))
        assert f[t] >= 1
    return f


def least_nondivisor(n):
    return next(d for d in range(2, n + 2) if n % d)


def least_prime_factor(n):
    return next(d for d in range(2, n + 1) if n % d == 0)


def prime_power(r):
    for p in range(2, r + 1):
        if r % p == 0:
            v = r
            while v % p == 0:
                v //= p
            return v == 1, p
    return False, None


def verify():
    N = 450
    f = relatively_prime_counts(N)
    assert f[:16] == [0, 1, 2, 5, 11, 26, 53, 116, 236, 488, 983, 2006, 4016, 8111, 16238, 32603]
    for n in range(1, 18):
        direct = 0
        for mask in range(1, 1 << n):
            g = 0
            for i in range(n):
                if mask >> i & 1:
                    g = gcd(g, i + 1)
            if g == 1:
                direct += 1
        assert direct == f[n], (n, direct, f[n])
    for n in range(3, N + 1):
        r, q = least_nondivisor(n), least_prime_factor(n)
        assert prime_power(r)[0]
        D = sum(f[d] for d in range(1, n + 1) if n % d == 0)
        Phi = sum(f[n // g] for g in range(1, n + 1) if gcd(g, n) == 1)
        delta_D, delta_Phi = (1 << n) - D, (1 << n) - Phi
        exp_D = 1 + sum(f[n // g] for g in range(1, n + 1) if n % g != 0)
        exp_Phi = 1 + sum(f[n // g] for g in range(1, n + 1) if gcd(g, n) > 1)
        assert delta_D == exp_D > 0
        assert delta_Phi == exp_Phi > 0
        t, s = n // r, n // q
        assert (1 << (t - 1)) <= delta_D <= 1 + n * (1 << t)
        assert (1 << (s - 1)) <= delta_Phi <= 1 + n * (1 << s)
        if n % 2 and n >= 5:
            assert delta_D > delta_Phi, ('odd', n)
        elif n >= 4:
            assert delta_D < delta_Phi, ('even', n)
    for r in range(2, 41):
        L = 1
        for j in range(1, r):
            L = lcm(L, j)
        is_pp, p = prime_power(r)
        if L > 300_000:
            break
        if is_pp:
            for n in range(1, min(L * (p + 2), 180_000) + 1):
                if n < r:
                    continue
                expected = (n % L == 0) and ((n // L) % p != 0)
                if expected:
                    assert least_nondivisor(n) == r, (r, n)
                elif n % L == 0 and n % r == 0:
                    assert least_nondivisor(n) > r, (r, n)
        else:
            assert all(least_nondivisor(n) != r for n in range(r, min(2000, L * 2 + 1)))
    for m in range(1, 161):
        L = 1
        for k in range(1, m + 1):
            L = lcm(L, k)
        for k in range(0, m + 1):
            assert L % comb(m, k) == 0
        assert L * (m + 1) >= 1 << m
    L60 = 60
    for r, count in [(2, 30), (3, 20), (4, 5), (5, 4)]:
        assert sum(least_nondivisor(n) == r for n in range(1, L60 + 1)) == count
    print('VERIFY_OK: exact gcd-subset formulas n<=450, brute subsets n<=17, prime-power fibers; LCM and phase masses')

if __name__ == '__main__':
    verify()
