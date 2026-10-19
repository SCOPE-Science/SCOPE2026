#!/usr/bin/env python3
"""Finite exhaustive verifier for ordinary zero forcing on the 4-cube."""
from collections import Counter
from itertools import permutations
import json

N=16
FULL=(1<<N)-1
ADJ=[sum(1<<(v^(1<<i)) for i in range(4)) for v in range(N)]
EXPECTED={8:2360,9:6016,10:6240,11:4032,12:1792,13:560,14:120,15:16,16:1}

def closure(initial):
    black=initial
    steps=0
    while black!=FULL:
        newly=0
        for v in range(N):
            if black&(1<<v):
                white_neighbors=ADJ[v]&~black
                if white_neighbors and white_neighbors.bit_count()==1:
                    newly|=white_neighbors
        if newly==0:
            return False,steps
        black|=newly
        steps+=1
    return True,steps

truth=[False]*(FULL+1)
prop={}
counts=Counter()
for mask in range(FULL+1):
    force,rounds=closure(mask)
    truth[mask]=force
    if force:
        counts[mask.bit_count()]+=1
        prop[mask]=rounds
assert dict(counts)==EXPECTED,counts
assert sum(counts.values())==21137
minimal=[m for m in range(FULL+1) if truth[m] and all(not truth[m^(1<<v)] for v in range(N) if m&(1<<v))]
assert len(minimal)==2360 and all(m.bit_count()==8 for m in minimal)
assert Counter(prop[m] for m in minimal)=={1:8,2:816,3:1152,4:384}

# Every automorphism is x -> a xor sigma(x): the image of 0 has 16 choices,
# and the 4 neighbors of 0 can be permuted in at most 4! ways. The maps
# below realize all 384 possibilities, and each preserves every edge.
perms=[]
for sigma in permutations(range(4)):
    for a in range(16):
        image=[a^sum(((v>>k)&1)<<sigma[k] for k in range(4)) for v in range(16)]
        assert all(ADJ[v].bit_count()==4 for v in range(16))
        assert all(((image[v]^image[v^(1<<k)]).bit_count()==1) for v in range(16) for k in range(4))
        perms.append(image)
assert len({tuple(p) for p in perms})==384

def act(s,p):
    t=0
    for v in range(16):
        if s&(1<<v):t|=1<<p[v]
    return t

def orbit_table(sets):
    remaining=set(sets)
    answer=[]
    while remaining:
        x=min(remaining)
        orb={act(x,p) for p in perms}
        assert orb<=remaining
        remaining.difference_update(orb)
        answer.append({'representative':x,'size':len(orb),'rounds':prop[x]})
    return answer
orbits=orbit_table(minimal)
assert len(orbits)==11
assert Counter(o['size'] for o in orbits)=={384:4,192:3,96:2,48:1,8:1}
assert Counter(o['rounds'] for o in orbits)=={1:1,2:6,3:3,4:1}
if __name__=='__main__':
    print('FORCING_OK tested=65536 zero_forcing=21137 polynomial='+str(sorted(counts.items())))
    print('FORCING_OK minimum=8 count=2360 all_inclusion_minimal=2360 propagation_times='+str(sorted(Counter(prop[m] for m in minimal).items())))
    print('FORCING_ORBITS_OK automorphisms=384 orbits=11 orbit_sizes='+str(sorted(Counter(o['size'] for o in orbits).items())))
    print('FORCING_REPRESENTATIVES='+json.dumps(orbits,separators=(',',':')))
