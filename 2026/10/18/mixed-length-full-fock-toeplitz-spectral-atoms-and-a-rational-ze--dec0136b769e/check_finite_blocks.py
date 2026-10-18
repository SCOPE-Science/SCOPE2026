import numpy as np
from collections import Counter

def strings(d,N):
 res=['']; begin=['']
 for l in range(1,N+1):
  begin=[str(a)+w for a in range(1,d+1) for w in begin]
  res+=begin
 return res

def tree(h):
 queue=[''];i=0
 while i<len(queue):
  v=queue[i]; i+=1
  if len(v)+1<=h:queue.append('1'+v)
  if len(v)+2<=h:queue.append('22'+v)
 return queue

def adj(vertices,N):
 idx={s:i for i,s in enumerate(vertices)}
 A=np.zeros((len(vertices),len(vertices)))
 for w in vertices:
  for c in ['1','22']:
   if c+w in idx:
    A[idx[w],idx[c+w]]=A[idx[c+w],idx[w]]=1.
 return A

for d in [2,3]:
 for N in range(2,7 if d==2 else 5):
  words=strings(d,N)
  A=adj(words,N)
  finite=np.linalg.eigvalsh(A)
  c=d*d-d-1
  parts=[]
  for h in range(N-1):parts.extend(np.linalg.eigvalsh(adj(tree(h),h)).tolist()*(c*d**(N-h-2)))
  parts.extend(np.linalg.eigvalsh(adj(tree(N-1),N-1)).tolist()*(d-1))
  parts.extend(np.linalg.eigvalsh(adj(tree(N),N)).tolist())
  diff=max(abs(x-y) for x,y in zip(sorted(parts),finite))
  z=np.count_nonzero(abs(finite)<1e-9)
  print(f'd={d} N={N} D={len(words)} max-err={diff:.2e} zero-fraction={z/len(words):.7f} target={c*(d-1)/(d**3-1):.7f}')
