"""Reproduce the exact spherical-shell Beer-index identities.

Requires only Python's standard library. Execute with Python 3.10+.
The exact rational grid is an algebraic-identity certificate, not a
finite sampling argument: the common-denominator polynomial has degree
at most 4*d, so 4*d+1 distinct exact roots force it to vanish.
"""
from fractions import Fraction as F
from math import comb, sqrt
import random


def square_moment(d, p, q, a):
    """Return E[(a/R)^p (1-a*a/(R*R))^(q/2)]**2 exactly.

    d is odd and p+q is odd, at most d-2. The integral has one
    possible square-root factor; squaring removes it.
    """
    assert d >= 3 and d % 2 and (p+q) % 2 and 1 <= p+q <= d-2
    k = (d-2-p-q)//2
    delta = 1-a*a
    acc = F(0)
    for j in range(k+1):
        exponent = j+(q//2)+1
        power = F(2*j+q+2, 2)
        acc += F(comb(k,j))*a**(2*(k-j))*delta**exponent/power
    coef = F(d)*a**p*acc/(2*(1-a**d))
    return coef*coef*(delta if q%2 else 1)


def power_mean_cos(d, k, a):
    return sum((-1)**q*comb(k,q)*square_moment(d,k-q,q,a)
               for q in range(k+1))


def computed_index(d, a):
    if d == 3:
        return (1-power_mean_cos(3,1,a))/2
    if d == 5:
        return (2-3*power_mean_cos(5,1,a)+power_mean_cos(5,3,a))/4
    raise ValueError('The verifier displays closed forms for d=3,5')


def closed_index(d, a):
    if d == 3:
        return (1-a)*(9*a**3+27*a*a+24*a+8)/(8*(a*a+a+1)**2)
    if d == 5:
        s=sum(a**j for j in range(5))
        p=65*a**6+260*a**5+405*a**4+320*a**3+160*a*a+64*a+16
        return (1-a)**2*p/(16*s*s)
    raise ValueError('The verifier displays closed forms for d=3,5')


def exact_checks():
    # A common-denominator certificate: each computed value has
    # denominator dividing (1-a**d)**2, and each closed value has
    # denominator dividing 16*(1+a+...+a**(d-1))**2.
    # Clearing both gives a polynomial of degree <= 4*d.
    # We test 4*d+1 distinct rational points, i.e. more roots than degree.
    for d in (3,5):
        count=4*d+1
        for t in range(1,count+1):
            a=F(t,count+3)
            assert computed_index(d,a) == closed_index(d,a), (d,t)
        assert closed_index(d,F(0)) == 1
        assert closed_index(d,F(1)) == 0
    # Exact special evaluations.
    assert closed_index(3,F(1,2)) == F(223,392)
    assert closed_index(5,F(1,2)) == F(10397,15376)
    print('EXACT_IDENTITIES_OK d=3,5 common-denominator degree certificate')


def monte_carlo_diagnostic():
    # This is a diagnostic only, not used for the mathematical proof.
    rng=random.Random(385012)
    for d in (3,5):
        for a in (0.30,0.65):
            n=9000; visible=0
            for _ in range(n):
                x=[rng.gauss(0,1) for _ in range(d)]
                y=[rng.gauss(0,1) for _ in range(d)]
                nr=sqrt(sum(v*v for v in x)); ns=sqrt(sum(v*v for v in y))
                r=(a**d+(1-a**d)*rng.random())**(1/d)
                s=(a**d+(1-a**d)*rng.random())**(1/d)
                x=[v*r/nr for v in x];y=[v*s/ns for v in y]
                z=[v-u for u,v in zip(x,y)]
                t=max(0.0,min(1.0,-sum(u*w for u,w in zip(x,z))/sum(w*w for w in z)))
                visible+=sum((u+t*w)**2 for u,w in zip(x,z))>=a*a
            observed=visible/n; predicted=float(closed_index(d,F(str(a))))
            se=sqrt(predicted*(1-predicted)/n)
            assert abs(observed-predicted)<5*se+0.002, (d,a,observed,predicted)
            print('MC_DIAGNOSTIC d=%d a=%.2f observed=%.5f predicted=%.5f'%(d,a,observed,predicted))


if __name__=='__main__':
    exact_checks()
    monte_carlo_diagnostic()
    print('VERIFY_OK')
