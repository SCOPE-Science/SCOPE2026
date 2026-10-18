"""Independent reproducibility checks for the reset Brownian-diffusivity theorem.

Requirements: Python 3, NumPy, SciPy. Scientific formulas have an analytic proof
in RESULT.md. These finite numerical checks test algebra, not infinite claims.
"""
from math import exp, isclose, factorial
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad

CHECKS = 0

def close(actual, expected, rtol=2e-9, atol=2e-10):
    global CHECKS
    if not isclose(float(actual), float(expected), rel_tol=rtol, abs_tol=atol):
        raise AssertionError((actual, expected))
    CHECKS += 1


def stationary_moments_generator(d, sigma, r):
    """Solve the stationary polynomial generator, without using age mixtures."""
    s2 = sigma*sigma
    # Unknowns EV, EQ, EV2, EQV.
    mat = np.array([
        [r, 0, 0, 0],
        [-2*d, r, 0, 0],
        [-12*s2, 0, r, 0],
        [0, -2*s2, -2*d, r],
    ], float)
    rhs = np.array([2*s2, 0, 0, 0], float)
    v, q, v2, qv = np.linalg.solve(mat, rhs)
    return v,q,v2,qv


def age_moments(d, sigma, r):
    """Independent age-integral calculation, using Gaussian Wick moments."""
    s4 = sigma**4
    f = lambda expression: quad(lambda y: exp(-y)*expression(y/r),0,60,
                                 epsabs=2e-11, epsrel=2e-11)[0]
    return (f(lambda a: 2*sigma**2*a),
            f(lambda a: 2*d*sigma**2*a*a),
            f(lambda a: 12*s4*a*a),
            f(lambda a: (28/3)*d*s4*a**3))


def lag_covariances_semigroup(d, sigma, r, t, moments):
    """Compute stationary correlations with the full resetting generator exp(tL)."""
    v,q,v2,qv = moments
    # Columns correspond to L(1), L(V), L(Q) in basis (1,V,Q).
    L = np.array([[0, 2*sigma**2, 0],
                  [0,-r,2*d],
                  [0,0,-r]],float)
    P = expm(t*L)
    cq = P[:,2]
    cv = P[:,1]
    forward = cq[0]*v+cq[1]*v2+cq[2]*qv-q*v
    backward = cv[0]*q+cv[1]*qv -q*v
    return forward,backward

for d in (1,2,5):
    for sigma,r in ((0.3,0.7),(1.1,2.4),(2.3,1.3)):
        gen = stationary_moments_generator(d,sigma,r)
        age = age_moments(d,sigma,r)
        expected=(2*sigma**2/r,4*d*sigma**2/r**2,
                  24*sigma**4/r**2,56*d*sigma**4/r**3)
        for one,two,three in zip(gen,age,expected):
            close(one,two)
            close(two,three)
        v,q,v2,qv = gen
        c0=qv-q*v
        vv=v2-v*v
        close(c0,48*d*sigma**4/r**3)
        close(vv,20*sigma**4/r**2)
        for rt in (0.1,0.5,1.,2.,5.):
            t=rt/r
            F,B=lag_covariances_semigroup(d,sigma,r,t,gen)
            close(F,(48*d*sigma**4/r**3+40*d*sigma**4*t/r**2)*exp(-rt))
            close(B,48*d*sigma**4/r**3*exp(-rt))
            close(F/B,1+5*rt/6)
            close((F-B)/c0,(5/6)*rt*exp(-rt))
            close(6*(F/B-1)/(5*t),r)
# The normalized arrow's maximum occurs at rt=1.
for rt in (0.1,0.5,0.9,1.1,2,5):
    close(float((rt*exp(-rt)) < 1/exp(1)),1)
print('PASS',CHECKS,'independent generator/age/semigroup checks')
