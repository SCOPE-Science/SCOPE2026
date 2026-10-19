"""Exact-rational and reproducible numerical checks for the temporally refreshed
three-person local-flip map. Python >=3.9; standard library only.
The proof of the infinite-time theorem is in RESULT.md, not this finite checker.
"""
from fractions import Fraction as F
from random import Random
from math import log, exp


def update(p, a, b):
    one = F(1)
    return ((one-b)*p**3 + 3*(one-a)*p**2*(one-p)
            + 3*a*p*(one-p)**2 + b*(one-p)**3)


def coefficient(x, a, b):
    return (3-x-3*(1-x)*a-(3+x)*b)/2


def second_moment(x):
    return (9-6*x+5*x*x)/24


def exact_tests():
    checks = 0
    vals = [F(i, 8) for i in range(9)]
    for p in vals:
        q = 2*p-1
        x = q*q
        for a in vals:
            for b in vals:
                assert 2*update(p,a,b)-1 == q*coefficient(x,a,b)
                assert coefficient(x,1-a,1-b) == -coefficient(x,a,b)
                assert 0 <= update(p,a,b) <= 1
                checks += 3
    for x in vals:
        va = -3*(1-x)/2
        vb = -(3+x)/2
        assert (va*va + vb*vb)/12 == second_moment(x)
        assert second_moment(x) <= F(3,8)
        assert second_moment(x) >= 0
        checks += 3
    assert F(3,8)-second_moment(F(0)) == 0
    assert second_moment(F(1)) == F(1,3)
    assert F(1,3)**2 == F(1,9)  # two instability triangles
    checks += 3
    return checks


def numerical_path(n=180000, seed=8173):
    rng = Random(seed)
    z_sign = 1
    ell = log(0.77)   # initial imbalance |z_0|; exact model via log amplitude
    nplus = 0
    increments = []
    for t in range(n):
        x = exp(2*ell) if ell > -375 else 0.0
        a, b = rng.random(), rng.random()
        c = (3-x-3*(1-x)*a-(3+x)*b)/2
        if c < 0: z_sign *= -1
        if z_sign > 0: nplus += 1
        ell += log(abs(c))
        if t in (49, 199, 999):
            increments.append((t+1,ell/(t+1)))
    target = log(1.5)-1.5
    rate = ell/n
    assert abs(rate-target) < 0.02, (rate,target)
    assert abs(nplus/n - 0.5) < 0.02
    return rate,target,nplus/n,increments

if __name__ == '__main__':
    k = exact_tests()
    rate, target, positive, early = numerical_path()
    print('Exact rational identities checked:',k)
    print('Observed logarithmic rate:',f'{rate:.9f}')
    print('Theoretical rate:',f'{target:.9f}')
    print('Fraction of positive-majority rounds:',f'{positive:.6f}')
    print('Early trajectory rates:',early)
    print('PASS: exact identities and indicative numerical checks')
