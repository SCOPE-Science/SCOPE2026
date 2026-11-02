"""Reproducible finite checks for a Gaussian-coupled two-point extrapolator.

Run: python verify.py
Only standard-library modules are required.  These checks supplement, and do
not replace, the analytic limit and moment proofs.
"""
from fractions import Fraction as F
from math import sqrt, pi, exp, erf, log, isclose
from statistics import NormalDist
from random import Random

checks=0

def check(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)

# The Anderson one-step expression agrees with the exact rational ratio form.
for a in [F(-1,2),F(0),F(1,4),F(3,4)]:
    c=1-a
    for theta in [F(-3,4),F(2,3)]:
        for x0,x1 in [(F(-2),F(1)),(F(1),F(7,2))]:
            d=x1-x0
            for e0,e1 in [(F(1,3),F(1,7)),(F(-1,2),F(2,7)),(F(1,3),F(1,3))]:
                r0=-c*(x0-theta)+e0
                r1=-c*(x1-theta)+e1
                D=r1-r0
                if not D: continue
                y0=x0+r0; y1=x1+r1
                raw=y1-(y1-y0)*r1/D
                mid=(x0+x1)/2-theta
                N=c*mid-(e0+e1)/2
                check(raw==theta+mid+d*N/D,'exact rational Anderson reduction')

# The two endpoint couplings have different mechanisms.
for theta in [F(-5,7),F(0),F(1,2)]:
    for c in [F(1,3),F(1),F(3,2)]:
        for d in [F(1,3),F(2),F(7,5)]:
            x0=theta-d/2; x1=theta+d/2
            for e in [F(-4,7),F(2,7),F(1,5)]:
                # Antithetic noise and symmetric trial points: exact recovery.
                r0=-c*(x0-theta)+e; r1=-c*(x1-theta)-e
                D=r1-r0
                if D: check(x0-d*r0/D==theta,'antithetic exact recovery')
                # Shared noise: noise is divided by contraction gap.
                r0=-c*(x0-theta)+e; r1=-c*(x1-theta)+e
                check(x0-d*r0/(r1-r0)==theta+e/c,'shared-noise Gaussian endpoint')

# Validate independent-normal decomposition for simulated Gaussian pairs.
rng=Random(104921)
for rho in [-1.0,-0.95,-0.5,0.0,0.37,0.85,1.0]:
    a=0.31; c=1-a; theta=0.7; x0=-1.1; x1=2.2
    d=x1-x0; m=(x0+x1)/2-theta; sig=1.14
    for _ in range(250):
        u=rng.gauss(0,1); v=rng.gauss(0,1)
        e0=sig*u; e1=sig*(rho*u+sqrt(max(0.0,1-rho*rho))*v)
        r0=-c*(x0-theta)+e0; r1=-c*(x1-theta)+e1
        D=r1-r0
        N=c*m-(e0+e1)/2
        if abs(D)>1e-12:
            z=x0-d*r0/D
            check(isclose(z-theta,m+d*N/D,rel_tol=5e-11,abs_tol=5e-11),'numerical stochastic identity')

# In the symmetric geometry, the asymptotic coefficient has one interior maximum.
for b in [0.01,0.1,0.5,1.0,2.0,10.0]:
    opt=(1-b)/(1+b)
    def kshape(rho):
        return sqrt((1+rho)/(1-rho))*exp(-b/(1-rho))
    check(-1<opt<1,'interior maximizer')
    check(isclose(kshape(opt),exp(-(1+b)/2)/sqrt(b),rel_tol=2e-14), 'max coefficient identity')
    for t in range(1,1000):
        rho=-1+2*t/1000
        check(kshape(rho)<=kshape(opt)*(1+1e-12),'global maximum grid')
    h=min(1e-6,(1-abs(opt))/100)
    der=(log(kshape(opt+h))-log(kshape(opt-h)))/(2*h)
    check(abs(der)<1e-6,'stationarity')

# The sharp probability tail follows from one-dimensional Gaussian integration.
def gaussian_tail_from_ratio(t,rho,m,c,d,sig):
    sd=sig*sqrt(2*(1-rho))
    muD=-c*d
    tau=sig*sqrt((1+rho)/2)
    n=5000
    a=-9.; b=9.; dz=(b-a)/n
    acc=0.
    for j in range(n+1):
        v=a+j*dz
        numerator=c*m-tau*v
        radius=abs(d*numerator)/t
        prob=NormalDist(mu=muD,sigma=sd).cdf(radius)-NormalDist(mu=muD,sigma=sd).cdf(-radius)
        value=exp(-v*v/2)/sqrt(2*pi)*prob
        acc+=(1 if j in (0,n) else 4 if j%2 else 2)*value
    return acc*dz/3

def abs_normal_mean(mu,tau):
    if tau==0: return abs(mu)
    return tau*sqrt(2/pi)*exp(-mu*mu/(2*tau*tau))+abs(mu)*erf(abs(mu)/(sqrt(2)*tau))

for rho,m in [(-1.,0.7),(-0.8,0.),(-0.3,0.5),(0.,0.),(0.9,0.2)]:
    c=0.8; d=1.7; sig=1.2
    sd=sig*sqrt(2*(1-rho)); tau=sig*sqrt((1+rho)/2)
    density=exp(-(c*d)**2/(2*sd**2))/(sd*sqrt(2*pi))
    K=2*abs(d)*density*abs_normal_mean(c*m,tau)
    for t in [100.,1000.,10000.]:
        estimate=t*gaussian_tail_from_ratio(t,rho,m,c,d,sig)
        check(abs(estimate/K-1)<0.08,'independent-Gaussian tail asymptotic')

print(f'VERIFY_OK {checks} finite checks (exact fractions, endpoint identities, Gaussian reduction, coupling optimum and tail quadrature)')
