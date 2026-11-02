"""Reproducible checks for Gaussian-sketch first-pivot probabilities.

Run with Python 3, numpy, scipy and sympy. The mathematical results for all
matrix dimensions and sketch sizes follow from the accompanying proof; this
file supplies exact finite checks and numerical tests, not an infinite proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial, gamma, lgamma, log, sqrt, pi, exp
import numpy as np
import scipy.integrate as integrate
import scipy.special as special
import sympy as sy


def failure_even(squared_norms, half_rows):
    """Exact rational first-pivot failure for mutually orthogonal columns."""
    assert len(squared_norms) >= 2 and half_rows >= 1
    assert squared_norms[0] > max(squared_norms[1:]) > 0
    a = [Fraction(x) for x in squared_norms]
    ratios = [a[0] / z for z in a[1:]]
    total = Fraction(0)
    m = half_rows
    for size in range(1, len(ratios)+1):
        for J in combinations(range(len(ratios)), size):
            r = [ratios[j] for j in J]
            term = Fraction(0)
            for ell in product(range(m), repeat=size):
                degree = sum(ell)
                factor = Fraction(factorial(m+degree-1), factorial(m-1))
                for x,j in zip(r,ell):
                    factor *= x**j / factorial(j)
                term += factor / (1+sum(r))**(m+degree)
            total += term if size % 2 else -term
    return total


def failure_integral(squared_norms, rows):
    a = rows / 2.0
    ratios = [squared_norms[0]/x for x in squared_norms[1:]]
    def integrand(t):
        if t <= 0: return 0.0
        # Conditional failure: at least one smaller column exceeds the first.
        Fs = [float(special.gammainc(a, r*t)) for r in ratios]
        return exp((a-1)*log(t)-t-lgamma(a)) * (1-np.prod(Fs))
    return integrate.quad(integrand, 0, np.inf, epsabs=1e-11, limit=200)[0]


def pair_error(squared_norm_a, squared_norm_b, rows):
    return special.betainc(rows/2, rows/2,
                          squared_norm_b/(squared_norm_a+squared_norm_b))


def run_checks():
    count = 0
    x=sy.symbols('x', positive=True)
    polynomial = sy.expand(4*(2*x+1)**3-27*x*(x+1)**2)
    assert sy.factor(polynomial) == (x-1)**2*(5*x+4)
    count+=1

    # Exact even-row formula against independent integration and beta tails.
    for values in ([9,4,1], [9,4,4,1], [4,2,2,1], [7,5], [25,16,9,4,1]):
        for m in range(1,5):
            exact=failure_even(values,m)
            numerical=failure_integral(values,2*m)
            assert abs(float(exact)-numerical) < 2e-9, (values,m,exact,numerical)
            count+=1
            assert float(exact)>pair_error(values[0],values[1],2*m)-1e-12
            assert float(exact)<=sum(pair_error(values[0],v,2*m) for v in values[1:])+1e-12
            count+=2
            if len(values)==2:
                t=Fraction(values[1],values[0]+values[1])
                binomial=sum(Fraction(comb(2*m-1,j))*t**j*(1-t)**(2*m-1-j)
                             for j in range(m,2*m))
                assert exact==binomial
                count+=1

    # Direct Gaussian sampling of actual sketched column norms.
    rng=np.random.default_rng(138946)
    for squared_norms,rows,trials in [([9,4,1],2,120000),
                                      ([9,4,4,1],4,120000),
                                      ([4,2,2,1],6,120000)]:
        cols=np.sqrt(np.array(squared_norms))
        # Orthogonal input columns: independent Gaussian sketch coordinates.
        sketch=rng.standard_normal((trials,rows,len(cols))) * cols
        sketched_norms=np.sum(sketch*sketch,axis=1)
        observed=np.mean(np.argmax(sketched_norms,axis=1)!=0)
        exact=float(failure_even(squared_norms,rows//2))
        sigma=sqrt(exact*(1-exact)/trials)
        assert abs(observed-exact) < 6*sigma + 5e-4,(observed,exact,sigma)
        count+=1

    # Endpoint Laplace expansion of the two-column beta tail.
    for R in (1.5,2.,5.,10.):
        t=1/(1+R)
        for k in (100,200,400):
            exact=special.betainc(k/2,k/2,t)
            leading=(4*t*(1-t))**(k/2)/((1-2*t)*sqrt(2*pi*k))
            if exact>0 and leading>0:
                assert abs(leading/exact-1) < 25/k
                count+=1
    print('PASS:',count,'exact, symbolic, integrated, direct-sketch and asymptotic checks')
    print('Example exact failure, squared norms [9,4,1], 2 rows:',failure_even([9,4,1],1))
    print('Example exact failure, squared norms [9,4,4,1], 4 rows:',failure_even([9,4,4,1],2))

if __name__=='__main__':run_checks()
