#!/usr/bin/env python3
"""Exhaustive small-plane lower-bound tests (all point marker configurations)."""
from itertools import combinations
from check_plane import Field,plane,refine
from collections import Counter
import sys,time

def check(q):
 if q==2:f=Field(2)
 elif q==3:f=Field(3)
 elif q==4:f=Field(2,2,[1,1,1])
 else:raise ValueError(q)
 V,I,adj=plane(f); n=len(V)
 bound={2:2,3:3,4:4}[q]
 start=time.monotonic()
 for k in range(bound+1):
  if k==0: continue
  count=0; most=0
  for M in combinations(range(n),k):
   colors,hist=refine(adj,M)
   most=max(most,len(set(colors)))
   if len(set(colors))==len(adj):
    raise AssertionError(f'Unexpected discrete config q={q} markers={M}')
   count+=1
  print(f'q={q} k={k} configurations={count} largest_class_count={most} expected_vertices={len(adj)}')
 print(f'q={q} passed all configurations up to {bound} marked points')

if __name__=='__main__':
 for q in (2,3,4):check(q)
