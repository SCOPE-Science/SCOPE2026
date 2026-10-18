#!/usr/bin/env python3
"""Standalone finite checks for the stated Bernoulli attachment-tree results.

Uses only Python's standard library. Finite tests are not proofs of limits.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def shape(bits):
    # Vertex labels 1,...,n. For k>=3 bit[k-3]=1 means parent k-1.
    n = len(bits)+2
    par = [0]*(n+1)
    par[2] = 1
    for k,b in enumerate(bits,3):
        par[k] = k-1 if b else k-2
    dep=[0]*(n+1)
    for k in range(2,n+1):
        dep[k]=dep[par[k]]+1
    degchild=[0]*(n+1)
    for k in range(2,n+1):
        degchild[par[k]]+=1
    height = max(dep[1:]); leaves=sum(degchild[k]==0 for k in range(1,n+1))
    # Independently calculated attachment-sequence observables.
    a=[1,1,1]+list(bits)
    y=1; ht=1; lv=1
    for k in range(3,n+1):
        y=1 if a[k] else 1-y
        ht+=y
        lv+=a[k-1]*(1-a[k])
    assert ht == height == dep[n]
    assert lv == leaves
    return ht,lv


def exhaustive(n,p):
    q=1-p
    tots=[F(0) for _ in range(5)]
    for bs in product((0,1),repeat=n-2):
        wt=p**sum(bs)*q**(n-2-sum(bs))
        h,l=shape(bs)
        vals=[h,l,h*h,l*l,h*l]
        for i,v in enumerate(vals): tots[i]+=wt*v
    mh,ml,h2,l2,hl=tots
    return mh,ml,h2-mh*mh,l2-ml*ml,hl-mh*ml


def exact_means(n,p):
    q=1-p
    return ((n-1)/(1+q)+q*(1-(-q)**(n-1))/(1+q)**2,
            1+q+(n-3)*p*q)


def sigma(p):
    q=1-p
    return (p*q/(1+q)**3,
            p*q*(1-3*p*q),
            p*q*(q*q+q-1)/(1+q)**2)


def moment_dp(n,p):
    """Exact/floating state-reward recursion without enumerating 2^(n-2) trees."""
    q=1-p
    # Keys (last depth increment, last attachment), entries
    # probability, sum H, sum L, sum H^2, sum L^2, sum HL.
    state={(1,1):(1.,1.,1.,1.,1.,1.)}
    for k in range(3,n+1):
        new={}
        for (old_y,old_a), (prob,eh,el,eh2,el2,ehl) in state.items():
            for a,w in ((0,q),(1,p)):
                y=1 if a else 1-old_y
                c=old_a*(1-a)
                z=(w*prob,
                   w*(eh+y*prob),
                   w*(el+c*prob),
                   w*(eh2+2*y*eh+y*y*prob),
                   w*(el2+2*c*el+c*c*prob),
                   w*(ehl+y*el+c*eh+y*c*prob))
                key=(y,a)
                if key not in new: new[key]=z
                else: new[key]=tuple(x+u for x,u in zip(new[key],z))
        state=new
    sums=tuple(sum(v[i] for v in state.values()) for i in range(6))
    w,eh,el,eh2,el2,ehl=sums
    assert abs(w-1)<1e-7
    return eh,el,eh2-eh*eh,el2-el*el,ehl-eh*el


def main():
    count=0
    for n in range(3,13):
        for p in (F(1,5),F(1,3),F(1,2),F(2,3),F(4,5)):
            mh,ml,vh,vl,c=exhaustive(n,p)
            emh,eml=exact_means(n,p)
            assert (mh,ml)==(emh,eml)
            dh,dl,dvh,dvl,dc=moment_dp(n,float(p))
            for a,b in zip((mh,ml,vh,vl,c),(dh,dl,dvh,dvl,dc)):
                assert abs(float(a)-b)<1e-7,(n,p,a,b)
                count+=1
    # Large-n exact moment recursion checks the predicted limiting covariance.
    for p in (0.1,0.25,0.3819660112501051,0.5,0.75,0.9):
        a,b,c=sigma(p)
        n=3000
        mh,ml,vh,vl,cov=moment_dp(n,p)
        assert abs(vh/n-a)<0.002
        assert abs(vl/n-b)<0.002
        assert abs(cov/n-c)<0.002
        count+=3
        assert abs(mh-exact_means(n,p)[0])<1e-5
        assert abs(ml-exact_means(n,p)[1])<1e-5
        count+=2
    # Exact covariance matrix has a strictly positive determinant.
    for q in (F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)):
        a,b,c=sigma(1-q)
        determinant = (1-q)**2*q**4*(1+q-q*q)/(1+q)**4
        assert a*b-c*c==determinant and determinant>0
        count+=1
    q0=(sqrt(5)-1)/2
    assert abs(q0*q0+q0-1)<1e-12
    assert sigma(0.8)[2]<0 and sigma(0.1)[2]>0
    count+=3
    print('VERIFIED', count, 'finite assertions; exact path enumeration n=3,...,12; six large-n moment recursions')


if __name__=='__main__':main()
