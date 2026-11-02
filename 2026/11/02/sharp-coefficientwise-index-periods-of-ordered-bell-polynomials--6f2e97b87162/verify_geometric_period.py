"""Exact finite checks of modular polynomial periods of ordered-Bell polynomials.

Run with Python 3.8+: python verify_geometric_period.py
All comparisons are integer arithmetic; the universal proof is separate.
"""
from math import factorial, gcd, lcm, comb

def factor(n):
    d, out = 2, []
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            out.append((d, a))
        d += 1
    if n > 1:
        out.append((n, 1))
    return out

def lam(m):
    z = 1
    for p, r in factor(m):
        local = (1 if r == 1 else 2 if r == 2 else 2 ** (r-2)) if p == 2 else (p-1)*p**(r-1)
        z = lcm(z, local)
    return z

def coefficients_upto(m, N):
    K = 1
    while factorial(K) % m:
        K += 1
    a = [0] * K
    a[0] = 1
    out = [tuple(factorial(k) * a[k] % m for k in range(K))]
    for n in range(1, N + 1):
        old = a
        a = [0] + [(k*old[k] + old[k-1]) % m for k in range(1, K)]
        out.append(tuple(factorial(k)*a[k] % m for k in range(K)))
    return out

def validate():
    checked = periods = sharp_pre = 0
    for m in range(2, 101):
        R = max(a for p, a in factor(m))
        L = lam(m)
        N = max(3*L + R + 10, 45)
        vals = coefficients_upto(m, N)
        for n in range(R, N-L+1):
            assert vals[n] == vals[n+L], (m, n, 'period')
            periods += 1
        for T in range(1, L):
            assert any(vals[n] != vals[n+T] for n in range(R, R+L)), (m, T, 'minimal period')
        for T in range(1, L+1):
            assert vals[R-1] != vals[R-1+T], (m, T, 'preperiod')
        sharp_pre += 1
        checked += 1
    direct = 0
    for n in range(0, 35):
        for k in range(0, n+1):
            c = sum((-1)**(k-j)*comb(k, j)*(j**n if j or n else 1) for j in range(k+1))
            # 0^0=1 makes c=0 for n=0 and k>0, c=1 at k=0.
            a = [0]*(k+1)
            a[0] = 1
            for _ in range(n):
                a = [0]+[j*a[j]+a[j-1] for j in range(1, k+1)]
            assert c == factorial(k)*a[k], (n,k,c,factorial(k)*a[k])
            direct += 1
    print('VERIFY_OK moduli=%d period_pairs=%d minimal_preperiod_checks=%d independent_coefficient_identities=%d' % (checked, periods, sharp_pre, direct))
if __name__ == '__main__':
    validate()
