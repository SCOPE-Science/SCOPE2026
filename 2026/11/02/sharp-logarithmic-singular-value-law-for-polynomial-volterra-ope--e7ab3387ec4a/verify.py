#!/usr/bin/env python3
"""Independent finite checks of displayed algebra and coefficient normalization.
The analytic singular-value limit is proved separately, not certified here.
"""
import cmath
import math
import random
from fractions import Fraction


def moment(n, alpha=1.7):
    # Gamma(alpha,1) probability measure on positive real shifts.
    return (1+2*math.log(n))**(-alpha)


def volterra_output(coefs, symbol):
    # n^{-s} -> sum_k a_k log(k)/log(n k) (nk)^{-s}.
    out = {}
    for n, val in coefs.items():
        for k, a in symbol.items():
            out[n*k] = out.get(n*k, 0) + val*a*math.log(k)/math.log(n*k)
    return out


def finite_fiber_test(m, poly, symbol):
    # poly specifies normalized input coefficients indexed by prime exponent.
    a = {m*(2**j): val/math.sqrt(moment(m*(2**j))) for j,val in poly.items()}
    raw = volterra_output(a, symbol)
    # Multiplication B(z) = sum a_k log k z^degree, for 2^degree symbols.
    expected = {}
    for j,c in poly.items():
        for k,sym in symbol.items():
            degree = k.bit_length()-1
            assert k==2**degree
            expected[j+degree] = expected.get(j+degree, 0)+c*sym*math.log(k)
    error = 0.0
    norm_expected = 0.0
    for degree, val in expected.items():
        actual = math.log(m)*raw.get(m*(2**degree),0)*math.sqrt(moment(m*(2**degree)))
        error += abs(actual-val)**2
        norm_expected += abs(val)**2
    return math.sqrt(error),math.sqrt(norm_expected)


def main():
    checks=0
    # Exact algebraic stationary point for the interference example.
    c=Fraction(-1,3)
    assert 20-8*c-12*c*c == Fraction(64,3); checks+=1
    # Exact norm formula for |1+2z-3z^2|² on the unit circle.
    for k in range(1001):
        theta=2*math.pi*k/1001
        z=cmath.exp(1j*theta)
        lhs=abs(1+2*z-3*z*z)**2
        rhs=20-8*math.cos(theta)-12*math.cos(theta)**2
        assert abs(lhs-rhs)<1e-11; checks+=1
    # The tilted Bergman moments converge to Hardy coefficients.
    for k in [2,3,4,6,8]:
        diffs=[abs(moment(m*k)/moment(m)-1) for m in (100,10**3,10**5,10**10)]
        assert all(diffs[j]>diffs[j+1] for j in range(len(diffs)-1)); checks+=1
    # Exact coefficient identity and splitting into coprime base fibers.
    rng=random.Random(19273)
    for _ in range(120):
        base=rng.choice([3,5,7,11,13,17,19,23,29,31])
        poly={j:(rng.random()-.5)+1j*(rng.random()-.5) for j in range(3)}
        symbol={2:1+0.2j,4:-0.3+0.2j,8:0.5-0.1j}
        e1,norm=finite_fiber_test(base*10**2,poly,symbol)
        e2,_=finite_fiber_test(base*10**8,poly,symbol)
        e3,_=finite_fiber_test(base*10**20,poly,symbol)
        assert e3<e2<e1 and norm>0;checks+=1
    # Density of odd base indices in intervals [sqrt K,K].
    for K in [10**3,10**4,10**5]:
        count=sum(1 for m in range(math.ceil(math.sqrt(K)),K+1) if m%2)
        assert abs(count/K-0.5)<0.03; checks+=1
    print('PASS',checks,'finite checks; does not certify infinite-dimensional limit')

if __name__=='__main__':main()
