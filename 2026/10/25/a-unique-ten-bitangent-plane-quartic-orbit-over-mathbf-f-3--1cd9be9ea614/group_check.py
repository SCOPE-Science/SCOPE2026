"""Verify the coefficient-action generators span all of PGL(3,3)."""
from itertools import product
from collections import deque
G=[((1,1,0),(0,1,0),(0,0,1)),((1,0,0),(0,1,1),(0,0,1)),((1,0,0),(0,1,0),(1,0,1)),((0,1,0),(1,0,0),(0,0,1)),((2,0,0),(0,1,0),(0,0,1))]
def mul(a,b):
 return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))%3 for j in range(3)) for i in range(3))
def norm(a):
 v=next(x for row in a for x in row if x)
 return tuple(tuple(x*(1 if v==1 else 2)%3 for x in row) for row in a)
one=((1,0,0),(0,1,0),(0,0,1));seen={norm(one)};todo=deque([one]);
while todo:
 a=todo.popleft()
 for g in G:
  x=norm(mul(a,g))
  if x not in seen:
   seen.add(x);todo.append(x)
assert len(seen)==5616,len(seen)
print('The five generators produce all 5616 projective matrices in PGL(3,F3).')
