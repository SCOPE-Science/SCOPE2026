#!/usr/bin/env python3
"""Finite independent spot checks for four-letter Green-geodesic classification."""
import itertools
from collections import defaultdict
A='pmuv'

def munn(word):
    pos=left=right=0
    for letter in word:
        if letter=='p':pos+=1
        elif letter=='m':pos-=1
        elif letter=='u':right=max(right,pos+1)
        elif letter=='v':left=min(left,pos-1)
        left=min(left,pos)
        right=max(right,pos)
    return (-left,right,pos)

def r_words(a,b):
    if a==b==0:return {''}
    if a==0:return {'p'*b,'p'*(b-1)+'u'}
    if b==0:return {'m'*a,'m'*(a-1)+'v'}
    s=set()
    if a<=b:
        s.add('m'*(a-1)+'v'+'p'*(a+b-1))
        s.add('m'*(a-1)+'v'+'p'*(a+b-2)+'u')
    if b<=a:
        s.add('p'*(b-1)+'u'+'m'*(a+b-1))
        s.add('p'*(b-1)+'u'+'m'*(a+b-2)+'v')
    return s

def d_words(n):
    if n==0:return {''}
    if n==1:return set(A)
    return {'p'*n,'m'*n,'p'*(n-1)+'u','m'*(n-1)+'v',
            'v'+'p'*(n-1),'u'+'m'*(n-1),
            'v'+'p'*(n-2)+'u','u'+'m'*(n-2)+'v'}

def inverse(word):
    return ''.join({'p':'m','m':'p','u':'u','v':'v'}[c] for c in word[::-1])

def r_length(a,b):
    return a+b if not a*b else a+b+min(a,b)-1

seen_R={};actual_R=defaultdict(set)
seen_D={};actual_D=defaultdict(set)
for n in range(10):
    for tup in itertools.product(A,repeat=n):
        word=''.join(tup)
        a,b,t=munn(word)
        rkey=(a,b);dkey=a+b
        if rkey not in seen_R:seen_R[rkey]=n
        if dkey not in seen_D:seen_D[dkey]=n
        if seen_R[rkey]==n:actual_R[rkey].add(word)
        if seen_D[dkey]==n:actual_D[dkey].add(word)
        # Inversion has left-root equal to the right-root of the inverse.
        ai,bi,ti=munn(inverse(word))
        assert (ai,bi)==(a+t,b-t), (word, (a,b,t),(ai,bi,ti))
    for (a,b),ell in seen_R.items():
        assert ell==r_length(a,b)
        assert actual_R[a,b]==r_words(a,b),((a,b),actual_R[a,b],r_words(a,b))
    for width,ell in seen_D.items():
        assert ell==width
        assert actual_D[width]==d_words(width)
    rcount=sum(x==n for x in seen_R.values())
    # Direct finite sums of rational-series geometric expansions.
    expected_classes=(1 if n==0 else 2)
    expected_words=(1 if n==0 else 4)
    for a in range(1,n+2):
        for b in range(1,n+2):
            if r_length(a,b)==n:
                expected_classes+=1
                expected_words+=4 if a==b else 2
    assert rcount==expected_classes,(n,rcount,expected_classes)
    assert sum(len(actual_R[k]) for k,ell in seen_R.items() if ell==n)==expected_words
    assert sum(len(actual_D[k]) for k,ell in seen_D.items() if ell==n)==(1 if n==0 else 4 if n==1 else 8)
print('GREEN_CLASS_FORMULAS_OK')
print('D_R_L_INVERSE_CORRESPONDENCE_OK')
print('TEN_COEFFICIENTS_OK')
print('VERIFY_OK')
