"""Independent finite-parameter checks for the spherical-cap antipodal boundary layer.

Requires only Python 3 standard library. The proof of the limit is analytical;
these quadratures check normalization, the explicit three-sphere profile, and
finite-distance identities rather than certifying an infinite statement.
"""
import math
from math import pi, sin, cos, gamma


def ball_volume(k):
    return pi ** (k / 2) / gamma(k / 2 + 1)


def sphere_area(k):
    return 2 * pi ** ((k + 1) / 2) / gamma((k + 1) / 2)


def simpson(fun, a, b, n=8000):
    if b <= a:
        return 0.0
    assert n % 2 == 0
    h = (b - a) / n
    summation = fun(a) + fun(b)
    for i in range(1, n):
        summation += (4 if i % 2 else 2) * fun(a + i * h)
    return summation * h / 3


def crossover_integral(q, lam):
    # J_q(lambda)=int_{|h|<1}(2lambda-h_q)_+dh.
    return ball_volume(q - 1) * simpson(
        lambda z: (2 * lam - z) * max(0.0, 1.0 - z*z) ** ((q - 1) / 2),
        -1., min(1., 2*lam), 6000)


def crossover_profile(q, lam):
    return sphere_area(q - 1) * crossover_integral(q, lam) / (sphere_area(q) / 2) ** 2


def cubic_sphere_profile(lam):
    if lam <= -.5:
        return 0.0
    if lam <= .5:
        return (3 - 2*lam) * (1 + 2*lam)**3 / (3 * pi*pi)
    return 32 * lam / (3 * pi*pi)


def cap_theta_normalization_q3(alpha):
    return .5*alpha - .25*sin(2*alpha)


def exact_q3_near_antipodal_probability(lam, eps):
    """Exact one-dimensional integral of the two-cap pair distance event.

    X,Y are area-uniform in a cap on S^3, alpha=pi/2+lam*eps,
    and P(d(X,Y)>pi-eps) is computed by integrating the uniform
    cosine of the equatorial directional difference, then one latitude.
    Formula applies for all small eps at any fixed real lam.
    """
    alpha = pi/2 + lam*eps
    assert 0 < alpha < pi
    assert eps * (abs(lam) + 2) < .3
    Z = cap_theta_normalization_q3(alpha)
    def integrand(s):
        width = 2*lam-s
        if width <= 0:
            return 0.
        inner = .5*(sin(eps*width)/eps + width*cos(eps*s))
        return sin(eps*(1+s)/2)*sin(eps*(1-s)/2)*inner
    integral = simpson(integrand,-1.,min(1.,2*lam),6000)
    return eps*eps*integral / (Z*Z)


def exact_q3_smallcap_tail(alpha,eps):
    """Exact triangle-domain quadrature valid for 0<eps<2alpha<pi."""
    assert 0 < eps < alpha < pi/2
    Z = cap_theta_normalization_q3(alpha)
    def inner(u):
        def g(v):
            return (sin(alpha-u)*sin(alpha-v)*
                    sin(2*alpha-(eps+u+v)/2)*sin((eps-u-v)/2))
        return simpson(g, 0.,eps-u, 120)
    return simpson(inner, 0.,eps, 120) / (Z*Z)


def q3_smallcap_coefficient(alpha):
    D = alpha - .5 * sin(2*alpha)
    return (2/3)*sin(alpha)**3*cos(alpha)/(D*D)


def execute():
    n=0
    for q in range(3,10):
        for lam in [-1.,-.51,-.5,-.4,-.15,0.,.2,.5,.51,1.,3.]:
            val = crossover_integral(q,lam)
            assert val >= -1.e-13
            if lam <= -.5: assert val == 0.
            if lam >= .5:
                assert math.isclose(val,2*lam*ball_volume(q),rel_tol=2e-9,abs_tol=1e-10),(q,lam,val)
            if lam == 0:
                assert math.isclose(val,ball_volume(q-1)/(q+1),rel_tol=2e-9,abs_tol=1e-10)
            n+=1
    for lam in [-.5,-.48,-.4,-.25,0.,.2,.4,.5,.6,1.,3.]:
        assert math.isclose(crossover_profile(3,lam),cubic_sphere_profile(lam),rel_tol=4e-9,abs_tol=1e-12),(lam,crossover_profile(3,lam),cubic_sphere_profile(lam))
        n+=1
    # True probability from an independent exact angular integral, not the
    # local Euclidean model. The finite-epsilon normalization converges.
    for lam in [-.3,0.,.2,.5,1.]:
        predicted = cubic_sphere_profile(lam)
        deviations=[]
        for eps in [.06,.03,.015]:
            actual = exact_q3_near_antipodal_probability(lam,eps)
            ratio=actual/(eps**4*predicted)
            assert .84 < ratio < 1.15,(lam,eps,ratio)
            deviations.append(abs(ratio-1))
            n+=1
        assert deviations[-1] < deviations[0],(lam,deviations)
        n+=1
    for alpha in [.7,1.1,1.35]:
        coefficient = q3_smallcap_coefficient(alpha)
        prev=None
        for eps in [.08,.04,.02]:
            value=exact_q3_smallcap_tail(alpha,eps)
            ratio=value/(coefficient*eps**3)
            assert .80 < ratio < 1.20,(alpha,eps,ratio)
            if prev is not None:assert abs(ratio-1)<abs(prev-1)
            prev=ratio
            n+=1
    print('PASS',n,'deterministic verification cases')
    print('S^3 critical coefficient at lambda=0:',cubic_sphere_profile(0.))
    print('S^3 profile samples:',[(lam,round(cubic_sphere_profile(lam),12)) for lam in [-.4,0.,.4,1.]])

if __name__=='__main__':
    execute()
