from itertools import combinations
from math import comb,prod

def bouquet(lengths):
  E=[]; h=0; nxt=1;B=[]
  for ell in lengths:
    verts=list(range(nxt,nxt+ell-1)); nxt+=ell-1;B.append(verts)
    cyc=[h]+verts
    E+=list(zip(cyc,cyc[1:]+[h]))
  E=[tuple(sorted(e)) for e in E]
  return nxt,E

def path_masks(n,edges):
  neighbors=[[] for _ in range(n)];ids={e:i for i,e in enumerate(edges)}
  for a,b in edges:neighbors[a].append(b);neighbors[b].append(a)
  seen={};
  def walk(path,mask):
    if len(path)>1:
      key=tuple(path) if path[0]<path[-1] else tuple(reversed(path))
      seen[key]=mask
    for v in neighbors[path[-1]]:
      if v not in path:
        e=tuple(sorted((path[-1],v)))
        walk(path+[v],mask|(1<<ids[e]))
  for u in range(n):walk([u],0)
  return sorted(set(seen.values()))

def predict(lengths):
 t=len(lengths)
 # perfect matching count of 2t spokes avoiding t forbidden pairings
 D=sum((-1)**j*comb(t,j)*(prod(range(1,2*(t-j),2))) for j in range(t+1))
 return D*prod(x-1 for x in lengths)

def test(L):
 n,edges=bouquet(L); masks=path_masks(n,edges); t=len(L)
 target=(1<<len(edges))-1
 print('L',L,'n',n,'edges',len(edges),'paths',len(masks),'pred',predict(L),end=' ')
 if t==1:print('skip');return
 if t>3:print('skip');return
 match=0
 # DFS lexicographically ordered path masks; disjoint edge path partition
 def rec(st,rest,k):
  if k==0:return int(rest==0)
  v=0
  for i in range(st,len(masks)):
   mask=masks[i]
   if mask & rest!=mask:continue
   v+=rec(i+1,rest^mask,k-1)
  return v
 match=rec(0,target,t)
 print('actual',match)
 assert match==predict(L),(L,match,predict(L))

if __name__=='__main__':
 for L in [(3,3),(3,4),(4,4),(3,5),(4,5),(5,5),(3,3,3),(3,3,4),(3,4,4)]:test(L)
 print('VERIFY_OK')
