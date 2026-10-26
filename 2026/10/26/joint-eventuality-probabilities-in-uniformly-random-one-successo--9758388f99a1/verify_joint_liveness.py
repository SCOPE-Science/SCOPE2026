#!/usr/bin/env python3
"""Independent finite checks of a joint temporal-liveness probability identity."""
from fractions import Fraction as F
from itertools import product
from math import factorial


def poly_mul(a,b,N):
    c=[F(0)]*(N+1)
    for i,x in enumerate(a[:N+1]):
        for j,y in enumerate(b[:N+1-i]): c[i+j]+=x*y
    return c

def poly_inv(a,N):
    assert a[0] == 1
    v=[F(0)]*(N+1);v[0]=1
    for i in range(1,N+1):v[i]=-sum(a[j]*v[i-j] for j in range(1,i+1))
    return v

def coeff_probability(n,qs):
    T=[F(0)]+[F(k**(k-1),factorial(k)) for k in range(1,n+1)]
    A=[F(1)]+[-x for x in T[1:]]
    out=poly_inv(A,n)
    r=len(qs)
    for mask in range(1,1<<r):
        a=F(1)
        for i,q in enumerate(qs):
            if mask & (1<<i): a*=1-q
        fac=[F(1)]+[-a*x for x in T[1:]]
        if mask.bit_count()%2:out=poly_mul(out,fac,n)
        else:out=poly_mul(out,poly_inv(fac,n),n)
    return out[n]*factorial(n)/n**n

def cycles(mapping):
    seen=set();out=[]
    for x in range(len(mapping)):
        if x in seen:continue
        walk=[];ix={};v=x
        while v not in seen and v not in ix:
            ix[v]=len(walk);walk.append(v);v=mapping[v]
        if v in ix:out.append(walk[ix[v]:])
        seen.update(walk)
    return out

def semantic_probability(n,qs):
    # Iterate every map and every independent Boolean atomic valuation.
    out=F(0); total=0
    for mapping in product(range(n),repeat=n):
        cc=cycles(mapping)
        for bits in product((0,1),repeat=n*len(qs)):
            prob=F(1)
            for j,q in enumerate(qs):
                for v in range(n):prob*= q if bits[j*n+v] else 1-q
            if all(any(bits[j*n+v] for v in c) for c in cc for j in range(len(qs))):out+=prob
            total+=1
    return out/n**n,total

def cycle_probability(n,qs):
    res=F(0)
    for f in product(range(n),repeat=n):
        val=F(1)
        for cyc in cycles(f):
            for q in qs:val*=1-(1-q)**len(cyc)
        res+=val
    return res/n**n

def birthday(n,c):
    return sum(F(k,n)*c**k * F(factorial(n),factorial(n-k)*n**k) for k in range(1,n+1))

def two_formula(n,p,q):
    c=(1-p)*(1-q)
    return p*q/(p+q-p*q)*(1-birthday(n,c))

def limiting(qs):
    z=F(1)
    for mask in range(1,1<<len(qs)):
        a=F(1)
        for j,q in enumerate(qs):
            if mask&(1<<j):a*=1-q
        z*= (1-a) if mask.bit_count()%2 else 1/(1-a)
    return z

def run():
    qs2=(F(1,2),F(2,3));qs3=(F(1,2),F(2,3),F(3,4))
    for qs,maxn in [(qs2,4),(qs3,3)]:
        for n in range(1,maxn+1):
            sem,count=semantic_probability(n,qs)
            coeff=coeff_probability(n,qs)
            cyc=cycle_probability(n,qs)
            assert sem==coeff==cyc,(n,qs,sem,coeff,cyc)
            print('SEMANTICS_EGF_OK',len(qs),n,count,str(sem))
    arr=[]
    for n in range(1,9):
        coef=coeff_probability(n,qs2)
        birth=two_formula(n,*qs2)
        assert coef==birth,(n,coef,birth)
        arr.append(coef)
    assert all(x<y for x,y in zip(arr,arr[1:])),arr
    assert arr[-1]<limiting(qs2)
    assert limiting(qs2)==F(1,2)*F(2,3)/(F(1,2)+F(2,3)-F(1,2)*F(2,3))
    for n in range(1,7):
        for q in (F(1,3),F(2,5),F(4,5)):
            assert coeff_probability(n,(q,))==q
    print('TWO_EVENT_BIRTHDAY_MONOTONIC_OK',len(arr),str(limiting(qs2)))
    print('SINGLE_EVENT_FINITE_IDENTITY_OK')
    print('JOINT_RANDOM_MAPPING_LIVENESS_OK')
if __name__=='__main__':run()
