"""Finite rational and palette-orbit checks for proper path words."""
from itertools import product, permutations
from collections import defaultdict, Counter


def words(q, n):
    stack = [(c,) for c in range(q)]
    while stack:
        w=stack.pop()
        if len(w)==n: yield w
        else: stack.extend(w+(c,) for c in range(q) if c != w[-1])


def transfer(q,t,a,b):
    numerator = (q-1)**t+(-1)**t*((q if a==b else 0)-1)
    assert numerator % q==0
    return numerator//q


def orbit_signature(p):
    # Canonical restricted-growth string for the equality relation on p.
    d={};sig=[]
    for c in p:
        if c not in d:d[c]=len(d)
        sig.append(d[c])
    return tuple(sig)


def verify():
    tested=0;word_count=0;orbit_tests=0
    for q,nmax in ((2,9),(3,10),(4,9),(5,7)):
        for n in range(2,nmax+1):
            ends=Counter();two_ends=Counter();cyclic=0
            for w in words(q,n):
                word_count+=1
                ends[(w[0],w[-1])]+=1
                if w[0]!=w[-1]:cyclic+=1
                if n>=4:two_ends[w[:2]+w[-2:]]+=1
            assert sum(ends.values())==q*(q-1)**(n-1)
            assert cyclic==(q-1)**n+(-1)**n*(q-1)
            for a,b in product(range(q),repeat=2):
                assert ends[(a,b)]==transfer(q,n-1,a,b)
                tested+=1
            if n>=4:
                for a,b,c,d in product(range(q),repeat=4):
                    expect=transfer(q,n-3,b,c) if a!=b and c!=d else 0
                    assert two_ends[(a,b,c,d)]==expect
                    tested+=1
    for L in range(2,7):
        ps=list(words(3,L))
        D=3*2**(L-1)
        assert len(ps)==D
        bins=defaultdict(int)
        for a in ps:
            for b in ps:
                bins[orbit_signature(a+b)]+=1
        assert len(bins)==D*D//6
        assert set(bins.values())=={6}
        orbit_tests+=len(bins)
    print('PROPER_COLOUR_SYMMETRY_EXACT_OK',tested,word_count,orbit_tests)

if __name__=='__main__':verify()
