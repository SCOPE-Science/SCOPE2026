#!/usr/bin/env python3
"""Independent arithmetic checks for epoch-order comparison in the three-leaf coalescent.
All checks are finite diagnostics, not a substitute for the accompanying proof.
"""
from fractions import Fraction as Q
from math import exp, log
import itertools
import sympy as S

def pair_integral(rate, previous, length, alpha):
    return exp(-alpha*previous)*(-__import__('math').expm1(-alpha*rate*length))/(alpha*rate)

def full_components(prefix, low, high, lengths, tail, order):
    # Numerical quadrature performed separately on all four intervals.
    import mpmath as mp
    mp.mp.dps=45
    rates=[mp.mpf(prefix), mp.mpf(order[0]), mp.mpf(order[1]),mp.mpf(tail)]
    lengths=[mp.mpf(1),mp.mpf(lengths[0]),mp.mpf(lengths[1])]
    sums=[]
    for alpha in [mp.mpf(1),mp.mpf(3)]:
        accumulator=mp.mpf(0)
        integral=mp.mpf(0)
        for r,dt in zip(rates[:3],lengths):
            integral+=mp.quad(lambda s:mp.exp(-alpha*(accumulator+r*s)),[0,dt])
            accumulator+=r*dt
        integral+=mp.exp(-alpha*accumulator)/(alpha*rates[3])
        sums.append(integral)
    return tuple([mp.mpf('1.5')*(sums[0]+sums[1]),mp.mpf('1.5')*(sums[0]-sums[1])])

def main():
    u,v,X,Y=S.symbols('u v X Y',nonzero=True)
    D=(v-u)*(1-X)*(1-Y)/(u*v)
    fuv=(1-X)/u+X*(1-Y)/v
    fvu=(1-Y)/v+Y*(1-X)/u
    assert S.factor(fuv-fvu-D)==0
    fuv3=(1-X**3)/(3*u)+X**3*(1-Y**3)/(3*v)
    fvu3=(1-Y**3)/(3*v)+Y**3*(1-X**3)/(3*u)
    R=(1+X+X**2)*(1+Y+Y**2)/3
    assert S.factor(fuv3-fvu3-D*R)==0
    assert S.factor((S.Rational(3,2)*(fuv+fuv3-fvu-fvu3))-(S.Rational(3,2)*D*(1+R)))==0
    assert S.factor((S.Rational(3,2)*(fuv-fuv3-fvu+fvu3))-(S.Rational(3,2)*D*(1-R)))==0
    X0=Q(3,4); Y0=Q(1,2)
    D0=(Q(2)-Q(1))*(1-X0)*(1-Y0)/(Q(1)*Q(2))
    R0=(1+X0+X0**2)*(1+Y0+Y0**2)/3
    assert D0==Q(1,16)
    assert R0==Q(259,192)
    assert Q(1)<R0<Q(4)
    for x in [0,log(2)]:
        for uu,vv,l1,l2 in [(1.0,2.0,log(4/3),log(2)/2),(.5,2.7,.45,.20),(1.25,3.5,1.1,.75),(.2,1.7,.10,.90)]:
            from mpmath import mp
            mp.dps=45
            a=full_components(x,uu,vv,(l1,l2),1.3,(uu,vv))
            b=full_components(x,uu,vv,(l2,l1),1.3,(vv,uu))
            Xf=mp.exp(-uu*l1);Yf=mp.exp(-vv*l2)
            dd=(vv-uu)*(1-Xf)*(1-Yf)/(uu*vv)
            rr=(1+Xf+Xf**2)*(1+Yf+Yf**2)/3
            target=(mp.mpf(3)/2*dd*mp.exp(-3*x)*(mp.exp(2*x)+rr),mp.mpf(3)/2*dd*mp.exp(-3*x)*(mp.exp(2*x)-rr))
            for i in range(2):
                assert abs((a[i]-b[i])-target[i])<mp.mpf('1e-13'),(x,uu,vv,l1,l2,i)
    # Check positivity / strict sign regimes at rational endpoints and the unique duration cut.
    for uu,vv in [(1,2),(.5,4),(1.5,1.9)]:
        import mpmath as mp
        mp.mp.dps=45
        f=lambda L:(1+mp.exp(-uu*L)+mp.exp(-2*uu*L))*(1+mp.exp(-vv*L)+mp.exp(-2*vv*L))/3-1
        left,right=mp.mpf(0),mp.mpf(10)
        assert f(left)>0 and f(right)<0
        for _ in range(180):
            midpoint=(left+right)/2
            if f(midpoint)>0:left=midpoint
            else:right=midpoint
        root=(left+right)/2
        assert root>0 and f(root/2)>0 and f(root*2)<0
    print('PASS: 4 symbolic polynomial identities, 16 quadrature spectrum comparisons, 3 duration-root brackets, exact rational phase witness')

if __name__=='__main__':main()
