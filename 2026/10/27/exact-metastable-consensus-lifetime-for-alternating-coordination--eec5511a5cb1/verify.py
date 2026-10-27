#!/usr/bin/env python3
"""Exact finite-state checks for a switched two-game best-response chain.

Standard library only. Run: python3 verify.py
The infinite-population exponential rate is proved analytically in RESULT.md,
not certified by this finite program.
"""
from fractions import Fraction as Q
from math import comb, log

checks = 0

def test(ok, message='failed'):
    global checks
    assert ok, message
    checks += 1

def rates(n, e):
    p = [Q(0)] * (n + 1)
    q = [Q(0)] * (n + 1)
    for k in range(1, n):
        x_B = Q(k, n - 1)
        x_A = Q(k - 1, n - 1)
        test(x_B != e and x_B != 1-e and x_A != e and x_A != 1-e,
             'tie would make model underdetermined')
        u = Q(0) if x_B < e else (Q(1) if x_B > 1-e else Q(1, 2))
        d = Q(1) if x_A < e else (Q(0) if x_A > 1-e else Q(1, 2))
        p[k] = Q(n - k, n) * u
        q[k] = Q(k, n) * d
    return p, q

def exact_formula(n, e):
    assert n % 2 == 0 and 0 < e < Q(1, 2)
    r = n // 2
    z = e * (n - 1)
    test(z.denominator != 1, 'tie at one threshold')
    m = z.numerator // z.denominator
    test(0 <= m <= r - 2, 'outside finite formula range')
    d = {}
    for k in range(m + 2, r + 1):
        total = sum((Q(comb(n, j)) for j in range(k, r)), Q(comb(n, r), 2))
        d[k] = Q(2 * n, k * comb(n, k)) * total
    d[m + 1] = Q(n, m + 1) + Q(n - m - 1, 2 * (m + 1)) * d[m + 2]
    t = sum((Q(n, j) for j in range(1, m + 1)), Q(0)) + sum(d.values(), Q(0))
    return m, t, d

def verify(n, e, micro=False):
    m, t, d = exact_formula(n, e)
    p, q = rates(n, e)
    r = n // 2
    u = [Q(0)] * (n + 1)
    for k in range(1, m + 1):
        u[k] = u[k - 1] + Q(n, k)
    for k in range(m + 1, r + 1):
        u[k] = u[k - 1] + d[k]
    for k in range(r + 1, n):
        u[k] = u[n-k]
    test(u[r] == t, 'closed formula vs reconstructed values')
    for k in range(n+1):
        test(p[k] == q[n-k], 'spin reversal symmetry')
    for k in range(1, n):
        test(0 <= p[k] <= 1 and 0 <= q[k] <= 1 and p[k]+q[k] <= 1)
        test(p[k] * (u[k+1] - u[k]) + q[k] * (u[k-1] - u[k]) == -1,
             'independent one-step expectation identity')
    for k in range(m+1):
        test(p[k] == 0, 'left absorbing corridor')
    for k in range(n-m, n+1):
        test(q[k] == 0, 'right absorbing corridor')
    if micro:
        for mask in range(1 << n):
            k = mask.bit_count()
            up = Q(0); down = Q(0)
            for focal in range(n):
                state = (mask >> focal) & 1
                n_A = k-state
                for game_threshold in (e, 1-e):
                    expected_A = n_A*game_threshold.denominator > (n-1)*game_threshold.numerator
                    # no tie in cases selected for the check
                    if state == 0 and expected_A:
                        up += Q(1, 2*n)
                    if state == 1 and not expected_A:
                        down += Q(1, 2*n)
            test(up == p[k] and down == q[k], 'individual-game update vs count chain')
    return m, t

if __name__ == '__main__':
    for den, num in ((5,1),(7,1),(7,2),(9,2),(9,3)):
        e = Q(num,den)
        for n in range(4,46,2):
            z=e*(n-1)
            m=z.numerator//z.denominator
            if z.denominator == 1 or m>n//2-2: continue
            verify(n,e,micro=(n<=10))
    m,t=verify(20,Q(1,5))
    test(m == 3 and t == Q(20759,21), 'reference exact value')
    print(f'CERTIFICATE_OK {checks} exact rational assertions')
    print('n=20, threshold=1/5, consensus-time expectation=',t)
    print('entropy exponent at threshold=1/5 =',
          log(2)+.2*log(.2)+.8*log(.8))
