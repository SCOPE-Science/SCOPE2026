"""Supplementary calculations for a first integral in the critical linear-feedback collective-risk game.

Dependencies: Python 3.10+, sympy, scipy, numpy.
Run: python check_critical_collective_risk.py
This file supplements, but does not replace, the analytical proof.
"""
from math import comb, log
from fractions import Fraction
import sympy as sp
from scipy.integrate import solve_ivp


def vector_field(N, M, b, c, eps, x, r):
    alpha, beta = M - 1, N - M
    h = b * comb(N - 1, alpha) * x**alpha * (1 - x)**beta
    u = alpha / beta
    return x * (1 - x) * (r * h - c) / eps, r * (1 - r) * (u * (1 - x) - x)


def gradient_integral(N, M, b, c, eps, x, r):
    alpha, beta = M - 1, N - M
    h = b * comb(N - 1, alpha) * x**alpha * (1 - x)**beta
    hp = h * (alpha - (N - 1)*x) / (x * (1 - x))
    a = beta * c / eps
    I = ((1 - r) / r)**a
    Hx = -I * hp / h**2
    Hr = beta / eps * I * (r - c / h) / (r * (1 - r))
    return Hx, Hr


def exact_algebra_checks():
    x, r = sp.symbols('x r', positive=True)
    B = sp.symbols('B', positive=True)
    for N in range(3, 11):
        for M in range(2, N):
            alpha, beta = M - 1, N - M
            # Choose positive rational payoffs and speed with integral exponent a=2.
            c, eps = sp.Rational(1, 7), sp.Rational(beta, 14)
            h = B * sp.binomial(N - 1, alpha) * x**alpha * (1 - x)**beta
            A = (1-r)/r
            I = A**2
            rhsx = x*(1-x)*(r*h-c)/eps
            rhsr = r*(1-r)*sp.Rational(1,beta)*(alpha-(N-1)*x)
            Hx = -I*sp.diff(h, x)/h**2
            Hr = sp.Rational(beta, 1)/eps * I*(r-c/h)/(r*(1-r))
            deriv = sp.factor(Hx*rhsx+Hr*rhsr)
            assert deriv == 0, (N, M, deriv)
    print('PASS: 36 symbolic rational identities (all N=3,...,10 and 2<=M<N).')


def numeric_orbit_check():
    N, M = 6, 3
    b, c, eps = 1., 0.1, 0.1
    p = (M-1)/(N-1)
    h0 = b*comb(N-1, M-1)*p**(M-1)*(1-p)**(N-M)
    rstar = c/h0
    a = (N-M)*c/eps
    assert abs(a-3) < 1e-10
    primitive = lambda r: -0.5/r**2+2/r+log(r)
    I = lambda r: ((1-r)/r)**3
    h = lambda x: b*comb(N-1,M-1)*x**(M-1)*(1-x)**(N-M)
    H = lambda x,r: I(r)/h(x)+30*(primitive(r)-primitive(rstar))
    Hlim = 30*(primitive(1)-primitive(rstar))
    Hmin = H(p,rstar)
    assert Hmin < H(p,0.5) < Hlim

    y0=(p, .5)
    sol = solve_ivp(lambda t,y:vector_field(N,M,b,c,eps,*y), (0,200), y0,
                    atol=1e-12, rtol=1e-11, max_step=.06, dense_output=False)
    assert sol.success
    energies=[H(*z) for z in sol.y.T]
    maxdiff=max(abs(v-energies[0]) for v in energies)
    assert maxdiff < 1e-7, maxdiff
    assert sol.y[0].min() < p-0.01 and sol.y[0].max() > p+0.01
    assert sol.y[1].min() < rstar and sol.y[1].max() > rstar
    print('PASS: exact example N=6,M=3, critical risk equilibrium and periodic sublevel.')
    print('H_min=',Hmin,'H(initial)=',energies[0],'H_boundary=',Hlim)
    print('PASS: 200 time-unit trajectory invariant drift <=',maxdiff)


if __name__=='__main__':
    exact_algebra_checks()
    numeric_orbit_check()
