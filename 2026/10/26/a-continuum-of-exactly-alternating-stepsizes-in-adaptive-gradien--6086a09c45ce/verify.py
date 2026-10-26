#!/usr/bin/env python3
"""Reproducible standard-library checks for the scalar adaptive rule.

All universal results are proved analytically in RESULT.md. These finite exact
algebra checks and high-precision examples diagnose implementation consistency.
"""
from decimal import Decimal, localcontext
from fractions import Fraction

D = Decimal

# Exact rational squared values of the explicit radical witness.
asq = Fraction(13, 12)
bsq = Fraction(13, 14)
assert 1/asq + 1/bsq == 2
assert asq/bsq == Fraction(7, 6)
assert asq > 1 and bsq < 1
assert asq < Fraction(25, 16)
# The ratio sqrt(7/6) is < 11/10, which is < r_*.
assert Fraction(7,6) < Fraction(11,10)**2
assert Fraction(11,10)**3 - Fraction(2,3)*Fraction(11,10) - 1 < 0

with localcontext() as ctx:
    ctx.prec = 80
    def p(r):
        return r**3 - D(2)*r/D(3) - D(1)
    def cap(z):
        den = D(2)*z*z-D(1)
        return z/den.sqrt() if den>0 else D('Infinity')
    lo,hi=D(1),D(5)/4
    for _ in range(300):
        mid=(lo+hi)/2
        if p(mid)<=0:lo=mid
        else:hi=mid
    rstar=(lo+hi)/2
    astar=((D(1)+rstar*rstar)/2).sqrt()
    bstar=astar/rstar
    assert D('1.2193')<rstar<D('1.2194')
    assert D('1.1150')<astar<D('1.1151')
    assert D('0.9144')<bstar<D('0.9146')

    def initial_run(c,n=30):
        s=[c]; ratio=D(1)/3
        for _ in range(n-1):
            q=s[-1]
            v=min(q*(D(2)/3+ratio).sqrt(),cap(q))
            ratio=v/q
            s.append(v)
        return s

    # The original algorithm's theta_0=1/3 creates different first transitions.
    count=0
    for k in range(1,80):
        r=D(1)+(rstar-D(1))*D(k)/80
        a=((D(1)+r*r)/2).sqrt(); b=a/r
        assert abs((a**(-2)+b**(-2))-2)<D('1e-75')
        assert b < 1 < a
        for start,offset in [(a,0),(b,1)]:
            values=initial_run(start,36)
            expected=[a,b] if offset==0 else [b,a]
            for j in range(offset,len(values)):
                goal=expected[(j-offset)%2]
                assert abs(values[j]-goal)<D('1e-65')
                assert values[j]!=1
                count+=1
        # Contraction of actual scalar primal trajectory per two steps.
        rho=(a-D(1))*(D(1)-b)
        assert D(0)<rho<D(1)
        # Away from the sharp threshold both successive caps dominate growth.
        assert b*(D(2)/3+b/a).sqrt() > a
        assert a*(D(2)/3+a/b).sqrt() > b
        # T^2 maps a neighborhood state (p,q) exactly to (cap(q),q).
        q=a+D('1e-12'); p0=b-D('2e-12')
        h=min(q*(D(2)/3+q/p0).sqrt(),cap(q))
        nxt=min(h*(D(2)/3+h/q).sqrt(),cap(h))
        assert abs(h-cap(q))<D('1e-65')
        assert abs(nxt-q)<D('1e-65')
    # At the critical ratio the two competing low-to-high candidates tie.
    assert abs(rstar**2-D(2)/3-D(1)/rstar)<D('1e-70')
    print('VERIFY_OK: exact radical identities; 79 interior cycles, 2 starts each;',
          count,'high-precision sequence checks; cutoff and local collapse')
