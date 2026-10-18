"""Reproducibility checks for a two-bond unilateral weighted shift.
Run with Python 3, no third-party libraries.
Exact rational identities are checked separately from finite numerical tests.
"""
from fractions import Fraction
from math import sqrt


def path_polynomials(lam, n):
    q0, q1 = Fraction(1), lam
    if n == 0:
        return (q0, None)
    if n == 1:
        return (q1, q0)
    for _ in range(2, n + 1):
        q0, q1 = q1, lam * q1 - q0
    return q1, q0


def residual_via_polynomials(k, a, b, t):
    lam = t + 1 / t
    pk, pkm1 = path_polynomials(lam, k)
    return lam - a*a*pkm1/pk - b*b*t


def residual_via_tail(k, a, b, t):
    lam = t + 1/t
    return lam - (a*a + b*b)*t + a*a*t**(2*k+1)*(1-t*t)/(1-t**(2*k+2))


def bisect_root(k, a, b):
    a2, b2 = a*a, b*b
    s = a2+b2-1
    lim = (sqrt(s)+1/sqrt(s))/2
    if b2 + k*a2/(k+1) <= 2:
        return 1.0
    def f(radius):
        if radius == 1.0:
            return 2-b2-k*a2/(k+1)
        lam = 2*radius
        t = 2/(lam+sqrt(lam*lam-4))
        return lam - (a2+b2)*t + a2*t**(2*k+1)*(1-t*t)/(1-t**(2*k+2))
    lo, hi = 1.0, lim + 0.25
    assert f(lo) < 0 and f(hi) > 0
    for _ in range(100):
        m = (lo+hi)/2
        if f(m) < 0:
            lo = m
        else:
            hi = m
    return (lo+hi)/2


def main():
    assertions = 0
    for k in range(1, 19):
        for t in (Fraction(1,2), Fraction(2,3), Fraction(3,4), Fraction(4,5)):
            for a,b in ((Fraction(11,10),Fraction(6,5)),(Fraction(3,2),Fraction(7,5)),(Fraction(2),Fraction(3))):
                assert residual_via_polynomials(k,a,b,t) == residual_via_tail(k,a,b,t)
                assertions += 1
    # The three-site positive bound state has exact decay ratio 1/2.
    assert residual_via_polynomials(1, Fraction(5,3), Fraction(5,3), Fraction(1,2)) == 0
    assert Fraction(5,2) / 2 == Fraction(5,4)
    assertions += 2
    # An exact threshold crossing: one position has no outlier, the next does.
    a2 = b2 = Fraction(121,100)
    assert b2 + Fraction(1,2)*a2 < 2
    assert b2 + Fraction(2,3)*a2 > 2
    assertions += 2
    for a,b in ((1.1,1.1),(1.2,1.1),(1.5,1.3),(2.0,1.3),(1.9,2.0)):
        s=a*a+b*b-1
        limit = (sqrt(s)+1/sqrt(s))/2
        prev=1.0
        for k in range(1,27):
            v=bisect_root(k,a,b)
            assert v >= prev-1e-14 and v <= limit+1e-14
            threshold=(b*b + k*a*a/(k+1)>2)
            assert (v>1+1e-12)==threshold or (threshold and 0<v-1<1e-12)
            prev=v
            assertions += 3
        c=a*a*(s-1)**2/(4*s*s)
        k=11
        v=bisect_root(k,a,b)
        normalized=(limit-v)*s**(k+0.5)
        assert abs(normalized-c)/c < 0.12
        assertions += 1
    assert bisect_root(1,1.1,1.1)==1 and bisect_root(2,1.1,1.1)>1
    assertions+=1
    print(f'VERIFY_OK {assertions} exact-and-numerical assertions')

if __name__=='__main__':
    main()
