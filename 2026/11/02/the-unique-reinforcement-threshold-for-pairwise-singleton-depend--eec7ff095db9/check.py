"""Exact arithmetic reproducibility checks for Dirichlet-multinomial singleton dependence.
No random simulation or external packages required.
Run: python3 check.py
"""
from fractions import Fraction
from math import comb, factorial


def rising(x, n):
    z = Fraction(1)
    for k in range(n):
        z *= x + k
    return z


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total-first, length-1):
            yield (first,) + tail


def closed_singletons(m, alpha):
    n = m + 1
    z = rising(m*alpha, n)
    p = n*alpha*rising((m-1)*alpha, n-1)/z
    q = n*(n-1)*alpha*alpha*rising((m-2)*alpha, n-2)/z if m >= 3 else Fraction(0)
    return p, q


def exhaustive_singletons(m, alpha):
    n = m + 1
    norm = rising(m*alpha, n)
    p = q = total = Fraction(0)
    for counts in compositions(n, m):
        weight = Fraction(factorial(n), 1)
        for c in counts:
            weight = weight*rising(alpha, c)/factorial(c)
        weight /= norm
        total += weight
        if counts[0] == 1:
            p += weight
            if counts[1] == 1:
                q += weight
    assert total == 1, (m, alpha, total)
    return p, q


def ratio(m, alpha):
    assert m >= 3
    n = m+1
    return (Fraction(m, n)*rising(m*alpha,n)*rising((m-2)*alpha,n-2)
            / (rising((m-1)*alpha,n-1)**2))


def small_parameter_limit(m):
    return Fraction(m**3*(m-2), (m+1)*(m-1)**3)


def large_parameter_limit(m):
    t = m-1
    return Fraction(m**3,(m+1)*t**2)*Fraction(t*t-1,t*t)**t


def prove_binomial_certificate(t):
    assert t >= 4
    L = Fraction(1)-Fraction(1,t)+Fraction(t-1,2*t**3)-Fraction((t-1)*(t-2),6*t**5)
    P = 3*t**6-7*t**5-6*t**4-2*t**3-t**2-3*t-2
    assert (t+1)**3 * L - (t+2)*t*t == Fraction(P,6*t**5)
    u = t-4
    assert P == (3*u**6+65*u**5+574*u**4+2622*u**3+6439*u**2+7829*u+3426)
    assert P > 0


def main():
    total = 0
    for m in range(2, 7):
        for alpha in (Fraction(1,4), Fraction(1), Fraction(2)):
            p,q = closed_singletons(m, alpha)
            pe,qe = exhaustive_singletons(m, alpha)
            assert p == pe and q == qe
            total += 2
            if m >= 3:
                assert ratio(m,alpha) == q/(p*p)
                total += 1
    assert Fraction(27,32) == small_parameter_limit(3)
    assert Fraction(243,256) == large_parameter_limit(3)
    assert Fraction(128,135) == small_parameter_limit(4)
    assert Fraction(32768,32805) == large_parameter_limit(4)
    assert Fraction(125,128) == small_parameter_limit(5)
    assert Fraction(2109375,2097152) == large_parameter_limit(5)
    total += 6
    for m in range(3,21):
        assert small_parameter_limit(m) < 1
        if m in (3,4):
            assert large_parameter_limit(m) < 1
        else:
            assert large_parameter_limit(m) > 1
        total += 2
    for t in range(4,51):
        prove_binomial_certificate(t)
        total += 3
    p,q = closed_singletons(5,Fraction(1,4))
    assert q-p*p == Fraction(-417706,13461800625)
    p,q = closed_singletons(5,Fraction(1))
    assert q-p*p == Fraction(1,3150)
    assert ratio(5,Fraction(1,4)) == Fraction(134008875,134217728)
    assert ratio(5,Fraction(1)) == Fraction(225,224)
    total += 4
    print('PASS:',total,'exact rational / identity / sign assertions')
    print('m=5, alpha=1/4: negative covariance -417706/13461800625')
    print('m=5, alpha=1: positive covariance 1/3150')
    print('Analytic infinite-family proof and strict monotonicity require RESULT.md.')

if __name__ == '__main__':
    main()
