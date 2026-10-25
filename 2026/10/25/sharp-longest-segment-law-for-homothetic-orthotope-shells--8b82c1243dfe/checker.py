"""Exact rational finite cross-checks for hollow orthotope maximal-line-segment formula.
Checks are corroborative; the independent analytic proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import isclose

def avoids_hole(P,Q,a):
    lo=F(0); hi=F(1)
    for x,y in zip(P,Q):
        if x==y:
            if a<x<1-a: continue
            return True
        t1=(a-x)/(y-x); t2=(1-a-x)/(y-x)
        lo=max(lo,min(t1,t2));hi=min(hi,max(t1,t2))
    return lo>=hi

def bound(s,a):
    rho=a/(1-a)
    return sum(x*x for x in s)-(1-rho*rho)*min(x*x for x in s)

def examples(s,a):
    j=min(range(len(s)),key=lambda i:s[i]);rho=a/(1-a)
    P=[F(0)]*len(s);Q=list(s);Q[j]=s[j]*rho
    return P,Q

def exhaustive():
    trials=0
    for d,grid in [(2,5),(3,3),(4,2)]:
      points=list(product((F(i,grid) for i in range(grid+1)),repeat=d))
      for ai in [F(1,6),F(1,3),F(2,5)]:
        for P,Q in combinations(points,2):
          if avoids_hole(P,Q,ai):
            dist=sum((x-y)**2 for x,y in zip(P,Q))
            assert dist<=bound([F(1)]*d,ai)
            if d==2:
                p,q=map(abs,(Q[0]-P[0],Q[1]-P[1]))
                assert p*q<=ai*(p+q)
          trials+=1
        for sides in ([F(1)]*d,[F(i+1) for i in range(d)],[F(1)]+[F(2)]*(d-1)):
          p,q=examples(sides,ai)
          assert avoids_hole([p[i]/sides[i] for i in range(d)],[q[i]/sides[i] for i in range(d)],ai)
          assert sum((q[i]-p[i])**2 for i in range(d))==bound(sides,ai)
    return trials

if __name__=='__main__':
 print('ORTHOTOPE_SHELL_OK cases=',exhaustive())
