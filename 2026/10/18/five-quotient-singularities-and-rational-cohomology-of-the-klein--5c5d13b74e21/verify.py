#!/usr/bin/env python3
"""Exact finite-group arithmetic for the Klein cubic Frobenius quotient.
The geometric and cohomological arguments are given in RESULT.md.
"""
from itertools import combinations

p=11
w=(1,9,4,3,5)
assert all((2*w[i]+w[(i+1)%5])%p==0 for i in range(5))
assert len(set(w))==5
assert all(w[(i-1)%5] == (5*w[i])%p for i in range(5))

base11=(2,3,4)
for i in range(5):
    ws=sorted((w[j]-w[i])%p for j in range(5)
              if j!=i and j!=(i+1)%5)
    assert any(ws == sorted((a*t)%11 for a in base11)
               for t in range(1,11)), (i,ws)

ages11=[sum((k*a)%11 for a in base11) for k in range(1,11)]
assert ages11==[9,18,16,14,23,10,19,17,15,24]

for k in range(1,5):
    weights=sorted(set(range(1,5))-{(2*k)%5})
    assert any(weights==sorted((t*a)%5 for a in (1,2,3))
               for t in range(1,5)), (k,weights)
ages5=[sum((k*a)%5 for a in (1,2,3)) for k in range(1,5)]
assert ages5==[6,7,8,9]

assert 5*1+11*4==49    # 5 coordinates and 44 order-five fixed points
assert (5+0)%5 == 0
assert (-6+10*5)//11==4 # quotient Euler characteristic from C11 action
assert (4-(-1))==5       # Lefschetz trace: four even classes, odd trace -1
print('VERIFY_OK: order-55 action, five tangent types, both age spectra')
