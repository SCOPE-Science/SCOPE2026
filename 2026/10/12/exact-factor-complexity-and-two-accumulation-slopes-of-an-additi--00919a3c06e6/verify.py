#!/usr/bin/env python3
"""Finite independent checks for the exact factor-complexity formula."""
from collections import defaultdict

def beta(s):
    return ''.join('00001' if c == '0' else '01101' for c in s)

def complexity(n):
    if n == 0:
        return 1
    total = 2*n
    k = 0
    while True:
        power = 5**k
        lo = (7*power+1)//4
        hi = (15*power-3)//4
        if lo >= n:
            break
        total += max(0, min(n-1, hi)-lo+1)
        k += 1
    return total

# Markers recognize the common 5-block phase in every factor of length >=8.
triples = sorted({'000', '001', '010', '011', '100', '101', '110'})
assert set(''.join(beta('0'))[i:i+3] for i in range(3)) <= set(triples)
for tri in triples:
    image = beta(tri)
    for i in range(len(image)-7):
        w = image[i:i+8]
        assert '0000' in w or '11' in w, (tri,i,w)

# All source length-three factors are represented by these seven triples.
seed = beta(beta('0'))
assert set(seed[i:i+3] for i in range(len(seed)-2)) == set(triples)

# Exhaustive seven-triple finite boundary enumeration for n<=7.
expected_nonzero = {0: {'':1}, 1:{'0':1}, 3:{'000':-1,'010':1,'101':-1}}
for n in range(8):
    neighbors=defaultdict(set)
    for tri in triples:
        im=beta(tri)
        for i in range(len(im)-n-1):
            neighbors[im[i+1:i+n+1]].add(im[i]+im[i+n+1])
    actual={}
    for w,edges in neighbors.items():
        order=len(edges)-len({z[0] for z in edges})-len({z[1] for z in edges})+1
        if order:actual[w]=order
    assert actual == expected_nonzero.get(n,{}), (n,actual)

# Brute sliding windows, independent of special-factor recurrence.
s='0'
for _ in range(7):
    s=beta(s)
bits=[int(x) for x in s]
for n in range(1,261):
    mask=(1<<n)-1
    x=0
    seen=set()
    for i,bit in enumerate(bits):
        x=((x<<1)|bit)&mask
        if i+1>=n:
            seen.add(x)
    assert len(seen)==complexity(n),(n,len(seen),complexity(n))

# Nonzero bispecial orders to lengths 93 via a different direct context method.
for n in [8,13,18,43,68,93]:
    edges=defaultdict(set)
    for i in range(1,len(s)-n):
        edges[s[i:i+n]].add(s[i-1]+s[i+n])
    counts={}
    for w,ext in edges.items():
        order=len(ext)-len({v[0] for v in ext})-len({v[1] for v in ext})+1
        if order:
            counts[order]=counts.get(order,0)+1
    expected={8:{1:1},13:{},18:{1:1,-1:2},43:{1:1},68:{},93:{1:1,-1:2}}[n]
    assert counts == expected,(n,counts,expected)
print('VERIFY_OK blocks=7 contexts=7 base=0..7 factors=1..260 bispecial_lengths=8,13,18,43,68,93 prefix=78125')
