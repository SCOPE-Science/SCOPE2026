#!/usr/bin/env python3
import math

def abc(k,s):
    sh=math.sinh
    return sh((k-1)*s)/sh(s), sh(k*s)/sh(s), sh((k+1)*s)/sh(s)

def phi(k,s):
    a,b,c=abc(k,s)
    return math.log(a)-k*math.log(c/b)

def endpoint(k):
    lo=1e-9; hi=0.5
    while phi(k,hi)>0:
        hi*=2
    for _ in range(100):
        m=(lo+hi)/2
        if phi(k,m)>0: lo=m
        else: hi=m
    return (lo+hi)/2

def branch(k,s):
    t=math.exp(2*s)
    A=sum(t**j for j in range(1,k))
    B=sum(t**j for j in range(k))
    C=sum(t**j for j in range(k+1))
    G=B*A**(1.0/k)-C
    lam=A**k/(B**k*G)
    return t,G,lam,t**k/G,1.0/G,A/G

def lc(k):
    r=(k-1)**(1.0/k)
    return (k-1)**k/(k**k*(k*r-(k+1)))

def Bcoef(k):
    r=(k-1)**(1.0/k)
    return k*(k+1)*(3*k+1-3*(k-1)*r)/(6*(k*r-(k+1)))

worst=0.0
cases=0
for k in range(4,21):
    sk=endpoint(k)
    # Endpoint is unique numerically because phi is sampled as strictly decreasing.
    prev=phi(k,sk/500)
    for i in range(2,500):
        cur=phi(k,sk*i/500)
        if not cur < prev:
            raise AssertionError(('phi monotonicity',k,i,prev,cur))
        prev=cur
    for frac in (0.1,0.25,0.5,0.8):
        s=sk*frac
        t,G,lam,z0,z1,z2=branch(k,s)
        rhs0=lam*((z0+z2)/z2)**k
        rhs1=lam*((z1+z2)/z2)**k
        rhs2=lam*((z0+z1+z2+1)/z2)**k
        scale=max(1.0,z0,z1,z2)
        err=max(abs(rhs0-z0),abs(rhs1-z1),abs(rhs2-z2))/scale
        worst=max(worst,err); cases+=1
        if err>5e-9: raise AssertionError(('residual',k,s,err))
        # Reciprocal t swaps z0 and z1 while keeping z2 and lambda.
        ti=1.0/t
        A=sum(ti**j for j in range(1,k)); BB=sum(ti**j for j in range(k)); C=sum(ti**j for j in range(k+1))
        GG=BB*A**(1.0/k)-C; ll=A**k/(BB**k*GG)
        zz0=ti**k/GG; zz1=1/GG; zz2=A/GG
        err2=max(abs(ll-lam),abs(zz0-z1),abs(zz1-z0),abs(zz2-z2))/max(1.0,lam,z0,z1,z2)
        worst=max(worst,err2)
        if err2>5e-9: raise AssertionError(('reciprocal',k,s,err2))

if not (Bcoef(4)>0 and Bcoef(5)>0): raise AssertionError('positive coefficient cases')
for k in range(6,501):
    if not Bcoef(k)<0: raise AssertionError(('negative coefficient',k,Bcoef(k)))

for k in (4,5,6,7,10,20):
    s=1e-4
    _,_,l,*_=branch(k,s)
    est=math.log(l/lc(k))/(s*s)
    if abs(est-Bcoef(k))>3e-4*max(1.0,abs(Bcoef(k))):
        raise AssertionError(('Taylor',k,est,Bcoef(k)))

# k=4 merger agrees with the source's closed form.
source4=81.0/(256.0*(4.0*3.0**0.25-5.0))
if abs(lc(4)-source4)>1e-12: raise AssertionError(('k4 source check',lc(4),source4))

# k=6 has genuine local descent and later divergence before the endpoint.
sk6=endpoint(6)
if not branch(6,0.01)[2] < lc(6): raise AssertionError('k6 local descent')
if not branch(6,0.99*sk6)[2] > lc(6): raise AssertionError('k6 endpoint rise')

print('VERIFY_OK cases=%d worst_residual=%.3e sign_orders=4..500' % (cases,worst))
