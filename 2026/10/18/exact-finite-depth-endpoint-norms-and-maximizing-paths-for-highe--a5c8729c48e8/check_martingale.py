#!/usr/bin/env python3
"""Independent exact-rational checks for finite b-adic signed martingale transforms."""
from fractions import Fraction as Q
from itertools import product
from random import Random

def closed_form(b, d):
    return Q(2*(b-1)*d,b+1) + Q((b-1)*(b+3),(b+1)**2) + Q(4, (b+1)**2)*Q(-1,b)**d

def column_shell(b, signs):
    y=Q(1)
    total=Q(0)
    for sign in signs:
        total += Q(b-1,b)*(1-sign*y)
        y=(y+(b-1)*sign)/b
    return total+abs(y)

def brute_path(b, d):
    vals=[(column_shell(b,s),s) for s in product((-1,1),repeat=d)]
    val=max(a for a,_ in vals)
    best=[s for a,s in vals if a==val]
    expected=tuple((-1)**j for j in range(1,d+1))
    assert val==closed_form(b,d), (b,d,val,closed_form(b,d))
    assert best==[expected],(b,d,best)

def prefix(x,k):
    return x[:k]

def matrix(b,d,signs):
    words=list(product(range(b),repeat=d))
    N=len(words)
    p=Q(1,N)
    M=[[p for k in range(N)] for i in range(N)]
    for j in range(1,d+1):
        for i,x in enumerate(words):
            e=signs[(j,prefix(x,j-1))]
            for k,y in enumerate(words):
                difference=(Q(b)**(j-d) if prefix(x,j)==prefix(y,j) else Q(0)) - (Q(b)**(j-1-d) if prefix(x,j-1)==prefix(y,j-1) else Q(0))
                M[i][k]+=e*difference
    return words,M

def test_matrix(b,d,signs):
    words,M=matrix(b,d,signs)
    largest=Q(0)
    for k,word in enumerate(words):
        l1=sum(abs(M[i][k]) for i in range(len(words)))
        path=tuple(signs[(j,prefix(word,j-1))] for j in range(1,d+1))
        assert l1==column_shell(b,path),(b,d,k,l1,path)
        largest=max(largest,l1)
    assert largest<=closed_form(b,d)
    return largest

def run():
    cases=0
    for b in range(3,9):
        for d in range(1,10):
            brute_path(b,d)
            cases+=1
    rng=Random(230524)
    for b,d in [(3,1),(4,1),(3,2),(4,2),(5,2),(3,3),(4,3)]:
        nodes=[(j,p) for j in range(1,d+1) for p in product(range(b),repeat=j-1)]
        alternating={node:(-1)**node[0] for node in nodes}
        assert test_matrix(b,d,alternating)==closed_form(b,d)
        cases+=1
        if len(nodes)<=6:
            sign_lists=product((-1,1),repeat=len(nodes))
        else:
            sign_lists=(tuple(rng.choice((-1,1)) for _ in nodes) for _ in range(30))
        for seq in sign_lists:
            signs=dict(zip(nodes,seq))
            norm=test_matrix(b,d,signs)
            matches=any(all(signs[(j,prefix(w,j-1))]==(-1)**j for j in range(1,d+1)) for w in product(range(b),repeat=d))
            assert (norm==closed_form(b,d))==matches,(b,d,norm,matches)
            cases+=1
    print('PASS',cases,'exact-rational cases; complete path exhaustive b=3..8, d=1..9, independent finite matrices.')
if __name__=='__main__': run()
