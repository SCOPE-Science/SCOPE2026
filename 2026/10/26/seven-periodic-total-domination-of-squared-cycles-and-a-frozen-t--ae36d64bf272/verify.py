"""Self-contained independent verification of total domination in squared cycles."""
from itertools import combinations
from math import gcd

def gap_test(n,S):
    a=sorted(S)
    d=[(a[(i+1)%len(a)]-a[i])%n for i in range(len(a))]
    return all(1<=x<=5 for x in d) and all(d[i]<=2 or d[(i+1)%len(d)]<=2 for i in range(len(d)))

def direct(n,S):
    return all(any(((v+s)%n) in S for s in (-2,-1,1,2)) for v in range(n))

def expected_gamma(n):
    k,r=divmod(n,7)
    return 2*k+(0 if r==0 else 1 if r<=2 else 2)

def full_check(n):
    t=expected_gamma(n)
    for j in range(1,t):
        for q in combinations(range(n),j):
            assert not direct(n,set(q)),(n,j,q)
    states=set()
    for q in combinations(range(n),t):
        s=frozenset(q)
        assert direct(n,s)==gap_test(n,s),(n,q)
        if direct(n,s): states.add(s)
    edges=set(); neighbors={s:set() for s in states}
    for s in states:
        for x in s:
            for y in range(n):
                if y in s:continue
                z=s.difference((x,)).union((y,))
                if z in states:neighbors[s].add(z);edges.add(frozenset((s,z)))
    if n%7==0:
        assert len(states)==7,(n,len(states))
        if n==7:assert len(edges)==7 and all(len(neighbors[s])==2 for s in states)
        else:assert len(edges)==0
    if n%7==2:
        assert len(states)==n and len(edges)==n and all(len(neighbors[s])==2 for s in states)
        base=next(iter(states))
        assert all(frozenset((a+7)%n for a in base)!=base for _ in [0])
        for s in states:
            predicted={frozenset((a+7)%n for a in s),frozenset((a-7)%n for a in s)}
            assert neighbors[s]==predicted,(n,s,neighbors[s],predicted)
    print('EXHAUSTIVE_OK',n,'gamma',t,'minima',len(states),'exchange_edges',len(edges))

for n in range(7,24):
    # n 22 would inspect 22 choose 7, acceptable as small finite test
    full_check(n)
print('ALL_VERIFY_OK')
