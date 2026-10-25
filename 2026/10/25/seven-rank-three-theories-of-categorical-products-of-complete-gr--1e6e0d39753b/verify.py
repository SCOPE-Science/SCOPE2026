"""Reproduce three-round theories of finite tensor products of complete graphs.

All graphs are simple and have vertex sets which are finite coordinate words.
Two independent checks are used: exhaustive 3-vertex extension signatures,
and a recursive Spoiler/Duplicator game for representatives.
"""
from itertools import product, combinations_with_replacement
from functools import lru_cache
from collections import defaultdict
from math import prod

REPRESENTATIVES = {
    'complete_two': (2,),
    'complete_at_least_three': (3,),
    'binary_two_factors': (2,2),
    'binary_at_least_three_factors': (2,2,2),
    'mixed_two_factors': (2,3),
    'mixed_at_least_three_factors': (2,2,3),
    'no_binary_at_least_two_factors': (3,3),
}

def category(qs):
    assert len(qs) >= 1 and min(qs)>=2
    d=len(qs)
    if d==1:return 'complete_two' if qs[0]==2 else 'complete_at_least_three'
    nb=sum(q==2 for q in qs)
    if nb==d:return 'binary_two_factors' if d==2 else 'binary_at_least_three_factors'
    if nb==0:return 'no_binary_at_least_two_factors'
    return 'mixed_two_factors' if d==2 else 'mixed_at_least_three_factors'

def graph(qs):
    vertices=list(product(*(range(q) for q in qs)))
    edges=[[all(x!=y for x,y in zip(a,b)) for b in vertices] for a in vertices]
    return vertices,edges

def signature(qs):
    v,e=graph(qs)
    N=len(v)
    result=set()
    for j in range(1,N):
        ext=set()
        for k in range(N):
            if k not in (0,j):ext.add((int(e[0][k]),int(e[j][k])))
        result.add((int(e[0][j]),tuple(sorted(ext))))
    return tuple(sorted(result))

def symbolic_signature(qs):
    d=len(qs);profile=set()
    for marks in product((0,1),repeat=d):
        if not any(marks): continue
        # marks: coordinates where the second vertex differs from the first
        adj=all(marks)
        common=all(q>=3 for q,m in zip(qs,marks) if m)
        if adj:
            single=(d>=2 and any(q>=3 for q in qs))
            neither=(d>=2)
        else:
            single=True
            if d>=3:neither=True
            else:
                other=next(i for i,m in enumerate(marks) if m)
                neither=qs[other]>=3
        ext=[]
        if common:ext.append((1,1))
        if single:ext.extend(((1,0),(0,1)))
        if neither:ext.append((0,0))
        profile.add((int(adj),tuple(sorted(ext))))
    return tuple(sorted(profile))

for sizes in REPRESENTATIVES.values():
    assert signature(sizes)==symbolic_signature(sizes)
rsigs={name:signature(qs) for name,qs in REPRESENTATIVES.items()}
assert len(set(rsigs.values()))==7
print('REPRESENTATIVES_OK classes=7 smallest_maximum_order=12')

# Independent exhaustive enumerator for each complete graph, with actual edge relations.
count=0
for d in range(1,6):
    for qs in combinations_with_replacement((2,3,4,5),d):
        if prod(qs)>100:continue
        sig=signature(qs)
        assert sig==rsigs[category(qs)],(qs,sig,category(qs))
        assert sig==symbolic_signature(qs)
        count+=1
print(f'DIRECT_ATOMIC_EXTENSION_OK instances={count} factors=1..5 alphabets=2..5 order<=100')

# Exhaustive symbolic check over up to 8 factors, a possibly very large graph.
count=0
for d in range(1,9):
    for qs in combinations_with_replacement((2,3,4,7),d):
        assert symbolic_signature(qs)==rsigs[category(qs)]
        count+=1
print(f'SYMBOLIC_ALL_FACTOR_PATTERNS_OK instances={count} factors=1..8 alphabets=2,3,4,7')

# Completely independent 3-round game, not using extension signatures.
def equivalent(qs, rs, rounds=3):
    A, ea=graph(qs);B,eb=graph(rs)
    @lru_cache(None)
    def win(t,aa,bb):
        for i,x in enumerate(aa):
            for j,y in enumerate(aa):
                if (x==y)!=(bb[i]==bb[j]) or ea[x][y]!=eb[bb[i]][bb[j]]:
                    return False
        if t==0:return True
        for x in range(len(A)):
            if not any(win(t-1,aa+(x,),bb+(y,)) for y in range(len(B))):return False
        for y in range(len(B)):
            if not any(win(t-1,aa+(x,),bb+(y,)) for x in range(len(A))):return False
        return True
    return win(rounds,(),())

reps=list(REPRESENTATIVES.items())
for i,(an,a) in enumerate(reps):
    for j,(bn,b) in enumerate(reps):
        if j<i:continue
        assert equivalent(a,b)==(i==j),(an,bn)
print('INDEPENDENT_THREE_ROUND_GAME_OK representatives=7 pairwise_games=28')

samples=((2,3),(2,4),(3,3),(3,5),(2,2,2),(2,2,3),(2,3,3),(2,2,2,2))
for q in samples:
    r=REPRESENTATIVES[category(q)]
    assert equivalent(q,r),(q,r)
print('CROSS_SIZE_THREE_ROUND_GAMES_OK instances=8')
print('VERIFY_OK')
