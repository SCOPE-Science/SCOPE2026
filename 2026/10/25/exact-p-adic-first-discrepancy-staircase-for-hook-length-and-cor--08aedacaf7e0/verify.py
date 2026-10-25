#!/usr/bin/env python3
"""Exact finite checks for hook-length/t-core congruence thresholds."""
from math import comb


def divisor_sums(N):
    s = [0] * (N + 1)
    for d in range(1, N + 1):
        for j in range(d, N + 1, d):
            s[j] += d
    return s


def euler_power_coefficients(E, N, sigma):
    # (q;q)_infinity^E; n*c[n] = -E*sum_{k=1}^n sigma(k)*c[n-k].
    c = [0] * (N + 1)
    c[0] = 1
    for n in range(1, N + 1):
        numerator = -E * sum(sigma[j] * c[n-j] for j in range(1, n+1))
        assert numerator % n == 0
        c[n] = numerator // n
    return c


def direct_euler_power(E, N):
    # Independently multiply the finite Euler factors, truncated at degree N.
    a = [0] * (N + 1)
    a[0] = 1
    for m in range(1, N + 1):
        b = [0] * (N + 1)
        for k in range(N // m + 1):
            if k > E:
                break
            z = (-1 if k & 1 else 1) * comb(E, k)
            for n in range(N - m*k + 1):
                b[n + m*k] += z * a[n]
        a = b
    return a


def vp(z, p):
    if z == 0:
        return 10**9
    v = 0
    while z % p == 0:
        z //= p
        v += 1
    return v


def test(p, a):
    t = p**a
    N = max(t * 2, 16)
    sigma = divisor_sums(N)
    f = euler_power_coefficients(t*t-1, N, sigma)
    u = euler_power_coefficients(t, N//t, sigma)
    partition = euler_power_coefficients(-1, N, sigma)
    core = [sum(partition[n-t*j] * u[j] for j in range(n//t+1)) for n in range(N+1)]
    dif = [f[n]-core[n] for n in range(N+1)]
    if t <= 9:
        direct_f = direct_euler_power(t*t-1, min(N, 20))
        assert f[:len(direct_f)] == direct_f
    # The uniform congruence is tested on the full truncation.
    assert all(z % p**(a+1) == 0 for z in dif)
    for j in range(a):
        n = p**j
        exp = 2*a-j
        assert dif[n] % p**(exp+1) == (-p**exp) % p**(exp+1), (p, a, j, dif[n])
        assert all(dif[k] % p**(exp+1) == 0 for k in range(n)), (p,a,j)
    for r in range(1, 2*a+4):
        candidates = [n for n in range(1, N+1) if dif[n] % p**r != 0]
        first = candidates[0] if candidates else None
        predicted = None if r <= a+1 else p**max(0, 2*a-r+1)
        assert first == predicted, (p,a,r,first,predicted)
    return N * (2*a+3)


def main():
    cases = [(2,a) for a in range(1,6)] + [(3,a) for a in range(1,5)] + [(5,a) for a in range(1,4)] + [(7,a) for a in range(1,3)]
    for p,a in cases:
        test(p,a)
    print('VERIFY_OK', len(cases), 'parameter cases')


if __name__ == '__main__':
    main()
