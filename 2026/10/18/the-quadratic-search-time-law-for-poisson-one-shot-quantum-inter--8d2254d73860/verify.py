"""Independent numerical checks for Poisson-interrogated quantum lattice searches.

Dependencies: Python 3.10+, numpy, scipy, mpmath.
Run: python verify.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, brentq
from scipy.special import jv, k0, k1
from scipy.linalg import expm
import mpmath as mp

mp.mp.dps = 40


def bessel_transform(n, a):
    value, error = quad(lambda u: math.exp(-a*u)*jv(n, u)**2,
                        0, np.inf, epsabs=8e-10, epsrel=3e-9, limit=900)
    return value


def legendre_transform(n, a):
    z = mp.mpf(1) + mp.mpf(str(a))**2 / 2
    return float(mp.re(mp.legenq(n-mp.mpf('0.5'), 0, z))/mp.pi)


def prefactor_integral(n,a):
    eta=2*math.asinh(a/2)
    # u^2 substitution removes endpoint singularity at t=eta
    def f(u):
        if u == 0:
            return 2*math.exp(-n*eta)/math.sqrt(2*math.sinh(eta))
        return 2*u*math.exp(-n*(eta+u*u)) / math.sqrt(2*(math.cosh(eta+u*u)-math.cosh(eta)))
    return quad(f,0,3.5,epsabs=1e-11,limit=200)[0]/math.pi


def objective(n, alpha):
    return alpha*alpha*bessel_transform(n, alpha/n)


def test():
    xstar=brentq(lambda x: 2*k0(x)-x*k1(x),.1,4,xtol=1e-14)
    assert abs(xstar-1.55265125564536)<1e-12
    alpha_opt=[]
    maxerr=0.
    checks=0
    # First compute two independently represented Laplace transforms.
    for n in (1,2,4,8,16):
        for a in (.2,.6,1.1):
            I=bessel_transform(n,a)
            Q=legendre_transform(n,a)
            assert abs(I-Q)<3e-8,(n,a,I,Q)
            maxerr=max(maxerr,abs(I-Q));checks+=1
    # Test the exact positive toroidal Legendre integral, distinct from Bessel integration.
    for n in (1,2,4,8):
        for a in (.2,.7):
            Q=prefactor_integral(n,a)
            I=legendre_transform(n,a)
            assert abs(Q-I)<2e-8,(n,a,Q,I)
            maxerr=max(maxerr,abs(Q-I));checks+=1
    # Independent direct Hamiltonian calculation on long finite paths.
    for target in (1,2,3,4):
        length=71
        origin=length//2
        adj=np.diag(np.ones(length-1),1)+np.diag(np.ones(length-1),-1)
        for t in (.2,.5,1.,1.6):
            U=expm(-1j*t*adj)
            err=abs(abs(U[origin+target,origin])**2-jv(target,2*t)**2)
            assert err<1e-12,(target,t,err)
            maxerr=max(maxerr,err)
            checks+=1
    # Long-distance local uniform asymptotic and optimized rate.
    for n in (3,7,15,30,60):
        res=minimize_scalar(lambda x:-objective(n,x),bounds=(.5,3.5),
                            method='bounded',options={'xatol':1e-5})
        assert res.success
        alpha_opt.append((n,res.x))
        assert abs(res.x-xstar)<.15/n,(n,res.x,xstar)
        checks+=1
    assert abs(alpha_opt[-1][1]-xstar)<.00005
    for n in (10,25,50,100):
        # n a = xstar; I_n(a) --> K0(xstar)/pi
        val=bessel_transform(n,xstar/n)
        assert abs(val-k0(xstar)/math.pi)<.006/(n*n),(n,val)
        checks+=1
    C=math.pi/(2*xstar*xstar*k0(xstar))
    assert abs(C-3.2622117493359415)<1e-11
    print('VERIFY_OK bessel_legendre=15 legendre_integrals=8'
          ' finite_path=16 optima=5 scaling=4'
          f' root={xstar:.12f} constant={C:.12f} max_error={maxerr:.3g}')

if __name__=='__main__':
    test()
