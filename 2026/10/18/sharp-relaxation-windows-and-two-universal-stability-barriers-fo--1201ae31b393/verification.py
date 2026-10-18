#!/usr/bin/env python3
"""Exact symbolic and sampled checks of a scalar four-term splitting stability calculation."""
import sympy as S
import math
import random

u,v,tau=S.symbols('u v tau', real=True)
b=(1+v)/2
a=(1-u)/(2*(1+u))
c=1/(1+u)
M=S.Matrix([[b,a],[tau*b,1-tau/2]])
T=S.factor(S.trace(M)); D=S.factor(M.det())
assert S.simplify(T-(v+3-tau)/2)==0
assert S.simplify(D-(1+v)*(1-tau/(1+u))/2)==0
assert S.simplify(1-T+D-tau*(u-v)/(2*(1+u)))==0
assert S.simplify(1+T+D-(v+3-tau*(u+v+2)/(2*(1+u))))==0
assert S.simplify(1-D-((1-v)+tau*(1+v)/(1+u))/2)==0
lower=(v-1)*(1+u)/(v+1)
upper=2*(1+u)*(v+3)/(u+v+2)
uc=v+8+16/(v-1)
assert S.factor(lower-upper) == S.factor((v-1)*(u-uc)*(1+u)/((v+1)*(u+v+2)))
assert S.simplify(lower.subs(u,uc)-(v+7))==0
assert S.simplify(upper.subs(u,uc)-(v+7))==0
Mc=S.simplify(M.subs({u:uc,tau:v+7}))
assert S.simplify((Mc+S.eye(2))**2)==S.zeros(2)
assert S.simplify(Mc+S.eye(2)) != S.zeros(2)
crit=(S.Integer(5)+S.sqrt(57))/2
assert S.simplify(crit**2-5*crit-8)==0
assert S.simplify((crit-1)-6*(1+crit)/(crit+2))==0

# Real original map is computed independently of matrix form.
def algorithm(uv,vv,tv,y,z):
    x=z/(1+uv)
    yp=(2*x-z)/2+(1+vv)*y/2
    zp=z+tv*(yp-x)
    return yp,zp,x

def rho(uv,vv,tv):
    mat=[[float(b.subs(v,vv)),float(a.subs(u,uv))],[tv*float(b.subs(v,vv)),1-tv/2]]
    tr=mat[0][0]+mat[1][1]; det=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    disc=tr*tr-4*det
    if disc<0: return math.sqrt(det)
    return max(abs((tr+math.sqrt(disc))/2),abs((tr-math.sqrt(disc))/2))

r=random.Random(5421)
for k in range(1000):
    uv=10**r.uniform(-1,2); vv=uv*r.random(); tv=10**r.uniform(-2,2)
    yy=r.uniform(-2,2); zz=r.uniform(-2,2)
    yp,zp,x=algorithm(uv,vv,tv,yy,zz)
    assert abs(yp-(float(b.subs(v,vv))*yy+float(a.subs(u,uv))*zz))<1e-9
    assert abs(zp-(tv*float(b.subs(v,vv))*yy+(1-tv/2)*zz))<1e-9
    lo=max(0,(vv-1)*(1+uv)/(1+vv)); hi=2*(1+uv)*(vv+3)/(uv+vv+2)
    pred=(lo<tv<hi)
    exact=(rho(uv,vv,tv)<1-1e-12)
    assert pred==exact, (k,uv,vv,tv,lo,hi,pred,exact)

# Purely rational counterexamples: one stable and one unattainable.
for uv,vv,tv,stable in [(S.Rational(16),S.Rational(5),S.Rational(23,2),True),
                         (S.Rational(20),S.Rational(5),S.Rational(10),False),
                         (S.Rational(17),S.Rational(5),S.Rational(12),False),
                         (S.Rational(30),S.Rational(2),S.Rational(10),False)]:
    Mi=M.subs({u:uv,v:vv,tau:tv})
    eig=[complex(x.evalf()) for x in Mi.eigenvals().keys()]
    spectral=max(abs(x) for x in eig)
    if stable: assert spectral<1
    else: assert spectral>=1-1e-12

# Strong-curvature critical Jordan block and robust-limits tests
assert S.simplify(M.subs({u:17,v:5,tau:12})+S.eye(2))!=S.zeros(2)
assert (M.subs({u:17,v:5,tau:12})+S.eye(2))**2==S.zeros(2)
for uv in [0.1,0.9,1,1.1,2,5,6,6.2,6.3,8,16,17,18,30]:
    # robust feasible iff uv < crit
    low=max(0,uv-1) if uv>1 else 0
    up0=6*(1+uv)/(uv+2)
    if uv>1: assert (low<up0)==(uv<float(crit))
    # pointwise feasibility over v-grid iff u<17; at u=17 with v=5 if allowed
    if uv>=17:
        assert uv>5 and not (max(0,4*(uv+1)/6)<2*(uv+1)*8/(uv+7))
# Genuine positive weak-concavity modulus in a globally strongly convex objective.
x=S.symbols('x',real=True)
p=-S.Rational(5,2)*x*x+S.Rational(5,2)*(1-S.cos(x))**2
p2=S.trigsimp(S.diff(p,x,2))
assert S.simplify(p2-(-5+5*(S.cos(x)-S.cos(2*x))))==0
assert S.simplify(p2.subs(x,0)+5)==0
# With c=cos(x), cos(x)-cos(2*x)= -2(c-1/4)^2+9/8.
cc=S.symbols('cc',real=True)
assert S.expand(-2*(cc-S.Rational(1,4))**2+S.Rational(9,8)- (cc-(2*cc**2-1)))==0
assert S.simplify((-5+5*S.Rational(9,8))-S.Rational(5,8))==0
assert S.simplify(20+(-5-10)-5)==0
# The exact nonlinear update's Jacobian at its minimizer is M(20,5,tau).
y,z=S.symbols('y z',real=True)
fp=S.Integer(20)
x0=z/(1+fp)
yp=S.Rational(1,2)*(2*x0-z)+S.Rational(1,2)*(y-S.diff(p,x).subs(x,y))
zp=z+tau*(yp-x0)
J=S.Matrix([yp,zp]).jacobian([y,z]).subs({y:0,z:0})
assert S.simplify(J-M.subs({u:20,v:5}))==S.zeros(2)
# The strict impossibility inequality at u=20,v=5 is rational.
assert S.simplify(lower.subs({u:20,v:5})-upper.subs({u:20,v:5}))>0
# Independent direct evaluation with dimensional stepsize alpha=beta=eta.
for k in range(200):
    eta=10**r.uniform(-1,1)
    U=10**r.uniform(-1,2)
    V=U*r.random()
    relaxation=10**r.uniform(-2,1.5)
    yy=r.uniform(-2,2);zz=r.uniform(-2,2)
    F=U/eta;P=V/eta
    xx=zz/(1+eta*F)
    gamma=eta/2
    yy2=(gamma/eta)*(2*xx-zz)+(gamma/eta)*(yy+eta*P*yy)
    zz2=zz+relaxation*(yy2-xx)
    yy1,zz1,_=algorithm(U,V,relaxation,yy,zz)
    assert abs(yy2-yy1)<1e-11 and abs(zz2-zz1)<1e-11
print('PASS: exact scalar and nonlinear-Jacobian identities; 1000 independent direct-step/Jury comparisons; 200 physical-scale matches; rational boundary tests; two universal thresholds')
