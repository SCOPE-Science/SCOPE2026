#!/usr/bin/env python3
"""Self-contained exact checks for translation traces of six-cube scale-four Rips."""
from functools import lru_cache
from math import comb

N=64
ADJ=[sum(1<<y for y in range(N) if (x^y).bit_count()>4) for x in range(N)]
assert all(mask.bit_count()==7 for mask in ADJ)
assert all(bool(ADJ[x]&(1<<y)) == ((x^y).bit_count()>4) for x in range(N) for y in range(N))

def polynomial_at_minus_one(neighbors, mask):
    @lru_cache(None)
    def go(S):
        if not S: return 1
        # Maximum-degree pivot, with exact inclusion/exclusion.
        v=max((i for i in range(len(neighbors)) if S>>i&1),key=lambda i:(S&neighbors[i]).bit_count())
        bit=1<<v
        return go(S^bit)-go(S&~(bit|neighbors[v]))
    result=go(mask)
    return result,go.cache_info().currsize

identity, visited=polynomial_at_minus_one(ADJ,(1<<64)-1)
assert identity==253
print('identity signed face count:',identity,'distinct recursion states:',visited)

# Independent, non-memoized count of orbit-independent subsets by parity.
def parity_census(neighbors, eligible):
    even=odd=0
    def rec(S,parity):
        nonlocal even,odd
        if not S:
            if parity:odd+=1
            else:even+=1
            return
        v=max((i for i in range(32) if S>>i&1),key=lambda i:(S&neighbors[i]).bit_count())
        bit=1<<v
        rec(S^bit,parity)
        rec(S&~(bit|neighbors[v]),1-parity)
    rec(eligible,0)
    return even,odd

character=[identity]
orbit_counts={}
for w in range(1,7):
    t=(1<<w)-1
    reps=[x for x in range(N) if x < (x^t)]
    assert len(reps)==32
    indices={v:i for i,r in enumerate(reps) for v in (r,r^t)}
    neighbors=[0]*32
    allowed=0
    for i,r in enumerate(reps):
        if not (ADJ[r] & (1<<(r^t))):allowed|=1<<i
        for v in (r,r^t):
            near=ADJ[v]
            while near:
                bit=near&-near
                j=indices[bit.bit_length()-1]
                if i!=j:neighbors[i]|=1<<j
                near^=bit
    assert all(neighbors[i]>>j&1 == neighbors[j]>>i&1 for i in range(32) for j in range(32))
    fast,states=polynomial_at_minus_one(neighbors,allowed)
    even,odd=parity_census(neighbors,allowed)
    assert fast==even-odd
    orbit_counts[w]=(allowed.bit_count(),even,odd)
    character.append(fast)
    print('translation weight:',w,'orbits eligible:',allowed.bit_count(),'even:',even,'odd:',odd,'trace:',fast)

assert character==[253,9,9,53,53,1,1]
multiplicities=[]
for a in range(N):
    numerator=sum(character[t.bit_count()] * (-1 if (a&t).bit_count()%2 else 1) for t in range(N))
    assert numerator%N==0
    multiplicities.append(numerator//N)
    assert multiplicities[-1]>=0
by_weight=[]
for k in range(7):
    vals={multiplicities[a] for a in range(N) if a.bit_count()==k}
    assert len(vals)==1
    by_weight.append(vals.pop())
assert by_weight==[36,1,0,6,6,0,1]
assert sum(comb(6,k)*by_weight[k] for k in range(7))==253
assert sum(comb(6,w)*character[w] for w in range(7))==N*36
print('CHARACTER',character)
print('FOURIER_MULTIPLICITIES_BY_DUAL_WEIGHT',by_weight)
print('TRANSLATION_FIXED_HOMOLOGY_DIMENSION',multiplicities[0])
print('Q6_RIPS_SCALE4_TRANSLATION_CHECKS_OK')
