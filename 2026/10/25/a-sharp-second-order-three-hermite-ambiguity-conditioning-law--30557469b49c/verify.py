#!/usr/bin/env python3
"""Finite, independently repeatable checks for a three-Hermite ambiguity-design asymptotic.
No numerical sampling is used as a proof of the theorem.
"""
import math
import random

s = math.sqrt(2)
rm, rp = 2 - s, 2 + s
p, q = 3 - 2*s, 3 + 2*s
alpha1 = (math.exp(rp) - math.exp(rm))/(q-p)
alpha0 = (q*math.exp(rm) - p*math.exp(rp))/(q-p)
C = alpha0 + alpha1

def L(x):
    return (1., 1.-x, 1.-2*x+x*x/2)

def g(x, w):
    ls = L(x)
    return math.exp(-x)*sum(a*b*b for a,b in zip(w,ls))

def gd(x, w):
    ls = L(x)
    dl = (0.,-1.,x-2.)
    return math.exp(-x)*sum(a*(2*b*d-b*b) for a,b,d in zip(w,ls,dl))

def F(R):
    return math.exp(-R)*L(R)[2]**2

def candidate(R):
    f=F(R)
    w0, w1 = (1+math.sqrt(f))*f*alpha0, (1+math.sqrt(f))*f*alpha1
    return (w0,w1,1.-w0-w1)

def bisection(f,lo,hi):
    fl=f(lo)
    for _ in range(65):
        mid=(lo+hi)/2
        fm=f(mid)
        if fl*fm<=0:
            hi=mid
        else:
            lo=mid;fl=fm
    return (lo+hi)/2

def stationary_candidates(R,w):
    N=12000
    xs=[R*j/N for j in range(N+1)]
    roots=[]
    old_x=xs[0]; old_y=gd(old_x,w)
    for x in xs[1:]:
        y=gd(x,w)
        if y*old_y < 0:
            roots.append(bisection(lambda z:gd(z,w),old_x,x))
        old_x=x;old_y=y
    return [0.,R]+roots

def check():
    n=0
    def test(flag,comment):
        nonlocal n
        n+=1
        if not flag:
            raise AssertionError(f'Assertion {n} failed: {comment}')
    test(alpha0>0 and alpha1>0 and C>0,'strict positive primal coefficients')
    for r in (rm,rp):
        test(abs(L(r)[2])<1e-14,'quadratic Laguerre root')
        test(abs(g(r,(alpha0,alpha1,0))-1)<3e-14,'node interpolation')
    u=math.exp(rm)*(q-1)/(q-p)
    v=math.exp(rp)*(1-p)/(q-p)
    test(u>0 and v>0 and abs(u+v-C)<1e-12,'strict dual optimality')
    test(abs(u*math.exp(-rm)+v*math.exp(-rp)-1)<1e-12,'dual first moment')
    test(abs(u*p*math.exp(-rm)+v*q*math.exp(-rp)-1)<1e-12,'dual second moment')
    rng=random.Random(20261023)
    for _ in range(500):
        a,b=rng.random()*80,rng.random()*80
        if g(rm,(a,b,0))>=1 and g(rp,(a,b,0))>=1:
            test(a+b>=C-1e-9,'dual lower bound for feasible node cover')
    for R in (12,14,16,18,20,22,24,27,30,34):
        f=F(R); w=candidate(R)
        test(min(w)>=0 and abs(sum(w)-1)<1e-14,'feasible weights')
        xs=stationary_candidates(R,w)
        vals=[g(x,w) for x in xs]
        min_g=min(vals)
        test(abs(min_g-g(R,w)) < max(f*f*1e-6,1e-14),'end point global minimum of candidate')
        upper=f/(1+C*f*(1-max(1.,(1-R)**2)/L(R)[2]**2))
        test(min_g<=upper*(1+1e-11),'candidate respects analytic upper bound')
        loss=(f-min_g)/f**2
        if R>=16:
            test(0<loss<C*(1+2*math.sqrt(f)),'second-order coefficient tending to C')
        if R>=24:
            test(abs(w[0]/f-alpha0)<0.03 and abs(w[1]/f-alpha1)<0.16,'leading weight scales')
        print(f'R={R:2d}: F={f:.11g}, candidate_min={min_g:.11g}, C_est={loss:.8f}, weights={w[0]:.6g},{w[1]:.6g},{w[2]:.6g}; stationary={len(xs)-2}')
    for R in (14.,20.,30.):
        f=F(R)
        for _ in range(100):
            a,b,c=rng.random(),rng.random(),rng.random()
            z=a+b+c;w=(a/z,b/z,c/z)
            test(g(R,w)<=f+1e-12,'endpoint dominated by highest Hermite multiplier')
    print('PASS:',n,'finite numerical assertions; none is an infinite-domain proof.')

if __name__=='__main__':
    check()
