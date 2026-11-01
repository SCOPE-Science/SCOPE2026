#!/usr/bin/env python3
"""Reproduce finite spectral values and analytic endpoint coefficients for a radial hyperbolic-harmonic concentration model."""
import math
from scipy.integrate import quad
from scipy.special import gamma, gammainc
from fractions import Fraction


def profile(p,y):
    den=gamma(p)*(p+1)*(p+4)
    return (gamma(p+2)*gammainc(p+2,y) + 4*gamma(p+1)*gammainc(p+1,y)+4*gamma(p)*gammainc(p,y))/den

def exact_eigenvalue(l,N,a,p,beta=1):
    if l==0:
        from scipy.special import betainc
        return 1-betainc(2,p,max(0,1-a/N**beta))
    high=min(l,a*l/N**beta)
    def f(s):
        if s>=l:return 0.
        return math.exp((l+1)*math.log1p(-s/l))*s**(p-1)*(s+2)**2
    den=quad(f,0,l,epsabs=1e-12,epsrel=1e-12,limit=250)[0]
    num=quad(f,0,high,epsabs=1e-12,epsrel=1e-12,limit=250)[0]
    return num/den

def curv(a,p):
    return 3*quad(lambda x:x*x*profile(p,a*x)*(1-profile(p,a*x)),0,1,epsabs=1e-12)[0]

checks=0
for p in [0.7,1.,2.2]:
    for N in [120,400,1000]:
        for ratio in [.25,.55,.9]:
            l=int(N*ratio); a=2.3
            v=exact_eigenvalue(l,N,a,p)
            limit=profile(p,a*l/N)
            assert 0<v<1 and abs(v-limit)<0.08,(p,N,l,v,limit)
            checks+=1
for p in [0.7,1.,2.2]:
    assert 0<curv(1.1,p)<.25
    csmall=12/(gamma(p+1)*(p+1)*(p+4)*(p+3))
    assert abs(curv(1e-3,p)/(csmall*1e-3**p)-1)<.025
    checks+=2
# p=1 is a finite exponential polynomial, so the large-collar constant is rational.
from scipy.integrate import quad
P=lambda y:1+3*y/5+y*y/10
large=3*quad(lambda y:y*y*(math.exp(-y)*P(y)-math.exp(-2*y)*P(y)**2),0,100,epsabs=1e-10)[0]
assert abs(large-float(Fraction(15837,800)))<1e-9
assert abs(curv(100,1)*100**3-large)/large<.03
checks+=2
# Independent finite-radius radial integral in t=|x|^2, not the s-change formula.
for p in [0.7,1.,2.2]:
    for l in [1,2,3,5,8]:
        N=20; a=2.3
        lo=1-a/N
        fun=lambda t: t**(l+1)*(1-t)**(p-1)*(1-l*t/(l+2))**2
        top=quad(fun,lo,1,epsabs=1e-12,epsrel=1e-11)[0]
        bottom=quad(fun,0,1,epsabs=1e-12,epsrel=1e-11)[0]
        assert abs(top/bottom-exact_eigenvalue(l,N,a,p))<2e-8
        checks+=1
# Full empirical defect convergence, with all multiplicities present.
for N in [80,160]:
    a=2.
    M=sum((l+1)**2 for l in range(N+1))
    defect=sum((l+1)**2*(v:=exact_eigenvalue(l,N,a,1.))*(1-v) for l in range(N+1))/M
    assert abs(defect-curv(a,1.))<.003
    checks+=1
# Trace CDF is strictly increasing and the critical scaling is nondegenerate.
for l,N in [(200,400),(500,1000)]:
    assert exact_eigenvalue(l,N,2.,1.,1)<exact_eigenvalue(l,N,4.,1.,1)
    checks+=1
print('PASSED',checks,'finite numerical tests')
print('critical profile p=1, y=1:',profile(1.,1.))
print('large-collar coefficient p=1:',large,'exact 15837/800')
