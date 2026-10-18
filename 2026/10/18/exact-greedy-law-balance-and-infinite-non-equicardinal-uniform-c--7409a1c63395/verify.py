"""Exhaustive consistency checks for greedy maximal independent sets on clique bouquets."""
from itertools import permutations, product
from fractions import Fraction
from collections import Counter
from math import factorial, prod

def case(sizes):
    blades=[]; p=1
    for m in sizes:
        blades.append(tuple(range(p,p+m))); p+=m
    n=p; adj=[set(range(1,n))]+[set([0]) for _ in range(n-1)]
    for blade in blades:
        for x in blade:
            adj[x].update(y for y in blade if y!=x)
    freq=Counter()
    for order in permutations(range(n)):
        picked=set()
        for v in order:
            if not adj[v]&picked:picked.add(v)
        freq[frozenset(picked)]+=1
    predicted={frozenset([0]):Fraction(1,n)}
    for choice in product(*blades):predicted[frozenset(choice)]=Fraction(n-1,n*prod(sizes))
    assert set(freq)==set(predicted)
    for s,prob in predicted.items():assert Fraction(freq[s],factorial(n))==prob,(sizes,s,freq[s],prob)
    uniform=len(set(freq.values()))==1
    nstates=len(freq)
    tv=sum((abs(Fraction(v, factorial(n))-Fraction(1,nstates)) for v in freq.values()), Fraction(0))/2
    expected_tv=Fraction(abs(prod(sizes)-sum(sizes)),(sum(sizes)+1)*(prod(sizes)+1))
    assert tv==expected_tv,(sizes,tv,expected_tv)
    assert uniform==(prod(sizes)==sum(sizes)),sizes
    return n,len(freq),uniform
if __name__=='__main__':
    test=((1,),(3,),(1,1),(2,2),(2,3),(1,2,3),(2,2,2),(2,3,1),(1,1,1,1),(2,4,1,1),(3,3,1,1,1))
    for sizes in test:
        if 1+sum(sizes)>9:continue
        print('PASS',sizes,case(sizes))
