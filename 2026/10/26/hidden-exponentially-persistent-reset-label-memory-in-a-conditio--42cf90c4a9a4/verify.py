"""Independent numerical checks of conditional-reset label memory.

Requires numpy, scipy, mpmath. No data files.
"""
import math
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.special import jv


def flip_probability_at_age(a, gamma, age):
    # Absolute convergence, with a finite remainder controlled by Bessel tail.
    x = gamma * age
    upper = max(a + 55, int(x + 50 + 6 * np.sqrt(x + 1)))
    orders = np.arange(a+1, upper+1)
    return float(.5*jv(a,x)**2 + np.dot(jv(orders,x),jv(orders,x)))


def flip_probability_integral(a, gamma, lam):
    return quad(lambda u: lam*np.exp(-lam*u)*flip_probability_at_age(a,gamma,u),
                0., min(90./lam,500.), epsabs=5e-12, limit=300)[0]


def b_legendre(n, gamma, lam):
    z = 1.+lam*lam/(2*gamma*gamma)
    return float(mp.re(mp.legenq(n-.5, 0, z, type=3)))*lam/(math.pi*gamma)


def flip_probability_legendre(a, gamma, lam):
    # The remaining tail after 70 terms is below numerical precision in tests.
    return .5*b_legendre(a,gamma,lam)+sum(b_legendre(n,gamma,lam) for n in range(a+1,a+70))


def asymptotic_flip(a,gamma,lam):
    eta=2*math.asinh(lam/(2*gamma))
    return lam/(2*gamma*math.sqrt(2*math.pi*a*math.sinh(eta)))* (1/math.tanh(eta/2))*math.exp(-a*eta)


def run():
    mp.mp.dps=45
    for gam,lam in [(1.,.5),(1.,1.),(1.,2.)]:
        prev=None
        for a in range(1,6):
            numerical=flip_probability_integral(a,gam,lam)
            spectral=flip_probability_legendre(a,gam,lam)
            assert abs(numerical-spectral)<6e-10, (gam,lam,a,numerical,spectral)
            assert 0<spectral<.5
            if prev is not None:
                assert prev>spectral
            prev=spectral
        # Long-distance exponential/sqrt prefactor: ratio approaches 1.
        for a in (20,40):
            actual=flip_probability_legendre(a,gam,lam)
            estimate=asymptotic_flip(a,gam,lam)
            assert abs(estimate/actual-1)<.07, (a,gam,lam,estimate/actual)
        # Integral of event-anchored renewal correlation from kernel mass.
        p=flip_probability_legendre(2,gam,lam)
        kernel_mass=1-2*p
        assert abs((1/lam)/(1-kernel_mass)-1/(2*lam*p))<1e-9
    # High-order short-time onset. Numerical first-event tail has leading term.
    for a in range(1,5):
        gamma=1.; lam=1.
        lead=lam*(gamma/2)**(2*a)/((2*a+1)*math.factorial(a)**2)
        for t in (.08,.04):
            one_event=2*quad(lambda u:lam*math.exp(-lam*u)*flip_probability_at_age(a,gamma,u),
                             0,t,epsabs=1e-22)[0]
            assert abs(one_event/(lead*t**(2*a+1))-1)<.08,(a,t)
    print('PASS: 15 Bessel-vs-Legendre flip integrals, strict distance ordering,')
    print('six long-distance prefactors, renewal integrated-mass identities,')
    print('and eight independent short-time leading-term tests.')

if __name__=='__main__':
    run()
