#!/usr/bin/env python3
"""Independent Boolean-depth obstruction evaluator for comparison classes."""
from verify import concepts,matrix
from functools import lru_cache

def exists_full_tree(masks,S,d):
    @lru_cache(maxsize=None)
    def deep(state,remaining):
        if remaining==0:return True
        if state.bit_count()<(1<<remaining):return False
        for M in masks:
            A=state&M;B=state^A
            if (A.bit_count() >= 1<<(remaining-1)
                and B.bit_count() >= 1<<(remaining-1)
                and deep(A,remaining-1) and deep(B,remaining-1)):
                return True
        return False
    ans=deep(S,d)
    return ans,deep.cache_info().currsize

if __name__=='__main__':
    for n,d,expected in ((11,7,True),(11,8,False),(12,8,True),(12,9,False)):
        C=concepts(n)
        queries,masks=matrix(C)
        split_minority=max(min(M.bit_count(),len(C)-M.bit_count()) for M in masks)
        if n==11:assert split_minority==126
        if n==12:assert split_minority==252
        yes,states=exists_full_tree(masks,(1<<len(C))-1,d)
        assert yes is expected,(n,d,yes)
        print('DEPTH_BOOLEAN_RECHECK_PASS',n,'depth',d,'exists',yes,'minority_max',split_minority,'states',states,flush=True)
    print('INDEPENDENT_BOOLEAN_DEPTH_RECHECK_ALL_PASS')
