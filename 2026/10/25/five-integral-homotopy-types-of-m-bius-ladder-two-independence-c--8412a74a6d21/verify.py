#!/usr/bin/env python3
"""Reproducible finite proof of small Möbius-ladder 2-independence types."""
from collections import Counter, deque
ORDERS = {
 4:(4,5,0,1,6,7,2,3),
 5:(0,3,4,2,5,9,7,1,8,6),
 6:(8,3,9,1,11,5,0,4,7,10,6,2),
 7:(5,13,11,1,12,9,3,7,4,6,0,2,10,8),
 8:(2,14,13,3,4,6,8,7,1,11,0,15,5,10,9,12),
}
EXPECTED={4:(2,1),5:(3,9),6:(3,6),7:(4,1),8:(5,31)}

def graph(n):
 N=2*n
 return [sum(1<<w for w in {(v-1)%N,(v+1)%N,(v+n)%N}) for v in range(N)]

def faces(n):
 N=2*n;nb=graph(n); yes=[]
 for x in range(1,1<<N):
  a=x;ok=True
  while a:
   low=a&-a;u=low.bit_length()-1;a-=low
   if (x&nb[u]).bit_count()>1:ok=False;break
  if ok:yes.append(x)
 return yes

def check_bfs(n,fs):
 N=2*n;adj=graph(n);faceset=set(fs)
 for s in range(1,1<<N):
  todo=s;ok=True
  while todo:
   start=todo&-todo;seen=start;front=start
   while front:
    nxt=0;t=front
    while t:
     b=t&-t;v=b.bit_length()-1;t-=b
     nxt|=adj[v]&s&~seen
    seen|=nxt;front=nxt
   if seen.bit_count()>2:ok=False;break
   todo &=~seen
  assert ok == (s in faceset), (n,s)

def proof(n):
 N=2*n;fs=faces(n);fset=set(fs)
 check_bfs(n,fs)
 remaining=set(fs);pairs=[]
 for v in ORDERS[n]:
  bit=1<<v
  for low in sorted(remaining,key=lambda a:(a.bit_count(),a)):
   high=low|bit
   if low&bit==0 and high in remaining:
    remaining.remove(low);remaining.remove(high);pairs.append((low,high))
 critical=Counter(x.bit_count()-1 for x in remaining)
 assert critical==Counter({0:1,EXPECTED[n][0]:EXPECTED[n][1]}),(n,critical)
 pair_set=set(pairs)
 # Every covering relation: direction upper -> lower except a matched arrow lower -> upper.
 incoming={x:0 for x in fs};out={x:[] for x in fs}
 for upper in fs:
  x=upper
  while x:
   b=x&-x; x-=b;low=upper^b
   if low==0:continue
   if (low,upper) in pair_set:
    src,dst=low,upper
   else: src,dst=upper,low
   out[src].append(dst);incoming[dst]+=1
 q=deque(x for x in fs if incoming[x]==0);visited=0
 while q:
  a=q.popleft();visited+=1
  for b in out[a]:
   incoming[b]-=1
   if incoming[b]==0:q.append(b)
 assert visited==len(fs),(n,visited,len(fs))
 expected_f={4:78,5:232,6:685,7:2046,8:6078}
 assert len(fs)==expected_f[n]
 return {'n':n,'faces_nonempty':len(fs),'matching_pairs':len(pairs),
  'critical_dimensions':dict(sorted(critical.items())),
  'critical_masks':sorted(remaining),'hasse_arrows':sum(map(len,out.values())),'acyclic':True}

if __name__=='__main__':
 for n in sorted(ORDERS):print(proof(n),flush=True)
 print('VERIFY_OK')
