"""Finite exact certificate for capacity-reversal onset in the binary sharing game.

Run: python3 netflix_capacity_census.py
Requires only Python 3.9+ standard library. All arithmetic is integral.
The first 15 edge positions at order six are (0,1),(0,2),...,(4,5).
"""
from collections import Counter
from itertools import permutations

EXPECTED_CONNECTED = {2:1, 3:4, 4:38, 5:728, 6:26704}
EXPECTED_CLASSES = {121:90, 693:360, 127:180, 954:180,
                    639:60, 703:360, 1759:90, 4060:10}

def edges_of(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def neighbors(n, edge_mask, edges):
    nbs=[0]*n
    for h,(i,j) in enumerate(edges):
        if edge_mask & (1<<h):
            nbs[i] |= 1<<j
            nbs[j] |= 1<<i
    return nbs

def connected(nbs):
    n=len(nbs)
    reached=1
    while True:
        next_reached=reached
        for i in range(n):
            if reached & (1<<i):
                next_reached |= nbs[i]
        if next_reached==reached:
            return reached==(1<<n)-1
        reached=next_reached

def feasible(nbs, buyers, capacity):
    """Exact cut-edge cover: each buyer takes precisely min(k, degree) receivers.

    Candidate masks are unions of distinct nomination sets, one per buyer.
    Every nonbuyer must be covered; no buyer is nominated.
    """
    n=len(nbs)
    p=((1<<n)-1)^buyers
    if not p:
        return False
    unions={0}
    for i in range(n):
        if not (buyers & (1<<i)):
            continue
        target=min(capacity,nbs[i].bit_count())
        available=nbs[i]&p
        if available.bit_count()<target:
            return False
        choices=[]
        sub=available
        while sub:
            if sub.bit_count()==target:
                choices.append(sub)
            sub=(sub-1)&available
        if not choices:
            return False
        unions={u|c for u in unions for c in choices}
    return p in unions

def min_buyers(nbs,capacity):
    n=len(nbs)
    for size in range(1,n):
        for buyer_mask in range(1,(1<<n)-1):
            if buyer_mask.bit_count()==size and feasible(nbs,buyer_mask,capacity):
                return size
    raise AssertionError('Connected positive-capacity graph must have equilibrium')

def canonical_map_precomputation(n):
    edges=edges_of(n)
    index={e:i for i,e in enumerate(edges)}
    maps=[]
    for perm in permutations(range(n)):
        maps.append([index[tuple(sorted((perm[i],perm[j])))] for i,j in edges])
    return maps

def canonical_edge_mask(mask,maps):
    best=1<<15
    for mapping in maps:
        new=0
        rem=mask
        while rem:
            lb=rem&-rem
            new |= 1<<mapping[lb.bit_length()-1]
            rem ^= lb
        if new<best:
            best=new
    return best

def main():
    maps=canonical_map_precomputation(6)
    total_per_size={}
    labeled_reversals=[]
    for n in range(2,7):
        es=edges_of(n)
        total=0
        for mask in range(1<<len(es)):
            nbs=neighbors(n,mask,es)
            if not connected(nbs):
                continue
            total+=1
            values=[min_buyers(nbs,k) for k in range(1,n)]
            reversals=[k for k in range(2,n) if values[k-1]>values[k-2]]
            if n<6:
                assert not reversals, (n,mask,values)
            if n==6 and reversals:
                assert reversals==[3], (mask,values)
                assert values[1:3]==[2,3], (mask,values)
                labeled_reversals.append(mask)
        total_per_size[n]=total
    assert total_per_size==EXPECTED_CONNECTED, total_per_size
    assert len(labeled_reversals)==1330
    classes=Counter(canonical_edge_mask(x,maps) for x in labeled_reversals)
    assert dict(classes)==EXPECTED_CLASSES, classes
    tree_codes=[x for x in classes if x.bit_count()==5]
    assert tree_codes==[121]
    assert sum(classes.values())==1330
    print('Connected labeled graphs:',total_per_size)
    print('No reversal on orders 2 through 5')
    print('Order-six labeled reversals:',len(labeled_reversals))
    print('Exactly eight isomorphism classes (canonical edge mask : labeled orbit size):')
    for code,multiplicity in sorted(classes.items(),key=lambda p:(p[0].bit_count(),p[0])):
        print(code, multiplicity)
    print('Only minimum-edge example: the five-edge double-star, canonical mask 121')
    print('PASS')

if __name__=='__main__':
    main()
