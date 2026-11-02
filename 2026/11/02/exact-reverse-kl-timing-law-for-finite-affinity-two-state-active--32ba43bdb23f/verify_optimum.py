#!/usr/bin/env python3
"""Reproducible numerical checks for a finite-affinity two-state charging theorem.
Requires only Python 3.10+ standard library. No claim that numerical checks prove universal statements.
"""
import math

def dkl(p,q):
    return p*math.log(p/q)+(1-p)*math.log((1-p)/(1-q))

def model(q,r,s):
    assert 0<q<r<1 and s>0
    gap=r-q
    alpha=math.log(r/(1-r))-math.log(q/(1-q))
    B=alpha*gap
    z=math.exp(-s)
    u=-math.expm1(-s)
    p=q+gap*u
    F=dkl(p,q)
    voltage=math.log(p/(1-p))-math.log(q/(1-q))
    Fp=gap*z*voltage
    Fpp=gap*z*(-voltage+gap*z/(p*(1-p)))
    Q=z*dkl(q,p)
    return B,u,F,Fp,Fpp,Q

def bisect(sign,lo,hi,its=100):
    flo=sign(lo);fhi=sign(hi)
    assert flo>0 and fhi<0,(lo,hi,flo,fhi)
    for _ in range(its):
        mid=(lo+hi)/2
        if sign(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def spower(q,r):
    return bisect(lambda s:s*model(q,r,s)[3]-model(q,r,s)[2],.02,60)

def optimum(q,r,chi):
    sp=spower(q,r)
    def slope(s):
        B,u,F,Fp,_,Q=model(q,r,s)
        return B*Q+chi*(s*Fp-F)
    hi=max(100,4*math.log(1/chi) if chi<1 else 100)
    return bisect(slope,sp,hi)

def eta(q,r,chi,s):
    B,u,F,*_=model(q,r,s)
    return F/(B*u+chi*s)

checks=0
for q,r in [(0.03,.30),(.08,.7),(.2,.8),(.38,.49),(.43,.97),(.01,.98)]:
    sp=spower(q,r)
    ss=[]
    for chi in [1e-7,1e-5,1e-3,.05,.5,2,20,200]:
        s=optimum(q,r,chi);ss.append(s)
        B,u,F,Fp,Fpp,Q=model(q,r,s)
        rr=B*Q/(F-s*Fp)
        assert abs(rr/chi-1)<2e-8,(q,r,chi,s,rr)
        assert s>sp
        assert eta(q,r,chi,s)>eta(q,r,chi,sp)
        for delta in [-.6,-.2,-.03,.03,.2,.6]:
            neighbor=s+delta
            if neighbor>0:
                assert eta(q,r,chi,s)>eta(q,r,chi,neighbor)-1e-12,(q,r,chi,s,neighbor)
                checks+=1
        checks+=3
    assert all(x>y for x,y in zip(ss,ss[1:])),(q,r,ss)
    checks+=1
    B,u,F,Fp,Fpp,Q=model(q,r,sp)
    for chi in [100,1000,10000]:
        s=optimum(q,r,chi)
        pred=sp+B*Q/(chi*(-sp*Fpp))
        assert abs(s-pred)<10/chi**2,(q,r,chi,s,pred)
        checks+=1
    F0=dkl(r,q);G0=dkl(q,r)
    for chi in [1e-6,1e-8]:
        s=optimum(q,r,chi)
        pred=math.log(B*G0/(chi*F0))
        assert abs(s-pred)<2e-3,(q,r,chi,s,pred)
        loss=F0/B-eta(q,r,chi,s)
        predloss=F0/(B*B)*chi*(pred+1)
        assert abs(loss-predloss)<2e-3*predloss,(q,r,chi,loss,predloss)
        checks+=2
    print(f'q={q:.2f} r={r:.2f} sp={sp:.9f}, s(chi=.05)={ss[3]:.9f}')
print('PASS',checks,'numerical assertions')
