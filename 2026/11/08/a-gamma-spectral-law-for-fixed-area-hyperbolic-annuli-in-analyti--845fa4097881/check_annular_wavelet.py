"""Reproducible numerical spot-checks for hyperbolic-annulus Bergman concentration.

Dependencies: Python 3.10+, NumPy and SciPy. Numerical comparisons do not
replace the analytical proofs of monotonicity, uniqueness, or the limits.
"""
import math
import numpy as np
from scipy.special import betainc, betaincc, gammaln
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

X, W = leggauss(48)
checks = 0


def verify(ok, why):
    global checks
    assert bool(ok), why
    checks += 1


def geometry(h, u):
    assert h > 0 and u > 1
    a = 1 - 1/u
    b = 1 - 1/(u+h)
    return a, b


def threshold(rho, h, u):
    return rho * math.log1p(h/u)/math.log1p(h/((u+h)*(u-1)))


def eig(rho, h, u, n):
    """Independent finite Gaussian integration of a beta density."""
    v = u/(u+h)
    y = (1+v)/2 + (1-v)/2*X
    logbase = (gammaln(n+rho+1)-gammaln(n+1)-gammaln(rho)
               -rho*math.log(u))
    e = np.exp(n*np.log1p(-y/u) + (rho-1)*np.log(y))
    return math.exp(logbase)*(1-v)/2*np.dot(W, e)


def diff_sign(rho,h,u,n):
    a,b=geometry(h,u)
    return math.exp((n+1)*math.log(a) +rho*math.log1p(-a)) - math.exp((n+1)*math.log(b)+rho*math.log1p(-b))


def profile(rho,h,x):
    return h * x**rho * math.exp(-x)/math.gamma(rho)

# Check exact spectral formulas by independently evaluating incomplete-beta CDFs.
for rho in [0.4,0.8,1.,2.,3.5]:
    for h in [0.2,1.,4.]:
        for u in [2.3,5.,19.]:
            a,b=geometry(h,u)
            verify(abs(((1/(1-b))-(1/(1-a)))-h)<1e-10,'invariant area')
            eigs=[]
            for n in range(0,28):
                q=eig(rho,h,u,n)
                independent=betainc(n+1,rho,b)-betainc(n+1,rho,a)
                verify(abs(q-independent) <2e-11,'beta-integral diagonal')
                verify(0<q<1, 'positive spectrum')
                eigs.append(q)
            t=threshold(rho,h,u)
            imax=max(range(len(eigs)),key=lambda n:eigs[n])
            if t<27.1:
                verify(imax==math.floor(t), 'unique mode index')
            for n in range(27):
                direct=eigs[n+1]-eigs[n]
                predicted=diff_sign(rho,h,u,n)
                if abs(direct)>1e-12:
                    verify((direct>0)==(predicted>0), 'forward beta difference sign')
# Check exact degeneracy surfaces and monotonicity of the crossover parameter.
for rho in [0.5,1.0,2.25]:
    for h in [0.3,1.,2.7]:
        us=np.geomspace(1+1e-5,400,100)
        Rs=[threshold(rho,h,float(u)) for u in us]
        verify(all(v1<v2 for v1,v2 in zip(Rs,Rs[1:])), 'strict threshold staircase')
        for k in [1,2,5,12]:
            lo=1+1e-10
            hi=500+10*k/rho
            root=brentq(lambda uu:threshold(rho,h,uu)-k,lo,hi)
            verify(abs(threshold(rho,h,root)-k)<1e-7,'crossover solution')
            verify(abs(eig(rho,h,root,k-1)-eig(rho,h,root,k))<1e-9,'paired modes tie')
# Compare the spectrum's scaling profile, norm coefficient, and Schatten moments.
for rho in [.5,1.,2.5]:
    h=1.3
    for u in [80.,240.]:
        kk=int(round(rho*u))
        for x in [.3, .8, 1.5, 2.7, 5.]:
            n=int(x*u)
            actual=u*eig(rho,h,u,n)
            target=profile(rho,h,x)
            verify(abs(actual-target)/max(target,1e-10)<.17,'local spectral profile')
        # Norm lies at floor(threshold) with a possible paired tie.
        idx=int(threshold(rho,h,u))
        nmax=max(0,idx)
        norm=u*eig(rho,h,u,nmax)
        target=profile(rho,h,rho)
        verify(abs(norm-target)/target<.08,'sharp operator norm rate')
        # Sum of all eigenvalues converges to exact trace rho*h.
        nmax_scan=int((rho+28)*u)
        e=np.array([eig(rho,h,u,n) for n in range(nmax_scan)])
        verify(abs(sum(e)-rho*h)<6e-7,'fixed trace')
        for q in [1.,2.,3.]:
            measured=(u**(q-1))*sum(e**q)
            target=(h/math.gamma(rho))**q*math.gamma(rho*q+1)/q**(rho*q+1)
            verify(abs(measured-target)/target<.10,'Schatten scaling')
print('ANNULAR_WAVELET_CHECKS_PASS',checks)
