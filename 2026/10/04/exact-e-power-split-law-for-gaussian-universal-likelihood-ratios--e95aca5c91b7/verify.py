#!/usr/bin/env python3
import math

def G(n,m,mu): return 0.5*(n-m)*(mu*mu-1.0/m)
def brute(n,mu,tol=1e-11):
    vals=[G(n,m,mu) for m in range(1,n)]; mx=max(vals)
    return [m for m,v in enumerate(vals,1) if abs(v-mx)<=tol*max(1.0,abs(mx))],mx
def threshold(n,mu,tol=1e-12):
    a=mu*mu; out=[]
    for m in range(1,n):
        lo=0.0 if m==n-1 else n/(m*(m+1)); hi=math.inf if m==1 else n/((m-1)*m)
        if a+tol>=lo and a<=hi+tol: out.append(m)
    return out
for n in range(2,81):
    for mu in [0.0,0.03,0.1,0.25,0.7,1.3,3.0]:
        for m in range(1,n-1):
            lhs=G(n,m+1,mu)-G(n,m,mu); rhs=0.5*(n/(m*(m+1))-mu*mu)
            assert abs(lhs-rhs)<2e-12*max(1.0,abs(lhs),abs(rhs))
for n in range(2,121):
    mus=[0.0,0.02,0.05,0.1,0.2,0.5,1.0,2.0]+[math.sqrt(n/(m*(m+1))) for m in range(1,n-1)]
    for mu in mus: assert brute(n,mu)[0]==threshold(n,mu),(n,mu,brute(n,mu)[0],threshold(n,mu))
for n in range(2,101):
    e=1/math.sqrt(n-1)
    for mu,pos in [(0.99*e,False),(e,False),(1.01*e,True)]: assert (brute(n,mu)[1]>1e-12)==pos
n=200000
for h,frac0,p0 in [(0.5,1,0),(1,1,0),(1.5,2/3,0.125),(2,0.5,0.5),(3,1/3,2)]:
    ms,mx=brute(n,h/math.sqrt(n)); assert abs(ms[0]/n-frac0)<2e-4 and abs(mx-p0)<2e-4
for mu in [0.05,0.1,0.3]:
    for n in [20000,80000]:
        ms,mx=brute(n,mu); assert abs(ms[0]-math.sqrt(n)/abs(mu))<=2
        assert abs(mx-(0.5*n*mu*mu-math.sqrt(n)*abs(mu)))<2
ms,mx=brute(1000,0.1); assert ms==[316] and abs(mx-2.3377215189873426)<1e-12 and abs(G(1000,500,0.1)-2)<1e-12
ms,mx=brute(10000,0.05); assert ms==[2000] and abs(mx-8)<1e-12 and abs(G(10000,5000,0.05)-5.75)<1e-12
print('VERIFY_OK')
