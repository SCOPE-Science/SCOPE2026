"""Exact first-order one-birth checks for an age-dependent branching process.

All arithmetic is rational. The analytic proof establishes the all-law result;
this program checks independent finite-support specializations and identities.
"""
from fractions import Fraction as F
from itertools import product


def contribution(q, z):
    # Integral over one potential birth time u in [0,q].
    # J(q,z) = integral_0^q max(0,u+z-q) du.
    j = z*z/F(2) if z <= q else q*z-q*q/F(2)
    # Direct N=0 vs N=1 small-rate coefficient for E[T], E[S], E[TS].
    return (j, q*z, q*q*z+(q+z)*j)


def verify(law):
    assert sum((p for q,p in law), F(0)) == 1
    assert sum((q*p for q,p in law), F(0)) == 1
    m2 = sum((q*q*p for q,p in law), F(0))
    dt=ds=dts=F(0)
    for (q,p),(z,w) in product(law,repeat=2):
        j1=contribution(q,z)[0]
        j2=contribution(z,q)[0]
        assert j1+j2 == q*z
        t,s,ts=contribution(q,z)
        dt+=p*w*t
        ds+=p*w*s
        dts+=p*w*ts
    d_cov=dts-dt-ds
    assert dt == F(1,2), (law,dt)
    assert ds == F(1), (law,ds)
    assert dts == 2*m2, (law,dts)
    assert d_cov == F(1,2)+2*(m2-1)
    return m2-1,d_cov


if __name__ == '__main__':
    laws = [
        [(F(1), F(1))],
        [(F(1,2),F(1,2)),(F(3,2),F(1,2))],
        [(F(1,4),F(1,4)),(F(1),F(1,2)),(F(7,4),F(1,4))],
        [(F(1,5),F(1,3)),(F(7,5),F(2,3))],
    ]
    for law in laws:
        variance, slope=verify(law)
        print('law=',law,'variance=',variance,'covariance_slope=',slope)
    print('PASS: all finite-support checks match the theorem exactly.')
