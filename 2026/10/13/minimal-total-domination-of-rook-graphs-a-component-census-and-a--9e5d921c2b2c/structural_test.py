from collections import Counter,deque

def is_total(mask,m,n):
 ds=[[0]*n for _ in range(m)]
 for i in range(m):
  for j in range(n):
   if mask>>(i*n+j)&1: ds[i][j]=1
 rs=[sum(row) for row in ds]
 cs=[sum(ds[i][j] for i in range(m)) for j in range(n)]
 if 0 in rs and 0 in cs: return False
 return all(rs[i]+cs[j]-2*ds[i][j]>=1 for i in range(m) for j in range(n) if ds[i][j])

def cls(mask,m,n):
 rs=[0]*m; cs=[0]*n; edges=[]
 for i in range(m):
  for j in range(n):
   if (mask>>(i*n+j))&1: rs[i]+=1;cs[j]+=1;edges.append((i,j))
 # row-only may have components A col-star >=2, B row P3, C row subdiv-star >=2
 if 0 in rs and 0 in cs:return False
 if all(rs) and all(cs):
  # every selected component is P3 (row centered or col centered): for each edge one endpoint deg2 other deg1
  return all((rs[i],cs[j]) in [(2,1),(1,2)] for i,j in edges)
 def rowtype():
  if (0 not in rs) and (0 in cs):
   for i,j in edges:
    if rs[i]==1: continue
    # e incident to row degree>=2, check row star P3 two col leaves, or col deg 2 paired with row leaf
    if rs[i]==2 and all(cs[c]==1 for c in range(n) if (mask>>(i*n+c))&1): continue
    if cs[j]==2 and sum((mask>>(ii*n+j))&1 and rs[ii]==1 for ii in range(m))==1:continue
    return False
   # additional row-star P3 uniform assured via condition; A col-degree>=2 if row deg1 all; forbid selected K2
   return all(rs[i]+cs[j]>=3 for i,j in edges)
  return False
 def coltype():
  if (0 not in cs) and (0 in rs):
   # transpose bit rows cols
   mask2=sum(((mask>>(i*n+j))&1)<<(j*m+i) for i in range(m) for j in range(n))
   return cls(mask2,n,m)
  return False
 return rowtype() or coltype()

for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
 counts=Counter(); bad=[]
 for mask in range(1<<(m*n)):
  actual=is_total(mask,m,n) and all(not is_total(mask^(1<<k),m,n) for k in range(m*n) if mask>>k&1)
  pred=cls(mask,m,n)
  if actual!=pred:bad.append((mask,actual,pred))
  if actual:counts[mask.bit_count()]+=1
 print(m,n,'minimal=',sum(counts.values()),'poly',sorted(counts.items()),'mismatch',len(bad),'first',bad[:4])
