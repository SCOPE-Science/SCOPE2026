#!/usr/bin/env python3
"""Exact reproducibility checks for an eighteen-fold Beatty sumset.

The finite membership scan is supplementary: the proof of nonmembership uses
an exact Pell approximation and does not depend on exhaustive enumeration.
"""
from math import isqrt

BOUND = 93041
NUMBER_OF_SUMMANDS = 18


def beatty(n):
    assert n >= 1
    return 9*n + isqrt(80*n*n)


def ceiling_theta(n):
    # theta = 9 - 4 sqrt(5), irrational for n >= 1.
    return 18*n-beatty(n)


def residue(n):
    return 323 - (18*n) % 323


def main():
    assert 2889**2 - 5*1292**2 == 1
    assert 2889 + 1292*2 > 5186  # strictly weaker certified bound sqrt(5)>2
    assert 18*18 % 323 == 1
    assert [beatty(i) for i in (5184,5185,5186,5187)] == [93023,93041,93058,93076]
    for n in range(1,5187):
        assert 323*ceiling_theta(n)==18*n+residue(n)
    assert (18*5185-BOUND)*323 -18*5185 ==17
    assert (18*5186-BOUND)*323 -18*5186 ==5813
    assert 5813 == 18*323-1
    assert 17*323+18 == 5509 > 5186
    print('EXACT_PELL_AND_REMAINDER_CHECKS_OK n=1..5186')

    values = []
    n=1
    while beatty(n)<=BOUND:
        values.append(beatty(n))
        n+=1
    mask=(1<<(BOUND+1))-1
    represented=1  # zero-term sum only
    for count in range(1,NUMBER_OF_SUMMANDS+1):
        nxt=0
        for b in values:
            nxt |= represented << b
        represented=nxt & mask
    assert ((represented >> BOUND)&1)==0
    print(f'EXACT_FINITE_SUMSET_CHECK_OK summands={NUMBER_OF_SUMMANDS} bound={BOUND} generators={len(values)}')
    print('NOTE: finitary scan alone gives no bound beyond 93041; global coverage is cited from Theorem 4.3 of Pongsriiam (2022).')

if __name__ == '__main__':
    main()
