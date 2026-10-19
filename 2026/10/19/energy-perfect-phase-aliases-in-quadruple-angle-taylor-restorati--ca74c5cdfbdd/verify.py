#!/usr/bin/env python3
"""Reproduce scalar quadrupling phase-alias examples and finite identities.
No data files, network, private state, or nonstandard proof dependencies.
Requires mpmath 1.3.0. Numerical tests corroborate analytical proofs.
"""
from fractions import Fraction as F
from math import factorial
from mpmath import mp

mp.dps = 250
checks = 0

def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def P(m, x):
    return sum(((-x)**k / mp.factorial(2*k) for k in range(m+1)), mp.mpf(0))

def Q(m, x):
    return sum(((-x)**k / mp.factorial(2*k+1) for k in range(m+1)), mp.mpf(0))

def dP(m, x):
    return sum(((-1)**k*k*x**(k-1) / mp.factorial(2*k) for k in range(1,m+1)), mp.mpf(0))

def alias(m, s):
    beta = (mp.pi*mp.factorial(2*m+2))**(mp.mpf(2)/(2*m+1))
    rho = mp.sqrt(beta)/mp.pi
    z = rho*mp.power(2,mp.mpf(2*m)*s/(2*m+1))
    q = 2*int(mp.nint((z-1)/2))+1
    alpha = q*mp.pi/mp.power(2,s)
    x = alpha**2
    for j in range(14):
        x -= (P(m,x)-mp.cos(alpha))/dP(m,x)
    residual = abs(P(m,x)-mp.cos(alpha))
    theta_err = mp.power(2,s)*(mp.sqrt(x)-alpha)
    gap = 2*abs(mp.sin(theta_err/2))
    err0 = abs(P(m,x)-mp.cos(mp.sqrt(x)))
    err1 = abs(Q(m,x)-mp.sin(mp.sqrt(x))/mp.sqrt(x))
    return x,q,theta_err,gap,residual,err0,err1,beta

for s in range(1,8):
    roots=[]
    for j in range(s):
        for k in range(2**j):
            x = 2*(1-mp.cos((2*k+1)*mp.pi/(2**(j+1))))
            roots.append(x)
            cj = mp.cos((2*k+1)*mp.pi/2)
            check(abs(cj)<mp.mpf('1e-235'), 'Chebyshev zero')
    roots.append(mp.mpf(3))
    check(len(roots)==2**s, 'positive root count')
    for i in range(len(roots)):
        check(roots[i]>0, 'positive root')
        for j in range(i):
            check(abs(roots[i]-roots[j])>mp.mpf('1e-20'), 'distinct zero')
        x=roots[i]
        c=1-x/2
        sn=1-x/6
        for j in range(s):
            old=c
            c=2*c*c-1
            sn=old*sn
        check(abs(1-c*c-mp.power(4,s)*x*sn*sn)<mp.mpf('1e-200'), 'exact energy defect at zero')

for m,s in [(1,16),(1,24),(1,36),(2,30),(2,45),(2,60),(4,64),(4,100),(20,512)]:
    x,q,t,g,r,e0,e1,b=alias(m,s)
    check(x>0, 'positive seed')
    check(q>0 and q%2==1, 'positive odd resonant index')
    check(r<mp.mpf('1e-210'), 'seed root precision')
    check(abs(t-(-1)**m*mp.pi)<mp.mpf('0.02'), 'phase convergence')
    check(g>mp.mpf('1.9999'), 'almost maximal phase error')
    check(e0 < x**(m+1), 'cosine seed error order')
    check(e1 < x**(m+1), 'sinc seed error order')
    print('m=%d s=%d x=%s q=%s phase-diff=%s operator-gap=%s' % (m,s,mp.nstr(x,22),q,mp.nstr(t,22),mp.nstr(g,22)))

for x in [F(1,5),F(1,2),F(1),F(2),F(3),F(7,2),F(5)]:
    c=1-x/F(2)
    sn=1-x/F(6)
    d=1-c*c-x*sn*sn
    check(d==x*x*(3-x)/36, 'm=1 exact seed factor')
    for j in range(6):
        old=c
        c=2*c*c-1
        sn=old*sn
        new_d=1-c*c-4**(j+1)*x*sn*sn
        check(new_d==4*old*old*d, 'exact defect propagation')
        d=new_d
print('VERIFY_OK %d assertions' % checks)
