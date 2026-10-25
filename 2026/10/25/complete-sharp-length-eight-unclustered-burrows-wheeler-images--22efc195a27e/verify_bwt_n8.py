#!/usr/bin/env python3
"""Exact, standalone census of sharp unclustered BWT images of length eight.
Run: python3 verify_bwt_n8.py (Python 3 standard library only).
"""
from collections import Counter,defaultdict
from itertools import combinations, product, permutations
from math import comb

EXPECTED = {
 '10120121', '10201020', '20212021',
 '10130232', '20312130', '30212031',
}

def reduced(w):
    alpha=sorted(set(w))
    return ''.join(str(alpha.index(x)) for x in w)

def one_cycle(p):
    n=len(p); seen=set(); x=0
    for i in range(n):
        if x in seen: return False
        seen.add(x); x=p[x]
    return x==0 and len(seen)==n

def stable_permutation(w):
    ranks={};out=[]
    sorted_positions=defaultdict(list)
    for i,x in enumerate(sorted(w)): sorted_positions[x].append(i)
    for x in w:
        j=ranks.get(x,0)
        out.append(sorted_positions[x][j])
        ranks[x]=j+1
    return out

def is_sharp_bwt_image(w):
    return (all(x!=y for x,y in zip(w,w[1:]))
            and one_cycle(stable_permutation(w))
            and sum(x!=y for x,y in zip(w,sorted(w)))==4)

# Independent route A: enumerate every candidate after a proved Parikh reduction.
profiles=[(4,4),(4,2,2),(2,4,2),(2,2,4),(2,2,2,2)]
pattern_sets={}
profile_stats={}
for profile in profiles:
    vals=set(permutations(tuple(i for i,n in enumerate(profile) for _ in range(n))))
    hits={''.join(map(str,w)) for w in vals if is_sharp_bwt_image(w)}
    pattern_sets[profile]=hits
    profile_stats[profile]=(len(vals),len(hits))
reduced_hits=set().union(*pattern_sets.values())
assert reduced_hits == EXPECTED, (reduced_hits,EXPECTED)
assert profile_stats == {
    (4,4):(70,0),(4,2,2):(420,1),(2,4,2):(420,1),
    (2,2,4):(420,1),(2,2,2,2):(2520,3)}, profile_stats

# Independent route B: construct the BWT of every primitive necklace over 4 letters;
# compute its runs directly in the original word (not via a permutation formula).
def is_primitive(w):
    n=len(w)
    return not any(n%d==0 and w == w[:d]*(n//d) for d in range(1,n))

def bwt(w):
    n=len(w)
    shifts=[w[i:]+w[:i] for i in range(n)]
    return ''.join(s[-1] for s in sorted(shifts))

def cyclic_runs(w):
    return sum(w[i]!=w[(i+1)%len(w)] for i in range(len(w)))

witness={};direct_hits=set(); tested=0
for w in product('0123',repeat=8):
    s=''.join(w)
    if not is_primitive(s): continue
    tested+=1
    if cyclic_runs(s)!=4: continue
    L=bwt(s)
    if any(L[i]==L[i+1] for i in range(7)):continue
    pat=reduced(L)
    direct_hits.add(pat)
    witness.setdefault(pat,s)
assert direct_hits==EXPECTED,(direct_hits,EXPECTED)
assert tested==4**8 - 4**4, tested # all proper periods divide 4
for pat,u in witness.items():
    L=bwt(u)
    assert reduced(L)==pat and cyclic_runs(u)==4

# Additional direct check for alphabets 3 and 4, taking necklaces only once.
for q in [3,4]:
    images=set()
    for w in product(range(q),repeat=8):
        w=tuple(w)
        if not is_primitive(w):continue
        if cyclic_runs(w)!=4: continue
        shifts=[w[i:]+w[:i] for i in range(8)]
        L=tuple(s[-1] for s in sorted(shifts))
        if all(L[i]!=L[i+1] for i in range(7)):images.add(L)
    target=sum(comb(q,t)*sum(len(v) for p,v in pattern_sets.items() if len(p)==t) for t in [2,3,4])
    assert len(images)==target,(q,len(images),target)

print('Parikh-profile candidates and accepted patterns:')
for p in profiles: print(p,profile_stats[p],sorted(pattern_sets[p]))
print('Independent direct BWT words examined:',tested)
print('All reduced sharp outputs:',sorted(direct_hits))
print('Universal count: 3*C(q,3)+3*C(q,4), q >= 3')
print('VALIDATION_OK')
