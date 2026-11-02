"""Exact-state and moment checks for two-scale leaf counts in batch recursive trees.

Requires Python 3 standard library only.  No stochastic simulation is used.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import sqrt, exp, factorial

checks = 0

def demand(value, message):
    global checks
    checks += 1
    if not value:
        raise AssertionError(message)

def exact_distribution(m, n):
    """Distribution of (leaf count, intact birth-cohort count) after n batches."""
    dist = {(m, 1): F(1)}
    for t in range(1, n):
        N = m*t+1
        new = defaultdict(F)
        for (L, C), prob in dist.items():
            demand(0 <= m*C <= L <= N, 'state feasibility')
            new[(L+m-1,C)] += prob * F(m*C,N)
            new[(L+m-1,C+1)] += prob * F(L-m*C,N)
            new[(L+m,C+1)] += prob * F(N-L,N)
        dist = {k:v for k,v in new.items() if v}
        demand(sum(dist.values()) == 1, 'normalization')
    return dist

def moments_exact(m,n):
    D = exact_distribution(m,n)
    EL = sum(F(L)*pr for (L,C),pr in D.items())
    EC = sum(F(C)*pr for (L,C),pr in D.items())
    LL = sum(F(L*L)*pr for (L,C),pr in D.items()) - EL*EL
    CC = sum(F(C*C)*pr for (L,C),pr in D.items()) - EC*EC
    LC = sum(F(L*C)*pr for (L,C),pr in D.items()) - EL*EC
    return EL,EC,LL,CC,LC

def moment_recursion(m,n, exact=True):
    cast=F if exact else float
    EL=cast(m)
    EC=cast(1)
    LL=CC=LC=cast(0)
    for t in range(1,n):
        N=m*t+1
        pL=EL/N
        pC=m*EC/N
        LL=(1-cast(2)/N)*LL+pL*(1-pL)
        CC=(1-cast(2*m)/N)*CC+pC*(1-pC)
        LC=(1-cast(m+1)/N)*LC+pC*(1-pL)
        EL=(1-cast(1)/N)*EL+m
        EC=(1-cast(m)/N)*EC+1
    return EL,EC,LL,CC,LC

for m in range(1,7):
    for n in range(1,10):
        a=moments_exact(m,n)
        b=moment_recursion(m,n)
        for aa,bb in zip(a,b):
            demand(aa==bb,f'exact state recursion m={m} n={n}: {aa} != {bb}')
        demand(a[0]==F(m*(m*n+1),m+1),'exact leaf mean')
        demand(a[1]==F(n,2)+F(n,2*(m*(n-1)+1)),'exact cohort mean')
        demand(a[4]>=0,'positive finite covariance')

for m in [1,2,3,5,11,50]:
    n=50000
    _,_,vl,vc,cov=moment_recursion(m,n,exact=False)
    target_l=m*m/((m+1)**2*(m+2))
    target_c=1/12
    target_x=m/(2*(m+1)*(2*m+1))
    for x,y in [(vl/n,target_l),(vc/n,target_c),(cov/n,target_x)]:
        demand(abs(x-y)<1.5e-4, f'asymptotic covariance m={m}: {x}, {y}')
    rho=target_x/sqrt(target_l*target_c)
    demand(abs(rho-sqrt(3*(m+2))/(2*m+1))<1e-12,'correlation identity')

# For growing m, verify covariance-normalizations approach independent normal limits.
for m,n in [(40,100000),(100,100000),(250,100000)]:
    _,_,vl,vc,cov=moment_recursion(m,n,exact=False)
    demand(abs(vl/(n/m)-1)<0.1, 'large-batch leaf variance')
    demand(abs(vc/n-1/12)<0.005, 'large-batch cohort variance')
    demand(abs(cov/sqrt(vl*vc))<0.17,'large-batch decorrelation')
# The rare internal recruiter count R is determined by the leaf count.  For
# finite m,n, compare its exact distribution to the Poisson law using an
# independent algebraic Markov recursion (not simulated samples).
for m in [20, 40, 80]:
    n=m
    probs=[0.0]*(n+1)
    probs[0]=1.0
    for t in range(1,n):
        new=[0.0]*(n+1)
        for r in range(t):
            if probs[r]==0:
                continue
            p=(t-r)/(m*t+1)
            new[r]+=probs[r]*(1-p)
            new[r+1]+=probs[r]*p
        probs=new
    lam=(n-1)/(m+1)
    pois=[exp(-lam)*lam**r/factorial(r) for r in range(n+1)]
    tv=.5*(sum(abs(x-y) for x,y in zip(probs,pois))+max(0,1-sum(pois)))
    demand(tv <= 3*n/(m*m)+1e-12, 'Poisson total variation coupling bound')
    demand(abs(sum(r*pr for r,pr in enumerate(probs))-lam)<1e-10,
           'Poisson crossover exact mean')
print(f'PASS {checks} exact-state, rational-moment, Poisson and asymptotic checks')
