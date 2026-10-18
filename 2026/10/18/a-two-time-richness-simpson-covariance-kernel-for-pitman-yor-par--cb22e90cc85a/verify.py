"""Exact finite-state checks of a Pitman–Yor two-time covariance formula.

Usage: python verify.py. Only the standard library is required.
"""

from fractions import Fraction as F
from math import prod

def enumerate_partitions(m,a,t):
    states={(0,):F(1)}
    for i in range(1,m):
        out={}
        for lab,p in states.items():
            k=max(lab)+1
            for j in range(k):
                size=lab.count(j)
                l=lab+(j,)
                out[l]=out.get(l,F(0))+p*(size-a)/(t+i)
            l=lab+(k,)
            out[l]=out.get(l,F(0))+p*(t+k*a)/(t+i)
        states=out
    return states
for a,t in [(F(0),F(1)),(F(1,3),F(2)),(F(1,2),F(1,2)),(F(2,3),F(-1,3))]:
 for n in range(2,6):
  for m in range(2,7):
   states=enumerate_partitions(max(n,m),a,t)
   assert sum(states.values())==F(1)
   q=lambda l: F(sum(l[i]==l[j] for i in range(m) for j in range(i+1,m))*2, m*(m-1))
   ek=sum((p*(max(l[:n])+1) for l,p in states.items()),F(0))
   eq=sum((p*q(l) for l,p in states.items()),F(0))
   ekq=sum((p*(max(l[:n])+1)*q(l) for l,p in states.items()),F(0))
   c=ekq-ek*eq
   f=-F(1-a)*F(t+a)/F((t+1)**2)*prod((t+k+a)/(t+k) for k in range(2,n))
   if m>n:f*=F(n*(n-1),m*(m-1))*F((t+m)*(t+m+1),(t+n)*(t+n+1))
   assert c==f,(a,t,n,m,c,f)
 print('PASSED cross sizes 2<=n<=5, 2<=m<=6 at alpha,theta:',a,t)
