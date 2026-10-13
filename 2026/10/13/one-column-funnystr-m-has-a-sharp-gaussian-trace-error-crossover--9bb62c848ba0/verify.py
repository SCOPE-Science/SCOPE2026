"""Standalone numerical consistency checks for the two-eigenvalue funNystrom trace formula.

Python 3 standard library only. These finite checks supplement an analytic proof;
they do not certify an infinite parameter range or literature priority.
"""
import math
from fractions import Fraction


def trace_eigenvalue(kappa, q, x, y):
    k = Fraction(kappa)
    x, y = Fraction(x), Fraction(y)
    return (k ** (2 * q) * x * x + y * y) / (k ** (2 * q - 1) * x * x + y * y)


def check_algebra():
    n = 0
    for k in [2, 3, 4, 7, 16]:
        for q in [1, 2, 3, 4]:
            for x, y in [(1, 1), (2, 3), (1, 7), (9, 2), (5, 11)]:
                tau = trace_eigenvalue(k, q, x, y)
                t = Fraction(x*x, y*y)
                assert k - tau == Fraction(k-1, 1)/(1 + Fraction(k)**(2*q-1)*t)
                assert 1 <= tau <= k
                n += 1
    return n


def simpson(f, a, b, n):
    h = (b-a)/n
    v = f(a)+f(b)
    for j in range(1,n):
        v += (4 if j%2 else 2)*f(a+j*h)
    return v*h/3


def integral_trace_excess(k, q, theta, n=25000):
    """Quadrature of the exact transformed half-Cauchy integral.

    The variable s=sqrt(z) is mapped to t=s/(1+s) in [0,1].
    """
    K=float(k)**(2*q-1)
    def integrand(t):
        if t>=1: return 0.
        s=t/(1-t)
        one_over=1/(1+s*s)
        loss=-math.expm1(theta*math.log1p(-(1-1/k)*one_over))
        return 2*loss/(1+s*s/K)/(1-t)**2
    return (float(k)**(theta-q+0.5))*simpson(integrand,0.,1.,n)/math.pi


def constant(theta):
    return 2*theta*math.gamma(theta+0.5)/(math.sqrt(math.pi)*math.gamma(theta+1))


def run():
    algebra_checks=check_algebra()
    numerical_checks=0
    for q in [1, 2]:
        for k in [4, 9, 16, 36]:
            obtained=integral_trace_excess(k,q,1.0)
            expected=(k-1)/(1+k**(q-0.5))
            assert abs(obtained-expected)<3.e-7, (k,q,obtained,expected)
            numerical_checks += 1
    for theta in [0.25, 0.5, 0.75, 1.0]:
        for q in [1, 2]:
            k=256 if q==1 else 64
            observed=integral_trace_excess(k,q,theta)
            scaled=observed/(k**(theta-q+0.5))
            assert 0.86*constant(theta)<scaled<constant(theta), (q,theta,scaled,constant(theta))
            numerical_checks += 1
    assert abs(constant(0.5)-2/math.pi)<1.e-15
    assert abs(constant(1)-1)<1.e-15
    print('CHECKS_OK algebra=%d quadrature=%d constants=2' % (algebra_checks,numerical_checks))

if __name__=='__main__': run()
