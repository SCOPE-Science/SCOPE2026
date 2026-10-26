#!/usr/bin/env python3
"""Finite checks for conjugacy-geodesic minima of free inverse monoids.
The data structures here are explicit finite trees; they are NOT an implementation
of the theoretical logarithmic-space algorithm proved in RESULT.md.
"""
from itertools import product
from collections import defaultdict

SIGMA='aAbB'
INV={'a':'A','A':'a','b':'B','B':'b'}

def reduce_word(w):
    st=[]
    for a in w:
        if st and INV[a]==st[-1]: st.pop()
        else:st.append(a)
    return ''.join(st)

def inv(w):return ''.join(INV[c] for c in w[::-1])
def mul(u,v):return reduce_word(u+v)
def dis(u,v):return mul(inv(u),v)

def path(w):
    cur='';v=['']
    for a in w:
        cur=mul(cur,a);v.append(cur)
    return v

def invariant(w):
    vs=path(w); uniq=set(vs)
    e=len(uniq)-1
    mx=0
    for u in uniq:
        for v in uniq:
            if dis('',u)==dis(vs[-1],v):
                mx=max(mx,len(dis(u,v)))
    return 2*e-mx, 2*e-len(dis('',vs[-1])), e, mx

def canonical(w):
    vs=path(w); V=set(vs)
    cases=[]
    for a in V:
        transformed=tuple(sorted((dis(a,x) for x in V)))
        cases.append((transformed,dis(a,''),dis(a,vs[-1])))
    return min(cases)

def runs(limit=6):
    words=[]
    by_shape=defaultdict(list)
    for n in range(limit+1):
        for v in product(SIGMA,repeat=n):
            w=''.join(v)
            can=canonical(w)
            by_shape[can[0]].append((can[1],can[2],n))
            words.append((w,can))
    totals=0
    shorter=[]
    for w,(shape,p,q) in words:
        M,g,E,L=invariant(w)
        assert len(w)>=M
        assert len(w)>=g
        assert 0<=M<=g<=len(w)
        found=min(n for a,b,n in by_shape[shape] if dis(p,a)==dis(q,b))
        assert M==found,(w,M,found,shape,p,q)
        totals+=1
        if g==len(w) and M<len(w):shorter.append((w,M,len(w),E,L))
    print('VERIFY_OK', 'rank=2', 'exhaustive_word_length<=',limit,'tested_words=',totals,'distinct_shape_classes=',len(by_shape),'geodesics_shortened_by_conjugacy=',len(shorter))
    if shorter:print('SAMPLE_SHORTENING',shorter[0])

if __name__=='__main__':runs(6)
