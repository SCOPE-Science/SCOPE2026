#!/usr/bin/env python3
"""Standalone exact checks for the Pareto-maxima / northeast-count identity.
Run: python3 check_pareto_records.py (Python standard library only).
All finite checks below are exhaustive at the stated sample sizes.
"""
from itertools import permutations
from fractions import Fraction
from math import comb, factorial


def cov_conditional_a(n, a, q):
    if a == 0 or a == n:
        return Fraction(0)
    return -a * (1-q) * sum(
        (1-(1-q)**(i-1))/Fraction(i*(i-1))
        for i in range(a+1,n+1)
    )


def cov_conditional_ab(n,a,b):
    if a == 0 or a == n:
        return Fraction(0)
    def miss(i):
        return Fraction(comb(n-b,i),comb(n,i)) if i<=n-b else Fraction(0)
    return -a * sum((1-miss(i)-Fraction(b,n))/Fraction(i*(i-1))
                    for i in range(a+1,n+1))


def unconditional(n,p,q):
    return sum(Fraction(comb(n,a)) * p**a * (1-p)**(n-a)
               * cov_conditional_a(n,a,q) for a in range(n+1))


def run():
    cells=0
    for n in range(2,8):
        permlist=permutations(range(1,n+1))
        aggregate=[[ [0,0,0] for _ in range(n+1)] for _ in range(n+1)]
        for perm in permlist:
            records=0; largest=0
            for rank in perm:
                if rank>largest:records+=1;largest=rank
            k=[0]*(n+1)
            for b in range(n+1):
                k[b]=0
            for a in range(1,n+1):
                z=perm[a-1]
                for b in range(n+1):
                    if z>n-b:k[b]+=1
                    item=aggregate[a][b]
                    item[0]+=records;item[1]+=k[b];item[2]+=records*k[b]
        den=factorial(n)
        for a in range(n+1):
            for b in range(n+1):
                if a==0: 
                    expected=Fraction(0)
                    got=Fraction(0)
                else:
                    sm,sk,smk=aggregate[a][b]
                    got=Fraction(smk,den)-Fraction(sm*sk,den*den)
                    expected=cov_conditional_ab(n,a,b)
                assert got==expected,(n,a,b,got,expected)
                cells+=1
        for a in range(n+1):
            for q in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
                mix=sum(Fraction(comb(n,b))*q**b*(1-q)**(n-b)*cov_conditional_ab(n,a,b)
                        for b in range(n+1))
                assert mix==cov_conditional_a(n,a,q),(n,a,q,mix)
    assert unconditional(2,Fraction(1,2),Fraction(1,2))==-Fraction(1,16)
    assert unconditional(3,Fraction(1,2),Fraction(1,2))==-Fraction(15,128)
    for n in range(2,35):
        for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
            for q in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
                c=unconditional(n,p,q)
                assert c < 0
                difference=c+(1-p)*(1-q)
                assert 0<difference<=(1-q)*((1-p)**n+(1-p*q)**n)
    print('PASS: exact permutation cells',cells)
    print('PASS: binomial mixture reduction, strict signs, exponential error bounds')
    print('EXACT: n=2, p=q=1/2 ->',unconditional(2,Fraction(1,2),Fraction(1,2)))
    print('EXACT: n=3, p=q=1/2 ->',unconditional(3,Fraction(1,2),Fraction(1,2)))

if __name__=='__main__':
    run()
