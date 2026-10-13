"""Reproduce elementary Dirichlet-spacing identities and asymptotic numeric diagnostics.

Requires Python 3 standard library only. Numerical diagnostics are not proofs.
"""
from fractions import Fraction
from math import comb, factorial, lgamma, log, pi, sqrt, exp

checks = 0


def moments(n, a):
    # n positive Dirichlet(1,...,1) coordinates; a positive integer
    first = Fraction(n * factorial(n-1) * factorial(a), factorial(n+a-1))
    second = Fraction(factorial(n-1) *
                      (n*factorial(2*a) + n*(n-1)*factorial(a)**2),
                      factorial(n+2*a-1))
    return first, second


for n in range(2, 40):
    for a in range(1, 13):
        m1, m2 = moments(n, a)
        assert m2 >= m1*m1
        checks += 1
        if a == 1:
            assert m1 == 1 and m2 == 1
            checks += 1
        if a == 2:
            assert m1 == Fraction(2, n+1)
            assert m2-m1*m1 == Fraction(4*(n-1), (n+1)**2*(n+2)*(n+3))
            checks += 2
        if n == 2:
            # Independent integration of (u**a + (1-u)**a)**2, u uniform [0,1]
            beta = Fraction(factorial(a)**2, factorial(2*a+1))
            assert m1 == Fraction(2, a+1)
            assert m2 == Fraction(2, 2*a+1) + 2*beta
            checks += 2


def cv2_log(n, a):
    # For moderate n, evaluate the exact gamma-moment ratio in log space.
    b = exp(lgamma(2*a+1) - 2*lgamma(a+1))
    h = exp(2*lgamma(n+a) - lgamma(n) - lgamma(n+2*a))
    return h * (1 + (b-1)/n) - 1


# Check that the finite-sample diagnostic heads toward the derived crossover.
for n in (1000, 10000, 100000):
    L = log(n)
    a = (L + 0.5*log(L))/log(4)
    value = cv2_log(n, a)
    target = sqrt(log(4)/pi)
    assert 0.4 < value/target < 1.3
    checks += 1
    print(f'N={n} alpha={a:.8f} CV^2={value:.8f} limiting={target:.8f}')

print(f'VERIFY_OK: {checks} finite exact/numeric checks')
