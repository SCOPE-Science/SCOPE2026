#!/usr/bin/env python3
"""Exact integer-arithmetic checks of odd-support mex of all overpartitions."""
from math import isqrt


def overpartition_coefficients(N, modulus=8):
    a = [1] + [0] * N
    for m in range(1, N+1):
        b = a[:]
        for n in range(m,N+1):
            b[n] = (a[n] + a[n-m] + b[n-m]) % modulus
        a = b
    return a


def excluded(a, m, modulus=8):
    b = a[:]
    for n in range(m,len(a)):
        b[n] = (a[n] - a[n-m] - b[n-m]) % modulus
    return b


def from_excluded_to_present(a, m, modulus=8):
    b = [0] * len(a)
    for n in range(m,len(a)):
        b[n] = (2*a[n-m] + b[n-m]) % modulus
    return b


def complete_sector_coefficients(N, modulus=8):
    p = overpartition_coefficients(N, modulus)
    sector = excluded(p, 1, modulus)
    out = [0] * (N+1)
    for j in range(isqrt(N)+1):
        for n in range(N+1):
            out[n] = (out[n]+(2*j+1)*sector[n])%modulus
        if (j+1)**2>N:
            break
        # Existing factor (1-q^(2j+1))/(1+q^(2j+1)) is removed,
        # and the odd part becomes present, then the next odd part absent.
        sector = from_excluded_to_present(sector,2*j+1,modulus)
        sector = excluded(sector,2*j+3,modulus)
    return p,out


def partitions(n,largest=None):
    if n == 0:
        yield ()
        return
    if largest is None:
        largest=n
    for t in range(min(n,largest),0,-1):
        for rest in partitions(n-t,t):
            yield (t,)+rest


def brute(n):
    total=0
    pbar=0
    for pi in partitions(n):
        d=len(set(pi))
        mult=1<<d
        missing=1
        while missing in pi:
            missing += 2
        total += missing*mult
        pbar += mult
    return pbar,total


def expected(n):
    if n==0:return 1
    r=isqrt(n)
    if r*r==n:return 6 if r%2 else 2
    s=isqrt(n//2)
    if n%2==0 and 2*s*s==n:return 0
    return 4


def run():
    N=1024
    p,f=complete_sector_coefficients(N,16)
    for n in range(N+1):
        if n:
            z=n-1
            mod16=(p[n]+4+8*(isqrt(z)-z-z//3))%16
            assert f[n] == mod16,(n,'theorem mod16',f[n],mod16)
        else:
            assert f[n]==p[n]==1
        assert f[n]%8==expected(n),(n,'mod8 classification',f[n],expected(n))
    for n in range(0,24):
        pbar,score=brute(n)
        assert (pbar%16,score%16)==(p[n],f[n]),(n,pbar,score,p[n],f[n])
    print('VERIFY_OK mod16_all_coefficients=1025 independent_partition_support_enumerations=24 mod8_square_twice_square=yes')

if __name__=='__main__':run()
