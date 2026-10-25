"""Exact finite type-count audit for EF1 Nash products under identical 1/2-valued goods."""

from itertools import combinations
from fractions import Fraction
from math import prod

def comps(s,n):
 if n==1:yield (s,);return
 for a in range(s+1):
  for rest in comps(s-a,n-1):yield (a,)+rest

def run(N=5,MAX_M=10):
 cnt=0; eq=[];min_rat={}
 for n in range(2,N+1):
  for m in range(n,MAX_M+1):
   for b in range(m+1):
    a=m-b
    ca=list(comps(a,n));cb=list(comps(b,n));data=[]; ef=[]
    for aa in ca:
     for bb in cb:
      x=tuple(aa[i]+2*bb[i] for i in range(n)); p=prod(x)
      data.append(p)
      mn=min(x)
      if all(x[j]-mn<= (2 if bb[j] else (1 if aa[j] else 0)) for j in range(n)):
       ef.append((p,aa,bb,x))
    if not ef: raise ValueError(('noef',n,a,b))
    o=max(data)
    rhs=Fraction(3,4)**(n//2)
    for p,aa,bb,x in ef:
     cnt+=1
     if Fraction(p,o)<rhs:raise AssertionError((n,a,b,p,o,aa,bb,x))
     if Fraction(p,o)==rhs:eq.append((n,a,b,x,o))
    key=n; rv=min(Fraction(p,o) for p,_,_,_ in ef)
    if key not in min_rat or rv<min_rat[key][0]:min_rat[key]=(rv,m,a,b)
 print('verified',cnt,'allocation count vectors; minimum product ratios',min_rat)
 print('equality samples',eq[:16],'; equality_total',len(eq))
if __name__=='__main__':run()
