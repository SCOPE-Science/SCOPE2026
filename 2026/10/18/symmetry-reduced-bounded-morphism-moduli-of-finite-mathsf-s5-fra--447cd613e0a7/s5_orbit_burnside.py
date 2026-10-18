"""Exact two-sided orbit count of surjective bounded maps of finite S5 frames."""
from collections import Counter
from itertools import permutations, product
from math import factorial

def partitions(n,lo=1):
 if n==0:yield ()
 for i in range(lo,n+1):
  for q in partitions(n-i,i):yield (i,)+q

def comps(n,k):
 if k==0:
  if n==0:yield ()
  return
 for i in range(1,n-k+2):
  for t in comps(n-i,k-1):yield (i,)+t

def frame(block_sizes):
 bs=[]; x=0
 for s in block_sizes:bs.append(tuple(range(x,x+s)));x+=s
 return bs

def auts(B):
 # all permutations respecting the equivalence partition
 m=sum(map(len,B)); size_groups=Counter(map(len,B))
 cats={s:[i for i,b in enumerate(B) if len(b)==s] for s in size_groups}
 perm_groups=[list(permutations(ids)) for ids in cats.values()]
 for block_maps in product(*perm_groups):
  idx={i:j for ids,js in zip(cats.values(),block_maps) for i,j in zip(ids,js)}
  choices=[list(permutations(B[idx[i]])) for i in range(len(B))]
  for ps in product(*choices):
   out=[0]*m
   for b,p in zip(B,ps):
    for v,w in zip(b,p):out[v]=w
   yield tuple(out),idx

def cycle_lengths(mapping):
 vis=set();out=[]
 for x in range(len(mapping)):
  if x not in vis:
   now=x;length=0
   while now not in vis:vis.add(now);length+=1;now=mapping[now]
   out.append(length)
 return out

def multisets_fixed_count(cycles,r):
 dp=[0]*(r+1);dp[0]=1
 for d in cycles:
  for i in range(d,r+1):dp[i]+=dp[i-d]
 return dp[r]

def orbits_burnside(source,target):
 A=frame(source);B=frame(target); n=sum(source); m=sum(target)
 bysize=Counter(source)
 # source block type (j, positive target-fibre vector)
 omega={a:[(j,c) for j,b in enumerate(B) for c in comps(a,len(b))] for a in bysize}
 ans=0;num_aut=0
 for h,idx in auts(B):
  num_aut+=1
  block_cycle=[]; seen=set()
  for j in range(len(B)):
   if j not in seen:
    q=[];k=j
    while k not in seen:q.append(k);seen.add(k);k=idx[k]
    block_cycle.append(tuple(q))
  fixed_cover=0
  for mask in range(1<<len(block_cycle)):
   allowed={j for t,q in enumerate(block_cycle) if mask>>t&1 for j in q}
   sign=(-1)**(len(block_cycle)-mask.bit_count())
   ways=1
   for a,r in bysize.items():
    types=[x for x in omega[a] if x[0] in allowed]
    inds={x:i for i,x in enumerate(types)}
    perm=[]
    for j,counts in types:
     src=B[j];dst=B[idx[j]]
     transformed=[0]*len(dst)
     dpos={v:i for i,v in enumerate(dst)}
     for v,c in zip(src,counts):transformed[dpos[h[v]]]=c
     perm.append(inds[(idx[j],tuple(transformed))])
    ways*=multisets_fixed_count(cycle_lengths(perm),r)
   fixed_cover+=sign*ways
  ans+=fixed_cover
 assert ans%num_aut==0,(source,target,ans,num_aut)
 return ans//num_aut

if __name__=='__main__':
 for n in range(1,7):
  for src in partitions(n):
   for m in range(1,5):
    for dst in partitions(m):
     if m>n:continue
     print(n,src,m,dst,orbits_burnside(src,dst))
