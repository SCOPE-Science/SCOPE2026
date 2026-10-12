"""Exact checks for the arithmetic node configuration of a genus-five Howe sextic.
Requires SymPy 1.14.0. Run: python verify_howe_nodes.py
"""
import itertools
import sympy as sp

x,u,v,Y,Z,W=sp.symbols('x u v Y Z W')
branch=(2,3,4,5,6)
a,b,c,d,e=branch
phi=x*(x-1)*(x-a)
q1=(x-b)*(x-c)
q2=(x-d)*(x-e)
g=sp.expand(sp.resultant(phi*u-q1,phi*v-q2,x))
assert g == -12*(600*u**3-520*u**2*v-50*u**2+142*u*v**2+33*u*v+u-12*v**3+13*v**2-v)
assert [sp.factor(e) for e in sp.groebner([g,sp.diff(g,u),sp.diff(g,v)],u,v).exprs]==[560*u-11,56*v-1]
u0=sp.Rational(11,560);v0=sp.Rational(1,56)
assert all(sp.cancel(h.subs({u:u0,v:v0}))==0 for h in [g,sp.diff(g,u),sp.diff(g,v)])
deth=sp.factor(sp.det(sp.hessian(g,(u,v))).subs({u:u0,v:v0}))
assert deth==-253584,deth
assert sp.simplify(sp.Rational(385,140**2)-u0)==0
assert sp.simplify(sp.Rational(14,28**2)-v0)==0
assert 385*14 != (sp.integer_nthroot(385*14,2)[0])**2
F=sp.Poly(g.subs({u:Y**2/W**2,v:Z**2/W**2})*W**6,Y,Z,W).as_expr()
assert sp.expand(F.subs(W,1)-g.subs({u:Y**2,v:Z**2}))==0
partials=[sp.diff(F,c) for c in (Y,Z,W)]
assert sp.simplify(sp.det(sp.hessian(F.subs(W,1),(Y,Z))).subs({Y:sp.sqrt(385)/140,Z:sp.sqrt(14)/28}))==sp.Rational(-348678,245)

# Direct modular singularity checks for representative good primes.
functions=[sp.lambdify((Y,Z,W),h,modules='math') for h in [F]+partials]

def predicted(p):
 def symbol(n):
  z=pow(n%p,(p-1)//2,p)
  return 1 if z==1 else (-1 if z==p-1 else 0)
 return 5 if symbol(385)==symbol(14)==1 else 1

def observed(p):
 pts=[]
 for yy,zz,ww in itertools.chain(((yy,zz,1) for yy in range(p) for zz in range(p)),((yy,1,0) for yy in range(p)),[(1,0,0)]):
  if all(int(fn(yy,zz,ww))%p==0 for fn in functions):pts.append((yy,zz,ww))
 return pts
for p in [13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83]:
 pts=observed(p)
 assert len(pts)==predicted(p),(p,predicted(p),pts)
assert sp.factorint(385)=={5:1,7:1,11:1}
assert sp.factorint(14)=={2:1,7:1}
assert sp.factorint(253584)=={2:4,3:3,587:1}
print('VERIFY_OK resultant exact, unique rational squared-node pair, nondegenerate nodes, independent square classes, 18 finite-field checks')
