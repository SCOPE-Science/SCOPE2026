"""Exact-rational checks for a two-exponential transient-storage travel-time model.

Run: python3 checks/reproduce.py
No third-party dependencies. All parameter identity tests use fractions, not tolerance.
The universal proof is mathematical; these are reproducible independent arithmetic checks.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, isqrt


def cumulants(m, alphas, return_rates, variance):
    inv = [1 / z for z in return_rates]
    out = [m + sum(m * a * x for a, x in zip(alphas, inv)),
           variance + 2 * sum(m * a * x**2 for a, x in zip(alphas, inv))]
    out += [factorial(k) * sum(m * a * x**k for a, x in zip(alphas, inv))
            for k in range(3, 7)]
    return out


def fraction_square_root(q):
    assert q >= 0
    p, d = isqrt(q.numerator), isqrt(q.denominator)
    assert p * p == q.numerator and d * d == q.denominator
    return F(p, d)


def recover(k):
    h0, h1, h2, h3 = [k[j - 1] / factorial(j) for j in (3, 4, 5, 6)]
    delta = h0 * h2 - h1 * h1
    assert delta > 0
    s1 = (h0*h3-h1*h2)/delta
    s2 = (h1*h3-h2*h2)/delta
    disc = s1*s1-4*s2
    assert disc > 0
    root = fraction_square_root(disc)
    xlow, xhigh = (s1-root)/2, (s1+root)/2
    assert 0 < xlow < h1/h0 < xhigh
    wlow = (h0*xhigh-h1)/(xhigh-xlow)
    whigh = (h1-h0*xlow)/(xhigh-xlow)
    assert min(wlow, whigh) > 0
    mobile = k[0] - wlow/xlow**2 - whigh/xhigh**2
    timing_variance = k[1] - 2*(wlow/xlow+whigh/xhigh)
    assert mobile > 0 and timing_variance > 0
    rates = [1/xhigh, 1/xlow]
    alphas = [whigh/(mobile*xhigh**3), wlow/(mobile*xlow**3)]
    return mobile, alphas, rates, timing_variance


def alternative_five(k, low):
    h0, h1, h2 = [k[j-1]/factorial(j) for j in (3,4,5)]
    mu = h1/h0
    vv = h2/h0-mu**2
    assert 0 < low < mu and vv > 0
    high = mu+vv/(mu-low)
    wl = h0*(high-mu)/(high-low)
    wh = h0*(mu-low)/(high-low)
    mobile = k[0]-wl/low**2-wh/high**2
    var = k[1]-2*(wl/low+wh/high)
    assert mobile > 0 and var > 0
    return mobile, [wh/(mobile*high**3), wl/(mobile*low**3)], [1/high,1/low], var


def five_moment_representation(k, d):
    c, mean, second = [k[j-1]/factorial(j) for j in (3, 4, 5)]
    mu = mean/c
    vv = second/c - mu*mu
    assert c > 0 and mu > 0 and vv > 0 and 0 < d < mu
    lo, hi = mu-d, mu+vv/d
    wlo = c*vv/(d*d+vv)
    whi = c*d*d/(d*d+vv)
    s1 = wlo/lo+whi/hi
    s2 = wlo/lo**2+whi/hi**2
    assert s1 == c*(d*(mu-d)+vv)/((mu-d)*(mu*d+vv))
    predicted_h3 = c*(mu**3+3*mu*vv+vv*(vv/d-d))
    return lo,hi,wlo,whi,s1,s2,predicted_h3


def main():
    cases = 0
    for mobile, a, b, fast_rate, slow_rate, sigma2 in product(
        [F(1),F(2),F(7,3)],
        [F(1,5),F(1),F(3,2)],
        [F(1,3),F(2),F(5,3)],
        [F(1),F(3,2),F(2)],
        [F(3),F(4),F(5)],
        [F(1,20),F(1,4),F(2)]):
        # rates sorted slow first, fast second for the returned representation
        k = cumulants(mobile, [a,b], [fast_rate,slow_rate], sigma2)
        m2, aa, bb, sv = recover(k)
        assert m2==mobile and sv==sigma2
        assert bb==[fast_rate,slow_rate]
        assert aa==[a,b]
        assert cumulants(m2,aa,bb,sv)==k
        c = k[2]/6
        mu = (k[3]/24)/c
        vv = (k[4]/120)/c - mu**2
        d = mu-F(1)/slow_rate
        lo,hi,wl,wh,s1,s2,pred_h3=five_moment_representation(k,d)
        assert hi==F(1)/fast_rate and pred_h3==k[5]/720
        assert k[0]-s2==mobile and k[1]-2*s1==sigma2
        assert mu > 0 and vv > 0 and k[0]>c/mu**2 and k[1]>2*c/mu
        cases += 1
    k = cumulants(F(2),[F(1,2),F(3,4)],[F(1),F(3)],F(1,4))
    assert k==[F(7,2),F(31,12),F(19,3),F(220,9),F(3260,27),F(19480,27)]
    other = alternative_five(k,F(3,10))
    assert cumulants(*other)[:5] == k[:5]
    assert cumulants(*other)[5] != k[5]
    m,aa,bb,sv = recover(k)
    assert (m,aa,bb,sv)==(F(2),[F(1,2),F(3,4)],[F(1),F(3)],F(1,4))
    print('PASS:',cases,'parameter sets reconstructed exactly from six cumulants')
    print('PASS: exact rational sample cumulants',', '.join(map(str,k)))
    print('PASS: distinct positive models share first five cumulants and have different sixth cumulants')
    print('PASS: positive feasibility recovered for all tested model cases')

if __name__=='__main__':
    main()
