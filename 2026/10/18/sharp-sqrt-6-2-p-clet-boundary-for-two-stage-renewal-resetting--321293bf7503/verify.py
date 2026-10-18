"""Independent symbolic and quadrature checks for the Erlang-two drift search theorem.

Run: python verify.py
Requires sympy, scipy, numpy, mpmath.
"""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.special import ndtr
from scipy.optimize import brentq

checks = 0
def require(condition, detail):
    global checks
    checks += 1
    if not bool(condition):
        raise AssertionError(detail)

u, d, m, n = sp.symbols('u d m n', positive=True)
q = u*(u+d)
A = 2*(2*u+d)*(sp.exp(u)-1)-q
B = q*(2*u+d+q)
M = A/B
N = sp.expand(sp.diff(A,u)*B-A*sp.diff(B,u))
P = sp.expand(N).coeff(sp.exp(u),1)
Q = sp.simplify(N-P*sp.exp(u))
require(sp.simplify(sp.diff(M,u)-N/B**2)==0,'derivative identity')
require(sp.simplify(P*sp.exp(u)+Q-N)==0,'exponential-polynomial split')

c = {k:sp.factor(sp.series(N,u,0,8).removeO().expand().coeff(u,k)) for k in range(3,7)}
expected = {
 3:2*d*(d*d-6)/3,
 4:(7*d**3+36*d**2-60*d-72)/12,
 5:(7*d**3+75*d**2+60*d-180)/30,
 6:(23*d**3+354*d**2+960*d-240)/360,
}
for k in range(3,7):
    require(sp.simplify(c[k]-expected[k])==0, f'coefficient c{k}')

cn_fact = sp.expand(sum(P.coeff(u,k)*sp.ff(n,k) for k in range(6)))
for k in range(7,18):
    require(sp.simplify(cn_fact.subs(n,k)-sp.factorial(k)*sp.series(N,u,0,k+1).removeO().expand().coeff(u,k))==0, f'coefficient extension {k}')
shift = sp.Poly(sp.expand(cn_fact.subs(n,m+7)),m)
expected_shift = [
  4*(17*d**3+336*d**2+1428*d+840),
  2*(12*d**3+383*d**2+2606*d+3376),
  2*(d**3+69*d**2+811*d+1848),
  4*(2*d**2+53*d+219),
  2*(5*d+48), 4]
for k,p in enumerate(expected_shift):
    require(sp.simplify(shift.coeff_monomial(m**k)-p)==0, f'positive coefficient of (n-7)^{k}')

# Each cubic has one positive root by Descartes; brackets order them strictly.
polys = [23*d**3+354*d**2+960*d-240,
          7*d**3+75*d**2+60*d-180,
          7*d**3+36*d**2-60*d-72]
intervals = [(sp.Rational(0),sp.Rational(1,4)),
             (sp.Integer(1),sp.Rational(6,5)),
             (sp.Rational(19,10),sp.Integer(2))]
for j,(p,(lo,hi)) in enumerate(zip(polys,intervals)):
    require(p.subs(d,lo)<0 and p.subs(d,hi)>0, f'root bracket {j}')
require(sp.sqrt(6)>2,'last root ordering')
require(sp.simplify(sp.series(M,u,0,4).removeO().expand().coeff(u,2)-(d*d-6)/(3*d**3))==0,'critical quadratic term')
require(sp.simplify(sp.series(M,u,0,4).removeO().expand().coeff(u,3).subs(d,sp.sqrt(6))-(8-sp.sqrt(6))/(2*sp.sqrt(6)**4))==0,'critical cubic term')

# Independent numerical integration from the inverse-Gaussian FPT density and CDF.
def analytic(dval,rval):
    uval=(math.sqrt(dval*dval+4*rval)-dval)/2
    return float((2*(2*uval+dval)*math.expm1(uval)-uval*(uval+dval))/(rval*(2*uval+dval+uval*(uval+dval))))

def direct(dval,rval):
    def pdf(t):
        if t<=0: return 0.0
        return math.exp(-((1-dval*t)**2)/(4*t))/(math.sqrt(4*math.pi)*t**1.5)
    def survival(t):
        if t<=0:return 1.0
        x=(dval*t-1)/math.sqrt(2*t)
        y=(-dval*t-1)/math.sqrt(2*t)
        return max(0.0,ndtr(-x)-math.exp(dval)*ndtr(y))
    def res_survival(t): return math.exp(-rval*t)*(1+rval*t)
    success=quad(lambda t:pdf(t)*res_survival(t),0,math.inf,epsabs=2e-12,limit=250)[0]
    duration=quad(lambda t:survival(t)*res_survival(t),0,math.inf,epsabs=2e-12,limit=250)[0]
    return duration/success
for dval in (0.,0.5,1.5,2.0,2.5,4.0):
    for rval in (0.2,1.,3.):
        av=analytic(dval,rval)
        dv=direct(dval,rval)
        require(abs(dv-av)<4e-8*max(1,av), f'quadrature independent check d={dval},r={rval}: {dv} vs {av}')

# Numerical optimality checks support (but do not replace) the sign-change proof.
import mpmath as mp
mp.mp.dps=50
mpN=sp.lambdify((u,d),N,'mpmath')
for dval in (0.01,0.5,1,1.9,2,2.3,2.4):
    # Bracket the proved single stationary point in the well-conditioned variable u.
    ustar=brentq(lambda z: float(mpN(z,dval)),0.002,12,xtol=1e-12)
    optimum=ustar*(ustar+dval)
    base=1/dval
    require(analytic(dval,optimum)<base,'strict acceleration below critical drift')
    require(analytic(dval,optimum)<analytic(dval,0.5*optimum),'minimum against lower rate')
    require(analytic(dval,optimum)<analytic(dval,2*optimum),'minimum against higher rate')
for dval in (2.45,3,5):
    rv=(0.05,0.2,0.5,1,2,4,8)
    vals=[analytic(dval,rval) for rval in rv]
    require(all(v2>v1 for v1,v2 in zip(vals,vals[1:])),'monotone above critical drift')

print('PASS:',checks,'symbolic and independent integral/optimization checks')
print('Critical dimensionless drift:',math.sqrt(6),'(Peclet',math.sqrt(6)/2,')')
print('Asymptotic slope for q_opt/(sqrt(6)-d):',16*math.sqrt(6)/(3*(8-math.sqrt(6))))
