#!/usr/bin/env python3
"""Exact rational checks for spatial default-delegation Nash equilibria."""
from fractions import Fraction as F
from itertools import product
from math import factorial

def walk(d, start):
    out=[]; seen=set(); j=start
    while j not in seen:
        out.append(j); seen.add(j); j=d[j]
    return tuple(out)

def payoff(i,d,x,p,tau):
    survival=F(1); value=F(0)
    for j in walk(d,i):
        value+=survival*p[j]*(tau-abs(x[i]-x[j]))
        survival*=1-p[j]
    return value

def is_equilibrium(d,x,p,tau):
    n=len(d)
    for i in range(n):
        actual=payoff(i,d,x,p,tau)
        for target in range(n):
            new=d[:i]+(target,)+d[i+1:]
            if payoff(i,new,x,p,tau)>actual:
                return False
    return True

def is_hamiltonian(d):
    n=len(d)
    w=walk(d,0)
    return len(w)==n and d[w[-1]]==0

def threshold(p,tau):
    q=[1-z for z in p]
    Q=F(1)
    for qi in q: Q*=qi
    return tau*min(p)*Q/(max(q)*max(q))

def brute_prob(i,d,x,p,tau):
    n=len(d); ans=F(0)
    for votes in product((False,True),repeat=n):
        prob=F(1)
        for j,vote in enumerate(votes):prob*=p[j] if vote else (1-p[j])
        ult=next((v for v in walk(d,i) if votes[v]),None)
        if ult is not None:ans+=prob*(tau-abs(x[i]-x[ult]))
    return ans

checks=0
# Utility expression is independently verified against all voter-turnout subsets.
for n in (2,3,4):
    x=tuple(F(i,3*n) for i in range(n))
    p=tuple(F(2*i+2,3*n+5) for i in range(n))
    for d in product(range(n),repeat=n):
        for i in range(n):
            assert payoff(i,d,x,p,F(1))==brute_prob(i,d,x,p,F(1))
            checks+=1
print('subset utility checks:',checks)

# Strong characterization: exact exhaustive best-response on several heterogeneous electorates.
for n in (2,3,4,5):
    turnout_sets=[tuple(F(1,2) for _ in range(n)), tuple(F(i+2,2*n+5) for i in range(n))]
    for p in turnout_sets:
        tau=F(1)
        b=threshold(p,tau)
        x=tuple(b*F(i,n+1) for i in range(n))
        found=0
        for d in product(range(n),repeat=n):
            eq=is_equilibrium(d,x,p,tau)
            hm=is_hamiltonian(d)
            assert eq==hm, (n,p,d,eq,hm)
            found+=int(eq);checks+=1
        assert found==factorial(n-1)
        print('robust NE count:',n,p,found,'diameter',x[-1],'threshold',b)

# Exact crossover for three voters, p_i=1/2, tau=1.
for a in (F(1,10), F(1,4), F(2,5)):
    for b in (F(j,40) for j in range(1,40)):
        if not 0<a<b<1:continue
        x=(F(0),a,b);p=(F(1,2),)*3
        eq=is_equilibrium((1,0,1),x,p,F(1))
        criterion=b>=max(2*a,(1+a)/2)
        assert eq==criterion,(a,b,eq,criterion)
        checks+=1
# Check boundary equality independently.
for a in (F(1,10),F(1,3),F(2,5)):
    b=max(2*a,(1+a)/2)
    assert b<1 and is_equilibrium((1,0,1),(F(0),a,b),(F(1,2),)*3,F(1))
    checks+=1
print('total exact assertions:',checks)
