#!/usr/bin/env python3
"""Independent state-graph enumeration of binary XOR dynamics and first-cycle arrival."""
from collections import Counter

def run(sizes):
 n=sum(sizes)
 missing=[set() for _ in range(n)]
 start=0
 for length in sizes:
  for a in range(length):
   v=start+a
   missing[v].add(start+(a-1)%length)
   missing[v].add(start+(a+1)%length)
  start+=length
 adjacency=[]
 for v in range(n):
  adjacency.append(sum(1<<j for j in range(n) if j!=v and j not in missing[v]))
 def nextstate(bits):
  result=0
  for v,neighbors in enumerate(adjacency):
   if (bits&neighbors).bit_count()%2:result|=1<<v
  return result
 total=1<<n
 successor=[nextstate(x) for x in range(total)]
 seen_time=[-1]*total
 T=[-1]*total
 for initial in range(total):
  if T[initial]>=0:continue
  current=initial; chain=[]; positions={}
  while current not in positions and T[current]<0:
   positions[current]=len(chain)
   chain.append(current)
   current=successor[current]
  if T[current]>=0:
   time=T[current]
   for state in reversed(chain):
    time+=1;T[state]=time
  else:
   cycle_start=positions[current]
   for state in chain[cycle_start:]:T[state]=0
   time=0
   for state in reversed(chain[:cycle_start]):
    time+=1;T[state]=time
 counts=Counter(T)
 lengths=[]
 for l in sizes:
  if l%3==0:lengths.append(l & -l)
 transient=(n%2)+2*sum(lengths)
 prev=0
 expected=Counter()
 for t in range(max(lengths+[n%2,0])+1):
  nullity=(n%2 if t>=1 else 0)+2*sum(min(t,e) for e in lengths)
  cumulative=1<<(n-transient+nullity)
  expected[t]=cumulative-prev;prev=cumulative
 assert counts==expected,(sizes,counts,expected)
 return total,counts
if __name__=='__main__':
 cases=[(3,3),(3,4),(3,5),(4,4),(3,6),(4,5),(5,5),(3,7),(3,3,3),(3,3,4),(3,4,4),(3,3,5),(3,3,6),(3,6,6),(6,6),(3,12)]
 states=0
 for c in cases:
  if sum(c)>16:continue
  N,d=run(c);states+=N
  print(f'{c}: {N} states, first-entry counts {dict(sorted(d.items()))}')
 print(f'PASS: orbit detection for {states} independently evolved initial configurations')
