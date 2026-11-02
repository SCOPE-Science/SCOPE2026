#!/usr/bin/env python3
"""Exact small-case checks for Littlestone dimension of ideals of uniform weak orders.
No external dependencies. This is a finite check, not a proof of the all-parameter statement.
"""
from functools import lru_cache
from itertools import product

@lru_cache(None)
def poset_rank(profile):
    profile=tuple(x for x in profile if x)
    if not profile:return 0
    answer=0
    for i,v in enumerate(profile):
        left=profile[:i]+(v-1,)
        right=(v-1,)+profile[i+1:]
        answer=max(answer,1+min(poset_rank(left),poset_rank(right)))
    return answer

def concepts(r,h):
    levels=[tuple(range(j*r,(j+1)*r)) for j in range(h)]
    ans=set()
    for i in range(h):
        below=sum(1<<v for level in levels[:i] for v in level)
        for bits in range(1<<r):
            ans.add(below|sum(1<<v for j,v in enumerate(levels[i]) if bits>>j&1))
    return tuple(sorted(ans))

def direct_rank(r,h):
    universe=concepts(r,h)
    @lru_cache(None)
    def rec(items):
        if len(items)<=1:return 0
        best=0
        for v in range(r*h):
            no=tuple(c for c in items if not c&(1<<v))
            yes=tuple(c for c in items if c&(1<<v))
            if no and yes:
                best=max(best,1+min(rec(no),rec(yes)))
        return best
    return len(universe),rec(universe)

def vc_dimension(sets,n):
    from itertools import combinations
    for d in range(n,0,-1):
        for sub in combinations(range(n),d):
            signatures={sum(int(bool(c>>v&1))<<j for j,v in enumerate(sub)) for c in sets}
            if len(signatures)==1<<d:return d
    return 0

def main():
    cases=0; profile_cases=0;total_concepts=0
    for r in range(1,5):
        for h in range(1,9):
            expected=r-1+(h+1).bit_length()-1
            got=poset_rank((r,)*h)
            assert got==expected,('poset recurrence',r,h,got,expected)
            profile_cases+=1
            if r*h<=11:
                n,d=direct_rank(r,h)
                assert d==expected,('direct',r,h,n,d,expected)
                assert n==1+h*((1<<r)-1),(r,h,n)
                assert vc_dimension(concepts(r,h),r*h)==r,('VC',r,h)
                cases+=1;total_concepts+=n
    # Endpoint-truncation lemma: all endpoint widths smaller than the full width.
    endpoints=0
    for r in range(1,7):
        for t in range(0,13):
            bound=r-1+(t+1).bit_length()-1
            for a in range(r):
                for b in range(r):
                    profile=((a,) if a else ()) + (r,)*t + ((b,) if b else ())
                    got=poset_rank(profile)
                    assert got<=bound,('endpoints',r,t,a,b,got,bound)
                    endpoints+=1
    # Larger profiles: recursion checks that cross several binary thresholds.
    for r in (1,2,3,4,5,6):
        for h in range(1,22):
            d=poset_rank((r,)*h)
            assert d==r-1+(h+1).bit_length()-1,(r,h,d)
            profile_cases+=1
    print('UNIFORM_WEAK_ORDER_IDEAL_CHECKS_PASS',cases,profile_cases,endpoints,total_concepts)
if __name__=='__main__':main()
