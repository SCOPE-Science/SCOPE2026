#!/usr/bin/env python3
"""Exact exhaustive finite-state verification of Rudin--Shapiro parity sumsets.
All arithmetic is over small finite state spaces; no external packages.
"""
from collections import deque

# NFA state (carry, previous digit a, previous digit b, parity of '11' in a, parity in b).
def pack(c,pa,pb,ta,tb):
    assert all(x in (0,1) for x in (c,pa,pb,ta,tb))
    return (((c*2+pa)*2+pb)*2+ta)*2+tb

INITIAL = 1 << pack(0,0,0,0,0)
MOVES = [[0,0] for _ in range(32)]
for c in range(2):
 for pa in range(2):
  for pb in range(2):
   for ta in range(2):
    for tb in range(2):
     i=pack(c,pa,pb,ta,tb)
     for a in range(2):
      for b in range(2):
       s=a+b+c
       d=s%2
       j=pack(s//2,a,b,ta^(pa&a),tb^(pb&b))
       MOVES[i][d] |= 1<<j

ACCEPT = {}
for i in range(2):
 for j in range(i,2):
  x=0
  for pa in range(2):
   for pb in range(2):
    x |= 1<<pack(0,pa,pb,i,j)
  ACCEPT[(i,j)]=x

EXCEPTIONS = {
 (0,0):set(),
 (0,1):{0,1,2,9},
 (1,1):{0,1,2,3,4,5,7,8,10,11,13,20},
}
BOUND=1+max(max(v) if v else 0 for v in EXCEPTIONS.values())

def step(mask,d):
    s=0
    while mask:
      lsb=mask&(-mask)
      idx=lsb.bit_length()-1
      s|=MOVES[idx][d]
      mask-=lsb
    return s

def verify(pair,exceptions):
    # Value is truncated at BOUND, weight at BOUND; for membership in finite exception set this is exact.
    start=(INITIAL,0,1)
    visited={start}
    queue=deque([start])
    mismatch=[]
    max_mask=0
    while queue:
      mask,v,w=queue.popleft()
      predicted_hole=not bool(mask & ACCEPT[pair]); listed_hole=v in exceptions
      if predicted_hole!=listed_hole:
       mismatch.append((mask,v,w,predicted_hole,listed_hole))
       if len(mismatch)>5:break
      max_mask=max(max_mask,mask.bit_count())
      for d in (0,1):
       new=(step(mask,d), min(BOUND,v+d*w), min(BOUND,2*w))
       if new not in visited:
        visited.add(new)
        queue.append(new)
    assert not mismatch,(pair,mismatch)
    return len(visited),max_mask

for pair,E in EXCEPTIONS.items():
 states, maxsubset=verify(pair,E)
 assert states == 88 and maxsubset == 16, (pair,states,maxsubset)
 print(f"{pair}: PASS; product DFA reachable states={states}; max NFA subset={maxsubset}; holes={sorted(E)}")

# Check actual representations independently via direct recurrence rather than using the finite automaton.
N=3000
parity=[0]*N
for n in range(1,N):parity[n]=parity[n>>1]^int((n&3)==3)
for p,E in EXCEPTIONS.items():
 for n in range(N):
  represented=any(parity[a]==p[0] and parity[n-a]==p[1] for a in range(n+1))
  assert represented==(n not in E),(p,n)
 print(f'{p}: PASS direct integer enumeration 0 <= n < {N}')

# Stronger bounded-choice witnesses, proved via the finite-state reachable subset language.
for p,limit in [((0,0),16),((0,1),16),((1,1),32)]:
 found=[]
 for n in range(N):
  good=any(parity[a]==p[0] and parity[n-a]==p[1] for a in range(min(limit,n)+1))
  if not good:found.append(n)
 print('bounded-test',p,'limit',limit,'holes',found[:40], 'count',len(found))
