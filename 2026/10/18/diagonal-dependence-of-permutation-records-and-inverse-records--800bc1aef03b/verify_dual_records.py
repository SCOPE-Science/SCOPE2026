#!/usr/bin/env python3
"""Independent exact checks for the finite permutation/inverse-record covariance theorem.

Runs exhaustive finite tests. The all-size result rests on the written proof.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, log


def records(word):
    flags=[]
    previous=0
    for val in word:
        new=val>previous
        flags.append(int(new))
        previous=max(previous,val)
    return flags


def inverse(word):
    v=[0]*len(word)
    for idx,key in enumerate(word,1):
        v[key-1]=idx
    return v


def predicted_joint(n,i,j):
    return Fraction(1,i*j)+(Fraction(i-1,i*i*comb(n,i)) if i==j else Fraction(0))


def audit():
    tests=0
    for n in range(1,9):
        actual=[[0]*n for _ in range(n)]
        marg_r=[0]*n
        marg_s=[0]*n
        for p in permutations(range(1,n+1)):
            r=records(p)
            s=records(inverse(p))
            for i in range(n):
                marg_r[i]+=r[i]
                marg_s[i]+=s[i]
                if r[i]:
                    for j in range(n):
                        actual[i][j]+=s[j]
        fact=factorial(n)
        for i in range(1,n+1):
            assert Fraction(marg_r[i-1],fact)==Fraction(1,i)
            assert Fraction(marg_s[i-1],fact)==Fraction(1,i)
            tests+=2
            for j in range(1,n+1):
                a=Fraction(actual[i-1][j-1],fact)
                b=predicted_joint(n,i,j)
                assert a==b, (n,i,j,a,b)
                cov=a-Fraction(1,i*j)
                expect_cov=Fraction(i-1,i*i*comb(n,i)) if i==j else Fraction(0)
                assert cov==expect_cov
                if i!=j:
                    assert a==Fraction(1,i)*Fraction(1,j)
                    tests+=1
                tests+=2
        exact=Fraction(sum(sum(row) for row in actual),fact) - Fraction(sum(Fraction(1,i) for i in range(1,n+1)))**2
        closed=sum((Fraction(i-1,i*i*comb(n,i)) for i in range(1,n+1)),Fraction(0))
        assert exact==closed, (n,exact,closed)
        tests+=1
    for n in (50,100,300,800):
        value=sum(float(Fraction(i-1,i*i*comb(n,i))) for i in range(2,n+1))
        expansion=1/n+1/(2*n*n)
        assert abs(value-expansion)<8/n**3
        tests+=1
    assert tests==660
    print('PASS: 656 exact-rational assertions and 4 numerical comparisons; exhaustive permutations through n=8')

if __name__=='__main__':
    audit()
