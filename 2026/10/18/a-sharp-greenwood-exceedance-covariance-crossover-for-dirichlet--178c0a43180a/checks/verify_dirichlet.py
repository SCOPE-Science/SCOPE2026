#!/usr/bin/env python3
"""Independent exact-rational and high-precision numerical checks for Dirichlet threshold/quadratic covariance."""
from fractions import Fraction as F
from math import factorial
import mpmath as mp

def beta_int(a,b):
    return F(factorial(a-1)*factorial(b-1),factorial(a+b-1))

def upper_beta_int(a,b,t):
    # elementary polynomial expansion of the incomplete beta integral
    lower=sum(((-1)**k)*F(factorial(b-1),factorial(k)*factorial(b-1-k))*t**(a+k)/F(a+k) for k in range(b))
    return beta_int(a,b)-lower

def exact_cov(params,i,t):
    a=params[i]; b=sum(params)-a; s=a+b
    H=sum(z*(z+1) for j,z in enumerate(params) if j != i)
    c=F(H,b*(b+1))
    ex=lambda k:upper_beta_int(a+k,b,t)/beta_int(a,b)
    eu=F(sum(z*(z+1) for z in params),s*(s+1))
    from_integrals=(1+c)*ex(2)-2*c*ex(1)+c*ex(0)-eu*ex(0)
    root=(2*c*(s+1)-(1+c)*(a+1))/(s*(1+c))
    den=beta_int(a,b)
    pdf=t**(a-1)*(1-t)**(b-1)/den
    formula=pdf*t*(1-t)*(1+c)/(s+1)*(t-root)
    assert from_integrals==formula,(params,i,t,from_integrals,formula)
    return formula,root

def mp_cov(params,i,t):
    s=sum(params);a=params[i];b=s-a
    c=sum(z*(z+1) for j,z in enumerate(params) if j!=i)/(b*(b+1))
    mu=sum(z*(z+1) for z in params)/(s*(s+1))
    f=lambda x: x**(a-1)*(1-x)**(b-1)/mp.beta(a,b)
    direct=mp.quad(lambda x: f(x)*(x*x+c*(1-x)**2-mu),[t,1])
    root=(2*c*(s+1)-(1+c)*(a+1))/(s*(1+c))
    rhs=f(t)*t*(1-t)*(1+c)/(s+1)*(t-root)
    assert mp.almosteq(direct,rhs, rel_eps=mp.mpf('1e-24'), abs_eps=mp.mpf('1e-27')),(params,i,t,direct,rhs)

if __name__=='__main__':
    count=0
    profiles=[[1,1],[1,1,1],[2,1,3],[1,2,2,4],[9,1,1],[2,3,4,1]]
    for ps in profiles:
        for i in range(len(ps)):
            for t in [F(1,10),F(1,4),F(2,5),F(1,2),F(3,4),F(9,10)]:
                exact_cov(ps,i,t); count+=1
    mp.mp.dps=65
    numeric=0
    for ps in [[mp.mpf('0.5'),mp.mpf('1.25'),mp.mpf('2')],
               [mp.mpf('0.2'),mp.mpf('0.4'),mp.mpf('0.6'),mp.mpf('1')],
               [mp.mpf('3.7'),mp.mpf('0.8'),mp.mpf('1.2')]]:
        for i in range(len(ps)):
            for t in [mp.mpf('.15'),mp.mpf('.45'),mp.mpf('.8')]:
                mp_cov(ps,i,t);numeric+=1
    asym=[]
    for aa in [mp.mpf('.5'),mp.mpf('1'),mp.mpf('2')]:
        for y in [mp.mpf('.7'),mp.mpf('2.7')]:
            ff=lambda z: (aa**aa/mp.gamma(aa))*z**(aa-1)*mp.exp(-aa*z)
            expected=y*ff(y)*(y-(aa+1)/aa)/aa
            ns=[]
            for m in [1000,10000]:
                s=m*aa;b=(m-1)*aa;t=y/m
                c=(aa+1)/(b+1)
                density=mp.exp((aa-1)*mp.log(t)+(b-1)*mp.log1p(-t)-mp.log(mp.beta(aa,b)))
                rhs=m*density*t*(1-t)*(1+c)/(s+1)*(t-(aa+1)/(s+2))
                ns.append(float(m*rhs))
            asym.append((float(aa),float(y),float(expected),ns))
    print('PASS exact rational',count,'PASS noninteger high precision',numeric)
    for item in asym:print('asym',item)

# The following independent integral checks test the limiting covariance matrix
# without using the finite-m Dirichlet formula.
def check_limit_cov():
    mp.mp.dps=50
    tot=0
    for a in [mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2.3')]:
        mu2=(a+1)/a
        ff=lambda z: (a**a/mp.gamma(a))*z**(a-1)*mp.exp(-a*z)
        bfun=lambda z:z*z-mu2-2*mu2*(z-1)
        varB=mp.quad(lambda z:ff(z)*bfun(z)**2,[0,mp.inf])
        assert mp.almosteq(varB,2*(a+1)/a**3,abs_eps=mp.mpf('1e-16'))
        for y in [mp.mpf('0.7'),mp.mpf('2.7')]:
            p=mp.gammainc(a,a*y,mp.inf)/mp.gamma(a)
            fn=ff(y)
            afun=lambda z:(mp.mpf(z>y)-p)-y*fn*(z-1)
            vA=mp.quad(lambda z:ff(z)*afun(z)**2,[0,y,mp.inf])
            cAB=mp.quad(lambda z:ff(z)*afun(z)*bfun(z),[0,y,mp.inf])
            assert mp.almosteq(vA,p*(1-p)-y*y*fn*fn/a,abs_eps=mp.mpf('1e-16'))
            assert mp.almosteq(cAB,y*fn*(y-(a+1)/a)/a,abs_eps=mp.mpf('1e-16'))
            tot+=1
    return tot
if __name__=='__main__':print('PASS independent limiting Gaussian covariance integrals',check_limit_cov())
