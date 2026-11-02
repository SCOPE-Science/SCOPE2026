#!/usr/bin/env python3
"""Standalone finite checks for single-marker subsequence coverage.
All universal quantifiers are proved in RESULT.md; finite checks are corroborative.
"""
from itertools import product, combinations
from math import isqrt, comb

def is_subsequence(target, host):
    j=0
    for ch in host:
        if j<len(target) and ch==target[j]:j+=1
    return j==len(target)

def literal_covers(host,k):
    return all(is_subsequence('0'*i+'1'+'0'*(k-1-i),host) for i in range(k))

def interval_covers(host,k):
    z=host.count('0');r=len(host)-z
    if z<k-1 or r==0:return False
    s=z-k+2
    xs=[];zeros=0
    for ch in host:
        if ch=='0':zeros+=1
        else:xs.append(zeros)
    return xs[0]<=s-1 and xs[-1]>=k-1 and all(xs[i+1]-xs[i]<=s for i in range(r-1))

def fixed_length(k,r):
    s=(k+r-1)//r
    return k-2+r+s

def global_length(k):
    root=isqrt(4*k)
    c=root if root*root==4*k else root+1
    return k-2+c

def polynomial_count(k,r):
    s=(k+r-1)//r;delta=r*s-k
    # coefficient of (1+...+y^(s-1))^2 (1+...+y^s)^(r-1)
    a=[1]+[0]*delta
    for hi in [s-1,s-1]+[s]*(r-1):
        b=[0]*(delta+1)
        for i,v in enumerate(a):
            for j in range(min(hi,delta-i)+1):b[i+j]+=v
        a=b
    return a[delta]

def witness(k,r):
    s=(k+r-1)//r;z=k-2+s
    xs=[min((j+1)*s-1,k-1) for j in range(r)]
    out=[];prev=0
    for x in xs:
        out+=['0'*(x-prev),'1'];prev=x
    out.append('0'*(z-prev))
    return ''.join(out)

def main():
    checked=0;mincounts={};polynomial_profiles=0
    # Exhaustively test every host at and below globally minimum length.
    for k in range(1,12):
        L=global_length(k);mn=0
        for n in range(L+1):
            for bits in product('01', repeat=n):
                w=''.join(bits)
                actual=literal_covers(w,k)
                assert actual==interval_covers(w,k),(k,w,actual)
                checked+=1
                if n<L:assert not actual,(k,w)
                elif actual:mn+=1
        by_formula=sum(polynomial_count(k,r) for r in range(1,L+1) if fixed_length(k,r)==L)
        assert mn==by_formula,(k,mn,by_formula)
        if isqrt(k)**2==k:assert mn==1
        mincounts[k]=mn
    # Exhaustively compare counts within every fixed-marker-composition optimum.
    for k in range(1,9):
        for r in range(1,k+3):
            L=fixed_length(k,r)
            if L>19:continue
            count=0
            for ids in combinations(range(L),r):
                pos=set(ids)
                w=''.join('1' if i in pos else '0' for i in range(L))
                if literal_covers(w,k):count+=1
            expect=polynomial_count(k,r)
            assert count==expect,(k,r,L,count,expect)
            polynomial_profiles+=1
    # Arithmetic and witness checks for large k; no exhaustive-string claim here.
    for k in range(1,2001):
        c=global_length(k)-k+2
        assert min(s+(k+s-1)//s for s in range(1,k+2))==c
        for r in (1,isqrt(k),isqrt(k)+1,k,k+3):
            w=witness(k,r)
            assert len(w)==fixed_length(k,r)
            assert interval_covers(w,k)
    print('VERIFY_OK checked_hosts=%d k_global=1..11 optimal_counts=%s fixed_marker_profiles=%d integer_witness_k=1..2000'%(checked,mincounts,polynomial_profiles))
if __name__=='__main__': main()
