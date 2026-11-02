#!/usr/bin/env python3
"""Exact rational tail enclosures for a generalized Fibonacci reciprocal-square identity."""
from fractions import Fraction

def check(s,r,n):
    end = r * (3*n + 12)
    U = [0,1]
    for i in range(2,end+r+1):
        U.append(s*U[-1]-U[-2])
    A = U[r*n]**2 - U[r*(n-1)]**2
    assert A >= 1
    L = sum((Fraction(1,U[r*k]**2) for k in range(n,3*n+13)), Fraction())
    nextu=U[r*(3*n+13)]
    bound=Fraction(4**r,(4**r-1)*nextu**2)
    H=L+bound
    assert L* A > 1, (s,r,n,'lower',A,L)
    if A>1:
        assert H*(A-1)<1,(s,r,n,'upper',A,H)
    return A

def main():
    count=0
    for s in range(3,11):
        for r in range(1,5):
            for n in range(1,9):
                check(s,r,n)
                count += 1
    print(f'VERIFY_OK certified_cases={count} integer_parameters=3..10,1..4,1..8')
if __name__=='__main__': main()
