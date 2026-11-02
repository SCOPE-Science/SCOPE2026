#!/usr/bin/env python3
"""Independent abstract truth-vector version-space algorithm."""
from functools import lru_cache
from itertools import product

def calculate(t,s):
    # Abstract values: a 3-valued arm has two nested tests, a leaf one.
    # Outside point has zero on every test, but root query distinguishes it.
    rows=[tuple([0]*(1+2*t+s))]
    for choice in product(range(3), repeat=t):
        for leaf in product(range(2), repeat=s):
            answers=[1]
            for val in choice:
                answers += [int(val>=1),int(val>=2)]
            answers+=list(leaf)
            rows.append(tuple(answers))
    assert len(rows)==1+3**t*2**s
    @lru_cache(None)
    def depth(state):
        res=0
        for c in range(len(rows[0])):
            y=tuple(i for i in state if rows[i][c])
            z=tuple(i for i in state if not rows[i][c])
            if y and z:
                res=max(res,1+min(depth(y),depth(z)))
        return res
    return depth(tuple(range(len(rows))))

cases=0
for t in range(5):
 for s in range(5):
    if 3**t*2**s>175:continue
    got=calculate(t,s)
    want=t+s+int(s==0)
    assert got==want,(t,s,got,want)
    cases+=1
    print(f'PRODUCT_RECURRENCE_PASS t={t} s={s} Ldim={got}')
print(f'ABSTRACT_ALL_PASS cases={cases}')
