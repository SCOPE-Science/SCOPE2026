from verify import paths

def test_perfect(n, limit=300000):
 vv, ds, pp=paths(n)
 masks=[]
 for p in pp:
  mask=sum(1<<i for i in p)
  cs=tuple(sorted({vv[i][2] for i in p}))
  masks.append((mask,cs))
 by=[[i for i,(mask,c) in enumerate(masks) if (mask>>v)&1] for v in range(len(vv))]
 allmask=(1<<len(vv))-1
 counter=0
 def walk(left,chosen):
  nonlocal counter
  if left==0:
   assert len(chosen)==n
   counter+=1
   deg={k:0 for k in range(n)};adj={k:[] for k in range(n)}
   for e in chosen:
    a,b=masks[e][1]
    deg[a]+=1;deg[b]+=1;adj[a].append(b);adj[b].append(a)
   assert all(v==2 for v in deg.values())
   seen=set()
   for a in range(n):
    if a in seen:continue
    chain=[];pending=[a]
    while pending:
     v=pending.pop()
     if v in seen:continue
     seen.add(v);chain.append(v)
     pending.extend(adj[v])
    assert len(chain)%2==0
   return
  v=(left&-left).bit_length()-1
  for idx in by[v]:
   mask,_=masks[idx]
   if mask&left==mask:
    walk(left^mask,chosen+(idx,))
    if counter>limit:raise RuntimeError('limit')
 walk(allmask,())
 return counter

for n in (2,3,4):print('PERFECT',n,test_perfect(n))
