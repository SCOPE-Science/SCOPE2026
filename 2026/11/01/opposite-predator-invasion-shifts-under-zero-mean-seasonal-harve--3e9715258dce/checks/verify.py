"""Finite reproducible sanity checks of a seasonal predator-invasion comparison.
The finite checks supplement, but never replace, the analytical theorem.
"""
from math import pi, cos, sin, exp
from fractions import Fraction as F
import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp

x=sp.symbols('x',real=True)
for a,b in [(sp.Rational(11,10),-2),(1,0)]:
    den=a*x*x+b*x+1
    p=x*x/den
    p1=sp.diff(p,x)
    p2=sp.factor(sp.diff(p,x,2))
    v=[sp.simplify(f.subs(x,sp.Rational(3,2))) for f in (p,p1)]
    print('symbolic a,b, p(X),pprime(X):',a,b,v,'psecond:',p2)
assert F(7,5)*(1-F(7,5)/2)-F(3,8)==F(9,200)>F(1,25)
assert F(3,8)-F(8,5)*(1-F(8,5)/2)==F(11,200)>F(1,25)

def periodic(nharm):
    T=2*pi
    def sig(t):
        if nharm==1:return .03*cos(t)
        if nharm==2:return .02*(cos(t)+.5*sin(2*t))
        return .01*(sin(3*t)+sin(5*t)+sin(7*t))
    def fun(t,Y):return [Y[0]*(1-Y[0]/2)-.375-sig(t)]
    v=1.5
    for _ in range(45):
        v=float(solve_ivp(fun,(0,T),[v],rtol=4e-12,atol=3e-13).y[0,-1])
    ts=np.linspace(0,T,30001)
    sol=solve_ivp(fun,(0,T),[v],rtol=4e-12,atol=3e-13,dense_output=True)
    xx=sol.sol(ts)[0]
    avg=lambda y:np.trapezoid(y,ts)/T
    m=avg(xx); var=avg((xx-m)**2); delta=1.5-m
    assert xx.min()>1.4 and xx.max()<1.6
    assert abs(var - delta*(1-delta))<2e-9
    pg=xx**2/(1.1*xx**2-2*xx+1)
    pm=xx**2/(xx**2+1)
    gain=avg(pg)-90/19
    loss=avg(pm)-9/13
    assert gain>(2400/361)*var
    assert loss<-(48/169)*var
    print(f'forcing={nharm}: x-min={xx.min():.11f}, x-max={xx.max():.11f}, mean={m:.11f}, variance={var:.11g}, group-defense log Floquet/T={gain:.11g}, monotone log Floquet/T={loss:.11g}')
for k in (1,2,3):periodic(k)
print('All finite verification checks passed.')
