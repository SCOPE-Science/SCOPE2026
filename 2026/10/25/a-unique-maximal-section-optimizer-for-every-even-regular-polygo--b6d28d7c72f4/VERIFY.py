"""Reproduction checks for maximal central sections of even polygonal prisms.

Run with: python3 VERIFY.py
Standard Python 3 library only.  Sampling is corroboration, not a proof.
"""
import math
import random

PI = math.pi


def probability(n, h):
    assert n >= 4 and n % 2 == 0 and h > 0
    beta = PI / n
    H = math.hypot(1., h)
    return (n / PI) * (2. * math.asin(math.sin(beta) / H)
                       - math.asin(math.sin(2. * beta) / H))


def best_height(n):
    assert n >= 4 and n % 2 == 0
    return math.sqrt(3. * math.cos(PI / n) ** 2 - 1.)


def count_section_vertices(n, h, u):
    # A generic section vertex is the intersection of the plane with a prism edge.
    # Check the signed endpoint values independently for all 3n polytope edges.
    values = [u[0] * math.cos(2*PI*j/n) + u[1] * math.sin(2*PI*j/n)
              for j in range(n)]
    top = [x + h*u[2] for x in values]
    bottom = [x - h*u[2] for x in values]
    return sum(a*b < 0 for a, b in zip(top, bottom)) + sum(
        top[j]*top[(j+1)%n] < 0 for j in range(n)) + sum(
        bottom[j]*bottom[(j+1)%n] < 0 for j in range(n))


def threshold_event(n, h, u):
    xy = math.hypot(u[0], u[1])
    if not xy:
        return False
    phi = math.atan2(u[1], u[0])
    absolute_cosines = sorted((abs(math.cos(phi-2*PI*j/n))
                              for j in range(n)), reverse=True)
    lam = h*abs(u[2])/xy
    return absolute_cosines[2] < lam < absolute_cosines[0]


def sphere_point(rng):
    z = 2*rng.random()-1
    phi = 2*PI*rng.random()
    rho = math.sqrt(1-z*z)
    return (rho*math.cos(phi), rho*math.sin(phi), z)


def direct_azimuth_quadrature(n, h, steps=20000):
    beta = PI/n
    dt = beta/steps
    val = 0.0
    for k in range(steps):
        theta = (k+0.5)*dt
        t1 = math.cos(theta)
        t2 = math.cos(2*beta-theta)
        val += (t1/math.hypot(h,t1)-t2/math.hypot(h,t2))*dt
    return n/PI*val


def main():
    rng=random.Random(1252026)
    for n in (6, 8, 10, 14, 20):
        opt=best_height(n)
        for h in (0.31, opt, 2.0):
            predicted=probability(n,h)
            quadrature=direct_azimuth_quadrature(n,h)
            assert abs(predicted-quadrature) < 3e-10
            observed=0
            samples=14000
            for _ in range(samples):
                u=sphere_point(rng)
                actual = count_section_vertices(n,h,u)==n+2
                assert actual == threshold_event(n,h,u), (n,h,u)
                observed+=actual
            empirical=observed/samples
            assert abs(predicted-empirical)<.025,(n,h,predicted,empirical)
        assert probability(n,opt)>probability(n,opt*.99)
        assert probability(n,opt)>probability(n,opt*1.01)
    print('INDEPENDENT_210000_PRISM_EDGE_INTERSECTIONS_AND_THRESHOLDS_OK')
    print('EXACT_ARCSINE_LAW_AGREES_WITH_DIRECT_AZIMUTH_QUADRATURE_OK')
    for n in (6,8,10,14,20,50,100,500):
        h=best_height(n)
        assert abs(h*h-(3*math.cos(PI/n)**2-1)) < 1e-13
        assert probability(n,h)>probability(n,math.sin(PI/n))
    print('UNIQUE_OPTIMUM_STATIONARY_EQUATION_AND_UNIFORM_PRISM_COMPARISON_OK')
    p6=6/PI*(2*math.asin(1/3)-math.asin(1/math.sqrt(3)))
    assert abs(probability(6,math.sqrt(5)/2)-p6) < 1e-14
    assert abs(probability(4,1/math.sqrt(2)) - (1-6*math.asin(1/3)/PI)) < 1e-14
    print('HEXAGONAL_PRISM_AND_KNOWN_CUBICAL_SPECIALIZATION_OK')
    opt_constant=2*PI**2/(3*math.sqrt(3))
    for n in (100,200,500):
        p_opt=probability(n,best_height(n))
        p_uniform=probability(n,math.sin(PI/n))
        assert abs(n*n*p_opt-opt_constant) < .003
        assert abs(n**4*p_uniform-PI**4) < .1
    print('SHARP_QUADRATIC_OPTIMAL_AND_QUARTIC_UNIFORM_ASYMPTOTICS_OK')
    print('ALL_EVEN_PRISM_CENTRAL_SECTION_CHECKS_OK')

if __name__=='__main__':
    main()
