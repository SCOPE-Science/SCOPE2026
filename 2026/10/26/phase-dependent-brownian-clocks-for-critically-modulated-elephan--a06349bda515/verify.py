"""Checks for the log-log-periodic elephant-walk covariance clocks.
Run with Python 3 and numpy/scipy (for numerical integrations only).
The mathematical theorem is proved analytically; these are independent finite checks.
"""
from fractions import Fraction
from itertools import product
from math import cos, sin, log, pi, exp, sqrt
from scipy.integrate import quad
import numpy as np

def check_transitions():
    p = [Fraction(3,4), Fraction(5,8), Fraction(7,8), Fraction(2,3), Fraction(3,5), Fraction(4,5)]
    b = Fraction(1)
    checked=0
    for n,prob in enumerate(p, start=1):
        a=2*prob-1
        bn=b/(1+a/Fraction(n))
        for hist in product((-1,1),repeat=n):
            s=sum(hist)
            qplus=(1+a*Fraction(s,n))/2
            qminus=1-qplus
            assert qplus>=0 and qminus>=0
            mean=qplus*bn*(s+1)+qminus*bn*(s-1)
            assert mean==b*s
            incrplus=bn*(s+1)-b*s
            incrminus=bn*(s-1)-b*s
            var=qplus*incrplus**2+qminus*incrminus**2
            assert var==bn**2*(1-a**2*Fraction(s*s,n*n))
            checked+=3
        b=bn
    return checked

def h(phi,c): return c*sin(phi)
def H(phi,c): return c*(1-cos(phi))
def f(phi,c): return exp(-4*H(phi,c))
def lam(phi,t,c):
    # Equivalent integral on v=-log(u), avoiding singular oscillations near u=0.
    return quad(lambda v: t*exp(-v)*f(phi+log(t)-v,c),0,48,epsabs=1e-12)[0]
def F(phi,c): return exp(4*H(phi,c))*lam(phi,1,c)

def clock_checks():
    c=0.1
    checked=0
    vals=[]
    for phi in np.linspace(0,2*pi,65,endpoint=False):
        t=0.65
        deriv=(lam(phi,t+1e-5,c)-lam(phi,t-1e-5,c))/(2e-5)
        assert abs(deriv-f(phi+log(t),c))<1e-8
        fp=(F(phi+1e-5,c)-F(phi-1e-5,c))/(2e-5)
        assert abs(fp-(1-F(phi,c)+4*h(phi,c)*F(phi,c)))<1e-8
        inv=(fp+F(phi,c)-1)/(4*F(phi,c))
        assert abs(inv-h(phi,c))<1e-8
        checked+=3
        vals.append(F(phi,c))
    assert max(vals)-min(vals)>0.3 # Nonconstant at c=0.1
    tiny=0.0001
    for phi in np.linspace(0,2*pi,49):
        expansion=1+2*tiny*(sin(phi)-cos(phi))
        assert abs(F(phi,tiny)-expansion)<3e-7
        checked+=1
    return checked,min(vals),max(vals)

def direct_products():
    c=0.1
    results=[]
    for N in (100000,500000,2000000):
        k=np.arange(1,N,dtype=float)
        p=np.full_like(k,0.75)
        sel=k>=3
        p[sel]+=c*np.sin(np.log(np.log(k[sel])))/np.log(k[sel])
        a=2*p-1
        log_b=np.empty(N,dtype=float)
        log_b[0]=0
        log_b[1:]=-np.cumsum(np.log1p(a/k))
        bn=np.exp(log_b[-1]); Q=np.sum(np.exp(2*log_b[1:]))
        phase=log(log(N))
        target=F(phase,c)
        measured=Q/(bn**2*N*log(N))
        results.append((N,measured,target,abs(measured-target)))
    assert results[-1][3]<0.25
    return results

if __name__=='__main__':
    r1=check_transitions()
    r2,lo,hi=clock_checks()
    r3=direct_products()
    print('PASS: rational transition identities:',r1)
    print('PASS: clock/ODE/inversion/linear-response checks:',r2)
    print('Variance profile sampled extrema:',lo,hi)
    print('Finite product approximations [N, empirical variance factor, asymptotic clock, abs error]:')
    for row in r3:print(row)
