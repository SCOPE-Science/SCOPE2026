#!/usr/bin/env python3
"""Independent exact tour computation for complement-tandem four-mer coverage.

Standard library only; exhaustive Held--Karp recurrence on 16 targets, with
an explicit cyclic witness and independent structural-orbit checks.
"""
from itertools import product

BAR = {"0":"1", "1":"0", "2":"3", "3":"2"}
ALPHABET = tuple("0123")
WITNESS = "00110013021303120312233223"
TARGETS = tuple(a+b+BAR[a]+BAR[b] for a,b in product(ALPHABET, repeat=2))

def overlap_step(u, v):
    return next(s for s in range(1, 5) if u[s:] == v[:4-s])

def check_witness():
    assert len(TARGETS) == len(set(TARGETS)) == 16
    assert len(WITNESS) == 26
    windows = {''.join(WITNESS[(i+j) % 26] for j in range(4)) for i in range(26)}
    assert set(TARGETS) <= windows
    return sorted(set(TARGETS)&windows)

def check_orbits():
    unseen = {(a,b) for a,b in product(ALPHABET, repeat=2)}
    orbits = []
    while unseen:
        a,b = min(unseen)
        orb = []
        for _ in range(4):
            assert (a,b) in unseen
            unseen.remove((a,b));orb.append((a,b))
            a,b = b,BAR[a]
        assert (a,b) == orb[0]
        orbits.append(orb)
    assert len(orbits) == 4
    for i,u in enumerate(TARGETS):
        a,b = u[:2]
        x=(b,BAR[a]); y=(BAR[a],BAR[b]);
        for j,v in enumerate(TARGETS):
            d=overlap_step(u,v)
            if d == 1: assert v[:2] == ''.join(x)
            if d == 2: assert v[:2] == ''.join(y)
            if d == 3: assert v[0] == BAR[b]
    return orbits

def tour_optimum():
    n = len(TARGETS)
    costs = [[overlap_step(u,v) for v in TARGETS] for u in TARGETS]
    # Fix first target to eliminate cyclic rotational symmetry.
    # Each DP state holds exact min path cost with first target 0,
    # set of visited targets mask, and current terminal target j.
    prev = {(1,0):0}
    for count in range(1,n):
        nxt = {}
        for (mask,j),val in prev.items():
            rest=((1<<n)-1) ^ mask
            while rest:
                bit=rest&-rest
                k=bit.bit_length()-1
                key=(mask|bit,k)
                z=val+costs[j][k]
                if z < nxt.get(key,10**9):nxt[key]=z
                rest-=bit
        prev=nxt
    full=(1<<n)-1
    answer=min(val+costs[j][0] for (mask,j),val in prev.items() if mask==full)
    assert answer==26,(answer,'not 26')
    return answer

if __name__=='__main__':
    targets=check_witness()
    orbits=check_orbits()
    optimum=tour_optimum()
    print('VERIFIED: 16 distinct motifs, 4 four-target overlap orbits')
    print('VERIFIED: circular witness length 26 covers all 16 motifs')
    print('VERIFIED: independent exact 16-vertex Held-Karp cyclic optimum',optimum)
    print('ORBIT_LENGTHS', [len(o) for o in orbits])
    print('VERIFY_OK')
