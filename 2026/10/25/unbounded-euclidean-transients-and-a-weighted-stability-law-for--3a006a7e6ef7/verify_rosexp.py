#!/usr/bin/env python3
"""Exact and floating-point checks for a partitioned Rosenbrock-exponential stability theorem.
Usage: python verify_rosexp.py
This checker supplements, but does not replace, the analytical matrix proof.
"""
import math
import sympy as s
import numpy as np

x=s.symbols('x',positive=True)
L=s.diag(1+x/2,1)
R=s.diag(1-x/2,1)
E=s.Matrix([[s.Rational(3,4),-s.Rational(1,4)],[-s.Rational(1,4),s.Rational(3,4)]])
X=s.diag(-x,0)
Y=s.Matrix([[-s.log(2)/2,-s.log(2)/2],[-s.log(2)/2,-s.log(2)/2]])
M=s.simplify(L.inv()*E*R)
expected=s.Matrix([[s.Rational(3,4)*(1-x/2)/(1+x/2),-s.Rational(1,4)/(1+x/2)],[-s.Rational(1,4)*(1-x/2),s.Rational(3,4)]])
assert s.simplify(M-expected)==s.zeros(2)
assert s.simplify(L*M*L.inv()-E*(L.inv()*R))==s.zeros(2)
assert s.simplify(M.det()-(1-x/2)/(2*(1+x/2)))==0
assert s.simplify(M.trace()-s.Rational(3,4)*(1+(1-x/2)/(1+x/2)))==0
assert s.simplify((M/x).applyfunc(lambda z: s.limit(z,x,s.oo))-s.Matrix([[0,0],[s.Rational(1,8),0]]))==s.zeros(2)
M16=M.subs(x,16)
assert M16==s.Matrix([[-s.Rational(7,12),-s.Rational(1,36)],[s.Rational(7,4),s.Rational(3,4)]])
assert s.simplify((M16.T*M16)[0,0]-s.Rational(245,72))==0
assert s.simplify(M16.charpoly().as_expr()-(s.Symbol('lambda')**2-s.Symbol('lambda')/6-s.Rational(7,18)))==0
lams={s.simplify(v) for v in M16.eigenvals()}
assert lams=={(1+s.sqrt(57))/12,(1-s.sqrt(57))/12}
print('PASS exact symbolic identities, witness and limits')

# Independent matrix-formula check on random symmetric dissipative pairs.
rng=np.random.default_rng(129731)
count=0
for n in [2,3,5]:
  for _ in range(150):
    G=rng.standard_normal((n,n)); F=rng.standard_normal((n,n))
    A=-(G.T@G)/n; B=-(F.T@F)/n
    h=rng.uniform(.01,6)
    Xh=h*A; Yh=h*B
    Evals,V=np.linalg.eigh(Yh)
    EE=(V*np.exp(Evals))@V.T
    phis=np.where(abs(Evals)<1e-8,1+Evals/2,(np.expm1(Evals))/Evals)
    Phi=(V*phis)@V.T
    Lh=np.eye(n)-Xh/2
    from_formula=np.eye(n)+np.linalg.solve(Lh, ((EE+np.eye(n))/2)@Xh+(Phi@Yh))
    from_factored=np.linalg.solve(Lh, EE@(np.eye(n)+Xh/2))
    assert np.allclose(from_formula,from_factored,atol=2e-12,rtol=1e-12)
    C=np.linalg.solve(Lh,np.eye(n)+Xh/2)
    assert np.linalg.norm(EE@C,2)<1+2e-12
    assert max(abs(np.linalg.eigvals(from_factored)))<1+2e-12
    count+=1
print(f'PASS {count} random symmetric-dissipative matrix identities and spectral sanity checks')

# Contrast of original and reversed operator order, evaluated for the exact witness.
h=1.; Efloat=np.array(E,float); Yi=np.array(Y,float)
w,U=np.linalg.eigh(Yi)
P=(U*np.array([(math.expm1(float(u))/float(u) if abs(u)>1e-12 else 1.) for u in w]))@U.T
for t in (4,16,64,256,1024):
    Xh=np.diag([-float(t),0.]); Lh=np.eye(2)-Xh/2
    m1=np.linalg.solve(Lh,Efloat@(np.eye(2)+Xh/2))
    m2=np.eye(2)+.5*(Efloat+np.eye(2))@np.linalg.solve(Lh,Xh)+P@np.linalg.solve(Lh,Yi)
    assert np.linalg.norm(m1,2)>=float(t)/8-.25-1e-10
    assert np.linalg.norm(m2,2)<=3+math.log(2)+1e-10
    assert max(abs(np.linalg.eigvals(m1)))<1
    assert np.linalg.norm(np.linalg.matrix_power(m1,200),2)<1e-8
print('PASS reversed-order uniform bound and stiffness-growing transient checks')
