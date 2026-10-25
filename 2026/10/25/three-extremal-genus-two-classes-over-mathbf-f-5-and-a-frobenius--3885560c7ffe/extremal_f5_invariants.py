#!/usr/bin/env python3
"""Independent finite-field secondary invariants for three extremal sextics."""
from sympy import Poly, symbols
from collections import Counter
from itertools import product
from extremal_f5 import ev, squarefree
x=symbols('x')
R=[(1,0,0,0,4,0,1),(1,0,1,0,3,0,4),(1,0,1,2,2,2,1)]
# F25=F5[t]/(t^2-2), 2 nonsquare.
def mul(u,v):
 a,b=u;c,d=v
 return ((a*c+2*b*d)%5,(a*d+b*c)%5)
def power(u,n):
 t=(1,0)
 while n:
  if n&1:t=mul(t,u)
  u=mul(u,u);n//=2
 return t

def fx(f,u):
 ret=(0,0)
 for a in reversed(f): ret=tuple((v+w)%5 for v,w in zip(mul(ret,u),(a,0)))
 return ret
F25=list(product(range(5),repeat=2))
for f in R:
 assert squarefree(list(f))
 n1=sum(2 if ev(f,a,1) in (1,4) else (1 if ev(f,a,1)==0 else 0) for a in range(5))+2
 assert n1==12
 n2=sum(2 if fx(f,a)!=(0,0) and power(fx(f,a),12)==(1,0) else (1 if fx(f,a)==(0,0) else 0) for a in F25)+2
 a2=(n2+10)//2
 ff=Poly(sum(v*x**i for i,v in enumerate(f)),x,modulus=5)
 pieces=ff.factor_list()[1]
 partition=sorted([fac.degree() for fac,mul in pieces for _ in range(mul)])
 print('rep',f,'N1',n1,'N2',n2,'weil_a2',a2,'branch_partition',partition,'factors',[(tuple(int(c)%5 for c in reversed(p.all_coeffs())),m) for p,m in pieces])
