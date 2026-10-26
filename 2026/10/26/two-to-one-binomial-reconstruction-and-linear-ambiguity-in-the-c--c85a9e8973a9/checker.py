#!/usr/bin/env python3
"""Finite checks for a two-to-one 2-binomial factor theorem of the Cantor word.
No finite computation is used in place of the all-scale proof.
"""
from collections import defaultdict

def cantor(k):
    w = bytes((1,))
    for _ in range(k):
        w = b''.join((b'\x01\x00\x01' if x else b'\x00\x00\x00') for x in w)
    return w

def signature(w):
    ones = [i for i, x in enumerate(w) if x == 1]
    return (len(ones), sum(ones))

def scattered2(w):
    n = len(w)
    z = len([x for x in w if x == 0]); o=n-z
    s01 = 0; before0 = 0
    for x in w:
        if x == 0: before0 += 1
        else: s01 += before0
    return (z, o, z*(z-1)//2, s01, z*o-s01, o*(o-1)//2)

def check(k):
    n = 3**k; c = cantor(k)
    assert len(c) == n and c == c[::-1]
    assert sum(c) == 2**k
    A = [bytes(n-r)+c[:r] for r in range(n+1)]
    B = [c[r:]+bytes(r) for r in range(n+1)]
    assert len(set(map(signature,A))) == n+1
    assert len(set(map(signature,B))) == n+1
    assert all(B[r] == A[n-r][::-1] for r in range(n+1))
    classes = defaultdict(set)
    for w in A+B:
        classes[signature(w)].add(w)
    assert max(map(len,classes.values())) <= 2
    # An actual prefix contains every predicted type: sigma^k(1), sigma^k(0),
    # sigma^k(1) occur consecutively at aligned blocks.
    actual = cantor(k+2)
    factors = {actual[i:i+n] for i in range(len(actual)-n+1)}
    assert factors == (set(A)|set(B))
    if k >= 3:
        r0 = 22*n//27; r1 = 24*n//27
        assert r1-r0+1 == 2*n//27+1
        pairs = []
        for r in range(r0,r1+1):
            u = 46*n//27-r
            aa = A[r]; bb = B[n-u]
            assert aa != bb and signature(aa) == signature(bb)
            assert aa in factors and bb in factors
            pairs.append(signature(aa))
        assert len(set(pairs)) == len(pairs)
        assert all(len(classes[s]) == 2 for s in pairs)
        assert len([s for s in classes if len(classes[s])==2]) >= 2*n//27+1
    if k<=7:
        for sig, members in classes.items():
            assert all((scattered2(w)[1], sum(i for i,z in enumerate(w) if z)) == sig for w in members)
            assert len({scattered2(w) for w in members}) == 1
    return (n,len(factors),len(classes),sum(len(v)==2 for v in classes.values()))

def main():
    for k in range(1,8):
        n, nf, nc, ambiguous = check(k)
        print(f'k={k}: n={n}; distinct_factors={nf}; 2_binomial_classes={nc}; double_classes={ambiguous}')
    print('PASS: all finite construction, covering, injectivity, and ambiguity checks')

if __name__ == '__main__': main()
