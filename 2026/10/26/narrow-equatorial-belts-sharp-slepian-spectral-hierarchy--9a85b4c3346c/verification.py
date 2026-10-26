"""Exact finite consistency checks for the equatorial Slepian spectral coefficients.
Runs using the Python standard library; this does not prove the all-degree theorem.
"""
from fractions import Fraction as F
from math import comb, factorial

def moment(n,m=0):
    if n%2: return F(0)
    return sum(((-1)**u*comb(m,u)*F(2,n+2*u+1) for u in range(m+1)),F(0))

def inv(a):
    n=len(a)
    x=[[F(v) for v in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        r=next(r for r in range(j,n) if x[r][j])
        x[j],x[r]=x[r],x[j]
        v=x[j][j]
        x[j]=[z/v for z in x[j]]
        for i in range(n):
            if i!=j:
                z=x[i][j]
                x[i]=[a-z*b for a,b in zip(x[i],x[j])]
    return [row[n:] for row in x]

def poch(x,n):
    ans=F(1)
    for z in range(n):ans*=x+z
    return ans

def endpoint_formula(m,j,k):
    a=F(2*j-1,2)
    s=(k-j-1)//2
    return sum((((2*r+a+m+1)*poch(r+a+1,m)/poch(F(r+1),m))*
                (poch(a+1,r)/factorial(r))**2 for r in range(s+1)),F(0))

def legendre_h(j):
    return F(2,2*j+1)*F(2**j,comb(2*j,j))**2

checks=0
for m in range(9):
    for k in range(1,10):
        for j in range(k):
            tail=k-j
            # Independent variational formula: coefficient-of-x^j evaluation norm
            # on x^j times polynomials of degree < k-j.
            T=[[moment(2*j+r+s,m) for s in range(tail)] for r in range(tail)]
            d=inv(T)[0][0]
            assert d==endpoint_formula(m,j,k),(m,k,j,'endpoint')
            # Independent moment Schur complement for monic Legendre norm.
            M=[[moment(r+s) for s in range(j)] for r in range(j)]
            if j:
                v=[moment(j+r) for r in range(j)]
                B=inv(M)
                h=moment(2*j)-sum((v[r]*B[r][s]*v[s] for r in range(j) for s in range(j)),F(0))
            else:h=moment(0)
            assert h==legendre_h(j),(m,k,j,'Legendre')
            checks+=2
for L in range(11):
    c=legendre_h(L)*endpoint_formula(0,L,L+1)
    assert c==F(2**L,comb(2*L,L))**2
    # Odd-integer multiplicity list totals dim of the full spherical band.
    assert sum(2*(L-j)+1 for j in range(L+1))==(L+1)**2
    checks+=2
print('PASS',checks,'exact rational consistency checks')
