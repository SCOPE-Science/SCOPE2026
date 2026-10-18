#!/usr/bin/env python3
"""Exact finite-state checks for balanced Pólya–Friedman urn transitions.

Run with Python 3 standard library. Finite checks test identities,
not the infinite-horizon convergence theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import log, exp


def step_distribution(state, a, b, p):
    k = len(state)
    c = a + (k-1)*b
    T = sum(state)
    out = {}
    for j, count in enumerate(state):
        for is_friedman, prob in ((False, 1-p), (True, p)):
            add = [c if (i == j and not is_friedman) else
                   (a if i == j else b) if is_friedman else 0
                   for i in range(k)]
            after = tuple(state[i]+add[i] for i in range(k))
            out[after] = out.get(after, F(0)) + F(count, T)*prob
    return out


def test_all():
    checks = 0
    for k in (2,3):
      for a,b in product((1,2),(1,2)):
       c = a+(k-1)*b
       for initial in product((1,2), repeat=k):
        R = sum(initial)
        theta = F(R,c)
        for p in (F(0),F(1,9),F(1,3),F(3,4),F(1)):
         dist = {initial:F(1)}
         predicted = [F(x,R)-F(1,k) for x in initial]
         gamma = F(k*b,c)*p
         for t in range(1,8):
          nd = {}
          for state, mass in dist.items():
           trans = step_distribution(state,a,b,p)
           assert sum(trans.values()) == 1
           checks += 1
           # Exact one-step conditional drift formula.
           old = [F(x,sum(state)) for x in state]
           for i in range(k):
            actual = sum(prob*F(s[i],sum(s)) for s,prob in trans.items())
            expected = F(1,k) + (1-gamma/(theta+t))*(old[i]-F(1,k))
            assert actual == expected, (k,a,b,state,p,i,actual,expected)
            checks += 1
           for s,prob in trans.items():
            nd[s]=nd.get(s,F(0))+mass*prob
          dist=nd
          assert sum(dist.values()) == 1
          factor=1-gamma/(theta+t)
          predicted=[factor*x for x in predicted]
          for i in range(k):
           actual=sum(weight*F(s[i],R+c*t) for s,weight in dist.items())-F(1,k)
           assert actual == predicted[i], (k,a,b,initial,p,t,i,actual,predicted[i])
           checks += 1
    # Deterministic scaling example: for each finite lambda the exact
    # centering coefficient approaches the predicted exp(-k b lambda s / c).
    for k, a,b, r, lam in ((2,2,1,(1,3),0.7),(3,1,2,(1,2,4),1.8)):
     c=a+(k-1)*b
     theta=sum(r)/c
     s=0.65
     for n in (10**3,10**5,10**7):
      p=lam/log(n)
      gamma=k*b*p/c
      t=int(n**s)
      # logarithmic harmonic representation evaluated by a loop for t<4e4
      lp=sum(log(1-gamma/(theta+j)) for j in range(1,t+1))
      assert abs(exp(lp)-exp(-k*b*lam*s/c))<0.08
      checks+=1
    return checks

if __name__ == '__main__':
 print('Exact finite-state and deterministic asymptotic checks passed:',test_all())
