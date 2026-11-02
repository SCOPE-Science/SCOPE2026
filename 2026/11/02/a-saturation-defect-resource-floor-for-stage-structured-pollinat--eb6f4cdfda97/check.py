"""Exact symbolic and rational checks for a plant–larva–adult balance identity.

Requires SymPy. Numerical checks are corroboration, not an infinite proof.
"""
from fractions import Fraction as F
from random import Random
import sympy as s

x,y,z,alpha,eta,eps,gamma,beta,mu,nu,phi,sigma,xi=s.symbols('x y z alpha eta eps gamma beta mu nu phi sigma xi',positive=True)
q=gamma*beta
c=eps*alpha/eta
xstar=s.symbols('xstar',positive=True)
# Characteristic reproduction threshold relation:
threshold = s.Eq((c*xstar+phi)*q*xstar,nu*(mu+q*xstar))
K=1+mu/(q*xstar)
f1=x*(1-x)+sigma*alpha*x*z/(eta+z)-beta*x*y
f2=eps*alpha*x*z/(eta+z)+phi*z-(mu+q*x)*y
f3=q*x*y-nu*z
Wprime=s.factor(f2+K*f3)
target=(x-xstar)*(mu*y/xstar+c*z)-c*x*z*z/(eta+z)
# Substitute nu via the defining threshold; exact symbolic identity.
nu_by_root=q*xstar*(c*xstar+phi)/(mu+q*xstar)
assert s.factor((Wprime-target).subs(nu,nu_by_root))==0
assert s.simplify(s.diff(q*x*(c*x+phi)/(nu*(mu+q*x)),x)).is_positive is not False
assert s.simplify(f1/x-(1-x+sigma*alpha*z/(eta+z)-beta*y))==0

# Exact nontrivial equilibrium, and a positive saturation defect.
val={alpha:s.Rational(3,2),eta:s.Integer(1),eps:s.Rational(1,2),gamma:s.Rational(1,2),
     beta:s.Integer(2),mu:s.Integer(1),nu:s.Integer(1),phi:s.Integer(0),
     sigma:s.Rational(177,44),x:s.Integer(3),y:s.Rational(11,48),z:s.Rational(11,16),xstar:s.Integer(2)}
assert [s.factor(f.subs(val)) for f in (f1,f2,f3)]==[0,0,0]
assert s.factor((s.Integer(1)+mu/(q*xstar)).subs(val))==s.Rational(3,2)
assert s.factor(((x-xstar)*(mu*y/xstar+c*z)).subs(val))==s.Rational(121,192)
assert s.factor((c*x*z*z/(eta+z)).subs(val))==s.Rational(121,192)
assert s.factor((q*xstar*(c*xstar+phi)-nu*(mu+q*xstar)).subs(val))==0
assert s.factor((1+sigma*alpha).subs({**val,sigma:s.Rational(1,2)}))==s.Rational(7,4)

# Positive rational samples of the threshold identity, exact and independent.
rng=Random(434)
checks=0
for i in range(500):
    aa=F(rng.randrange(1,13),rng.randrange(1,9))
    ee=F(rng.randrange(1,10),rng.randrange(2,15))
    ep=F(rng.randrange(1,8),rng.randrange(8,17))
    gg=F(rng.randrange(1,8),rng.randrange(8,17))
    bb=F(rng.randrange(1,14),rng.randrange(1,9))
    mm=F(rng.randrange(1,15),rng.randrange(1,10))
    nn=F(rng.randrange(1,14),rng.randrange(1,10))
    pp=F(rng.randrange(0,9),rng.randrange(1,7))
    xx=F(rng.randrange(1,16),rng.randrange(1,8))
    yy=F(rng.randrange(1,16),rng.randrange(1,8))
    zz=F(rng.randrange(1,16),rng.randrange(1,8))
    qs=gg*bb
    cs=ep*aa/ee
    # Choose a threshold xstar, solve for nu>0 exactly.
    xs=F(rng.randrange(1,16),rng.randrange(1,8))
    ns=qs*xs*(cs*xs+pp)/(mm+qs*xs)
    kp=1+mm/(qs*xs)
    sigma_s=F(rng.randrange(1,14),rng.randrange(1,9))
    dy=ep*aa*xx*zz/(ee+zz)+pp*zz-(mm+qs*xx)*yy
    dz=qs*xx*yy-ns*zz
    direct=dy+kp*dz
    rhs=(xx-xs)*(mm*yy/xs+cs*zz)-cs*xx*zz*zz/(ee+zz)
    assert direct==rhs
    checks+=1
    assert cs*xx+pp>0 and xs>0 and kp>1
    checks+=1
print(f'Symbolic identity verified; exact positive-equilibrium example verified; {checks} positive rational assertions passed.')
