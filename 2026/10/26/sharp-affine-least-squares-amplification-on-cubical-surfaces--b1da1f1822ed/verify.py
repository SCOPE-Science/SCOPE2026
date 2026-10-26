"""Exact and independent high-precision tests for affine facet-surface projector constants.
Requires Python 3.9+ and mpmath. Run: python verify.py
"""
from fractions import Fraction as F
from math import comb, factorial, pi, sqrt
import mpmath as mp


def uniform_shift_moment(k, t):
    """Exact mean absolute value of sum of k iid U[-1,1] plus nonnegative t."""
    t = F(t)
    assert k >= 1 and t >= 0
    a = (F(k) - t)/2
    if a <= 0:
        return t
    return t + F(4, factorial(k+1))*sum(
        (-1)**j*comb(k,j)*(a-j)**(k+1)
        for j in range(a.numerator//a.denominator+1)
    )


def surface_constant(d):
    assert isinstance(d,int) and d >= 2
    c = F(3*d,d+2)
    a = 1/c
    return c/2*(uniform_shift_moment(d-1,1+a)
                +uniform_shift_moment(d-1,1-a))


def volume_constant(d):
    assert isinstance(d,int) and d>=1
    a=F(3*d-1,6)
    return F(1) + F(12,factorial(d+1))*sum(
        (-1)**j*comb(d,j)*(a-j)**(d+1)
        for j in range(a.numerator//a.denominator+1)
    )


def density_sum_uniform(k,s):
    """Independent Irwin--Hall density in mpmath: piecewise polynomial."""
    t=(mp.mpf(s)+k)/2
    if t<=0 or t>=k:return mp.mpf(0)
    a=mp.fsum([(-1)**j * comb(k,j) * (t-j)**(k-1)
            for j in range(int(mp.floor(t))+1)])
    return a/(2*factorial(k-1))


def integrated_surface(d):
    """Independent facet-mixture integral of an absolute affine kernel."""
    k=d-1
    c=mp.mpf(3*d)/(d+2)
    total=mp.mpf(0)
    for sign in [-1,1]:
        root=-mp.mpf(1)/c-sign
        knots=sorted(set([-mp.mpf(k),mp.mpf(k),root] +
                         [mp.mpf(2*j-k) for j in range(k+1)]))
        for lo,hi in zip(knots[:-1],knots[1:]):
            lo=max(lo,-k);hi=min(hi,k)
            if hi<=lo:continue
            total+=mp.quad(lambda s: abs(1+c*(s+sign))*density_sum_uniform(k,s),[lo,hi])/2
    return total


def main():
    mp.mp.dps=65
    checked=0
    assert surface_constant(2)==F(5,3);checked+=1
    assert surface_constant(3)==F(94,45);checked+=1
    assert volume_constant(2)==F(233,108);checked+=1
    for d in range(2,11):
        a=surface_constant(d);b=volume_constant(d)
        assert a>1 and b>1;checked+=2
        assert a < b;checked+=1  # finite sample only; not an all-d proof
        assert abs(mp.mpf(a.numerator)/a.denominator-integrated_surface(d)) < mp.mpf('1e-24')
        checked+=1
    for d in [20,30,50,80,100,150,200]:
        s=float(surface_constant(d));v=float(volume_constant(d))
        lead=sqrt(6*d/pi)
        delta=d*(s/lead-1)
        # First correction should approach -47/60; residual is O(1/d).
        assert abs(delta+47/60)<5/d
        assert abs(d*(v/lead-1)-13/60)<1/d
        assert abs((v-s)*sqrt(d)/sqrt(6/pi)-1)<4/d
        checked+=3
    print(f'PASS: {checked} rational/high-precision and asymptotic checks')

if __name__=='__main__': main()
