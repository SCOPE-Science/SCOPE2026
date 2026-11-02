#!/usr/bin/env python3
"""Deterministic finite checks for the linear delayed-diffusion critical kernel.
Requires only the Python standard library. These diagnostics do not prove the theorem.
"""
from decimal import Decimal, localcontext
from math import factorial

D = Decimal
count = 0

def check(condition, msg):
    global count
    if not condition:
        raise AssertionError(msg)
    count += 1

def response(t, tau):
    """Method-of-steps exact formula for a = 1/tau, zero history."""
    t, tau = D(str(t)), D(str(tau))
    a = 1 / tau
    n = int(t // tau)
    total = D(0)
    for k in range(n + 1):
        q = t - k*tau
        total += (-a)**k * (q**k if k>0 else D(1)) / D(factorial(k)) * (a*q).exp()
    return total

def de(t, tau):
    t, tau = D(str(t)), D(str(tau))
    a = 1/tau
    n = int(t // tau)
    total = D(0)
    for k in range(n+1):
        q = t - k*tau
        base = (-a)**k / D(factorial(k)) * (a*q).exp()
        deriv = a*(q**k if k>0 else D(1)) + (D(k)*(q**(k-1) if k>1 else D(1)) if k>0 and (q>0 or k==1) else D(0))
        total += base*deriv
    return total

def trap_var(t, tau, Dvalue=Decimal(1), panels=400):
    t, tau = D(str(t)), D(str(tau))
    h=t/D(panels)
    s=(response(0,tau)**2+response(t,tau)**2)/2
    for i in range(1,panels):
        v=response(i*h,tau)
        s+=v*v
    return 2*Dvalue*h*s

with localcontext() as ctx:
    ctx.prec=72
    for tau in [D('0.7'), D('1'), D('1.6')]:
        for i in range(0, 49):
            t=tau*D(i)/4
            r=response(t,tau)
            lo=2*t/tau
            check(r+ D('1e-40') >=lo, f'lower {tau} {t} {r}')
            check(r<=lo+1+D('1e-40'), f'upper {tau} {t} {r}')
            if i>=1 and i%4!=0:
                lag=response(t-tau,tau) if t>=tau else D(0)
                derr=de(t,tau)-(r-lag)/tau
                check(abs(derr)<D('1e-20'),f'DDE {tau} {t} {derr}')
    check(response(0,1)==1,'sharpness')
    for t in [D('1'), D('3'), D('6')]:
        v=trap_var(t,D(1),panels=300)
        low=D(8)*t**3/3
        high=low+4*t**2+2*t
        check(low<v<high,f'variance bracket t={t}, variance={v}')
        print('t=',t,' variance=',str(v)[:22], ' lower=',str(low)[:22], ' upper=',str(high)[:22])
    for t in [D('8'), D('12')]:
        measured=trap_var(t,D(1),panels=250)
        correction=(measured-D(8)*t**3/3)/t**2
        check(abs(correction-D(8)/3)<D('0.15'),f'subleading variance {t}: {correction}')
    for t in [D('1'),D('5'),D('10'),D('12')]:
        r=response(t,1)
        print('critical response',t,str(r)[:28], 'offset',str(r-2*t)[:28])
    print('PASS:',count,'deterministic assertions; analytical inequalities and path limit require proof.')
