import collections,itertools,functools,heapq
n,m=7,3;NV=n*m; ALL=(1<<NV)-1
adj=[0]*NV
for i in range(n):
 for a in range(m):
  u=i*m+a
  for j in ((i+1)%n,(i-1)%n):
   for b in range(m):
    if b!=a:adj[u]|=1<<(j*m+b)
cells=set()
def enum(avail,s):
 if s:cells.add(s)
 while avail:
  bit=avail&-avail;avail^=bit;v=bit.bit_length()-1
  enum(avail & ~adj[v],s|bit)
enum(ALL,0)
F=collections.Counter(v.bit_count()-1 for v in cells)
assert len(cells)==5281 and sorted(F.items())==[(0,21),(1,168),(2,658),(3,1365),(4,1554),(5,1022),(6,402),(7,84),(8,7)]
ORDER=[8,13,3,20,2,9,5,16,19,7,10,4,14,17,11,0,1,15,12,6,18]
avail=cells.copy();pairs=[]
for v in ORDER:
 bit=1<<v
 for s in sorted(avail):
  if not (s&bit) and (s|bit) in avail:
   avail.remove(s);avail.remove(s|bit);pairs.append((s,s|bit))
crit=avail
assert collections.Counter(s.bit_count()-1 for s in crit)=={0:1,3:1,4:3}
assert len(pairs)==2638
# Verify acyclicity of the entire directed Hasse diagram; matched edges point up.
pair_set=set(pairs)
adjacency={s:[] for s in cells}
indegree={s:0 for s in cells}
for upper in cells:
    for v in range(NV):
        if not ((upper>>v)&1):continue
        lower=upper^(1<<v)
        if lower not in cells:continue
        source,target=(lower,upper) if (lower,upper) in pair_set else (upper,lower)
        adjacency[source].append(target)
        indegree[target]+=1
queue=collections.deque(s for s in cells if indegree[s]==0)
removed=0
while queue:
    source=queue.popleft(); removed+=1
    for target in adjacency[source]:
        indegree[target]-=1
        if indegree[target]==0:queue.append(target)
assert removed==len(cells),(removed,len(cells))
del adjacency,indegree,pair_set,queue
up=dict(pairs);down={b:a for a,b in pairs}
@functools.lru_cache(None)
def bd(face):
 return [(face^(1<<i),(-1)**j) for j,i in enumerate(i for i in range(NV) if (face>>i)&1)]
@functools.lru_cache(None)
def proj(face):
 if face in crit:return {face:1}
 if face in down:return {}
 U=up[face];e=dict(bd(U))[face];out=collections.Counter()
 for S,c in bd(U):
  if S!=face:
   for C,b in proj(S).items():out[C]-=(c//e)*b
 return {k:v for k,v in out.items() if v}

def cycle_lift(c):
 k=c.bit_count()-1
 lows=[s for s in up if s.bit_count()==k]
 out_edges={s:[] for s in lows};indeg={s:0 for s in lows};lset=set(lows)
 for s in lows:
  for t,_ in bd(up[s]):
   if t!=s and t in lset:
    out_edges[s].append(t);indeg[t]+=1
 q=[s for s in lows if indeg[s]==0]; heapq.heapify(q); topo=[]
 while q:
  s=heapq.heappop(q);topo.append(s)
  for t in out_edges[s]:
   indeg[t]-=1
   if not indeg[t]:heapq.heappush(q,t)
 assert len(topo)==len(lows),(len(topo),len(lows))
 z=collections.Counter({c:1}); boundary=collections.Counter(dict(bd(c)))
 for s in topo:
  a=boundary[s]
  if a:
   U=up[s];e=dict(bd(U))[s];coeff=-a//e
   z[U]+=coeff
   for t,v in bd(U):boundary[t]+=coeff*v
 assert all(v==0 for v in boundary.values()), [(i,v) for i,v in boundary.items() if v][:5]
 return {k:v for k,v in z.items() if v}

def permute_simplex(face,perm):
 vertices=[i for i in range(NV) if face>>i&1]
 mapped=[perm[i] for i in vertices]
 neg=sum(1 for i in range(len(mapped)) for j in range(i+1,len(mapped)) if mapped[i]>mapped[j])
 new=sum(1<<v for v in mapped)
 return new,(-1)**neg

def symmetry(shift,reflect,colors):
 return [( ( ((-i if reflect else i) +shift)%n)*m + colors[a] ) for i in range(n) for a in range(m)]

critical_by_dim={k:sorted(s for s in crit if s.bit_count()-1==k) for k in (0,3,4)}
cycles={c:cycle_lift(c) for k in (3,4) for c in critical_by_dim[k]}
assert sorted(len(z) for c,z in cycles.items() if c.bit_count()==5)==[90,96,154]
assert sorted(len(z) for c,z in cycles.items() if c.bit_count()==4)==[16]
# The signed integral Morse attaching degree 4 -> 3 vanishes.
for c in critical_by_dim[4]:
    b=collections.Counter()
    for f,a in bd(c):
        for e,v in proj(f).items():b[e]+=a*v
    assert all(v==0 for v in b.values())


def matrix(perm,k):
 basis=critical_by_dim[k]
 cols=[]
 for c in basis:
  image=collections.Counter()
  for s,a in cycles[c].items():
   t,sign=permute_simplex(s,perm)
   for d,b in proj(t).items():image[d]+=a*sign*b
  cols.append([image[b] for b in basis])
 return [list(row) for row in zip(*cols)]

def direct_lefschetz(perm):
 v=0
 for s in cells:
  t,e=permute_simplex(s,perm)
  if t==s:v+=(-1)**(s.bit_count()-1)*e
 return v

data={}
for a in range(n):
 for refl in (0,1):
  for colors in itertools.permutations(range(m)):
   p=symmetry(a,refl,colors)
   M3=matrix(p,3);M4=matrix(p,4)
   trace3=M3[0][0];trace4=sum(M4[i][i] for i in range(3))
   LF=direct_lefschetz(p)
   assert LF==1-trace3+trace4,(a,refl,colors,LF,trace3,trace4)
   data[(a,refl,colors)]=(trace3,trace4,M3,M4)
assert len(data)==84
assert collections.Counter((v[0],v[1]) for v in data.values())=={(-1,-1):21,(1,-1):21,(1,0):14,(-1,0):14,(1,3):7,(-1,3):7}
identity=(0,1,2)
for shift in range(n):
    for reflection in (0,1):
        color_identity=data[(shift,reflection,identity)]
        assert color_identity[2]==[[(-1)**reflection]]
        assert color_identity[3]==[[1,0,0],[0,1,0],[0,0,1]]
        for colors in itertools.permutations(range(m)):
            inversions=sum(colors[i]>colors[j] for i in range(m) for j in range(i+1,m))
            sign=(-1)**inversions
            t3,t4,_,_=data[(shift,reflection,colors)]
            assert t3==sign*(-1)**reflection
            assert t4==(3 if colors==identity else (0 if all(colors[i]!=i for i in range(m)) else -1))
assert sum(data[(0,0,c)][1]*1 for c in itertools.permutations(range(m)))==0
print('C7K3_COMPLETE_INTEGER_MORSE_AND_84_EQUIVARIANT_CHARACTERS_OK')
