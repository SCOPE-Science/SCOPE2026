#!/usr/bin/env python3
"""Independent finite-field tests of a root-fiber formula for square-zero path algebras.

Execute with Python 3 (no external dependencies): python root_fiber_verifier.py
"""
from itertools import product
from collections import Counter
from math import gcd

class Field:
    def __init__(self,q):
        if q not in (2,3,4,5,7):
            raise ValueError('verifier supports q=2,3,4,5,7')
        self.q=q
        self.p=2 if q==4 else q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        # GF(4)=GF(2)[t]/(t^2+t+1); bit 0 is 1, bit 1 is t.
        out=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1):out^=(1<<(i+j))
        if out&4:out ^=7
        return out
    def power(self,a,k):
        z=1
        for _ in range(k):z=self.mul(z,a)
        return z

def mul(a,b,n,edges,F):
    aa,ax=a[:n],a[n:]
    bb,bx=b[:n],b[n:]
    out=[F.mul(aa[i],bb[i]) for i in range(n)]
    for idx,(s,t) in enumerate(edges):
        out.append(F.add(F.mul(aa[s],bx[idx]),F.mul(ax[idx],bb[t])))
    return tuple(out)

def power(a,k,n,edges,F):
    z=tuple([1]*n+[0]*len(edges))
    for _ in range(k):z=mul(z,a,n,edges,F)
    return z

def target_predict(y,n,edges,k,F):
    q,p=F.q,F.p
    rootsets=[]
    for u in y[:n]:
        roots=[x for x in range(1,q) if F.power(x,k)==u]
        if not roots:return 0
        rootsets.append(roots)
    if k%p==0:
        if any(y[n+j]!=0 and y[s]==y[t] for j,(s,t) in enumerate(edges)):
            return 0
        return q**sum(y[s]==y[t] for s,t in edges) * (len(rootsets[0])**n)
    total=0
    for d in product(*rootsets):
        count=1
        for j,(s,t) in enumerate(edges):
            if y[s]==y[t] and d[s]!=d[t]:
                if y[n+j]!=0:
                    count=0
                    break
                count*=q
        total+=count
    return total

def chromatic_partition(n,edges,labels,q):
    return sum(q**sum(color[s]!=color[t] for s,t in edges if s!=t)
               for color in product(range(labels),repeat=n))

def fk_partition(n,edges,labels,q):
    edges=[e for e in edges if e[0]!=e[1]]
    total=0
    for mask in range(1<<len(edges)):
        p=list(range(n))
        def find(x):
            while p[x]!=x:x=p[x]
            return x
        for j,(s,t) in enumerate(edges):
            if mask>>j&1:p[find(s)]=find(t)
        c=len({find(i) for i in range(n)})
        size=mask.bit_count()
        total+=q**(len(edges)-size)*(1-q)**size*labels**c
    return total

cases=[
    (2,2,[(0,1)]), (3,2,[(0,1)]), (4,2,[(0,1)]), (5,2,[(0,1)]),
    (7,2,[(0,1)]), (3,3,[(0,1),(1,2)]),
    (4,3,[(0,1),(1,2)]), (5,3,[(0,1),(1,2)]),
    (3,3,[(0,1),(1,2),(2,0)]), (4,3,[(0,1),(1,2),(2,0)]),
    (3,2,[(0,1),(0,1),(1,1)]), (5,2,[(0,1),(0,1)]),
    (4,2,[(0,1),(1,1)]), (3,3,[(0,0),(1,2),(2,1)])
]
ks=(1,2,3,4,5,6,8,9,10)
checks=0
for q,n,edges in cases:
    F=Field(q)
    values=list(product(range(1,q),repeat=n))
    arrows=list(product(range(q),repeat=len(edges)))
    domain=[v+x for v in values for x in arrows]
    image_set=set(domain)
    for k in ks:
        targets=Counter(power(a,k,n,edges,F) for a in domain)
        for y in image_set:
            got=targets[y]
            want=target_predict(y,n,edges,k,F)
            if got!=want:
                raise AssertionError(('fiber',q,n,edges,k,y,got,want))
        h=gcd(k,q-1)
        diag_images={F.power(x,k) for x in range(1,q)}
        r=len(diag_images)
        if k%F.p:
            expected_identity=chromatic_partition(n,edges,h,q)
            expected_image=q**len(edges)*r**n
        else:
            expected_identity=q**len(edges)*h**n
            expected_image=chromatic_partition(n,edges,r,q)
        identity=tuple([1]*n+[0]*len(edges))
        if targets[identity]!=expected_identity or len(targets)!=expected_image:
            raise AssertionError(('identity/image',q,n,edges,k,targets[identity],expected_identity,len(targets),expected_image))
        if chromatic_partition(n,edges,h,q)!=fk_partition(n,edges,h,q):
            raise AssertionError(('FK',q,n,edges,k))
        checks+=1
print('VERIFY_OK_SQUARE_ZERO_QUIVER_POWER_FIBERS',checks,'complete-target cases',sum((q-1)**n*q**len(edges) for q,n,edges in cases),'elements per exponent setting')
print('SAMPLE_CYCLE3_Q5_K2_TORSION',chromatic_partition(3,[(0,1),(1,2),(2,0)],2,5))
print('SAMPLE_CYCLE3_Q5_K5_IMAGE',chromatic_partition(3,[(0,1),(1,2),(2,0)],4,5))
