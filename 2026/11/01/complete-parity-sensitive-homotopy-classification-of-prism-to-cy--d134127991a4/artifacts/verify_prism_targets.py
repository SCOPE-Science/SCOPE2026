import itertools, collections

def compute(n,q):
  vs=[]; steps=range(n)
  for bits in itertools.product((-1,1),repeat=n):
    if sum(bits)%q: continue
    for a in range(q):
      t=[a]
      for s in bits[:-1]: t.append((t[-1]+s)%q)
      for ss in itertools.product((-1,1),repeat=n):
        bot=tuple((t[i]+ss[i])%q for i in range(n))
        if all((bot[(i+1)%n]-bot[i])%q in (1,q-1) for i in range(n)):
          vs.append(tuple(t)+bot)
  vs=list(set(vs)); ids={v:i for i,v in enumerate(vs)}
  def neighbors(i):
    layer=i//n; j=i%n
    return (layer*n+(j-1)%n,layer*n+(j+1)%n,(1-layer)*n+j)
  seen=set(); comps=collections.defaultdict(list)
  for st in vs:
    if st in seen:continue
    work=[st]; seen.add(st); sz=0; w=sum((1 if (st[(i+1)%n]-st[i])%q==1 else -1) for i in range(n))//q
    while work:
      f=work.pop(); sz+=1
      for i in range(2*n):
        for c in range(q):
          if c==f[i] or not all((c-f[j])%q in (1,q-1) for j in neighbors(i)):continue
          g=f[:i]+(c,)+f[i+1:]
          if g not in seen: assert g in ids;seen.add(g);work.append(g)
    comps[w].append(sz)
  return len(vs),dict(sorted((w,sorted(v)) for w,v in comps.items()))

if __name__=='__main__':
 for n,q in [(3,3),(4,3),(5,3),(6,3),(4,5),(5,5),(6,5),(7,5),(4,6),(6,6),(8,6),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(4,8),(8,8)]:
  num,c=compute(n,q)
  exp={}
  if (q%2 or n%2==0):
    for w in range(-n//q-1,n//q+2):
      if abs(q*w)>n or ((q*w-n)%2): continue
      if abs(q*w)==n: exp[w]=[1]*(2*q)
      else: exp[w]=[-1]*(1 if q%2 else 2)
  assert sorted(c)==sorted(exp), (n,q,c,exp)
  for w,components in c.items():
    assert len(components)==len(exp[w]), (n,q,w,components)
    if exp[w][0]==1:assert all(size==1 for size in components)
    else:assert all(size>1 for size in components)
  print((n,q),num,c,flush=True)

print("PRISM_ALL_CYCLES_WINDING_AND_COMPONENT_COUNTS_VERIFIED")
