#!/usr/bin/env python3
"""Generate five proposed irredundant domination types and independently test minimality."""
from itertools import combinations
from math import comb

def canonical(edge):
    return tuple(sorted(edge))

def template_families(n):
    U=tuple(range(n))
    for tri in combinations(U,3):
        yield 'triangle', frozenset(map(canonical,combinations(tri,2)))
    for six in combinations(U,6):
        a=six[0]
        def match(x):
            if not x:
                yield ()
            else:
                for index in range(1,len(x)):
                    for remaining in match(x[1:index]+x[index+1:]):
                        yield ((x[0],x[index]),)+remaining
        for matching in match(six):
            yield 'three_matching',frozenset(map(canonical,matching))
    for five in combinations(U,5):
        a=five[0]
        from itertools import permutations
        for q in permutations(five[1:]):
            if q[0]>q[-1]: continue
            cycle=(a,)+q
            yield 'five_cycle',frozenset(canonical((cycle[i],cycle[(i+1)%5])) for i in range(5))
    for v in U:
        yield 'full_star',frozenset(canonical((v,u)) for u in U if u!=v)
    for a,b in combinations(U,2):
        others=tuple(x for x in U if x not in (a,b))
        for A in combinations(others,2):
            for B in combinations((x for x in others if x not in A),2):
                yield 'balanced_double_star',frozenset((canonical((a,b)),)+tuple(canonical((a,x)) for x in A)+tuple(canonical((b,x)) for x in B))

def dominates(n,S):
    return all(e in S or any(not(set(e)&set(f)) for f in S)
               for e in combinations(range(n),2))

if __name__=='__main__':
    for n in range(5,10):
        F={};by_type={}
        for name,S in template_families(n):
            assert S not in F,(n,name,S)
            assert dominates(n,S),(n,name,S)
            assert all(not dominates(n,S-{e}) for e in S),(n,name,S)
            F[S]=name
            by_type[name]=by_type.get(name,0)+1
        expected={'triangle':comb(n,3),'three_matching':15*comb(n,6),
                  'five_cycle':12*comb(n,5),'full_star':n,
                  'balanced_double_star':comb(n,2)*comb(n-2,2)*comb(n-4,2)}
        assert all(by_type.get(k,0)==v for k,v in expected.items()),(n,by_type,expected)
        print('n',n,'total',len(F),'template_counts',sorted(by_type.items()))
    print('STRUCTURAL_CHECK_OK')
