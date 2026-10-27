"""Independent finite consistency checks for the two-floor scalar iteration."""
import math
import random
from fractions import Fraction as Q

def L(r, lam, eps, delta):
    return (eps**4*(lam*r+delta)**4+(lam*r)**4)**.25

def step(x, lam, gamma, eps, delta):
    return x*(1-gamma*lam/L(abs(x),lam,eps,delta))

def root(lam,gamma,eps,delta):
    lo,hi=0.,max(1.,gamma*2/eps)
    while L(hi,lam,eps,delta)<gamma*lam/2: hi*=2
    for _ in range(130):
        m=(lo+hi)/2
        if L(m,lam,eps,delta)<gamma*lam/2:lo=m
        else:hi=m
    return (lo+hi)/2

R=random.Random(1729)
count=0
for _ in range(500):
    eps=Q(R.randint(1,10),R.randint(1,10)); delta=Q(R.randint(1,10),R.randint(1,10)); lam=Q(R.randint(1,10),R.randint(1,10)); A=Q(R.randint(1,10),R.randint(1,10))
    D=eps**4*(A+delta)**4+A**4
    numerator=A*(eps**4*(A+delta)**3+A**3)
    assert D-numerator==eps**4*delta*(A+delta)**3>0
    assert 0<numerator<D
    count+=2
for _ in range(300):
    eps=R.uniform(.1,3);delta=R.uniform(.1,3);lam=R.uniform(.2,4)
    C=R.uniform(2.01,7.)*eps*delta;gamma=C/lam
    a=root(lam,gamma,eps,delta)
    assert abs(step(a,lam,gamma,eps,delta)+a)<1.e-12*max(1,a)
    A=lam*a
    D=eps**4*(A+delta)**4+A**4
    q=A*(eps**4*(A+delta)**3+A**3)/D
    mult=(-1+2*q)**2
    assert 0<q<1 and mult<1
    tiny=1.e-6*max(1.,a)
    assert abs((step(a+tiny,lam,gamma,eps,delta)-step(a-tiny,lam,gamma,eps,delta))/(2*tiny)-(-1+2*q))<1.e-7
    count+=4
# Critical asymptotics
lam,eps,delta=1.4,1.3,2.1
C=2*eps*delta
x=0.005
for n in range(1,40001):
    x=step(x,lam,C/lam,eps,delta)
assert abs(40000*abs(x)-delta/(2*lam))<.011
count+=1
# Matched critical local rate order two
lam,eps,delta=2.,1.6,.7
for x in [1.e-3,1.e-4,1.e-5]:
    ratio=step(x,lam,eps*delta/lam,eps,delta)/x**2
    assert abs(ratio-lam/delta)<.015
    count+=1
# delta -> 0 selects symmetric midpoint of discontinuous sign cycle
lam,eps,gamma=1.7,.8,1.2
s=(1+eps**4)**.25
for d in [1.e-3,1.e-4,1.e-5]:
    a=root(lam,gamma,eps,d)
    assert abs(a-gamma/(2*s))<.02
    count+=1
print('VERIFY_OK',count,'checks')
