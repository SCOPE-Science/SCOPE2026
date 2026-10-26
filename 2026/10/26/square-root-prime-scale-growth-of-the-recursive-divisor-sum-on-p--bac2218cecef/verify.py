"""Independent finite checks of the recursive-divisor primorial identities.

Only Python's standard library is required.  No finite computation
certifies the prime-number-theorem asymptotic.
"""
from math import prod, log, log1p, sqrt, exp, fsum


def first_primes(k):
    primes = []
    n = 2
    while len(primes) < k:
        if all(n % p for p in primes if p * p <= n):
            primes.append(n)
        n += 1
    return primes


def ordered_bell(k):
    # F_j = sum_{m=0}^j m! S(j,m), computed via the first-block recursion.
    F = [1]
    from math import comb
    for n in range(1, k + 1):
        F.append(sum(comb(n, j) * F[n-j] for j in range(1, n + 1)))
    return F


def exact_polynomial_value(primes):
    # coefficients of product (p+r), in ascending powers of r
    coeffs = [1]
    for p in primes:
        out = [0] * (len(coeffs) + 1)
        for j, c in enumerate(coeffs):
            out[j] += p * c
            out[j+1] += c
        coeffs = out
    F = ordered_bell(len(primes))
    return sum(c * f for c, f in zip(coeffs, F))


def exact_recursive_value(primes):
    # All squarefree divisor values, with subset dynamic programming.
    k = len(primes)
    n = [1] * (1 << k)
    value = [1] * (1 << k)
    for mask in range(1, 1 << k):
        last = mask & -mask
        i = last.bit_length() - 1
        n[mask] = n[mask ^ last] * primes[i]
        total = n[mask]
        sub = (mask - 1) & mask
        while True:
            total += value[sub]
            if sub == 0:
                break
            sub = (sub - 1) & mask
        value[mask] = total
    return value[-1]


def simple_sieve(limit):
    a = bytearray(b'\x01') * (limit + 1)
    a[:2] = b'\x00\x00'
    for p in range(2, int(limit ** 0.5) + 1):
        if a[p]:
            a[p*p:limit+1:p] = b'\x00' * (((limit-p*p)//p)+1)
    return [i for i in range(2, limit+1) if a[i]]


def saddle_diagnostics(x):
    ps = simple_sieve(x)
    upper = int(3 * sqrt(x)) + 5
    best = (-1.0e99, -1)
    for r in range(upper + 1):
        val = fsum(log1p(r/p) for p in ps) - r * log(2)
        if val > best[0]:
            best = (val, r)
    h, r = best
    return (r, h, h * log(x) / sqrt(x))


def main():
    for k in range(1, 11):
        ps = first_primes(k)
        rec = exact_recursive_value(ps)
        pol = exact_polynomial_value(ps)
        assert rec == pol, (k, rec, pol)
        print('exact',k,ps[-1],rec)
    for x in (101, 503, 2003, 10007, 50021):
        r, h, ratio = saddle_diagnostics(x)
        assert h > 0
        print('saddle',x,r,round(r / sqrt(x),4),round(h,4),round(ratio,4))
    print('Finite checks passed; no asymptotic is certified numerically.')


if __name__ == '__main__':
    main()
