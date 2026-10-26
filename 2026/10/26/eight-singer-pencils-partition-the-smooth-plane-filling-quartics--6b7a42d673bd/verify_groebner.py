#!/usr/bin/env python3
"""Independent Groebner verification of the filling-plane-quartic incidence."""
from sympy import symbols, Poly, groebner
x,y,z=symbols('x y z')
U=y*y*z+y*z*z
V=z*z*x+z*x*x
W=x*x*y+x*y*y
I=(1<<0)|(1<<4)|(1<<8)

def form(A):
  v=(x,y,z);expr=0
  for j,q in enumerate((U,V,W)):
    l=sum(((A>>(3*i+j))&1)*v[i] for i in range(3))
    expr+=l*q
  pol=Poly(expr,x,y,z,modulus=2)
  return pol.as_expr()

def issmooth(f):
  for u,v,w in ((x,y,z),(y,x,z),(z,x,y)):
    g=Poly(f,x,y,z,modulus=2).eval(u,1).as_expr()
    # Other two coordinates are free; g, partials must have no common zeros over algebraic closure.
    G=groebner([g,g.diff(v),g.diff(w)],v,w,order='lex',modulus=2)
    if list(G)!=[1]: return False
  return True

# Distinct forms are indexed by the 256 cosets of {0,I} in binary matrices.
forms={min(a,a^I):form(a) for a in range(512)}
assert len(forms)==256
smooth={a for a,f in forms.items() if a and issmooth(f)}
assert len(smooth)==24,(len(smooth),sorted(smooth))
pencils={frozenset((a,b,min(a^b,(a^b)^I))) for a in smooth for b in smooth if a<b and min(a^b,(a^b)^I) in smooth}
assert len(pencils)==8 and all(len(p)==3 for p in pencils)
assert sum(len(t) for t in pencils)==24
for a in sorted(smooth):
    assert sum(a in t for t in pencils)==1
# Exhibit one pair and its sum as explicit polynomials.
p=sorted(pencils,key=lambda s:min(s))[0]
print('distinct filling quartics',len(forms)-1,'geometrically smooth',len(smooth),'pencils',len(pencils))
for a in sorted(p):print('matrix coset',a,'quartic=',form(a))
print('PASS')
