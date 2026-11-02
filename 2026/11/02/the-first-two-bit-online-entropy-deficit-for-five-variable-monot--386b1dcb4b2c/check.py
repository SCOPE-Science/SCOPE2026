#!/usr/bin/env python3
"""Exact finite Littlestone upper bounds for order ideals of Boolean lattices.
Only Python standard library is required. All data are generated here.
"""
from functools import lru_cache
from math import comb

def ideals_by_dimension():
    layers=[[0,1]]  # downsets of the one-element Boolean lattice B_0
    for n in range(1,6):
        prior=layers[-1]
        shift=1<<(n-1)
        current=[a|(b<<shift) for a in prior for b in prior if (b&a)==b]
        assert len(set(current))==len(current)
        layers.append(current)
    return layers

def queries(ideals,n):
    N=len(ideals)
    out=[]
    for x in range(1<<n):
        mask=0
        for i,s in enumerate(ideals):
            if s>>x&1: mask|=1<<i
        out.append(mask)
    return out

def can_shatter(candidates,depth,queries,full):
    @lru_cache(None)
    def feasible(S,d):
        if d==0:return True
        if S.bit_count()<(1<<d):return False
        target=1<<(d-1)
        for q in queries:
            yes=S&q
            no=S&(full^q)
            if min(yes.bit_count(),no.bit_count())<target:continue
            if feasible(yes,d-1) and feasible(no,d-1):return True
        return False
    answer=feasible(candidates,depth)
    return answer,feasible.cache_info().currsize

def main():
    layers=ideals_by_dimension()
    expected=[2,3,6,20,168,7581]
    assert [len(x) for x in layers]==expected
    print('DEDEKIND_COUNTS_PASS',expected)
    for n in range(1,6):
        ideals=layers[n]; N=len(ideals); full=(1<<N)-1
        q=queries(ideals,n)
        # Independently verify the defining ideal condition on every generated word.
        for I in ideals:
            for x in range(1<<n):
                if I>>x&1:
                    for j in range(n):
                        if x>>j&1:assert I>>(x^(1<<j))&1
        width=comb(n,n//2)
        if n<5:
            yes,calls=can_shatter(full,width,q,full)
            no,upper_calls=can_shatter(full,width+1,q,full)
            assert yes and not no
            print('DIMENSION_PASS',n,'VC',width,'Ldim',width,'states',calls,upper_calls)
            continue
        # A fixed rank-two antichain of size ten is shattered by the ideals;
        # this supplies a complete adaptive depth-ten tree.
        assert sum(x.bit_count()==2 for x in range(1<<n))==width==10
        # For depth 11, a first query requires >=1024 candidates in both branches.
        # Ranks 0,1,4,5 have smaller side at most 168; remaining S5 orbits
        # are represented by x=3 (rank two) and x=7 (rank three).
        rank_counts={k:[] for k in range(n+1)}
        for x in range(1<<n):
            rank_counts[x.bit_count()].append(min(q[x].bit_count(),N-q[x].bit_count()))
        assert all(len(set(v))==1 for v in rank_counts.values())
        assert [rank_counts[k][0] for k in range(n+1)]==[1,168,2008,2008,168,1]
        for x,side in [(3,'no'),(7,'yes')]:
            S=(full^q[x]) if side=='no' else q[x]
            assert S.bit_count()==2008
            result,calls=can_shatter(S,10,q,full)
            assert result is False
            print('SMALL_BRANCH_DEPTH_TEN_EXCLUDED',x,side,'concepts',S.bit_count(),'states',calls)
        print('DIMENSION_PASS 5 VC 10 Ldim 10 entropy_bound 12')
    print('BOOLEAN_LATTICE_IDEALS_ALL_CHECKS_PASS')
if __name__=='__main__': main()
