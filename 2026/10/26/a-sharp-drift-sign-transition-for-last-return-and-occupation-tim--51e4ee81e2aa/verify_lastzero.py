"""Exact rational finite checks for a Bernoulli walk's last-zero/occupation dependence."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb

def exact_enumeration(n,p):
    q=1-p;joint=defaultdict(F)
    for steps in product((-1,1),repeat=2*n):
        ups=sum(e==1 for e in steps)
        weight=p**ups*q**(2*n-ups)
        s=0;last=0;above=0
        for t,e in enumerate(steps,1):
            s2=s+e
            if s+s2>0: above+=1
            s=s2
            if s==0:last=t//2
        assert above%2==0
        joint[last,above//2]+=weight
    return joint

def symbolic_joint(n,p):
    q=1-p; d=defaultdict(F)
    for k in range(n+1):
        if k==n:
            mass=comb(2*n,n)*(p*q)**n
            for u in range(n+1):d[k,u]=mass/F(n+1)
        else:
            m=n-k
            b=lambda r:F(r,m)*comb(2*m,m-r)
            pos=sum((b(r)*p**(m+r)*q**(m-r) for r in range(1,m+1)),F(0))
            neg=sum((b(r)*p**(m-r)*q**(m+r) for r in range(1,m+1)),F(0))
            mass=comb(2*k,k)*(p*q)**k/F(k+1)
            for j in range(k+1):
                d[k,j]+=mass*neg
                d[k,j+m]+=mass*pos
    return d

runs=0
for n in range(1,8):
    for p in [F(1,9),F(1,3),F(1,2),F(3,5),F(7,8)]:
        a=exact_enumeration(n,p);b=symbolic_joint(n,p)
        assert sum(a.values())==1
        for k in range(n+1):
            for u in range(n+1):assert a[k,u]==b[k,u],(n,p,k,u,a[k,u],b[k,u])
        E=lambda h:sum((w*h(k,u) for (k,u),w in a.items()),F(0))
        cov=E(lambda k,u:k*u)-E(lambda k,u:k)*E(lambda k,u:u)
        assert (cov>0)-(cov<0) == (p<F(1,2))-(p>F(1,2)),(n,p,cov)
        runs+=1
    print('PASS n=%d, paths=%d, five rational drifts'%(n,4**n))
print('Exact joint cells and drift-covariance signs passed:',runs)
