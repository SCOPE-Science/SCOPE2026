#!/usr/bin/env python3
"""Exact Fano incidence-poset rowmotion certificate, Python 3 standard library only."""
from collections import Counter
from itertools import product
from math import lcm

P = range(1, 8)
DOT = lambda a, b: (a & b).bit_count() % 2
LINES = {a: sum(1 << (p - 1) for p in P if DOT(a,p) == 0) for a in P}
BY_BLOCK = {block: a for a, block in LINES.items()}
assert len(BY_BLOCK) == 7
assert all(b.bit_count() == 3 for b in LINES.values())
assert all(sum(bool(b & (1 << (p-1))) for b in LINES.values()) == 3 for p in P)
assert all(sum(bool(b & (1 << (p-1))) and bool(b & (1 << (q-1))) for b in LINES.values()) == 1 for p in P for q in P if p<q)

def allowed(p,l):
    return all(not(l >> (a-1) & 1) or (p & block) == block for a,block in LINES.items())

IDEALS = {p | (l << 7) for p in range(128) for l in range(128) if allowed(p,l)}
# Also check the point-subset summation identity.
assert len(IDEALS) == sum(2**sum(p & block == block for block in LINES.values()) for p in range(128)) == 458

def row(x):
    p,l = x & 127, x >> 7
    new_lines = sum(1 << (a-1) for a,b in LINES.items() if (p&b)==b and not(l>>(a-1)&1))
    new_points = (~p) & 127
    for a,b in LINES.items():
        if new_lines>>(a-1)&1: new_points |= b
    return new_points | (new_lines<<7)

assert {row(x) for x in IDEALS} == IDEALS

def toggle(x):
    # Upper-rank toggles followed by lower-rank toggles implement rowmotion.
    for a,block in LINES.items():
        bit = 1 << (a+6)
        if x & bit: x ^= bit
        elif (x&block)==block: x ^= bit
    for p in P:
        bit = 1 << (p-1)
        if x & bit:
            # Can remove p iff no selected incident upper element depends on p.
            if not any((x >> (a+6)&1) and (block&bit) for a,block in LINES.items()): x^=bit
        else: x^=bit
    return x

assert all(row(x) == toggle(x) for x in IDEALS)

# All 168 invertible F_2-linear permutations of the seven projective points.
GL = []
for a,b,c in product(P, repeat=3):
    f = {x: ((a if x&1 else 0) ^ (b if x&2 else 0) ^ (c if x&4 else 0)) for x in P}
    if len(set(f.values())) != 7: continue
    h = {}
    for k,block in LINES.items():
        image = sum(1<<(f[p]-1) for p in P if block>>(p-1)&1)
        h[k] = BY_BLOCK[image]
    GL.append((f,h))
assert len(GL) == 168

def apply(x,g):
    f,h=g; p,l=x&127,x>>7
    q=sum(1<<(f[a]-1) for a in P if p>>(a-1)&1)
    s=sum(1<<(h[a]-1) for a in P if l>>(a-1)&1)
    return q | (s<<7)

assert all(apply(row(x),g) == row(apply(x,g)) for x in IDEALS for g in GL)

# One representative for each orbit of rowmotion cycles under the collineation group.
# (point mask, line mask, length, number of cycles in GL orbit, size sum on a cycle)
REPS = [
    (0,  0, 3,  1, 21),
    (47, 1, 3, 14, 18),
    (63, 3, 3, 14, 24),
    (1,  0, 5,  7, 38),
    (3,  0, 5, 21, 35),
    (7,  0, 5,  7, 32),
    (11, 0, 7, 28, 49),
]
cycles = []
visited = set()
for x in sorted(IDEALS):
    if x in visited: continue
    curr=x; cyc=[]
    while curr not in visited:
        visited.add(curr);cyc.append(curr);curr=row(curr)
    assert curr == x
    cycles.append(frozenset(cyc))
assert visited == IDEALS
cycset=set(cycles)
assert Counter(map(len,cycles)) == Counter({3:29,5:35,7:28})
assert Counter((len(c),sum(x.bit_count() for x in c)) for c in cycles) == Counter({(3,18):14,(3,21):1,(3,24):14,(5,32):7,(5,35):21,(5,38):7,(7,49):28})

partition=set()
for p,l,n,m,size_sum in REPS:
    x=p|(l<<7);assert x in IDEALS
    orb=[];y=x
    while y not in orb:
        orb.append(y);y=row(y)
    assert y==x and len(orb)==n and sum(z.bit_count() for z in orb)==size_sum
    cls={frozenset(apply(z,g) for z in orb) for g in GL}
    assert len(cls)==m and cls <=cycset and not (cls & partition)
    partition|=cls
    print('ORBIT_CLASS_OK', 'representative', (p,l), 'period',n,'group_orbit',m,'size_sum',size_sum, 'stabilizer',168//m)
assert partition==cycset
assert lcm(*{len(c) for c in cycles})==105
print('FULL_CERTIFICATE_OK', 'ideals',len(IDEALS),'cycle_lengths',dict(Counter(map(len,cycles))), 'row_order',105, 'group_classes',len(REPS))
