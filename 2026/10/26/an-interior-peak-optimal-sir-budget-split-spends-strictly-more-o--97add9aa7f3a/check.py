#!/usr/bin/env python3
"""Independent arithmetic and numerical checks for the two-objective SIR allocation theorem.
Numerical sampling illustrates, but does not prove, global inequalities."""
from fractions import Fraction as F
from math import exp, log, isclose
from scipy.optimize import brentq
from scipy.integrate import solve_ivp

checks = 0

def ck(ok, note='check'):
    global checks
    assert ok, note
    checks += 1

# Symbolic rational margins in the analytic high-transmission example.
s0,i0,beta0,gamma0,B,G=F(9,10),F(1,10),F(30),F(1),F(1),F(1)
rmin=F(40,3)
rmax=F(15)
ck(rmin==beta0/F(9,4))
ck(rmax==beta0/F(2))
# e^(4/3) > 1 + 4/3 > 2, so e^(-4/3) < 1/2
ck(1+F(4,3)>2)
# e^(22/3) > sum_{j=0}^3 (22/3)^j/j! > 81/2.
x=F(22,3)
partial=sum((x**j)/F(__import__('math').factorial(j)) for j in range(4))
ck(partial>F(81,2))
# Therefore y=R*S_infinity < (15*9/10)*e^(-22/3) < 1/3.
ck(F(15)*s0 / F(81,2) <= F(1,3))
# Universal signs: g>=1/2, h<=1, hence g-y*h>1/6.
ck(F(1,2)-F(1,3)>0)

# Two fully independent final-size calculations: brent root and Lambert W.
import mpmath as mp
mp.mp.dps=40

def final(R, S, I):
    M=S+I
    f=lambda z: z-S*exp(-R*(M-z))
    return brentq(f,0,S,xtol=1e-15)

def final_w(R,S,I):
    M=mp.mpf(str(S+I))
    y=-mp.mpf(str(R))*mp.mpf(str(S))*mp.exp(-mp.mpf(str(R))*M)
    return float(-mp.lambertw(y,0)/mp.mpf(str(R)))

for v in [j/100 for j in range(101)]:
    gamma=2-v
    R=30/((1+v)*gamma)
    s=final(R,.9,.1)
    A=1-s
    y=R*s
    h=1/(1+v)
    g=1/(2-v)
    ck(0<s<.9)
    ck(y<1)
    ck(abs(s-final_w(R,.9,.1))<1e-12,'Lambert W crosscheck')
    ck(g-y*h>0,'analytic sign')
    Q=A/gamma
    # numeric derivative of Q follows the claimed analytic expression
    eps=1e-5
    if eps<v<1-eps:
        def q(z):
            r=30/((1+z)*(2-z))
            return (1-final(r,.9,.1))/(2-z)
        centered=(q(v+eps)-q(v-eps))/(2*eps)
        rhs=Q*(g-y*h)/(1-y)
        ck(abs(centered-rhs)<2e-8,'analytic derivative')

q0=(1-final(15,.9,.1))/2
qh=(1-final(F(40,3),.9,.1))/1.5
ck(q0 < qh)
ck(.4999<q0<.5001)
ck(.6666<qh<.6667)
# Source peak formula: monotone in R when S0*R>1.
def peak(r): return 1-(1+log(.9*r))/r
ck(peak(40/3)<peak(15))

# Solve the dynamical ODE independently, verify integral I dt vs final-size A/gamma.
for u in [0,.5,1]:
    beta=30/(1+u)
    gamma=2-u
    def ode(t,x):
        S,I,C=x
        return [-beta*S*I,beta*S*I-gamma*I,I]
    ans=solve_ivp(ode,(0,65),[.9,.1,0],rtol=3e-11,atol=3e-12,method='DOP853')
    ck(ans.success)
    s=final(beta/gamma,.9,.1)
    ck(abs(ans.y[0,-1]-s)<1e-8)
    ck(abs(ans.y[2,-1]-(1-s)/gamma)<1e-8)

print('CERTIFICATE_OK',checks,'checks')
print('q0=',q0,'qhalf=',qh,'peak0=',peak(15),'peakhalf=',peak(40/3))
