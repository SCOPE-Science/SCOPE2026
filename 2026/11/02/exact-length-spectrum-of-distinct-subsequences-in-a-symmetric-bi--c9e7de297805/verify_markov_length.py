#!/usr/bin/env python3
"""Exact finite verification of a binary Markov subsequence-spectrum formula.
Uses independently enumerated word probabilities and distinct scattered subsequence sets.
Standard library only. The proof of the all-n rational identity is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter

def clean(p):
    return {i:c for i,c in p.items() if c}
def add(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,0)+v
    return clean(c)
def mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
    return clean(c)
def neg(p):return {i:-v for i,v in p.items()}

def from_rational(r,nmax):
    # (1-z)(1-(1-r+t)z+t(1-2r)z^2) * sum S_n z^n
    #                = t z - t(1-2r)z^2.
    denominator={1:{0:r-2,1:-1},2:{0:1-r,1:2*(1-r)},3:{1:-(1-2*r)}}
    numerator={1:{1:Q(1)},2:{1:-(1-2*r)}}
    coefs=[]
    for n in range(nmax+1):
        curr=dict(numerator.get(n,{}))
        for j,d in denominator.items():
            if n>=j:curr=add(curr,neg(mul(d,coefs[n-j])))
        coefs.append(curr)
    return coefs

def literal(r,n):
    ans={}
    for word in product('01',repeat=n):
        flips=sum(word[i]!=word[i-1] for i in range(1,n))
        prob=Q(1,2)*r**flips*(1-r)**(n-1-flips)
        seen={''}
        for ch in word:
            seen |= {s+ch for s in seen}
        for l,m in Counter(map(len,seen- {''})).items():
            ans[l]=ans.get(l,0)+prob*m
    return clean(ans)

def test():
    rlist=[Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]
    wordcases=0;length_coefficients=0
    for r in rlist:
        seq=from_rational(r,10)
        assert not seq[0]
        for n in range(1,11):
            observed=literal(r,n)
            if observed!=seq[n]:raise AssertionError((r,n,observed,seq[n]))
            wordcases+=2**n
            length_coefficients+=n
        if r==0:
            for n in range(1,11):assert seq[n]=={i:Q(1) for i in range(1,n+1)}
    # IID fair case: E distinct nonempty words = 2(3/2)^n - 2.
    seq=from_rational(Q(1,2),10)
    for n in range(1,11):assert sum(seq[n].values())==2*Q(3,2)**n-2
    print('VERIFY_OK switch_parameters=%d n_range=1..10 enumerated_host_words=%d checked_length_coefficients=%d fair_iid_and_constant_boundaries=TRUE' %(len(rlist),wordcases,length_coefficients))
if __name__=='__main__':test()
