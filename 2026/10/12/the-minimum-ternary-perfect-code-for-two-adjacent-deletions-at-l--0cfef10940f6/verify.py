"""Finite exact verification for a ternary perfect two-burst deletion code."""
from itertools import product
from functools import lru_cache
from collections import Counter

alphabet='012'
witness=('02200','01001','10021','11002','21012','22120','21111','20122')

def shadows(x):
    return {x[:i]+x[i+2:] for i in range(4)}

universe={''.join(a) for a in product(alphabet,repeat=3)}
seen={}
for x in witness:
    assert len(x)==5 and set(x)<=set(alphabet)
    for y in shadows(x):
        assert y not in seen, ('non-disjoint', x,y,seen.get(y))
        seen[y]=x
assert set(seen)==universe and len(witness)==8
words=[''.join(a) for a in product(alphabet,repeat=5)]
index={x:i for i,x in enumerate(sorted(universe))}
masks=[]
covers=[[] for _ in range(27)]
for j,x in enumerate(words):
    m=sum(1<<index[y] for y in shadows(x))
    masks.append(m)
    for t in range(27):
        if m>>t&1:covers[t].append(j)

@lru_cache(None)
def impossible(uncovered,left):
    if uncovered==0:return False
    if left==0 or uncovered.bit_count()>4*left:return True
    remaining=uncovered.bit_count()
    need=max(1,remaining-4*(left-1))
    trials=None
    for t in range(27):
        if not(uncovered>>t&1):continue
        options=[j for j in covers[t] if (masks[j]&uncovered).bit_count()>=need]
        if not options:return True
        if trials is None or len(options)<len(trials):trials=options
    return all(impossible(uncovered&~masks[j],left-1) for j in trials)

assert impossible((1<<27)-1,7), 'A seven-word covering code was found'
print('VERIFY_OK',len(words),len(universe),'witness',len(witness), 'states',impossible.cache_info().currsize)
