#!/usr/bin/env python3
"""Standalone finite diagnostics for sharp Lipschitz moduli of weighted best-line approximation."""
import math
import random

def predicted(v,p):
    v=[abs(x) for x in v if x]
    k=len(v)
    if k==1:return 1.0
    vn=sum(x**p for x in v)**(1/p)
    if p==2:return 1.0
    if p<2 and k>=3:return vn/min(v)
    q=p/(p-1)
    pairs=[]
    for i in range(k):
        for j in range(i+1,k):
            c=(v[j]/v[i])**(1/(p-1))
            pairs.append((1+c**q)**(1/q)/(v[i]+c*v[j]))
    return vn*max(pairs)

def grad_ratio(v,p,r):
    # Requires weighted signed residual moment to vanish.
    q=p/(p-1)
    g=[vi*abs(ri)**(p-2) for vi,ri in zip(v,r)]
    mx=max(g)
    g=[u/mx for u in g]
    return (sum(x**q for x in g)**(1/q))/(sum(vi*gi for vi,gi in zip(v,g)))*sum(vi**p for vi in v)**(1/p)

def balanced(v,p,rad,split):
    # Split residuals into opposing signs and rescale negative side to balance moment.
    raw=[abs(x) for x in rad]
    sp=sum(v[i]*raw[i]**(p-1) for i in range(len(v)) if i in split)
    sn=sum(v[i]*raw[i]**(p-1) for i in range(len(v)) if i not in split)
    if not sp or not sn:return None
    factor=(sp/sn)**(1/(p-1))
    return [raw[i] if i in split else -raw[i]*factor for i in range(len(v))]

random.seed(20261017)
count=0
for p in (1.2,1.5,1.9,2.1,2.5,3,4,7,15):
    for k in (2,3,4,5):
        for _ in range(60):
            v=[math.exp(random.uniform(-2,2)) for i in range(k)]
            L=predicted(v,p)
            for _ in range(50):
                split=set(random.sample(range(k),random.randrange(1,k)))
                rad=[math.exp(random.uniform(-2,2)) for i in range(k)]
                r=balanced(v,p,rad,split)
                if r is None:continue
                z=grad_ratio(v,p,r)
                assert z <= L*(1+2e-10), (p,k,v,L,z,r)
                count+=1
print('PASS',count,'bounded residual-gradient comparisons')
for p in (1.2,1.5,1.9,2.1,3,4,8):
    for k in (3,4,5):
        for _ in range(20):
            v=[math.exp(random.uniform(-1,1)) for i in range(k)]
            L=predicted(v,p)
            if p<2:
                imin=min(range(k),key=lambda i:v[i]); others=[i for i in range(k) if i!=imin]
                r=[1.0]*k
                j=others[-1]
                for e in (1e-70,1e-80):
                    r[imin]=e
                    r[j]=-(sum(v[h]*abs(r[h])**(p-1) for h in range(k) if h!=j)/v[j])**(1/(p-1))
                    z=grad_ratio(v,p,r)
                    assert z/L > .999,(p,k,z,L)
            else:
                q=p/(p-1)
                pair=max(((1+(v[j]/v[i])**(q/(p-1)))**(1/q)/(v[i]+(v[j]/v[i])**(1/(p-1))*v[j]),i,j) for i in range(k) for j in range(i+1,k))
                i,j=pair[1:]
                r=[0.0]*k
                r[i]=v[i]**(-1/(p-1));r[j]=-v[j]**(-1/(p-1))
                z=grad_ratio(v,p,r)
                assert abs(z/L-1)<1e-11,(p,k,z,L)
print('PASS prescribed two-support extremizers and endpoint gradients')
