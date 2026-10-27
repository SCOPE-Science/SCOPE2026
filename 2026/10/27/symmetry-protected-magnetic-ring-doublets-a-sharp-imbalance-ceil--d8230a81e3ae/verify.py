#!/usr/bin/env python3
"""Independent numerical diagnostics for an antipodal two-barrier flux ring.
All spectral assertions with infinitely many levels are established analytically;
these calculations only cross-check finite samples.
"""
import math
import random

pi=math.pi
assertions=0

def check(x,msg):
    global assertions
    assertions+=1
    if not x: raise AssertionError(msg)

def rfun(k):
    return 2*k/math.tan(pi*k)

def root(alpha,n):
    lo=n+0.5
    hi=n+1.0-1e-10
    for _ in range(85):
        mid=(lo+hi)/2
        if rfun(mid)>-alpha:lo=mid
        else:hi=mid
    return (lo+hi)/2

def trace_half(k,alpha,beta):
    c,s=math.cos(pi*k),math.sin(pi*k)
    return c*c-s*s + (alpha+beta)*c*s/k+alpha*beta*s*s/(2*k*k)

def trace_direct(k,alpha,beta):
    c,s=math.cos(pi*k),math.sin(pi*k)
    # P=[[c,s/k],[-ks,c]], J(t)=[[1,0],[t,1]], T=J(beta)*P*J(alpha)*P
    P=((c,s/k),(-k*s,c))
    J1=((1.0,0.0),(alpha,1.0))
    J2=((1.0,0.0),(beta,1.0))
    def mul(X,Y):
        return ((X[0][0]*Y[0][0]+X[0][1]*Y[1][0],X[0][0]*Y[0][1]+X[0][1]*Y[1][1]),(X[1][0]*Y[0][0]+X[1][1]*Y[1][0],X[1][0]*Y[0][1]+X[1][1]*Y[1][1]))
    T=mul(J2,mul(P,mul(J1,P)))
    return (T[0][0]+T[1][1])/2

def secular(k,g,d,theta):
    return trace_half(k,g+d,g-d)-math.cos(theta)

def eigen_cone(g,d,eps,n):
    kn=root(g,n)
    def F(k):
        h=rfun(k)+g
        return h*h-d*d-(2*k*math.cos((pi+eps)/2)/math.sin(pi*k))**2
    def bisection(a,b):
        fa=F(a)
        fb=F(b)
        check(fa*fb<0,'bad cone bracket')
        for _ in range(75):
            m=(a+b)/2
            fm=F(m)
            if fa*fm<=0:b=m;fb=fm
            else:a=m;fa=fm
        return (a+b)/2
    left=bisection(kn-0.08,kn)
    right=bisection(kn,kn+0.08)
    return left,right

random.seed(20261024)
for _ in range(500):
    a,b=10**random.uniform(-1,1.3),10**random.uniform(-1,1.3)
    k=random.uniform(0.10,12)
    check(abs(trace_half(k,a,b)-trace_direct(k,a,b))<4e-12*max(1,abs(trace_half(k,a,b))),'transfer trace')
    for n in [0,1,3,8]:
        ka,kb=root(a,n),root(b,n)
        check(n+0.5<ka<n+1 and n+0.5<kb<n+1,'branch interval')
        check(abs(secular(ka,(a+b)/2,(a-b)/2,pi))<1e-11,'branch secular a')
        check(abs(secular(kb,(a+b)/2,(a-b)/2,pi))<1e-11,'branch secular b')
        check(abs(ka*ka-kb*kb)<abs(a-b)/pi+1e-12,'universal gap bound')

for alpha,beta in [(0.3,1.7),(2.1,8.3),(1.4,2.2),(4.0,0.5)]:
    for n in [10,30,100,400,1600]:
        delta=abs(root(alpha,n)**2-root(beta,n)**2)
        relative_err=abs(delta-abs(alpha-beta)/pi)
        check(relative_err<3.0/max(1,n),'high-energy convergence')

for g in [0.15,0.8,4.0]:
    for n in [0,1,3,6]:
        kn=root(g,n)
        D=2*pi*kn+g/kn+pi*g*g/(2*kn)
        for scale in [0.0001,0.00003]:
            for z,w in [(0.4,1.2),(1.4,0.3),(1.0,1.0)]:
                d=scale*z
                eps=scale*w
                left,right=eigen_cone(g,d,eps,n)
                check(abs(secular(left,g,d,pi+eps))<2e-10,'cone left secular')
                check(abs(secular(right,g,d,pi+eps))<2e-10,'cone right secular')
                gap=right*right-left*left
                predicted=(4*kn/D)*math.hypot(d,math.sqrt(kn*kn+g*g/4)*eps)
                check(abs(gap/predicted-1)<0.005,'cone slope')

print('VERIFY_OK',assertions)
