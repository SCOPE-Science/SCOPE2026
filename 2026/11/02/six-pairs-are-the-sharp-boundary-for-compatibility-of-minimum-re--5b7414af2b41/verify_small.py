#!/usr/bin/env python3
"""Optional finite regression for every complete strict n=3 market.

The universal small-market conclusion is proved analytically in RESULT.md.
"""
from itertools import product,permutations
PERMS=list(permutations(range(3)))
INVERSE_RANK=[{v:k+1 for k,v in enumerate(p)} for p in PERMS]
count=0
for prof in product(range(6),repeat=6):
    ranks=[INVERSE_RANK[t] for t in prof]
    candidates=[]
    for m in PERMS:
        inverse=[m.index(j) for j in range(3)]
        if any(ranks[i][j]<ranks[i][m[i]] and ranks[3+j][i]<ranks[3+j][inverse[j]]
               for i in range(3) for j in range(3) if j!=m[i]):
            continue
        attained=[ranks[i][m[i]] for i in range(3)]+[ranks[3+j][inverse[j]] for j in range(3)]
        candidates.append((m,max(attained)-min(attained),max(attained)))
    mingap=min(x[1] for x in candidates)
    minreg=min(x[2] for x in candidates)
    assert any(x[1]==mingap and x[2]==minreg for x in candidates)
    count+=1
assert count==46656
print('PASS: common optimum in all',count,'strict complete 3x3 profiles')
