#!/usr/bin/env python3
"""Exact finite overlap certificate and independent text census for four-bit patterns."""
from itertools import combinations, product
from math import comb
from fractions import Fraction

CLASSES = {
    '0000': (1,20,90,140,70),
    '0001': (1,14,60,110,70),
    '0011': (1,12,56,104,70),
    '0010': (1,10,44,94,70),
    '0110': (1,10,42,84,70),
    '0101': (1,8,36,80,70),
}

def overlap_counts(pattern):
    result=[]
    for t in range(4,9):
        count=0
        for first in combinations(range(t),4):
            dfirst={v:j for j,v in enumerate(first)}
            firstset=set(first)
            for second in combinations(range(t),4):
                if len(firstset.union(second))!=t: continue
                if all(pattern[dfirst[v]]==pattern[j] for j,v in enumerate(second) if v in firstset):
                    count+=1
        result.append(count)
    return tuple(result)

def orbit(pattern):
    return {pattern,pattern[::-1],''.join('1' if c=='0' else '0' for c in pattern),''.join('1' if c=='0' else '0' for c in pattern[::-1])}

def subseq_count(text,pattern):
    dp=[1,0,0,0,0]
    for ch in text:
        for k in range(4,0,-1):
            if ch==pattern[k-1]: dp[k]+=dp[k-1]
    return dp[4]

def moment_variance(n,coeff):
    ez2=sum(Fraction(c*comb(n,t),2**t) for t,c in enumerate(coeff,4) if n>=t)
    return ez2-Fraction(comb(n,4)**2,256)

def check():
    patterns={''.join(b) for b in product('01',repeat=4)}
    for p,coeff in CLASSES.items():
        assert overlap_counts(p)==coeff,(p,overlap_counts(p),coeff)
        for equivalent in orbit(p):
            assert overlap_counts(equivalent)==coeff
        patterns-=orbit(p)
    assert not patterns, patterns
    ordered=list(CLASSES)
    assert all(CLASSES[ordered[i]][t]>=CLASSES[ordered[i+1]][t] for i in range(5) for t in range(5))
    for i in range(5):
        assert any(CLASSES[ordered[i]][t]>CLASSES[ordered[i+1]][t] for t in [1,2,3])
    assert [moment_variance(4,CLASSES[p]) for p in ordered]==[Fraction(15,256)]*6
    assert moment_variance(5,CLASSES['0010'])==moment_variance(5,CLASSES['0110'])
    for n in range(4,12):
        texts=list(product('01',repeat=n))
        for p in ordered:
            ct=[subseq_count(t,p) for t in texts]
            mean=Fraction(sum(ct),len(ct))
            variance=Fraction(sum(x*x for x in ct),len(ct))-mean*mean
            assert mean==Fraction(comb(n,4),16)
            assert variance==moment_variance(n,CLASSES[p]),(n,p,variance,moment_variance(n,CLASSES[p]))
    print('VERIFY_OK: six symmetry classes, 30 overlap coefficients, 8 exhaustive word-length censuses, exact moment and strict-order checks')

if __name__=='__main__': check()
