import itertools,math
from collections import defaultdict,Counter
def ordered_partitions(items):
    """Generate every ordered partition exactly once."""
    if not items:
        yield ()
        return
    x=items[-1]
    for partition in ordered_partitions(items[:-1]):
        for j in range(len(partition)):
            groups=[tuple(z) for z in partition]
            groups[j]+= (x,)
            yield tuple(groups)
        for j in range(len(partition)+1):
            groups=[tuple(z) for z in partition]
            groups.insert(j,(x,))
            yield tuple(groups)

def allcones(m):
 n=m+2;edges=[(a,b) for a in range(2) for b in range(2,n)]
 seen={}
 for p in ordered_partitions(tuple(range(n))):
  lev={v:i for i,block in enumerate(p) for v in block}
  sig=tuple((lev[u]>lev[v])-(lev[u]<lev[v]) for u,v in edges)
  seen[sig]=1
 data={}
 for sig in seen:
  pa=list(range(n))
  def rt(a):
   while a!=pa[a]:a=pa[a]
   return a
  for (u,v),s in zip(edges,sig):
   if s==0:pa[rt(u)]=rt(v)
  roots=sorted(set(rt(i) for i in range(n)));ind={a:i for i,a in enumerate(roots)};q=len(roots)
  arcs={(ind[rt(u)],ind[rt(v)]) if s==-1 else (ind[rt(v)],ind[rt(u)]) for (u,v),s in zip(edges,sig) if s}
  G={i:[] for i in range(q)}
  for a,b in arcs:G[a].append(b)
  covers=[]
  for a,b in arcs:
   todo=list(x for x in G[a] if x!=b);reach=set(todo)
   while todo:
    for c in G[todo.pop()]:
     if c not in reach:reach.add(c);todo.append(c)
   if b not in reach:covers.append((a,b))
  d=q-1;data[sig]={'dim':d,'bad':len(covers)>d,'covers':len(covers)}
 bad=[s for s,v in data.items() if v['bad']]
 minbad=[]
 for s in bad:
  idx=[i for i,x in enumerate(s) if x]
  mini=True
  for mask in range(1,1<<len(idx)):
   t=list(s)
   for j,i in enumerate(idx):
    if mask>>j&1:t[i]=0
   tv=data.get(tuple(t))
   if tv and tv['bad']:
    mini=False;break
  if mini:minbad.append(s)
 return data,minbad

if __name__=='__main__':
 import sys
 for m in map(int,sys.argv[1:] or [2,3,4,5]):
  D,M=allcones(m)
  counts=Counter(D[s]['dim'] for s in M)
  expected=Counter({3:6}) if m==2 else Counter({3:(2**(m-1))*math.comb(m,2),m+1:2**m})
  assert counts==expected,(m,counts,expected)
  print('m=',m,' minimal_singular_cones=',dict(sorted(counts.items())), 'checked_total=',len(D))
 print('VERIFY_OK')
