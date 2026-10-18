#!/usr/bin/env python3
"""Independent numerical checks of the angular-reset displacement and sorting rate."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.special import ive


def theta_sum(z):
    return 1.0 + 2.0 * sum(math.exp(-m * m * z) for m in range(1, 250))


def laplace_wrapped(q, z):
    # E[exp(q (cos Theta-1))], computed with scaled modified Bessel functions.
    return float(ive(0, q) + 2.0 * sum(
        math.exp(-m * m * z) * ive(m, q) for m in range(1, 250)
    ))


def quadrature_wrapped(q, z):
    def density(theta):
        return (1.0 + 2.0 * sum(
            math.exp(-m*m*z) * math.cos(m*theta) for m in range(1, 250)
        )) / (2.0*math.pi)
    return quad(lambda theta: math.exp(q*(math.cos(theta)-1.0))*density(theta),
                -math.pi, math.pi, epsabs=1e-11, epsrel=1e-11)[0]


def rate(epsilon, z):
    result = minimize_scalar(
        lambda q: epsilon*q*q + math.log(laplace_wrapped(q, z)),
        bounds=(0.0, 3.0/math.sqrt(epsilon)), method="bounded",
        options={"xatol": 1e-10},
    )
    assert result.success
    return result.x, -result.fun


def asymptotic_rate(epsilon, z):
    return .25*math.log(1.0/epsilon) - .25 - math.log(theta_sum(z)/math.sqrt(math.pi))


def check():
    comparisons = 0
    for z in (0.1, 0.8, 5.0):
        for q in (0.2, 1.0, 5.0, 20.0):
            f = laplace_wrapped(q, z)
            g = quadrature_wrapped(q, z)
            assert abs(f/g-1.0) < 2e-9, (z,q,f,g)
            comparisons += 1
    print("Bessel / independent angular quadrature matches:", comparisons)

    rate_checks = 0
    for z in (0.2, 1.0, 3.0):
        q, i = rate(1e-7, z)
        assert abs(q*math.sqrt(1e-7)-.5) < .01, (z,q)
        assert abs(i-asymptotic_rate(1e-7,z)) < .003, (z,i)
        q2,i2 = rate(1e-5,z)
        assert i2 < i, (z,i,i2)
        rate_checks += 1
    print("Sharp weak-residual-noise rate and optimizer comparisons:", rate_checks)

    # Direct Euler-Ito discretization of the original 3D coupled mobility SDE.
    # The finite-time exact formula is NOT used to construct the path positions.
    rng = np.random.default_rng(20261014)
    theta_thermal = 1.0
    c = 1.5
    kappa = .12
    h = np.array([.6,-.3])
    duration = .8
    npaths = 26000
    steps = 320
    dt = duration/steps
    theta = np.zeros(npaths)
    x = np.zeros((npaths,2))
    jh = np.array([-h[1],h[0]])
    for _ in range(steps):
        da = rng.normal(0.0,math.sqrt(2*theta_thermal*c*dt),npaths)
        db = rng.normal(0.0,math.sqrt(dt),(npaths,2))
        a = np.cos(theta)
        b = np.sin(theta)
        body = da[:,None]*(h/c)[None,:] + math.sqrt(2*theta_thermal*kappa)*db
        drift = theta_thermal*dt*jh
        dx_body=body+drift[None,:]
        x[:,0] += a*dx_body[:,0]-b*dx_body[:,1]
        x[:,1] += b*dx_body[:,0]+a*dx_body[:,1]
        theta += da
    u = np.array([h[1]/c,-h[0]/c])
    amp = np.linalg.norm(u)
    e = u/amp
    j = np.array([-e[1],e[0]])
    z = theta_thermal*c*duration
    long = x@e
    trans = x@j
    mu = amp*(math.exp(-z)-1.0)
    var_long = amp**2*.5*(1-math.exp(-2*z))**2+2*theta_thermal*kappa*duration
    var_trans= amp**2*.5*(1-math.exp(-4*z))+2*theta_thermal*kappa*duration
    assert abs(long.mean()-mu) < .018, (long.mean(),mu)
    assert abs(trans.mean()) < .018, trans.mean()
    assert abs(long.var()-var_long) < .03, (long.var(),var_long)
    assert abs(trans.var()-var_trans) < .03, (trans.var(),var_trans)
    print("Direct coupled-noise SDE checks: longitudinal and transverse mean / variance passed")
    print("ALL CHECKS PASSED")


if __name__=="__main__":
    check()
