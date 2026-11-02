#!/usr/bin/env python3
"""Exact independent finite checks for the prime-seven Lucas residue theorem."""
from collections import Counter


def square_roots_count(s: int, j: int) -> int:
    if j == 0:
        return 1
    mod = 7**j
    s %= mod
    if s == 0:
        return 7 ** (j // 2)
    v = 0
    while s % 7 == 0:
        v += 1
        s //= 7
    if v & 1 or pow(s % 7, 3, 7) != 1:
        return 0
    return 2 * 7 ** (v // 2)


def predicted_frequency(y: int, k: int) -> int:
    base = {0: 2, 1: 2, 3: 4, 4: 4, 6: 2}
    r = y % 7
    if r in base:
        return base[r]
    if k == 1:
        return 1
    if y % 49 not in (2, 47):
        return 0
    j = k - 2
    modulus = 7**j
    s = ((y*y - 4) // 49) * pow(5, -1, modulus) % modulus if modulus > 1 else 0
    return 7 * square_roots_count(s, j)


def square_residue_count(j: int) -> int:
    return 1 + sum(3 * 7 ** (j - 2*h - 1) for h in range((j + 1)//2))


def matmul(a, b, m):
    return ((a[0]*b[0]+a[1]*b[2])%m,
            (a[0]*b[1]+a[1]*b[3])%m,
            (a[2]*b[0]+a[3]*b[2])%m,
            (a[2]*b[1]+a[3]*b[3])%m)


def matrix_power(e, m):
    a=(1,1,1,0)
    out=(1,0,0,1)
    while e:
        if e & 1: out=matmul(out,a,m)
        a=matmul(a,a,m)
        e>>=1
    return out


def check():
    assert matrix_power(16, 7) == (1,0,0,1)
    assert matrix_power(8, 7) != (1,0,0,1)
    raw_m16=(1597,987,987,610)
    assert matrix_power(16,10**9) == raw_m16
    assert tuple((v-w)//7 for v,w in zip(raw_m16,(1,0,0,1))) == (228,141,141,87)
    total_fibers=0
    for k in range(1,7):
        m=7**k
        period=16*7**(k-1)
        counts=[0]*m
        a,b=2,1
        for _ in range(period):
            counts[a]+=1
            a,b=b,(a+b)%m
        assert (a,b)==(2,1),('period not closed',k)
        assert matrix_power(period,m)==(1,0,0,1)
        for prime in (2,7):
            if period%prime == 0:
                assert matrix_power(period//prime,m)!=(1,0,0,1),('period reducible',k,prime)
        for y in range(m):
            c=predicted_frequency(y,k)
            assert counts[y]==c,('frequency mismatch',k,y,counts[y],c)
        distinct=sum(x>0 for x in counts)
        expected=5*7**(k-1)+2*square_residue_count(max(0,k-2))
        assert distinct==expected,('support size',k,distinct,expected)
        hist=dict(sorted(Counter(counts).items()))
        total_fibers+=m
        print(f'LEVEL_OK k={k} modulus={m} period={period} image={distinct} histogram={hist}',flush=True)
    print(f'VERIFY_OK full_fibers={total_fibers} levels=1..6 minimal_periods_and_exact_multiplicities',flush=True)

if __name__=='__main__':
    check()
