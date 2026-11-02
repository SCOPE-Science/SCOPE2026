#!/usr/bin/env python3
"""Exact integer checks for the binomial-convolution valuation identity.

This finite replay is not a proof of the universally quantified result.
"""
from math import comb

N = 240
A = [comb(6*n, 3*n) * comb(3*n, n) for n in range(N+1)]


def v2(m):
    assert m > 0
    return (m & -m).bit_length()-1


def bitweight(n):
    return n.bit_count()


for n in range(N+1):
    convolution = sum(A[k] * A[n-k] for k in range(n+1))
    clausen = sum(
        (-432)**(n-k) * A[k] * comb(2*k, k) * comb(k, n-k)
        for k in range((n+1)//2, n+1)
    )
    assert convolution == clausen, (n, 'Clausen coefficient')
    if n == 0:
        assert convolution == 1
        continue
    assert v2(convolution) == 3*bitweight(n), (n, 'convolution valuation')
    divisor = (2*n-1) * comb(3*n, n)
    quotient, remainder = divmod(convolution, divisor)
    assert remainder == 0, (n, 'integral normalization')
    assert v2(quotient) == bitweight(n) + bitweight(3*n), (n, 'normalized valuation')

print(f'VERIFY_OK positive_indices={N} clausen_coefficients={N+1} normalized_quotients={N}')
