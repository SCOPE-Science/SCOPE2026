#!/usr/bin/env python3
"""Independent two-round game check using atomic two-point diagrams."""
from itertools import product
from verify import invariant

def two_round_invariant(w, oriented):
    n=len(w); types=set()
    for i in range(n):
        diagrams=set()
        for j in range(n):
            succ=(j==(i+1)%n)
            pred=(j==(i-1)%n)
            if oriented: relation=(succ,pred)
            else: relation=(succ or pred,)
            diagrams.add((w[i],w[j],i==j,relation))
        types.add(frozenset(diagrams))
    return frozenset(types)

if __name__=='__main__':
    cnt=0; signature_class_map={}
    for n in range(3,10):
        undirected2directed={}; simple2game={}; game2simple={}
        for w in product((0,1),repeat=n):
            U=two_round_invariant(w,False)
            D=two_round_invariant(w,True)
            assert undirected2directed.setdefault(U,D)==D
            for orient in (True,False):
                s=invariant(w,orient);g=two_round_invariant(w,orient)
                t=(n,orient)
                simple2game.setdefault(t,{})
                game2simple.setdefault(t,{})
                assert simple2game[t].setdefault(s,g)==g
                assert game2simple[t].setdefault(g,s)==s
            cnt+=1
        signature_class_map[n]=len(undirected2directed)
    print('PASS: direct atomic-diagram two-round game,',cnt,'binary cycles length 3..9')
    print('PASS: exact agreement with independent pointed-triple invariants at each tested order')
    print('rank-two class counts by order:',signature_class_map)
