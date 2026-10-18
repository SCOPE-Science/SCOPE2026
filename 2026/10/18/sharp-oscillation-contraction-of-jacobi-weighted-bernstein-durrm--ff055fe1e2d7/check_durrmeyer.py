"""Reproducible finite checks for Jacobi Bernstein--Durrmeyer oscillation norms.

Requires Python 3, scipy, and numpy. The analytic proof, not this finite
checker, establishes the theorem for all positive parameters and degrees.
"""
from math import exp, log, lgamma, comb, isclose
from scipy.special import betaln, betainc
from scipy.integrate import quad
from scipy.optimize import brentq

checks = 0

def check(cond, msg):
    global checks
    assert cond, msg
    checks += 1


def crossing(n, a, b):
    log_ratio = (betaln(a+n,b)-betaln(a,b+n))/n
    return 1/(1+exp(-log_ratio))


def overlap(n, a, b):
    c = crossing(n,a,b)
    return betainc(a+n,b,c)+betainc(b+n,a,1-c)


def gap_asym(n,a,b):
    return exp((2-a-b)*log(2)-0.5*(lgamma(a)+lgamma(b))
               +((a+b)/2-1)*log(n)-n*log(2))


def beta_pdf(y,a,b):
    if y<=0 or y>=1:
        return 0.
    return exp((a-1)*log(y)+(b-1)*log(1-y)-betaln(a,b))


def kernel(n,a,b,x,y):
    return sum(comb(n,k)*x**k*(1-x)**(n-k)*beta_pdf(y,a+k,b+n-k)
               for k in range(n+1))


def tv_pair(n,a,b,x1,x2):
    assert x1 < x2
    root = brentq(lambda y:kernel(n,a,b,x1,y)-kernel(n,a,b,x2,y),
                  1e-8,1-1e-8,xtol=1e-13)
    F1 = sum(comb(n,k)*x1**k*(1-x1)**(n-k)*betainc(a+k,b+n-k,root)
             for k in range(n+1))
    F2 = sum(comb(n,k)*x2**k*(1-x2)**(n-k)*betainc(a+k,b+n-k,root)
             for k in range(n+1))
    return F1-F2


for a,b in [(1.,1.),(2.,1.),(1.5,2.5),(0.7,0.8)]:
    for n in [1,2,3,5,8,12]:
        c = crossing(n,a,b)
        check(0<c<1,(n,a,b,'cross'))
        f0 = beta_pdf(c,a,b+n)
        f1 = beta_pdf(c,a+n,b)
        check(abs(f0-f1)<2e-9*max(f0,f1),(n,a,b,'crossdens'))
        d = 1-overlap(n,a,b)
        check(0<d<1,(n,a,b,'coefficient'))
        t = tv_pair(n,a,b,0.,1.)
        check(abs(t-d)<4e-11,(n,a,b,'endpointTV',t,d))
        numerical_integral=0.5*quad(lambda y:abs(beta_pdf(y,a,b+n)-beta_pdf(y,a+n,b)),
                                     0,1,epsabs=5e-11,limit=250,points=[c])[0]
        check(abs(numerical_integral-d)<3e-10,(n,a,b,'quadrature'))
        for x1,x2 in [(0.,0.25),(.1,.6),(.3,.85),(.01,.99)]:
            t = tv_pair(n,a,b,x1,x2)
            check(-1e-11<t<=d+4e-11,(n,a,b,x1,x2,'maximization'))
        for x in [0.,.2,.5,.8,1.]:
            E = sum(comb(n,k)*x**k*(1-x)**(n-k)*(a+k)/(n+a+b)
                    for k in range(n+1))
            check(abs(E-(a+n*x)/(n+a+b))<1e-13,(n,a,b,'eigen'))
        for x1,x2,y1,y2 in [(.2,.6,.25,.7),(.1,.9,.1,.9),(.15,.7,.5,.8)]:
            det=kernel(n,a,b,x1,y1)*kernel(n,a,b,x2,y2)-kernel(n,a,b,x1,y2)*kernel(n,a,b,x2,y1)
            check(det>0,(n,a,b,'TP2',det))

for n in range(1,100):
    check(abs(overlap(n,1.,1.)-2.**(-n))<1e-14,(n,'uniform identity'))

for a,b in [(1.,1.),(2.,1.),(2.,3.),(.5,1.5),(4.,4.)]:
    for n in [100,250,500,1000]:
        r=overlap(n,a,b)/gap_asym(n,a,b)
        check(.97<r<1.25,(n,a,b,'asym',r))

print('PASS:',checks,'finite assertions')
print('examples:')
for n,a,b in [(4,1.,1.),(10,2.,1.),(25,2.,3.),(200,1.5,2.5)]:
    print({'degree':n,'a':a,'b':b,'crossing':crossing(n,a,b),
           'one_minus_Dobrushin':overlap(n,a,b),'spectral_gap':(a+b)/(n+a+b),
           'asym_ratio':overlap(n,a,b)/gap_asym(n,a,b)})
