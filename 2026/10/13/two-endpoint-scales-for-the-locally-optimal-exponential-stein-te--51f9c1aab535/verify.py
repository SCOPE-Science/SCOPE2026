"""Exact symbolic and numerical checks for exponential Poisson Stein tuning."""
import math
from fractions import Fraction
import sympy as sp
from scipy.optimize import minimize_scalar

L, t, u = sp.symbols('L t u', positive=True)
a = sp.exp(L*(u-1))
b = sp.exp(L*(u*u-1))
# The fixed-mean Stein residual H=X*u**X-L*u**(X+1) has mean zero.
# E[H**2] and Cov(H,X) follow by Poisson factorial-moment identities.
E_H2 = L*u*u*(1+L*(1-u)**2)*b
cov_H_X = L*u*a
variance_influence = sp.simplify(E_H2-2*u*a*cov_H_X +u*u*a*a*L)
assert sp.simplify(variance_influence - L*u*u*a*a*((1+L*(1-u)**2)*sp.exp(L*(1-u)**2)-1)) == 0

F = L*(sp.exp(L*t)-1)**2/((1+L*t*t)*sp.exp(L*t*t)-1)
series_L = sp.series(F,L,0,5).removeO().expand()
assert sp.simplify(series_L.coeff(L,2)-sp.Rational(1,2)) == 0
assert sp.simplify(series_L.coeff(L,3)-(t/2-sp.Rational(3,8)*t*t)) == 0
G = 1+L*t*t-sp.exp(-L*t*t)-t*(2+L*t*t)*(1-sp.exp(-L*t))
numerator = sp.diff(L*(sp.exp(L*t)-1)**2,t)*((1+L*t*t)*sp.exp(L*t*t)-1)-L*(sp.exp(L*t)-1)**2*sp.diff((1+L*t*t)*sp.exp(L*t*t)-1,t)
assert sp.simplify(numerator/(2*L**2*(sp.exp(L*t)-1)*sp.exp(L*t)*sp.exp(L*t*t))-G)==0
assert sp.simplify(G.subs(t,1)-((L+1)*sp.exp(-L)-1)) == 0

# Independent finite truncation Poisson-sum verification of influence variance
# (no numerical tests are used for claims over a continuum).
checks=5
for lam in (.2,.5,1.0,2.0,4.0,8.0):
    for uu in (.15,.3,.5,.7,.9):
        aa=math.exp(lam*(uu-1))
        probs=[];p=math.exp(-lam)
        for k in range(180):
            if k: p*=lam/k
            probs.append(p)
        empirical=sum(pk*(k*uu**k-lam*uu**(k+1)-uu*aa*(k-lam))**2 for k,pk in enumerate(probs))
        theorem=lam*uu**2*aa**2*((1+lam*(1-uu)**2)*math.exp(lam*(1-uu)**2)-1)
        assert abs(empirical-theorem) < 2e-10*(1+theorem), (lam,uu,empirical,theorem)
        checks+=1

def f(lam, tt):
    if tt==0.0:return lam*lam/2
    if lam*tt*tt>650: # not used, since lam <= 90
        raise ValueError('out of verification regime')
    a1=math.expm1(lam*tt)
    a2=math.expm1(lam*tt*tt)+lam*tt*tt*math.exp(lam*tt*tt)
    return lam*a1*a1/a2
for lam in (.01,.03,.1,.3,1,2,3,5,10,20,40,80):
    result=minimize_scalar(lambda tt:-f(lam,tt),bounds=(.00001,1.0),method='bounded',options={'xatol':1e-12})
    assert result.success and result.x>0 and result.x<1
    assert f(lam,result.x)>f(lam,0) and f(lam,result.x)>f(lam,1)
    tt=result.x
    q=1+lam*tt*tt-math.exp(-lam*tt*tt)-tt*(2+lam*tt*tt)*(1-math.exp(-lam*tt))
    assert abs(q)<2e-6*(1+lam)
    if lam<=.03: assert abs(tt-2/3) < .003
    if lam>=40: assert abs(lam*(1-tt)-1) < .002
    checks+=5

# Verify exact mean-residual expression under mean-preserving ZIP via PGFs.
w=sp.symbols('w',positive=True)
m= L/(1-w)
phi=w+(1-w)*sp.exp(m*(u-1))
mean_residual=sp.simplify(u*sp.diff(phi,u)*u/u-L*u*phi)
assert sp.simplify(mean_residual - L*u*w*(sp.exp(m*(u-1))-1))==0
checks+=1
print('PASS: symbolic moment/derivative/ZIP identities; exact series; sampled Poisson sums and optimizations;',checks,'checks')
