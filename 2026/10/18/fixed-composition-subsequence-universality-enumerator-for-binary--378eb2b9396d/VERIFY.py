#!/usr/bin/env python3
"""Exact coefficient arithmetic for palindrome composition/universality counts."""
from collections import Counter
from itertools import product

def idx(s):
    t=set(); k=0
    for a in s:
        t.add(a)
        if len(t)==2:
            t.clear();k+=1
    return k

def brute_idx(s):
    for k in range(len(s)//2+1,0,-1):
        def exists(pattern):
            p=0
            for a in s:
                if a==pattern[p]:
                    p+=1
                    if p==len(pattern):return True
            return False
        if all(exists(p) for p in product('01',repeat=k)):
            return k
    return 0

# D(x,y,u) F(x,y,u) = N(x,y,u)
# triples (length, ones, index): coefficient
D={(0,0,0):1,(2,0,0):-1,(2,2,0):-1,(4,2,0):1,(4,2,2):-2,(6,2,2):1,(6,4,2):1}
N=Counter({(0,0,0):1,(4,2,0):-1,(1,0,0):1,(1,1,0):1,(3,1,1):1,(3,2,1):1,(3,1,0):-1,(3,2,0):-1,(5,2,1):-1,(5,3,1):-1})
# coefficients indexed (n,weight,index)
A=Counter()
for n in range(0,23):
    for wt in range(n+1):
        for k in range(n//2+1):
            z=N[(n,wt,k)]
            for (dn,dw,dk),coef in D.items():
                if dn==0:continue
                if n>=dn and wt>=dw and k>=dk:
                    z-=coef*A[(n-dn,wt-dw,k-dk)]
            if z:A[(n,wt,k)]=z
for n in range(0,21):
    B=Counter()
    for h in product('01',repeat=(n+1)//2):
        if n%2: s=''.join(h)+''.join(h[-2::-1]);
        else:s=''.join(h)+''.join(h[::-1]);
        r=idx(s)
        if n<=12:
            rr=brute_idx(s)
            assert r==rr,(n,s,r,rr)
        B[(n,s.count('1'),r)]+=1
    for (nn,wt,r),v in B.items():
        assert A[(nn,wt,r)]==v,('coefficient mismatch',nn,wt,r,A[(nn,wt,r)],v)
    for (nn,wt,r),v in A.items():
        if nn==n:assert B[(nn,wt,r)]==v,('extra coefficient',nn,wt,r,v)
    print(n, 'palindromes',sum(B.values()),'indices',dict(sorted(Counter({r:sum(v for (nn,wt,k),v in B.items() if k==r) for (nn,wt,r) in B}).items())))
print('VERIFY_OK_GF_ALL_COMPOSITION_LENGTHS_0_20_SUBSEQ_INDEPENDENT_0_12')
