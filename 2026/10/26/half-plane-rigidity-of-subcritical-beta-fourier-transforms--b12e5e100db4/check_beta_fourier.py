#!/usr/bin/env python3
"""Numerical checks for the centered beta Fourier transform and Bessel zero drift.

Requires mpmath. Finite tests are diagnostic and do not prove global results.
"""
import mpmath as mp

mp.mp.dps=55


def f(s,a,t):
    return mp.hyp1f1(a,s,1j*t)


def g(s,a,t):
    return mp.exp(-1j*t/2)*f(s,a,t)


def gp(s,a,t):
    return mp.exp(-1j*t/2)*(1j*a/s*mp.hyp1f1(a+1,s+1,1j*t)-0.5j*f(s,a,t))


def Jroot(s,n):
    nu=(s-1)/2
    # Initial approximation for the nth positive Bessel root.
    guess=(n + nu/2 - mp.mpf('0.25'))*mp.pi
    j=mp.findroot(lambda x:mp.besselj(nu,x), (guess-mp.mpf('0.2'),guess+mp.mpf('0.2')))
    assert j>0
    return 2*j


def drift_formula(s,T):
    nu=(s-1)/2
    jprime=mp.diff(lambda x:mp.besselj(nu,x),T/2)
    numerator=mp.quad(lambda r:mp.besselj(nu,r/2)**2,[0,T])
    return 4*numerator/(T*jprime*jprime)


def check(s,a):
    d=a-s/2
    for T in (mp.mpf('0.15'),mp.mpf('1'),mp.mpf('3.2'),mp.mpf('8.7'),mp.mpf('19.5')):
        G=g(s,a,T)
        left=mp.im(gp(s,a,T)/G)
        I=mp.quad(lambda r:r**(s-1)*abs(g(s,a,r))**2,[0,T])
        right=d*I/(T**s*abs(G)**2)
        assert mp.almosteq(left,right,rel_eps=mp.mpf('1e-35'),abs_eps=mp.mpf('1e-35')), (s,a,T,left,right)
        assert d*left>0, (s,a,T,left)
    return str(s),str(a)


print('centered Wronskian/phase identity:')
for s in map(mp.mpf,['0.6','1.0','1.6','1.9']):
    for fraction in map(mp.mpf,['0.15','0.3','0.73','0.9']):
        print('  PASS', check(s,s*fraction))

print('symmetric Bessel zeros and parameter drift:')
for s in map(mp.mpf,['0.6','1.0','1.6','1.9']):
    a0=s/2
    for n in (1,2,3,5):
        T=Jroot(s,n)
        zero=f(s,a0,T)
        assert abs(zero)<mp.mpf('1e-40')
        z=1j*T
        implicit=-mp.diff(lambda a:mp.hyp1f1(a,s,z),a0)/(a0/s*mp.hyp1f1(a0+1,s+1,z))
        predicted=-drift_formula(s,T)
        assert abs(implicit-predicted)<mp.mpf('1e-30'), (s,n,implicit,predicted)
        assert mp.re(implicit)<0 and abs(mp.im(implicit))<mp.mpf('1e-30')
        if n in (1,5):
            a=a0+mp.mpf('0.000002')
            root=mp.findroot(lambda z:mp.hyp1f1(a,s,z),(1j*T+mp.mpf('0.000002')*predicted,1j*T+mp.mpf('0.000002')*predicted+mp.mpf('0.000001')))
            deviation=abs((mp.re(root)/(a-a0))-predicted)
            assert deviation<mp.mpf('0.003'),(s,n,deviation)
    print('  PASS s=',mp.nstr(s,6),'four zeros')

print('drift logarithmic asymptotic:')
for s in map(mp.mpf,['0.6','1.0','1.9']):
    ds=[]
    for n in (10,20,40):
        T=Jroot(s,n)
        ds.append(mp.nstr(drift_formula(s,T)-2*mp.log(n),12))
    print('  s=',mp.nstr(s,5),' A_n-2log(n) for n=10,20,40:',','.join(ds))

print('PASS: all numerical identity checks (not an all-parameter proof)')
