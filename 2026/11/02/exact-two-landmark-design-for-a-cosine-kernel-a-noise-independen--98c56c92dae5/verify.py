"""Independent numerical and rational checks for the two-landmark cosine-kernel design."""
from fractions import Fraction as F
from math import acos, cos, pi, sin, sqrt, isclose
import random

N=0

def check(condition, message):
    global N
    N+=1
    if not condition:
        raise AssertionError(message)

def formula(a,t,u):
    return a+1-(2*a*a+u)/(t+2*a+2*u)-(1-u)/(t+2-2*u)

def closed_optimum(a,t):
    C=t+2*a*(1-2*a)
    if C<=0:
        return 0.0
    u=((t+2)*sqrt(C)-(t+2*a)*sqrt(t))/(2*(sqrt(C)+sqrt(t)))
    return max(0.0,u)

def root_threshold(t):
    return (-t*t+4*t+4+(t+2)*sqrt(17*t*t+20*t+4))/(4*(t*t+5*t+4))

# Independently compute posterior variance using the 2-by-2 inverse and a midpoint integral.
def direct(a,t,theta,steps=256):
    z0=-theta/2
    z1=theta/2
    diag=a+1+t
    off=a+cos(theta)
    det=diag*diag-off*off
    def variance(x):
        p=a+cos(x-z0)
        q=a+cos(x-z1)
        return a+1-(diag*(p*p+q*q)-2*off*p*q)/det
    return sum(variance(2*pi*(j+.5)/steps) for j in range(steps))/steps

rnd=random.Random(731)
for _ in range(240):
    a=10**rnd.uniform(-2,1)
    t=10**rnd.uniform(-3,2)
    theta=rnd.uniform(0,pi)
    u=cos(theta/2)**2
    check(abs(formula(a,t,u)-direct(a,t,theta))<1e-10, 'direct Gram / trig integral mismatch')

# Exact rational calculations on independently expanded Gram matrix in symmetric coordinates.
for numerator in range(1,13):
    for ti in range(1,11):
        for ui in range(0,11):
            a=F(numerator,11)
            t=F(ti,13)
            u=F(ui,10)
            symmetric_signal=2*a*a+u
            antisymmetric_signal=1-u
            lam_plus=t+2*a+2*u
            lam_minus=t+2-2*u
            independently=a+1-symmetric_signal/lam_plus-antisymmetric_signal/lam_minus
            check(independently==formula(a,t,u), 'rational spectral decomposition mismatch')

for a in (0.02,0.10,0.20,0.49,0.50,0.51,0.70,0.90,1.2,3.0):
    for t in (0.001,0.01,0.1,1.0,10.0,100.0):
        optimum=closed_optimum(a,t)
        crt=root_threshold(t)
        check((optimum>1e-12)==(a<crt), 'threshold phase classification mismatch')
        check(optimum<=1, 'outside optimum domain')
        v0=formula(a,t,optimum)
        for j in range(101):
            check(v0<=formula(a,t,j/100)+1e-10, 'not global minimum')

for t in (1e-8,0.001,0.02,0.5,1,1000):
    check(abs(closed_optimum(0.5,t)-0.25)<2e-12,'120 degree law fails')

for a in (0.05,0.2,0.45):
    c0=2*a*(1-2*a)
    constant=2*sqrt((a+1)/sqrt(c0))
    for t in (1e-8,1e-10,1e-12):
        u=closed_optimum(a,t)
        theta=2*acos(sqrt(u))
        check(abs(theta/(t**0.25)-constant)/constant<0.002,'quarter power coefficient wrong')

for a in (F(1,5),F(1,2),F(4,5)):
    for ui in (0,F(1,4),F(1,2),F(9,10)):
        check(formula(a,F(0),ui)==a*(2*ui+1)/(2*(a+ui)),'noiseless formula wrong')
    collision=a+1-(a*a+F(1,2))/(a+1)
    limit=a*F(3,2)/(a+1)
    check(collision-limit==F(1,2),'pseudoinverse collision jump wrong')

print('PASS:',N,'assertions; direct Gram integration, rational spectral identity, global threshold, universal angle, quarter-power asymptotic, noiseless collision jump.')
