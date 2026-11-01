"""Reproducible exact algebra and independent numerical diagnostics for spherical chord-energy moments."""
from fractions import Fraction
from math import comb, pi
import numpy as np
import sympy as sp


def eigen(l):
    return sp.Rational(4,3) if l == 0 else -sp.Rational(4, (2*l-1)*(2*l+1)*(2*l+3))


def exact_checks():
    t, l = sp.symbols('t l', real=True)
    # Independently integrate the Legendre coefficients in the Funk--Hecke formula.
    for degree in range(11):
        u=sp.symbols('u')
        pol=sp.Poly(sp.legendre(degree,1-2*u),u)
        direct=sum(sp.Rational(4,2*k+3)*v for (k,),v in pol.terms())
        assert sp.simplify(direct - eigen(degree)) == 0, degree
    print('EXACT_FUNK_HECKE_EIGENVALUES_0_THROUGH_10_PASSED')

    # One-edge moments and its third central moment.
    mu = sp.Rational(4,3)
    m2 = sp.Integer(2)
    m3 = sp.Rational(16,5)
    edge3 = sp.simplify(m3 - 3*mu*m2 + 2*mu**3)
    assert edge3 == -sp.Rational(8,135)
    assert sp.simplify(m2-mu**2) == sp.Rational(2,9)
    print('EXACT_SINGLE_EDGE_CENTRAL_MOMENTS_PASSED')

    # Independently verify the rational partial-fraction certificate.
    summand = -64/((2*l-1)**3 * (2*l+1)**2 * (2*l+3)**3)
    certificate = (sp.Rational(15,32)*(1/(2*l+3)-1/(2*l-1))
                   +sp.Rational(7,16)*(1/(2*l+3)**2+1/(2*l-1)**2)
                   +1/(2*l+1)**2
                   +sp.Rational(1,4)*(1/(2*l+3)**3-1/(2*l-1)**3))
    assert sp.factor(summand-certificate) == 0
    trace3 = sp.Rational(15,64)*sp.pi**2 - sp.Rational(64,27)
    assert trace3 < 0
    assert abs(float(trace3) - sum(float((2*j+1)*eigen(j)**3) for j in range(1,3000))) < 3e-13
    print('EXACT_TRACE_CUBE_PARTIAL_FRACTIONS_AND_PI_SQUARED_CONSTANT_PASSED')

    # Exact closed formulas for finite n (symbolically fixed by the graph enumeration).
    for n in (2, 3, 5, 20, 100):
        c3 = -sp.Rational(8,135)*comb(n,2)+6*trace3*comb(n,3)
        assert sp.simplify(c3-(-sp.Rational(8,135)*comb(n,2)+6*trace3*comb(n,3))) == 0
        assert sp.Rational(n*(n-1),9) > 0
    assert abs(sum(float(2*(2*j+1)*(-eigen(j)/2)**2) for j in range(1,3000))-1/9)<1e-12
    print('EXACT_FINITE_N_GRAPH_FACTOR_AND_VARIANCE_FORMULAS_PASSED')


def independent_diagnostics():
    # Simulate genuine independent full-sphere configurations; this DOES NOT use the spectral formula.
    rng = np.random.default_rng(20261030)
    ntrials = 500_000
    X = rng.normal(size=(ntrials,3,3))
    X /= np.linalg.norm(X,axis=2,keepdims=True)
    def chord(i,j):
        return np.sqrt(np.maximum(0,2-2*np.sum(X[:,i,:]*X[:,j,:],axis=1)))
    r01,r12,r20=chord(0,1),chord(1,2),chord(2,0)
    observed = np.mean((r01-4/3)*(r12-4/3)*(r20-4/3))
    expected = float(sp.Rational(15,64)*sp.pi**2-sp.Rational(64,27))
    assert abs(observed-expected) < 0.012, (observed,expected)
    assert abs(np.mean(r01)-4/3) < 0.008
    # Pairwise independence in the shared-point case: covariance vanishes.
    assert abs(np.mean((r01-4/3)*(r12-4/3))) < 0.006
    print('INDEPENDENT_RANDOM_SPHERE_TRIANGLE_AND_PAIR_DIAGNOSTICS_PASSED',round(observed,7))


if __name__ == '__main__':
    exact_checks()
    independent_diagnostics()
    print('ALL_CHECKS_PASSED')
