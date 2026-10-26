"""Reproducible consistency checks for the three-eigenvalue BLD/spectral mismatch.
Only verifies identities and finite sampled cases; universal statements rest on the written proof.
"""
import math
import numpy as np
import sympy as sp

z, u, eps, M, w = sp.symbols('z u eps M w', positive=True)
phi = lambda y: y-sp.log(y)-1
assert sp.simplify(sp.diff(z-sp.log(z)-1,z)-(z-1)/z)==0
assert sp.simplify(sp.diff(-M+M/u+sp.log(u),u)-(u-M)/u**2)==0
assert sp.simplify((-M+M/u+sp.log(u)).subs(u,M)+phi(M))==0
assert sp.simplify((M-1/M-2*sp.log(M)).diff(M)-(M-1)**2/M**2)==0

# Sherman--Morrison determinant and trace terms symbolically, with exact rational data.
S=sp.diag(sp.Rational(1,20),1,6)
v=sp.Matrix([sp.Rational(1,3),sp.Rational(2,3),sp.Rational(2,3)])
P=sp.eye(3)+w*v*v.T
inv_SM=sp.eye(3)-(w/(1+w))*v*v.T
assert sp.simplify(P*inv_SM-sp.eye(3))==sp.zeros(3)
assert sp.factor(P.det())==w+1
assert sp.simplify(sp.trace(S*inv_SM)-(sp.trace(S)-w*sp.trace(S*v*v.T)/(1+w)))==0

# Strict BLD choice M=6, eps=1/20 and exact pencil condition ratios.
e=.05;m=6.
assert phi(6).evalf()>phi(sp.Rational(1,20)).evalf()
assert m<1/e
P_BLD=sp.diag(1,1,6)
P_cond=sp.diag(sp.Rational(1,20),1,1)
assert list((P_BLD.inv()*S).diagonal())==[sp.Rational(1,20),1,1]
assert list((P_cond.inv()*S).diagonal())==[1,1,6]
assert sp.Rational(20,6)==sp.Rational(10,3)

# Numerical root and the sharp (strict-choice) gap for a fixed upper eigenvalue.
def f(x):return x-math.log(x)-1
for m in [1.1,2,6,10,30]:
    lo=1e-15; hi=1/m
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)>f(m):lo=mid
        else:hi=mid
    root=(lo+hi)/2
    assert 0<root<1/m
    assert abs(f(root)-f(m))<1e-6
    for e in [root*.9,(root+1/m)/2,(1/m+1)/2]:
        bld_M=f(m)>f(e)
        opt_M=(m>1/e)
        if root<e<1/m:assert bld_M and not opt_M
        if e<root:assert (not bld_M) and (not opt_M)
        if e>1/m:assert bld_M and opt_M

# Finite random signed rank-one preconditioners stay above the analytic global infimum.
rng=np.random.default_rng(923)
S=np.diag([.05,1.,6.]); bound=6.
for k in range(1200):
    v=rng.normal(size=3);v=v/np.linalg.norm(v)
    w=(rng.random()*.999-0.999) if (k%2) else rng.random()*70
    P=np.eye(3)+w*np.outer(v,v)
    L=np.linalg.cholesky(P)
    eig=np.linalg.eigvalsh(np.linalg.solve(L,S)@np.linalg.inv(L.T))
    assert eig[-1]/eig[0] >= bound-2e-9

for m in (8,16,64,256):
    e=m**-2
    assert f(m)>f(e)
    assert abs((1/e)/m-m)<1e-8
print('VERIFY_OK: identities, transitions, exact rational case, and 1200 sampled updates')
