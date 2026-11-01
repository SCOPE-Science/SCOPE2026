from itertools import product
from collections import defaultdict,deque
from math import gcd

def sample(m,n):
    maps=[]
    for a in range(n):
      for eps in product((-1,1), repeat=m):
        if sum(eps)%n:continue
        v=[a]
        for s in eps[:-1]:v.append((v[-1]+s)%n)
        maps.append(tuple(v))
    ids={v:i for i,v in enumerate(maps)}
    adj=[{} for _ in maps]
    for idx,f in enumerate(maps):
      for i in range(m):
        pred=f[(i-1)%m]; succ=f[(i+1)%m]
        if pred != succ:continue
        alt=(2*pred-f[i])%n
        if alt==f[i]:continue
        g=list(f);g[i]=alt;g=tuple(g)
        j=ids[g]
        if i==0:
          delta=(alt-f[i])%n
          assert delta in (2,n-2),(m,n,delta)
          d=2 if delta==2 else -2
        else:d=0
        adj[idx][j]=d
    groups=[]; seen=set()
    for ii in range(len(maps)):
      if ii in seen:continue
      q=deque([ii]);seen.add(ii); parent={ii:None}; pots={ii:0}
      while q:
        u=q.popleft()
        for v,d in adj[u].items():
          if v not in parent:
            parent[v]=u; pots[v]=pots[u]+d
            q.append(v); seen.add(v)
      inds=set(parent)
      val=maps[ii]
      eps=[1 if (val[(j+1)%m]-val[j])%n==1 else -1 for j in range(m)]
      w=sum(eps)//n
      p=val[0]%2 if n%2==0 else None
      windgcd=0
      for u in inds:
        for v,d in adj[u].items():
          residual=pots[u]+d-pots[v]
          assert residual%n==0,(residual,n)
          windgcd=gcd(windgcd,abs(residual//n))
      groups.append((w,p,len(inds),windgcd))
    groups.sort()
    predicted=[]
    for r in range(1,m):
      total=m-2*r
      if total%n==0:
        w=total//n
        for p in (range(2) if n%2==0 else [None]):
          predicted.append((w,p))
    print(f'm={m},n={n},vertex_count={len(maps)}, component_tags={[(w,p) for w,p,sz,g in groups]}, sizes_gcd={groups}',flush=True)
    for w,p,sz,g in groups:
      if g==0: assert abs(w)==m/n # isolated
      else: assert g==(1 if n%2==0 else 2)
      if g!=0: assert (w,p) in predicted
    return len(maps),groups

if __name__=='__main__':
    for m,n in [(5,5),(6,5),(7,5),(8,5),(8,6),(10,6),(10,5),(12,6),(6,7),(9,7)]:
      sample(m,n)
    print('ALL_CHECKS_PASS')
