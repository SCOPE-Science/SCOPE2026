#!/usr/bin/env python3
"""Numerical reproduction of a conditional active-Brownian exit-time susceptibility.
Dependencies: numpy, scipy, mpmath. All input parameters are dimensionless.
"""
import math
import numpy as np
import mpmath as mp
from scipy.sparse import bmat, csr_matrix, diags
from scipy.sparse.linalg import spsolve


def closed_coefficient(e):
    """Exact weak-propulsion, zero-force coefficient as a real scalar."""
    t = mp.mpf(1) / mp.sqrt(mp.mpf(e))
    y = mp.exp(-t / 2)
    A = y**4 + 2*y**3 + 6*y**2 + 2*y + 1
    B = y**4 - 8*y**2 + 1
    return (t*(1-y)*A/(4*(1+y)*(1+y*y)**2)
            +t*t*B/(12*(1+y)**2*(1+y*y))
            -t**3*y/(8*(1-y)*(1+y)))


def resolvent_coefficient(e):
    """Independent half-interval Green/resolvent quadratures."""
    e = mp.mpf(e)
    h = mp.sqrt(e)
    a = mp.mpf('0.5')
    A = a / h
    f = lambda x: mp.cosh(x/h)/mp.cosh(A)
    gprime = lambda x: mp.cosh(x/h)/(h*mp.sinh(A))
    psi = lambda x: a**3/3-a*x*x/2+x**3/6
    m1even = lambda x: ((a*a-3*x*x)/(6*e)
                    +f(x)*(a*a/(3*e)-a*mp.tanh(A)/(2*h))
                    +x*mp.sinh(x/h)/(2*h*mp.cosh(A)))
    Hb_on_half = lambda x: 1-mp.cosh((x-a/2)/h)/mp.cosh(a/(2*h))
    odd_source = lambda x: (x-a*mp.sinh(x/h)/mp.sinh(A)
                            +x*(a*a-x*x)/(6*e))
    Kb = mp.quad(lambda x: psi(x)*(2-f(x)-a*gprime(x)), [0,a])/(2*e)
    Km = mp.quad(lambda x:(a-x)*m1even(x), [0,a])
    Ic = mp.quad(lambda x:Hb_on_half(x)*odd_source(x), [0,a])
    c20 = (Kb+Km/2+Ic/2)/e
    b20 = (a*a-e*(1-1/mp.cosh(A))-a*h*mp.tanh(A/2))/(2*e)
    m0 = a**3/(2*e)
    return 2*c20 - 4*m0*b20


def direction_mean(e, u, force, intervals=420):
    """Separate finite-difference solution of the angular-harmonic BVP.
    Modes 0, 1, 2 are sufficient for the leading order in u^2.
    """
    n = intervals-1
    step = 1.0/intervals
    D2 = diags([np.ones(n-1), -2*np.ones(n), np.ones(n-1)],
               [-1,0,1],format='csr')/step**2
    D1 = diags([-np.ones(n-1),np.ones(n-1)],[-1,1],format='csr')/(2*step)
    I = diags(np.ones(n),0,format='csr')
    Z = csr_matrix((n,n))
    drift = float(e)*(D2+float(force)*D1)
    G = bmat([[drift, u*D1/2, Z],
              [u*D1, drift-I, u*D1/2],
              [Z, u*D1/2, drift-4*I]],format='csr')
    rhs = np.zeros(3*n)
    rhs[n-1] = -float(e)/step**2-float(e)*float(force)/(2*step)
    splitting = spsolve(G,rhs)
    first = spsolve(G,-splitting)
    center = n//2
    return first[center]/splitting[center]


def main():
    mp.mp.dps = 55
    for e in ['0.001','0.01','0.03','0.1','0.3','1.0']:
        value = closed_coefficient(e)
        integral = resolvent_coefficient(e)
        relative = abs(value-integral)/(1+abs(value))
        assert relative < mp.mpf('1e-38'), (e,relative)
        print('green identity',e,mp.nstr(value,15),'relative',mp.nstr(relative,3))
    for e in [0.03,0.1,0.3,1.0]:
        u,force = 0.025,0.06
        observed = direction_mean(e,u,force)-direction_mean(e,u,-force)
        expected = -u*u*force*float(closed_coefficient(e))
        relative = abs(observed/expected-1)
        print('direct-BVP',e,'observed',f'{observed:.10g}',
              'expected',f'{expected:.10g}', 'rel.error',f'{relative:.5g}')
        assert relative < 0.035, (e,relative)
    e = mp.mpf('1e-6')
    exact = closed_coefficient(e)
    lead = 1/(12*e)+1/(4*mp.sqrt(e))
    assert abs(exact-lead) < mp.mpf('1e-20')
    assert abs(e*exact-mp.mpf(1)/12) < mp.mpf('0.0003')
    print('asymptotic',mp.nstr(exact,18),
          'two-term',mp.nstr(lead,18), 'difference',mp.nstr(exact-lead,6))
    print('All numerical checks passed. These are checks, not an infinite proof.')


if __name__ == '__main__':
    main()
