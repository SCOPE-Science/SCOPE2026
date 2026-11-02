from functools import lru_cache
from collections import defaultdict,deque
import time, sys
@lru_cache(None)
def words(n):
 if n==0:return ('',)
 ans=[]
 if n>=1:
  for q in words(n-1):
   ans.append('H'+q);ans.append('V'+q)
 if n>=2:
  for q in words(n-2):ans.append('D'+q)
 return tuple(ans)
def layers(n):
 d=defaultdict(list)
 for s in words(n):d[s.count('V')+s.count('D')].append(s)
 return d

def neigh(w):
 r=set()
 for i,c in enumerate(w):
  if c=='H':r.add(w[:i]+'V'+w[i+1:])
  if c=='D':r.add(w[:i]+'VV'+w[i+1:])
  if w[i:i+2]=='HH':r.add(w[:i]+'D'+w[i+2:])
 return r
class Dinic:
 def __init__(self,n):self.g=[[] for _ in range(n)]
 def add(self,u,v,c):
  a=[v,c,None];b=[u,0,a];a[2]=b;self.g[u].append(a);self.g[v].append(b)
 def run(self,s,t):
  res=0
  while 1:
   level=[-1]*len(self.g);level[s]=0;d=deque([s])
   while d:
    u=d.popleft()
    for e in self.g[u]:
     if e[1]>0 and level[e[0]]<0:level[e[0]]=level[u]+1;d.append(e[0])
   if level[t]<0:break
   it=[0]*len(self.g)
   def dfs(u,f):
    if u==t:return f
    while it[u]<len(self.g[u]):
     e=self.g[u][it[u]];v=e[0]
     if e[1]>0 and level[v]==level[u]+1:
      z=dfs(v,min(e[1],f))
      if z:e[1]-=z;e[2][1]+=z;return z
     it[u]+=1
    return 0
   while z:=dfs(s,10**24):res+=z
  return res

def test(n):
 d=layers(n);print('n',n,'size',sum(map(len,d.values())),'ranks',[len(d[i]) for i in range(n+1)],flush=True)
 for k in range((n+1)//2):
  l=d[k];r=d[k+1];L=len(l);R=len(r);inds={x:i for i,x in enumerate(r)};net=Dinic(L+R+2);S=L+R;T=S+1
  for i,x in enumerate(l):
   net.add(S,i,R)
   for y in neigh(x):net.add(i,L+inds[y],L*R)
  for j in range(R):net.add(L+j,T,L)
  t=time.monotonic();flow=net.run(S,T)
  print(' rank',k, '->',k+1,'size',L,R,'ratio',flow/(L*R),'secs',round(time.monotonic()-t,2),flush=True)
  if flow!=L*R:
   print('FAILED',n,k,flow,L*R)
   return False
 return True
if __name__=='__main__':
 for n in range(0,14):
  assert test(n)
 print('INDEPENDENT_VERIFY_OK_0_TO_13')
