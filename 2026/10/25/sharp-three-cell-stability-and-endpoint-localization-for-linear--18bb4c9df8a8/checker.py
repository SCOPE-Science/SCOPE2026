#!/usr/bin/env python3
"""Exact symbolic and numerical checks for a three-element linear-spline projector."""
from fractions import Fraction
import sympy as s
import math

a,b,c=s.symbols('a b c', positive=True)
h=[a,b,c]
G=s.zeros(4)
for j,d in enumerate(h):
    G[j,j]+=d/3;G[j+1,j+1]+=d/3
    G[j,j+1]+=d/6;G[j+1,j]+=d/6
C=s.simplify(G.inv())

def row_formula(i):
    answer=0
    for j,d in enumerate(h):
        u=(-1)**(i+j)*C[i,j]
        v=(-1)**(i+j+1)*C[i,j+1]
        answer+=d*(u*u+v*v)/(2*(u+v))
    return s.factor(answer)
R=[row_formula(i) for i in range(4)]
E=4*a*b+3*a*c+2*b*b+2*b*c
Ep=2*a*b+3*a*c+2*b*b+4*b*c
D=4*a*b+3*a*c+4*b*b+4*b*c
N=s.factor(s.Rational(5,3)+8*b*(a+b)*(b+c)**2*(4*b+3*c)/(3*(2*b+c)*E*D))
assert s.cancel(R[0]-N)==0
assert s.cancel(R[3]-N.xreplace({a:c,c:a}))==0
assert s.cancel(R[0]-R[1]-8*b*b*(b+c)*(4*a*b+3*a*c+4*b*b+5*b*c+c*c)/(3*(2*b+c)*E*D))==0
H=24*a*a*b*b+30*a*a*b*c+9*a*a*c*c+60*a*b**3+86*a*b*b*c+30*a*b*c*c+36*b**4+60*b**3*c+24*b*b*c*c
assert s.cancel(R[0]-R[3]+8*b*(a+b)*(a-c)*(b+c)*H/(3*(a+2*b)*(2*b+c)*E*Ep*D))==0
F=a*a*(96*b**3+192*b*b*c+126*b*c*c+27*c**3)+a*(112*b**4+236*b**3*c+154*b*b*c*c+30*b*c**3)+16*b**3*(b+c)**2
assert s.cancel(s.Rational(8,3)-R[0]-F/(3*(2*b+c)*E*D))==0
assert all(q>0 for q in s.Poly(H,a,b,c).coeffs())
assert all(q>0 for q in s.Poly(F,a,b,c).coeffs())
assert s.limit(R[0].subs({a:s.Symbol('t',positive=True)**2,b:s.Symbol('t',positive=True),c:1}),s.Symbol('t',positive=True),0,dir='+')==s.Rational(8,3)
t=s.symbols('t', positive=True)
assert all(s.limit(v.subs({a:1,b:t,c:1}),t,0,dir='+')==s.Rational(5,3) for v in R)

assert all(s.factor((-1)**(i+j)*C[i,j]).subs({a:2,b:3,c:5})>0 for i in range(4) for j in range(4))
assert G==G.T
assert all(s.cancel((G*C)[i,j]-int(i==j))==0 for i in range(4) for j in range(4))

# Independent midpoint Riemann quadrature against the symbolic endpoint kernel.
import numpy as np
checks=0
for aa in [1,2,3,5,8]:
 for bb in [1,2,5]:
  for cc in [1,3,9]:
   vals={a:aa,b:bb,c:cc}
   cv=np.array(C.subs(vals), dtype=float)
   lengths=[aa,bb,cc]
   for i in range(4):
    numeric=0
    for j,dd in enumerate(lengths):
     qs=(np.arange(1500)+.5)/1500
     line=cv[i,j]*(1-qs)+cv[i,j+1]*qs
     numeric+=dd*float(np.mean(np.abs(line)))
    symbolic=float(R[i].subs(vals))
    assert abs(symbolic-numeric)<4e-6,(aa,bb,cc,i,symbolic,numeric)
    checks+=1
   rr=[float(v.subs(vals)) for v in R]
   assert all(s.Rational(5,3)<v.subs(vals)<s.Rational(8,3) for v in R)
   assert max(rr[:])==max(rr[0],rr[3])
   assert ((rr[0]>rr[3]) == (aa<cc)) if aa!=cc else abs(rr[0]-rr[3])<1e-9
   checks+=4
print(f'PASS: symbolic rational identities, positive polynomial certificates, limit identities, and {checks} quadrature/numerical assertions.')
