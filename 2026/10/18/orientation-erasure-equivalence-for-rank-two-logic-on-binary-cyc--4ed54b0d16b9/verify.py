#!/usr/bin/env python3
"""Direct finite checks for two-round orientation erasure on coloured cycles.
No external packages needed. The all-order assertion has a separate proof.
"""
from itertools import product

def invariant(word, oriented):
    n=len(word)
    out=set()
    for i,b in enumerate(word):
        a,c=word[(i-1)%n],word[(i+1)%n]
        F=frozenset(word[j] for j in range(n) if j not in {(i-1)%n,i,(i+1)%n})
        if oriented:
            out.add((b,a,c,F))
        else:
            out.add((b,frozenset((a,c)),F))
    return frozenset(out)

def check_binary(bound=14):
    words=0; groups=0
    for n in range(3,bound+1):
        lookup={}
        for w in product(range(2),repeat=n):
            u=invariant(w,False)
            d=invariant(w,True)
            prior=lookup.setdefault(u,d)
            assert prior==d,('counterexample',n,w)
            # Every oriented 3-factor occurs with its reversed oriented factor.
            for i in range(n):
                trip=(w[(i-1)%n],w[i],w[(i+1)%n])
                assert any((w[(j-1)%n],w[j],w[(j+1)%n])==trip[::-1] for j in range(n))
            words+=1
        groups+=len(lookup)
    return words,groups

def check_three_colors():
    a=(0,1,2); b=(0,2,1)
    assert invariant(a,False)==invariant(b,False)
    assert invariant(a,True)!=invariant(b,True)
    # Formula exists x(P0(x) and exists y(P1(y) and R(x,y))).
    def forward(w):
        return any(w[i]==0 and w[(i+1)%len(w)]==1 for i in range(len(w)))
    assert forward(a) and not forward(b)

if __name__=='__main__':
    words,grp=check_binary()
    check_three_colors()
    print('PASS: all',words,'binary cyclic words, lengths 3..14; directed rank-2 pointed-type sets determined by undirected sets')
    print('PASS: all reversed binary length-3 factors occur; aggregate undirected theory groups:',grp)
    print('PASS: ternary directed 012 versus 021 is separated by a rank-2 directed sentence, but has identical undirected reduct')
    print('FINITE TESTS ONLY: all-order theorem is established in RESULT.md proof')
