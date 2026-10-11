"""Reproduce algebraic reductions and numerical phase cross-checks for positive harmonic cubics.

This script uses only Python's standard library. Tests supplement, but do not replace,
the exact analytic argument in RESULT.md.
"""
import cmath
import math
import random


def phase(a, b):
    """Claimed number of DISTINCT complex zeros, for real a,b>0 away from roundoff."""
    if not a > 0 or not b > 0:
        raise ValueError('positive parameters only')
    disc = 4*(2*b - a)**3 - 27
    if b <= a:
        if disc < 0:
            return 3
        if disc > 0:
            return 7
        return 5
    h = 3*a - 2*b
    e = 4*(a+2*b)**2*(b-a) - 27
    if disc < 0:
        return 3
    if disc == 0:
        return 5 if h > 0 else 3
    if e > 0:
        return 5
    if e == 0:
        return 5 if h > 0 else 3
    return 7 if h > 0 else 3


def bisect(f, lo, hi):
    flo = f(lo)
    fhi = f(hi)
    assert flo*fhi < 0, (lo, hi, flo, fhi)
    for _ in range(90):
        mid = (lo+hi)/2
        if f(mid)*flo <= 0:
            hi = mid
            fhi = f(mid)
        else:
            lo = mid
            flo = f(mid)
    return (lo+hi)/2


def cubic_real_roots(a, b):
    """Independent root determination from sign changes at stationary points."""
    s = 2*b-a
    g = lambda x: 8*x*x*x-2*s*x+1
    bound = 3+abs(s)
    if s <= 0:
        return [bisect(g,-bound,0)]
    xi = math.sqrt(s/12)
    v = g(xi)
    if v > 1e-10:
        return [bisect(g,-bound,0)]
    negative = bisect(g,-bound,0)
    if abs(v)<1e-10:
        return [negative,xi]
    return [negative, bisect(g,0,xi),bisect(g,xi,bound)]


def actual_count(a, b):
    d = b-a
    roots=cubic_real_roots(a,b)
    return 1+2*sum(3*x*x-d > 1e-10 for x in roots)


def explicit_witness():
    a=3.0
    b=2.5
    roots=[.5,(-1+math.sqrt(5))/4,(-1-math.sqrt(5))/4]
    vals=[]
    for x in roots:
        y=math.sqrt(3*x*x+a-b)
        for sign in [-1,1]:
            z=complex(x,sign*y)
            residual=z**3+a*z+b*z.conjugate()-1
            assert abs(residual)<2e-13,(z,residual)
            jac=abs(3*z*z+a)**2-b*b
            assert abs(jac)>1e-5
            vals.append(z)
    xr=bisect(lambda x:x**3+(a+b)*x-1,0,1)
    vals.append(xr+0j)
    assert abs((xr+0j)**3+a*xr+b*xr-1)<1e-13
    assert len(vals)==7
    assert min(abs(z-w) for i,z in enumerate(vals) for w in vals[i+1:])>.05
    assert phase(a,b)==7


def test_random():
    rng=random.Random(1729)
    tested=0
    for _ in range(20000):
        a=10**rng.uniform(-1.7, 1.4)
        b=10**rng.uniform(-1.7, 1.4)
        d=b-a
        D=4*(2*b-a)**3-27
        E=4*(a+2*b)**2*d-27
        h=3*a-2*b
        if min(abs(D),abs(E),abs(d),abs(h))<1e-6:
            continue
        pred=phase(a,b)
        actual=actual_count(a,b)
        assert pred==actual,(a,b,pred,actual,D,E,h)
        tested+=1
    return tested


def check_boundaries():
    tau=(27/4)**(1/3)
    # The discriminant fold on the orientation-preserving linear sector.
    a=3
    b=(a+tau)/2
    assert a>b and abs(4*(2*b-a)**3-27)<5e-13
    xi=math.sqrt(tau/12)
    assert 3*xi*xi+a-b>0
    # Positive-parameter cusp where discriminant and real-axis collision meet.
    d=tau/4
    a=tau/2
    b=3*tau/4
    t=math.sqrt(d/3)
    xi=math.sqrt(tau/12)
    assert abs(t-xi)<1e-14
    assert abs((t**3+(a+b)*t)-1)<1e-13
    assert abs(4*(2*b-a)**3-27)<1e-12
    assert abs(4*(a+2*b)**2*(b-a)-27)<1e-12
    # Real-axis collision curve on two sides of the cubic minimum.
    for a in (4.0,.05):
        fn=lambda d:4*(3*a+2*d)**2*d-27
        d=bisect(fn,1e-7,8)
        b=a+d
        D=4*(2*b-a)**3-27
        assert D>0,(a,b,D)
        t=math.sqrt(d/3)
        assert abs(t**3+(a+b)*t-1)<1e-12
        assert (3*a-2*b > 0)==(a==4)


if __name__ == '__main__':
    explicit_witness()
    check_boundaries()
    count=test_random()
    print('PASS: exact-form witness, discriminant/collision boundaries, and',count,'independent sampled phase checks')
    print('Finite checks are not the proof of the all-parameter theorem.')
