#!/usr/bin/env python3
import math

r,a=1.0,1.4
xb=r/a
nu=3.0
tau_star=1.1
zeta=0.9
muM=0.25
rho=0.7
bp=0.8
bep=0.6
dp=0.08
dep=0.12
L=30.0

def softplus(x):
    if x>40.0:
        return x
    if x<-40.0:
        return math.exp(x)
    return math.log1p(math.exp(x))

def phiA(t,ts=tau_star):
    return 1.0/(1.0+math.exp(-nu*(t-ts)))

def H(t,ts=tau_star):
    # xb * integral_0^t 1/(1+exp(nu*(s-ts))) ds
    return xb*(t-(softplus(nu*(t-ts))-softplus(-nu*ts))/nu)

def MB(t):
    return (dp/dep)*math.exp(-dep*L)*(math.exp(dep*t)-1.0)

def tildeB(t,ts=tau_star):
    return 0.0 if t<ts else bp*(math.exp(-bep*(t-ts))+1.0)

hunger=muM*math.exp(-rho*xb)

def trap(f,hi=60.0,n=12000):
    h=hi/n
    total=0.5*(f(0.0)+f(hi))
    for i in range(1,n):
        total += f(i*h)
    return total*h

def R(g,k):
    def f(t):
        S=math.exp(-hunger*t-MB(t)-g*H(t))
        B=k*xb*phiA(t)+tildeB(t)*(1.0-math.exp(-zeta*xb))
        return B*S
    return trap(f)

vals=[R(g,0.7) for g in (0.0,0.25,0.5,1.0)]
assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))

g=0.4
r0,r1,r2=R(g,0.0),R(g,0.5),R(g,1.0)
assert r0<r1<r2
assert abs((r2-r1)-(r1-r0))<2e-8

def AC(g):
    A=R(g,0.0)
    C=(R(g,1.0)-A)/xb
    return A,C

positive=[]
for gg in (0.2,0.5,0.8,1.2):
    A,C=AC(gg)
    if A<1.0:
        positive.append((gg,(1.0-A)/(xb*C)))
if len(positive)>=2:
    assert all(positive[i][1]<positive[i+1][1] for i in range(len(positive)-1))

def Qsharp(ts,k):
    def f(s):
        F=k*xb+bp*(math.exp(-bep*s)+1.0)*(1.0-math.exp(-zeta*xb))
        return F*math.exp(-hunger*(ts+s)-MB(ts+s))
    return trap(f)

def Rsharp_trans(ts,g,k):
    return math.exp(-g*xb*ts)*Qsharp(ts,k)

def Rsharp_direct(ts,g,k):
    def f(t):
        if t<ts:
            return 0.0
        B=k*xb+bp*(math.exp(-bep*(t-ts))+1.0)*(1.0-math.exp(-zeta*xb))
        return B*math.exp(-g*xb*ts-hunger*t-MB(t))
    return trap(f)

for ts in (0.5,1.0,1.5):
    x=Rsharp_trans(ts,0.35,0.7)
    y=Rsharp_direct(ts,0.35,0.7)
    assert abs(x-y)<3e-3

ts_grid=(0.5,1.0,1.5,2.0)
qs=[Qsharp(ts,0.7) for ts in ts_grid]
assert all(qs[i]>qs[i+1] for i in range(len(qs)-1))

pairs=[(ts,math.log(q)/(xb*ts)) for ts,q in zip(ts_grid,qs) if q>1.0]
assert len(pairs)>=2
assert all(pairs[i][1]>pairs[i+1][1] for i in range(len(pairs)-1))

print("VERIFY_OK")
