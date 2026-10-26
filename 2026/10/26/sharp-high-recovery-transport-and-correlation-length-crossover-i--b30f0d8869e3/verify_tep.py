"""Independent symbolic and numerical checks for the tandem-exclusion strong-recovery theorem.

Dependencies: Python 3, sympy, numpy, scipy. Run: python verify_tep.py.
This script checks finite identities and numerical asymptotics; the proof covers the full parameter ranges.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize_scalar

s, q = sp.symbols('s q', positive=True)
rho = s * (1 + q*s)/(1 + 2*s + q*s*s)
J = q*s*s*((q+1)*s+2)/((1+s)*(1+q*s)*(1+2*s+q*s*s))
P = ((q**3+q**2)*s**5 + 4*q**2*s**4 - (2*q**2+2)*s**3
     -(2*q**2+8*q+6)*s**2 -(5*q+9)*s - 4)
assert sp.simplify(q*(1-rho)*s**2+(1-2*rho)*s-rho)==0
assert sp.simplify(sp.diff(rho,s)-(q*s*s+2*q*s+1)/(1+2*s+q*s*s)**2)==0
assert sp.simplify(sp.diff(J,s)+q*s*P/((1+s)**2*(1+q*s)**2*(1+2*s+q*s*s)**2))==0
A = q*s/(1+q*s)
B = s/(1+s)
markov_current = rho*(A*(1-A) + q*(1-A)*B)
assert sp.simplify(J-markov_current)==0
R = (q-1)*s/((1+s)*(1+q*s))
assert sp.simplify((q-1)*s*s*(1-rho)/(rho*(1+s)**2)-R)==0
assert sp.simplify(J.subs(q,1)-2*rho.subs(q,1)**2*(1-rho.subs(q,1)))==0

# Singular root scaling and the first two optimized coefficients.
e, v = sp.symbols('e v', positive=True)
F = sp.expand(e**4*P.subs({q:e**(-3),s:e*v}))
assert sp.simplify(F.subs(e,0) - (v**5-2*v**2))==0
c = sp.real_root(2,3)
s_as = c*e + c**2*e**2/3
q_as = e**(-3)
scaled_delta = sp.series((1-rho).subs({q:q_as,s:s_as}),e,0,3).removeO().expand()
scaled_j = sp.series(J.subs({q:q_as,s:s_as}),e,0,3).removeO().expand()
assert sp.simplify(scaled_delta.coeff(e,1)-2**(-sp.Rational(2,3)))==0
assert sp.simplify(scaled_delta.coeff(e,2)+2**(-sp.Rational(4,3))/3)==0
assert sp.simplify(scaled_j.coeff(e,1)+3*2**(-sp.Rational(2,3)))==0
assert sp.simplify(scaled_j.coeff(e,2)-5*2**(-sp.Rational(4,3)))==0

# Numerically independent optimization in the density coordinate.
def original_current_density(r, qq):
    disc = (1-2*r)**2 + 4*qq*(1-r)*r
    # Cancellation-free positive root of quadratic, valid for all density values.
    ss = 2*r / (math.sqrt(disc) + (1-2*r))
    tt = qq*ss
    return r*tt*(ss+2+tt)/((1+ss)*(1+tt)**2)

def station_root(qq):
    def poly(z):
        return ((qq**3+qq**2)*z**5 + 4*qq**2*z**4 -(2*qq**2+2)*z**3
                -(2*qq**2+8*qq+6)*z**2-(5*qq+9)*z-4)
    hi = 1.
    while poly(hi) <= 0: hi *= 2.
    return brentq(poly,1e-15,hi,xtol=1e-15)

checks = 11
for qq in [.2,1.,2.,10.,100.,1e3,1e5,1e7]:
    ss = station_root(qq)
    rr = ss*(1+qq*ss)/(1+2*ss+qq*ss*ss)
    jj = float(J.subs({s:ss,q:qq}))
    opt = minimize_scalar(lambda r:-original_current_density(r,qq),bounds=(1e-7,1-1e-8),method='bounded',options={'xatol':1e-13})
    assert abs(rr-opt.x)<3e-7, (qq,rr,opt.x)
    assert abs(jj+opt.fun)<1e-8,(qq,jj,opt.fun)
    # Markov transition calculation as a separate current evaluation.
    a=qq*ss/(1+qq*ss); b=ss/(1+ss)
    assert abs(jj-rr*(a*(1-a)+qq*(1-a)*b))<1e-9
    checks+=3

for rr in [.2,.3,.5,.8]:
    for qq in [1e4,1e6,1e8]:
        # First evaluate using the original density quadratic.
        disc=(1-2*rr)**2+4*qq*(1-rr)*rr
        ss=2*rr/(math.sqrt(disc)+(1-2*rr))
        lam=(qq-1)*ss/((1+ss)*(1+qq*ss))
        corr=-1/math.log(lam)
        pred=math.sqrt(qq*rr*(1-rr))
        assert abs(corr/pred-1)<5e-4,(rr,qq,corr,pred)
        checks+=1

for qq in [1e4,1e5,1e6,1e7,1e8]:
    ss=station_root(qq)
    rr=ss*(1+qq*ss)/(1+2*ss+qq*ss*ss)
    jj=original_current_density(rr,qq)
    eps=qq**(-1/3)
    d_pred=2**(-2/3)*eps-2**(-4/3)*eps*eps/3
    j_pred=1-3*2**(-2/3)*eps+5*2**(-4/3)*eps*eps
    assert abs((1-rr)-d_pred)<.12*eps**3
    assert abs(jj-j_pred)<.12*eps**3
    lam=(qq-1)*ss/((1+ss)*(1+qq*ss))
    xi=-1/math.log(lam)
    xi_pred=2**(-1/3)*qq**(1/3)-1/3
    chi=rr*(1-rr)*(1+lam)/(1-lam)
    assert abs(chi-(1-2**(1/3)*eps))<2*eps*eps
    assert abs(xi-xi_pred)<.05*eps, (qq,xi,xi_pred)
    checks+=4
print('PASS:',checks,'symbolic and numerical check groups')
print('Optimized current deficit coefficient:',3*2**(-2/3))
print('Optimal vacancy density coefficient:',2**(-2/3))
print('Optimal correlation-length coefficient:',2**(-1/3))
