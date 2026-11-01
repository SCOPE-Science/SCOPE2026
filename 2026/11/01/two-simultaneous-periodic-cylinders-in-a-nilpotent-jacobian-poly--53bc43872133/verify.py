"""Standalone executable checks for the stated polynomial-flow identities.
These finite checks complement, and do not replace, the analytical proof.
Run with python verify.py after pip install -r requirements.txt.
"""
from math import sqrt, pi, cos, sin
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

x,y,z,k,r = sp.symbols('x y z k r', real=True)
s=y+x*x
g=s*s-k
F=sp.Matrix([g,z-2*x*g,g*g-r*r])
J=F.jacobian([x,y,z])
assert all(sp.simplify(a)==0 for a in J**3), 'non-nilpotent Jacobian'
u,v,w=sp.symbols('u v w',real=True)
# Conjugacy, applied to time derivatives of v=y+x^2.
assert sp.simplify(F[1]+2*x*F[0]-z)==0
U=-v**5/sp.Integer(5)+2*k*v**3/sp.Integer(3)+(r*r-k*k)*v
assert sp.simplify(sp.diff(U,v) - (r*r-(v*v-k)**2))==0
assert sp.simplify(w*sp.diff(U,v)+w*((v*v-k)**2-r*r))==0

def P(t,k=2.,r=1.):
    return -t**5/5+2*k*t**3/3+(r*r-k*k)*t

def integral(E,side,k=2.,r=1.):
    a,b=sqrt(k-r),sqrt(k+r)
    if side=='left':
        vl=brentq(lambda t:P(t,k,r)-E,-b-10*(k+r+1),-b-1e-10)
        vr=brentq(lambda t:P(t,k,r)-E,-b+1e-10,-a-1e-10)
    else:
        vl=brentq(lambda t:P(t,k,r)-E,-a+1e-10,a-1e-10)
        vr=brentq(lambda t:P(t,k,r)-E,a+1e-10,b-1e-10)
    center=(vl+vr)/2
    radius=(vr-vl)/2
    def integrands(t):
        if t<5e-5: 
            v0=vr
            timeweight=2*sqrt(radius/(r*r-(v0*v0-k)**2))
        elif pi-t<5e-5:
            v0=vl
            timeweight=2*sqrt(radius/((v0*v0-k)**2-r*r))
        else:
            v0=center+radius*cos(t)
            timeweight=sqrt(2)*radius*sin(t)/sqrt(E-P(v0,k,r))
        return timeweight,(v0*v0-k)*timeweight
    T=quad(lambda t:integrands(t)[0],0,pi,epsabs=1e-9,limit=200)[0]
    D=quad(lambda t:integrands(t)[1],0,pi,epsabs=1e-9,limit=200)[0]
    return T,D

for k0,r0 in [(2.,1.),(3.,1.),(5.,2.)]:
    assert k0>=1.5*r0
    a,b=sqrt(k0-r0),sqrt(k0+r0)
    assert abs(P(b,k0,r0)-4*(k0+r0)**1.5*(3*r0-2*k0)/15)<1e-11
    assert abs(P(-a,k0,r0)-4*(k0-r0)**1.5*(2*k0+3*r0)/15)<1e-11
    for side,E1,E2 in [('left',P(-b,k0,r0),P(-a,k0,r0)),
                       ('right',P(a,k0,r0),P(b,k0,r0))]:
        f=lambda E:integral(E,side,k0,r0)[1]
        A=E1+(E2-E1)*0.0001
        B=E1+(E2-E1)*0.9999
        assert f(A)*f(B)<0, f'no bracket for {k0},{r0},{side}'
        root=brentq(f,A,B,xtol=1e-11)
        T,D=integral(root,side,k0,r0)
        assert T>0 and abs(D)<1e-6
        print(f'k={k0:g} r={r0:g} {side:5} E={root:.11f} T={T:.11f} D={D:.3g}')
print('CHECK_OK')
