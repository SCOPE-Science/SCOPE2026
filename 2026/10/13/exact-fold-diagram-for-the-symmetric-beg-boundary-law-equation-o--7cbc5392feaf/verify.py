#!/usr/bin/env python3
from fractions import Fraction
import math

def poly(k,c1,c2,s):
    return c1*s**(k+1)-c2*s**k+s-1.0

def q(k,c1,s):
    return c1*s+(s-1.0)/s**k

def H(k,c1,s):
    return c1*s**(k+1)-(k-1)*s+k

def bisect_root(fun,a,b,it=100):
    fa,fb=fun(a),fun(b)
    assert fa*fb <= 0, (a,b,fa,fb)
    for _ in range(it):
        m=(a+b)/2.0
        fm=fun(m)
        if fa*fm <= 0:
            b,fb=m,fm
        else:
            a,fa=m,fm
    return (a+b)/2.0

# Exact cusp identities.
for k in range(2,21):
    rho=Fraction(k-1,k+1)
    s=1/rho
    c1=rho**(k+1)
    c2=rho**(k-1)
    P=c1*s**(k+1)-c2*s**k+s-1
    P1=(k+1)*c1*s**k-k*c2*s**(k-1)+1
    P2=k*(k+1)*c1*s**(k-1)-k*(k-1)*c2*s**(k-2)
    P3=k*(k-1)*(k+1)*c1*s**(k-2)-k*(k-1)*(k-2)*c2*s**(k-3)
    assert P == 0 and P1 == 0 and P2 == 0
    assert P3 == k*(k-1)*rho*rho and P3 > 0

# Representative subcritical fold geometry and actual root counts.
for k in (2,3,4,6,10):
    rho=(k-1)/(k+1)
    crit=rho**(k+1)
    c1=0.5*crit
    smid=(k+1)/(k-1)
    left0=k/(k-1)
    sminus=bisect_root(lambda s:H(k,c1,s), left0, smid)
    hi=smid
    while H(k,c1,hi) <= 0:
        hi*=2
    splus=bisect_root(lambda s:H(k,c1,s), smid, hi)
    c2hi=q(k,c1,sminus)
    c2lo=q(k,c1,splus)
    assert 0 < c2lo < c2hi
    # Interior level: one crossing in each monotonicity interval.
    c2=(c2lo+c2hi)/2
    eps=1e-10
    r1=bisect_root(lambda s:q(k,c1,s)-c2, eps, sminus)
    r2=bisect_root(lambda s:q(k,c1,s)-c2, sminus, splus)
    upper=splus*2
    while q(k,c1,upper) < c2:
        upper*=2
    r3=bisect_root(lambda s:q(k,c1,s)-c2, splus, upper)
    roots=[r1,r2,r3]
    assert roots[0] < roots[1] < roots[2]
    assert max(abs(poly(k,c1,c2,r)) for r in roots) < 2e-7
    # Outside levels: monotonicity leaves only one crossing.
    for c2out in (0.5*c2lo, 1.5*c2hi):
        # Count sign-changing brackets on a dense logarithmic grid only as a corroborative check.
        grid=[10**(-6 + 12*i/20000) for i in range(20001)]
        vals=[poly(k,c1,c2out,x) for x in grid]
        changes=sum(1 for a,b in zip(vals,vals[1:]) if a==0 or a*b<0)
        assert changes == 1, (k,c2out,changes)
    # Physical coefficient reconstruction at xi=2.
    xi=2.0
    b=math.log(c1/2.0,xi)
    a=1-b+math.log(c2/(1+xi*xi),xi)
    assert abs(2*xi**b-c1) < 1e-12
    assert abs(xi**(a+b-1)*(1+xi*xi)-c2) < 1e-12

print('VERIFY_OK cusp_orders=2..20 fold_orders=2,3,4,6,10')
