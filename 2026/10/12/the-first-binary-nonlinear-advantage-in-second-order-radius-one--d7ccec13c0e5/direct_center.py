#!/usr/bin/env python3
"""Independent literal-matrix check of the 29-word length-six code."""
from verify import WITNESS6
C=WITNESS6
N=6
covers=set()
for u in C:
 for v in C:
  for coordinate in range(N):
   for a in (0,1):
    for b in (0,1):
     # row targets differing from u and v at only this common coordinate
     x=(u & ~(1<<coordinate)) | (a<<coordinate)
     y=(v & ~(1<<coordinate)) | (b<<coordinate)
     covers.add((x,y))
assert len(covers)==(1<<N)**2,len(covers)
print('VERIFY_OK literal 4096 two-row target matrices covered')
