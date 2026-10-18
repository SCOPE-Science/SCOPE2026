#!/usr/bin/env python3
"""Separate enumeration of every 2-space in the 9-space over GF(2)."""
from collections import Counter
from verify import smooth, q, bitquad

smooth_flags=[False]+[smooth(i) for i in range(1,512)]
all_spaces=set()
for a in range(1,512):
    for b in range(a+1,512):
        all_spaces.add(tuple(sorted((a,b,a^b))))
assert len(all_spaces)==43435
quadric_points=[p for p in range(1,16) if not q(p)]
hist=Counter()
for triple in all_spaces:
    if all(smooth_flags[v] for v in triple):
        b=sum(all(not bitquad(v,p) for v in triple)
              for p in quadric_points)
        hist[b]+=1
assert dict(hist)=={0:1440,1:1920,2:540,3:120}
print('PASS: all 43,435 two-dimensional subspaces independently enumerated')
print('PASS: all-smooth base incidence (1440,1920,540,120)')
