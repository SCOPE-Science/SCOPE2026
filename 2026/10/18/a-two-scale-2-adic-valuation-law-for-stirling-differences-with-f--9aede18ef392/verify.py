#!/usr/bin/env python3
"""Exact modular arithmetic checks for the fifteen-block Stirling difference law."""
from math import comb, factorial

def v2(t):
    assert t != 0
    return (abs(t) & -abs(t)).bit_length() - 1

def numerator_difference(a, b, n, precision):
    assert n >= 10 and a > b >= 1
    mod = 1 << precision
    na, nb = a * (1 << n), b * (1 << n)
    return sum(((-1) ** (15-j)) * comb(15,j) *
               (pow(j,na,mod)-pow(j,nb,mod))
               for j in range(1,16)) % mod

def verify():
    assert v2(factorial(15)) == 11
    mod = 1 << 23
    moment = sum(comb(15,j) * (pow(j,1 << 10,mod) - 1)
                 for j in range(1,16,2)) % mod
    assert moment == 1 << 22
    assert sum(comb(15,j) for j in (2,6,10,14)) == 8128
    assert 8128 % 128 == 64
    for n in (10,11,12):
        for a,b in ((2,1),(3,1),(4,1),(9,5),(64,1)):
            alpha = n + 1 + v2(a-b)
            beta = b*(1 << n)-5
            assert alpha != beta
            num = numerator_difference(a,b,n,alpha+20)
            assert v2(num) == min(alpha,beta)+11
    # Resonance: n=10, b=1, nu_2(a-b)=1008 gives alpha=beta=1019.
    n,b,c = 10,1,1 << 1008
    alpha = n+1+v2(c)
    beta = b*(1<<n)-5
    assert alpha == beta
    num = numerator_difference(b+c,b,n,alpha+19)
    assert num % (1 << (alpha+12)) == 0
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
