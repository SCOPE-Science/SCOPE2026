#!/usr/bin/env python3
"""Independent exact checks for the three-zero halving-partition deficit theorem."""
from functools import lru_cache

@lru_cache(None)
def stern(n):
    if n<=1: return n
    if n%2==0:return stern(n//2)
    return stern(n//2)+stern(n//2+1)

@lru_cache(None)
def generalized_chain(n, r=0):
    if r < -n: return 0
    if r == -n: return 1
    if n==1: return int(r >= -1)
    if n%2==0: return generalized_chain(n//2,r)
    return generalized_chain(n//2,r+1)+generalized_chain(n//2+1,r-1)

@lru_cache(None)
def direct_halving(n):
    @lru_cache(None)
    def complete(prev, rem):
        if rem==0: return 1
        if rem<0: return 0
        return sum(complete(t,rem-t) for t in {prev//2,(prev+1)//2} if t>0 and t<=rem)
    return complete(n,n)

def three_zeros(n):
    return n%2==1 and bin(n)[2:].count('0')==3

def runs(n):
    s=bin(n)[2:]
    return sum(c=='1' and (i==0 or s[i-1]=='0') for i,c in enumerate(s))

def hyperbinary_expansions(n):
    def dfs(position, remainder, digits):
        if 2**position>remainder:
            if remainder==0: yield tuple(digits)
            return
        place=2**position
        for e in (0,1,2):
            if e*place<=remainder:
                yield from dfs(position+1,remainder-e*place,digits+[e])
    return list(dfs(0,n,[]))

def admits_cut(e):
    width=len(e)
    for t in range(1,max(width+3,sum(e)+3)):
        if any(v==2 for v in e[t:]):continue
        L=sum(e[:t]); R=sum(v*2**(j-t) for j,v in enumerate(e) if j>=t)
        if 1+L+R-t==0: return True
    return False


def check():
    total=0; cases={1:0,2:0,3:0,4:0}
    for n in range(1,1<<16,2):
        if not three_zeros(n):continue
        d=stern(n)-generalized_chain(n,0)
        predicted=runs(n-1)
        assert d==predicted, (n,d,predicted)
        cases[d]+=1;total+=1
    assert total>500
    print('BINARY_ZERO_EXACT_OK', 'checked_odd_inputs',total,'deficit_histogram',cases)
    direct_count=0
    for n in range(1,1025):
        if n<=384:
            actual=direct_halving(n)
            assert actual==generalized_chain(n,0),(n,actual,generalized_chain(n,0))
            direct_count+=1
        if three_zeros(n):
            assert stern(n)-generalized_chain(n,0)==runs(n-1)
    print('DIRECT_HALVING_OK','inputs',direct_count)
    hypercases=0; admissible_count=0
    for n in range(17,257,2):
        if not three_zeros(n): continue
        e=hyperbinary_expansions(n-1)
        assert len(e)==stern(n), (n,len(e),stern(n))
        good=sum(map(admits_cut,e))
        assert good==direct_halving(n),(n,good,direct_halving(n))
        bad=len(e)-good
        assert bad==runs(n-1)
        hypercases+=1;admissible_count+=len(e)
    print('INDEPENDENT_HYPERBINARY_CUT_OK','inputs',hypercases,'expansions_examined',admissible_count)
    for n in [17,35,75,171]:
        assert three_zeros(n)
        print('EXAMPLE',n,'a',generalized_chain(n,0),'stern',stern(n),'deficit',stern(n)-generalized_chain(n,0),'ones_runs',runs(n-1))
    print('VERIFY_OK exact=True independent_methods=3 finite_only=True')

if __name__=='__main__': check()
