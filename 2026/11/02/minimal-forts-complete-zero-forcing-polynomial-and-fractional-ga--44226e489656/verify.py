#!/usr/bin/env python3
"""Direct finite checks of a crown graph's minimal forts and forcing sets.

Standard library only.  Set subsets, forcing actions and packing recurrence are
recomputed directly from adjacency, not from the structural theorem.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


def adjacency(n):
    out=[]
    for vertex in range(2*n):
        neighbors=range(n,2*n) if vertex<n else range(n)
        out.append(sum(1<<w for w in neighbors if w % n != vertex % n))
    return out


def independent_minimal_forts(n):
    adjacent=adjacency(n)
    N=2*n
    ans=[]
    all_mask=(1<<N)-1
    for card in range(1,N+1):
        for index_tuple in combinations(range(N),card):
            mask=sum(1<<i for i in index_tuple)
            if any((mask&old)==old for old in ans):
                continue
            external=all_mask^mask
            if all((adjacent[v]&mask).bit_count()!=1
                   for v in range(N) if external>>v&1):
                ans.append(mask)
    return set(ans)


def formula_forts(n):
    result=set()
    for source in (0,n):
        for idx in combinations(range(n),3):
            result.add(sum(1<<(source+i) for i in idx))
    for i,j in combinations(range(n),2):
        result.add((1<<i)|(1<<j)|(1<<(n+i))|(1<<(n+j)))
    return result


def direct_zero_forcing(n,black):
    adjacent=adjacency(n)
    all_mask=(1<<(2*n))-1
    while black!=all_mask:
        newblack=black
        for v in range(2*n):
            if black>>v&1:
                outside=adjacent[v] & (all_mask^black)
                if outside and outside&(outside-1)==0:
                    newblack|=outside
        if newblack==black:
            return False
        black=newblack
    return True


def zero_forcing_polynomial(n):
    coeff=Counter()
    for mask in range(1<<(2*n)):
        if direct_zero_forcing(n,mask):
            coeff[mask.bit_count()]+=1
    return dict(sorted(coeff.items()))


def expected_zero_forcing_polynomial(n):
    c=comb(n,2)
    return {2*n-4:c*(c-1), 2*n-3:2*n*c,
            2*n-2:n*n+2*c, 2*n-1:2*n, 2*n:1}


def direct_packing(forts,n):
    N=2*n
    full=(1<<N)-1
    contain=[[] for _ in range(N)]
    for m in forts:
        for v in range(N):
            if m>>v&1:contain[v].append(m)
    @lru_cache(None)
    def dp(avail):
        if not avail:return 0
        v=(avail&-avail).bit_length()-1
        best=dp(avail & ~(1<<v))
        for m in contain[v]:
            if avail & m == m:
                best=max(best,1+dp(avail^m))
        return best
    return dp(full)


def lp_certificate(n,forts):
    # Every 3-subset in each shore gets dual weight 1/comb(n-1,2).
    # Every vertex has cumulative dual incident weight exactly one.
    shore3=[m for m in forts if m.bit_count()==3]
    total=sum(1 for m in shore3)
    degree=[sum(1 for f in shore3 if f>>v&1) for v in range(2*n)]
    assert degree==[comb(n-1,2)]*(2*n)
    assert total==2*comb(n,3)
    assert 3*total==2*n*comb(n-1,2)
    assert all(m.bit_count()>=3 for m in forts)


def main():
    for n in range(3,9):
        actual=independent_minimal_forts(n)
        expected=formula_forts(n)
        assert actual==expected, (n,actual^expected)
        assert len(actual)==2*comb(n,3)+comb(n,2)
        observed=zero_forcing_polynomial(n)
        predicted=expected_zero_forcing_polynomial(n)
        assert observed==predicted,(n,observed,predicted)
        lp_certificate(n,actual)
        if n<=7:
            pack=direct_packing(actual,n)
            assert pack==2*n//3,(n,pack)
        print('n=%d | minimal_forts=%d | zero_forcing=%s | fort_packing=%s | LP=2n/3' %
              (n,len(actual),observed,str(2*n//3) if n<=7 else 'not enumerated'))
    print('VERIFY_OK')

if __name__=='__main__':main()
