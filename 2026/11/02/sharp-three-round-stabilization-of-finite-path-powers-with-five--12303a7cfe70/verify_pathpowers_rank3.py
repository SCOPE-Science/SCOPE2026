#!/usr/bin/env python3
"""Standalone finite checks for a theorem on rank-three path powers.
Exact q-types use the complete finite Ehrenfeucht--Fraisse recursion;
the separate arithmetic formulas encode third-vertex extension patterns.
The infinite theorem uses an elementary arithmetic proof, not this test range.
"""
from functools import lru_cache


def path_power(n,r):
    assert n>=r+2 and r>=1
    return tuple(tuple(0<int(abs(i-j))<=r for j in range(n)) for i in range(n))


def cycle_power(n,r):
    assert n>=2*r+2 and r>=1
    return tuple(tuple(i!=j and min(abs(i-j),n-abs(i-j))<=r for j in range(n)) for i in range(n))


class TypePool:
    def __init__(self):
        self.cache={}

    def intern(self,key):
        if key not in self.cache: self.cache[key]=len(self.cache)
        return self.cache[key]

    def type(self,adj,rounds=3):
        n=len(adj)
        @lru_cache(None)
        def rec(tup,r):
            if r==0:
                diagram=tuple((int(tup[i]==tup[j]),int(adj[tup[i]][tup[j]]))
                              for i in range(len(tup)) for j in range(i+1,len(tup)))
                return self.intern((0,len(tup),diagram))
            children=frozenset(rec(tup+(v,),r-1) for v in range(n))
            return self.intern((r,len(tup),children))
        return rec((),rounds)


def mask_direct(n,r,x,y):
    ans=0
    for z in range(1,n+1):
        if z not in (x,y):
            a=int(abs(x-z)<=r)
            b=int(abs(y-z)<=r)
            ans|=1<<(2*a+b)
    return ans


def mask_formula(n,r,x,y):
    assert 1<=x<y<=n and r>=2 and n>=4*r+3
    d=y-x
    p00=True
    p11=(d<=2*r)
    p10=(y>=r+2 and not (x==1 and y==r+2))
    p01=(x<=n-r-1 and not (x==n-r-1 and y==n))
    return int(p00)+2*int(p01)+4*int(p10)+8*int(p11)


def profiles(n,r):
    ans=[]
    for x in range(1,n+1):
        p=set()
        for y in range(1,n+1):
            if x!=y:
                if x<y: m=mask_formula(n,r,x,y)
                else:
                    m=mask_formula(n,r,y,x)
                    m=(m&9)|((m&2)<<1)|((m&4)>>1)
                p.add((int(abs(x-y)<=r),m))
        ans.append(frozenset(p))
    return ans


def expected_group(a,r):
    if a==0:return {(0,7),(0,11),(0,15),(1,11)}
    if a<r:return {(0,7),(0,15),(1,11),(1,13),(1,15)}
    if a==r:return {(0,7),(0,15),(1,13),(1,15)}
    if a==r+1:return {(0,7),(0,13),(0,15),(1,15)}
    return {(0,7),(0,15),(1,15)}


def verify():
    cnt=0
    for r in range(2,17):
        for n in range(4*r+3,4*r+9):
            v=profiles(n,r)
            for x in range(1,n+1):
                assert v[x-1]==expected_group(min(x-1,n-x),r),(n,r,x)
                for y in range(x+1,n+1):
                    assert mask_formula(n,r,x,y)==mask_direct(n,r,x,y),(n,r,x,y)
                    cnt+=1
    print('PAIR_FORMULA_AND_FIVE_TYPES_OK',cnt,'pairs across 90 graphs')

    pool=TypePool()
    reps=[(11,2),(15,3),(19,4),(23,5),(27,6)]
    typs=[pool.type(path_power(n,r)) for n,r in reps]
    assert len(set(typs))==1
    print('COMPLETE_THREE_ROUND_TAIL_OK',reps)

    for r in range(2,7):
        assert pool.type(path_power(4*r+2,r))!=typs[0]
    print('COMPLETE_THREE_ROUND_SHARPNESS_OK',[(4*r+2,r) for r in range(2,7)])

    small=[(n,r) for n in range(3,11) for r in range(1,n-1)]
    assert all(pool.type(path_power(n,r))!=typs[0] for n,r in small)
    print('MINIMAL_STABLE_REPRESENTATIVE_OK',len(small),'smaller graph parameter pairs')

    assert pool.type(cycle_power(11,2))!=typs[0]
    print('STABLE_CYCLE_FAMILY_SEPARATION_EXAMPLE_OK')
    print('EXACT_TYPE_POOL_SIZE',len(pool.cache))
    print('VERIFY_OK')

if __name__=='__main__': verify()
