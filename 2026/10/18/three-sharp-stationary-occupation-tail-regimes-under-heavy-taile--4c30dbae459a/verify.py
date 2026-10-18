"""Numerical consistency checks for Pareto-renewal birth--death--immigration tails.

Run: python verify.py. Needs scipy>=1.9 and Python>=3.9.
These are finite numerical checks, not a proof of the asymptotic theorem.
"""
import math
from scipy.integrate import quad
from scipy.special import gammaln, gamma

checks = 0

def check(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1


def theta(lam, mu, t):
    g = lam - mu
    return lam*t if abs(g) < 1e-12 else lam*math.expm1(g*t)/g


def pgf(lam, mu, u, t, z):
    return (1+theta(lam,mu,t)*(1-z))**(-u/lam)

# Kolmogorov PGF PDE: H_t=(z-1)[u H + (lambda*z-mu) H_z].
for lam,mu,u in [(0.7,1.1,0.91),(1.,1.,1.7),(1.5,0.5,2.4)]:
    for t in [0.1,0.4,1.0,3.]:
        for z in [0.2,0.6,0.9]:
            h = 1e-6
            ht = (pgf(lam,mu,u,t+h,z)-pgf(lam,mu,u,t-h,z))/(2*h)
            hz = (pgf(lam,mu,u,t,z+h)-pgf(lam,mu,u,t,z-h))/(2*h)
            rhs = (z-1)*(u*pgf(lam,mu,u,t,z)+(lam*z-mu)*hz)
            check(abs(ht-rhs)<2e-8, 'PGF PDE residual')

alpha,b=1.5,2.
def adens(t): return (alpha/b)*(1+t/b)**(-alpha-1)
def atail(t):return (1+t/b)**(-alpha)

# Subcritical: ratio to no-reset NB mass has predicted (log n)^-alpha scale.
lam,mu,k=.7,1.1,1.3
c=mu-lam;q=lam/mu
previous=float('inf')
for n in [100,1000,10000,100000]:
    t0=math.log(n)/c
    def integrand(t):
        x=math.exp(-c*t)
        log_ratio=-k*math.log1p(-q*x)+n*(math.log1p(-x)-math.log1p(-q*x))
        return adens(t)*math.exp(log_ratio)
    val,_=quad(integrand,0,max(300,5*t0),epsabs=1e-11,points=[t0*.5,t0,2*t0],limit=300)
    ratio=val/atail(t0)
    check(1<ratio<1.3,'subcritical tail ratio bounds')
    check(ratio<previous,'subcritical approach')
    previous=ratio

# Critical with k=1: NB survival is q(t)^n. Integrate on t=n*s.
lam=mu=1.
for n in [100,1000,10000,100000]:
    val,_=quad(lambda s:n*adens(n*s)*math.exp(-n*math.log1p(1/(lam*n*s))) if s else 0.,0,math.inf,epsabs=1e-13,limit=500)
    asym=(b*lam)**alpha*gamma(1+alpha)*n**(-alpha)
    check(abs(val/asym-1)<8./n,'critical survival constant')

# Supercritical with k=1: conditional NB survival q(t)^n.
lam,mu=1.5,.5
g=lam-mu
for n in [100,1000,10000,100000,10000000]:
    def integrand(t):
        x=math.exp(-g*t)
        loss=(1-mu/lam)*x/(1-(mu/lam)*x)
        return adens(t)*math.exp(n*math.log1p(-loss))
    val,_=quad(integrand,0,4000,epsabs=1e-12,limit=500)
    ratio=val/atail(math.log(n)/g)
    check(.98<ratio<1.03,'supercritical logarithmic ratio')

print(f'PASS: {checks} independent finite consistency checks (analytic proof required separately)')
