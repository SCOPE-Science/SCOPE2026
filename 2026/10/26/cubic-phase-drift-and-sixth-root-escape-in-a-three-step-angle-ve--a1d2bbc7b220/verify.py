"""Reproduce finite checks for an implicit sine-driven velocity map.

All observations below are finite precision diagnostics. The uniform
all-phase theorem and long-time laws follow from the analytic proof.
"""
from decimal import Decimal, localcontext
from math import sin, pi


def high_precision_step(y, a):
    with localcontext() as ctx:
        ctx.prec = 65
        t = a / y
        r = (Decimal(1) + t + (Decimal(1)+6*t+t*t).sqrt()) / 2
        return y*r*r


def return_map(y, p, theta):
    with localcontext() as ctx:
        ctx.prec = 65
        a0 = Decimal(str(p*sin(theta)))
        a1 = Decimal(str(p*sin(theta+2*pi/3)))
        a2 = -a0-a1
        for a in (a0, a1, a2):
            y = high_precision_step(y, a)
        return y


def fast_step(y, a):
    t = a/y
    r = (1+t+(1+6*t+t*t)**0.5)/2
    return y + 4*a + a*((r-1)**2)/r


def main():
    print('Leading cubic return coefficients:')
    for p in (1, -1):
        for theta in (pi/12, pi/6, pi/4):
            y0=Decimal(10000)
            yy=return_map(y0,p,theta)
            scaled = float((yy-y0)*y0*y0) / (p**3 * sin(3*theta))
            assert abs(scaled+3)<0.002, (p,theta,scaled)
            print(f'P={p:+d}, theta/pi={theta/pi:.6f}, coefficient={scaled:.9f}')
    print('Exact cancelling force triples:')
    for a in (Decimal('0.2'), Decimal('-0.7')):
        for aa in ((Decimal(0), a, -a), (a, Decimal(0), -a), (a,-a,Decimal(0))):
            y=Decimal(100)
            for v in aa: y=high_precision_step(y,v)
            assert abs(y-Decimal(100))<Decimal('1e-55'), (a,aa,y)
    print('Phase-grid cancellation: PASS')
    print('Sixth-root growth diagnostic:')
    p=-1.0; theta=0.1
    a0=p*sin(theta); a1=p*sin(theta+2*pi/3); a2=-a0-a1
    y=40.0; m=500000
    for _ in range(m):
        y=fast_step(fast_step(fast_step(y,a0),a1),a2)
    limit=-9*p**3*sin(3*theta)
    observed=y**3/m
    print(f'cycles={m}, y^3/cycles={observed:.7f}, predicted limit={limit:.7f}, ratio={observed/limit:.5f}')
    assert observed/limit>0.95 and observed/limit<1.12
    print('CHECKS_PASS')

if __name__=='__main__':main()
