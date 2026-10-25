"""Reproducible numerical diagnostics for local containment of random boundary polygons.

Requires Python 3, numpy, scipy. The analytical theorem is proved in RESULT.md;
finite numerical checks are only corroborating evidence.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipeinc, ellipe, spence
from scipy.stats import qmc
PI = math.pi


def circle_containment(n, delta, alpha=0.0):
    """Exact one-dimensional semicircle-anchor integral; density (1+alpha cos t)/(2 pi)."""
    radius = 1.0 - delta
    def integrand(theta):
        gap = .5 + math.atan2(radius * math.sin(theta),
                                1.0 - radius * math.cos(theta)) / PI
        endpoint = theta + 2 * PI * gap
        mass = gap + alpha * (math.sin(endpoint) - math.sin(theta)) / (2 * PI)
        return (1 + alpha * math.cos(theta)) * mass ** (n - 1) / (2 * PI)
    q = math.sqrt(delta)
    cuts = [0, delta, q, .2, PI, 2*PI-.2, 2*PI-q, 2*PI-delta, 2*PI]
    return 1 - n * sum(quad(integrand, a, b, epsabs=2e-13, epsrel=2e-13,
                            limit=400)[0] for a, b in zip(cuts, cuts[1:]))


def ellipse_containment(n, delta, a=2.0, b=1.0):
    """Exact angular integral with arclength sampling on a semiaxes-a,b ellipse."""
    eccentricity_sq = 1 - (b / a)**2
    perimeter = 4 * a * ellipe(eccentricity_sq)
    origin = ellipeinc(PI / 2, eccentricity_sq)
    def cumulative_length(t):
        return a * (ellipeinc(t + PI/2, eccentricity_sq) - origin)
    def speed(t):
        return math.hypot(a * math.sin(t), b * math.cos(t))
    normalized_x = 1 - delta / a
    def integrand(t):
        angle = math.atan2(normalized_x * math.sin(t),
                           1 - normalized_x * math.cos(t))
        opposite_angle = t + PI + 2 * angle
        arc_mass = (cumulative_length(opposite_angle) - cumulative_length(t)) / perimeter
        return speed(t) / perimeter * arc_mass ** (n - 1)
    q = math.sqrt(delta / a)
    cuts = [0, delta/a, q, .2, PI, 2*PI-.2, 2*PI-q, 2*PI-delta/a, 2*PI]
    p = 1 - n * sum(quad(integrand, l, r, epsabs=2e-13, epsrel=2e-13,
                         limit=400)[0] for l, r in zip(cuts, cuts[1:]))
    return p, perimeter


def run():
    for delta in (1e-2, 1e-3, 1e-4):
        exact_classical = .25 - 1.5 / PI**2 * spence(1-(1-delta)**2)
        assert abs(circle_containment(3, delta) - exact_classical) < 2e-11
    print('CLASSICAL_CIRCLE_THREE_POINT_DILOGARITHM_IDENTITY_OK')

    for n in (3, 4, 5, 7):
        delta = 1e-5
        measured = circle_containment(n, delta)
        coefficient = n * (n-1) / (2*PI*PI)
        assert abs(measured/(coefficient*delta*math.log(1/delta)) - 1) < .12
    print('CIRCLE_GENERAL_FIXED_SAMPLE_ASYMPTOTICS_OK')

    for n in (3, 5):
        delta = 1e-5
        measured, length = ellipse_containment(n, delta)
        curvature_at_right_tip = 2.0
        coefficient = 2*n*(n-1)/(length**2 * curvature_at_right_tip)
        assert abs(measured/(coefficient*delta*math.log(length/delta))-1) < .10
    print('ELLIPSE_CURVATURE_AND_ARCLENGTH_NORMALIZATION_OK')

    for alpha in (-.4, .5):
        for n in (3, 5):
            delta = 1e-5
            measured = circle_containment(n, delta, alpha)
            f0 = (1 + alpha)/(2*PI)
            coefficient = 2*n*(n-1)*f0*f0
            assert abs(measured/(coefficient*delta*math.log(1/delta))-1) < .17
    print('NONUNIFORM_BOUNDARY_DENSITY_SQUARE_LAW_OK')

    # Independently classify containment from all consecutive chord halfplanes.
    a, b = 2., 1.
    ecc = 1-(b/a)**2
    grid = np.linspace(0, 2*PI, 150001)
    F = a*(ellipeinc(grid+PI/2,ecc)-ellipeinc(PI/2,ecc)) / (4*a*ellipe(ecc))
    for n, delta in ((3,.25), (5,.15)):
        u = qmc.Sobol(d=n, scramble=True, seed=83475+n).random_base2(17)
        angles = np.sort(np.interp(u,F,grid),axis=1)
        x = a*np.cos(angles)
        y = b*np.sin(angles)
        xn, yn = np.roll(x,-1,axis=1), np.roll(y,-1,axis=1)
        cross = (xn-x)*(-y) - (yn-y)*(a-delta-x)
        empirical = float(np.mean(np.all(cross >= -1e-12,axis=1)))
        formula,_ = ellipse_containment(n,delta)
        assert abs(empirical-formula)<.004, (n,empirical,formula)
    print('INDEPENDENT_RANDOM_ELLIPSE_POLYGON_CONTAINMENT_OK')
    print('ALL_LOCAL_CONTAINMENT_CHECKS_OK')


if __name__ == '__main__':
    run()
