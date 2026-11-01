#!/usr/bin/env python3
"""Independent vertex-level cross-check; intentionally does not use profiles."""
from collections import Counter
from count_profiles import census

def step(x,n):
    y=0
    for col in range(n):
        for row in range(3):
            i=row*n+col
            own=(x>>i)&1
            neighbors=sum((x>>(row*n+c))&1 for c in range(n) if c!=col)
            neighbors+=sum((x>>(r*n+col))&1 for r in range(3) if r!=row)
            value=(1 if 2*neighbors>n+1 else (0 if 2*neighbors<n+1 else own))
            y|=value<<i
    return y

def first_period(x,n):
    seen={};k=0
    while x not in seen:
        seen[x]=k;x=step(x,n);k+=1
    return k-seen[x],seen[x]

for n in range(2,7):
    count=Counter(first_period(s,n) for s in range(1<<(3*n)))
    expected=census(n)
    assert count==expected,(n,count,expected)
    print('n',n,'labelled',1<<(3*n),'MATCH',sorted(count.items()))
print('INDEPENDENT_VERTEX_CHECK_OK')
