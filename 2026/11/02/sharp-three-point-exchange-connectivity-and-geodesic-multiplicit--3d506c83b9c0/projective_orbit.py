"""Independent projective-linear orbit and exact code-exchange enumeration."""
from itertools import product,combinations
from collections import Counter,deque

def multiply(a,b):
    out=0
    for i in range(2):
        if b&(1<<i):out^=a<<i
    if out&8:out^=10
    if out&4:out^=7
    return out

def reduce(v):
    first=next(x for x in v if x)
    inverse=next(x for x in (1,2,3) if multiply(first,x)==1)
    return tuple(multiply(x,inverse) for x in v)

pts=sorted({reduce(v) for v in product(range(4),repeat=3) if any(v)})
assert len(pts)==21
loc={p:i for i,p in enumerate(pts)}
# A regular hyperoval, with f(t)=t^2, together with the two points at infinity.
seed={reduce((multiply(t,t),t,1)) for t in range(4)} | {(1,0,0),(0,1,0)}
assert len(seed)==6
initial=frozenset(loc[p] for p in seed)

def generators():
    for a,b in ((0,1),(1,2)):
        yield lambda v,a=a,b=b:tuple(v[b] if i==a else v[a] if i==b else v[i] for i in range(3))
    for a in range(3):
        for b in range(3):
            if a!=b:
                yield lambda v,a=a,b=b:tuple(v[i]^v[b] if i==a else v[i] for i in range(3))
    yield lambda v: (multiply(2,v[0]),v[1],v[2])

perms=[]
for g in generators():
    p=tuple(loc[reduce(g(v))] for v in pts)
    assert len(set(p))==21
    perms.append(p)

seen={initial};todo=deque([initial])
while todo:
    obj=todo.popleft()
    for perm in perms:
        next_obj=frozenset(perm[i] for i in obj)
        if next_obj not in seen:
            seen.add(next_obj);todo.append(next_obj)
assert len(seen)==168, ('orbit',len(seen))
H=sorted(sum(1<<i for i in subset) for subset in seen)
N=len(H)
intersections=Counter((H[i]&H[j]).bit_count() for i in range(N) for j in range(i+1,N))
assert dict(intersections)=={0:840,1:6048,2:3780,3:3360}
AD=[set() for _ in H]
for i in range(N):
 for j in range(i+1,N):
  if (H[i]&H[j]).bit_count()==3:
   AD[i].add(j);AD[j].add(i)
assert {len(row) for row in AD}=={40}
common= {t:set() for t in range(4)}
for i in range(N):
 for j in range(i+1,N):
  t=(H[i]&H[j]).bit_count()
  common[t].add(len(AD[i]&AD[j]))
assert common=={0:{4},1:{5},2:{16},3:{11}},common
for start in range(N):
 seen_d={start:0};Q=deque([start])
 while Q:
  x=Q.popleft()
  for y in AD[x]:
   if y not in seen_d:seen_d[y]=seen_d[x]+1;Q.append(y)
 assert len(seen_d)==N and max(seen_d.values())==2
print('INDEPENDENT_PGL_ORBIT_PASS')
print('hyperovals',N,'edges',sum(map(len,AD))//2,'intersection',sorted(intersections.items()),'common',common)
