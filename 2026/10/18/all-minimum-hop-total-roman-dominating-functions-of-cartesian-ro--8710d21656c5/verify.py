"""Independent direct graph checks of minimum hop-total-Roman functions of Cartesian rook graphs.
No external packages; enumerate label functions by their exact small weights and evaluate graph distances.
"""
from itertools import combinations,product
from collections import Counter,deque
from math import comb


def graph(m,n):
 v=[(r,c) for r in range(m) for c in range(n)]
 adj=[set() for _ in v]
 for i,(r,c) in enumerate(v):
  for j,(s,d) in enumerate(v):
   if i!=j and (r==s or c==d):adj[i].add(j)
 dist=[]
 for i in range(len(v)):
  d=[-1]*len(v);d[i]=0;q=deque([i])
  while q:
   u=q.popleft()
   for t in adj[u]:
    if d[t]<0:d[t]=d[u]+1;q.append(t)
  dist.append(d)
 return adj,[[j for j in range(len(v)) if dist[i][j]==2] for i in range(len(v))]

def valid(labels,adj,hop):
 N=len(labels)
 for i in range(N):
  if labels[i]:
   if not any(labels[j]>0 for j in adj[i]):return False
  elif not any(labels[j]==2 for j in hop[i]):return False
 return True

def target(m,n):
 if m==2:return (4,9 if n==2 else n)
 if m==3:return (5,18 if n==3 else 3*n)
 assert m>=4
 return 6,6*comb(m,2)*comb(n,2)+(6*n if m==4 else 0)+(6*m if n==4 else 0)

def classify(m,n,labels):
 N=m*n;A={(i//n,i%n) for i in range(N) if labels[i]==2}
 B={(i//n,i%n) for i in range(N) if labels[i]==1}
 if not A:return 'all-one'
 if len(A)==1:return 'one-two-cross'
 if len(A)==2:
  ps=list(A)
  if ps[0][0]==ps[1][0]:return 'same-row'
  if ps[0][1]==ps[1][1]:return 'same-column'
  return 'diagonal-two'
 if len(A)==3:return 'three-two-L'
 return 'other'

cases=[(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5),(4,6),(5,5),(5,6),(6,6)]
checks=0
for m,n in cases:
 adj,hop=graph(m,n);N=m*n
 observed=Counter();patterns=Counter()
 # Under weight <=6, a function can have at most 3 twos.
 # The no-two case requires all vertices positive and is explicitly checked if N <=6.
 if N<=6:
  label_space=product((0,1,2),repeat=N)
 else:
  def assignments():
   indices=range(N)
   for k2 in (1,2,3):
    for k1 in range(0,7-2*k2):
     for twos in combinations(indices,k2):
      rem=[i for i in indices if i not in twos]
      for ones in combinations(rem,k1):
       labels=[0]*N
       for i in twos: labels[i]=2
       for i in ones: labels[i]=1
       yield labels
  label_space=assignments()
 for lab in label_space:
  checks+=1
  w=sum(lab)
  if w>6:continue
  if valid(lab,adj,hop):
   observed[w]+=1
   patterns[classify(m,n,lab)]+=int(w==target(m,n)[0])
 k,v=target(m,n)
 assert all(observed.get(w,0)==0 for w in range(k)),(m,n,observed)
 assert observed[k]==v,(m,n,k,v,observed)
 print('PASS',m,n,'minimum',k,'minimum_count',v,'types',dict(patterns),'candidate_functions_tested',checks)
print('VERIFY_OK cases=',len(cases),'candidate_labelings_tested=',checks)
