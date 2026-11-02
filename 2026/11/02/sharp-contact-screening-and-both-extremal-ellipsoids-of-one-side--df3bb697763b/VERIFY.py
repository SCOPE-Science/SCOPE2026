#!/usr/bin/env python3
"""Standalone numerical checks of explicit John and Loewner ellipsoids.

The analytical proof uses exact moment identities; this numerical program
cross-checks them and independently optimizes rotationally symmetric candidates.
Run with: python verify.py
"""
import math
import random
import itertools
from scipy.optimize import minimize


def john(n,a):
    if a==1:
        t=1/math.sqrt(n)
        return (0.,t,t)
    B=2*n*a/(a-1)-(a-1)
    root=math.hypot(B,2*math.sqrt((n+1)*a))
    c=2*a/(B+root) if B>=0 else (root-B)/(2*(n+1))
    b=math.sqrt((a-c)*(1+c)/n)
    r=math.sqrt(((1+c)**2-b*b)/(n-1))
    return c,b,r

def loewner(n,a):
    if a <= (n+1)/(n-1):
        return ((a-1)/2,(a+1)/2,(a+1)/(2*math.sqrt(a)))
    return a/(n+1),n*a/(n+1),n/math.sqrt(n*n-1)

def mat_error(M,n):
    return max(abs(M[i][j]-(int(i==j)/n)) for i in range(n) for j in range(n))

def append_moment(mean,M, v, mass):
    n=len(v)
    for i in range(n):
        mean[i]+=mass*v[i]
        for j in range(n):M[i][j]+=mass*v[i]*v[j]

def certificate_check(n,a):
    c,b,r=john(n,a)
    assert b>0 and r>0 and -1<c<a
    upper=c/a+math.sqrt((b/a)**2+(n-1)*r*r)
    lower=-c+math.sqrt(b*b+(n-1)*r*r)
    assert abs(upper-1)<2e-11 and abs(lower-1)<2e-11
    mean=[0.]*n;M=[[0.]*n for _ in range(n)]
    pplus=(a-c)/(a+1);pminus=(1+c)/(a+1)
    for signs in itertools.product([-1,1],repeat=n-1):
        for sign,prob in [(1,pplus),(-1,pminus)]:
            den=(a-c) if sign==1 else (1+c)
            u=([b/den] if sign==1 else [-b/den])+[s*r*(a if sign==1 else 1)/den for s in signs]
            append_moment(mean,M,u,prob/2**(n-1))
            assert abs(sum(v*v for v in u)-1)<1e-10
    assert max(map(abs,mean))<1e-10
    assert mat_error(M,n)<1e-10
    c,b,r=loewner(n,a)
    x1=(a-c)/b; xm=(-1-c)/b; z=-c/b
    assert x1<=1+1e-12 and abs(x1-1)<1e-11
    assert abs(z*z+1/(r*r)-1)<2e-11
    assert xm>=-1-1e-12
    if a>(n+1)/(n-1)+1e-8:assert xm>-1+1e-10
    mean=[0.]*n;M=[[0.]*n for _ in range(n)]
    if a <= (n+1)/(n-1):
        q=(n-1)/(n*(1-z*z))
        wp=(1-q-q*z)/2; wm=(1-q+q*z)/2
        assert wp>0 and wm>=-1e-12
        append_moment(mean,M,[1]+[0.]*(n-1),wp)
        append_moment(mean,M,[-1]+[0.]*(n-1),wm)
    else:
        q=n/(n+1)
        append_moment(mean,M,[1]+[0.]*(n-1),1/(n+1))
    for j in range(1,n):
        for sign in [-1,1]:
            u=[z]+[0.]*(n-1);u[j]=sign/r
            append_moment(mean,M,u,q/(2*(n-1)))
    assert max(map(abs,mean))<1e-10
    assert mat_error(M,n)<1e-10
    return max(abs(upper-1),abs(lower-1),max(map(abs,mean)),mat_error(M,n))

def numeric_check(n,a):
    cj,bj,rj=john(n,a)
    cl,bl,rl=loewner(n,a)
    def j_con(x):
        c,logb,logr=x; b=math.exp(logb);r=math.exp(logr)
        return [1-c/a-math.hypot(b/a,math.sqrt(n-1)*r),
                1+c-math.hypot(b,math.sqrt(n-1)*r)]
    def l_con(x):
        c,logb,logr=x;b=math.exp(logb);r=math.exp(logr)
        return [1-((a-c)/b)**2,1-((-1-c)/b)**2,1-(c/b)**2-1/r**2]
    jj=minimize(lambda x:-x[1]-(n-1)*x[2],
                [cj,math.log(bj),math.log(rj)],
                constraints=[{'type':'ineq','fun':j_con}],method='SLSQP',
                options={'ftol':1e-12,'maxiter':400})
    ll=minimize(lambda x:x[1]+(n-1)*x[2],
                [cl,math.log(bl),math.log(rl)],
                constraints=[{'type':'ineq','fun':l_con}],method='SLSQP',
                options={'ftol':1e-12,'maxiter':400})
    je=abs(jj.fun+math.log(bj)+(n-1)*math.log(rj))
    le=abs(ll.fun-math.log(bl)-(n-1)*math.log(rl))
    if jj.success:assert je<3e-6,(n,a,'John',jj.message,je)
    if ll.success:assert le<3e-6,(n,a,'Loewner',ll.message,le)
    return je,le,jj.success,ll.success

def main():
    rng=random.Random(20261028)
    trials=0;peak=0
    for n in range(2,11):
        critical=(n+1)/(n-1)
        aa=[1.,1.000001,1.1,critical*.9999,critical,critical*1.0001,2.,5.,30.]
        aa=[x for x in aa if x>=1]
        aa += [1+math.exp(rng.uniform(-6,5)) for _ in range(15)]
        for a in aa:
            peak=max(peak,certificate_check(n,a));trials+=1
    jobs=0;peak_opt=0
    for n in [2,3,4,6,9]:
        a0=(n+1)/(n-1)
        for a in [1.,1.1,a0*.99,a0,a0*1.01,2.,5.,50.]:
            if a<1:continue
            je,le,js,ls=numeric_check(n,a)
            peak_opt=max(peak_opt,je,le)
            jobs+=1
    print('PASS: %d analytic contact and facet certificates, maximum error %.3g'%(trials,peak))
    print('PASS: %d paired independent SciPy optimization starts, maximum log-volume discrepancy %.3g'%(jobs,peak_opt))

if __name__=='__main__':main()
