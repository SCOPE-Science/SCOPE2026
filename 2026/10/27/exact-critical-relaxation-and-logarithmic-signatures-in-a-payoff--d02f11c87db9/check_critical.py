#!/usr/bin/env python3
"""Reproducibility checks for critical relaxation of the feedback replicator.

Only uses the Python standard library. Finite checks accompany, not replace,
the analytically proved separations and global asymptotics.
"""
from fractions import Fraction as Q
from math import log, isfinite

checks=0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def drift(x,a,b):
    return x*(1-x)*(2*x-1)*(a+(b-a)*x)


def payoff_drift(x,R,S,T,P):
    ucc=(1-x)*T+x*R
    ucd=(1-x)*P+x*S
    udc=(1-x)*R+x*T
    udd=(1-x)*S+x*P
    pc=x*ucc+(1-x)*ucd
    pd=x*udc+(1-x)*udd
    return x*(1-x)*(pc-pd)

# Algebra: directly reconstruct the ODE from the time-dependent payoff matrix.
for R in range(-2,4):
 for S in range(-2,4):
  for T in range(-2,4):
   for P in range(-2,4):
    for i in range(1,10):
     x=Q(i,10)
     verify(payoff_drift(x,Q(R),Q(S),Q(T),Q(P))==drift(x,Q(S-P),Q(R-T)), "payoff reduction")

# Test the three exact critical specializations as rational identities.
for i in range(1,49):
 u=Q(i,100)
 for c in [Q(1,3),Q(2,5),Q(1),Q(3)]:
  boundary=-c*u*u*(1-u)*(1-2*u)
  verify(drift(u,0,c)==boundary, "boundary at zero")
  verify(-drift(1-u,c,0)==boundary, "boundary at one")
  interior=-c*u*u*(1-4*u*u)
  verify(drift(Q(1,2)+u,c,-c)==interior, "interior from right")
  verify(-drift(Q(1,2)-u,-c,c)==interior, "interior from left")


def F(z):
    return z-log(z-1)+4*log(z-2)

def G(z):
    return z+log((z-2)/(z+2))

def bifurcation_inverse(H,z0,c,t):
    target=H(z0)+c*t
    lo=z0
    hi=max(z0+2, c*t+z0+40)
    while H(hi)<target:
        hi=hi*2
    for _ in range(90):
        mid=(lo+hi)/2
        if H(mid)<target:lo=mid
        else:hi=mid
    return (lo+hi)/2

# Exact antiderivatives verified through rational derivatives.
for z0 in [Q(9,4),Q(3),Q(4),Q(9),Q(43,3),Q(100)]:
    fbprime=1-Q(1)/(z0-1)+4/(z0-2)
    fgprime=1+Q(1)/(z0-2)-Q(1)/(z0+2)
    verify(fbprime*(1-Q(1)/z0)*(1-Q(2)/z0)==1, "boundary differential identity")
    verify(fgprime*(1-Q(4)/(z0*z0))==1, "interior differential identity")

# Verify the two distinct asymptotic constants via implicit flow and their signs.
for H in [F,G]:
    for u0 in [0.14,0.23,0.37]:
        for c in [0.5,1.0,2.0]:
            z0=1/u0
            for t in [10000,100000,1000000]:
                z=bifurcation_inverse(H,z0,c,t)
                verify(abs(H(z)-H(z0)-c*t)<1e-7, "integral identity")
                if H is F:
                    r=z-c*t+3*log(c*t)
                    verify(abs(r-F(z0))<0.025,"boundary constant with logarithmic correction")
                    if t==1000000:
                        verify(abs(z-c*t-F(z0))>25,"endpoint log term is nonzero")
                else:
                    r=z-c*t
                    verify(abs(r-G(z0))<0.002, "interior constant without log term")

# Independent time integration: RK4 directly on original vector field.
def rk4(x0,a,b,endtime=25,step=.0025):
    x=x0
    n=round(endtime/step)
    for _ in range(n):
        k1=drift(x,a,b)
        k2=drift(x+step*k1/2,a,b)
        k3=drift(x+step*k2/2,a,b)
        k4=drift(x+step*k3,a,b)
        x+=step*(k1+2*k2+2*k3+k4)/6
    return x

for x0,a,b,c,H,side in [
    (.3,0,1,1,F,'at_zero'),
    (.7,1,0,1,F,'at_one'),
    (.75,1,-1,1,G,'mid_right'),
    (.25,-1,1,1,G,'mid_left')]:
    x=rk4(x0,a,b)
    u0= x0 if side=='at_zero' else 1-x0 if side=='at_one' else abs(x0-.5)
    z=bifurcation_inverse(H,1/u0,c,25)
    expected=1/z if side=='at_zero' else 1-1/z if side=='at_one' else .5+1/z if side=='mid_right' else .5-1/z
    verify(abs(x-expected)<1e-9,'independent RK4 comparison '+side)

# Signs/orientation at all three lines and the frozen corner.
for x in [Q(i,100) for i in range(1,100) if i!=50]:
    verify(drift(x,0,0)==0,'double degeneracy is frozen')
    if x<Q(1,2):
        verify(drift(x,0,1)<0,'zero-boundary attraction')
        verify(drift(x,-1,1)>0,'interior-left attraction')
    else:
        verify(drift(x,1,0)>0,'one-boundary attraction')
        verify(drift(x,1,-1)<0,'interior-right attraction')
print('PASS: %d exact/numerical checks' %checks)
