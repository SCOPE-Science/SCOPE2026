import json
from functools import lru_cache
from collections import deque
from pathlib import Path

def cat(m):
 if m==2:return [[1],[0]]
 if m==3:return [[1,2,3],[0],[0],[0]]
 I=m-2
 adj=[[] for _ in range(2*m-2)]
 for i in range(I-1):adj[i].append(i+1);adj[i+1].append(i)
 q=I
 for i in range(I):
  for _ in range(2 if i in (0,I-1) else 1):
   adj[i].append(q);adj[q].append(i);q+=1
 assert q==len(adj)
 return adj

def get_paths(adj):
 n=len(adj); leaves=[i for i in range(n) if len(adj[i])==1]
 pairs=[];paths=[]
 for i,a in enumerate(leaves):
  par={a:-1};q=deque([a])
  while q:
   v=q.popleft()
   for w in adj[v]:
    if w not in par:par[w]=v;q.append(w)
  for b in leaves[i+1:]:
   x=b;p=0
   while x!=-1:p|=1<<x;x=par[x]
   pairs.append([a,b]);paths.append(p)
 return pairs,paths

def solve(adj):
 pairs,paths=get_paths(adj);n=len(adj);N=len(paths)
 qs=[sum(1<<i for i,p in enumerate(paths) if (p>>v)&1) for v in range(n)]
 @lru_cache(None)
 def LD(s):
  if s.bit_count()<=1:return 0
  upper=s.bit_count().bit_length()-1
  best=0
  opts=[]
  for v,q in enumerate(qs):
   yes=s&q;no=s&~q
   if yes and no:opts.append((abs(yes.bit_count()-no.bit_count()),v,yes,no))
  for _,v,yes,no in sorted(opts):
   rank=1+min(LD(yes),LD(no))
   if rank>best:best=rank
   if best==upper:break
  return best
 S=(1<<N)-1;rank=LD(S)
 def witness(s,k):
  if k==0:
   idx=(s&-s).bit_length()-1
   return {'pair':pairs[idx]}
  for v,q in enumerate(qs):
   yes=s&q;no=s&~q
   if yes and no and LD(yes)>=k-1 and LD(no)>=k-1:
    return {'query':v,'0':witness(no,k-1),'1':witness(yes,k-1)}
  raise AssertionError('failed witness')
 tree=witness(S,rank)
 return {'m':len([a for a in adj if len(a)==1]),'adjacency':adj,'rank':rank,'concept_count':N,'shattered_tree':tree,'states':LD.cache_info().currsize}

def verify(cert):
 adj=cert['adjacency'];pairs,paths=get_paths(adj)
 assert len(paths)==cert['concept_count']
 P={tuple(pair):p for pair,p in zip(pairs,paths)}
 leaves=[];nodes=0
 def rec(node,conds):
  nonlocal nodes
  if 'pair' in node:
   pair=tuple(node['pair']);assert pair in P
   for v,val in conds:
    assert ((P[pair]>>v)&1)==val,(pair,v,val)
   leaves.append(pair)
  else:
   v=node['query'];nodes+=1
   assert 0<=v<len(adj)
   rec(node['0'],conds+[(v,0)])
   rec(node['1'],conds+[(v,1)])
 rec(cert['shattered_tree'],[])
 assert nodes==2**cert['rank']-1
 assert len(leaves)==2**cert['rank']==len(set(leaves))
 return nodes,len(leaves)

if __name__=='__main__':
 out=[]
 for m in range(2,11):
  row=solve(cat(m));verify(row)
  print('m',m,'rank',row['rank'],'N',row['concept_count'],'states',row['states'],'tree_nodes',2**row['rank']-1)
  out.append(row)
 Path(__file__).with_name('certificates.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n')
