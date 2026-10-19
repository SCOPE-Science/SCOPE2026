#!/usr/bin/env python3
"""Numerical cross-checks for planar-graph Gabor operator spectra.
Uses Python standard library; calculations are finite checks, not the proof.
"""
from __future__ import annotations
import cmath
import itertools
import math
from collections import Counter

class Field:
    def __init__(self,q):
        self.q=q
        if q==9:
            self.p=3
            self.vals=list(range(9))
        else:
            assert q in (3,5,7)
            self.p=q
            self.vals=list(range(q))
    def add(self,a,b):
        return ((a%3+b%3)%3 + 3*((a//3+b//3)%3)) if self.q==9 else (a+b)%self.q
    def sub(self,a,b):
        return ((a%3-b%3)%3 + 3*((a//3-b//3)%3)) if self.q==9 else (a-b)%self.q
    def mul(self,a,b):
        if self.q!=9:return a*b%self.q
        x,y=a%3,a//3; u,v=b%3,b//3
        # F_9 = F_3[t]/(t^2+1)
        return (x*u-y*v)%3+3*((x*v+y*u)%3)
    def chi(self,a):
        trace=(2*(a%3))%3 if self.q==9 else a
        return cmath.exp(2j*math.pi*trace/self.p)
    def chi2(self,a,b,alpha,beta):
        return self.chi(self.add(self.mul(a,alpha),self.mul(b,beta)))

def ambiguity_values(q, opt=False, nonplanar=False):
    F=Field(q)
    graph={x:(F.mul(x,F.mul(x,x)) if nonplanar else F.mul(x,x)) for x in F.vals}
    weights={ (x,graph[x]): ((2 if x==0 else 1)/(q+1) if opt else 1/q)**.5 for x in F.vals }
    values=[]; count=Counter()
    zero_freq=0
    for u,v in itertools.product(F.vals,repeat=2):
      inter=[]
      for x in F.vals:
        x2=F.sub(x,u)
        if F.sub(graph[x],v)==graph[x2]:
            inter.append((x,graph[x],weights[(x,graph[x])]*weights[(x2,graph[x2])]))
      for alpha,beta in itertools.product(F.vals,repeat=2):
        a=sum(w*F.chi2(x,y,alpha,beta) for x,y,w in inter)
        if abs(a)<1e-8:kind='zero'
        elif abs(abs(a)-1)<1e-8:kind='one'
        elif abs(abs(a)-1/math.sqrt(q))<1e-8:kind='sqrt'
        elif abs(abs(a)-1/q)<1e-8:kind='small'
        else:kind='other'
        count[kind]+=1
        values.append((u,v,alpha,beta,a))
        if u==v==beta==0 and alpha!=0 and abs(a)<1e-8:zero_freq+=1
    return F,values,count,zero_freq

def run():
    for q in (3,5,7,9):
        F,unif,c,z=ambiguity_values(q)
        expected={'one':1, 'sqrt':q*(q-1), 'small':q**3*(q-1), 'zero':(q-1)*(q*q+1)}
        assert dict(c)==expected,(q,c,expected)
        assert z==q-1
        assert len(unif)==q**4
        _,opt,oc,_=ambiguity_values(q,opt=True)
        assert oc.get('zero',0)==(q-1)*q*q
        smallest=min(abs(a) for u,v,alpha,beta,a in opt if u!=0 or (u==v==0))
        bound=1/(q+1)
        assert abs(smallest-bound)<1e-8,(q,smallest,bound)
        largest=max(abs(a) for *_,a in opt)
        assert abs(largest-1)<1e-8
        forced=sum(abs(a)<1e-8 for u,v,alpha,beta,a in opt if u==0 and v!=0)
        assert forced==(q-1)*q*q
        print('PLANAR_OK',q,'unweighted',dict(c),'optimized_min',round(smallest,12),'unavoidable_zeros',forced)
    _,bad,c,_=ambiguity_values(5,opt=True,nonplanar=True)
    forced_extra=sum(abs(a)<1e-8 for u,v,alpha,beta,a in bad if u!=0)
    assert forced_extra>0
    print('NONPLANAR_OBSTRUCTION_OK q=5 extra_missing',forced_extra)

if __name__=='__main__':run()
