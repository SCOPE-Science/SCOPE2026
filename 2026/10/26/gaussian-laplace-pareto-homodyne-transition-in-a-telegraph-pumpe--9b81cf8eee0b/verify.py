#!/usr/bin/env python3
"""Reproducible checks for randomly switched parametric-cavity quadrature tails."""
import math
from scipy.integrate import quad
from scipy.special import beta as B
from scipy.stats import norm


def formulas(a,b,h):
    p0=b/(a+b)
    if h<1:
        d=1-h; eta=b/d
        zmax=h/d
        def f0(u):return p0*u**(a-1)*(1-u)**eta/B(a,eta+1)
        def f1(u):return f0(u)*u/(d*(1-u))
        z_from_u=lambda u:zmax*u
        tag='bounded'
    elif h==1:
        def f0(u):return p0*b**a/math.gamma(a)*u**(a-1)*math.exp(-b*u)
        def f1(u):return u*f0(u)
        z_from_u=lambda u:u
        tag='exponential'
    else:
        k=h-1; theta=b/k-a
        assert theta>0
        def f0(u):return p0*u**(a-1)*(1-u)**(theta-1)/B(a,theta)
        def f1(u):return u*f0(u)/k
        z_from_u=lambda u:(h/k)*u/(1-u)
        tag='pareto'
    return tag,f0,f1,z_from_u


def quadrature_tail(a,b,h,c,R):
    tag,f0,f1,zfun=formulas(a,b,h)
    if tag=='exponential':
        upper=max(50/b,10*R/math.sqrt(2*b*c))
        return quad(lambda z:(f0(z)+f1(z))*2*norm.sf(R/math.sqrt(c*(1+z))),0,upper,epsabs=2e-14,limit=500)[0]
    # Concentrate integration near u=1 by transformed uniform logarithmic chart.
    def integrand(t):
        u=1-math.exp(-t)
        if u<=0:return 0
        z=zfun(u)
        return (f0(u)+f1(u))*math.exp(-t)*2*norm.sf(R/math.sqrt(c*(1+z)))
    return quad(integrand,0,32,epsabs=1e-13,limit=500)[0]


def check():
    for a,b,h in [(0.7,2.6,0.65),(0.7,2.6,1),(0.7,2.6,1.7),(0.7,1.5,2)]:
        typ,f0,f1,zfun=formulas(a,b,h)
        domain=(0,1) if typ!='exponential' else (0,math.inf)
        integrals=[quad(fi,*domain,epsabs=1e-12,limit=500)[0] for fi in (f0,f1)]
        assert abs(integrals[0]-b/(a+b))<2e-10,(typ,integrals)
        assert abs(integrals[1]-a/(a+b))<2e-10,(typ,integrals)
        print('normalized',typ,'a,b,h=',a,b,h,'mode masses=',integrals)
    a,b,h=.8,3.6,1.9
    k=h-1; theta=b/k-a
    _,f0,f1,zfun=formulas(a,b,h)
    for m in (1,2):
        formula=(b/(a+b))*(h/k)**m/B(a,theta)*(B(a+m,theta-m)+B(a+m+1,theta-m)/k)
        numeric=quad(lambda u:(f0(u)+f1(u))*zfun(u)**m,0,1,epsabs=1e-9)[0]
        assert abs(numeric-formula)<1e-8*(1+formula)
        print('moment',m,formula,numeric)
    expected_mean=h*a*(1+a+b)/((a+b)*(b-(h-1)*(1+a)))
    assert abs(expected_mean - quad(lambda u:(f0(u)+f1(u))*zfun(u),0,1)[0])<1e-9
    # Direct generator test: stationary density flux equation, independent of quadrature integration.
    for h,a,b,z in [(0.7,.8,2.1,.2),(1,.8,2.1,.4),(2,.8,2.1,.5)]:
        k=h-1
        def unnorm(z):return z**(a-1)*(h+k*z)**(-b/k) if k!=0 else z**(a-1)*math.exp(-b*z)
        f=unnorm(z);f1=z*f/(h+k*z)
        dlog=(a-1)/z-b/(h+k*z)
        divergence=-(f+z*f*dlog)
        assert abs(divergence - (-a*f+b*f1))<1e-10*(1+abs(f))
    # Gaussian mixture heavy-tail constant: conditional normal variance c*y.
    a,b,h,c=.7,1.5,2,1.5
    k=h-1;theta=b/k-a
    ky=(b/(a+b))*(h/k)**(theta+1)/(theta*B(a,theta))
    kq=ky*(2*c)**theta*math.gamma(theta+.5)/math.sqrt(math.pi)
    print('tail constants (variance, homodyne)',ky,kq,'theta',theta)
    for R in (20,40,80,160):
        prob=quadrature_tail(a,b,h,c,R)
        ratio=prob*R**(2*theta)/kq
        print('homodyne Pareto scale',R,'ratio',ratio)
    assert abs(quadrature_tail(a,b,h,c,160)*160**(2*theta)/kq-1)<.012
    # Critical and subcritical logarithmic large-deviation slopes.
    a,b,c=.7,2.6,1.5
    vcrit=[(R,math.log(quadrature_tail(a,b,1,c,R))/R) for R in (12,20,35)]
    target=-math.sqrt(2*b/c)
    print('critical Laplace slopes',vcrit,'target',target)
    assert abs(vcrit[-1][1]-target)<.4
    vsub=[(R,math.log(quadrature_tail(a,b,.65,c,R))/R**2) for R in (10,20,35)]
    target2=-(1-.65)/(2*c)
    print('bounded Gaussian slopes',vsub,'target',target2)
    assert abs(vsub[-1][1]-target2)<.03

if __name__=='__main__':check()
