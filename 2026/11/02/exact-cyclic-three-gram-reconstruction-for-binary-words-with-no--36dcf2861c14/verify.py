#!/usr/bin/env python3
"""Standalone finite corroboration for cyclic three-gram reconstruction with 010 forbidden.
Uses exact integer arithmetic and the definitions in RESULT.md; no external packages.
"""
from collections import defaultdict
from itertools import product
from math import comb, gcd

GRAMS=tuple(product((0,1), repeat=3))

def ph(k):
    return sum(gcd(i,k)==1 for i in range(1,k+1))

def choose(n,r):
    return comb(n,r) if n>=0 and 0<=r<=n else 0

def fiber(t,v,A,B):
    if not(1<=t and 0<=v<=t and A>=0 and B>=0):return 0
    if v==0 and A!=0:return 0
    g=gcd(gcd(t,v),gcd(A,B))
    sm=0
    for d in range(1,g+1):
        if g%d:continue
        a,b,c,e=t//d,v//d,A//d,B//d
        counts=choose(a,b)*(choose(c+b-1,b-1) if b else int(c==0))*choose(e+a-1,a-1)
        sm+=ph(d)*counts
    assert sm%t==0
    return sm//t

def theoretical(n):
    profiles={(n,0,0,0,0,0,0,0):1, (0,0,0,0,0,0,0,n):1}
    for t in range(1,n//3+1):
        for v in range(t+1):
            rem=n-3*t-v
            if rem<0:continue
            for A in range(rem+1):
                B=rem-A
                f=fiber(t,v,A,B)
                if f:
                    p=(A,v,0,t-v,t,t,v,B) # lex 000,001,010,011,100,101,110,111? see below
                    # Correct ordered vector: 000=A,001=v,010=0,011=t,
                    # 100=v,101=t-v,110=t,111=B.
                    p=(A,v,0,t,v,t-v,t,B)
                    assert p not in profiles
                    profiles[p]=f
    return profiles

def observed(n):
    profiles=defaultdict(set)
    for w in product((0,1),repeat=n):
        grams=[tuple(w[(i+j)%n] for j in range(3)) for i in range(n)]
        if (0,1,0) in grams:continue
        p=tuple(grams.count(g) for g in GRAMS)
        necklaces={tuple(w[k:]+w[:k]) for k in range(n)}
        profiles[p].add(min(necklaces))
    return {p:len(a) for p,a in profiles.items()}

def gf_C(n):
    out=2
    for t in range(1,n//3+1):
        if n>=3*t:out+=1
        for v in range(1,t+1):
            out+=max(0,n-3*t-v+1)
    return out

def gf_U(n):
    out=2+int(n>=3)+max(0,n-3)
    for t in range(2,n//3+1):
        out+=int(n in (3*t,3*t+1)) # v=0, B=0 or 1
        out+=int(n>=3*t+1)        # v=1, B=0, A arbitrary
        out+=int(n in (4*t,4*t+1))+(int(n==4*t+1))  # v=t, A+B<=1
        if t>=3:out+=int(n==4*t-1) # v=t-1 with no extras
    return out

def singleton(t,v,A,B):
    if t==1:return (v>0 or A==0)
    if t<1 or v<0 or v>t or A<0 or B<0:return False
    return ((v==0 and A==0 and B<=1) or
            (v==t and A+B<=1) or
            (v==1 and B==0) or
            (v==t-1 and A==B==0))

def main():
    literal_words=0; literal_profiles=0
    for n in range(1,19):
        a=observed(n);b=theoretical(n)
        assert a==b,(n,[(p,a.get(p),b.get(p)) for p in a.keys()|b.keys() if a.get(p)!=b.get(p)][:4])
        assert len(b)==gf_C(n)
        assert sum(v==1 for v in b.values())==gf_U(n)
        literal_words+=2**n
        literal_profiles+=len(a)
    for n in range(1,151):
        b=theoretical(n)
        assert len(b)==gf_C(n)
        assert sum(v==1 for v in b.values())==gf_U(n)
    for t in range(1,17):
        for v in range(t+1):
            for A in range(9):
                for B in range(9):
                    assert (fiber(t,v,A,B)==1)==singleton(t,v,A,B),(t,v,A,B)
    print('VERIFY_OK', 'literal_indexed_words='+str(literal_words),
          'literal_n=1..18', 'matched_profiles='+str(literal_profiles),
          'generating_functions_n=1..150', 'singleton_cases_checked='+str(sum((t+1)*81 for t in range(1,17))))
    print('COUNTS', [(n,len(theoretical(n)),sum(f==1 for f in theoretical(n).values())) for n in (8,9,10,12,18,24,36)])

if __name__=='__main__':main()
