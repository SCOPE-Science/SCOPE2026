"""Finite reproducibility checks for the affine generalized-Mobius criterion.

No finite check substitutes for the proof in RESULT.md. Python >=3.9;
standard library only. Run: python verify.py
"""
from math import comb


def mu_sieve(limit):
    out = [1] * (limit + 1)
    out[0] = 0
    primes = []
    composite = [False] * (limit + 1)
    out[1] = 1
    for i in range(2, limit + 1):
        if not composite[i]:
            primes.append(i)
            out[i] = -1
        for p in primes:
            if p * i > limit:
                break
            composite[i * p] = True
            if i % p == 0:
                out[i * p] = 0
                break
            out[i * p] = -out[i]
    return out


def values_by_divisor_recurrence(c, limit):
    # h(n)=-1-c*sum_{1<d<n,d|n}h(d), valid for f(k)=1+c(k-1).
    h = [0] * (limit + 1)
    h[1] = 1
    proper_sum = [0] * (limit + 1)
    for d in range(2, limit + 1):
        h[d] = -1 - c * proper_sum[d]
        for multiple in range(2 * d, limit + 1, d):
            proper_sum[multiple] += h[d]
    return h


def values_by_original_recurrence(c, limit):
    h = [0] * (limit + 1)
    h[1] = 1
    for n in range(2, limit + 1):
        h[n] = 1 - n - sum(h[d] * (1+c*(n // d - 1))
                              for d in range(2, n))
    return h


def squarefree_value(c, r):
    # Each j-element proper subset contributes C(r,j) times h_j.
    h = [1]
    for k in range(1, r+1):
        h.append(-1 - c*sum(comb(k, j)*h[j] for j in range(1,k)))
    return h[r]


def check():
    limit = 2500
    mu = mu_sieve(limit)
    for c in range(0, 9):
        h = values_by_divisor_recurrence(c, limit)
        direct = values_by_original_recurrence(c, 240)
        assert h[:241] == direct, (c, 'original-vs-divisor')
        if c >= 2:
            assert all((h[n]-mu[n]) % (c-1) == 0
                       for n in range(1, limit+1)), (c,'modular')
        if c >= 3:
            assert all(h[n] != -1 for n in range(4, limit+1)
                       if not is_prime(n)), (c,'composite false positive')
            assert all(h[n] == -1 for n in range(2,limit+1)
                       if is_prime(n)), (c,'prime formula')
        for r in range(1, 7):
            if prod_first_primes(r) <= limit:
                assert squarefree_value(c, r) == h[prod_first_primes(r)], (c,r)
        for a in range(1, 10):
            if 2**a <= limit:
                assert h[2**a] == -(1-c)**(a-1), (c,a)
    assert values_by_divisor_recurrence(0,40)[4] == -1
    assert values_by_divisor_recurrence(1,40)[30] == -1
    assert values_by_divisor_recurrence(2,40)[8] == -1
    print('PASS: original/divisor recurrences, modulus, prime and composite',
          'tests, squarefree layers and prime-power formulas; c=0..8, n<=2500')


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prod_first_primes(r):
    x = 1
    count = 0
    n = 2
    while count < r:
        if is_prime(n):
            x *= n
            count += 1
        n += 1
    return x

if __name__ == '__main__':
    check()
