"""Exact finite checks for scalar Bernoulli control-variate positivity.

These checks test the algebra at finite sizes; they do not replace proofs.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt


def calc(p, eta, beta, mask):
    n = len(p)
    return beta + sum((p[i] - beta) for i in range(n) if mask >> i & 1) / (n * eta)


def threshold(p, eta):
    a = sorted(p)
    n = len(p)
    return min(sum(a[:k]) / (k - n * eta)
               for k in range(1, n + 1) if k > n * eta)


def finite_dispersion_cap(n, high):
    return max([F(k*(n-k), n) * (high-1) /
                (k+(n-k)*high) for k in range(1,n)] or [F(0)])


def test():
    masks = 0
    bounds = 0
    phase = 0
    for n in range(1, 6):
        for pp in product((F(1), F(2), F(4), F(9)), repeat=n):
            mean = sum(pp)/n
            minimum = sum((mean - x) for x in pp if x < mean) / n
            raw = minimum / mean
            assert raw <= finite_dispersion_cap(n, F(9))
            bounds += 1
            for eta in (F(1,5), F(2,5), F(1,2), F(3,4)):
                beta_crit = threshold(pp, eta)
                mval = min(calc(pp,eta,mean,mask) for mask in range(1<<n))
                assert mval == mean-minimum/eta
                assert beta_crit > 0
                assert all(calc(pp,eta,beta_crit*F(9,10),mask)>0
                           for mask in range(1<<n))
                assert min(calc(pp,eta,beta_crit,mask)
                           for mask in range(1<<n)) == 0
                assert min(calc(pp,eta,beta_crit*F(11,10),mask)
                           for mask in range(1<<n)) < 0
                phase += 1
                masks += 3*(1<<n)
    p=(F(1),F(1),F(1),F(9))
    eta=F(2,5)
    assert sum(p)/4==3
    assert threshold(p,eta)==F(15,7)
    assert calc(p,eta,F(3),7)==F(-3,4)
    assert calc(p,F(1,2),F(3),7)==0
    # Exact endpoints for square condition ratios: kappa=t^2, low/high frequencies t:(1).
    for t in range(2,11):
        p=(F(1),)*t+(F(t*t),)
        eta=F(t-1,t+1)
        mean=sum(p)/len(p)
        assert mean==t
        assert min(calc(p,eta,mean,mask) for mask in range(1<<len(p)))==0
    print('VERIFY_OK coefficient_arrays=', bounds,
          ' mask_tests=', masks, ' positivity_threshold_tests=',phase,
          ' square_contrast_equalities=',9)


if __name__ == '__main__':
    test()
