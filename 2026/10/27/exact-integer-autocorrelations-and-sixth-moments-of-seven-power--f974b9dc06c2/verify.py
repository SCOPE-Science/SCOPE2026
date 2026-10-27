#!/usr/bin/env python3
"""Independent exact finite checks for base-seven very odd sequence correlations."""
from collections import Counter
from itertools import product
from math import comb


def support(bits):
    S = {0}
    for j, bit in enumerate(bits):
        D = (0, 1, 3) if bit == 0 else (0, 2, 3)
        S = {s + d * 7**j for s in S for d in D}
    return S

def zbalanced(t, k):
    z = 0
    for _ in range(k):
        r = t % 7
        if r > 3: r -= 7
        z += r == 0
        t = (t - r) // 7
    assert t == 0
    return z

def correlations(S):
    H = Counter()
    for u in S:
        for v in S:
            if v >= u: H[v-u] += 1
    return H

moments = [1,99]
for k in range(2,6):
    moments.append(118*moments[-1]-873*moments[-2])
for k in range(1, 6):
    N = (7**k + 1) // 2
    sets = []
    for bits in product((0,1),repeat=k):
        S = support(bits)
        assert len(S) == 3**k and min(S) == 0 and max(S) == N-1
        sets.append(S)
        if k <= 4:
            coeff={0:1}
            for _ in range(3):
                nxt=Counter()
                for n,c in coeff.items():
                    for u in S: nxt[n+u]+=c
                coeff=nxt
            moment=sum(c*c for c in coeff.values())
            assert moment==moments[k],(k,bits,moment,moments[k])
        H=correlations(S)
        assert H[0] == 3**k
        assert len(H) == N
        for t in range(1,N):
            assert H[t] == 3**zbalanced(t,k), (k,bits,t)
        hist = Counter(H[t] for t in range(1,N))
        assert hist == Counter({3**j:comb(k,j)*6**(k-j)//2 for j in range(k)})
    assert len({frozenset(S) for S in sets}) == 2**k
    first = correlations(sets[0])
    assert all(correlations(S)==first for S in sets)
    assert len({min(tuple(sorted(S)),tuple(sorted(N-1-x for x in S))) for S in sets}) == 2**(k-1)
    for j in range(1,k+1):
        modulus=7**j
        order=1
        value=2%modulus
        while value !=1:
            value=(value*2)%modulus
            order+=1
        assert order == 3*7**(j-1)
    print('depth',k,'length',N,'sequences',2**k,'all-shifts verified')
print('VERIFY_OK: full integer correlation and histogram for 62 sequences, depths 1..5; sixth moments through depth 4; modular orders and reflection classes')
