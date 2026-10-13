#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import comb

D=2
NMAX=11
EXPECTED_SOURCE=(1,1,1,2,3,4,6,9,13,19)  # n=2..11
EXPECTED_OPT=(1,1,1,1,1,1,2,2,3,4)
EXPECTED_MAX_COUNTS=(1,1,1,2,3,4,1,6,3,3)
EXPECTED_MAX11={
    frozenset(['00000000000','00000100100','00010001000','00100100000']),
    frozenset(['00000000000','00001000100','00010010000','00100001000']),
    frozenset(['00000000000','00001001000','00010000100','00100010000']),
}

def rll_source(n,d=D):
    out=[]
    for tup in product('01', repeat=n):
        s=''.join(tup)
        if s[0]!='0' or s[-1]!='0':
            continue
        runs=[]
        ch=s[0]; length=1
        for c in s[1:]:
            if c==ch:
                length+=1
            else:
                runs.append((ch,length)); ch=c; length=1
        runs.append((ch,length))
        if any(ch=='1' and length!=1 for ch,length in runs):
            continue
        if any(ch=='0' and length<d for ch,length in runs):
            continue
        out.append(s)
    return tuple(out)

def shadow1(s):
    return frozenset(s[:i]+s[i+1:] for i in range(len(s)))

def lcs(a,b):
    dp=[0]*(len(b)+1)
    for ca in a:
        diagonal=0
        for j,cb in enumerate(b,1):
            old=dp[j]
            if ca==cb:
                dp[j]=diagonal+1
            else:
                dp[j]=max(dp[j],dp[j-1])
            diagonal=old
    return dp[-1]

def all_optima(n):
    V=rll_source(n)
    sh={x:shadow1(x) for x in V}
    def compatible(x,y):
        return sh[x].isdisjoint(sh[y])
    # Independent pairwise criterion: common one-deletion descendant iff LCS >= n-1.
    for x,y in combinations(V,2):
        assert compatible(x,y) == (lcs(x,y) <= n-2), (n,x,y)
    best=0; opt=()
    for k in range(1,len(V)+1):
        good=[]
        for C in combinations(V,k):
            if all(compatible(x,y) for x,y in combinations(C,2)):
                good.append(frozenset(C))
        if not good:
            # Any larger code would contain a k-subset, so failure here is an exhaustive upper bound.
            break
        best=k; opt=tuple(good)
    return V,sh,best,opt

def kk_bound(n,d=D):
    # Kulkarni--Kiyavash Theorem V.2, equation (27).
    rb=(n-1-d)//(d+1)
    rbp=(n-d)//(d+1)
    val=Fraction(0,1)
    for r in range(rb+1):
        top=n-2-r-(d-1)*(r+1)
        if 0 <= r <= top:
            val += Fraction(comb(top,r),2*r+1)
    for r in range(1,rbp+1):
        top=n-2-r-(d-1)*(r+1)
        if 0 <= r-1 <= top:
            val += Fraction((r+1)*comb(top,r-1),2*r+1)
    return val

source_sizes=[]; opt_sizes=[]; opt_counts=[]; cache={}
for n in range(2,NMAX+1):
    V,sh,best,opt=all_optima(n)
    cache[n]=(V,sh,best,opt)
    source_sizes.append(len(V)); opt_sizes.append(best); opt_counts.append(len(opt))
assert tuple(source_sizes)==EXPECTED_SOURCE, source_sizes
assert tuple(opt_sizes)==EXPECTED_OPT, opt_sizes
assert tuple(opt_counts)==EXPECTED_MAX_COUNTS, opt_counts

V,sh,best,opt=cache[11]
M=set(opt)
assert M==EXPECTED_MAX11, M
assert best==4 and len(M)==3
core=set.intersection(*(set(C) for C in M))
assert core=={'00000000000'}
for C in M:
    assert '00000000000' in C
    nonzero=C-{'00000000000'}
    assert all(x.count('1')==2 for x in nonzero)
    assert sorted(len(sh[x]) for x in C)==[1,5,5,5]
    assert len(set().union(*(sh[x] for x in C)))==16
# Reversal is a source/channel symmetry; one maximum is fixed and the other two are interchanged.
rev=lambda C:frozenset(x[::-1] for x in C)
assert all(rev(C) in M for C in M)
fixed=sum(rev(C)==C for C in M)
assert fixed==1
orbits=[]; seen=set()
for C in M:
    if C in seen: continue
    O={C,rev(C)}; seen|=O; orbits.append(len(O))
assert Counter(orbits)==Counter({1:1,2:1})

b=kk_bound(11,2)
assert b==Fraction(823,105)
assert int(b)==7

print('VERIFY_OK',
      'd=2',
      'n=2..11',
      'source_sizes='+','.join(map(str,source_sizes)),
      'optima='+','.join(map(str,opt_sizes)),
      'maximizer_counts='+','.join(map(str,opt_counts)),
      'n11_source=19',
      'n11_maximum=4',
      'n11_labeled_maxima=3',
      'n11_core=00000000000',
      'n11_shadow_profile=1,5,5,5',
      'n11_covered_outputs=16',
      'reversal_orbits=1,2',
      'KK_bound_n11=823/105_floor7')
for C in sorted(M,key=lambda C:sorted(C)):
    print('MAX11',','.join(sorted(C)))
