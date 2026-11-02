#!/usr/bin/env python3
"""Exact modular certificates for the 3-canonical Wronskian of Klein quartic.
Pure Python plus Sympy. Mathematical statement and assumptions appear in RESULT.md.
"""
import math
import sympy as sp
from klein_jet_check import jets_at

x,y,z=sp.symbols('x y z')
f=x**3*y+y**3*z+z**3*x
u=x**5*z+x*y**5+y*z**5-5*x*x*y*y*z*z
H=sp.hessian(f,(x,y,z));v=sp.Matrix([sp.diff(u,t) for t in (x,y,z)]);
M=H.row_join(v).col_join(sp.Matrix([list(v)+[0]]))
A=sp.expand(M.det(method='berkowitz')/9)
B=sp.expand(sp.det(sp.Matrix([[sp.diff(h,t) for t in (x,y,z)] for h in (f,u,A)]))/14)
assert sp.Poly(B*B-A*A*A+1728*u**7,x,y,z).rem(sp.Poly(f,x,y,z)).is_zero
polys=[sp.Poly(q.subs(z,1),x,y) for q in (u,A,B)]
def evalpoly(poly,a,b,p):
 return sum(int(v)*pow(a,int(ex[0]),p)*pow(b,int(ex[1]),p) for ex,v in poly.terms())%p

def allchecks(p):
 pairs=[];fact=math.prod(math.factorial(k) for k in range(10))%p
 for a in range(1,p):
  for b in range(p):
   if (a**3*b+b**3+a)%p!=0:continue
   fy=(a**3+3*b*b)%p
   if not fy:continue
   u0,A0,B0=[evalpoly(q,a,b,p) for q in polys]
   U=pow(u0,9,p)*B0%p
   V=pow(u0,2,p)*pow(A0,3,p)*B0%p
   W=jets_at(p,a,b)*pow(fy,45,p)*fact%p
   q=(21962*U+3*V)%p
   if q and W and U and V:
    pairs.append((a,b,U,V,W,q, W*pow(q,-1,p)%p))
   if len(pairs)>=5:break
  if len(pairs)>=5:break
 assert len(pairs)>=3, (p,pairs)
 assert len(set(row[-1] for row in pairs))==1,(p,pairs)
 c=pairs[0][-1]
 assert c
 assert (pairs[0][2]*pairs[1][3]-pairs[0][3]*pairs[1][2])%p!=0,(p,pairs)
 print('p',p,'constant_ratio',c,'evaluations',[(row[0],row[1],row[4],row[5]) for row in pairs]);
 return pairs

for p in (79,139,277): allchecks(p)
print('VERIFY_MODULAR_WRONSKIAN_OK')
