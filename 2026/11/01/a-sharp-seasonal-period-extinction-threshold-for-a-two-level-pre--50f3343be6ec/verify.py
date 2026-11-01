#!/usr/bin/env python3
"""Independent checks of two-season logistic residence and invasion identities.
Uses only the Python standard library. Numerical tests are not proofs.
"""
import math

def stats(high, low, period):
    assert 0 < low < high and period > 0
    d = high - low
    contrast = d / (high + low)
    g = math.atanh(contrast * math.tanh(period / 4))
    mean = (high + low) / 2 - 2*d*g/period
    q = math.exp(-period/2)
    inverse_start = (1/low + q/ high) / (1+q)
    inverse_mid = (1/high + q/low) / (1+q)
    return mean, inverse_start, inverse_mid

def prey_area(high, low, period, count=12000):
    _, y0, ym = stats(high, low, period)
    half=period/2
    def integrand(t):
        if t<half:
            return 1.0/(1/high+(y0-1/high)*math.exp(-t))
        return 1.0/(1/low+(ym-1/low)*math.exp(-(t-half)))
    # Split at discontinuity, Simpson rule on smooth half segments.
    def simp(a, b):
        h=(b-a)/count
        z=integrand(a)+integrand(math.nextafter(b,a))
        for j in range(1,count):
            x=a+j*h
            z+=(4 if j%2 else 2)*integrand(x)
        return z*h/3
    return (simp(0,half)+simp(half,period))/period

def brent_bisection(high,low, target=1):
    l=1e-5; r=1.0
    while stats(high,low,r)[0]<target: r*=2
    for _ in range(85):
        t=(l+r)/2
        if stats(high,low,t)[0]<target: l=t
        else: r=t
    return (l+r)/2

if __name__=='__main__':
    cnt=0
    for high,low in [(2,.5),(3,.6),(5,2),(1.3,.1),(10,.01),(.8,.2)]:
        means=[]
        for T in [.05,.1,.2,.4,1.,2.,4.,8.,16.,32.]:
            mean,y0,ym=stats(high,low,T)
            integral=prey_area(high,low,T,192000 if low/high<0.01 and T>=16 else 12000)
            assert abs(integral-mean)<2e-9, (high, low,T,integral,mean)
            assert abs((1/low+(ym-1/low)*math.exp(-T/2))-y0)<5e-13
            assert 2*high*low/(high+low)<mean<(high+low)/2
            means.append(mean)
            cnt+=1
        assert all(v>u for u,v in zip(means,means[1:])), (high,low,means)
    high,low=2.,.5
    root=brent_bisection(high,low)
    assert 7.90<root<7.91
    assert abs(stats(high,low,root)[0]-1)<4e-15
    assert stats(high,low,root/2)[0]<1<stats(high,low,root*2)[0]
    # Independent quadrature of the scalar transverse variational exponent.
    for high,low,T in [(2.,.5,5.),(2.,.5,12.),(3.,.6,8.)]:
        exact=stats(high,low,T)[0]
        numeric=prey_area(high,low,T)
        for lam in (.25,1.,2.):
            rho_num=math.exp(lam*T*(numeric-1.))
            rho_exact=math.exp(lam*T*(exact-1.))
            assert abs(rho_num/rho_exact-1)<1e-10
    print('PASS: smooth-segment quadrature vs exact formulas, positivity, periodicity, monotonic samples:',cnt)
    print('PASS: unique transverse invasion threshold example K_hi=2,K_lo=0.5: T*=%.12f'%root)
    print('PASS: independently integrated transverse linear exponent agrees with Floquet expression')
