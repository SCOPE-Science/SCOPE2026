#!/usr/bin/env python3
"""Standalone finite algebra checks for the geometric-emigration branching theorem.
These checks support, but do not replace, the infinite-state proof.
"""
from fractions import Fraction as Q
import math

checks = 0

def same(x,y,msg):
    global checks
    if x != y:
        raise AssertionError(f'{msg}: {x} != {y}')
    checks += 1

# Conditional PGF, geometric-emigration truncation, and moment identities.
for p in (Q(3,5), Q(2,3), Q(3,4), Q(4,5)):
    a=p/(1-p)
    for y in range(19):
        m_mean=sum((1-p)*p**k*(y+1-k) for k in range(y+1))
        same(m_mean,Q(y+1)-a + p**(y+2)/(1-p),f'mean {p},{y}')
        for s in (Q(0), Q(1,4), Q(2,5), Q(3,4), Q(9,10)):
            F=1/(2-s)
            if F==p: continue
            # Exact sum over all emigration possibilities.
            lhs=sum((1-p)*p**k*F**(y+1-k) for k in range(y+1))+p**(y+1)
            rhs=(1-p)*F**2/(F-p)*F**y + p**2*(F-1)/(F-p)*p**y
            same(lhs,rhs,f'conditional PGF {p},{y},{s}')

# The stationary anchor identity and resulting exact rational recurrence.
for a in (Q(6,5),Q(3,2),Q(2),Q(3),Q(5)):
    p=a/(a+1)
    Hp=1-Q(1)/a**2
    same(p*a*Hp,a-1,'stationary anchor')
    u=a+1
    g=1/a**2
    for n in range(90):
        g_next=1/u**2 + (u+1)*(u-a)/u**2*g
        H=1-g
        H_next=1-g_next
        original=u**2/((u+1)*(u-a))*H_next -p*a/(u-a)*Hp
        same(H,original,f'stationary functional recurrence {a},{n}')
        u+=1
        g=g_next

# At the critical parameter, the discrete PGF is an exact harmonic-number expression.
u=Q(3); g=Q(1,4)
for n in range(90):
    harmonic=sum((Q(1,j) for j in range(1,n+3)),Q(0))
    expected=u/((u-1)*(u-2))*(harmonic+Q(2)/u-2)
    same(g,expected,f'critical harmonic identity {n}')
    g=1/u**2+(u+1)*(u-2)/u**2*g
    u+=1

# The gamma constants follow the beta-integral computation in the proof.
try:
    import mpmath as mp
    mp.mp.dps=40
    for a_str in ('1.25','1.5','1.75'):
        a=mp.mpf(a_str)
        h0=mp.gamma(a)/(a*(a+1))
        integral=mp.gamma(a)*(mp.beta(a,2-a)-mp.beta(a,2))
        C=h0+integral
        target=mp.gamma(a)**2*mp.gamma(2-a)
        assert mp.almosteq(C,target,rel_eps=mp.mpf('1e-35'))
        checks+=1
    for a_str in ('1.25','1.5'):
        a=float(a_str); u=a+1; g=1/a**2
        for k in range(100000):
            g=1/u**2+(u+1)*(u-a)/u**2*g
            u+=1
        C=math.gamma(a)**2*math.gamma(2-a)
        assert abs(g*u**(a-1)/C-1)<.07
        checks+=1
    for a in (2.,3.,4.):
        u=a+1; g=1/a**2
        for k in range(100000):
            g=1/u**2+(u+1)*(u-a)/u**2*g
            u+=1
        observed=u*g
        if a==2:
            target=math.log(u)+float(mp.euler)-2
            assert abs(observed-target)<.003, (a,observed,target)
        else:
            target=1/(a-2)
            assert abs(observed/target-1)<.06, (a,observed,target)
        checks+=1
except ImportError:
    print('mpmath unavailable: gamma-constant numerical checks not run')
print(f'PASS: {checks} exact and numerical assertions; no infinite theorem is certified by this finite run')
