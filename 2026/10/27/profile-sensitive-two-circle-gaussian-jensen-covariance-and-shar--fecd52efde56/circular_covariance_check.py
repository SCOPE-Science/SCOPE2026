"""Numerical checks for a two-circle Gaussian logarithmic covariance law.

Requires numpy and scipy. Checks are corroborative, not a proof of the limits.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import spence


def f_transform(w, z):
    # Smooth positive test profiles: affine functions of x on [0,1].
    # w(x) = a+b*x. Formula obtained by integrating exp(z*x).
    a, b = w
    if abs(z) < 1e-5:
        # Controlled Taylor series at z=0.
        return sum(z**k / math.factorial(k) * (a/(k+1)+b/(k+2))
                   for k in range(7))
    f0 = np.expm1(z)/z
    f1 = (np.exp(z)*(z-1)+1)/(z*z)
    return a*f0+b*f1


def limit_cov(w, t, u):
    den = float(np.real(f_transform(w, 2*t)*f_transform(w, 2*u)))
    def integrand(x):
        v = f_transform(w, t+u+1j*x)
        q = min(1.0, max(0.0, abs(v)**2/den))
        return spence(1-q)
    # Long-range tail O(x^-2), with intervals to stabilize quadrature.
    edges = [0, 1, 4, 20, 100, 400, 1000]
    integ = sum(quad(integrand, edges[k], edges[k+1], limit=450,
                     epsabs=1e-9)[0] for k in range(len(edges)-1))
    return integ/(4*math.pi)


def finite_cov(w, n, t, u):
    j = np.arange(n)
    a, b = w
    coeff = (a+b*j/n)*np.exp((t+u)*j/n)
    nt = 16*n
    f = np.fft.ifft(coeff, nt)*nt
    den = (np.sum((a+b*j/n)*np.exp(2*t*j/n))
           *np.sum((a+b*j/n)*np.exp(2*u*j/n)))
    q = np.minimum(1.0, np.maximum(0.0, abs(f)**2/den))
    return n*np.mean(spence(1-q))/4


def tail_coefficient(w, m):
    a,b=w
    integ=quad(lambda x:(a+b*x)**2*np.exp(4*m*x),0,1)[0]
    return math.exp(-2*m)*integ/(a*(a+b))


def main():
    test_profiles = [(1.0,0.0),(1.0,0.5),(2.0,-0.6)]
    checks = 0
    for w in test_profiles:
        for t,u in [(0.,0.),(0.6,-0.4),(1.2,0.3)]:
            limit=limit_cov(w,t,u)
            a=finite_cov(w,512,t,u)
            b=finite_cov(w,1024,t,u)
            # At n=1024, the continuum tail beyond 1000 is O(0.001).
            if abs(b-limit)>0.0025:
                raise AssertionError((w,t,u,limit,a,b))
            if abs(b-limit)>abs(a-limit)+0.0008:
                raise AssertionError(('nonconvergent',w,t,u,limit,a,b))
            checks+=2
        rev = (w[0]+w[1],-w[1])
        v1=limit_cov(w,0.6,-0.4)
        v2=limit_cov(rev,-0.6,0.4)
        if abs(v1-v2)>2e-9:
            raise AssertionError(('reversal', w, v1, v2))
        checks+=1
        m=0.35
        vals=[limit_cov(w,m+d,m-d) for d in (0.,0.5,1.3,2.5)]
        if not all(vals[i]>vals[i+1]>0 for i in range(3)):
            raise AssertionError(('monotonicity',w,vals))
        checks+=3
        d=7.
        asym=tail_coefficient(w,m)*d*d*math.exp(-2*d)
        actual=limit_cov(w,m+d,m-d)
        if not 0.975<actual/asym<1.035:
            raise AssertionError(('tail',w,actual,asym,actual/asym))
        checks+=1
    assert abs(finite_cov((1.,0.),1,0,0)-math.pi**2/24)<1e-12
    checks+=1
    print('PASS',checks,'finite and asymptotic corroboration checks')
    print('H_flat(0,0), cutoff 1000 =',limit_cov((1.,0.),0,0))
    print('H_affine(0.6,-0.4) =',limit_cov((1.,0.5),0.6,-0.4))

if __name__=='__main__':
    main()
