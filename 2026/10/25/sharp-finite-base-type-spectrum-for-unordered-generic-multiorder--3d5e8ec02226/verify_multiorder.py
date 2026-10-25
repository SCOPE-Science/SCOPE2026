#!/usr/bin/env python3
"""Finite orbit checks for unordered generic multiorders; independent signed-coordinate action."""
from itertools import permutations, product, combinations_with_replacement
from collections import Counter
from math import comb, factorial

def rev(p):return p[::-1]
def canon(p):return min(p,rev(p))
def predicted(patterns):
    m=len(patterns[0]); r=Counter(canon(p) for p in patterns)
    return 1 if m==1 else __import__('math').prod(comb(m+v,v) for v in r.values())
def orbit_count(patterns):
    m=len(patterns[0]); d=len(patterns)
    group=[]
    for sigma in permutations(range(d)):
        if m==1:
            for signs in product((0,1),repeat=d):group.append((sigma,signs))
            continue
        signs=[]
        for i,j in enumerate(sigma):
            if patterns[i]==patterns[j]:signs.append(0)
            elif patterns[i]==rev(patterns[j]): signs.append(1)
            else:break
        else:group.append((sigma,tuple(signs)))
    assert group
    def images(v):
        return [tuple((m-v[sigma[i]]) if signs[i] else v[sigma[i]] for i in range(d)) for sigma,signs in group]
    orbits={min(images(v)) for v in product(range(m+1),repeat=d)}
    return len(orbits),len(group)

tests=0; checks=0
for m,d in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3)]:
    pats=sorted({canon(p) for p in permutations(range(m))})
    seen=[]
    for cs in combinations_with_replacement(pats,d):
        seen.append(cs)
        # Check orientation twists at odd positions, independently of classification.
        for variant in range(2 if m>=2 else 1):
            pp=tuple(rev(p) if (variant and i%2==0) else p for i,p in enumerate(cs))
            actual,size=orbit_count(pp)
            expected=predicted(pp)
            r=Counter(canon(p) for p in pp)
            assert actual==expected,(m,d,pp,actual,expected)
            assert size==(2**d*factorial(d) if m==1 else __import__('math').prod(factorial(v) for v in r.values())),(m,d,pp,size)
            tests+=1
    low=min(predicted(x) for x in seen)
    high=max(predicted(x) for x in seen)
    K=len(pats)
    q,s=divmod(d,K)
    expected_min=comb(m+d,d) if m>1 else 1
    expected_max=(comb(m+q,q)**(K-s)*comb(m+q+1,q+1)**s) if m>1 else 1
    assert low==expected_min and high==expected_max,(m,d,low,high,expected_min,expected_max)
    checks+=1
    print('m',m,'d',d,'patterns',len(seen),'type-action tests',tests,'min',low,'max',high)
print('ALL_CHECKS_PASS; type_action_instances=',tests,'extremal_instances=',checks)
