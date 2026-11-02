"""Reproduce exact algebraic identities and finite diagnostic tests for the
period-two stability frontier of variable-step four-step BDFL.
Requires Python 3.10+, sympy and numpy. No network or external data.
Analytical inequalities in RESULT.md, not finite tests, prove the theorem.
"""
import math
import numpy as np
import sympy as sp

r,z=sp.symbols('r z',positive=True); x=sp.symbols('lam')
rt=sp.sqrt(2)
a,b,c=62+6*rt,24-40*rt,5-22*rt
p=(-5+22*rt)/41
q=(-7-2*rt)/41
alpha2=2*(1+12*rt)/41
alpha3=-2*(18+11*rt)/41
u=(a*r*r+b*r+c)/(41*(4*r+3))
v=(c*r*r+b*r+a)/(41*r*(3*r+4))

# Independently reconstruct alpha0 and alpha1 from polynomial order-two
# consistency on the exactly alternating mesh.
def reconstructed(h,prev):
    cc=[sp.Integer(0)]
    for j in range(4):
        cc.append(cc[-1]+(prev if j%2==0 else h)/h)
    t=lambda j: cc[j]**2-2*cc[4]*cc[j]
    alpha1=-(t(2)*alpha2+t(3)*alpha3+t(4))/t(1)
    alpha0=-(alpha1+alpha2+alpha3+1)
    beta4=sum(cc[j]*val for j,val in [(0,alpha0),(1,alpha1),(2,alpha2),(3,alpha3),(4,1)])
    return cc,alpha0,alpha1,beta4

checks=0
def eq(lhs,rhs):
    global checks
    assert sp.cancel(lhs-rhs)==0,(lhs,rhs)
    checks+=1
for h,prev,w in [(r,sp.Integer(1),u),(sp.Integer(1),r,v)]:
    cc,alpha0,alpha1,beta4=reconstructed(h,prev)
    eq(alpha0,w)
    eq(1+alpha3+alpha2+alpha1+alpha0,0)
    eq(sum(cc[j]*val for j,val in [(0,alpha0),(1,alpha1),(2,alpha2),(3,alpha3),(4,1)]),beta4)
    eq(sum(cc[j]**2*val/2 for j,val in [(0,alpha0),(1,alpha1),(2,alpha2),(3,alpha3),(4,1)]),cc[4]*beta4)

# Difference-state recurrence: [d_(n+1),d_n,d_(n-1)]^T=C(w)[d_n,d_(n-1),d_(n-2)]^T.
w1,w2=sp.symbols('w1 w2')
def C(w): return sp.Matrix([[p,q,w],[1,0,0],[0,1,0]])
P_generic=C(w1)*C(w2)
tr=p**2+2*q
E=q**2-p*(w1+w2)
char_expected=x**3-tr*x**2+E*x-w1*w2
assert sp.expand(P_generic.charpoly(x).as_expr()-char_expected)==0
checks+=1

# Symmetric expressions in the alternating step ratio s=r+1/r.
D=1681*(12*z+25)
Su=82*((93+9*rt)*z**2+(170-92*rt)*z-75-244*rt)/D
V=((46-1334*rt)*z**2+(2888-3064*rt)*z+8593+1272*rt)/D
eq((u+v),Su.subs(z,r+1/r))
eq(u*v,V.subs(z,r+1/r))
eq(tr,(419-384*rt)/1681)

# Exact Schur inequalities: |V|<1, 1-tr+E-V>0, 1+tr+E+V>0,
# 1-E+tr*V-V^2>0, with E=q^2-p*Su.
Cplus=1-tr+(q**2-p*(u+v))-u*v
Cminus=1+tr+(q**2-p*(u+v))+u*v
F=r**4+((65-82*rt)/23)*(r**3+r)+(3-179*rt/23)*r**2+1
Cp_fact=(92-2668*rt)*(r+1)**2*(r*r-(2+98*rt/23)*r+1)/(1681*r*(3*r+4)*(4*r+3))
Cm_fact=(184-5336*rt)*F/(1681*r*(3*r+4)*(4*r+3))
eq(Cplus,Cp_fact)
eq(Cminus,Cm_fact)

# Frozen companion with four levels has determinant equal to the
# constant term of its reduced difference cubic; the r=4 phase fails.
u4=sp.factor(u.subs(r,4))
eq(u4,(1093-86*rt)/779)
assert float(u4)>1
checks+=1

s0=float(((82*rt-65)/23+sp.sqrt(((65-82*rt)/23)**2-4*(1-179*rt/23)))/2)
# Equivalent formula directly from s^2+A*s+B-2=0.
Aq=(65-82*rt)/23; Bq=3-179*rt/23
sstar=sp.simplify((-Aq+sp.sqrt(Aq**2-4*(Bq-2)))/2)
R=(sstar+sp.sqrt(sstar**2-4))/2
Rfloat=float(R)
assert 4<Rfloat<4.25
assert abs(Rfloat-4.222826044904903)<1e-12
checks+=2

def companion(wf):
    # The four-state companion; its eigenvalues include 1.
    a0=float(wf)
    a1=float(-1-alpha3-alpha2)-a0
    return np.array([[-float(alpha3),-float(alpha2),-a1,-a0],
                     [1,0,0,0],[0,1,0,0],[0,0,1,0]],float)

# Independent eigenvalue diagnostics across the exact frontier.
for rr in np.r_[np.linspace(.1,.95,75),np.linspace(1.05,10,180)]:
    U=float(u.subs(r,float(rr)))
    VV=float(v.subs(r,float(rr)))
    PP=companion(U)@companion(VV)
    ev=np.linalg.eigvals(PP)
    parasitic=[e for e in ev if abs(e-1)>1e-7]
    assert len(parasitic)==3
    stable=max(abs(e) for e in parasitic)<1
    predicted=1/Rfloat<float(rr)<Rfloat
    assert stable==predicted,(rr,ev,predicted)
    checks+=1

for rr in [sp.Rational(1,2),1,2,sp.Rational(9,2),5]:
    uu=float(u.subs(r,rr));vv=float(v.subs(r,rr))
    spectrum=np.linalg.eigvals(companion(uu)@companion(vv))
    assert abs(np.prod(spectrum)-uu*vv)<1e-8
    checks+=1

print('PASS:',checks,'symbolic and finite tests; R=',format(Rfloat,'.15f'))
