"""Reproduce the switching-trap two-time collective covariance formulas.

Requirements: Python 3, sympy, numpy, scipy. Run: python verify.py
This program provides independent algebraic and numerical checks; the theorem
and its infinite-time asymptotics are established analytically in RESULT.md.
"""
import math
import random
import sympy as sp
import numpy as np
from scipy.linalg import expm

a,b,r,D = sp.symbols('a b r D', positive=True)
Q=sp.Matrix([[-r,r],[r,-r]])
pi=sp.Matrix([sp.Rational(1,2), sp.Rational(1,2)])
A=Q-2*sp.diag(a,b)
A2=Q-4*sp.diag(a,b)
m=sp.simplify(-2*D*A.inv()*pi)
z=sp.simplify(-4*D*A2.inv()*m)
bar=sp.factor(sum(m))
var=sp.factor(sum(z)-bar**2)
w=sp.factor(4*(a*a*z[0]+b*b*z[1])-4*D*D)
K=2*a*b+r*(a+b)
J=4*a*b+r*(a+b)
P=4*a*b+3*r*(a+b)+2*r*r
var_expected=D**2*(a-b)**2*P/(K*K*J)
w_expected=4*D**2*r*(a-b)**2*(a+b+r)/(K*J)
assert sp.factor(var-var_expected)==0
assert sp.factor(w-w_expected)==0
assert sp.factor(bar-D*(a+b+2*r)/K)==0
c0=m-bar*pi
c1=z-bar*m
assert sp.factor(sum(c0))==0
assert sp.factor(sum(c1)-var)==0
u=sp.symbols('u')
G=sp.factor((sp.ones(1,2)*(u*sp.eye(2)-A).inv()*(c1+2*D*c0/(u+2*r)))[0])
poly=sp.factor((u*sp.eye(2)-A).det())
assert sp.factor(poly-(u*u+2*(a+b+r)*u+2*K))==0
# C'(0)=0 and C''(0)=-W from the asymptotic of the Laplace transform.
assert sp.limit(u**2*(G-var/u),u,sp.oo)==0
assert sp.factor(sp.limit(u**3*(G-var/u),u,sp.oo)+w)==0
# Environment pole's coefficient away from collision.
residue=sp.factor(sp.limit((u+2*r)*G,u,-2*r))
assert sp.factor(residue-D**2*(a-b)**2/(K*(2*a*b-r*(a+b))))==0
# At the collision (a,b,r,D)=(2,2/3,1,1), double pole is genuine.
sample={a:2,b:sp.Rational(2,3),r:1,D:1}
Gs=sp.factor(G.subs(sample)); U=sp.symbols('U')
explicit=sp.Rational(79,600)/(u+2)+sp.Rational(1,5)/(u+2)**2-sp.Rational(19,1600)/(u+sp.Rational(16,3))
assert sp.factor(Gs-explicit)==0
assert sp.factor(var.subs(sample)-sp.Rational(23,192))==0
assert sp.factor(w.subs(sample)-sp.Rational(11,18))==0
checks=11
rng=random.Random(410026)
for k in range(350):
    aa,bb,rr,dd=[10**rng.uniform(-1.5,1.5) for j in range(4)]
    if abs(aa-bb)<1e-8: continue
    qn=np.array([[-rr,rr],[rr,-rr]],float)
    An=qn-2*np.diag([aa,bb]); A2n=qn-4*np.diag([aa,bb])
    pin=np.ones(2)/2
    mn=np.linalg.solve(-An,2*dd*pin)
    zn=np.linalg.solve(-A2n,4*dd*mn)
    mean=mn.sum()
    c0n=mn-mean*pin
    c1n=zn-mean*mn
    Vn=zn.sum()-mean**2
    Wn=4*(aa*aa*zn[0]+bb*bb*zn[1])-4*dd**2
    Kn=2*aa*bb+rr*(aa+bb); Jn=4*aa*bb+rr*(aa+bb)
    Vformula=dd**2*(aa-bb)**2*(4*aa*bb+3*rr*(aa+bb)+2*rr**2)/(Kn**2*Jn)
    Wformula=4*dd**2*rr*(aa-bb)**2*(aa+bb+rr)/(Kn*Jn)
    assert math.isclose(Vn,Vformula,rel_tol=2e-8,abs_tol=1e-9)
    assert math.isclose(Wn,Wformula,rel_tol=3e-8,abs_tol=1e-8)
    ell=math.sqrt(rr*rr+(aa-bb)**2)
    a1,a2=rr+aa+bb-ell,rr+aa+bb+ell
    # The exact 4x4 block system is independent of the scalar 3-mode formula.
    B=np.zeros((4,4)); B[:2,:2]=qn;B[2:,2:]=An;B[2:,:2]=2*dd*np.eye(2)
    for tt in [0,.07,.4,1.3,3.5]:
        target=(expm(tt*B)@np.r_[c0n,c1n])[2:].sum()
        if abs(a1-2*rr)>1e-5*max(1,rr):
            C1=(a2*(2*rr)*Vformula-Wformula)/((a2-a1)*(2*rr-a1))
            C2=(a1*(2*rr)*Vformula-Wformula)/((a1-a2)*(2*rr-a2))
            Cs=(a1*a2*Vformula-Wformula)/((a1-2*rr)*(a2-2*rr))
            predicted=C1*math.exp(-a1*tt)+C2*math.exp(-a2*tt)+Cs*math.exp(-2*rr*tt)
            assert math.isclose(target,predicted,rel_tol=1e-5,abs_tol=3e-8),(aa,bb,rr,tt,target,predicted)
            checks+=1
        assert target>=-1e-8
    checks+=3
for tt in [0,.03,.2,.7,2,5]:
    C=math.exp(-2*tt)*(79/600+tt/5)-(19/1600)*math.exp(-16*tt/3)
    assert C>0
    checks+=1
print(f'All {checks} independent symbolic and numerical checks passed.')
