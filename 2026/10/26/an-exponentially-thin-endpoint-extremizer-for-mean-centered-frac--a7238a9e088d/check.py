#!/usr/bin/env python3
"""Reproducibility checks for the mean-centered fractional integral theorem.

Requires mpmath (pip install mpmath). The analytic proof, rather than these
finite numerical checks, establishes the theorem for all stated orders.
"""
import mpmath as mp

mp.mp.dps = 100

def root(a):
    a=mp.mpf(a)
    x0=a**(1/(1-a))
    h=lambda x: x**(1-a)*(1-x)**a
    # Root is unique in (0,x0), with h(x0)>a/2.
    lo,hi=mp.mpf('0'),x0
    for j in range(500):
        mid=(lo+hi)/2
        if h(mid)<a/2: lo=mid
        else: hi=mid
    return (lo+hi)/2

def row_norm(a,x):
    a,x=mp.mpf(a),mp.mpf(x)
    if x==0:
        return 1/(mp.gamma(a)*a*(a+1))
    x0=a**(1/(1-a))
    F=x**a/a-1/(a*(a+1))+2*(1-x)**(a+1)/(a*(a+1))
    if x<=x0: return F/mp.gamma(a)
    # Locate the additional sign crossing by bisection.
    lo,hi=mp.mpf(0),x
    for j in range(500):
        mid=(lo+hi)/2
        # logarithmic crossing equation avoids large fractional powers.
        sign=(1-a)*mp.log(x-mid)+a*mp.log(1-mid)-mp.log(a)
        if sign>0: lo=mid
        else: hi=mid
    t=(lo+hi)/2
    early_neg=(1-(1-t)**(a+1))/(a*(a+1))-(x**a-(x-t)**a)/a
    return (F+2*early_neg)/mp.gamma(a)

def direct_quadrature(a,x):
    a,x=mp.mpf(a),mp.mpf(x)
    if x==0: return mp.quad(lambda t:(1-t)**a/a,[0,1])/mp.gamma(a)
    x0=a**(1/(1-a))
    # Substitute s=x-t and integrate the singular part exactly on (0,x).
    # quadrature of |s^(a-1)-(1-x+s)^a/a| needs a near-zero split.
    f=lambda s:abs(s**(a-1)-(1-x+s)**a/a)
    # Gauss-Legendre adaptive integration near 0 using s=u^(1/a), and
    # factor u^(a-1) analytically to remove the endpoint singularity.
    p=lambda u:abs(1-(u**(1/a-1)/a)*(1-x+u**(1/a))**a)/a
    if x>x0:
        lo,hi=mp.mpf(0),x
        for _ in range(500):
            mid=(lo+hi)/2
            g=(1-a)*mp.log(x-mid)+a*mp.log(1-mid)-mp.log(a)
            if g>0:lo=mid
            else:hi=mid
        u_cross=(x-(lo+hi)/2)**a
        I1=mp.quad(p,[0,u_cross,x**a])
    else:
        I1=mp.quad(p,[0,x**a])
    I2=(1-x)**(a+1)/(a*(a+1))
    return (I1+I2)/mp.gamma(a)

assert abs(((3*mp.sqrt(6)+mp.sqrt(2)-4)/(3*mp.sqrt(mp.pi)))-mp.mpf('0.89568534008928865'))<mp.mpf('1e-17')
checks=0
for a_str in ['0.5','0.55','0.6','0.75','0.9','0.95','0.99']:
    a=mp.mpf(a_str);x0=a**(1/(1-a));x=root(a)
    assert 0<x<x0<1/mp.e
    assert abs(x**(1-a)*(1-x)**a-a/2)<mp.mpf('1e-65')
    checks+=2
    N=row_norm(a,x)
    assert N>row_norm(a,0) and N>row_norm(a,1)
    checks+=1
    for t in ['0.0','0.03','0.15','0.3','0.5','0.8','0.95','0.999','1.0']:
        at=mp.mpf(t)
        v=row_norm(a,at)
        assert v<=N+mp.mpf('1e-60'),(a_str,t,mp.nstr(v-N,12))
        checks+=1
    for t in [x/2, x, x0, (1+x0)/2,mp.mpf('0.99')]:
        if t>0:
            approx=direct_quadrature(a,t)
            err=abs(approx-row_norm(a,t))
            assert err<mp.mpf('1e-28'),(a,t,err)
            checks+=1
    print('alpha=',a_str,'x*=',mp.nstr(x,25),'sharp norm=',mp.nstr(N,25))

# Abel radical and extremal point.
x=root(mp.mpf('0.5'))
assert abs(x-(2-mp.sqrt(3))/4)<mp.mpf('1e-80');checks+=1
assert abs(row_norm(mp.mpf('0.5'),x)-(3*mp.sqrt(6)+mp.sqrt(2)-4)/(3*mp.sqrt(mp.pi)))<mp.mpf('1e-80');checks+=1

# This non-uniform boundary-layer limit is beyond all orders in epsilon.
for eps_s in ['0.05','0.03','0.02','0.01']:
    eps=mp.mpf(eps_s);a=1-eps;x=root(a)
    baseline=1/(mp.gamma(a+1)*(a+1))
    increment=row_norm(a,x)-baseline
    asymptotic=2*mp.e**(-1)*eps*2**(-1/eps)
    ratio=increment/asymptotic
    assert abs(ratio-1)<mp.mpf('0.055'),(eps_s,ratio)
    checks+=1
    print('epsilon=',eps_s,'increment=',mp.nstr(increment,22),'asymptotic ratio=',mp.nstr(ratio,16))
print('PASS:',checks,'independent mathematical/numerical assertions; no infinite-range certification implied')
