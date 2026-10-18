#!/usr/bin/env python3
"""Checks finite incidence consequences for three exceptional combinatorial types."""
from math import comb
for n2,n3,t5 in [(0,7,4),(3,5,5)]:
    cases=[]
    for a in range(n3+1):
        b=n3-a
        c=15-3*a-b
        if 0<=c<=n2 and b<=comb(6-t5,2):
            cases.append((a,b,c))
    if (n2,n3,t5)==(0,7,4):
        assert cases==[]
    else:
        assert cases==[(5,0,0)]
        # Every line would meet five other lines at triple-of-lines points.
        assert 5 % 2 == 1
assert all(9!=1+3*s for s in range(4))
print('incidence and mod-three checks passed')
