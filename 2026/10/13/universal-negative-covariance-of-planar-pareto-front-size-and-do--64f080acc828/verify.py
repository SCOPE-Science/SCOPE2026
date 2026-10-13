#!/usr/bin/env python3
"""Exact validation of record-count/hypervolume covariance for product power-law coordinates."""
from fractions import Fraction
from itertools import permutations
from math import factorial

def rising(a,b):
    z=1
    for j in range(b): z*=a+j
    return z

def moments(n,pow_):
    den=rising(n+1,pow_)
    return [Fraction(rising(j,pow_),den) for j in range(n+1)]

def explicit_cov(n,a,b):
    mx=moments(n,a)
    my=moments(n,b)
    dx=[mx[n-k+1]-mx[n-k] for k in range(1,n+1)]
    assert all(d>0 for d in dx)
    total=Fraction(0)
    for k in range(1,n):
        for r in range(1,n-k+1):
            ku=Fraction(k,k+r+b)-Fraction(k*k,(k+b)*(k+r))
            assert ku>0
            total-=dx[k-1]*ku/r
    return total

def enumeration(n,a,b):
    mx=moments(n,a); my=moments(n,b)
    dx=[mx[n-k+1]-mx[n-k] for k in range(1,n+1)]
    E_M=E_V=E_MV=Fraction(0)
    for perm in permutations(range(1,n+1)):
        m=0; mxrank=0; av=Fraction(0)
        for k,rank in enumerate(perm):
            if rank>mxrank:
                mxrank=rank
                m+=1
            av+=dx[k]*my[mxrank]
        E_M+=m; E_V+=av; E_MV+=m*av
    E_M/=factorial(n); E_V/=factorial(n); E_MV/=factorial(n)
    assert E_M == sum((Fraction(1,j) for j in range(1,n+1)),Fraction(0))
    return E_MV-E_M*E_V

def uniform_formula(n):
    H=sum((Fraction(1,k) for k in range(1,n+1)),Fraction(0))
    H2=sum((Fraction(1,k*k) for k in range(1,n+1)),Fraction(0))
    return -(H-H2-(n-H)/Fraction(n+1))/Fraction(n+1)

def run():
    cases=0
    for n in range(2,8):
        for a in (1,2,3):
            for b in (1,2,3):
                c1=explicit_cov(n,a,b)
                c2=enumeration(n,a,b)
                assert c1==c2,(n,a,b,c1,c2)
                assert c1<0
                if a==b==1:
                    assert c1==uniform_formula(n)
                cases+=1
    assert explicit_cov(1,2,3)==0
    for n in range(2,100):
        assert explicit_cov(n,1,1)==uniform_formula(n)<0
    print(f'PASS {cases} independent permutation / exact-kernel comparisons, 98 longer uniform identities; strict sign for all checked n>=2')
    print('n=2,uniform: ',uniform_formula(2))
    print('n=5,uniform: ',uniform_formula(5))
if __name__=='__main__': run()
