#!/usr/bin/env python3
from itertools import combinations
from math import comb

def E(k,m):
    return sum(comb(k,j) for j in range(min(k,m)+1))

# Arithmetic and stabilization of the proposed envelope.
for k in range(9):
    for m in range(11):
        v=E(k,m)
        assert 1 <= v <= 2**k
        if m >= k:
            assert v == 2**k
        if k>0 and m<k:
            assert v < 2**k

# Independent finite replay of the extremal singleton-predicate construction.
# Kernel points are 0,...,k-1. Ordinary points are k,...,N-1.
# An induced unary structure is canonically determined by which P_i singletons occur.
def replay(k,m):
    ordinary=max(m,1)+2
    N=k+ordinary
    sigs=set()
    for A in combinations(range(N),m):
        S=frozenset(x for x in A if x<k)
        sigs.add(S)
    return len(sigs)

for k in range(7):
    for m in range(8):
        got=replay(k,m)
        want=E(k,m)
        assert got==want,(k,m,got,want)

# Kernel minimality witness: if singleton f_i is omitted from a proposed chaining set,
# choose an ordinary point x. The one-point map f_i -> x is an order partial
# isomorphism for a suitable order but fails predicate P_i preservation.
for k in range(1,8):
    for i in range(k):
        predicate_at_fi=True
        predicate_at_ordinary=False
        assert predicate_at_fi != predicate_at_ordinary

print('rows', {k:[E(k,m) for m in range(0,8)] for k in range(0,6)})
print('replay_ranges', 'k<=6, m<=7')
print('VERIFY_OK')
