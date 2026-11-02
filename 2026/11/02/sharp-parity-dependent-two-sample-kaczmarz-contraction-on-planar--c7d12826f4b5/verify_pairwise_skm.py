"""Reproduce numerical tests for the sharp pairwise sample-and-project bound.

Requires Python >= 3.9 standard library only. Finite tests corroborate, but do not prove,
the exact trigonometric identities and their global extremality.
"""
import math
import random


def exact_factor(m):
    assert isinstance(m, int) and m >= 3
    if m % 2:
        c = math.cos(math.pi/(2*m)) / math.sin(math.pi/(2*m))
        return 0.5 + c*c/(2*m*(m-1))
    p = math.pi/m
    return 0.5 + 2*math.cos(p)/(math.sin(p)**2*m*(m-1))


def direct_factor(m, theta):
    weights = [math.cos(theta - j*math.pi/m)**2 for j in range(m)]
    total = sum(max(weights[i], weights[j])
                for i in range(m) for j in range(i+1, m))
    return total/(m*(m-1)/2)


def row_factor_even(m):
    p=math.pi/m
    return 0.5 + (2/(math.sin(p)**2)-1)/(m*(m-1))


def verify():
    rng=random.Random(20261027)
    cases=0
    for m in range(3, 75):
        lam=exact_factor(m)
        f0=direct_factor(m,0)
        f1=direct_factor(m,math.pi/(2*m))
        if m%2:
            assert abs(f0-f1)<4e-13
            assert abs(lam-f0)<4e-13
        else:
            gap = (math.tan(math.pi/(2*m))**2)/(m*(m-1))
            assert abs(f0-row_factor_even(m))<4e-13
            assert abs(f0-f1-gap)<4e-13
            assert abs(lam-f1)<4e-13
        for k in range(100):
            theta=(k+0.381*rng.random())*math.pi/(100*m)
            f=direct_factor(m, theta)
            assert f+5e-13>=lam, (m,theta,f,lam)
            cases+=1
        # Uniformly sampled single-row expected progress equals 1/2.
        for theta in (0.0, .02, .43):
            avg=sum(math.cos(theta - j*math.pi/m)**2 for j in range(m))/m
            assert abs(avg-.5)<4e-13
    for m in (101, 251, 501):
        assert abs(exact_factor(m)-(.5+2/math.pi**2))<.004
    # Exact small example: m=4, bisector has factor (3+sqrt(2))/6.
    assert abs(exact_factor(4)-(.5+math.sqrt(2)/6))<1e-13
    # The global minimum is attained at the stated orientation.
    for m in range(3, 75):
        th=0.0 if m%2 else math.pi/(2*m)
        assert abs(direct_factor(m,th)-exact_factor(m))<4e-13
    print('VERIFY_OK: m=3..74, %d angular probes, even parity gaps, odd ties, and large-m limits' % cases)

if __name__=='__main__':
    verify()
