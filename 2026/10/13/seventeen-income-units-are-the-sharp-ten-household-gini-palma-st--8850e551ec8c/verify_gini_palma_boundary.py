#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
def parts(total,length):
    def rec(rem,k,low,prefix):
        if k==0:
            if rem==0: yield tuple(prefix)
            return
        for x in range(low,rem//k+1):
            yield from rec(rem-x,k-1,x,prefix+[x])
    yield from rec(total,length,1,[])
def gnum(x): return sum(b-a for a,b in combinations(x,2))
def palma(x): return Fraction(x[-1],sum(x[:4]))
pc={}; rc={}; wc={}; first=[]
for S in range(10,18):
    ps=list(parts(S,10)); pc[S]=len(ps); rev=[]; weak=[]
    for a,b in combinations(ps,2):
        dg=(gnum(a)>gnum(b))-(gnum(a)<gnum(b))
        dp=(palma(a)>palma(b))-(palma(a)<palma(b))
        if dg*dp<0: rev.append((a,b))
        if (dg==0)!=(dp==0) or dg*dp<0: weak.append((a,b))
    rc[S]=len(rev); wc[S]=len(weak)
    if S==17: first=rev
assert pc=={10:1,11:1,12:2,13:3,14:5,15:7,16:11,17:15}
assert rc=={10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:2}
assert wc=={10:0,11:0,12:0,13:0,14:1,15:2,16:9,17:17}
expected=[
((1,1,1,1,1,1,1,2,4,4),(1,1,1,1,1,1,2,2,2,5)),
((1,1,1,1,1,1,2,3,3,3),(1,1,1,1,1,2,2,2,2,4))]
assert first==expected
a,b=expected[0]
assert (gnum(a),gnum(b),palma(a),palma(b))==(53,51,Fraction(1),Fraction(5,4))
assert Fraction(gnum(a),170)==Fraction(53,170) and Fraction(gnum(b),170)==Fraction(3,10)
a,b=expected[1]
assert (gnum(a),gnum(b),palma(a),palma(b))==(45,43,Fraction(3,4),Fraction(1))
assert Fraction(gnum(a),170)==Fraction(9,34) and Fraction(gnum(b),170)==Fraction(43,170)
print("VERIFY_OK")
print("profile_counts",pc)
print("strict_reversal_counts",rc)
print("weak_disagreement_counts",wc)
print("first_strict_layer",expected)
