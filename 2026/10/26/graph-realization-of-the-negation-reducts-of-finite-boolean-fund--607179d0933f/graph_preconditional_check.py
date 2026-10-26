#!/usr/bin/env python3
"""Finite verification of graph-induced Boolean preconditionals."""
from itertools import combinations

def check(n):
    U=(1<<n)-1
    pairs=list(combinations(range(n),2))
    checked=0
    for m in range(1<<len(pairs)):
        nbr=[0]*n
        for k,(i,j) in enumerate(pairs):
            if m>>k&1:
                nbr[i]|=1<<j
                nbr[j]|=1<<i
        def neg(x):
            z=U
            for i in range(n):
                if x>>i&1:
                    z &= nbr[i]
            return z
        def imp(a,b):
            return neg(a & (U^b)) | (a&b)
        for a in range(1<<n):
            assert imp(U,a)==a
            assert imp(a,a)==U
            assert (a&neg(a))==0
            assert (a&neg(neg(a)))==a
            assert imp(a,0)==neg(a)
            for b in range(1<<n):
                assert (a&b)& ~imp(a,b)==0
                assert imp(a,b)==imp(a,a&b)
                assert (a&imp(a,b)) & ~b==0   # MP
                for c in range(1<<n):
                    assert imp(a,b&c)& ~imp(a,b)==0
                    assert imp(a,b)&imp(a,c)==imp(a,b&c) # normality
                    assert imp(a,imp(a&b,c))& ~imp(a&b,c)==0
                    checked+=1
        all_edges=m==(1<<len(pairs))-1
        ni=all((neg(imp(a,b)) & ~imp(a,neg(b)))==0
              for a in range(1<<n) for b in range(1<<n))
        # n=1 has trivially complete graph
        assert ni==all_edges
    return 1<<len(pairs),checked
if __name__=='__main__':
    tot=0
    for n in range(1,5):
        graphs,triples=check(n)
        tot+=triples
        print('atoms',n,'graphs',graphs,'axiom-triples',triples)
    print('GRAPH_PRECONDITIONAL_OK',tot)
