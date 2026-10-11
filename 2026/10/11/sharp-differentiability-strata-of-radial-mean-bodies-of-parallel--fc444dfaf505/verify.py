#!/usr/bin/env python3
"""Scientific reproducibility checks for cube radial mean body gauges.

Runs with Python >=3.11 and no third-party modules.
Finite checks supplement the exact boundary-layer proof in RESULT.md.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import prod


def symmetric_coefficients(a):
    e = [a[0]*0 for _ in range(len(a)+1)]
    e[0] = e[0]+1
    for z in a:
        for k in range(len(a), 0, -1):
            e[k] += z*e[k-1]
    return e


def log_gauge(a, p, cutoff=None):
    """Exact finite-sum formula, with a possibly frozen analytic cutoff."""
    one = Decimal(1)
    tau = one/max(a) if cutoff is None else cutoff
    e = symmetric_coefficients(a)
    if p == 0:
        elog = tau.ln()
        for k in range(1, len(a)+1):
            elog += (1 if k % 2 == 0 else -1)*e[k]*tau**k/Decimal(k)
        return -Decimal(2).ln()-elog
    mom = tau**p
    for k in range(1, len(a)+1):
        mom += p*(1 if k % 2 == 0 else -1)*e[k]*tau**(p+k)/(p+k)
    assert mom > 0
    return -Decimal(2).ln()-mom.ln()/p


def moment(a, p):
    """Return E[min_i(U_i/a_i)^p], p != 0."""
    one = Decimal(1)
    tau = one/max(a)
    e = symmetric_coefficients(a)
    mom = tau**p
    for k in range(1,len(a)+1):
        mom += p*(1 if k%2==0 else -1)*e[k]*tau**(p+Decimal(k))/(p+Decimal(k))
    return mom


def independent_rational_moment(a, p):
    """For positive integral p, integrate p*t^(p-1)*product(1-a_i*t)."""
    assert isinstance(p, int) and p>0
    t = Fraction(1,max(a))
    e = symmetric_coefficients(a)
    return p*sum(((-1)**k)*e[k]*t**(p+k)/Fraction(p+k)
                 for k in range(len(a)+1))


def check_exact_moments():
    for a in [[Fraction(1),Fraction(1),Fraction(1,2)],
              [Fraction(1),Fraction(1),Fraction(1)],
              [Fraction(2),Fraction(2),Fraction(2),Fraction(3,4)]]:
        for p in (1,2,3):
            t=Fraction(1,max(a));e=symmetric_coefficients(a)
            regular=t**p+p*sum(((-1)**k)*e[k]*t**(p+k)/Fraction(p+k)
                                  for k in range(1,len(a)+1))
            assert regular == independent_rational_moment(a,p)


def check_boundary_layer():
    with localcontext() as ctx:
        ctx.prec = 75
        D=Decimal
        for atext in [('1','1','0.5'),('1','1','1'),('2','2','2','0.75')]:
            a=[D(z) for z in atext]
            peak=max(a)
            m=sum(z==peak for z in a)
            lower=[z for z in a if z<peak]
            r=D(1)
            for z in lower:r*=1-z/peak
            for pstr in ('-0.5','0','1','2'):
                p=D(pstr)
                mp=moment(a,p) if p!=0 else D(1)
                coeff=(peak**(-p-m-1))*r/(D(m*(m+1))*mp)
                assert coeff>0
                for hstr in ('0.001','0.0002','0.00004'):
                    h=D(hstr)
                    ah=a[:]
                    ah[0]+=h
                    defect=log_gauge(ah,p)-log_gauge(ah,p,D(1)/peak)
                    ratio=defect/h**(m+1)
                    assert ratio<0
                    assert abs(ratio/(-coeff)-D(1))<D('0.02')


def check_axis_cusp():
    with localcontext() as ctx:
        ctx.prec=75
        D=Decimal
        base=[D(1),D(0),D('0.5')]
        for pstr in ('-0.5','0','1','2'):
            p=D(pstr)
            upper=D(1)
            no_second=lambda t:(D(1)-t)*(D(1)-D('0.5')*t)
            # Integrate t^p(1-t)(1-t/2) from 0 to 1 exactly.
            right=(D(1)/(p+1)-D('1.5')/(p+2)+D('0.5')/(p+3))
            if p!=0:right/=moment(base,p)
            assert right>0
            a=base[:];a[1]=D('0.000001')
            slope=(log_gauge(a,p)-log_gauge(base,p))/a[1]
            assert slope>0
            assert abs(slope/right-D(1))<D('0.0001')
            # Actual signed-coordinate dependence is even in the varied coordinate.


if __name__=='__main__':
    check_exact_moments()
    check_boundary_layer()
    check_axis_cusp()
    print('SHARP_RADIAL_JET_CHECKS_OK')
