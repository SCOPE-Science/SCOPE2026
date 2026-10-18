"""Independent stationary-moment and distributional checks for reset log-harmonic radial energy.
Run: python check.py   Dependencies: numpy, scipy.
These finite checks corroborate; they do not substitute for the all-parameter proof.
"""
from fractions import Fraction as Q
from math import isclose, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

count = 0

def check(ok, detail=''):
    global count
    assert ok, detail
    count += 1

def direct(eta, w, q):
    return 2*eta*(1+w*q)/((q+1)*(q+2))+(w-1)**2*q/((q+1)**2*(q+2))

def polynomial(eta, w, q):
    A = (w-1)**2+eta*(2*w-3)
    B = (w-1)**2+eta*(5-2*w)
    C = (w-1)**2+eta*(w+2)
    return A - B*q - C*q*q - eta*w*q*q*q

def moments_from_generator(eta, w, q):
    D = 1.
    beta = 1.
    alpha = 2./eta-1.
    m = (alpha+D)/beta
    z0 = w*m
    r = 2*beta*q
    m1 = (2*(alpha+D)+r*z0)/(2*beta+r)
    m2 = (4*(alpha+3*D)*m1+r*z0*z0)/(4*beta+r)
    return (m2-m1*m1)/(m*m)

etas = (.07,.2,.33,.5,.8,1.3,1.9)
ws = (.02,.12,.4,.8,1.,1.3,2.,4.,9.)
qs = (0.,.002,.03,.2,.9,2.,8.,30.)
for eta in etas:
    for w in ws:
        A = polynomial(eta,w,0)
        B = (w-1)**2+eta*(5-2*w)
        C = (w-1)**2+eta*(w+2)
        check(B>0 and C>0 and eta*w>0,'strict negative nonconstant coefficients')
        lo = 1-eta-sqrt(eta*(1+eta))
        hi = 1-eta+sqrt(eta*(1+eta))
        check((A>0)==((w<lo) or (w>hi)),'analytic reset-distance criterion')
        for q in qs:
            d = direct(eta,w,q)
            g = moments_from_generator(eta,w,q)
            check(isclose(d,g,rel_tol=3e-12,abs_tol=4e-12),'independent generator moments')
            check(d>=0,'variance nonnegative')
            if q>0:
                h = min(2e-5, q/4)
                diff = (direct(eta,w,q+h)-direct(eta,w,q-h))/(2*h)
                rhs = 2*polynomial(eta,w,q)/((q+1)**3*(q+2)**2)
                check(isclose(diff,rhs,rel_tol=5e-6,abs_tol=3e-9),'derivative polynomial')
        if A>0:
            root=brentq(lambda q:polynomial(eta,w,q),0,1e8)
            check(root>0 and polynomial(eta,w,root*.9)>0 and polynomial(eta,w,root*1.1)<0,'unique root')
            check(direct(eta,w,root)>direct(eta,w,0),'overshoot above no-reset value')
            check(direct(eta,w,root)>direct(eta,w,2*root),'strict maximum')
        else:
            check(all(direct(eta,w,qs[i+1])<direct(eta,w,qs[i]) for i in range(len(qs)-1)),'strict decrease')

# Exact arithmetic checks of equivalence between the independent generator recursion
# and the polynomial variance formula on rational input values.
for k in range(1,121):
    eta=Q(1+(k%11),8)  # includes some >1 but remains less than 2
    w=Q(1+(k%17),5)
    q=Q(1+(k%13),9)
    D=Q(1); beta=Q(1)
    alpha=2/eta-1
    m=2/eta
    z0=w*m
    r=2*q
    M1=(2*(alpha+D)+r*z0)/(2*beta+r)
    M2=(4*(alpha+3*D)*M1+r*z0*z0)/(4*beta+r)
    check((M2-M1*M1)/(m*m)==direct(eta,w,q),'exact rational moment identity')

# Independent renewal-age integration, not just algebraic moment substitution.
for eta,w,q in [(0.2,.08,.15),(.2,.5,2.),(.2,2.,.53),(.8,.9,.2),(.8,2.,.45),(1.5,3.,4.)]:
    D=1.; beta=1.; alpha=2/eta-1.; m=alpha+1.; z0=w*m
    r=2*q
    def conditional(age):
        s=np.exp(-2*beta*age)
        mean=m+(z0-m)*s
        variance=4*D/beta*z0*s*(1-s)+2*D/beta*m*(1-s)**2
        return mean,variance+mean*mean
    mm=quad(lambda a:r*np.exp(-r*a)*conditional(a)[0],0,np.inf,epsabs=1e-10)[0]
    m2=quad(lambda a:r*np.exp(-r*a)*conditional(a)[1],0,np.inf,epsabs=1e-10)[0]
    check(isclose((m2-mm*mm)/(m*m),direct(eta,w,q),rel_tol=5e-10,abs_tol=5e-11),'independent regenerative quadrature')

# Exact CIR transition sampler at a stationary exponential reset age.
rng=np.random.default_rng(20261017)
for eta,w,q in [(0.2,.08,.15),(.2,.5,.5),(.2,2.,.53),(.8,.5,.4),(.8,2.,.45),(1.5,3.,.67)]:
    D=1.; beta=1.; alpha=2/eta-1.; m=alpha+1.;z0=w*m;r=2*q
    n=130000
    age=rng.exponential(1/r,n)
    s=np.exp(-2*beta*age)
    scale=D/beta*(1-s)
    df=1+alpha/D
    noncentrality=z0*s/scale
    z=scale*rng.noncentral_chisquare(df,noncentrality)
    empirical=np.var(z,ddof=1)/(m*m)
    target=direct(eta,w,q)
    check(abs(empirical-target)<.045*target+0.006,f'Monte Carlo stationary energy variance {eta,w,q,empirical,target}')
print(f'PASS {count} assertions: algebra, exact rationals, stationary regenerative integrals, and direct exact-transition samples')
