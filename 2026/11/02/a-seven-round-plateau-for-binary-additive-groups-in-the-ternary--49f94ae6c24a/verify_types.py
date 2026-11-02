from functools import lru_cache
import sys,time
MAXQ=int(sys.argv[1]) if len(sys.argv)>1 else 7
assert MAXQ == 7, 'The accompanying certificate is for ranks 1 through 7.'
sp=[{()}]
for t in range(MAXQ):
  nn=set()
  for u in sp[-1]:
    for p in range(1<<len(u)):
      nn.add(tuple(b|(((p>>i)&1)<<t) for i,b in enumerate(u)))
    nn.add(u+(1<<t,))
  sp.append(nn)
  print('spaces',t+1,len(nn),flush=True)
@lru_cache(None)
def atom(u,t):
  bits=0;o=0
  for i in range(t):
    for j in range(t):
      bits|=int(all(not(((b>>i)^(b>>j))&1) for b in u))<<o;o+=1
  for i in range(t):
    for j in range(t):
      for k in range(t):
        bits|=int(all(not(((b>>i)^(b>>j)^(b>>k))&1) for b in u))<<o;o+=1
  return bits
@lru_cache(None)
def edges(u,t):
  arr=[tuple(b|(((p>>i)&1)<<t) for i,b in enumerate(u)) for p in range(1<<len(u))]
  return arr,u+(1<<t,)
for Q in range(1,MAXQ+1):
  inter=[{} for _ in range(Q+1)]
  roots=[]
  for d in range(1,Q+2):
    ids={}
    for t in range(Q,-1,-1):
      new={}
      for u in sp[t]:
        if len(u)>d:continue
        a=atom(u,t)
        if t==Q:key=(a,())
        else:
          inspan,other=edges(u,t)
          vv=[ids[w] for w in inspan]
          if len(u)<d:vv.append(ids[other])
          key=(a,tuple(sorted(set(vv))))
        if key not in inter[t]:inter[t][key]=len(inter[t])+1
        new[u]=inter[t][key]
      ids=new
    roots.append(ids[()])
  expected = {1:[1,1],2:[1,2,2],3:[1,2,3,3],4:[1,2,3,3,3],5:[1,2,3,4,4,4],6:[1,2,3,4,5,5,5],7:[1,2,3,4,5,5,5,5]}[Q]
  assert roots == expected, (Q,roots,expected)
  print('Q',Q,'roots',roots,'nclasses',len(set(roots)),flush=True)
print('EXACT_ORBIT_RECURRENCE_OK')
