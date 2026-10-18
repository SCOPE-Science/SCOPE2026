#!/usr/bin/env python3
"""Finite exact-rational cross-checks of the beta-binomial curvature theorem."""
from fractions import Fraction as Q
from math import comb, prod

GRID=[Q(1,8),Q(1,3),Q(1,2),Q(3,4),Q(9,10),Q(1),
      Q(11,10),Q(5,4),Q(3,2),Q(2),Q(5,2),Q(3),Q(5),Q(10),Q(40)]

def pmf(n,alpha,beta):
    weights=[comb(n,k)*prod(alpha+j for j in range(k))*
             prod(beta+j for j in range(n-k)) for k in range(n+1)]
    z=sum(weights)
    return [v/z for v in weights]

def predicted(n,alpha,beta):
    u=alpha-1
    v=beta-1
    if u>=0 and v>=0:
        return True
    if u>0 and v<0:
        d=2+(n+1)*v
        return d>0 and u*d>=-n*(n-1)*v
    if v>0 and u<0:
        d=2+(n+1)*u
        return d>0 and v*d>=-n*(n-1)*u
    return False

def check():
    cases=identities=0
    for n in range(2,32):
        for a in GRID:
            for b in GRID:
                p=pmf(n,a,b)
                actual=all(p[k]*p[k]>=p[k-1]*p[k+1]
                           for k in range(1,n))
                assert predicted(n,a,b)==actual,(n,a,b)
                for k in range(1,n):
                    r0=(n-k+1)*(a+k-1)/(k*(b+n-k))
                    r1=(n-k)*(a+k)/((k+1)*(b+n-k-1))
                    F=(n-k)*(n-k+1)
                    G=k*(k+1)
                    N=F*(a-1)+G*(b-1)+(n+1)*(a-1)*(b-1)
                    den=k*(k+1)*(b+n-k)*(b+n-k-1)
                    assert r0-r1==N/den,(n,k,a,b)
                    assert (p[k]*p[k]>=p[k-1]*p[k+1])==(N>=0)
                    identities+=1
                cases+=1
    n,a,b=3,Q(5,2),Q(3,4)
    assert pmf(n,a,b)==[Q(x,221) for x in [11,30,60,120]]
    p=pmf(n,a,b)
    assert p[2]*p[2]==p[1]*p[3]
    p=pmf(4,a,b)
    assert p[3]*p[3]<p[2]*p[4]
    print('PASS',cases,'complete finite parameter grids;',identities,
          'interior-index ratio identities and signs; equality/failure examples.')

if __name__=='__main__':
    check()
