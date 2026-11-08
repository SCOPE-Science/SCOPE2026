#!/usr/bin/env python3
"""Exact checks for sharp fourth moments of rank-two Grassmannian trace functions.
Requires sympy. Finite-dimensional tests corroborate, not replace, the all-n proof.
"""
import sympy as sp
from functools import lru_cache
n,x,y,z,w,S2,S3,S4=sp.symbols('n x y z w S2 S3 S4')
d=n-1
# Integrate second Gram-Schmidt column conditional on the first, using
# spherical quadratic-form moments in its (n-1)-dimensional orthocomplement.
t1=-x
t2=S2-2*y+x**2
t3=S3-3*z+3*x*y-x**3
t4=S4-4*w+4*x*z+2*y**2-4*x**2*y+x**4
v1=t1/d
v2=(t1*t1+2*t2)/(d*(d+2))
v3=(t1**3+6*t1*t2+8*t3)/(d*(d+2)*(d+4))
v4=(t1**4+12*t1*t1*t2+12*t2*t2+32*t1*t3+48*t4)/(d*(d+2)*(d+4)*(d+6))
q=sp.Poly(sp.expand(x**4+4*x**3*v1+6*x*x*v2+4*x*v3+v4),x,y,z,w,S2,S3,S4)
D2=n*(n+2);D3=D2*(n+4);D4=D3*(n+6)
M={
(4,0,0,0,0,0,0):(12*S2**2+48*S4)/D4,
(2,1,0,0,0,0,0):(2*S2**2+8*S4)/D3,
(2,0,0,0,1,0,0):2*S2**2/D2,
(1,0,1,0,0,0,0):2*S4/D2,
(1,0,0,0,0,1,0):sp.Integer(0),
(0,2,0,0,0,0,0):(S2**2+2*S4)/D2,
(0,1,0,0,1,0,0):S2**2/n,
(0,0,0,1,0,0,0):S4/n,
(0,0,0,0,2,0,0):S2**2,
(0,0,0,0,0,0,1):S4,
}
assert set(dict(q.terms()))==set(M)
expression=sp.factor(sum(c*M[mon] for mon,c in q.terms()))
target=48*((n*n+2*n+8)*S2**2+2*(n*n-6*n-8)*S4)/(n*(n-1)*(n+1)*(n+2)*(n+4)*(n+6))
assert sp.cancel(expression-target)==0
print('SYMBOLIC_ALL_DIMENSIONS_FOURTH_MOMENT_IDENTITY_OK')
var=sp.factor((1-2/d+3/(d*(d+2)))*2*S2/D2+2*(S2-2*S2/n)/(d*(d+2)))
var_target=4*(n-2)*S2/(n*(n-1)*(n+2))
assert sp.cancel(var-var_target)==0
print('SYMBOLIC_SECOND_MOMENT_NORMALIZATION_OK')
ratio=sp.factor(target/var_target**2)
K=3*n*(n-1)*(n+2)*((n*n+2*n+8)+2*(n*n-6*n-8)*S4/S2**2)/((n-2)**2*(n+1)*(n+4)*(n+6))
assert sp.cancel(ratio-K)==0
print('SYMBOLIC_NORMALIZED_KURTOSIS_IDENTITY_OK')
# Independent Dirichlet formula for squared coordinates of a random unit vector.
@lru_cache(None)
def dirichlet(a):
 nn=len(a); total=sum(a)
 v=sp.Integer(1)
 for e in a:v*=sp.rf(sp.Rational(1,2),e)
 return v/sp.rf(sp.Rational(nn,2),total)

def raw4(eigen):
 nn=len(eigen); U=sp.symbols('u:'+str(nn)); d0=nn-1
 X=sum(eigen[i]*U[i] for i in range(nn))
 Y=sum(eigen[i]**2*U[i] for i in range(nn))
 Z=sum(eigen[i]**3*U[i] for i in range(nn))
 W=sum(eigen[i]**4*U[i] for i in range(nn))
 val=q.as_expr().subs({n:nn,x:X,y:Y,z:Z,w:W,S2:sum(t*t for t in eigen),S3:sum(t**3 for t in eigen),S4:sum(t**4 for t in eigen)})
 poly=sp.Poly(val,*U)
 return sp.factor(sum(coef*dirichlet(exp) for exp,coef in poly.terms()))
for nn in [5,6,7,8,9,10]:
 test_sets=[[nn-1]+[-1]*(nn-1), [1,-1]+[0]*(nn-2), [1,1,-1,-1]+[0]*(nn-4)]
 for ev in test_sets:
  actual=raw4(ev)
  predicted=target.subs({n:nn,S2:sum(a*a for a in ev),S4:sum(a**4 for a in ev)})
  assert sp.factor(actual-predicted)==0,(nn,ev)
 print('INDEPENDENT_DIRICHLET_CROSS_CHECK_OK',nn)
for nn in range(5,201):
 B=sp.Rational(1,nn) if nn%2==0 else sp.Rational(nn*nn+3,nn*(nn*nn-1))
 U=sp.Rational(nn*nn-3*nn+3,nn*(nn-1))
 coeff=nn*nn-6*nn-8
 assert 0<B<U<1 and (coeff<0)==(nn<=7)
 kfun=lambda t:sp.factor(K.subs({n:nn,S2:1,S4:t}))
 kl,ku=sorted([kfun(B),kfun(U)])
 assert kl>0 and ku>kl
print('DIMENSION_TRANSITION_AND_EXACT_EXTREMAL_ORDER_OK n=5..200')
print('EXACT_CHECKS_PASSED')
