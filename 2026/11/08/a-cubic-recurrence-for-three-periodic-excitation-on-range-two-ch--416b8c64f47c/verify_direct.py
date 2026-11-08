#!/usr/bin/env python3
"""Exhaustive direct dynamical check, independent of the transfer algorithm."""
from itertools import product

def step(x):
    n = len(x)
    y = []
    for i, state in enumerate(x):
        if state == 1:
            y.append(2)
        elif state == 2:
            y.append(0)
        else:
            y.append(int(any(x[j] == 1 for j in range(max(0,i-2),min(n,i+3)) if j!=i)))
    return tuple(y)

def support(x):
    n = len(x)
    return all(any((x[j]-x[i])%3==1 for j in range(max(0,i-2), min(n,i+3)) if j!=i)
               for i in range(n))

counts = []
examined = 0
for n in range(3,12):
    total = 0
    for x in product(range(3), repeat=n):
        after1=step(x)
        after2=step(after1)
        after3=step(after2)
        cyclic3=(after3==x and after1!=x)
        assert cyclic3 == support(x), f'disagreement n={n}, x={x}'
        total += cyclic3
        examined += 1
    counts.append(total)
    if len(counts)>=4:
        assert counts[-1]==3*counts[-2]-2*counts[-3]+2*counts[-4]
assert counts==[6,18,42,102,258,654,1650,4158,10482]
print('COMPLETE_STATES:',examined)
print('COUNTS_n3_to_n11:',counts)
print('TRANSFER_INDEPENDENT_CHECK: direct F^3 vs exact local condition')
print('PASS')
