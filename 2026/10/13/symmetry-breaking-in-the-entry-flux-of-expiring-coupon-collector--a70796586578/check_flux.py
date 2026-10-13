#!/usr/bin/env python3
"""Exact arithmetic checks for weighted sliding-window entry flux."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, factorial


def onto(word, n):
    return len(set(word)) == n


def direct_flux(p, M):
    n = len(p)
    ans = F(0)
    for w in product(range(n), repeat=M+1):
        if not onto(w[:M], n) and onto(w[1:], n):
            weight = F(1)
            for c in w:
                weight *= p[c]
            ans += weight
    return ans


def formula_flux(p, M):
    n = len(p)
    L = M-1
    out = F(0)
    for i in range(n):
        others = [j for j in range(n) if j != i]
        a = F(0)
        for size in range(len(others)+1):
            for subset in combinations(others, size):
                a += (-1)**(len(others)-size)*sum((p[j] for j in subset), F(0))**L
        out += p[i]*(1-p[i])*a
    return out


def short_flux(p, M):
    n = len(p)
    prod = F(1)
    for x in p: prod *= x
    if M == n:
        return factorial(n-1)*(n-1)*prod
    if M == n+1:
        return F(factorial(n),2)*prod*sum(((1-x)**2 for x in p),F(0))
    raise ValueError


def H(m,k,r):
    if m < 0:
        return F(0)
    return sum(((-1)**j*comb(k,j)*(r-j)**m for j in range(k+1)),0)


def curvature(n,M):
    r=n-1; L=M-1
    B=H(L,r,r)
    Q=r*H(L-2,r-1,r)-(r-1)*H(L-2,r-2,r)
    return F(-2*B,1)+F(-2*(r-1)*L*B,r)+r*L*(L-1)*Q


def polynomial_curvature(n,M):
    # Exact coefficient of t^2 in mu(p0+t,p0-t,p0,...).
    r=F(1,n);L=M-1
    d=[1,-1]+[0]*(n-2)
    out=F(0)
    for i in range(n):
        others=[j for j in range(n) if j!=i]
        coeff=[F(0),F(0),F(0)]
        for size in range(len(others)+1):
            for subset in combinations(others,size):
                b=sum(d[j] for j in subset)
                s=r*len(subset)
                sign=(-1)**(len(others)-size)
                for j in range(3):
                    if j<=L:
                        coeff[j]+=sign*comb(L,j)*s**(L-j)*b**j
        g0=r*(1-r)
        g1=F(d[i])*(1-2*r)
        g2=-F(d[i]**2)
        out+=g0*coeff[2]+g1*coeff[1]+g2*coeff[0]
    return out

checks=0
cases=[]
for n, Ms, vectors in [
    (2,range(2,9),[[F(1,2)]*2,[F(1,3),F(2,3)]]),
    (3,range(3,8),[[F(1,3)]*3,[F(1,2),F(1,3),F(1,6)]]),
    (4,range(4,7),[[F(1,4)]*4,[F(1,2),F(1,4),F(1,8),F(1,8)]])
]:
    for M in Ms:
        for p in vectors:
            actual=direct_flux(p,M)
            assert actual==formula_flux(p,M),(n,M,p,actual,formula_flux(p,M))
            checks+=1
            if M<=n+1:
                assert actual==short_flux(p,M)
                checks+=1
            cases.append((n,M))
for n in range(2,9):
    for M in range(max(3,n), min(n+12,20)):
        assert polynomial_curvature(n,M)==curvature(n,M)/n**(M-1),(n,M)
        checks+=1
for M in range(2,20):
    # This identity is the exact binary flux polynomial in z=p(1-p).
    for p in (F(1,2),F(1,3),F(1,7),F(2,5)):
        q=1-p
        assert formula_flux([p,q],M)==p*q*(p**(M-1)+q**(M-1))
        checks+=1
for n in range(2,11):
    p=[F(1,n)]*n
    for M in (n,n+1):
        assert formula_flux(p,M)==short_flux(p,M)
        checks+=1
# Exact M=4 certificate: with z=p(1-p), mu=1/12 - 3(z-1/6)^2.
for a in range(1,20):
    p=F(a,20);q=1-p;z=p*q
    assert formula_flux([p,q],4)==F(1,12)-3*(z-F(1,6))**2
    checks+=1
print(f'PASS: {checks} exact checks; {len(cases)} direct window enumerations; n<=8 Hessian coefficients')
