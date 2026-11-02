from functools import lru_cache
from itertools import combinations_with_replacement

def run(m, cap):
  def norm(c, ps):return (c,)+tuple(v for pair in sorted((tuple(sorted(p,reverse=True)) for p in ps),reverse=True) for v in pair)
  @lru_cache(None)
  def fun(s):
    t=sum(s)
    ps=[s[1+2*i:3+2*i] for i in range(m)]
    st=sum(bool(x) for x in s)==1
    cl=t==1
    if st and cl: return (True,True)
    adj=[list(range(1,2*m+1))]+[[0,i+1 if i%2==1 else i-1] for i in range(1,2*m+1)]
    for i,x in enumerate(s):
      if x<2:continue
      for j in adj[i]:
        nxt=list(s);nxt[i]-=2;nxt[j]+=1
        nx=norm(nxt[0],[nxt[1+2*k:3+2*k] for k in range(m)])
        res=fun(nx);st=st or res[0];cl=cl or res[1]
        if st and cl:return (True,True)
    return (st,cl)
  for t in range(1,cap+1):
    bad=[0,0];witness=[None,None];ct=0
    # Enumerate canonical sorted unordered pairs from generating weak compositions for each pair
    pairlists=[[(a,b) for a in range(q,-1,-1) for b in range(a,-1,-1) if a+b==q] for q in range(t+1)]
    def gen(k,rem,last,ps):
      if k==m:
        yield norm(rem,ps);return
      for a in range(rem,-1,-1):
        for u,v in pairlists[a]:
          if last is not None and (u,v)>last:continue
          yield from gen(k+1,rem-a,(u,v),ps+[(u,v)])
    for s in gen(0,t,None,[]):
      # gen permits remaining hub
      res=fun(s);ct+=1
      for k in range(2):
        if not res[k]:bad[k]+=1;witness[k]=s
    print('m',m,'t',t,'canonical',ct,'badstack',bad[0],'badclear',bad[1],'examples',witness,'cache',fun.cache_info().currsize,flush=True)
    if t == cap:
      assert bad == [0,0], ('upper_bound_counterexample',m,witness)
    if t == cap-1:
      assert bad[0] > 0, ('lower_bound_counterexample_missing',m)
  badw=(1,1,1) if m==1 else norm(0, [(2*m+1,0)]+[(1,1)]*(m-1))
  assert fun(badw) == (False,False), ('explicit_witness_not_obstructive',m,badw)
if __name__=='__main__':
 for m in range(1,6):
  run(m,4*m)
 print('VERIFY_OK: complete canonical configurations at 4m for m=1..5')

# The replay below uses orbit representatives only after verifying that
# the designated hub and peripheral-pair permutations preserve adjacency.
