#!/usr/bin/env python3
"""Reproducible checks for a Rudin-Shapiro initial-repetition theorem."""
from collections import Counter

def theta(state):
    b,p=state
    return ((b,0),(b^p,1))

def expand(seed,depth):
    letters=[seed]
    for _ in range(depth):
        letters=[z for x in letters for z in theta(x)]
    return letters

def direct(n):
    return (n & (n >> 1)).bit_count() & 1

# Exhaustive two-letter language of the four-state fixed point.
seed=(0,0)
pairs={(theta(seed)[0],theta(seed)[1])}
while True:
    new=set(pairs)
    for a,b in pairs:
        u=theta(a)+theta(b)
        new.update(zip(u,u[1:]))
    if new==pairs:
        break
    pairs=new
assert len(pairs)==8, sorted(pairs)
phase=[set(),set()]
for a,b in pairs:
    block=expand(a,3)+expand(b,3)
    for offset in range(8):
        word=tuple(x[0] for x in block[offset:offset+8])
        phase[offset & 1].add(word)
assert (len(phase[0]),len(phase[1]),len(phase[0]&phase[1]))==(24,32,0)
print('PHASE_OK eight_state_pairs=8 even8=24 odd8=32 intersection=0')

# Independent calculation: morphic states versus overlapping-11 arithmetic.
N=1<<17
state_bits=bytes(x[0] for x in expand(seed,17))
arithmetic_bits=bytes(direct(i) for i in range(N))
assert state_bits==arithmetic_bits
print('CODING_OK length='+str(N))

# Exact first-collision scan by finite strings, with all preceding starts inspected.
def first_collision(n):
    seen={}
    for j in range(N-n+1):
        word=arithmetic_bits[j:j+n]
        if word in seen:
            earlier=[i for i in range(j) if arithmetic_bits[i:i+n]==word]
            return j,earlier
        seen[word]=j
    raise AssertionError(('prefix too short',n))

def predicted(n):
    if n<=2:return 1,0
    if n<=5:return 4,1
    return 1 << (1+(n-1).bit_length()),0

for n in range(1,1025):
    j,earlier=first_collision(n)
    ans,k=predicted(n)
    assert j==ans,(n,j,ans)
    assert earlier==[k],(n,j,earlier,k)
for n in [1025,1536,2048,2049,3073,4096,4097,6145,8192]:
    j,earlier=first_collision(n)
    ans,k=predicted(n)
    assert (j,earlier)==(ans,[k]),(n,j,earlier,ans,k)
print('COLLISIONS_OK all_lengths=1..1024 plus=9_through_8192')
print('INITIAL_TABLE',[(n,first_collision(n)[0],first_collision(n)[1][0]) for n in range(1,12)])
print('VERIFY_OK')
