"""Finite checks for the three-valued semialgebra generation theorem.
Run with Python 3, standard library only. No external data.
"""
from itertools import product, combinations
from collections import Counter

VALS=(0,1,2)  # 1 is undefined, 0 false, 2 true

def kleene_closure(m, gens):
    bot=(0,)*m; top=(2,)*m
    elements={bot,top,*gens}
    while True:
        old=set(elements)
        for a in old:
            elements.add(tuple(2-x for x in a))
        old=list(elements)
        for a in old:
            for b in old:
                elements.add(tuple(min(x,y) for x,y in zip(a,b)))
                elements.add(tuple(max(x,y) for x,y in zip(a,b)))
        if len(elements)==len(old) and all(tuple(2-x for x in a) in elements for a in old):
            return elements

def passes_word_condition(m, gens):
    k=len(gens)
    words=[tuple(gens[j][i] for j in range(k)) for i in range(m)]
    if any(1 not in w for w in words):
        return False
    return all(any((x,y) in ((0,2),(2,0)) for x,y in zip(a,b))
               for a,b in combinations(words,2))

def exhaustive(m,k):
    full=set(product(VALS,repeat=m))
    count=0
    for gens in product(tuple(full),repeat=k):
        observed=(kleene_closure(m,gens)==full)
        predicted=passes_word_condition(m,gens)
        assert observed==predicted,(m,k,gens,observed,predicted)
        count+=observed
    return count

def counts_via_words(k,m):
    partial=[t for t in product(VALS,repeat=k) if 1 in t]
    answer=0
    for words in product(partial,repeat=m):
        if all(any((x,y) in ((0,2),(2,0)) for x,y in zip(a,b))
               for a,b in combinations(words,2)):
            answer+=1
    return answer

def perfect_matchings_cube(k):
    vertices=tuple(range(1<<k))
    def recur(remaining):
        if not remaining:
            return 1
        v=min(remaining)
        return sum(recur(remaining-{v,u}) for u in remaining if u !=v and (u^v).bit_count()==1)
    return recur(frozenset(vertices))

def local_probability_moments():
    options=(0,1,2)
    compatible=lambda a,b: (a==1 or b==1 or a==b)
    pcount=sum(compatible(a,b) for a,b in product(options,repeat=2))
    qcount=sum(compatible(a,b) and compatible(a,c) for a,b,c in product(options,repeat=3))
    assert pcount==7 and qcount==17
    assert (17/27)*(9/7)**1.5 < 1
    assert (2/3)*(9/7)**0.5 < 1
    print('one_coordinate_pair_compatible',pcount,'of',9,'adjacent_pairs',qcount,'of',27)

if __name__ == '__main__':
    local_probability_moments()
    for m,k in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]:
        a=exhaustive(m,k)
        b=counts_via_words(k,m)
        assert a==b,(m,k,a,b)
        print('K3_power',m,'generators',k,'tuples',a)
    for k in [1,2,3,4]:
        M=perfect_matchings_cube(k)
        import math
        maximal=counts_via_words(k,1<<(k-1)) if k<=3 else None
        if maximal is not None: assert maximal==math.factorial(1<<(k-1))*M
        print('dimension',k,'maximum_coordinates',1<<(k-1),'perfect_matchings',M,'maximal_ordered_generators',maximal)
    print('ALL_CHECKS_OK')
