"""Standalone checks of the finite-time separatrix boundary formulas.
Run: python check.py (requires sympy and mpmath).
Finite examples are diagnostics, not proofs of the asymptotic statements.
"""
import sympy as sp
from mpmath import mp
x,y,p,r = sp.symbols('x y p r',real=True,nonzero=True)
X=x-x*x*y+p*x*y*y+y**3
Y=y+p*y**3
assert sp.expand((X*y-x*Y)/y**2 - y**2*(1-(x/y)**2))==0
# Exact ratio dynamics, with x=yr.
assert sp.expand((X/y-r*Y/y-y*y*(1-r*r)).subs(x,r*y)) == 0
mp.dps=75

def flight(pval,y0,eps):
    k=(2+eps)/eps
    if pval==0:
        return mp.log(1+mp.log(k)/(y0*y0))/2
    return mp.log(1+(-mp.expm1(-pval*mp.log(k)))/(pval*y0*y0))/2

def fly_y(pval,y0,t):
    if pval==0:return y0*mp.exp(t)
    f=1-pval*y0*y0*mp.expm1(2*t)
    return y0*mp.exp(t)/mp.sqrt(f)

def energy(pval,y0,t):
    if pval==0:return y0*y0*mp.expm1(2*t)/2
    f=1-pval*y0*y0*mp.expm1(2*t)
    return -mp.log(f)/(2*pval)

for pp in (mp.mpf('-2.2'),mp.mpf('-0.25'),mp.mpf('0'),mp.mpf('0.4'),mp.mpf('1'),mp.mpf('2.5')):
    for yy in (mp.mpf('0.5'),mp.mpf('1.7')):
        for ee in (mp.mpf('0.03'),mp.mpf('0.000001')):
            t=flight(pp,yy,ee)
            k=(2+ee)/ee
            assert t>0
            assert abs(energy(pp,yy,t)-mp.log(k)/2)<mp.mpf('1e-48')
            if pp>0:
                t_y=mp.log(1+1/(pp*yy*yy))/2
                assert t<t_y
            yT=fly_y(pp,yy,t)
            yT_sq= yy*yy+mp.log(k) if pp==0 else (yy*yy+1/pp)*k**pp-1/pp
            assert abs(yT*yT-yT_sq)<mp.mpf('1e-45')*(1+abs(yT_sq))
            for dt in (min(mp.mpf('1e-10'), (t_y-t)*mp.mpf('1e-7')) if pp>0 else mp.mpf('1e-10'),):
                if dt>=t:continue
                tt=t-dt
                I=energy(pp,yy,tt)
                rtt=(1+k*mp.exp(-2*I))/(1-k*mp.exp(-2*I))
                xx=fly_y(pp,yy,tt)*rtt
                # approaching blow-up -x*y(T)*(T-t) -> 1
                assert abs(-xx*yT*dt-1)<mp.mpf('0.005')

# Three fixed-parameter singular regimes.
y0=mp.mpf('1.3'); ee=mp.mpf('1e-40'); lk=mp.log((2+ee)/ee)
for pp in (mp.mpf('-1.3'),mp.mpf('-0.3')):
    t=flight(pp,y0,ee)
    target=(-pp/2)*lk-mp.log((-pp)*y0*y0)/2
    assert abs(t-target)<mp.mpf('1e-10')
t=flight(mp.mpf(0),y0,ee)
assert abs(t-(mp.log(lk)/2-mp.log(y0)))<mp.mpf('0.012')
for pp in (mp.mpf('0.4'),mp.mpf('1'),mp.mpf('2.5')):
    ee_pos=mp.mpf('1e-18')
    t=flight(pp,y0,ee_pos)
    ty=mp.log(1+1/(pp*y0*y0))/2
    expected=mp.power(2,-pp-1)/(1+pp*y0*y0)
    assert abs((ty-t)/ee_pos**pp-expected)<mp.mpf('1e-7')

# Critical two-scale crossover for p*log(k) held fixed.
for delta in (mp.mpf('-3'),mp.mpf('0'),mp.mpf('2')):
    pp=delta/lk
    tau=flight(pp,y0,ee)
    kernel=-mp.expm1(-delta)/delta if delta!=0 else mp.mpf(1)
    asym=mp.log(lk)/2-mp.log(y0)+mp.log(kernel)/2
    assert abs(tau-asym)<mp.mpf('0.035')
print('CHECK_OK')
