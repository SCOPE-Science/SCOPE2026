"""Finite exact checks for a sparse convolution identity in arithmetic functions.
Run with Python 3, no third-party dependencies. Not an infinite proof.
"""
from fractions import Fraction
from math import isqrt


def factorization(n):
    fac=[]
    p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p;e+=1
            fac.append((p,e))
        p+=1 if p==2 else 2
    if n>1: fac.append((n,1))
    return fac


def direct(n,r):
    out=Fraction(1)
    for p,a in factorization(n):
        out*=Fraction((a+r-1)//r+1,2)
    return out


def sparse(n,r):
    out=Fraction(1)
    for p,a in factorization(n):
        if a<r+1 or (a-1)%r:
            return Fraction(0)
        out/=2
    return out


def verify():
    cells=0; tests=0
    for r in (2,3,4,5):
        B=2500
        b=[sparse(n,r) for n in range(B+1)]
        sums=[Fraction(0) for _ in range(B+1)]
        for d in range(1,B+1):
            if b[d]:
                for n in range(d,B+1,d):
                    sums[n]+=b[d]
        for n in range(1,B+1):
            assert sums[n] == direct(n,r), (r,n,sums[n],direct(n,r))
            cells+=1
        for N in (1,2,15,27,125,256,729,2500):
            S1=sum((direct(n,r) for n in range(1,N+1)),Fraction(0))
            S2=sum((b[d]*(N//d) for d in range(1,N+1)),Fraction(0))
            assert S1==S2
            tests+=1
        # Compare first Euler coefficients of zeta(s)G_r(s), exactly.
        for e in range(0,25):
            got=sum((Fraction(1,2) for t in range(1,e+1) if t>=r+1 and (t-1)%r==0),Fraction(1))
            assert got == Fraction((e+r-1)//r+1,2) if e else got==1
            tests+=1
    print(f'VERIFY_OK independent_dirichlet_coefficient_cells={cells} full_summatory_checks={tests-100} local_euler_checks=100 exact_fractions=PASS finite_only=YES')

if __name__=='__main__': verify()
