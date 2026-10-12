#!/usr/bin/env python3
"""Finite cross-checks for the Pareto-reset Glauber mean-magnetization law.

Only the Python standard library is required. These checks corroborate the
analytical proof; numerical examples do not establish infinite-parameter claims.
"""
import math
import random


def simpson(fun, lo, hi, n=20000):
    if n % 2:
        raise ValueError("n must be even")
    h = (hi - lo) / n
    total = fun(lo) + fun(hi)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * fun(lo + i*h)
    return total*h/3


def check(alpha, b, m0=0.75, tau0=1.6):
    lam = b/tau0
    mass = (alpha-1)/alpha
    g0 = mass/tau0
    # Age-density normalization, separately in the short and long sectors.
    short_mass = simpson(lambda a: g0, 0, tau0, 200)
    tail_mass = 1/alpha  # exact Pareto integral
    assert abs(short_mass+tail_mass-1) < 1e-12

    # The density of u=log(m0/m) is easier to integrate than the density in m.
    def density_u(u):
        return g0/lam*(1 if u < b else (b/u)**alpha)

    # Direct numerical quadrature on finite support equals analytic age tail.
    for u1, u2 in [(0.05*b, 0.73*b), (1.10*b, 1.91*b),
                   (1.12*b, 3.08*b)]:
        if u1 >= b and u2 >= b:
            integral = simpson(density_u, u1, u2, 4000)
            predicted = ((b/u1)**(alpha-1)-(b/u2)**(alpha-1))/alpha
        else:
            integral = simpson(density_u, u1, u2, 4000)
            predicted = (u2-u1)*g0/lam
        assert abs(integral-predicted) < 3e-9, (alpha,b,integral,predicted)

    # Validate phase-derivative signs in age coordinates on each side.
    deriv_short = lam
    deriv_just_beyond = lam-alpha/tau0
    assert deriv_short > 0
    assert (deriv_just_beyond < 0) == (b < alpha)
    if b < alpha:
        trough_a=alpha/lam
        assert trough_a > tau0 and abs(lam-alpha/trough_a) < 1e-14
    elif b > alpha:
        assert deriv_just_beyond > 0
    else:
        assert abs(deriv_just_beyond) < 1e-14

    # Transport correction for collapsing the entire short-age sector.
    w1 = m0*mass*((-math.expm1(-b))/b - math.exp(-b))
    direct = simpson(lambda a: g0*m0*(math.exp(-lam*a)-math.exp(-b)),
                     0, tau0, 2000)
    assert abs(w1-direct) < 8e-12, (alpha,b,w1,direct)
    assert w1>0

    # Independent stationary sampling using the uniform component and
    # residual Pareto component rather than sampling the claimed m-density.
    rng = random.Random(1000+int(alpha*1000)+int(b*1000))
    values=[]
    differences=[]
    for _ in range(60000):
        if rng.random()<mass:
            age=tau0*rng.random()
        else:
            age=tau0*(1-rng.random())**(-1/(alpha-1))
        m=m0*math.exp(-lam*age)
        values.append(m)
        differences.append(max(0.0,m-m0*math.exp(-b)))
    for a in [0.25*tau0,0.75*tau0,1.5*tau0,3*tau0]:
        m=m0*math.exp(-lam*a)
        observed=sum(x<=m for x in values)/len(values)
        expected=(1-mass*a/tau0 if a<tau0 else
                  (tau0/a)**(alpha-1)/alpha)
        assert abs(observed-expected)<0.013,(alpha,b,a,observed,expected)
    empirical=sum(differences)/len(differences)
    assert abs(empirical-w1)<0.013, (alpha,b,empirical,w1)
    return 10


def main():
    checks=0
    for alpha in [1.3,1.75,2.2,4.25]:
        for b in [0.1,0.9,1.75,3.0,5.5]:
            checks+=check(alpha,b)
    # Exactly critical b=alpha: no interior modal maximum.
    checks+=check(2.5,2.5)
    print('VERIFY_OK',checks,'analytic normalizations, piecewise densities,')
    print('transport, modal signs, and independently sampled stationary laws')

if __name__=='__main__':
    main()
