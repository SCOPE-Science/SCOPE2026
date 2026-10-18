#!/usr/bin/env python3
"""Exact finite checks for extremal distinct-prime partitions.

No finite check certifies the asymptotic theorem; its proof uses the
ternary Goldbach count and the primorial envelope.
"""
from math import isqrt


def prime_list(bound):
    prime = bytearray(b'\x01') * (bound + 1)
    prime[0] = prime[1] = 0
    for p in range(2, isqrt(bound) + 1):
        if prime[p]:
            prime[p*p::p] = b'\x00' * ((bound-p*p)//p + 1)
    return [i for i in range(2, bound + 1) if prime[i]]


def main():
    N = 2000
    ps = prime_list(N)
    product = [-1] * (N + 1)
    products_parts = [-1] * (N + 1)
    length = [-1] * (N + 1)
    product[0] = 1
    products_parts[0] = length[0] = 0
    for p in ps:
        for x in range(N, p - 1, -1):
            if product[x-p] >= 0:
                candidate = product[x-p] * p
                if candidate > product[x]:
                    product[x] = candidate
                    products_parts[x] = products_parts[x-p] + 1
            if length[x-p] >= 0:
                length[x] = max(length[x], length[x-p] + 1)
    k = 0
    primorial = 1
    s = 0
    bounded_product = 1
    min_first_discrepancy = None
    confirmed = 0
    for n in range(1, N + 1):
        while k < len(ps) and s + ps[k] <= n:
            s += ps[k]
            primorial *= ps[k]
            k += 1
        bounded_product = max(bounded_product, product[n])
        if product[n] < 0:
            continue
        confirmed += 1
        assert length[n] <= k, (n, 'length cap')
        assert primorial <= bounded_product, (n, 'primorial floor')
        next_prime = ps[k] if k < len(ps) else None
        if next_prime is not None:
            assert bounded_product <= primorial * next_prime, (n, 'primorial ceiling')
        if length[n] > products_parts[n] and min_first_discrepancy is None:
            min_first_discrepancy = n
    assert min_first_discrepancy == 319, min_first_discrepancy
    print('VERIFY_OK finite_exact_sums=%d first_L_minus_K=%d max_n=%d' %
          (confirmed, min_first_discrepancy, N))


if __name__ == '__main__':
    main()
