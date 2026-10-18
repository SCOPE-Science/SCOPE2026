"""Independent algebraic and finite-section checks for a one-bond Sobolev inequality.

The infinite-dimensional theorem requires the proof in RESULT.md.
Run: python verify.py
"""
from math import sqrt
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

checks = 0

def check(condition, label):
    global checks
    assert condition, label
    checks += 1

r,t=sp.symbols('r t', positive=True)
lam=(1-r)**2/r
g0=r/(1-r**2)
denom=1+(2*t-1)*r
A=r*(1+(t-1)*r)/((1-r)*denom)
B=t*r*r/((1-r)*denom)
G0=sp.factor(g0-(t-1)*(r/(1+r))**2/(1+2*(t-1)*r/(1+r)))
K=sp.factor(2*(1-r)/sp.sqrt(r)*A)
P=1+(t-2)*r+(t-1)*(2*t-1)*r*r
R=2/(2-t+sp.sqrt(t*(8-7*t)))
check(sp.simplify(G0-A)==0,'rank-one resolvent diagonal')
check(sp.simplify((lam+1+t-r)*A-t*B-1)==0,'source vertex recurrence')
check(sp.simplify((lam+1+t-r)*B-t*A)==0,'opposite vertex recurrence')
check(sp.simplify(K-2*sp.sqrt(r)*(1+(t-1)*r)/denom)==0,'point norm')
check(sp.simplify(sp.diff(K,r)-K*P/(2*r*(1+(t-1)*r)*denom))==0,'derivative')
check(sp.simplify(P.subs(r,R))==0,'critical point')
check(sp.simplify(P.subs(r,0))==1,'left derivative sign')
check(sp.simplify(P.subs(r,1)-2*t*(t-1))==0,'right derivative sign')

critical=(4-sp.sqrt(2))/7
rmin=4*sp.sqrt(2)-5
check(sp.simplify(R.subs(t,critical)-rmin)==0,'minimum localization radius')
check(sp.simplify(P.subs({r:rmin,t:critical}))==0,'localization stationary value')
check(sp.simplify(sp.diff(P,t).subs({r:rmin,t:critical}))==0,'localization double condition')

z=sp.symbols('z',positive=True)
Ksmall=K.subs({t:z*z,r:R.subs(t,z*z)})
Ks=sp.series(Ksmall,z,0,3).removeO()
check(sp.simplify(Ks-(2-2*sp.sqrt(2)*z+sp.Rational(9,2)*z*z))==0,'disconnected limit')
Knear=K.subs({t:1-z,r:R.subs(t,1-z)})
Kn=sp.series(Knear,z,0,4).removeO()
check(sp.simplify(Kn-(1+z*z/sp.Integer(2)-z**3))==0,'weak-defect onset')

for tau in [0.04,0.15,0.25,0.36,0.5,0.7,0.9,0.99]:
    rr=float(R.subs(t,tau))
    cf=float(K.subs({t:tau,r:rr}))
    opt=minimize_scalar(lambda x:-float(K.subs({t:tau,r:x})),bounds=(1e-6,1-1e-6),method='bounded',options={'xatol':1e-13})
    check(abs(opt.x-rr)<2e-6,'numeric optimizer radius')
    check(abs(-opt.fun-cf)<2e-9,'numeric optimizer norm')
    check(cf>1,'weak link improves embedding')
    A0=float(A.subs({t:tau,r:rr}));B0=float(B.subs({t:tau,r:rr}))
    half=max(180,int(np.ceil(35/(1-rr))))
    u=np.array([A0*rr**(-n) if n<=0 else B0*rr**(n-1) for n in range(-half,half+1)])
    Eu=np.sum(np.diff(u)**2)+(tau-1)*(u[half+1]-u[half])**2
    value=float(np.max(np.abs(u))**2/np.sqrt(np.sum(u*u)*Eu))
    check(abs(value-cf)<3e-11,'direct extremizer norm')
    check(abs(u[half]-np.max(u))<1e-8,'peak at 0')
    for k in range(1,9):
        center=g0-(t-1)*r*r/((1+r)*denom)
        remote=g0-(t-1)*r*r*r**(2*k)/((1+r)*denom)
        check(float((center-remote).subs({r:rr,t:tau}))>0,'strict spatial localization')

for tau in [0.05,0.25,0.5,1.0,1.25,2.0]:
    for rr in [0.35,0.6,0.83]:
        lamb=(1-rr)**2/rr
        half=160; m=2*half+1; ids=np.arange(-half,half+1)
        L=np.zeros((m,m))
        for j in range(m-1):
            weight=tau if ids[j]==0 else 1.0
            L[j,j]+=weight;L[j+1,j+1]+=weight
            L[j,j+1]-=weight;L[j+1,j]-=weight
        rhs=np.zeros(m);rhs[half]=1
        from scipy.sparse import csr_matrix, eye
        from scipy.sparse.linalg import spsolve
        sol=spsolve(csr_matrix(L)+lamb*eye(m),rhs)
        exactA=float(A.subs({r:rr,t:tau})); exactB=float(B.subs({r:rr,t:tau}))
        check(abs(sol[half]-exactA)<2e-10,'finite section local resolvent')
        check(abs(sol[half+1]-exactB)<2e-10,'finite section cross resolvent')
        check(abs(sol[half-1]-rr*exactA)<2e-10,'finite section left tail')
        check(abs(sol[half+2]-rr*exactB)<2e-10,'finite section right tail')

for tau in [1,1.3,3]:
    for rr in [0.3,0.5,0.8,0.95,0.995]:
        ko=float(K.subs({t:tau,r:rr}))
        check(ko<1,'strong link has strictly subcritical local parameter')

print('PASS:',checks,'independent symbolic, optimization, and finite-section assertions')
