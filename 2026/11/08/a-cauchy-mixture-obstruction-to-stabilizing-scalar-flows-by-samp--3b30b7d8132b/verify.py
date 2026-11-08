"""Independent finite/numerical consistency checks for a sampled stable-noise scalar system.

Requires Python 3 and SciPy. This is not a proof of an asymptotic statement.
"""
from math import atan, exp, expm1, hypot, isclose, log, log1p, pi, sqrt, tan
from random import Random
from scipy.integrate import quad


def scale_stable(theta, tau, alpha):
    if abs(theta) < 1e-14:
        return tau ** (1 / alpha)
    return ( expm1(alpha * theta * tau) / (alpha * theta)) ** (1 / alpha)


def exact_cauchy_exponent(theta, b, sigma, tau):
    a = exp(theta*tau)
    d = b * sigma * scale_stable(theta, tau, 1)
    return log(hypot(a,d))/tau


def half_stable_exponent(theta, b, sigma, tau):
    a = exp(theta*tau)
    d = abs(b) * sigma * scale_stable(theta, tau, .5)
    if d == 0:
        return theta
    ratio = d / a
    # Positive 1/2-stable mixing: V = 1/(2 Z^2), Z standard normal.
    integrand = lambda z: sqrt(2/pi)*exp(-z*z/2)*log1p((ratio/(2*z*z))**2)
    val, err = quad(integrand, 0, 12, epsabs=2e-9, limit=300)
    return theta + val/(2*tau)


def quadrature_cauchy_potential(a, d):
    if d == 0:
        return log(abs(a))
    z = -atan(a/d)
    def f(t):
        return log(abs(a+d*tan(t))) / pi
    chunks = [(-pi/2,z),(z,pi/2)]
    return sum(quad(f,left,right,epsabs=2e-8,limit=150)[0] for left,right in chunks)


checks = 0
for theta in (-1.6,-0.3,0.,0.2,1.1):
    for tau in (0.1,0.7,2.4):
        a = exp(theta*tau)
        for b in (-4.,-.8,0.,.8,4.):
            d=b*1.2*scale_stable(theta,tau,1.)
            v=exact_cauchy_exponent(theta,b,1.2,tau)
            assert isclose(v, log(hypot(a,d))/tau,abs_tol=1e-12)
            assert v >= theta - 1e-12
            if b:
                assert v > theta
            checks += 3

for theta,tau in [(-1.1,.3),(-1.1,2.),(-.2,3.)]:
    crit = abs(theta) * sqrt((exp(-theta*tau)+1)/(exp(-theta*tau)-1))
    assert abs(exact_cauchy_exponent(theta,crit,1.,tau)) < 1e-12
    assert exact_cauchy_exponent(theta,crit*.8,1.,tau) < 0
    assert exact_cauchy_exponent(theta,crit*1.2,1.,tau) > 0
    checks += 3

for a,d in [(0.5,.2),(.5,1.7),(2.3,2.2),(4.1,-.6)]:
    numerical = quadrature_cauchy_potential(a,d)
    exact=log(hypot(a,d))
    assert abs(numerical-exact) < 1e-7,(a,d,numerical,exact)
    checks+=1

for theta in [-.8,0.,.8]:
    xs=[half_stable_exponent(theta,b,1.,.7) for b in [0.,.1,1.,4.]]
    assert abs(xs[0]-theta)<1e-12
    assert xs[0]<xs[1]<xs[2]<xs[3]
    checks+=4

rng=Random(480231)
# Stable index 1/2: S=VC with V=1/(2 Z^2), C standard Cauchy.
# Compare direct Monte-Carlo log average to analytical one-dimensional quadrature.
for theta,b in [(0.,.5),(-.5,1.),(.3,.3)]:
    tau=.8
    a=exp(theta*tau)
    d=b*scale_stable(theta,tau,.5)
    total=0.
    n=120000
    for j in range(n):
        z=rng.gauss(0,1)
        v=1/(2*z*z)
        c=tan(pi*(rng.random()-.5))
        total+=log(abs(a+d*v*c))
    monte=total/(n*tau)
    exact=half_stable_exponent(theta,b,1.,tau)
    assert abs(monte-exact)<.07,(theta,b,monte,exact)
    checks+=1
print(f'PASS: {checks} grouped checks; analytic Cauchy potential, threshold, monotonicity, and half-stable Monte Carlo.')
