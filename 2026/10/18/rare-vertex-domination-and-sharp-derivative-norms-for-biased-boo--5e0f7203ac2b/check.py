"""Exact arithmetic validation of finite biased-product noise-operator derivative norms.

Run: python check.py.  This checks finite instances only; the analytic proof
supplies the unrestricted statement.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

def derivative_row(x, masses, rho, k):
    n=len(masses)
    total=F(0)
    for y in product((0,1), repeat=n):
        poly=[F(1)]
        for xi, yi, ai in zip(x,y,masses):
            mu= ai if yi == 1 else 1-ai
            # probability of yi given input xi and correlation rho
            p0=mu
            p1=F(int(xi==yi))-mu
            nxt=[F(0)]*(len(poly)+1)
            for j,c in enumerate(poly):
                nxt[j]+=p0*c
                nxt[j+1]+=p1*c
            poly=nxt
        d=sum((c*F(factorial(j),factorial(j-k))*rho**(j-k) for j,c in enumerate(poly) if j>=k),F(0))
        total+=abs(d)
    return total

def binprob(n,r,q):
    return F(0) if r<0 or r>n else F(comb(n,r))*q**r*(1-q)**(n-r)

def binomial_formula(n,a,rho,k):
    if k>n:return F(0)
    q=a+(1-a)*rho
    return (1-a)**k * F(factorial(n),factorial(n-k))*sum(
        abs(sum(((-1)**(k-j)*comb(k,j)*binprob(n-k,r-j,q) for j in range(k+1)),F(0)))
        for r in range(n+1))

def first_formula(n,a,rho):
    q=a+(1-a)*rho
    # At q=1 the boundary value uses n-1 rather than n.
    m=min(n-1, (n*q).numerator//(n*q).denominator)
    return 2*n*(1-a)*binprob(n-1,m,q)

def main():
    count=0
    asets=[[F(1,3)],[F(1,4),F(2,5)],[F(1,5),F(1,3),F(2,5)],
           [F(2,5),F(1,6),F(1,4),F(1,2)],
           [F(1,3),F(2,5),F(1,7),F(1,4),F(1,2)]]
    for a in asets:
        n=len(a)
        for rho in [F(0),F(1,7),F(1,2),F(5,6),F(1)]:
            for k in range(1,n+1):
                rr=derivative_row((1,)*n,a,rho,k)
                for x in product((0,1), repeat=n):
                    v=derivative_row(x,a,rho,k)
                    assert v<=rr,(a,rho,k,x,v,rr)
                    count+=1
    for n in range(1,9):
        for a in [F(1,2),F(1,3),F(1,5)]:
            for rho in [F(0),F(1,6),F(2,3),F(1)]:
                for k in range(1,min(n,4)+1):
                    v=derivative_row((1,)*n,[a]*n,rho,k)
                    w=binomial_formula(n,a,rho,k)
                    assert v==w,(n,a,rho,k,v,w)
                    count+=1
                assert derivative_row((1,)*n,[a]*n,rho,1)==first_formula(n,a,rho)
                count+=1
    print('PASS',count,'exact rational comparisons')

if __name__=='__main__':main()
