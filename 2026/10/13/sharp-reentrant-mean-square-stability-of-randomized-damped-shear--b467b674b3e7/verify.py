"""Exact finite-word checks and numerical threshold diagnostics for damped-shear time splitting.

Only the two matrices S1(z), S2(z), with common damping removed, are
used in exact computations. The infinite-step theorem is proved analytically.
No third-party packages required; run with: python verify.py
"""
from fractions import Fraction
from math import exp, isclose, log, sqrt


def apply(which, z, xy):
    x, y = xy
    return (x + z*y, y) if which == 1 else (x, y-z*x)


def norm2(v):
    return v[0]*v[0]+v[1]*v[1]


def exact_checks():
    trials = 0
    for z in [Fraction(0),Fraction(1,2),Fraction(2),Fraction(5,3)]:
        q = 1+z*z/2
        m = 1+z*z/4
        for v in [(Fraction(1),Fraction(0)),
                  (Fraction(1),Fraction(2)),
                  (Fraction(3),Fraction(-4))]:
            initial_norm = norm2(v)
            for n in range(0,8):
                paths = [v]
                for step in range(n):
                    paths = [apply(j,z,xy) for xy in paths for j in (1,2)]
                avg_n2 = sum((norm2(xy) for xy in paths), Fraction(0))/len(paths)
                assert avg_n2 == q**n*initial_norm
                avg = (sum((xy[0] for xy in paths),Fraction(0))/len(paths),
                       sum((xy[1] for xy in paths),Fraction(0))/len(paths))
                assert norm2(avg) == m**n*initial_norm
                trials += 2
    return trials


def threshold_checks():
    def g(s):
        return 2*s/(1+s)-log(1+s)
    low, high = 1.0, 100.0
    for _ in range(90):
        mid = (low+high)/2
        if g(mid)>0: low=mid
        else: high=mid
    s=(low+high)/2
    z=sqrt(2*s)
    beta=2*z/log(1+s)
    assert 3.514698 < beta < 3.514700
    assert isclose(g(s),0,abs_tol=1e-14)
    for b_over_a in [1, 3.5, beta, 3.6, 4, 10]:
        def q(zz):
            return exp(-2*zz/b_over_a)*(1+zz*zz/2)
        samples=[.0001,.5,1,z,3,5,10,100]
        if b_over_a<beta-1e-6:
            assert all(q(xx)<1 for xx in samples)
        if b_over_a>beta+1e-6:
            assert q(z)>1
        if b_over_a==beta:
            assert isclose(q(z),1,abs_tol=1e-13)
    assert 2 < exp(1) < 3
    assert 3/exp(1)>1 and 2/exp(1)<1
    return s,z,beta


if __name__ == '__main__':
    n=exact_checks()
    s,z,beta=threshold_checks()
    print('FINITE_EXACT_CHECKS_OK', n)
    print('THRESHOLD_OK s*=%.12f z*=%.12f b/a*=%.12f'%(s,z,beta))
    print('VERIFICATION_OK')
