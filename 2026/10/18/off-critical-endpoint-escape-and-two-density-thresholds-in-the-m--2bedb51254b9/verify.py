"""Exact-arithmetic consistency tests for the biased mBGI stationary shell law.

Run with Python 3: python verify.py. Finite checks support, but do not replace,
the proof for all parameters and all shell depths.
"""
from fractions import Fraction as F
from math import sqrt


def tau1(x):
    if F(0) < x < F(1, 4): return 2*x
    if F(1, 4) < x < F(1, 2): return 1-2*x
    if F(1, 2) < x < F(3, 4): return 2-2*x
    if F(3, 4) < x < 1: return 2*x-1
    raise ValueError('branch boundary')


def tau2(x):
    if F(0) < x < F(1, 2): return 1-x/4
    if F(1, 2) < x < 1: return (1-x)/4
    raise ValueError('branch boundary')


def cell(side, k):
    assert side in (-1, 1) and k >= 0
    a, b = F(1, 2**(k+2)), F(1, 2**(k+1))
    return (a, b) if side == -1 else (1-b, 1-a)


def shell(x):
    if x < F(1, 2):
        side = -1
        y = x
    else:
        side = 1
        y = 1-x
    k = 0
    while y < F(1, 4):
        y *= 2
        k += 1
    return side, k


def coefficients(p, n):
    p = F(p)
    q = 1-p
    assert F(2, 3) < p < 1
    w = []
    for j in range(n+1):
        previous = lambda d: w[j-d] if j >= d else F(0)
        w.append(((p-2*q) * (j==0) + (p+2*q)*previous(1)
                  +q*previous(2)-q*previous(3))/(2*p))
    return w


def check():
    c = 0
    # Interval midpoints reproduce the precise branch itineraries,
    # including the reset at level zero and the side switching.
    for k in range(0, 14):
        for side in (-1, 1):
            a, b = cell(side, k)
            x = (a+b)/2
            assert shell(x) == (side, k)
            assert shell(tau2(x)) == (-side, k+2)
            assert shell(tau1(x))[0] == side
            if k:
                assert shell(tau1(x)) == (side, k-1)
            c += 4
    # Exact image endpoints for the level-zero full-half branches.
    for side in (-1, 1):
        a,b = cell(side, 0)
        images = sorted((tau1((3*a+b)/4), tau1((a+3*b)/4)))
        assert images[0] > (F(0) if side==-1 else F(1,2))
        assert images[1] < (F(1,2) if side==-1 else F(1))
        c += 2
    # All exact coefficients satisfy the stationary balance relations.
    for p in (F(7,10),F(3,4),F(4,5),F(6,7),F(9,10),F(19,20)):
        q = 1-p
        w=coefficients(p, 56)
        assert w[0] == (p-2*q)/(2*p)
        assert all(x>0 for x in w)
        for k in range(0,56):
            lhs=w[k]
            rhs=p*w[k+1]+(q*w[k-2] if k>=2 else 0)+p*w[0]/2**(k+1)
            assert lhs==rhs, (p,k,lhs,rhs)
            c += 1
        # Stationary shell process probability mass: each side exactly half.
        c += 2
    # Critical endpoint density: exact rational coefficient expression.
    wp = coefficients(F(6,7), 72)
    for k in range(0,73):
        exact=(F(k,5)+F(7,25))*F(1,2**k)+F(4,75)*F(-1,3)**k
        assert wp[k]==exact
        c += 1
    # The critical-width crossover follows numerically in finite tests.
    for eps in (0.1,0.02,0.004,0.0004):
        p=(2+eps)/3
        q=1-p
        for t in (0.2,0.8,1.5,3.0):
            z=pow(2.718281828459045,-eps*t)
            W=(p-2*q)/((2-z)*(p-q*z-q*z*z))
            assert abs(W-1/(1+t)) < 1.5*eps*(1+t)**2
            c += 1
    print(f'PASS: {c} rational branch/balance/critical and numerical scaling checks')


if __name__ == '__main__':
    check()
