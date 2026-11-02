"""Standalone algebraic and numerical checks for a two-dimensional Langevin Euler scheme.

All mathematical proofs are in RESULT.md; these checks independently reconstruct
second-moment evolution, symbolic formulae, and sample limiting regimes.
Requires Python 3, sympy, numpy.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

lam,c,h=sp.symbols('lam c h',positive=True,real=True)
m=1+c; n=lam+c
A1=1-m*h; A2=1-n*h
T=sp.Matrix([[A1*A1,2*c*h],[2*c*h,A2*A2]])
D=sp.factor((sp.eye(2)-T).det()/h**2)
Dclaim=m*n*(2-m*h)*(2-n*h)-4*c*c
assert sp.simplify(D-Dclaim)==0
R=sp.sqrt((1-lam)**2+4*c*c)
hstar=(1+lam+2*c-R)/(m*n)
assert sp.simplify(Dclaim.subs(h,hstar))==0
u=(2*n*(2-n*h)+4*c*lam)/Dclaim
v=(4*c+2*lam*m*(2-m*h))/Dclaim
z=sp.Matrix([u,v])
assert all(sp.simplify(s)==0 for s in ((sp.eye(2)-T)*z - sp.Matrix([2*h,2*h*lam])))
assert sp.simplify(u.subs(h,0)-1)==0
assert sp.simplify(v.subs(h,0)-1)==0
assert sp.simplify(hstar.subs(c,1)-(3+lam-sp.sqrt((1-lam)**2+4))/(2*(1+lam)))==0
hgold=(sp.Integer(3)-sp.sqrt(5))/2
assert sp.simplify(hstar.subs({c:1,lam:0})-hgold)==0
assert sp.simplify(v.subs(c,1).subs(lam,0)-1/(1-3*h+h*h))==0
assert sp.simplify(u.subs(c,1).subs(lam,0)-(2-h)/(2*(1-3*h+h*h)))==0
assert sp.limit(hstar.subs(lam,0),c,0,dir='+')==2
assert sp.limit(c**2*hstar.subs(lam,0),c,sp.oo)==1

rng=np.random.default_rng(1729)
count=0
for i in range(1500):
    lv=10.0**rng.uniform(-4.0,0.0)
    cv=10.0**rng.uniform(-4.0,4.0)
    mv,nv=1+cv,lv+cv
    RR=math.hypot(1-lv,2*cv)
    # Rationalized root avoids catastrophic cancellation.
    H=4*(lv+cv*(1+lv))/(mv*nv*(mv+nv+RR))
    step=H*rng.uniform(.002,1.4)
    B=np.diag([1-mv*step,1-nv*step])
    J=np.array([[0.0,1.0],[-1.0,0.0]])
    Q=math.sqrt(2*step*cv)*J
    M=np.array([[B[0,0]**2,2*step*cv],[2*step*cv,B[1,1]**2]])
    # Independent full 3x3 symmetric covariance representation.
    basis=[np.array([[1.,0.],[0.,0.]]), np.array([[0.,.5],[.5,0.]]), np.array([[0.,0.],[0.,1.]])]
    Cmat=np.zeros((3,3))
    for j,C in enumerate(basis):
        Cp=B@C@B.T+Q@C@Q.T
        Cmat[:,j]=[Cp[0,0],2*Cp[0,1],Cp[1,1]]
    r_full=max(abs(np.linalg.eigvals(Cmat)))
    r_diag=max(abs(np.linalg.eigvals(M)))
    assert abs(r_full-r_diag)<4.e-8*max(1,r_diag)
    assert (r_full<1-1.e-9)==(step<H) or abs(r_full-1)<1.e-9
    if step<H and (1-r_full)>1.e-8:
        q=np.array([2*step,2*step*lv])
        sol=np.linalg.solve(np.eye(2)-M,q)
        dd=mv*nv*(2-mv*step)*(2-nv*step)-4*cv*cv
        # robust closed form from Cramer's rule
        ex=np.array([(2*nv*(2-nv*step)+4*cv*lv)/dd,(4*cv+2*lv*mv*(2-mv*step))/dd])
        assert np.max(abs(sol-ex)) < 4.e-7*max(1,np.max(abs(ex)))
        assert sol[0]>1-1.e-8 and sol[1]>1-1.e-8
    count+=1

# Exact-rational sample checks independently via 3x3 matrix and formula.
for lv,cv,hh in [(sp.Rational(1,2),1,sp.Rational(1,5)),(sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,10)),(1,1,sp.Rational(1,4)),(sp.Rational(1,100),sp.Rational(1,10),sp.Rational(1,20))]:
    TT=T.subs({lam:lv,c:cv,h:hh})
    zz=(sp.eye(2)-TT).inv()*sp.Matrix([2*hh,2*hh*lv])
    assert all(sp.simplify(a-b)==0 for a,b in zip(zz,z.subs({lam:lv,c:cv,h:hh})))

print('PASS: exact determinant, h-star polynomial, stationary covariance, stiff-limit identities')
print('PASS: 1500 independent full-covariance spectral tests and stable/unstable comparisons')
print('PASS: 4 exact-rational invariant second-moment systems')
print('h-star at c=1 lambda->0:',float(hgold))
