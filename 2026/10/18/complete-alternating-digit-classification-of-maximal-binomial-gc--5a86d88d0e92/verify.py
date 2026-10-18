"""Exact finite checks for the two-digit extremal-row theorem.

All valuations are computed from base-p residues (Kummer's theorem); an
independent factorial-valuation identity cross-checks selected instances.
"""
from math import comb

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]

def vp_factorial(n, p):
    v = 0
    while n:
        n //= p
        v += n
    return v

def valuation_legendre(n, k, p):
    return vp_factorial(n, p)-vp_factorial(k, p)-vp_factorial(n-k, p)

def valuation_borrow(n, k, p):
    v, mod = 0, p
    while mod <= n:
        v += (k % mod) > (n % mod)
        mod *= p
    return v

def two_unit_opposite(n, p):
    positions = []
    index = 0
    while n:
        n, digit = divmod(n, p)
        if digit == 1:
            positions.append(index)
        elif digit > 1:
            return False
        index += 1
    return len(positions) == 2 and ((positions[0] - positions[1]) & 1) == 1

def trial(p, N):
    assert N % (p+1) == 0 and N > p+1
    m = p+1
    dmax = N // m
    vs = [valuation_borrow(N, m*d, p) for d in range(1, dmax)]
    actual = min(vs)
    expected = 2 if two_unit_opposite(N, p) else actual < 2
    if two_unit_opposite(N, p):
        assert actual == 2, (p, N, actual)
    else:
        assert actual <= 1, (p, N, actual)
    return dmax - 1

if __name__ == '__main__':
    rows, samples = 0, 0
    for p in PRIMES:
        m = p+1
        for N in range(2*m, 1201, m):
            samples += trial(p,N)
            rows += 1
    cross = 0
    for p in PRIMES:
        m = p+1
        for N in range(2*m, 180, m):
            for k in range(m,N,m):
                assert valuation_borrow(N,k,p) == valuation_legendre(N,k,p)
                cross += 1
    # sparse instances beyond the contiguous test interval
    for p in PRIMES:
        for a,b in [(0,3),(0,5),(1,4),(2,7)]:
            N = p**a+p**b
            if N <= p+1 or N > 20000:
                continue
            samples += trial(p,N)
            rows += 1
    print('VERIFY_OK', 'prime_fields',len(PRIMES),'rows',rows,
          'selected_indices',samples,'independent_legendre_checks',cross)
