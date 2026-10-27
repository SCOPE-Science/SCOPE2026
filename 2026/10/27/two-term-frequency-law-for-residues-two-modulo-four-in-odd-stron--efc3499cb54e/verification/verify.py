"""Exact finite checks for residue frequencies of odd strongly unimodal sequences.

Standard-library only. Finite verification supports but does not prove the
asymptotic formula.
"""
from math import isqrt


def is_prime_sieve(limit):
    a = bytearray(b'\x01') * (limit + 1)
    a[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if a[p]:
            a[p*p::p] = b'\x00' * (len(a[p*p::p]))
    return [i for i in range(2, limit+1) if a[i]]


def coeff_mod4(bound):
    """Calculate coefficients of sum_j q^(2j+1) prod_(h<j)(1+q^(2h+1))^2."""
    coeff = [0] * (bound + 1)
    prod = [0] * (bound + 1)
    prod[0] = 1
    for j in range((bound - 1) // 2 + 1):
        s = 2*j + 1
        for k in range(bound + 1 - s):
            coeff[k+s] = (coeff[k+s] + prod[k]) & 3
        nextprod = prod.copy()
        for k in range(bound + 1 - s):
            nextprod[k+s] = (nextprod[k+s] + 2*prod[k]) & 3
        for k in range(bound + 1 - 2*s):
            nextprod[k+2*s] = (nextprod[k+2*s] + prod[k]) & 3
        prod = nextprod
    return coeff


def classify(n):
    """Published characterization, applied to odd positive n."""
    assert n >= 1 and n % 2 == 1
    v = 3*n - 1
    if v % 2 == 0 and isqrt(v//2)**2 == v//2:
        return 'odd'
    r = v
    p = 2
    candidate = 0
    while p*p <= r:
        if r % p == 0:
            e = 0
            while r % p == 0:
                r //= p
                e += 1
            if p != 2 and e % 2 == 1:
                if e % 4 != 1 or p % 8 not in (5, 7) or candidate:
                    return 'zero'
                candidate = p
        p += 1 if p == 2 else 2
    if r > 1:
        if r % 8 not in (5, 7) or candidate:
            return 'zero'
        candidate = r
    return 'two' if candidate else 'zero'


def count_by_prime_param(X):
    """Distinct unique prime-exponent representations, two parity branches."""
    lim = 3*X - 1
    count = [0, 0]
    for p in is_prime_sieve(lim):
        if p % 24 not in (5, 23, 7, 13):
            continue
        y = p
        while y <= lim:
            eps = 1 if p % 24 in (5, 23) else 2
            if eps * y > lim:
                break
            bound = isqrt(lim // (eps*y))
            for m in range(1, bound + 1):
                if (eps == 1 and m % 2) or m % 3 == 0 or m % p == 0:
                    continue
                count[eps-1] += 1
            y *= p**4
    return tuple(count)


def main():
    bound = 2500
    coeff = coeff_mod4(bound)
    for n in range(1, bound + 1, 2):
        v = coeff[n]
        t = classify(n)
        assert (v % 2 == 1) == (t == 'odd'), (n, v, t)
        assert (v == 2) == (t == 'two'), (n, v, t)
        assert (v == 0) == (t == 'zero'), (n, v, t)
    print('COEFFICIENT_CLASSIFICATION_OK', (bound+1)//2, 'odd indices')
    for X in [100, 1000, 10000, 100000]:
        count = count_by_prime_param(X)
        if X <= 10000:
            direct = sum(classify(n) == 'two' for n in range(1, X + 1, 2))
            assert sum(count) == direct, (X, count, direct)
        print('EXACT_COUNTS', X, *count, sum(count))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
