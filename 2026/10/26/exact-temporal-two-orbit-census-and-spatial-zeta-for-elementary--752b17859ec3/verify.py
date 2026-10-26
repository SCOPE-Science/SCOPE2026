#!/usr/bin/env python3
"""Exact finite-graph certificate and small-ring cross-check for ECA rule 18."""
from itertools import product
from collections import Counter

def local(a,b,c):
    return int((a,b,c) in ((0,0,1),(1,0,0)))

def two_center(w):
    y = [local(w[j], w[j+1], w[j+2]) for j in range(3)]
    return local(*y)

words = [''.join(map(str,w)) for w in product((0,1), repeat=5)
         if two_center(w) == w[2]]
assert len(words) == 20
nodes = [''.join(map(str,w)) for w in product((0,1), repeat=4)]
adj = {v: [] for v in nodes}
for w in words:
    adj[w[:4]].append(w[1:])
for u in adj:
    assert len(adj[u]) == len(set(adj[u]))

# Enumerate elementary directed cycles once, canonically rooted at their
# lexicographically smallest four-bit vertex.
cycles = set()
def visit(start, path):
    for nxt in adj[path[-1]]:
        if nxt == start:
            cycles.add(tuple(path))
        elif nxt > start and nxt not in path:
            visit(start, path + [nxt])
for v in nodes:
    visit(v,[v])
cycle_list = list(cycles)
assert Counter(map(len,cycle_list)) == Counter({1:1,4:1,5:2,6:1,10:2})
# Independently derive det(I-zA) by the finite directed-cycle expansion.
coeff = Counter({0:1})
def disjoint_sets(i, occupied, exponent, parity):
    if i == len(cycle_list):
        return [(exponent,parity)]
    output = disjoint_sets(i+1, occupied, exponent, parity)
    c = cycle_list[i]
    if not (set(c) & occupied):
        output += disjoint_sets(i+1, occupied | set(c), exponent+len(c), -parity)
    return output
calc = Counter()
for exponent,sign in disjoint_sets(0,set(),0,1):calc[exponent]+=sign
calc = {i:c for i,c in calc.items() if c}
# Factorization: (1-z)(1-z^4-2z^5-z^6).
expected = Counter()
for e, c in [(0,1),(4,-1),(5,-2),(6,-1)]:
    expected[e] += c
    expected[e+1] -= c
assert calc == {k:v for k,v in expected.items() if v}

def F(x):
    n=len(x)
    return tuple(local(x[(i-1)%n],x[i],x[(i+1)%n]) for i in range(n))

b=[0]*51
b[4:7]=[4,10,6]
for n in range(7,len(b)):
    b[n] = b[n-4]+2*b[n-5]+b[n-6]
assert [b[n] for n in range(1,19)] == [0,0,0,4,10,6,0,4,18,30,22,10,26,70,100,84,68,132]
for n in range(1,16):
    fixed2 = 0
    fixed1 = 0
    for x in product((0,1),repeat=n):
        fx=F(x)
        fixed1 += fx==x
        fixed2 += F(fx)==x
    assert fixed1 == 1,(n,fixed1)
    assert fixed2 == 1+b[n],(n,fixed2,b[n])
assert all(b[n]>0 for n in [4,5,6]+list(range(8,51)))
assert [n for n in range(1,51) if b[n]==0] == [1,2,3,7]
print('VERIFY_OK')
print('five_block_count=20; elementary_cycles_by_length='+str(dict(Counter(map(len,cycle_list)))))
print('det(I-zA)=(1-z)(1-z^4-2z^5-z^6)')
print('direct_bruteforce_ring_range=1..15')
print('a_n_1..18=' + str([1+b[n] for n in range(1,19)]))
