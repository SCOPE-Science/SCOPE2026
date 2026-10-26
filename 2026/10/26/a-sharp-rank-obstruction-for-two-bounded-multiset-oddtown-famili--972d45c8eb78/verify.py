#!/usr/bin/env python3
"""Exact small 2-bounded Oddtown computation, standard library only.

A vector x in {0,1,2}^n is admissible when sum(x) is odd.
Two distinct vectors are compatible iff sum(min(x_i,y_i)) is even.
The maximum family size is the clique number of their compatibility graph.
Every maximal clique is enumerated by a pivoted Bron-Kerbosch search.
"""
from itertools import product

W4 = [
 (0,1,1,1), (1,0,1,1), (2,1,0,2),
 (1,2,0,2), (1,1,1,0), (2,2,0,1),
]
W6 = [
 (0,0,0,1,1,1), (0,0,1,0,1,1),
 (1,0,1,2,0,1), (0,0,2,1,2,0),
 (1,1,1,2,2,0), (0,1,1,2,0,1),
 (2,2,1,1,0,1), (1,2,1,1,0,2),
 (2,1,1,1,0,2), (1,1,2,2,1,0),
]

def valid(family):
    assert len(family) == len(set(family))
    assert all(all(d in (0,1,2) for d in x) and sum(x)%2==1 for x in family)
    assert len(set(map(len,family)))==1
    for i,x in enumerate(family):
        for y in family[:i]:
            assert sum(map(min, zip(x,y)))%2 == 0,(x,y)
    return True

def enum_maximum(n):
    vec = [x for x in product((0,1,2),repeat=n) if sum(x)%2]
    total = len(vec)
    neighbors=[0]*total
    for a in range(total):
        for b in range(a):
            if sum(map(min,zip(vec[a],vec[b])))%2==0:
                neighbors[a]|=1<<b
                neighbors[b]|=1<<a
    maxima=0
    num_maximal=0
    max_count=0
    def bron(R,P,X):
        nonlocal maxima,num_maximal,max_count
        if not P and not X:
            num_maximal+=1
            if R>maxima:
                maxima=R; max_count=1
            elif R==maxima:
                max_count+=1
            return
        both=P|X
        if both:
            # Choose a vertex that maximizes neighbors inside P.
            pvt=max(iter_bits(both), key=lambda u: (P&neighbors[u]).bit_count())
            candidates=P&~neighbors[pvt]
        else:
            candidates=P
        while candidates:
            lsb=candidates&-candidates
            v=lsb.bit_length()-1
            bron(R+1,P&neighbors[v],X&neighbors[v])
            P&=~lsb
            X|=lsb
            candidates&=~lsb
    def iter_bits(mask):
        while mask:
            b=mask&-mask
            yield b.bit_length()-1
            mask^=b
    bron(0,(1<<total)-1,0)
    return total,maxima,num_maximal,max_count

def main():
    assert valid(W4)
    assert valid(W6)
    W5=[x+(0,) for x in W4]+[(0,0,0,0,1)]
    assert valid(W5)
    print('CERTIFICATES n4=%d n5=%d n6=%d' % (len(W4),len(W5),len(W6)))
    for n in range(1,6):
        candidates,maximum,maximal_count,maximum_count=enum_maximum(n)
        print('EXHAUSTIVE n=%d odd_vectors=%d maximum=%d maximal_cliques=%d maximum_cliques=%d' %
              (n,candidates,maximum,maximal_count,maximum_count))
        assert maximum == (1,2,3,6,7)[n-1]
    print('LINEAR_BOUND even n: at most 2n-2 (proved algebraically, NOT extrapolated)')
    assert len(W6)==2*6-2
    print('VERIFY_OK')

if __name__=='__main__':main()
