"""Reproducibility checks for a three-state switching-flow stationary law.

Requires Python 3 with scipy and sympy. These finite checks supplement the
explicit stationary generator identity and the analytic modality proof.
"""
from fractions import Fraction
from itertools import product
from math import gamma, isfinite
from scipy.integrate import quad
from scipy.special import beta


def poch(a, n):
    v = Fraction(1)
    for j in range(n):
        v *= a + j
    return v


def moment(a, e):
    return poch(a, e[0]) * poch(a, e[1]) * poch(a, e[2]) / poch(3 * a, sum(e))


def density(a, x):
    assert 0 < x < 1
    c = gamma(3*a) / (2**(2*a-1) * gamma(a)**3)
    # The transformation u=x+(1-x)t resolves both algebraic endpoint weights.
    f = lambda t: (t*(2*x+(1-x)*t))**(a-1) * (1-t)**(a-1)
    val, err = quad(f, 0.0, 1.0, points=[0, 1], epsabs=2e-10, epsrel=2e-10, limit=400)
    assert err < 5e-7 * (1 + abs(val)), (a,x,err)
    return c * (1-x)**(2*a-1) * val


def check():
    nchecks = 0
    for a in [Fraction(1, 5), Fraction(1,2), Fraction(3,4), Fraction(1), Fraction(2), Fraction(5,2)]:
        q = a
        for n in product(range(6), repeat=3):
            total = sum(n)
            m = moment(a,n)
            for i in range(3):
                e = list(n);e[i] += 1
                residual = (n[i]+q)*m - (total+3*q)*moment(a,e)
                assert residual == 0, (a,n,i,residual)
                nchecks += 1
        # Fractional parameter joint stationary normalization.
        assert sum(moment(a,tuple(1 if j==i else 0 for j in range(3))) for i in range(3)) == 1
        nchecks+=1
    # The exact alpha=1 density is 1-|x|; alpha=2 has a polynomial integrand.
    for x in [0.01,.1,.2,.35,.5,.7,.9,.99]:
        assert abs(density(1,x) - (1-x)) < 2e-9
        nchecks += 1
    # Exact one-point variance: 2/[3(3a+1)].
    for a in [Fraction(1,5),Fraction(1,2),Fraction(1),Fraction(3)]:
        e1,e3 = (1,0,0),(0,0,1)
        var = moment(a,(2,0,0)) + moment(a,(0,0,2)) - 2*moment(a,(1,0,1))
        assert var == Fraction(2,3) / (3*a+1)
        nchecks += 1
    # Strictly decreasing on (0,1) at/above the critical concentration.
    for a in [.5,.51,.7,1.,1.5,3.]:
        xs=[.015,.07,.15,.3,.5,.7,.85,.97]
        ys=[density(a,x) for x in xs]
        assert all(v>u for v,u in zip(ys,ys[1:])),(a,ys)
        nchecks+=len(ys)-1
    # Below critical: exactly the expected downhill-then-uphill trend and
    # nonnegative discrete log-curvature; proof uses Hölder, not this grid.
    for a in [.2,.3,.45]:
        xs=[.01+i*.004 for i in range(245)]
        ys=[density(a,x) for x in xs]
        assert min(ys[15:-15]) < ys[0] and min(ys[15:-15]) < ys[-1]
        from math import log
        ls=[log(v) for v in ys]
        assert min(ls[i]+ls[i+2]-2*ls[i+1] for i in range(len(ls)-2)) > -2e-7
        nchecks+=len(xs)-2
    print(f"PASS: {nchecks} exact and finite numerical checks")

if __name__ == '__main__':
    check()
