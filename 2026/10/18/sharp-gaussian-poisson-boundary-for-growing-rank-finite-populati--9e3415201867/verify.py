#!/usr/bin/env python3
"""Independent finite checks of discrete rank-statistic identities; no external packages."""
from fractions import Fraction
from itertools import combinations
from math import comb, erf, sqrt, lgamma, exp

def rise(a,k):
    v=1
    for j in range(k): v*=a+j
    return v

def bb(m,a,b):
    den=rise(a+b,m)
    return [Fraction(comb(m,j)*rise(a,j)*rise(b,m-j),den) for j in range(m+1)]

def direct(n,N,k):
    m=N-n; tally=[0]*(m+1)
    for subset in combinations(range(1,N+1),n):
        tally[subset[k-1]-k]+=1
    den=comb(N,n)
    return [Fraction(t,den) for t in tally]

def exact():
    laws=0
    for N in range(3,12):
        for n in range(2,N):
            for k in range(1,n+1):
                m=N-n; a=k; b=n-k+1; A=a+b
                z=bb(m,a,b)
                assert z==direct(n,N,k)
                assert sum(z)==1
                mu=sum(j*p for j,p in enumerate(z))
                var=sum((Fraction(j)-mu)**2*p for j,p in enumerate(z))
                assert mu==Fraction(m*a,A)
                assert var==Fraction(m*a*b*(A+m),A*A*(A+1))
                laws+=1
    return laws

def fast_bb(m,a,b):
    # loggamma to avoid integer overflow in larger finite checks
    A=a+b
    lz=lgamma(m+1)-lgamma(a+b+m)+lgamma(A)
    r=[]
    for j in range(m+1):
        lp=lz-lgamma(j+1)-lgamma(m-j+1)+lgamma(a+j)-lgamma(a)+lgamma(b+m-j)-lgamma(b)
        r.append(exp(lp))
    total=sum(r)
    return [x/total for x in r]

def normcdf(z): return (1+erf(z/sqrt(2)))/2

def dk_norm(m,a,b):
    mu=m*a/(a+b)
    v=m*a*b*(a+b+m)/((a+b)**2*(a+b+1))
    pmf=fast_bb(m,a,b);cdf=0.;err=0.
    for j,pj in enumerate(pmf):
        f=normcdf((j-mu)/sqrt(v))
        err=max(err,abs(f-cdf))
        cdf+=pj
        err=max(err,abs(f-cdf))
    return err

def poisson_tv(m,a,b):
    pmf=fast_bb(m,a,b);lam=m*a/(a+b)
    pq=[exp(-lam)]
    for j in range(1,m+1): pq.append(pq[-1]*lam/j)
    tail=max(0.,1-sum(pq))
    return (sum(abs(x-y) for x,y in zip(pmf,pq))+tail)/2

def main():
    n=exact()
    # These checkpoints are illustrative, not claims of any universal finite rate.
    g1=dk_norm(140,120,150)
    g2=dk_norm(350,220,270)
    g3=dk_norm(900,40,520)
    pois=poisson_tv(180,65,5900)
    print('Exact finite population PMFs / moments verified:',n)
    print('Gaussian illustrative Kolmogorov distances:',*(f'{x:.5f}' for x in [g1,g2,g3]))
    print('Poisson illustrative total-variation distance:',f'{pois:.5f}')
    assert max(g1,g2,g3)<0.20
    assert pois<0.08
    print('ALL FINITE CHECKS PASSED (not an infinite proof)')

if __name__=='__main__':main()
