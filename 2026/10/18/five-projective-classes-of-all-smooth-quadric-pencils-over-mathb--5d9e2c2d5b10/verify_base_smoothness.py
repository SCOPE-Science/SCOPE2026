import itertools
from verify_census import D,orbs
# polynomial tuples of exponents over F2
Z=(0,0,0)
def add(a,b):return a^b
def sh(a,m):return frozenset(tuple(x+y for x,y in zip(t,m)) for t in a)
def led(a):return max(a)
def divide(a,G):
 a=set(a)
 while a:
  m=max(a)
  hit=False
  for g in G:
   lt=max(g)
   if all(m[i]>=lt[i] for i in range(3)):
    delta=tuple(m[i]-lt[i] for i in range(3))
    a.symmetric_difference_update(sh(g,delta))
    hit=True;break
  if not hit: return frozenset(a)  # bad remainder early? need accumulate irreducibles separately
 return frozenset()
def red(a,G):
 a=set(a);r=set()
 while a:
  m=max(a)
  for g in G:
   lt=max(g)
   if all(m[i]>=lt[i] for i in range(3)):
    delta=tuple(m[i]-lt[i] for i in range(3))
    a.symmetric_difference_update(sh(g,delta));break
  else:
   r.add(m);a.remove(m)
 return frozenset(r)
def groebner(polys):
 G=[]
 for p in polys:
  r=red(p,G) if G else p
  if not r:continue
  if r==frozenset({Z}):return True,len(G)
  G.append(r)
 pairs=list(itertools.combinations(range(len(G)),2));i=0
 while i<len(pairs):
  x,y=pairs[i];i+=1;a,b=G[x],G[y];m=tuple(max(v,w) for v,w in zip(led(a),led(b)))
  diff1=tuple(u-v for u,v in zip(m,led(a)))
  diff2=tuple(u-v for u,v in zip(m,led(b)))
  s=add(sh(a,diff1),sh(b,diff2))
  r=red(s,G)
  if not r:continue
  if r==frozenset({Z}):return True,len(G)
  ni=len(G)
  pairs.extend((j,ni) for j in range(ni));G.append(r)
 return False,len(G)

def chart_polys(rep,fix):
 var=[i for i in range(4) if i!=fix]
 def to_poly(q):
  terms=set()
  for k,(i,j) in enumerate(D):
   if q>>k&1:
    exp=[0,0,0]
    if i!=fix:exp[var.index(i)]+=1
    if j!=fix:exp[var.index(j)]+=1
    t=tuple(exp)
    if t in terms:terms.remove(t)
    else:terms.add(t)
  return frozenset(terms)
 def deriv(p,v):
  out=set()
  for t in p:
   if t[v]%2:
    e=list(t);e[v]-=1;out.add(tuple(e))
  return frozenset(out)
 def times(a,b):
  out=set()
  for u in a:
   for v in b:
    t=tuple(x+y for x,y in zip(u,v))
    if t in out:out.remove(t)
    else:out.add(t)
  return frozenset(out)
 f,g=map(to_poly,rep[:2]);df=[deriv(f,i) for i in range(3)];dg=[deriv(g,i) for i in range(3)]
 return [f,g]+[add(times(df[i],dg[j]),times(df[j],dg[i])) for i,j in itertools.combinations(range(3),2)]

if __name__=='__main__':
 for rep,size,n1 in orbs:
  print(rep,size,n1)
  if n1 in(2,4):
   for k in range(4):
    print('chart',k,groebner(chart_polys(rep,k)))
assert len(orbs)==5
for rep,size,n1 in orbs:
 if n1 in (2,4):
  for chart in range(4):
   value,_=groebner(chart_polys(rep,chart))
   assert value,(rep,chart)
 else:
  assert n1 in (0,6)
print('BASE_SMOOTHNESS_VERIFY_OK')
