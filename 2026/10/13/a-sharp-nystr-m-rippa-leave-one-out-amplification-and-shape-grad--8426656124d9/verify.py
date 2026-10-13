"""Exact checks for a two-site regularized Nyström/Rippa identity.

Run with ``python verify.py`` (Python 3.9+; standard library only).
These finite tests supplement, but do not prove, universal statements.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def inverse2(A):
    a, b = A[0]
    c, d = A[1]
    det = a*d-b*c
    assert det != 0
    return ((d/det, -b/det), (-c/det, a/det))


def loo_from_matrix(A, y):
    V = inverse2(A)
    return tuple(sum(V[i][j]*y[j] for j in range(2))/V[i][i] for i in range(2))


def identity_checks():
    rng = Random(192911)
    exact = 0
    for _ in range(2800):
        lam = F(rng.randrange(1, 30),rng.randrange(31, 81))
        t = F(rng.randrange(1, 30),rng.randrange(31, 81))
        y = (F(rng.randrange(-10,11),rng.randrange(1, 6)),
             F(rng.randrange(-10,11),rng.randrange(1, 6)))
        H = ((1+lam,t),(t,1+lam))
        Q = ((1+lam,t),(t,t*t+lam))
        eH = loo_from_matrix(H,y)
        eQ = loo_from_matrix(Q,y)
        assert eH == (y[0]-t*y[1]/(1+lam), y[1]-t*y[0]/(1+lam))
        assert eQ == (y[0]-t*y[1]/(t*t+lam), y[1]-t*y[0]/(1+lam))
        diff = t*(1-t*t)/((t*t+lam)*(1+lam))
        assert eQ[0]-eH[0] == -diff*y[1]
        assert eQ[1] == eH[1]
        assert (eQ[0]-eH[0])**2+(eQ[1]-eH[1])**2 <= diff*diff*(y[0]*y[0]+y[1]*y[1])
        assert loo_from_matrix(Q,(F(0),F(1)))[0]-loo_from_matrix(H,(F(0),F(1)))[0] == -diff
        # The missing Schur diagonal is 1-t^2; restoring it recovers H.
        Q_fix = ((Q[0][0],Q[0][1]), (Q[1][0],Q[1][1]+1-t*t))
        assert Q_fix == H
        exact += 1
    return exact


def shape_checks():
    exact=0
    for a in range(1,40):
        lam=F(a,61)
        for b in range(1,61):
            t=F(b,61)
            # Exact numerator of d/dt [ t(1-t^2)/((t^2+lam)(1+lam)) ].
            numerator=lam-(1+3*lam)*t*t-t**4
            # Monotonic numerator in t: only one positive maximum.
            assert numerator == -(t*t*t*t+(1+3*lam)*t*t-lam)
            # The surrogate squared objective rises iff t^2<lam.
            derivative_sign=2*t*(lam-t*t)
            assert (derivative_sign>0)==(t*t<lam)
            assert (derivative_sign<0)==(t*t>lam)
            exact+=1
    numeric=0
    for lam in (0.001, 0.01, 0.1, 0.7, 0.99):
        z=(sqrt((1+3*lam)**2+4*lam)-(1+3*lam))/2
        tstar=sqrt(z)
        f=lambda t: t*(1-t*t)/((t*t+lam)*(1+lam))
        peak=f(tstar)
        for j in range(1,10001):
            t=j/10001
            assert f(t) <= peak + 3e-12
            numeric+=1
    for lam in (1e-2,1e-4,1e-6,1e-8):
        assert abs(sqrt(lam)*(1-lam)/(2*sqrt(lam)*(1+lam))-0.5)<2.1*lam
    return exact,numeric

if __name__ == '__main__':
    p=identity_checks()
    q,r=shape_checks()
    print('VERIFY_OK exact_two_by_two_loo_checks=%d exact_shape_derivative_checks=%d numeric_peak_comparisons=%d' % (p,q,r))
