#!/usr/bin/env python3
"""Independent finite two-variable, no-counting logical-type refinement.

All structures are considered simultaneously so types are comparable across
structures. The set-valued recurrence implements ordinary (not counting) FO2.
"""
from itertools import product
from collections import defaultdict

MAX_SIDE = 9
rectangles = [(a,b) for b in range(1,MAX_SIDE+1) for a in range(1,b+1)]
rel_rows, blocks = [], []
start = 0
for a,b in rectangles:
    points = list(product(range(a),range(b)))
    indices = list(range(start,start+len(points)))
    blocks.append(((a,b),indices))
    for x in points:
        rel_rows.append(tuple(
            0 if x==y else
            1 if (x[0]<=y[0] and x[1]<=y[1]) else
            2 if (y[0]<=x[0] and y[1]<=x[1]) else 3
            for y in points))
    start += len(points)

labels=[0]*start
counts=[]
for depth in range(1, MAX_SIDE*2+5):
    keys=[]
    for rect,indices in blocks:
        for i in indices:
            keys.append(frozenset((relation,labels[j])
                                  for relation,j in zip(rel_rows[i],indices)))
    canon={k:i for i,k in enumerate(sorted(set(keys),key=repr))}
    new_labels=[canon[k] for k in keys]
    theories={rect:frozenset(new_labels[i] for i in indices)
              for rect,indices in blocks}
    counts.append(len(set(theories.values())))
    labels=new_labels
    if counts[-1]==len(rectangles):
        break
assert counts[-1]==len(rectangles), (counts,len(rectangles))
print('PASS: jointly refined',len(rectangles),'nonisomorphic finite rectangles.')
print('PASS: distinct FO2 theories by refinement depth:',counts)
print('PASS: every rectangle in the tested range is distinguished at finite depth.')
