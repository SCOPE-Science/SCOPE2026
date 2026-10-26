"""Reproduce bifurcation identities and quantitative checks for a shifted-Poisson ecological cavity model.
Run with Python 3 and SymPy/SciPy installed. This is supplementary, not an exhaustive proof.
"""
import math
import random
import sympy as sp
from scipy.optimize import brentq, root

q,z,l = sp.symbols('q z l', real=True)
s = 1-sp.exp(-z*q)
H = s*(1+l*s)*sp.exp(l*(s-1))/(1+l)
F=1-sp.exp(-z*H)
for k in (1,2,3):
    ck=sp.factor(sp.diff(F,q,k).subs(q,0)/sp.factorial(k))
    if k==1: assert sp.simplify(ck-z*z*sp.exp(-l)/(1+l))==0
    if k==2:
        test=sp.factor((ck-(z*(4*l-1)-1)/2).subs(sp.exp(l),z*z/(1+l)))
        assert test==0, test
    if k==3:
        ck2=sp.factor(ck.subs(sp.exp(l),z*z/(1+l)).subs(l,(1+1/z)/4))
        assert sp.simplify(ck2+(23*z*z+30*z+23)/96)==0
print('Three symbolic Taylor identities: PASS')

def zzero(L): return math.sqrt((1+L)*math.exp(L))
def f(x,Z,L):
    y=-math.expm1(-Z*x)
    h=y*(1+L*y)*math.exp(L*(y-1))/(1+L)
    return -math.expm1(-Z*h)
def fp(x,Z,L):
    y=-math.expm1(-Z*x)
    h=y*(1+L*y)*math.exp(L*(y-1))/(1+L)
    hp=math.exp(L*(y-1))/(1+L)*(1+3*L*y+L*L*y*y)
    return Z*Z*(1-y)*hp*math.exp(-Z*h)
def roots(Z,L):
    # Quantitative stress-testing only; not an exhaustive mathematical search.
    grid=[k/4000 for k in range(1,4001)]
    out=[]
    p=1.e-11; y=f(p,Z,L)-p
    for x in grid:
        yy=f(x,Z,L)-x
        if y*yy<0:
            r=brentq(lambda t: f(t,Z,L)-t,p,x,xtol=1e-14)
            if not out or abs(out[-1]-r)>1e-8:out.append(r)
        p,y=x,yy
    return out
lc=brentq(lambda L: zzero(L)*(4*L-1)-1,.25,.8,xtol=1e-15)
zc=zzero(lc)
assert .42<lc<.421 and 1.47<zc<1.471

# Check all three qualitative regimes and roots' multipliers.
for L in (0,.1,.35,lc,lc+.07,.6,1,1.5,2):
    zz=zzero(L)
    for relative in (.7,.9,.98,.999,1.001,1.05,1.3):
        Z=zz*relative
        r=roots(Z,L)
        if relative>1.0: assert len(r)==1,(L,relative,r)
        if relative<1.0 and L <=lc: assert len(r)==0,(L,relative,r)
        if len(r)==2: assert fp(r[0],Z,L)>1 and 0<fp(r[1],Z,L)<1
        if len(r)==1: assert fp(r[0],Z,L)<1
print('Root regimes and branch multipliers over sampled parameters: PASS')

r=root(lambda a: [f(a[0],a[1],1)-a[0], fp(a[0],a[1],1)-1], [.366,1.94],tol=1e-12)
assert r.success and max(abs(x) for x in r.fun)<1e-12
qs,zs=r.x
assert zs < zzero(1) and .36<qs<.38
print('For lambda=1 fold (z,q):',repr(float(zs)),repr(float(qs)))

# Critical asymptotic slopes/amplitudes from symbolic Taylor terms.
L=0.2; zz=zzero(L); dd=zz*(4*L-1)-1; predicted=-4/(zz*dd)
for eps in (1e-3,3e-4,1e-4):
    rr=roots(zz+eps,L)[0]
    assert abs(rr/eps-predicted)/predicted<.05,(rr,eps,predicted)
critical_amp=math.sqrt(192/(zc*(23*zc*zc+30*zc+23)))
for eps in (1e-3,2e-4,1e-4):
    rr=roots(zc+eps,lc)[0]
    assert abs(rr/math.sqrt(eps)-critical_amp)/critical_amp<.09,(rr,eps,critical_amp)
print('Linear and tricritical square-root asymptotic checks: PASS')
print('lambda_c=',repr(lc),'tau_c=',repr(1+lc),'z_c=',repr(zc),'critical amplitude=',repr(critical_amp))
print('All checks passed.')
