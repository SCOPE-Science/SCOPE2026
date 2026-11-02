#!/usr/bin/env python3
"""Independent finite enumeration and numerical checks for conditional component spectrum."""
from fractions import Fraction
from itertools import product
from collections import Counter, defaultdict
import math

checks=0

def check(ok, msg):
    global checks
    checks+=1
    if not ok: raise AssertionError(msg)

def forest_profile(n, parents):
    root=list(range(n))
    def find(j):
        while root[j]!=j:
            j=root[j]
        return j
    for i, u in enumerate(parents):
        if u<i: root[find(i)]=find(u)
    counts=Counter(find(i) for i in range(n))
    h=Counter(counts.values())
    number=sum(1 for i,u in enumerate(parents) if u>i)
    return number, tuple(h.get(k,0) for k in range(1,n+1))

def recursion(n,weight):
    m=[Fraction(0)]*(n+1)
    for i in range(1,n+1):
        d=Fraction(i-1)+weight*(n-i)
        p=weight*(n-i)/d
        old=m[:]
        for k in range(1,n+1):
            m[k]=old[k]+(p if k==1 else 0)+((k-1)*old[k-1]-k*old[k])/d
    return tuple(m[1:])

for n in range(2,7):
    choices=[[j for j in range(n) if j!=i] for i in range(n)]
    joint=defaultdict(lambda:[0]*(n+1))
    for sequence in product(*choices):
        r,h=forest_profile(n,sequence)
        for k,a in enumerate(h,1):joint[r][k]+=a
        joint[r][0]+=1
    check(sum(v[0] for v in joint.values())==(n-1)**n,('total',n))
    for lam in (Fraction(1),Fraction(2),Fraction(3,2)):
        denom=sum(v[0]*lam**r for r,v in joint.items())
        em=tuple(sum(v[k]*lam**r for r,v in joint.items())/denom for k in range(1,n+1))
        ans=recursion(n,lam)
        for k in range(n):check(em[k]==ans[k],('mean',n,lam,k,em[k],ans[k]))
        check(sum((k+1)*em[k] for k in range(n))==n,('mass',n,lam))
        check(sum(em)==sum(r*v[0]*lam**r for r,v in joint.items())/denom,('roots',n,lam))
    for r,vals in joint.items():
        check(sum(k*vals[k] for k in range(1,n+1))==n*vals[0],('partition',n,r))

def d(t,l):return l+(1-l)*t

def p(t,l):return l*(1-t)/d(t,l)

def q(t,l):return math.exp(t-1) if abs(l-1)<1e-12 else d(t,l)**(1/(1-l))

def integrate(f, N=30000):
    h=1/N
    return h*(0.5*f(0)+sum(f(i*h) for i in range(1,N))+0.5*f(1))

def profile(l,k):return integrate(lambda t:p(t,l)*q(t,l)*(1-q(t,l))**(k-1),6000)

def euler(l,n,K):
    a=[0.0]*(K+1)
    for i in range(1,n+1):
        t=(i-1)/(n-1)
        den=(i-1)+l*(n-i)
        pp=l*(n-i)/den
        old=a[:]
        for k in range(1,K+1):
            a[k]=old[k]+(pp if k==1 else 0)+((k-1)*old[k-1]-k*old[k])/den
    return [a[k]/n for k in range(1,K+1)]

for l in (0.25,0.5,1,2,4,10):
    alpha=integrate(lambda t:p(t,l),6000)
    formula=(l*(l-1-math.log(l))/(l-1)**2) if l!=1 else 0.5
    check(abs(alpha-formula)<3e-8,('alpha',l,alpha,formula))
    for k,x in enumerate(euler(l,20000,7),1):
        v=profile(l,k)
        check(abs(x-v)<0.0002,('euler',l,k,x,v))
    total=sum(profile(l,k) for k in range(1,200))
    mass=sum(k*profile(l,k) for k in range(1,200))
    check(abs(total-alpha)<0.002,('components',l,total,alpha))
    check(abs(mass-1)<0.01,('mass',l,mass))
print(f'PASS: {checks} independent exact-enumeration, recurrence, and numerical assertions')
