"""Exact independent set-based enumeration for the five-term valuation-one problem."""
from itertools import combinations
from collections import Counter
R=tuple(v for v in range(25) if v%5)
target={5,10,15,20}
visits=Counter(); bad10=[]
def go(start, seq, reachable):
    visits[len(seq)] += 1
    if len(seq)==10:
        bad10.append(seq)
    if len(seq)==11:
        raise AssertionError('eleven-element counterexample')
    for i in range(start,len(R)):
        r=R[i]
        nxt=list(reachable)
        for j in range(5,0,-1):
            nxt[j] = reachable[j] | {(x+r)%25 for x in reachable[j-1]}
        if nxt[5].isdisjoint(target):
            go(i, seq+(r,), tuple(nxt))
go(0,(),(frozenset({0}),)+tuple(frozenset() for _ in range(5)))
assert visits[10]==3900 and visits[11]==0,visits
example=bad10[0]
assert all(sum(z)%25 not in target for z in combinations(example,5))
print('VERIFY_OK visits='+str(dict(sorted(visits.items())))+' witness='+str(example))
