#!/usr/bin/env python3
"""Exact small-case checks for a resetting two-colour reinforced urn.

Only standard-library Python is required. This program checks finite identities;
its finite computations are not proofs of the asymptotic statements.
"""
from fractions import Fraction as F
from math import comb

checks=0

def check(expr, detail):
    global checks
    assert expr, detail
    checks += 1

def rise(a,k):
    r=F(1)
    for j in range(k):r*=a+j
    return r

def mass(n,k,j):
    a=F(n,2)
    return F(comb(k,j))*rise(a,j)*rise(a,k-j)/rise(F(n),k)

# The beta-binomial coefficient formula is independently compared with
# the urn transition recursion (red, blue increments), using exact rationals.
for n in range(2,22,2):
    p={0:F(1)}
    for k in range(0,31):
        q={j:mass(n,k,j) for j in range(k+1)}
        check(sum(q.values())==1,(n,k,'normalization'))
        check(p==q,(n,k,'recursion'))
        mean=sum(q[j]*F(n//2+j,n+k) for j in q)
        second=sum(q[j]*F(n//2+j,n+k)**2 for j in q)
        check(mean==F(1,2),(n,k,'mean'))
        var=second-mean*mean
        check(var==F(k,4*(n+1)*(n+k)),(n,k,'variance'))
        pnext={j:F(0) for j in range(k+2)}
        for j,w in p.items():
            pnext[j]+=w*F(n//2+k-j,n+k)
            pnext[j+1]+=w*F(n//2+j,n+k)
        p=pnext

# Construct a truncated stationary marked-age distribution, and check
# every interior stationarity equation directly (including reset mass).
for n in range(2,12,2):
  for r in [F(1,2),F(1,3),F(2,5),F(1,7)]:
    K=26
    pi={(k,j):r*(1-r)**k*mass(n,k,j)
        for k in range(K+1) for j in range(k+1)}
    check(pi[(0,0)]==r,(n,r,'reset flow'))
    check(sum(pi.values())==1-(1-r)**(K+1),(n,r,'tail mass'))
    for k in range(1,K+1):
      for j in range(k+1):
        inc=F(0)
        if j<=k-1:
          inc+=pi[(k-1,j)]*F(n//2+k-1-j,n+k-1)*(1-r)
        if j>=1:
          inc+=pi[(k-1,j-1)]*F(n//2+j-1,n+k-1)*(1-r)
        check(inc==pi[(k,j)],(n,r,k,j,'stationarity'))
    # Independently derive conditional second moments from exact state masses.
    for k in range(0,11):
      q={j:pi[(k,j)]/(r*(1-r)**k) for j in range(k+1)}
      var=sum(w*(F(n//2+j,n+k)-F(1,2))**2 for j,w in q.items())
      check(var==F(k,4*(n+1)*(n+k)),(n,r,k,'conditional stationary variance'))

# For every state in the truncated chain, the conditional mean after h
# steps is exactly a contraction toward 1/2 by the no-reset probability.
# We calculate this via the full finite branching state recursion, without
# invoking the claimed covariance formula in the calculation.
for n in (2,4,6):
  for r in (F(1,2),F(1,3)):
    for k in range(0,5):
      for j in range(k+1):
        x=F(n//2+j,n+k)
        states={(k,j):F(1)}
        for h in range(1,7):
          nxt={}
          for (age,red),w in states.items():
            nxt[(0,0)]=nxt.get((0,0),F(0))+w*r
            redprob=F(n//2+red,n+age)
            for state,prob in [((age+1,red+1),redprob),
                               ((age+1,red),1-redprob)]:
              nxt[state]=nxt.get(state,F(0))+w*(1-r)*prob
          states=nxt
          condmean=sum(w*F(n//2+red,n+age)
                       for (age,red),w in states.items())
          target=F(1,2)+(1-r)**h*(x-F(1,2))
          check(condmean==target,(n,r,k,j,h,'mean contraction'))

print(f'PASS: {checks} exact rational assertions; finite tests only')
