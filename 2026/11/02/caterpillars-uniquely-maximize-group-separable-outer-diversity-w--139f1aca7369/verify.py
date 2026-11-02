"""Exact reproducibility checks for a group-separable domain theorem."""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb

LEAF = '*'

@lru_cache(None)
def invdist(a,b):
    if not a or not b: return {0:1}
    z=defaultdict(int)
    for k,c in invdist(a-1,b).items(): z[k+b]+=c
    for k,c in invdist(a,b-1).items(): z[k]+=c
    return dict(z)

@lru_cache(None)
def g(a,b):
    p=invdist(a,b)
    assert sum(p.values())==comb(a+b,a)
    return F(sum(min(u,a*b-u)*c for u,c in p.items()),comb(a+b,a))

@lru_cache(None)
def leaves(t):
    return 1 if t==LEAF else leaves(t[0])+leaves(t[1])

@lru_cache(None)
def cost(t):
    if t==LEAF:return F(0)
    return cost(t[0])+cost(t[1])+g(leaves(t[0]),leaves(t[1]))

@lru_cache(None)
def shapes(n):
    if n==1:return (LEAF,)
    out=set()
    for a in range(1,n//2+1):
        b=n-a
        for l in shapes(a):
            for r in shapes(b):
                if a==b and repr(l)>repr(r):continue
                out.add((l,r))
    return tuple(sorted(out,key=repr))

@lru_cache(None)
def cat(n):
    return LEAF if n==1 else (LEAF,cat(n-1))

@lru_cache(None)
def f(n):
    return sum((g(1,k) for k in range(1,n)),F(0))

def is_cat(t):
    if t==LEAF:return True
    a,b=t
    return (a==LEAF and is_cat(b)) or (b==LEAF and is_cat(a))

def min_branch_count(t):
    if t==LEAF:return 0
    a,b=t
    return (leaves(a)>=2 and leaves(b)>=2)+min_branch_count(a)+min_branch_count(b)

def core_shaped(t):
    if t==LEAF:return False
    a,b=t
    if leaves(a)==leaves(b)==2:
        return a==(LEAF,LEAF) and b==(LEAF,LEAF)
    if a==LEAF:return core_shaped(b)
    if b==LEAF:return core_shaped(a)
    return False

def frontiers(t,start=0):
    if t==LEAF:return ((start,),)
    a,b=t
    left=frontiers(a,start)
    right=frontiers(b,start+leaves(a))
    return tuple(x+y for x in left for y in right)+tuple(y+x for x in left for y in right)

def kendall(p,q):
    idx={x:i for i,x in enumerate(q)}
    return sum(idx[p[i]]>idx[p[j]] for i in range(len(p)) for j in range(i+1,len(p)))

def brute(t):
    n=leaves(t)
    domain=frontiers(t)
    return F(sum(min(kendall(p,q) for q in domain) for p in permutations(range(n))),__import__('math').factorial(n))

def main():
    assert [(g(a,b),a,b) for a,b in [(2,2),(2,3),(2,4),(2,5),(3,3)]]==[
        (F(1),2,2),(F(8,5),2,3),(F(34,15),2,4),(F(61,21),2,5),(F(13,5),3,3)]
    direct_checks=0
    for a in range(1,9):
        for b in range(1,9):
            n=a+b
            ds=[min(sum(p-(i+1) for i,p in enumerate(pos)),a*b-sum(p-(i+1) for i,p in enumerate(pos))) for pos in combinations(range(1,n+1),a)]
            assert g(a,b)==F(sum(ds),len(ds))
            direct_checks+=1
    print('Independent interleaving enumeration checks:',direct_checks)
    checks=0
    for a in range(2,26):
        for b in range(a,26):
            assert g(a,b)>=F(a*b,4)
            assert (g(a,b)==F(a*b,4))==((a,b)==(2,2))
            if 3*a*b>=4*(a+b+1):
                assert g(a,b)>=F(a*b,4)
            checks+=1
    print('Cross-inversion bounds checked:',checks)
    for n in range(2,15):
        cc=shapes(n)
        best=min(cost(t) for t in cc)
        tops=[t for t in cc if cost(t)==best]
        assert best==f(n)
        # n-1 has floor((n-1)/2) even indices: 2,4,...
        harmonic=sum((F(1,2*j+1) for j in range(1,(n-1)//2+1)),F(0))
        assert f(n)==F((n-1)*(n-2),8)+harmonic/4
        assert len(tops)==1 and is_cat(tops[0])
        if n>=4:
            second=min(cost(t) for t in cc if not is_cat(t))
            optsec=[t for t in cc if not is_cat(t) and cost(t)==second]
            assert second-best==F(1,6)
            assert len(optsec)==1 and core_shaped(optsec[0])
        print('n',n,'shapes',len(cc),'best',best,'second_gap',str(second-best) if n>=4 else 'N/A')
    for n in range(2,7):
        for t in shapes(n):
            assert brute(t)==cost(t),(n,t,brute(t),cost(t))
        print('Direct permutation-versus-DP verified for all shapes at n=',n)
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
