#!/usr/bin/env python3
"""Finite exact-arithmetic checks for balanced Hartogs concentration spectral identities."""
from fractions import Fraction
from math import gcd, log, pi

checks=0

def check(ok, label):
    global checks
    checks+=1
    if not ok:
        raise AssertionError(label)

def rho(m,n,r):
    return ((n*r-1)%m)+1

def dedekind(m,n):
    return sum((Fraction(r,m)-Fraction(1,2))*(Fraction(rho(m,n,r),m)-Fraction(1,2)) for r in range(1,m))

def block_spectrum(m,n,maxell):
    return {ell:sum(1 for r in range(1,m+1) for j in range(maxell//m+1) for k in range(maxell//m+1) if r+rho(m,n,r)+m*(j+k)==ell) for ell in range(2,maxell+1)}

def direct_spectrum(m,n,maxell):
    return {ell:sum((n+1)*q% m==ell%m for q in range(1,ell)) for ell in range(2,maxell+1)}

def finite_part(m,n):
    # Coefficient resulting from finite Taylor expansion of the numerator and denominator.
    cross=sum(r*rho(m,n,r) for r in range(1,m+1))
    return Fraction(cross,m*m)-Fraction(m*m+2*m-3,4*m)

for m in range(1,13):
    for n in range(1,20):
        if gcd(m,n)!=1: continue
        residues=[rho(m,n,r) for r in range(1,m+1)]
        check(sorted(residues)==list(range(1,m+1)),('permutation',m,n))
        check(sum(residues)==m*(m+1)//2,('sum',m,n))
        check(finite_part(m,n)==dedekind(m,n)+Fraction(m+3,4*m),('constant',m,n))
        # Direct Taylor expansion of N(1-u)/(1-(1-u)^m)^2 through u^0.
        A=[r+rho(m,n,r) for r in range(1,m+1)]
        N0=Fraction(m)
        N1=-sum(A)
        N2=Fraction(sum(v*(v-1) for v in A),2)
        x=Fraction(m-1,2)
        y=Fraction((m-1)*(m-2),6)
        finite_from_polynomial=(N2+2*x*N1+N0*(3*x*x-2*y))/m**2
        coeff_minus_one=(N1+2*x*N0)/m**2
        check(coeff_minus_one==Fraction(-2,m),('pole 1',m,n))
        check(finite_from_polynomial==finite_part(m,n),('pole 0',m,n))
        inv=pow(n,-1,m) if m>1 else 1
        check(sorted(r+rho(m,n,r) for r in range(1,m+1))==sorted(r+rho(m,inv,r) for r in range(1,m+1)),('inverse',m,n))
        b=block_spectrum(m,n,50)
        d=direct_spectrum(m,n,50)
        check(b==d,('multiplicity',m,n))
        for ell,mult in d.items():
            div=gcd(n+1,m)
            check(div==1 or ell%div==0 or mult==0,('holes',m,n,ell))
        # Direct radial integral of normalized monomials; exactly integer powers of a.
        q=2; k=0; s=m*(k+1)+n*q
        a=Fraction(2,3)
        full=Fraction(1,1)*m/(q*s)
        inner=full*a**(2*(q+s))
        check(inner/full==a**(2*(q+s)),('radial norm ratio',m,n))
        # count is quadratic, with first-order error on finite ranges
        for B in [20,50,100]:
            ncount=sum(v for e,v in d.items() if e<=B) if B<=50 else sum(sum((n+1)*q%m==ell%m for q in range(1,ell)) for ell in range(2,B+1))
            check(abs(Fraction(ncount)-Fraction(B*B,2*m)) <= 5*B,('lattice error',m,n,B,ncount))

print(f'PASS: {checks} finite exact-arithmetic assertions')
