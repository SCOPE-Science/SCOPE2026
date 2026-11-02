"""Independent algebraic and numerical checks for a three-state exchange spectrum.
Run: python verify_tristate.py  (requires sympy, numpy, scipy).
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq

w,k,d=sp.symbols('w k d',real=True,positive=True)
x,y=sp.symbols('x y',real=True)
Q=sp.Matrix([[-k,k,0],[k,-2*k,k],[0,k,-k]])
F=sp.diag(-d,0,d)
p=sp.ones(1,3)/3
M=sp.I*w*sp.eye(3)-Q+sp.I*F
res=sp.factor((p*M.inv()*sp.ones(3,1))[0])
D=w**2*(d**2+3*k**2-w**2)**2+4*k**2*(2*w**2-d**2)**2
S=2*d**2*k*(d**2+9*k**2+w**2)/(3*D)
assert sp.simplify(sp.re(res).expand(complex=True)-S)==0
N=1+9*y+x
Den=x*(1+3*y-x)**2+4*y*(2*x-1)**2
P=sp.expand(sp.diff(Den,x)*N-Den)
assert sp.expand(P-(2*x**3+(1+37*y)*x**2+(180*y**2-16*y-4)*x+81*y**3-81*y**2-5*y+1))==0
c=sp.factor(P.subs(x,0))
assert sp.expand(sp.discriminant(P,x)-16*(6*y+1)**2*(4913*y**3+447*y**2-21*y+17))==0
assert sp.expand((180*y**2-16*y-4)-4*(5*y-1)*(9*y+1))==0
assert c.subs(y,0)>0 and c.subs(y,sp.Rational(1,5))<0 and c.subs(y,2)>0
# Two positive roots of the exact cubic c(y), with isolating intervals.
yminus=brentq(sp.lambdify(y,c,'numpy'),.08,.1,xtol=1e-15)
yplus=brentq(sp.lambdify(y,c,'numpy'),1.04,1.06,xtol=1e-15)
assert .087<yminus<.088 and 1.047<yplus<1.048

def exact_shape(q,delta,omega):
    den=omega**2*(delta**2+3*q*q-omega**2)**2+4*q*q*(2*omega**2-delta**2)**2
    return 2*delta**2*q*(delta**2+9*q*q+omega**2)/(3*math.pi*den)

def matrix_shape(q,delta,omega):
    QQ=np.array([[-q,q,0],[q,-2*q,q],[0,q,-q]],float)
    FF=np.diag([-delta,0,delta])
    return np.real(np.full(3,1/3)@np.linalg.solve(1j*omega*np.eye(3)-QQ+1j*FF,np.ones(3)))/math.pi

rng=np.random.default_rng(26473)
errors=[]
for _ in range(120):
    delta=math.exp(rng.uniform(-2,2));q=math.exp(rng.uniform(-3,2))*delta
    omega=rng.uniform(-3,3)*delta
    a=exact_shape(q,delta,omega);b=matrix_shape(q,delta,omega)
    errors.append(abs(a-b)/max(abs(a),abs(b),1e-15))
assert max(errors)<1e-10
# Independent root-based shape checks and signs for 3/2/1 regions
regions=[(.1,3),(.25,3),(.295,3),(.3,2),(.65,2),(1.,2),(1.03,1),(1.3,1),(3.,1)]
for r,expected in regions:
    yy=r*r
    zroots=np.roots([2,1+37*yy,180*yy**2-16*yy-4,float(c.subs(y,yy))])
    positive=[float(z.real) for z in zroots if abs(z.imag)<1e-7 and z.real>1e-9]
    # For a positive central curvature there is one central maximum and the
    # two positive x-roots form a minimum and a side-pair of maxima.
    if float(c.subs(y,yy))>0:
        assert len(positive) in (0,2)
        observed=1+(2 if len(positive)==2 else 0)
    else:
        assert len(positive)==1
        observed=2
    assert observed==expected,(r,expected,observed,positive)
print('symbolic resolvent identity PASS')
print('symbolic derivative and discriminant PASS')
print('two positive cubic thresholds isolated PASS')
print('120 direct complex-resolvent numerical tests PASS; maximum relative error %.3g'%max(errors))
print('9 independent root-count classification tests PASS')
print('low critical rate k/delta: %.12f'%math.sqrt(yminus))
print('high critical rate k/delta: %.12f'%math.sqrt(yplus))
print('cutoff cubic in y:',c)
