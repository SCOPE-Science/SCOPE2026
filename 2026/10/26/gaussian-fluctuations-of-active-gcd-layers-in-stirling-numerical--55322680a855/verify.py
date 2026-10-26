import math,heapq

def run():
 c=[1]
 rows={}
 for n in range(1,101):
  nc=[0]*(n+1)
  for k in range(1,n+1):nc[k]=(c[k-1] if k-1<len(c) else 0)+ (n-1)*(c[k] if k<len(c) else 0)
  c=nc
  if n<4: continue
  a=n*(n-1)//2
  b=[c[n-2*j] for j in range(1,(n-1)//2+1)]
  d=a;active=[]
  for j,v in enumerate(b,1):
   dnew=math.gcd(d,v)
   if dnew<d:active.append((j,v,d//dnew))
   d=dnew
  def pf(v):
   r=[];t=2
   while t*t<=v:
    if v%t==0:
     e=0
     while v%t==0:v//=t;e+=1
     r.append((t,e))
    t+=1
   if v>1:r.append((v,1))
   return r
  f=pf(n*(n-1))
  omg=len(f);bigomega=sum(e for p,e in f)
  e_dim=1+len(active)
  assert omg-2 <=e_dim<=bigomega+1, (n,e_dim,f,active)
  for p,ex in f:
   if p>=5:assert (p-1)//2 in {j for j,v,q in active},(n,p,active)
  if n<=28:
   gens=[a]+[v for j,v,q in active]
   for z in gens:
    rest=[g for g in gens if g!=z]
    if not rest:continue
    dist=[None]*a;dist[0]=0
    heap=[(0,0)]
    while heap:
     w,mod=heapq.heappop(heap)
     if dist[mod]!=w:continue
     if w>z:break
     for g in rest:
      u=(mod+g)%a;ww=w+g
      if ww<=z and (dist[u] is None or ww<dist[u]):dist[u]=ww;heapq.heappush(heap,(ww,u))
    assert dist[z%a]!=z,('nonminimal',n,z,gens)
 if __name__=='__main__':pass
 print('VERIFY_OK Stirling row n=4..100, active prime thresholds and omega sandwich; minimality n=4..28')
run()
