#!/usr/bin/env python3
"""Independent symbolic and deterministic quadrature checks of the radial shell laws.
Run: python verify.py. Requires SymPy and SciPy (and their dependencies).
The analytic proof, not these finite checks, establishes the all-parameter statements.
"""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.special import gammaln

s, a, b, lam = sp.symbols('s a b lam', positive=True)
log_g = 3*sp.log(s) + (b-1)*sp.log(s*s-1) - b*(s*s-1)
derivative = sp.diff(log_g, s)
assert sp.simplify(derivative.subs(b, a/2) -
                   (-a*s**4+(2*a+1)*s*s-3)/(s*(s*s-1))) == 0
q = a*s**4-(2*a+1)*s*s+3
u = sp.symbols('u')
assert sp.simplify(sp.discriminant(a*u*u-(2*a+1)*u+3,u)-(4*a*a-8*a+1)) == 0
assert sp.simplify((a*u*u-(2*a+1)*u+3).subs(u,1)-(2-a)) == 0
assert sp.simplify(sp.diff(2*lam**2*(1-lam), lam) - (4*lam-6*lam**2)) == 0
assert sp.simplify(sp.factor(sp.diff(sp.log((1-lam)**(b-1)*lam**(-b-2)*sp.exp(-b/lam)),lam)) -
    ((b-1)*(-1)/(1-lam)-(b+2)/lam+b/lam**2)) == 0


def g_density(x, alpha):
    beta=alpha/2
    if x<=1: return 0.
    return math.exp(beta*math.log(beta)-math.lgamma(beta)+
                    3*math.log(x)+(beta-1)*math.log(x*x-1)-beta*(x*x-1))

def g_dlog(x, alpha):
    return (-alpha*x**4+(2*alpha+1)*x*x-3)/(x*(x*x-1))

def f_d_derivative(x,alpha,d):
    """Exact conditional-chi density integral and its analytic derivative."""
    beta=alpha/2
    k=d/2
    norm=math.log(.5)+beta*math.log(beta)+beta-math.lgamma(beta)
    def integrand(l):
        if not (0<l<1): return 0.,0.
        lp=norm+(beta-1)*math.log(1/l-1)-beta/l-3*math.log(l)
        lc=math.log(2)+k*math.log(d*l/2)-gammaln(k)+(d-1)*math.log(x)-d*l*x*x/2
        w=math.exp(lp+lc)
        return w,w*((d-1)/x-d*l*x)
    kwargs=dict(epsabs=2e-9,epsrel=1e-7,limit=350)
    val=quad(lambda l: integrand(l)[0],0,1,**kwargs)[0]
    dv=quad(lambda l: integrand(l)[1],0,1,**kwargs)[0]
    return val,dv

# Explicit check of the effective-stiffness-to-gamma-mixture Jacobian.
for beta in [0.05,0.45,1.3]:
    for t in [0.07,0.5,2.0,5.0]:
        lv=beta/(beta+t)
        left=math.exp(beta*math.log(beta)+beta-math.log(2)-math.lgamma(beta)
                      +(beta-1)*math.log(1-lv)-(beta+2)*math.log(lv)-beta/lv)
        left*=beta/(beta+t)**2
        right=math.exp(-t+(beta-1)*math.log(t)-math.lgamma(beta))*(beta+t)/(2*beta)
        assert abs(left/right-1)<2e-12,(beta,t,left,right)

for alpha in [0.10,0.50,1.00,1.90,2.0,3.0]:
    beta=alpha/2
    # Exact gamma-mixture normalization is 1/2 + 1/2.
    cdf=quad(lambda t: math.exp(-t)*t**(beta-1)*(beta+t)/(2*beta*math.gamma(beta)),
             0,math.inf,epsrel=2e-8,limit=300)[0]
    assert abs(cdf-1)<5e-7, (alpha,cdf)

for alpha, pts, signs in [
    (.1,[1.2,2.2,3.5],[-1,1,-1]),
    (1.9,[1.01,1.1,1.3],[-1,1,-1]),
    (1.0,[1.2,1.5,2.0],[-1,-1,-1]),
    (3.0,[1.01,1.15,2], [1,1,-1]),
]:
    for x,sign in zip(pts,signs):
        assert sign*g_dlog(x,alpha)>1e-6,(alpha,x,g_dlog(x,alpha))

# Explicit finite-dimensional two-shell witness, without assuming it proves
# existence for all sufficiently large dimensions.
for x,sign in [(.95,1),(1.30,-1),(2.20,1),(3.50,-1)]:
    dens,dv=f_d_derivative(x,.1,100)
    assert dens>0 and sign*dv>0.001,(x,dens,dv)
print('PASS: symbolic transformation, gamma normalization, limiting sign regimes, and four finite-dimensional derivative tests')
