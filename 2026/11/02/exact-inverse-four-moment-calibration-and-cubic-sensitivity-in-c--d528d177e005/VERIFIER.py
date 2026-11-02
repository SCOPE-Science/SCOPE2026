"""Exact rational checks for cyclic phase-type four-moment calibration."""
from fractions import Fraction as F
from math import comb, factorial


def polynomials(s, x):
    b2 = (s + 1) + 2 * s * x
    b3 = (s + 1) * (s + 2) + 6 * s * (s + 1) * x + 6 * s * s * x * x
    b4 = ((s + 1) * (s + 2) * (s + 3)
          + 2 * s * (s + 1) * (7 * s + 11) * x
          + 36 * s * s * (s + 1) * x * x + 24 * s**3 * x**3)
    return b2, b3, b4


def moments_by_recurrence(s, p):
    a = [F(1)]
    for k in range(1, 5):
        a.append(-sum(F((-1)**j * comb(s, j)) * a[k-j]
                      for j in range(1, min(s, k)+1)) / (1-p))
    return [factorial(k) * a[k] for k in range(5)]


def derivative_numerator(s, x):
    return (2*s*(s-1)*(s+1) *
            (18*s*s*x*x + (4*s**3+18*s*s+14*s)*x
             + 2*s**3+7*s*s+7*s+2))


def derivative_identity(s, x):
    b2,b3,b4 = polynomials(s,x)
    db2 = 2*s
    db3 = 6*s*(s+1)+12*s*s*x
    db4 = (2*s*(s+1)*(7*s+11)+72*s*s*(s+1)*x+72*s**3*x*x)
    return ((db2*b4+b2*db4)*b3-2*b2*b4*db3 == derivative_numerator(s,x))


def run():
    n=0
    for s in range(3,25):
        for p in (F(0), F(1,10), F(1,3), F(1,2), F(3,4), F(9,10)):
            x=p/(1-p)
            mu=moments_by_recurrence(s,p)
            b2,b3,b4=polynomials(s,x)
            assert mu[1] == s*(1+x)
            assert mu[2] == s*(1+x)*b2
            assert mu[3] == s*(1+x)*b3
            assert mu[4] == s*(1+x)*b4
            assert mu[2]*mu[4]/mu[3]**2 == b2*b4/b3**2
            assert derivative_identity(s,x)
            assert derivative_numerator(s,x) > 0
            H=b2*b4/b3**2
            assert F(s+3,s+2) <= H < F(4,3)
            n+=1
    print('PASS:',n,'exact-rational PH moment and derivative cases')
    for s in range(3,25):
        for x in (F(0), F(1,10), F(1), F(7), F(100)):
            assert derivative_identity(s,x)
    print('PASS: additional derivative identities')
    print('Universal theorem uses the displayed polynomial identity and positivity, not finite enumeration.')


if __name__ == '__main__':
    run()
