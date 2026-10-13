#!/usr/bin/env python3
"""Independent conflict-graph exhaustive verification (enumerates flag sets directly)."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import csv
U=tuple(range(6))
P=tuple(combinations(U,2))
def matchings(pool):
    if not pool:
        yield frozenset()
    else:
        x=pool[0]
        for y in pool[1:]:
            for tail in matchings(tuple(z for z in pool if z not in (x,y))):
                yield frozenset({(x,y)}) | tail
L=tuple(sorted(matchings(U), key=lambda a:tuple(sorted(a))))
assert len(L)==15
flags=tuple((p,l) for p in P for l in range(15) if frozenset({p})<=L[l])
assert len(flags)==45
compatible=[0]*len(flags)
upper=[0]*len(flags)
for i,(p,l) in enumerate(flags):
    for j,(q,m) in enumerate(flags):
        if i!=j and p!=q and l!=m and p not in L[m] and q not in L[l]:
            compatible[i] |= 1<<j
            if j>i: upper[i] |= 1<<j
allbits=(1<<45)-1
coefs=Counter(); maximal=Counter(); extensions=Counter(); top=[]

def visit(sel,candidates,available):
    k=len(sel)
    coefs[k]+=1
    # Extension count checks all 45 flags, including those preceding the current set.
    ext=sum(1 for i in range(45) if available>>i&1)
    extensions[(k,ext)]+=1
    if ext==0:
        maximal[k]+=1
    if k==9:
        top.append(tuple(sel))
    while candidates:
        bit=candidates & -candidates
        candidates-=bit
        i=bit.bit_length()-1
        visit(sel+(i,),candidates & upper[i],available & compatible[i])

visit((),allbits,allbits)
assert [coefs[k] for k in range(10)] == [1,45,720,5160,16920,22680,8520,720,90,10]
assert sum(coefs.values())==54866
assert dict(maximal)=={5:3060,6:5520,7:360,9:10}
assert len(top)==10 and len(set(top))==10
assert extensions[(8,1)] == 90 and sum(v for (k,e),v in extensions.items() if k==8 and e!=1)==0
root=Path(__file__).resolve().parent
with (root/'spectrum.csv').open(newline='',encoding='utf8') as f:
    rows=list(csv.DictReader(f))
assert [(int(r['edges']),int(r['induced_matchings']),int(r['inclusion_maximal_induced_matchings'])) for r in rows]==[(k,coefs[k],maximal[k]) for k in range(10)]
with (root/'maxima.csv').open(newline='',encoding='utf8') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==10
flag_index={(P.index(p), l): i for i,(p,l) in enumerate(flags)}
recorded=set(frozenset(flag_index[tuple(map(int,flag.split(':')))] for flag in row['nine_flags_duad_idx:syntheme_idx'].split(';')) for row in rows)
assert recorded=={frozenset(F) for F in top}
print('VERIFY_CONFLICT_OK flags=45 enumerated_induced_matchings=54866 polynomial=1,45,720,5160,16920,22680,8520,720,90,10')
print('VERIFY_CONFLICT_OK inclusion_maximal=5:3060,6:5520,7:360,9:10')
print('VERIFY_CONFLICT_OK size8_unique_extension=90/90 size9=10')
