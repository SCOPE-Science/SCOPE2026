"""Reproduce finite-sample rank-one Gaussian inverse-Hessian sketch identities.

Requires numpy and scipy. Run: python verify.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln

CHECKS = 0

def check(statement, explanation):
    global CHECKS
    CHECKS += 1
    if not statement:
        raise AssertionError(explanation)


def spectral_means(m, h, lam, nodes=160):
    tau = lam * (1 - h / (m * (lam + h)))
    k = m / 2
    log_norm = -float(gammaln(k))
    def weight(t):
        return math.exp((k-1)*math.log(t)-t+log_norm) if t>0 else 0.0
    def integrate(fn):
        return quad(lambda t: weight(t)*fn(2*t/m), 0, math.inf,
                    epsabs=3e-12, epsrel=3e-11,limit=250)[0]
    a = integrate(lambda x: x/(tau+h*x))
    b = (1 - h*a/m)/tau
    e = integrate(lambda x: x/(tau+h*x)**2)
    return tau, a, b, e


def tests():
    for m in (2, 3, 4, 6, 12, 24, 48, 96):
        for h in (0.25, 1., 3., 7.):
            for lam in (0.5, 1., 2.):
                tau, a, b, e = spectral_means(m,h,lam)
                L = h + lam
                check(0 < tau < lam, 'positive and shrunk regularizer')
                check(a < 1/L-1e-10, 'strict negative signal bias')
                check(b > 1/lam+1e-10, 'strict positive nullspace bias')
                check(abs((tau+h)*a+2*h*tau*e/m-1)<2e-10, 'Gamma integration by parts')
                check(abs(b-1/lam-h*(1/L-a)/(m*tau))<2e-12,
                      'spectral bias balance')
                A = h*(2*tau-lam)/(m*L**2)
                gprime=tau+h+4*h*tau/(m*L)
                check((1/L-a) > A/gprime-2e-11, 'positive quantitative lower bound')
    for m in (16, 32, 64, 128):
        h=lam=1.0
        _,a,b,_=spectral_means(m,h,lam,190)
        check(abs(m*(1/(h+lam)-a)-h*lam/(h+lam)**3)<0.016,
              'sharp signal bias coefficient')
        check(abs(m*m*(b-1/lam)-h*h/(h+lam)**3)<0.03,
              'sharp null bias coefficient')
    rng=np.random.default_rng(235918)
    for m in (2,3,5):
        d=m+1;h=2.5;lam=1.5
        tau,a,b,_=spectral_means(m,h,lam)
        for _ in range(50):
            S=rng.standard_normal((m,d))/np.sqrt(m)
            g=S[:,0]
            H=h*np.outer(g,g)+tau*np.eye(m)
            W=S.T@np.linalg.solve(H,S)
            X=float(g@g)
            check(abs(W[0,0]-X/(tau+h*X))<3e-12,'actual matrix signal construction')
            z=S[:,1]
            b_sample=float(z@z/tau -h*(g@z)**2/(tau*(tau+h*X)))
            check(abs(W[1,1]-b_sample)<3e-12,'actual matrix null construction')
        batch=120_000
        g=rng.standard_normal((batch,m))/np.sqrt(m)
        z=rng.standard_normal((batch,m))/np.sqrt(m)
        X=np.einsum('ij,ij->i',g,g)
        aprobe=X/(tau+h*X)
        bprobe=np.einsum('ij,ij->i',z,z)/tau-h*np.einsum('ij,ij->i',g,z)**2/(tau*(tau+h*X))
        check(abs(float(np.mean(aprobe))-a)<0.012, 'MC signal expectation')
        check(abs(float(np.mean(bprobe))-b)<0.025, 'MC nullspace expectation')
        # The exact spectral covariance is diagonal for any ambient dimension d>m.
        check(abs(float(np.mean(np.einsum('ij,ij->i',g,z)/(tau+h*X))))<0.022,
              'zero mean off-diagonal by reflection')
    print('PASS:',CHECKS,'analytical-quadrature, direct matrix, and Monte Carlo checks')
    for m in (2, 3, 8, 32):
        tau,a,b,_=spectral_means(m,1.,1.)
        print(f'm={m}; corrected lambda={tau:.9f}; signal mean={a:.9f}; null mean={b:.9f}; signal bias={a-.5:.9f}; null bias={b-1:.9f}')

if __name__ == '__main__':
    tests()
