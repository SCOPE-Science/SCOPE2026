"""Reproducible finite and quadrature checks of the absorption-maximizer theorem.

Run: python verify.py  (requires numpy and scipy). Numerical checks are not
substitutes for the analytic proofs of uniqueness and asymptotic formulas.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply

PI = math.pi


def P(m, x):
    assert m >= 2 and x > 0
    bulk = (2*x/PI) * quad(lambda k: math.sin(k)/(1+x*x+2*x*math.sin(k)),
                           0, PI, epsabs=1e-12)[0]
    edge = (2*x/PI) * quad(lambda q: q**(2*m-2)*(1-q*q)/(1+x*x*q*q),
                           0, 1, epsabs=1e-12)[0]
    return bulk + edge


def derivative(m, x):
    bulk = (2/PI) * quad(lambda k: math.sin(k)*(1-x*x)/(1+x*x+2*x*math.sin(k))**2,
                          0, PI, epsabs=1e-12)[0]
    edge = (2/PI) * quad(lambda q: q**(2*m-2)*(1-q*q)*(1-x*x*q*q)/(1+x*x*q*q)**2,
                          0, 1, epsabs=1e-12)[0]
    return bulk + edge


def reciprocal_difference(m, x):
    return (2*x*(x*x-1)/PI) * quad(
        lambda q: q**(2*m-2)*(1-q*q)**2/((1+x*x*q*q)*(x*x+q*q)),
        0, 1, epsabs=1e-12)[0]


def partial_absorption(m, x, T=140, N=420):
    # Independent finite-volume non-Hermitian evolution; Omega = 1.
    diagonal = -1j * np.ones(N) - .5*x*(np.arange(N) == 0)
    off = .5j*np.ones(N-1)
    generator = diags([off, diagonal, off],[-1,0,1],format='csr')
    initial = np.zeros(N, complex); initial[m-1] = 1
    propagated = expm_multiply(generator,initial,start=0,stop=T,
                                num=281,endpoint=True)[-1]
    return 1 - float(np.vdot(propagated,propagated).real)


def run():
    checks=0
    for m in [2,3,4,8,16,32,64]:
        root = brentq(lambda x: derivative(m,x), 1,math.sqrt(3), xtol=2e-12)
        assert 1 < root < math.sqrt(3)
        assert abs(derivative(m, root)) < 2e-10
        checks += 3
        for x in [.2,.8,1,root+max(.01,(math.sqrt(3)-root)/2),2,4,12]:
            expected = x < root - 1e-10
            assert (derivative(m,x)>0) == expected, (m,x,root)
            checks += 1
        print('m',m,'eta_star',format(root,'.12f'),
              'm^3(eta_star-1)',format(m**3*(root-1),'.9f'))
    for m in [2,3,5,10,32]:
        for x in [.4,.7,1.2,1.8,3.5]:
            lhs=P(m,x)-P(m,1/x)
            rhs=reciprocal_difference(m,x)
            assert abs(lhs-rhs)<2e-12,(m,x,lhs,rhs)
            assert (lhs>0)==(x>1)
            checks+=2
    for m,x in [(2,.5),(2,1),(2,2),(4,1),(4,2),(7,1)]:
        infinite=P(m,x)
        finite=partial_absorption(m,x)
        assert 0<=finite<infinite and infinite-finite<.001,(m,x,infinite,finite)
        checks+=1
        print('finite-volume m eta',m,x,'P_infty',format(infinite,'.12f'),
              'P_T',format(finite,'.12f'))
    for m in [64,128,256]:
        root=brentq(lambda x:derivative(m,x),1,1+.001,xtol=2e-14)
        asym=1+.75/m**3+1.125/m**4
        print('large-m',m,'eta_star',format(root,'.14f'),
              'two-term-asym',format(asym,'.14f'))
        assert abs(root-asym)<15/m**5
        checks+=1
    print('PASS:',checks,'checks. Infinite-size claims require the analytic proof.')

if __name__ == '__main__':
    run()
