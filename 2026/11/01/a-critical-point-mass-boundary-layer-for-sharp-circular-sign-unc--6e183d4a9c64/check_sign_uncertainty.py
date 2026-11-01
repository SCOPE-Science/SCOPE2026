"""Reproducibility checks for the sharp sign-change boundary layer.
Requires Python 3 with mpmath and sympy.
Finite checks corroborate formulas but do not replace the analytic proof.
"""
from fractions import Fraction
import math
import mpmath as mp

mp.mp.dps=50

def edge(m,tau):
    if tau == 0:
        return mp.pi/m
    a=mp.mpf(tau)/(1+m*mp.mpf(tau))
    def g(x):
        return mp.cos(x/2)-a*mp.cos(x/(2*m))/mp.sin(x/(2*m))*mp.sin(x/2)
    left=mp.mpf('1e-15')
    right=mp.pi
    for _ in range(210):
        mid=(left+right)/2
        if g(mid)>0:left=mid
        else:right=mid
    return (left+right)/(2*m)

for m in [2,3,5,11]:
    for tau in [Fraction(0), Fraction(1,7), Fraction(2,3)]:
        a=tau/(1+m*tau)
        # monic coefficients, low orders -a and top order 1
        co=[-a]*m+[Fraction(1)]
        # Haar Gram plus tau evaluation; all moments exact
        for k in range(m):
            ip=co[k] + tau*sum(co)
            assert ip==0,(m,tau,k,ip)

for c in ['0.2','1','5','25']:
    c=mp.mpf(c)
    eq=lambda x: mp.tan(x/2)/(x/2)-(1+1/c)
    lo=mp.mpf('1e-10');hi=mp.pi-mp.mpf('1e-10')
    for _ in range(200):
        md=(lo+hi)/2
        if eq(md)<0:lo=md
        else:hi=md
    limit=(lo+hi)/2
    for m in (250,1000,4000):
        x=m*edge(m,c/m)
        assert abs(x-limit)<mp.mpf('20')/m,(c,m,x,limit)

for tau in ['0.05','0.5','4']:
    tau=mp.mpf(tau)
    for m in (400,1500,5000):
        rho=edge(m,tau)/(2*mp.pi)
        ratio=m**(mp.mpf('1.5'))*mp.sqrt(tau)*rho/(mp.sqrt(3)/mp.pi)
        assert abs(ratio-1)<mp.mpf('10')/(m*tau),(m,tau,ratio)
print('CHECK_OK: rational OPUC Gram identities, critical-window roots, fixed-mass edge scaling')
