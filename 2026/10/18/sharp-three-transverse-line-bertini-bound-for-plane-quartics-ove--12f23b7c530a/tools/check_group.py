"""Verify that the five listed generators exhaust GL(3,3), of order 11232."""
from collections import deque
S=[((0,1,0),(1,0,0),(0,0,1)),((1,0,0),(0,0,1),(0,1,0)),((2,0,0),(0,1,0),(0,0,1)),((1,1,0),(0,1,0),(0,0,1)),((1,0,0),(0,1,1),(0,0,1))]
def mul(A,B):
 return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%3 for j in range(3)) for i in range(3))
e=((1,0,0),(0,1,0),(0,0,1))
seen={e};q=deque([e])
while q:
 a=q.popleft()
 for b in S:
  c=mul(a,b)
  if c not in seen:
   seen.add(c);q.append(c)
assert len(seen)==11232,len(seen)
print('PASS five generators span GL(3,3), order 11232, projective order 5616')
