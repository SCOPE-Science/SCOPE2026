"""Independent exhaustive verification of power domination on Kneser K(n,2).

Usage: python verify_power_kneser.py
Only the Python standard library is required.
"""
from itertools import combinations
from math import comb
from collections import Counter
import random
import json


def adjacency(n):
    pairs = list(combinations(range(n), 2))
    neighborhoods = []
    for a, b in pairs:
        mask = 0
        for i, (c, d) in enumerate(pairs):
            if a != c and a != d and b != c and b != d:
                mask |= 1 << i
        neighborhoods.append(mask)
    return pairs, neighborhoods


def power_dominates(mask, neighborhoods):
    """Direct original rule: closed-neighborhood observation, then forcing."""
    full = (1 << len(neighborhoods)) - 1
    observed = mask
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        observed |= neighborhoods[bit.bit_length()-1]
        remaining -= bit
    while observed != full:
        new = observed
        remaining = observed
        while remaining:
            bit = remaining & -remaining
            white_neighbors = neighborhoods[bit.bit_length()-1] & ~observed
            if white_neighbors and white_neighbors & (white_neighbors-1) == 0:
                new |= white_neighbors
            remaining -= bit
        if new == observed:
            return False
        observed = new
    return True


def predicted(n, pairs, chosen):
    k=len(chosen)
    if k==0 or k==1:
        return False
    if n==5 and k==2:
        return bool(set(pairs[chosen[0]]) & set(pairs[chosen[1]]))
    if k==2:
        return False
    if n <= 7:
        return True
    common = set(pairs[chosen[0]])
    for i in chosen[1:]:
        common.intersection_update(pairs[i])
        if not common:
            return True
    return k >= n-4


def predicted_coeff(n,k):
    N=comb(n,2)
    if k<2:
        return 0
    if n==5 and k==2:
        return 30
    if k==2:
        return 0
    return comb(N,k) - (n*comb(n-1,k) if n>=8 and 3<=k<=n-5 else 0)


def choose_masks(N,k):
    for c in combinations(range(N),k):
        yield c, sum(1 << i for i in c)

checks=[]
for n in (5,6,7):
    pairs, nei = adjacency(n)
    N=len(pairs)
    counts=Counter()
    for m in range(1<<N):
        chosen=[i for i in range(N) if m>>i&1]
        got=power_dominates(m,nei)
        want=predicted(n,pairs,chosen)
        assert got==want,(n,chosen,got,want)
        if got:
            counts[len(chosen)]+=1
    for k in range(N+1):
        assert counts[k]==predicted_coeff(n,k),(n,k,counts[k],predicted_coeff(n,k))
    checks.append({'n':n,'type':'all_subsets','checked':1<<N,
                   'minimum':min(counts),'minimum_count':counts[min(counts)]})

# Independent size-restricted direct checks for larger orders.
for n, max_k in ((8,4),(9,4),(10,3),(11,3)):
    pairs, nei=adjacency(n)
    counts=Counter()
    checked=0
    for k in range(max_k+1):
        for chosen,mask in choose_masks(len(pairs),k):
            got=power_dominates(mask,nei)
            want=predicted(n,pairs,chosen)
            assert got==want,(n,chosen,got,want)
            checked+=1
            if got:
                counts[k]+=1
        assert counts[k]==predicted_coeff(n,k),(n,k,counts[k],predicted_coeff(n,k))
    checks.append({'n':n,'type':f'all_subsets_up_to_{max_k}',
                   'checked':checked,'counts':{str(k):counts[k] for k in range(max_k+1)}})

# Check the predicted extra inclusion-minimal star sets for several orders.
for n in range(8,14):
    pairs, nei=adjacency(n)
    index={edge:i for i,edge in enumerate(pairs)}
    checked=0
    for center in range(n):
        for leaves in combinations([i for i in range(n) if i!=center],n-4):
            chosen=[index[tuple(sorted((center,x)))] for x in leaves]
            mask=sum(1<<i for i in chosen)
            assert power_dominates(mask,nei), (n,center,leaves)
            for j in chosen:
                assert not power_dominates(mask^(1<<j),nei), (n,center,leaves,j)
            checked+=1
    assert checked==n*comb(n-1,3)
    checks.append({'n':n,'type':'all_minimal_large_stars', 'checked':checked})

rng=random.Random(923587)
for n in range(8,14):
    pairs,nei=adjacency(n)
    checked=0
    for _ in range(1000):
        k=rng.randrange(0,len(pairs)+1)
        chosen=rng.sample(range(len(pairs)),k)
        mask=sum(1<<i for i in chosen)
        assert power_dominates(mask,nei)==predicted(n,pairs,chosen)
        checked+=1
    checks.append({'n':n,'type':'random_sizes_seed_923587','checked':checked})

print(json.dumps({'status':'PASS','definition':'closed-neighborhood then one-white-neighbor forcing',
                  'checks':checks, 'total_checked':sum(c['checked'] for c in checks)},indent=2))
