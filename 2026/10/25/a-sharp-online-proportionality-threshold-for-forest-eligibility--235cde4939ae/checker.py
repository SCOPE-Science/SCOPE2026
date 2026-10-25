from functools import lru_cache
from math import log2

def game_value(n, horizon):
 @lru_cache(None)
 def val(state):
  pa=list(range(n))
  def root(x):
   while pa[x]!=x:x=pa[x]
   return x
  d=[0]*n
  for a,b,loser in state:
   d[loser]+=1
   d[b if loser==a else a]-=1
   x,y=root(a),root(b)
   pa[x]=y
  worst=max([0]+d)
  if len(state)==horizon: return worst
  for a in range(n):
   for b in range(a+1,n):
    if root(a)==root(b):continue
    child=min(val(tuple(sorted(state+((a,b,l),)))) for l in (a,b))
    worst=max(worst,child)
  return worst
 v=val(())
 return v,val.cache_info()
if __name__=='__main__':
 for n in range(2,7):
  for t in range(n):
   v,info=game_value(n,t)
   b=(min(n,t+1)).bit_length()-1
   assert v==b,(n,t,v,b)
   print('n,t',n,t,'value',v,'cache',info.currsize,flush=True)


def witness(level, allocate, start=0):
    """Return (edges with loser, marked deficiency witness) for 2**level vertices."""
    d = {}
    edges=[]
    def build(vertices):
        if len(vertices)==1:
            d[vertices[0]]=0
            return vertices[0]
        half=len(vertices)//2
        a=build(vertices[:half])
        b=build(vertices[half:])
        loser=allocate(a,b,d.copy())
        assert loser in (a,b)
        winner=b if loser==a else a
        d[loser]+=1
        d[winner]-=1
        edges.append((a,b,loser))
        return loser
    marked=build(list(range(start,start+2**level)))
    assert len(edges)==2**level-1
    assert d[marked]==level, (level,d,marked)
    return edges,marked


def greedy_upper(n, edges):
    """Check the component-size certificate on an insertion forest."""
    parent=list(range(n))
    def root(a):
        while parent[a]!=a:a=parent[a]
        return a
    b=[0]*n
    for a,c in edges:
        ra,rc=root(a),root(c)
        assert ra!=rc
        loser=c if b[a]>=b[c] else a
        winner=a if loser==c else c
        b[loser]+=1
        b[winner]-=1
        parent[ra]=rc
        for v in range(n):
            comp=sum(root(u)==root(v) for u in range(n))
            if b[v]>0:assert (1<<b[v])<=comp, (n,edges,v,b,comp)
    return b

if __name__ == '__main__':
    for level in range(1,5):
        for policy in [lambda a,b,d:a, lambda a,b,d:b,
                       lambda a,b,d:a if d[a]>=d[b] else b]:
            edges, marked=witness(level,policy)
            assert len(edges)==(1<<level)-1
            assert marked < 1<<level
            upper=greedy_upper(1<<level,[(a,b) for a,b,l in edges])
            assert max(upper)<=level
    print('CONSTRUCTION: levels 1..4, three policies, all passed')
