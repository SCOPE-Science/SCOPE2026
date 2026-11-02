#!/usr/bin/env python3
"""Independent exact finite-sample checks for threshold spacing-count laws.
Science-only standalone checker. No external files/packages required.
"""
from fractions import Fraction as F
from math import comb, factorial, exp, log
from itertools import product

def tailpow(z,p):
    return max(F(0), z)**p

def cross(n, r, s):
    assert n >= 2 and F(0) < r <= s < 1
    return n*(tailpow(1-s,n-1)+(n-1)*tailpow(1-r-s,n-1)-n*tailpow(1-r,n-1)*tailpow(1-s,n-1))

def pgf(n,r,s,u,v):
    value=F(0)
    for a in range(n+1):
        for b in range(n+1-a):
            coeff = factorial(n)//(factorial(a)*factorial(b)*factorial(n-a-b))
            value += coeff*(u-1)**a*(u*(v-1))**b*tailpow(1-a*r-b*s,n-1)
    return value

def distribution(n, r, s):
    # Direct joint factorial moments, inverted by binomial inclusion-exclusion.
    # Let K=# large (gap>s), H=# medium (r<gap<=s). F_{a,b}=E binom(K,a) binom(H,b).
    # For specific disjoint selected indices, medium gaps have requirement r<G<=s
    # and large gaps have G>s. Apply inclusion-exclusion to disjoint coordinates.
    moments={}
    for a in range(n+1):
      for b in range(n+1-a):
        inner=sum((-1)**j*comb(b,j)*tailpow(1-(a+j)*s-(b-j)*r,n-1) for j in range(b+1))
        moments[(a,b)]=F(factorial(n), factorial(a)*factorial(b)*factorial(n-a-b))*inner
    # Inverse factorial moment transform.
    result={}
    for k in range(n+1):
      for h in range(n+1-k):
        prob=sum((-1)**(a-k+b-h)*comb(a,k)*comb(b,h)*moments[(a,b)] for a in range(k,n+1) for b in range(h,n-a+1))
        result[(k,h)]=prob
    return result

def brute_cov_from_distribution(n,r,s):
    dist=distribution(n,r,s)
    assert all(p>=0 for p in dist.values()), (n,r,s,'negative mass',[(x,p) for x,p in dist.items() if p<0])
    assert sum(dist.values())==1,(n,r,s,'mass')
    EH=sum((k+h)*p for (k,h),p in dist.items())
    EK=sum(k*p for (k,h),p in dist.items())
    EHK=sum((k+h)*k*p for (k,h),p in dist.items())
    assert EH==n*tailpow(1-r,n-1)
    assert EK==n*tailpow(1-s,n-1)
    return EHK-EH*EK

def critical(n):
    return 1-n**(-1/(n-1))

def zero(n,r):
    q=(n*(1-r)**(n-1)-1)/(n-1)
    assert 0<q<1
    return 1-r/(1-q**(1/(n-1)))

def checks():
    count=0
    for n in range(2,9):
      for i in range(1,10):
        for j in range(i,10):
          r,s=F(i,11),F(j,11)
          c=cross(n,r,s)
          got=brute_cov_from_distribution(n,r,s)
          assert c==got, (n,r,s,c,got)
          count+=1
          # Direct bivariate PGF vs independent inversion (u on total r, v on s)
          for u,v in [(F(1,3),F(2,3)), (F(7,5),F(4,3))]:
            pv=sum(p*u**(k+h)*v**k for (k,h),p in distribution(n,r,s).items())
            assert pgf(n,r,s,u,v)==pv, (n,r,s,u,v)
            count+=1
    # Independently integrate the n=2 sample on its native uniform parameter.
    # The two circular gaps are (u,1-u), u uniform on (0,1).
    for i in range(1,10):
      for j in range(i,10):
        r,s=F(i,10),F(j,10)
        if r>=1: continue
        cuts=sorted(set([F(0),F(1),r,s,1-r,1-s]))
        E1=E2=E12=F(0)
        for a,b in zip(cuts,cuts[1:]):
          z=(a+b)/2; gap1=z;gap2=1-z
          X=int(gap1>r)+int(gap2>r)
          Y=int(gap1>s)+int(gap2>s)
          E1+=(b-a)*X; E2+=(b-a)*Y; E12+=(b-a)*X*Y
        assert E12-E1*E2==cross(2,r,s),(r,s)
        count+=1
    assert cross(2,F(1,2),F(1,2))==0
    assert distribution(2,F(1,2),F(1,2))[(1,0)]==1
    count+=2
    # For all r where below critical, unique crossing tested high precision
    for n in range(2,31):
      rc=critical(n)
      for frac in [0.03,0.25,0.5,0.9]:
        r=rc*frac
        s0=zero(n,r)
        assert r<s0<1-r, (n, r, s0)
        assert abs(float(cross(n,r,s0)))<2.e-10, (n,r,s0,cross(n,r,s0))
        assert float(cross(n,r,(r+s0)/2))>0
        assert float(cross(n,r,(s0+1)/2))<0
        count+=4
      for frac in [1.001,1.1]:
        r=rc*frac
        if r>=1: continue
        for s in [r,(1+r)/2,0.999]:
          assert float(cross(n,r,s))>0, (n,r,s)
          count+=1
    for x,y in [(0.2,0.5),(0.5,1),(1,2),(2,4),(4,6)]:
      expected=exp(-y)*(1-(1+x*y)*exp(-x))
      for n in [1000,10000]:
        observed=float(cross(n,F(str(x))/n,F(str(y))/n))/n
        assert abs(observed-expected)<0.002,(n,x,y,observed,expected)
        count+=1
    print(f'PASS {count} grouped exact and numerical assertions')
    for n,r,s in [(3,F(1,10),F(3,5)),(4,F(1,10),F(1,2)),(5,F(1,10),F(2,5)),(8,F(1,20),F(3,5)),(2,F(1,5),F(3,5))]:
      print(f'n={n}, r={r}, s={s}, covariance={cross(n,r,s)}')
if __name__=='__main__': checks()
