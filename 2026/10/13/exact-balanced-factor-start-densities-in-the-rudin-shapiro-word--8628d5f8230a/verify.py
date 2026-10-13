#!/usr/bin/env python3
"""Finite exact checks of the Rudin–Shapiro balanced-factor theorem.
Tests independent binary-digit generation, block descriptions, pair types,
all starts in long finite prefixes, and substitution prefix identities.
The unbounded theorem is proved by induction in RESULT.md.
"""
from collections import Counter
M = {'A':'AB','B':'AD','C':'CD','D':'CB'}
SIG = {'A':1,'B':1,'C':-1,'D':-1}

def expand(seed,steps):
    for _ in range(steps):
        seed = ''.join(M[x] for x in seed)
    return seed

def rudin_shapiro_sign(n):
    bits = bin(n)[2:]
    return (-1)**sum(bits[t:t+2]=='11' for t in range(len(bits)-1))

def prefix(word):
    acc=[0]
    for letter in word:acc.append(acc[-1]+SIG[letter])
    return acc

def offsets(k):
    assert k>=1
    base = {1+sum((1+2*((mask>>a)&1))*4**a for a in range(k-1))
               for mask in range(1<<(k-1))}
    return base,{2*4**(k-1)+t for t in base}

def wanted(xy,j,k):
    a,b=offsets(k)
    return ((xy in ('AD','BC','CB','DA') and j in a) or
            (xy in ('AB','CD') and j in b))

def check_blocks():
    for m in range(7):
        q=4**m;h=2**m
        pa=prefix(expand('A',2*m));pb=prefix(expand('B',2*m))
        assert len(pa)==q+1 and pa[-1]==pb[-1]==h
        assert all(0<x<=2*h-1 for x in pa[1:])
        assert all(0<x<=h for x in pb[1:])
        t={j for j in range(1,q+1) if pa[j]==h}
        assert t=={j for j in range(1,q+1) if pb[j]==h}
        assert t==offsets(m+1)[0]
        for x,y in [('A','C'),('B','D')]:
            assert all(SIG[v]==-SIG[w] for v,w in zip(expand(x,2*m),expand(y,2*m)))
    print('BLOCK_PREFIX_RECURRENCES_OK m=0..6')

def check_factors():
    n=2**17
    word=expand('A',17)
    assert len(word)==n
    assert all(SIG[ch]==rudin_shapiro_sign(i) for i,ch in enumerate(word))
    ps=prefix(word)
    present=set(word[t:t+2] for t in range(n-1))
    assert present==set(('AB','AD','BA','BC','CB','CD','DA','DC'))
    for k in range(1,7):
        length=4**k
        truecount=predcount=0
        off1,off2=offsets(k)
        for i in range(n-length+1):
            truth=(ps[i+length]==ps[i]); pred=wanted2(word[i//length:i//length+2],i%length,off1,off2)
            if truth!=pred:raise AssertionError(('factor_mismatch',k,i,truth,pred))
            truecount+=truth;predcount+=pred
        assert truecount==predcount
        print('FACTOR_OK k=%d length=%d balanced=%d starts=%d density_limit=%d/%d' %
              (k,length,truecount,n-length+1,3,8*(2**k)))

def wanted2(xy,j,a,b):
    return ((xy in ('AD','BC','CB','DA') and j in a) or
            (xy in ('AB','CD') and j in b))

if __name__=='__main__':
    check_blocks()
    check_factors()
    print('VERIFY_OK full_finite_classification_k=1..6 independent_RS_terms=131072')
