import itertools,collections,math
from collections import Counter,deque

def graph(ts):
 m=len(ts); n=m; edges=[]; pend=[]; spine=[]
 for i in range(m-1):spine.append(len(edges));edges.append((i,i+1))
 for i,t in enumerate(ts):
  for _ in range(t):pend.append(len(edges));edges.append((i,n));n+=1
 return n,edges,spine,pend

def brute(ts):
 n,edges,spine,pend=graph(ts); E=len(edges)
 adj=[[] for _ in range(n)]
 for i,(a,b) in enumerate(edges):adj[a].append((b,i));adj[b].append((a,i))
 paths=[]
 for a in range(n):
  for b in range(a+1,n):
   Q=deque([(a,0)]);seen={a}; found=None
   while Q:
    v,mask=Q.popleft()
    if v==b:found=mask;break
    for w,e in adj[v]:
     if w not in seen:seen.add(w);Q.append((w,mask|(1<<e)))
   paths.append(found)
 valid=set()
 for mask in range(1<<E):
  if all((mask&p).bit_count()<3 for p in paths):valid.add(mask)
 fac={mask for mask in valid if not any((mask|(1<<i)) in valid for i in range(E) if not mask>>i&1)}
 return Counter(m.bit_count() for m in valid), Counter(m.bit_count() for m in fac), valid,fac

def predicted(ts):
 m=len(ts);T=sum(ts)
 sets=set()
 n,edges,spine,pend=graph(ts)
 assert len(spine)==m-1
 # pendant index grouped by spine
 grp=[[] for _ in ts]
 for idx,(a,b) in enumerate(edges):
  if idx not in spine:grp[a].append(idx)
 def masksfrom(allowed,fixed):
  out=[]
  for rr in range(1<<len(allowed)):
   mask=fixed
   for k,e in enumerate(allowed):
    if rr>>k&1:mask|=1<<e
   out.append(mask)
  return out
 sets.update(masksfrom(pend,0))
 for i,e in enumerate(spine):
  sets.update(masksfrom(list(itertools.chain.from_iterable(grp[:i+1])),1<<e))
  sets.update(masksfrom(list(itertools.chain.from_iterable(grp[i+1:])),1<<e))
 for i,j in itertools.combinations(range(m-1),2):
  sets.update(masksfrom(list(itertools.chain.from_iterable(grp[i+1:j+1])),(1<<spine[i])|(1<<spine[j])))
 fac=set()
 pends=sum((list(x) for x in grp),[])
 fac.add(sum(1<<e for e in pends))
 for i,e in enumerate(spine):
  fac.add((1<<e)+sum(1<<f for g in grp[:i+1] for f in g))
  fac.add((1<<e)+sum(1<<f for g in grp[i+1:] for f in g))
 for i,j in itertools.combinations(range(m-1),2):
  fac.add((1<<spine[i])+(1<<spine[j])+sum(1<<f for g in grp[i+1:j+1] for f in g))
 return Counter(m.bit_count() for m in sets),Counter(m.bit_count() for m in fac),sets,fac

if __name__=='__main__':
 cases=0; examined=0
 for m in range(2,6):
  for ts in itertools.product(range(1,3),repeat=m):
   if sum(ts)+m-1>14:continue
   a,b,cc,dd=brute(ts); e,f,ee,ff=predicted(ts)
   assert cc==ee,('sets',ts,a,e,sorted(cc-ee),sorted(ee-cc))
   assert dd==ff,('fac',ts,b,f,sorted(dd-ff),sorted(ff-dd))
   cases+=1;examined+=1<<(sum(ts)+m-1)
 print('VERIFICATION_OK configurations=',cases,'subsets=',examined)
 for ts in [(1,1,1),(1,1,1,1),(2,1,2,1),(1,2,2,2,1)]:
  a,b,_,_=predicted(ts);print(ts,'set_poly',dict(sorted(a.items())),'facet_poly',dict(sorted(b.items())))
