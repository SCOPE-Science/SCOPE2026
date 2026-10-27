"""Direct exhaustive finite checks for full chain-type majorization of nilpotent partial injections.
All calculations use only the Python standard library.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import comb


def nonempty_compositions(n, k):
    for cuts in combinations(range(1, n), k-1):
        positions=(0,)+cuts+(n,)
        yield tuple(positions[i+1]-positions[i] for i in range(k))

@lru_cache(None)
def profile_by_recursion(sizes):
    """Remove chain containing a distinguished vertex of the first nonempty level."""
    k=len(sizes)
    if not any(sizes):
        return {(0,)*k:1}
    i=next(j for j,a in enumerate(sizes) if a)
    others=[j for j in range(k) if j != i and sizes[j]>0]
    answer=Counter()
    for t in range(len(others)+1):
        for chosen in combinations(others,t):
            indices=(i,)+chosen
            choices=1
            new=list(sizes)
            for j in indices:
                if j != i: choices*=sizes[j]
                new[j]-=1
            for prof,number in profile_by_recursion(tuple(new)).items():
                updated=list(prof)
                updated[t]+=1  # chain has t+1 vertices
                answer[tuple(updated)]+=choices*number
    return dict(answer)


def all_partial_injections(n):
    points=tuple(range(n))
    for r in range(n+1):
        for dom in combinations(points,r):
            for im in combinations(points,r):
                for images in permutations(im):
                    f=[-1]*n
                    for u,v in zip(dom,images): f[u]=v
                    yield tuple(f)


def chain_type(f,k):
    n=len(f)
    has_incoming=[False]*n
    for image in f:
        if image>=0: has_incoming[image]=True
    result=[0]*k
    seen=set()
    for start in range(n):
        if has_incoming[start]: continue
        cur=start
        length=0
        while cur>=0:
            assert cur not in seen, 'a cycle or branch was encountered'
            seen.add(cur)
            length+=1
            cur=f[cur]
        assert 1<=length<=k
        result[length-1]+=1
    assert len(seen)==n
    return tuple(result)


def verify():
    brute_profiles=0
    checked_shapes=0
    max_compositions=0
    for n in range(1,7):
        for k in range(1,min(4,n)+1):
            for sizes in nonempty_compositions(n,k):
                level=tuple(j for j,size in enumerate(sizes) for _ in range(size))
                actual=Counter()
                for f in all_partial_injections(n):
                    if any(level[i]>=level[v] for i,v in enumerate(f) if v>=0):
                        continue
                    actual[chain_type(f,k)]+=1
                expected=profile_by_recursion(sizes)
                assert dict(actual)==expected,(n,k,sizes,actual,expected)
                brute_profiles+=sum(actual.values())
                checked_shapes+=len(actual)
                max_compositions+=1
    dominate=0
    strict=0
    for n in range(2,12):
        for k in range(2,min(5,n)+1):
            q,r=divmod(n,k)
            balanced=(q,)*(k-r)+(q+1,)*r
            best=profile_by_recursion(balanced)
            for sizes in nonempty_compositions(n,k):
                current=profile_by_recursion(sizes)
                for profile,value in current.items():
                    assert value<=best.get(profile,0),(n,k,sizes,profile,value,best.get(profile,0))
                    dominate+=1
                if max(sizes)-min(sizes)>1:
                    # For one length-2 chain and n-2 isolated vertices,
                    # the coefficient equals sum of cross-block pairs.
                    prof=(n-2,1)+(0,)*(k-2)
                    assert current.get(prof,0)<best.get(prof,0)
                    strict+=1
    print('VERIFY_OK_FULL_CHAIN_TYPE_DOMINANCE')
    print('brute_elements',brute_profiles,'profile_cells',checked_shapes,'layer_compositions',max_compositions)
    print('coefficient_dominance_checks',dominate,'strict_unbalanced_cases',strict)

if __name__ == '__main__': verify()
