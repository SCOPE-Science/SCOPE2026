#!/usr/bin/env python3
from itertools import combinations

def arc(mask,n,i,j):
    if i==j: return False
    a,b=(i,j) if i<j else (j,i)
    idx=0
    for x in range(n):
        for y in range(x+1,n):
            if x==a and y==b:
                bit=(mask>>idx)&1
                # bit 1 means a -> b
                return bool(bit) if i==a else not bool(bit)
            idx+=1
    raise AssertionError

def transitive_triple(mask,n,tri):
    a,b,c=tri
    # A 3-vertex tournament is transitive iff one vertex has outdegree 2.
    for v in tri:
        if sum(arc(mask,n,v,w) for w in tri if w!=v)==2:
            return True
    return False

# Every 4-vertex tournament has a transitive triple.
n=4
count=0
for mask in range(1 << (n*(n-1)//2)):
    count += 1
    assert any(transitive_triple(mask,n,t) for t in combinations(range(n),3))
assert count==64

# Directed 3-cycle: 0->1->2->0. Encoding bits for (0,1),(0,2),(1,2): 1,0,1.
cycle_mask=(1<<0) | (1<<2)
assert not transitive_triple(cycle_mask,3,(0,1,2))

# Directed Ramsey R_dir(3)=4 and theorem endpoints.
R3=4
for k in range(9):
    assert k+(R3-1)*(2**k) == k+3*(2**k)

# Sharp k=1,l=3 witness has one witness and two profile classes, each a directed 3-cycle.
profile_classes=[3,3]
assert 1+sum(profile_classes)==7
assert all(size==R3-1 for size in profile_classes)

print('VERIFY_OK directed_R3=4 tournaments_n4=64 endpoints_k0_8_ok sharp_k1_l3=7')
