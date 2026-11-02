"""Exact finite-dimensional checks for the generalized Hénon fold formulas.

Run: python verify_generalized_henon.py
The arbitrary-dimensional theorem is proved algebraically; finite checks are diagnostics.
"""
from fractions import Fraction as F
from math import log


def step(v, a, b):
    return [a - v[-2] ** 2 + b * v[-1]] + v[:-1]


def ell(v, b):
    return sum(v[:-1]) + b * v[-1]


def test_exact():
    for m in range(3, 21):
        for b in (F(1, 9), F(1, 2), F(4, 5), F(9, 10)):
            S = m - 1 + b
            c = (b - 1) / 2
            a0 = -c * c
            D = F((m-1)*(m-2), 2) + (m-1)*b
            Q = [F(j, 1) / S - D / S**2 for j in range(m)]
            assert ell(Q, b) == 0
            # Perron projection and the quadratic center-manifold invariance.
            u = [F(1) for _ in range(m)]
            P = [ (1-b)*u[-2] + b*u[-1] ] + u[:-1]
            assert P == u
            PQ = [(1-b)*Q[-2]+b*Q[-1]]+Q[:-1]
            forcing = [F(1)]+[F(0)]*(m-1)
            assert all(PQ[j]-Q[j] == forcing[j]-F(1,S) for j in range(m))
            H = F((m-1)*(m-2), 2)-b
            assert Q[-2] == H/S**2
            # Coefficient from inversion of the center-map series.
            assert S+2*H == (m-1)**2-b
            for z in (F(-2, 7), F(0), F(1, 11)):
                vector = [c+z+Q[j]*z*z for j in range(m)]
                drift = ell(step(vector, a0, b), b)-ell(vector,b)
                assert drift == -(vector[-2]-c)**2
                at = a0+F(1, 13)
                drift_general = ell(step(vector,at,b),b)-ell(vector,b)
                assert drift_general == (at-a0)-(vector[-2]-c)**2
    print('Exact rational identities: PASS (m=3..20, four rational damping values).')


def test_observed_rate():
    # Numerical tests are only supplementary: no finite test proves an asymptotic.
    for m,b in ((3,.5),(4,.7),(5,.2)):
        c=(b-1)/2
        a0=-c*c
        S=m-1+b
        x=[c+.15]*m
        checkpoints={}
        for n in range(1,80001):
            x=step(x,a0,b)
            if n in (10000,20000,40000,80000):
                z=ell([t-c for t in x],b)/S
                checkpoints[n]=n*n*(z-S/n)
        empirical=(checkpoints[80000]-checkpoints[10000])/log(8)
        theoretical=-((m-1)**2-b)
        # Slow approach because the remaining O(1/n) correction is not removed.
        assert abs(empirical-theoretical)<0.5
        print(f'm={m}, b={b}: expected logarithmic slope {theoretical:.6g}, finite-window {empirical:.6g}')
    print('Finite-trajectory diagnostics: PASS (not an infinite-time proof).')


if __name__ == '__main__':
    test_exact()
    test_observed_rate()
