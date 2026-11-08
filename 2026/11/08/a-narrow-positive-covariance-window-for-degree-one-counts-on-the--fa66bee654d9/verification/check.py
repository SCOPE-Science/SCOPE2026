#!/usr/bin/env python3
"""Exact finite-space verification for two-sided degree-one counts.

Only standard-library Python is required. Finite enumeration corroborates the
separately supplied all-size counting and asymptotic proof; it is not an
infinite verification certificate.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def choose(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def moments(n, k):
    N = n*n
    A = N - n
    B = (n-1)**2
    denominator = choose(N, k)
    if not denominator:
        raise ValueError('Outside the sample space')
    P = Fraction(n*choose(A, k-1), denominator)
    J = Fraction(choose(B,k-1)+B*choose(B,k-2),denominator)
    return (P, J, n*n*(J-P*P))


def complete_enumeration(n):
    totals = defaultdict(lambda: [0,0,0,0])
    row_mask = (1<<n)-1
    for mask in range(1<<(n*n)):
        k = mask.bit_count()
        rows = [(mask>>(n*i)) & row_mask for i in range(n)]
        left = sum(r.bit_count()==1 for r in rows)
        right = sum(sum((r>>j)&1 for r in rows)==1 for j in range(n))
        a = totals[k]
        a[0]+=1
        a[1]+=left
        a[2]+=right
        a[3]+=left*right
    checks=0
    for k in range(n*n+1):
        count,sl,sr,slr=totals[k]
        assert count==choose(n*n,k)
        P,J,cov=moments(n,k)
        assert Fraction(sl,count)==n*P
        assert Fraction(sr,count)==n*P
        assert Fraction(slr,count)==n*n*J
        assert Fraction(slr,count)-Fraction(sl,count)*Fraction(sr,count)==cov
        checks+=5
    return checks


def factorial_product_check():
    checks=0
    for n in range(3,26):
        A=n*n-n
        B=(n-1)**2
        for k in range(2,min(3*n,B+1)):
            P,J,_=moments(n,k)
            if P==0 or B-k+2<=0:
                continue
            factor=1+Fraction((k-1)*(k-2),k*(B-k+2))
            product=Fraction(1)
            for j in range(k-1):
                product*=1-Fraction(B,(A-j)**2)
            assert J/(P*P)==factor*product
            checks+=1
    return checks


def finite_signs():
    checks=0
    for n in range(3,81):
        assert moments(n,2*n)[2]>0
        checks+=1
        if n>=7:
            assert moments(n,n)[2]<0
            checks+=1
            assert moments(n,3*n)[2]<0
            checks+=1
    assert moments(10,20)[2]>0
    assert moments(10,5)[2]<0
    return checks+2


def main():
    checks=sum(complete_enumeration(n) for n in (2,3,4))
    checks+=factorial_product_check()
    checks+=finite_signs()
    print(f'PASS: {checks} exact assertions; complete binary matrices through 4x4.')
    print('Asymptotics are established analytically in RESULT.md, not by enumeration.')

if __name__=='__main__':
    main()
