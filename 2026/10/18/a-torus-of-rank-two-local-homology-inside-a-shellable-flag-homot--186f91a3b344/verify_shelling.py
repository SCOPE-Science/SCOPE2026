#!/usr/bin/env python3
"""Exact shelling and face census for the well-covered circulant example.
The shelling order below was constructed by a face-adjacency greedy search.
The underlying well-covered circulant was introduced as the shellable non-vertex-decomposable example of Earl--Vander Meulen--Van Tuyl (2015).
No external packages are required.
"""
from itertools import combinations
from collections import Counter
N=16
STEPS={1,4,8}
ORDER_TEXT='''
1 7 12 14 7 9 12 14 1 4 7 14 1 7 10 12 1 3 12 14 4 7 9 14 1 10 12 15
4 9 11 14 0 7 9 14 0 5 7 14 0 2 7 9 1 4 7 10 2 7 9 12 0 2 7 13
3 9 12 14 4 6 9 11 2 4 7 9 5 7 12 14 3 5 12 14 3 5 8 14 0 2 5 7
2 4 7 13 0 3 5 14 1 4 10 15 0 3 9 14 1 4 11 14 4 7 10 13 4 10 13 15
5 7 10 12 1 3 8 14 0 7 10 13 1 4 6 11 1 8 11 14 0 9 11 14 2 4 9 11
1 4 6 15 2 4 13 15 2 4 9 15 0 5 11 14 2 5 7 12 1 3 10 12 5 10 12 15
2 4 11 13 0 5 7 10 1 6 12 15 4 6 13 15 4 6 9 15 1 3 6 12 1 6 8 11
3 5 10 12 5 8 11 14 0 6 9 11 1 3 6 8 1 6 8 15 0 3 5 10 3 5 8 10
0 2 9 11 4 6 11 13 6 8 11 13 2 8 11 13 1 3 8 10 0 2 11 13 0 6 11 13
0 2 5 11 2 5 8 11 3 6 8 13 6 8 13 15 2 8 13 15 1 8 10 15 8 10 13 15
3 8 10 13 0 3 10 13 5 8 10 15 0 3 6 13 0 3 6 9 2 5 8 15 3 6 9 12
6 9 12 15 2 9 12 15 2 5 12 15
'''
nums=list(map(int,ORDER_TEXT.split()))
assert len(nums)==320, (len(nums),len(nums)//4)
shelling=[tuple(nums[4*j:4*j+4]) for j in range(80)]
assert len(set(shelling))==80

def allowed(face):
 return all(min((b-a)%N,(a-b)%N) not in STEPS for a,b in combinations(face,2))
faces={tuple(c) for size in range(5) for c in combinations(range(N),size) if allowed(c)}
facets={f for f in faces if len(f)==4}
assert set(shelling)==facets
assert Counter(map(len,faces))=={0:1,1:16,2:80,3:144,4:80}
for i,F in enumerate(shelling):
 if i==0:continue
 for J in shelling[:i]:
  if not any(len(set(F)-set(R))==1 and (set(F)-set(R)).isdisjoint(set(J)) for R in shelling[:i]):
   raise AssertionError(('shelling failure',i,F,J))
print('PASS: 80 constructed shelling facets independently checked; 321 faces including empty, pure dimension 3.')
