"""Standalone numerical checks for the two-block product-ball radial-moment theorem.

This checks representative cases only. The all-parameter theorem follows from
ordered-support integral ratios, not from numerical sampling.
"""
import math


def simpson(f, lo, hi, slices=4000):
    if slices % 2:
        raise ValueError("slices must be even")
    h = (hi - lo) / slices
    ans = f(lo) + f(hi)
    for j in range(1, slices):
        ans += (4 if j % 2 else 2) * f(lo + j*h)
    return ans*h/3


def beta(a, b):
    return math.gamma(a)*math.gamma(b)/math.gamma(a+b)


def kappa(d):
    return math.pi**(d/2)/math.gamma(1+d/2)


def integrals(p, q, t, r):
    corner = math.atan(1/r)
    left = simpson(lambda z: math.sin(z)**(p-1)*math.cos(z)**(q-1-t),
                   0, corner)
    right = simpson(lambda z: math.sin(z)**(p-1-t)*math.cos(z)**(q-1),
                    corner, math.pi/2)
    return left, right


def moment(p, q, t, r):
    n = p+q
    a, b = r**(-q/n), r**(p/n)
    left, right = integrals(p, q, t, r)
    return 2*(b**t*left + a**t*right)/beta(p/2, q/2)


def derivative_sign_numerator(p, q, t, r):
    left, right = integrals(p, q, t, r)
    return p*r**t*left - q*right


def root(p, q, t):
    lo, hi = 0.15, 6.0
    vlo = derivative_sign_numerator(p,q,t,lo)
    vhi = derivative_sign_numerator(p,q,t,hi)
    assert vlo*vhi < 0
    for _ in range(43):
        mid = (lo+hi)/2
        v = derivative_sign_numerator(p,q,t,mid)
        if v*vlo > 0:
            lo, vlo = mid, v
        else:
            hi = mid
    return (lo+hi)/2


def verify():
    tests = [(1,2,1,1.1245045156105282),
             (2,3,1,1.0934711358927625),
             (2,2,1,1.0),
             (2,3,7,math.sqrt(5/4)),
             (2,5,9,math.sqrt(7/4))]
    for p,q,t,target in tests:
        r = root(p,q,t)
        assert abs(r-target) < 0.000002, (p,q,t,r,target)
        delta = 0.16
        center = moment(p,q,t,r)
        low = moment(p,q,t,r*math.exp(-delta))
        high = moment(p,q,t,r*math.exp(delta))
        if t < p+q:
            assert center > low and center > high
        else:
            assert center < low and center < high
    for p,q in ((1,2),(2,3),(2,5),(3,3)):
        n = p+q
        expected = kappa(p)*kappa(q)/kappa(n)
        for r in (0.27,0.8,1,2.0,4.1):
            assert abs(moment(p,q,n,r)-expected) < 1e-7
    assert abs(moment(2,2,1,1)-(4-2*math.sqrt(2))) < 1e-9
    for p,q in ((1,2),(2,3),(3,3)):
        t = p+q+2
        r = math.sqrt((q+2)/(p+2))
        assert abs(derivative_sign_numerator(p,q,t,r)) < 1e-8
    print("VERIFY_OK roots=5 critical_moments=20 isotropic_checks=3 closed_example=1")

if __name__ == "__main__":
    verify()
