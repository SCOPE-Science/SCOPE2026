#!/usr/bin/env python3
"""Independent exact rational identities and numerical trajectory checks for
alternating survival in quadratic density-limited recruitment. Standard library only.
Run: python3 verify.py
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext


def exact_certificate(delta, q, h):
    """Given rational delta and q=sqrt(1+delta^2), check all asserted identities."""
    delta, q, h = map(F, (delta, q, h))
    assert q*q - delta*delta == 1
    assert h > q
    a, b = h+delta, h-delta
    assert a > 0 and b > 0 and a*b > 1
    r = q+delta
    u2, v2 = (h-q)/r, r*(h-q)
    # u and v need not be rational, but their squares are exact.
    assert (1+u2)*r == a
    assert (1+v2) == b*r
    assert v2 == r*r*u2
    assert r + 1/r == 2*q
    assert r - 1/r == 2*delta
    mean2 = (q+1)*(h-q)/2
    assert mean2 == (u2+v2+2*(h-q))/4  # uv=h-q
    constant_eq2 = h-1
    assert mean2-constant_eq2 == (q-1)*(h-q-2)/2
    return ('resonant' if mean2>constant_eq2 else
            'attenuant' if mean2<constant_eq2 else 'neutral')


def numerical_trajectory(a, b, *, initial):
    with localcontext() as ctx:
        ctx.prec = 65
        a, b, x = Decimal(str(a)), Decimal(str(b)), Decimal(str(initial))
        h, delta = (a+b)/2, (a-b)/2
        q = (Decimal(1)+delta*delta).sqrt()
        if a*b <= 1:
            for t in range(30000):
                c = a if t%2==0 else b
                x = c*x/(1+x*x)
            assert x < Decimal('0.02')
            return
        r = q+delta
        u, v = ((h-q)/r).sqrt(), (r*(h-q)).sqrt()
        for t in range(2000):
            c = a if t%2==0 else b
            x = c*x/(1+x*x)
        # after even number of updates, x approaches u.
        assert abs(x-u) < Decimal('1e-24'), (a,b,initial,x,u)
        assert abs(a*u/(1+u*u)-v) < Decimal('1e-55')
        assert abs(b*v/(1+v*v)-u) < Decimal('1e-55')
        assert abs(((u+v)/2)**2-(q+1)*(h-q)/2) < Decimal('1e-55')


def main():
    cases = (
        (F(3,4), F(5,4), F(2), 'attenuant'),
        (F(3,4), F(5,4), F(13,4), 'neutral'),
        (F(3,4), F(5,4), F(4), 'resonant'),
        (F(0), F(1), F(2), 'neutral'),
        (F(0), F(1), F(8), 'neutral'),
        (F(4,3), F(5,3), F(2), 'attenuant'),
        (F(4,3), F(5,3), F(5), 'resonant'),
    )
    for d,q,h,outcome in cases:
        assert exact_certificate(d,q,h) == outcome
    for a,b in ((7,3),(8,2),(9,1),(3,2),(8,8),(1.1,1.01),(2.1,0.3),
                (10,0.1),(1,1),(3,4),(2,1)):
        for initial in (0.25,1,5):
            numerical_trajectory(a,b,initial=initial)
    # Two contrasting strengths with identical arithmetic mean five.
    with localcontext() as ctx:
        ctx.prec=65
        def gap(a,b):
            h,delta=(Decimal(a)+Decimal(b))/2,(Decimal(a)-Decimal(b))/2
            q=(Decimal(1)+delta*delta).sqrt()
            return (q-1)*(h-q-2)/2
        assert gap(7,3) > 0 and gap(8,2) < 0 and gap(9,1) < 0
    print('VERIFY_OK rational_identity_cases=7 global_orbit_cases=33 finite_amplitude_reversal=PASS')

if __name__=='__main__':
    main()
