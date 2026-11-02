"""Supplementary exact-rational checks for scalar capped Anderson AA(1).

The finite checks below supplement the analytic proof; they do not replace its
all-parameter and all-iteration arguments. Run: python verify.py
"""
from fractions import Fraction as F
from math import acos, ceil, isclose, pi, sqrt


def direct_step(q, a, old, cur):
    """Exact constrained two-residual least-squares update."""
    assert old != cur
    t0 = -cur / (old - cur)
    t = min(1 + a, max(-a, t0))
    assert abs(t) + abs(1 - t) <= 1 + 2 * a
    return q * (cur + t * (old - cur))


def capped_orbit(q, a, limit=200):
    errors = [F(1), q]
    if q == 0:
        return errors, 1
    for n in range(1, limit):
        z = direct_step(q, a, errors[-2], errors[-1])
        errors.append(z)
        if z == 0:
            return errors, n + 1
    return errors, None


def raw_affine_orbit(q, b, x0, a, limit=100):
    fixed = b / (1-q)
    xs = [x0, q*x0+b]
    for n in range(1, limit):
        old = xs[-2]
        cur = xs[-1]
        rold = q*old+b-old
        rcur = q*cur+b-cur
        t0 = -rcur/(rold-rcur)
        t = min(1+a, max(-a,t0))
        nxt = t*(q*old+b) + (1-t)*(q*cur+b)
        xs.append(nxt)
        if nxt == fixed:
            return xs, n+1
    return xs, None


def check():
    checks = 0
    # Rational recurrence and independent actual constrained-LS calculation.
    for k in range(1, 20):
        q = F(k, 20)
        for a in [F(0), F(1, 20), F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(1), F(2), F(5)]:
            es, stop = capped_orbit(q, a, 35)
            u = [F(1), q]
            for n in range(2,len(es)):
                u.append(q*((1+a)*u[-1]-a*u[-2]))
            expected = next((n for n in range(2,len(u)) if u[n] <= 0),None)
            assert stop == expected, (q,a,stop,expected)
            if stop is None:
                assert es == u
            else:
                assert es[:-1] == u[:stop] and es[-1] == 0
            checks += len(es)-2
    # A closed-form repeated characteristic root at q=3/4, a=1/3.
    q,a = F(3,4), F(1,3)
    es,stop = capped_orbit(q,a,90)
    assert stop is None
    for n,e in enumerate(es):
        assert e == (F(1)+F(n,2))*F(1,2)**n
        checks += 1
    # The cap-three exact trigonometric first-zero index for rational q.
    for k in range(1,100):
        q=F(k,100)
        es,stop = capped_orbit(q,F(1),150)
        theta=acos(sqrt(float(q)))
        nreal=pi/(2*theta)
        predicted=ceil(nreal-1.e-10)
        assert stop==predicted,(q,stop,predicted,nreal)
        assert es[-1]==0
        checks+=1
    # Fully rational q=9/10 witness, independent from floating point.
    q=F(9,10)
    hypothetical=[F(1),q]
    for n in range(2,6):
        hypothetical.append(q*(2*hypothetical[-1]-hypothetical[-2]))
    assert hypothetical==[F(1),F(9,10),F(18,25),F(243,500),F(567,2500),-F(729,25000)]
    actual,stop=capped_orbit(q,F(1),12)
    assert stop==5 and actual[:-1]==hypothetical[:-1] and actual[-1]==0
    checks+=12
    # Translation and sign covariance of the constrained residual optimization.
    for q in [F(1,4),F(3,5),F(9,10)]:
        for a in [F(1,10),F(1),F(3)]:
            for b,x0 in [(F(2),F(-3)),(F(-5,2),F(4))]:
                xs,ns=raw_affine_orbit(q,b,x0,a,40)
                errors,nr=capped_orbit(q,a,40)
                assert ns==nr and len(xs)==len(errors)
                fixed=b/(1-q)
                e0=x0-fixed
                assert [((x-fixed)/e0) for x in xs]==errors
                checks+=len(xs)-2
    print('VERIFY_OK; exact-rational supplementary checks:',checks)


if __name__=='__main__':
    check()
