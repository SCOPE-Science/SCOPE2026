from collections import Counter,defaultdict
from math import comb

def F(n,state):
 mask=(1<<n)-1
 c=state&mask;l=(state>>n)&mask;s=c.bit_count()
 cc=0
 for i in range(n):
  bit=(s-((c>>i)&1)+((l>>i)&1))
  if bit>n/2 or (bit==n/2 and ((c>>i)&1)): cc|=1<<i
 return cc|(c<<n)

def graph(n):
 N=1<<(2*n); succ=[F(n,s) for s in range(N)]; visiting=[0]*N;dist=[-1]*N; basin_id=[-1]*N; cycles=[]
 for x in range(N):
  if visiting[x]:continue
  trail=[];d={};v=x
  while not visiting[v] and v not in d:
   d[v]=len(trail);trail.append(v);v=succ[v]
  if v in d:
   cy=trail[d[v]:]; cid=len(cycles);cycles.append(cy)
   for w in cy:visiting[w]=1;dist[w]=0;basin_id[w]=cid
   trail=trail[:d[v]]
  for w in reversed(trail):
   visiting[w]=1;dist[w]=dist[succ[w]]+1;basin_id[w]=basin_id[succ[w]]
 basin_sizes=Counter(basin_id); fixed=Counter({cid:basin_sizes[cid] for cid,cy in enumerate(cycles) if len(cy)==1}); p2=Counter({cid:basin_sizes[cid] for cid,cy in enumerate(cycles) if len(cy)==2})
 dist0=Counter(dist)
 print(n,dict(periods=Counter(map(len,cycles)),fixed_basin=Counter(fixed.values()),period2_basin=Counter(p2.values()),maxtrans=max(dist),dist=dist0))
 m=n//2
 if n%2==0:
  C=comb(n,m);predfixed=C+2;predp2=(C*C-C)//2;predfixedbasin=Counter({1:C,(4**n-C*C)//2:2});pred2basin=Counter({2:predp2})
 else:
  C=comb(n,m);predfixed=2;predp2=C*(m+2);predfixedbasin=Counter({(4**n-predp2*(2**(m+1)))//2:2});pred2basin=Counter({2**(m+1):predp2})
 print('PRED',predfixed,predp2,predfixedbasin,pred2basin)
 assert len(fixed)==predfixed and len(p2)==predp2
 assert Counter(fixed.values())==predfixedbasin and Counter(p2.values())==pred2basin
 if n>=4:assert max(dist)==3
 if n in (2,3):assert max(dist)==2
 if n==1:assert max(dist)==0
 print('OK')
for n in range(2,9):graph(n)
