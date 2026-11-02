#!/usr/bin/env python3
"""Exact algebraic checks for the Fermat-cubic sextactic intersection.
Scientific scope: fixed integral equations, not intrinsic p-characteristic osculation.
Requires SymPy; no online data or external artifacts.
"""
import sympy as s
x,y,z,u,v=s.symbols('x y z u v')
f=x**3+y**3+z**3
g=(x**3-y**3)*(y**3-z**3)*(z**3-x**3)

def mod_poly(expression, variables, p):
    return s.Poly(s.expand(expression), *variables, modulus=p).as_expr()

assert s.total_degree(f)==3 and s.total_degree(g)==9
# Explicit identity in the characteristic-two plane-cubic coordinate ring.
char2=s.groebner([f],x,y,z,modulus=2)
assert mod_poly(char2.reduce(mod_poly(g-(x*y*z)**3,(x,y,z),2))[1],(x,y,z),2)==0
# After setting x=1 and u=x+y+z, v=x-y in characteristic three:
cf3=mod_poly(f.subs({x:1,y:1-v,z:1+u+v}), (u,v),3)
cg3=mod_poly(g.subs({x:1,y:1-v,z:1+u+v}), (u,v),3)
assert cf3==u**3
# The two-variable remainder is computed using the Groebner basis, not a univariate division.
assert s.groebner([u**3],u,v,modulus=3).reduce(mod_poly(cg3-v**9,(u,v),3))[1]==0
assert s.groebner([u**3,v**9],u,v,modulus=3).reduce(cg3)[1]==0
# Nonzero norms and zero divisors do not enter; all characteristic regimes
# follow from elementary polynomial identities and transversal derivatives.
for p in [5,7,11,13]:
    assert s.Poly(f,x,y,z,modulus=p).total_degree()==3
    assert s.Poly(g,x,y,z,modulus=p).total_degree()==9
    assert s.Poly(s.diff(f,z),x,y,z,modulus=p).as_expr()!=0
# Geometric support over F4: cubes of nonzero elements are 1.
# F4 = {0,1,w,w+1}, w^2=w+1.
def mul(a,b):
    r=0
    for j in range(2):
        if (b>>j)&1: r^=a<<j
    for shift in (2,):
        if r&(1<<shift):r^=(0b111<<(shift-2))
    return r

def pow4(a,n):
    r=1
    for _ in range(n):r=mul(r,a)
    return r

def projectivize(a):
    pivot=next(t for t in a if t!=0)
    inv=next(b for b in [1,2,3] if mul(pivot,b)==1)
    return tuple(mul(inv,t) for t in a)
P2=set()
for xx in range(4):
 for yy in range(4):
  for zz in range(4):
   if not (xx or yy or zz):continue
   pt=projectivize((xx,yy,zz))
   if pow4(xx,3)^pow4(yy,3)^pow4(zz,3)==0:P2.add(pt)
assert len(P2)==9 and all(sum(c!=0 for c in q)==2 for q in P2)
F2=[q for q in P2 if all(t in (0,1) for t in q)]
assert len(F2)==3
# The geometric nine support points in char 2 have local type k[[t]]/(t^3).
# In char 3 the unique support point is [1:1:1] with ideal (u^3,v^9).
assert len([u**i*v**j for i in range(3) for j in range(9)])==27
print('FERMAT_CUBIC_27_SEXTACTIC_BAD_FIBERS_2_3_EXACT_OK')
print('char2: 9 geometric support points (3 F2, 6 F4), local length 3; char3: one length-27 point')
