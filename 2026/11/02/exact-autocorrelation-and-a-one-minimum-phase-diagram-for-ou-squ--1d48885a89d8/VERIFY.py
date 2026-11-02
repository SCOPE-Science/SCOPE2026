"""Numerical checks of an exact autocorrelation in a harmonic trap with OU stiffness.
Run: python VERIFY.py    (requires numpy and scipy).
Finite computations corroborate but do not prove global assertions.
"""
from math import exp, isclose
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import hyp1f1


def integral_pair(A, mu, d, b):
    """Hypergeometric expression for I(A,b) and its h-weighted mean."""
    a = A / mu
    f = hyp1f1(a, a + 1, b)
    I = exp(-b) * f / A
    M = 1 - (a / (a + 1)) * hyp1f1(a + 1, a + 2, b) / f
    return I, M


def direct_integrals(A, mu, b):
    w = lambda s: exp(-A*s - b*(-np.expm1(-mu*s)))
    I = quad(w, 0, np.inf, epsabs=1e-11, epsrel=1e-11)[0]
    J = quad(lambda s: (-np.expm1(-mu*s))*w(s), 0, np.inf,
             epsabs=1e-11, epsrel=1e-11)[0]
    return I, J / I


def correlation(t, kappa, mu, Dk, Dx):
    d = Dk / mu**3
    A = 2*kappa - 4*Dk/mu**2
    assert A > 0
    lam = kappa - Dk/mu**2
    y = exp(-mu*t)
    I, _ = integral_pair(A, mu, d, 2*d*(1+y))
    return 2*Dx*exp(-lam*t-d*(1-y))*I


def thresholds(mu, d):
    root = lambda b: brentq(lambda a: integral_pair(mu*a, mu, d, b)[1]-0.5,
                            1e-8, 4, xtol=1e-13)
    return mu*root(4*d), mu*root(2*d)


def correlated_stiffness_path_check():
    """Simulate OU stiffness histories, integrating out independent positional noise.
    This samples Gaussian histories directly rather than the Gaussian MGF in the proof.
    """
    N = 30000
    dt = 0.02
    mu = Dx = 1.0
    Dk = .3
    kappa = 1.35
    t = .6
    past_horizon = 12
    rng = np.random.default_rng(912043)
    q = exp(-mu*dt)
    sd = np.sqrt(Dk/mu*(1-q*q))
    k0 = rng.normal(scale=np.sqrt(Dk/mu), size=N)
    k = k0.copy()
    J = np.zeros(N)
    weighted = np.full(N, Dx*dt)
    for j in range(round(past_horizon/dt)):
        next_k = q*k + sd*rng.standard_normal(N)
        J += dt*(k+next_k)/2
        k = next_k
        s = (j+1)*dt
        weighted += 2*Dx*dt*np.exp(-2*kappa*s-2*J)
    k = k0.copy()
    J = np.zeros(N)
    for j in range(round(t/dt)):
        next_k = q*k + sd*rng.standard_normal(N)
        J += dt*(k+next_k)/2
        k = next_k
    samples = weighted*np.exp(-kappa*t-J)
    observed = float(np.mean(samples))
    standard_error = float(np.std(samples, ddof=1)/np.sqrt(N))
    target = correlation(t, kappa, mu, Dk, Dx)
    assert abs(observed-target) < 5*standard_error+0.004*target
    return target, observed, standard_error


def main():
    count = 0
    for mu in (0.7, 1.0, 1.8):
        for d in (.05, .3, 1.0):
            for a in (.3, .8, 1.7):
                for y in (0, .4, 1):
                    A = mu*a
                    b = 2*d*(1+y)
                    x, m = integral_pair(A, mu, d, b)
                    q, n = direct_integrals(A, mu, b)
                    assert isclose(x, q, rel_tol=5e-10)
                    assert isclose(m, n, abs_tol=5e-10)
                    count += 1
    print('Integral pair direct-quadrature comparisons:', count)

    for d in (.05, .3, 1., 2.):
        lo, hi = thresholds(1., d)
        assert 0 < lo < hi
        for A in (lo*.5, (lo+hi)/2, hi*1.5):
            kappa = 2*d + A/2
            lam = kappa-d
            grid = np.linspace(0, 10, 801)
            E = np.array([exp(lam*t)*correlation(t,kappa,1,d,1) for t in grid])
            changes = np.diff(E)
            nmins = np.sum((changes[:-1]<0)&(changes[1:]>0))
            nmaxs = np.sum((changes[:-1]>0)&(changes[1:]<0))
            assert nmaxs == 0
            if A < lo: assert np.min(changes)>0
            elif A > hi: assert np.max(changes)<0
            else: assert nmins == 1
            G = lambda t: exp(-lam*t - d*(1-exp(-t)))
            C0 = correlation(0,kappa,1,d,1)
            assert all(correlation(t,kappa,1,d,1)>C0*G(t) for t in (.1,.5,1.5,4))
        print('d, threshold A-, A+:', d, lo, hi)

    for d in (.002,.005,.01):
        lo, hi = thresholds(1., d)
        assert abs(lo-(1-4*d/3)) < 2*d*d
        assert abs(hi-(1-2*d/3)) < d*d
    print('Weak-noise threshold expansion: PASS')

    for d, A in ((.3,.3),(.3,.7),(.3,1.4),(1.,.15),(1.,.6)):
        kappa=2*d + A/2
        lam=kappa-d
        I,M=integral_pair(A,1,d,2*d)
        E_inf=2*np.exp(-d)*I
        for t in (6,8):
            y=exp(-t)
            E=exp(lam*t)*correlation(t,kappa,1,d,1)
            remainder=E/E_inf-1-d*(1-2*M)*y
            assert abs(remainder) < 10*y*y
    print('Long-lag expansion: PASS')

    a,b,se = correlated_stiffness_path_check()
    print('Independent OU path check: analytic, Monte Carlo, SE:',a,b,se)
    print('All tests passed.')

if __name__ == '__main__':
    main()
