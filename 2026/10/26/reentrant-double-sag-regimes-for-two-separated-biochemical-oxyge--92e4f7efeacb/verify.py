"""Reproducibility checks for the two-outfall oxygen-deficit phase diagram.

Only Python's standard library is needed. Finite checks supplement rather
than replace the analytical proof.
"""
import math
import random
from fractions import Fraction


def g(t, a, b):
    return math.exp(-a*t)-math.exp(-b*t)


def gp(t, a, b):
    return -a*math.exp(-a*t)+b*math.exp(-b*t)


def kappa(t, a, b):
    return (a*math.exp(-a*t)-b*math.exp(-b*t))/(b-a)


def downstream_peak(a, b, k, s):
    return math.log(b*(1+k*math.exp(b*s))/(a*(1+k*math.exp(a*s))))/(b-a)


def d(t, a, b, k, s):
    return g(t,a,b) + (k*g(t-s,a,b) if t>=s else 0.0)


def dd(t, a, b, k, s):
    return gp(t,a,b)+(k*gp(t-s,a,b) if t>=s else 0.0)


def checks():
    # Exact rational phase witnesses, for (a,b,k)=(1,2,1/16).
    k=Fraction(1,16)
    vals=[(Fraction(4,9),Fraction(4,81),True),
          (Fraction(1,4),Fraction(1,8),False),
          (Fraction(1,16),Fraction(7,128),True)]
    for y,threshold,two in vals:
        assert y-2*y*y == threshold
        assert (k>threshold) == two
        s=-math.log(float(y))
        peak=downstream_peak(1.,2.,float(k),s)
        assert (peak>s)==two
        assert abs(dd(s,1.,2.,float(k),s)-float(k-threshold))<1e-12
    assert (Fraction(1,16)-Fraction(4,81))==Fraction(17,1296)
    assert (Fraction(1,16)-Fraction(1,8))==-Fraction(1,16)
    assert (Fraction(1,16)-Fraction(7,128))==Fraction(1,128)

    random.seed(734827)
    tested=0
    for _ in range(15000):
        a=math.exp(random.uniform(-1.5,1.0))
        b=a*random.uniform(1.1,4.0)
        t0=math.log(b/a)/(b-a)
        # Keep exponentials moderate and avoid nearly equal slopes.
        s=random.uniform(.05,5.0)*t0
        k=math.exp(random.uniform(-7,1))
        v=d(s,a,b,k,s)
        left=g(s,a,b)
        assert math.isclose(v,left,rel_tol=1e-12,abs_tol=2e-13)
        kstar=(a/b)**((a+b)/(b-a))
        assert kappa(2*t0,a,b)<=kstar*(1+3e-13)
        assert abs(kappa(2*t0,a,b)/kstar-1)<2e-12
        tpeak=downstream_peak(a,b,k,s)
        right_pos=dd(s,a,b,k,s)>0
        assert (tpeak>s)==right_pos or abs(tpeak-s)<1e-12
        if s>t0 and abs(k-kappa(s,a,b))>1e-11:
            assert right_pos==(k>kappa(s,a,b))
        # The downstream derivative must be positive before its unique
        # stationary point, negative after; test admissible samples.
        for t in [s+0.15*t0,s+1.2*t0,s+3.0*t0]:
            deriv=dd(t,a,b,k,s)
            if abs(t-tpeak)>1e-10:
                assert (deriv>0)==(t<tpeak)
        tested+=1
    return tested

if __name__=='__main__':
    print('Phase witnesses: 3 exact rational cases')
    print('Randomized derivative/comparison checks:',checks())
