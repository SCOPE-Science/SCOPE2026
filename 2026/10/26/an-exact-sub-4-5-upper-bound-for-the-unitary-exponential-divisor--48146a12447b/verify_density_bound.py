#!/usr/bin/env python3
"""Exact-rational certificate: upper density for unitary/exponential divisor comparison."""
from fractions import Fraction
from math import prod

PRIMES = (2, 3, 5, 7, 11, 13, 17)
K = 6
M = 10**7
C1, D1 = 71, 5000
C2, D2 = 31, 50000


def sieve(limit):
    a = bytearray(b'\x01') * (limit + 1)
    a[:2] = b'\x00\x00'
    for k in range(2, int(limit**0.5) + 1):
        if a[k]:
            a[k*k::k] = b'\x00' * len(a[k*k::k])
    return [k for k in range(2, limit + 1) if a[k]]


def ceildiv(a, b):
    return (a + b - 1) // b


def run():
    # Explicit rational prime-tail bounds, including all primes beyond 1000.
    ptail = [p for p in sieve(1000) if p > 17]
    s2 = sum((Fraction(1, p*p) for p in ptail), Fraction(1, 1000))
    s3 = sum((Fraction(1, p*p*p) for p in ptail), Fraction(1, 2*1000*1000))
    u1 = s2/(1-s2)
    u2 = (s3/(1-s3)+s2*s2)/(1-s2)**2
    assert s2 < 1 and s3 < 1
    assert u1 < Fraction(C1, D1)
    assert u2 < Fraction(C2, D2)

    opts=[]
    for p in PRIMES:
        z=[]
        for a in range(K+1):
            if a == 0:
                num,den=1,1
            else:
                num=1+p**a
                den=sum(p**d for d in range(1,a+1) if a%d==0)
            # Density (p-1)/p^(a+1) over common denominator p^(K+1).
            weight=(p-1)*p**(K-a)
            z.append((num, den, weight))
        # Exponent >= K+1: local ratio <=1 and density p^(-K-1).
        z.append((1,1,1))
        assert sum(t[2] for t in z)==p**(K+1)
        opts.append(z)

    total=0
    leaves=0
    positive_weight=0
    def recurse(i,num,den,weight):
        nonlocal total,leaves,positive_weight
        if i==len(PRIMES):
            leaves +=1
            if num>=den:
                b=M
                positive_weight+=weight
            else:
                dif=den-num
                a1=ceildiv(M*C1*num,D1*dif)
                a2=ceildiv(M*C2*num*num,D2*dif*dif)
                b=min(M,a1,a2)
            total += weight*b
            return
        for nu,de,w in opts[i]:
            recurse(i+1,num*nu,den*de,weight*w)
    recurse(0,1,1,1)
    Q=prod(p**(K+1) for p in PRIMES)
    assert leaves == 8**7
    assert total*5 < 4*Q*M, 'Failed to certify strict upper bound < 4/5.'
    print('CERTIFICATE_OK')
    print('leaf_count',leaves)
    print('common_denominator',Q)
    print('fixed_point_denominator',M)
    print('certified_upper_numerator',total)
    print('certified_upper_denominator',Q*M)
    print('certified_upper_decimal',format(total/(Q*M),'.12f'))
    print('head_ratio_ge_one_mass',positive_weight,'/',Q)
    print('tail_first_moment_bound',C1,'/',D1)
    print('tail_second_moment_bound',C2,'/',D2)
    print('strict_gap_from_4_over_5_numerator',4*Q*M-5*total)

if __name__=='__main__':
    run()
