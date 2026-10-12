#!/usr/bin/env python3
from fractions import Fraction as F

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b))
    out=[F(0)]*n
    for i in range(n):
        out[i]=(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))
    return trim(out)

def scale(a,c):
    return trim([c*x for x in a])

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(out)

def val(p,x):
    y=F(0)
    for c in reversed(p):
        y=y*x+c
    return y

mu=F(1)
g1=F(2); g2=F(3)
v1=g1+mu; v2=g2+mu
b1=F(3); b2=F(2)
eta1=eta2=sig1=sig2=F(1)
th1=th2=th12=F(1)
d1=mu+th1; d2=mu+th2; d12=mu+th12
Lam=F(10)
s1=v1/b1
s2=v2/b2

S=[F(0),F(1)]
r2=[s1/(eta1*sig1), -F(1)/(eta1*sig1)]
r1=[s2/(eta2*sig2), -F(1)/(eta2*sig2)]

Delta=add(scale(mul(S,S),g1*g2),
          scale(mul(r1,r2),-sig1*sig2*v1*v2))

N1=mul(r1, add(scale(S,g2*d1), scale(r2,sig2*v2*d2)))
N2=mul(r2, add(scale(S,g1*d2), scale(r1,sig1*v1*d1)))

A=add([Lam],scale(S,-mu))
A=add(A,scale(r1,th1))
A=add(A,scale(r2,th2))

num_r12=add(scale(mul(r2,N1),g1*sig1),
            scale(mul(r1,N2),g2*sig2))

P=scale(mul(Delta,A),-1)
P=add(P,scale(mul(S,N1),v1))
P=add(P,scale(mul(S,N2),v2))
P=add(P,scale(num_r12,-th12/d12))

assert s1 == 1 and s2 == 2
assert P == [F(260),F(-356),F(53),F(1)]
assert len(P)-1 == 3

# Check the defining rational identity at exact rational points.
for x in (F(1,2), F(4,5), F(9,10), F(3,2)):
    D=val(Delta,x)
    assert D != 0
    c1=val(N1,x)/D
    c2=val(N2,x)/D
    rr1=val(r1,x)
    rr2=val(r2,x)
    r12=(g1*sig1*rr2*c1 + g2*sig2*rr1*c2)/d12
    Fg=(Lam-mu*x
        -v1*x*c1-v2*x*c2
        +th1*rr1+th2*rr2+th12*r12)
    assert val(P,x) == -D*Fg

print("VERIFY_OK")
