"""Independent reconfiguration cross-check on known structural candidates."""
from itertools import combinations
from collections import deque

def run(n):
 es=list(combinations(range(n),2));m=[sum(1<<v for v in e) for e in es];p=len(es)
 states=set()
 for t in combinations(range(p),4):
  if any(not(m[a]&m[b] or m[a]&m[c] or m[b]&m[c]) for a,b,c in combinations(t,3)):
   states.add(sum(1<<i for i in t))
 q=deque([next(iter(states))]);seen={q[0]}
 while q:
  state=q.popleft();ins=[j for j in range(p) if (state>>j)&1]
  for i in ins:
   without=state^(1<<i)
   for j in range(p):
    if state>>j & 1:continue
    k=without|(1<<j)
    if k in states and k not in seen:
     seen.add(k);q.append(k)
 assert len(seen)==len(states),(n,len(seen),len(states))
 print(f'reconfiguration n={n} connected=True states={len(states)}')

if __name__=='__main__':
 for n in range(6,10):run(n)
 print('RECONFIGURATION_OK n=6..9')
