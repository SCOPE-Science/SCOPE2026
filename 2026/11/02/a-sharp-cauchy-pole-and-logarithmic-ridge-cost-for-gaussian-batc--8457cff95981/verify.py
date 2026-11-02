"""Reproducible algebraic and numerical checks for the scalar Gaussian-batch Polyak theorem.

Run with Python 3.10+ using only the standard library. The analytic proof, not
finite samples or numerical quadrature, establishes all asymptotic statements.
"""
import math
import random
from fractions import Fraction


def simpson(f, a, b, n=6000):
    assert n > 0 and n % 2 == 0
    h = (b-a)/n
    total = f(a) + f(b)
    for j in range(1,n):
        total += (4 if j % 2 else 2)*f(a+j*h)
    return total*h/3


def c_constant(k, beta, sigma, delta):
    return (beta*sigma/math.sqrt(math.pi)
            * math.gamma((k+1)/2)/math.gamma(k/2)
            * (1+(delta/sigma)**2)**(-(k-1)/2))


def verify():
    rng = random.Random(20261028)
    rational_tests = 0
    for k in (1,2,3,5,9):
        for _ in range(140):
            xx = [Fraction(rng.randint(-9,9),rng.randint(1,9)) for j in range(k)]
            yy = [Fraction(rng.randint(-9,9),rng.randint(1,9)) for j in range(k)]
            s = sum(v*v for v in xx)
            if not s:
                continue
            ht = sum(a*b for a,b in zip(xx,yy))/s
            residual = sum((b-a*ht)**2 for a,b in zip(xx,yy))
            x = Fraction(rng.randint(-8,8),rng.randint(1,9))
            if x == ht:
                continue
            loss = sum((a*x-b)**2 for a,b in zip(xx,yy))/(2*k)
            gradient = sum(a*(a*x-b) for a,b in zip(xx,yy))/k
            assert loss == (s*(x-ht)**2+residual)/(2*k)
            assert gradient == s*(x-ht)/k
            assert x-loss/gradient == x-(x-ht)/2-residual/(2*s*(x-ht))
            assert x-(loss-residual/(2*k))/gradient == (x+ht)/2
            e = Fraction(rng.randint(1,15),rng.randint(1,15))
            ridge=x-loss*gradient/(gradient*gradient+e)
            t=x-ht
            ridge_formula=x-(t/2+residual/(2*s*t))/(1+e*k*k/(s*s*t*t))
            assert ridge == ridge_formula
            rational_tests += 1

    gamma_integrals=0
    for k in (2,3,5,8):
        for delta in (0.,0.4,1.2):
            # S is chi-square(k); integrate E[S^-1/2 exp(-delta^2 S/2)]
            z=1+delta**2
            quadrature=simpson(lambda t: 2*t**(k-2)*math.exp(-z*t*t/2)
                /(2**(k/2)*math.gamma(k/2)),0,12)
            exact=(math.gamma((k-1)/2)/math.gamma(k/2)
                   /math.sqrt(2)*z**(-(k-1)/2))
            assert abs(quadrature-exact)<2e-5, (k,delta,quadrature,exact)
            # Independent expression for the tail constant, before gamma simplification.
            direct=(k-1)/math.sqrt(2*math.pi)*quadrature
            assert abs(direct-c_constant(k,1,1,delta))<2e-5
            gamma_integrals += 1

    # The calibrated recursion has innovation variance sigma^2/(k-2).
    variance_tests=0
    for k in (3,4,7,12):
        for beta in (Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(2)):
            a=1-beta/2
            b=beta/2
            expression=b*b/(1-a*a)*Fraction(1,k-2)
            expected=beta/(4-beta)*Fraction(1,k-2)
            assert expression == expected
            variance_tests+=1

    # Diagnostics only: iid Gaussian regression batch, at population optimum.
    sample_count=190000
    for k in (2,3,5):
        hits=0
        threshold=32
        for _ in range(sample_count):
            s=sum(rng.gauss(0,1)**2 for _ in range(k))
            zz=rng.gauss(0,1)
            vv=sum(rng.gauss(0,1)**2 for _ in range(k-1))
            val=(zz+vv/zz)/(2*math.sqrt(s))
            hits+=abs(val)>threshold
        observed=threshold*hits/sample_count
        exact=c_constant(k,1,1,0)
        assert abs(observed-exact)/exact<0.17,(k,observed,exact)
        print(f'tail k={k}: t*P(|step|>t)~{observed:.4f}; limit={exact:.4f}')
    print(f'PASS: {rational_tests} exact rational update checks; '
          f'{gamma_integrals} gamma-constant quadratures; '
          f'{variance_tests} exact variance identities; '
          f'{3*sample_count} diagnostic tail samples')


if __name__ == '__main__':
    verify()
