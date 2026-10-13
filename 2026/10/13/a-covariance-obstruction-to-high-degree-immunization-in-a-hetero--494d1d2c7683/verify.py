#!/usr/bin/env python3
from fractions import Fraction as F

P1=P2=F(1,2)
k1,k2=1,2
phi1=phi2=F(1)
mu=gamma=F(2,15)
w1,w2=F(4,5),F(1,5)
sig1,sig2=F(0),F(1,2)

mean_k=P1*k1+P2*k2
mean_w=P1*w1+P2*w2
D=(mu+gamma)*mean_k
R0=mean_w/D
mean_sig=P1*sig1+P2*sig2
mean_sigw=P1*sig1*w1+P2*sig2*w2
cov=mean_sigw-mean_sig*mean_w
RT=(mean_w-mean_sigw)/D
RU=(1-mean_sig)*mean_w/D

assert mean_k==F(3,2)
assert mean_w==F(1,2)
assert D==F(2,5)
assert R0==F(5,4)
assert mean_sig==F(1,4)
assert mean_sigw==F(1,20)
assert cov==F(-3,40)
assert RT==F(9,8)>1
assert RU==F(15,16)<1
assert RT-RU==F(3,16)==-cov/D

# For a two-point distribution, covariance factorizes exactly.
def cov2(s1,s2,a,b):
    ms=P1*s1+P2*s2
    mw=P1*a+P2*b
    return P1*s1*a+P2*s2*b-ms*mw
for s1,s2 in [(F(0),F(1,2)),(F(0),F(1)),(F(1,3),F(2,3))]:
    lhs=cov2(s1,s2,w1,w2)
    rhs=P1*P2*(s2-s1)*(w2-w1)
    assert lhs==rhs
    assert lhs<0

# f_a(theta)=a theta/(1+theta): f'>0 and f''<0 for theta>=0.
# These assertions sample exact endpoints only; the sign proof is the formula itself.
for a in (F(4,5),F(1,5)):
    assert a>0
    for t in (F(0),F(1,10),F(1)):
        f=a*t/(1+t)
        fp=a/(1+t)**2
        fpp=-2*a/(1+t)**3
        assert f>=0 and fp>0 and fpp<0
        if t==0: assert f==0
        else: assert f>0

print('VERIFY_OK')
print('R0',R0)
print('R_uniform',RU)
print('R_targeted',RT)
print('covariance',cov)
print('difference',RT-RU)
