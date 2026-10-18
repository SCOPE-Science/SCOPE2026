"""Standalone exhaustive verifier of the minimal diameter-three multiset-partition threshold."""
import itertools,collections

def parts(n):
 def visit(prefix,hi):
  if len(prefix)==n:
   yield tuple(prefix)
   return
  for v in range(hi+2): yield from visit(prefix+[v],max(hi,v))
 return list(visit([0],0))

def distances(n,edge_mask):
 ad=[0]*n;edges=list(itertools.combinations(range(n),2))
 for i,(u,v) in enumerate(edges):
  if edge_mask>>i &1:ad[u]|=1<<v;ad[v]|=1<<u
 out=[];diam=0
 for i in range(n):
  cur=[99]*n;cur[i]=0;visited=1<<i;front=1<<i;d=0
  while front:
   new=0
   while front:
    bit=front&-front;front-=bit;v=bit.bit_length()-1;new|=ad[v]
   new&=~visited
   if not new:break
   visited|=new;front=new;d+=1
   while new:
    bit=new&-new;new-=bit;cur[bit.bit_length()-1]=d
  if visited != (1<<n)-1:return None
  diam=max(diam,d);out.append(cur)
 return (diam,out)

def find_partition(dists,pre):
 n=len(dists)
 for p in pre:
  k=max(p)+1
  if k >n:continue
  blocks=[[]for _ in range(k)]
  for i,j in enumerate(p):blocks[j].append(i)
  codes=set()
  for v in range(n):
   code=tuple(sorted(min(dists[v][u] for u in block) for block in blocks))
   if code in codes:break
   codes.add(code)
  else:return p
 return None

def iso_to_witness(n,mask,wm):
 edges=list(itertools.combinations(range(n),2))
 for perm in itertools.permutations(range(n)):
  em=0
  for i,(u,v) in enumerate(edges):
   if wm>>i &1:
    a,b=sorted((perm[u],perm[v]));em|=1<<edges.index((a,b))
  if em==mask:return True
 return False

witness=[(0,1),(0,3),(0,4),(1,2),(1,5),(2,3),(3,4)]
n=6;edges=list(itertools.combinations(range(n),2));wm=sum(1<<edges.index(e) for e in witness)
counts={};unique_masks=[]
for n in (4,5,6):
 p=parts(n); total=0;hit=0;low4=0
 for mask in range(1<<(n*(n-1)//2)):
  d=distances(n,mask)
  if d is None or d[0]!=3:continue
  total+=1
  q=find_partition(d[1],p)
  if q is not None:
   hit+=1
   if max(q)+1==4:low4+=1
   if n==6:unique_masks.append(mask)
 counts[n]=(total,hit,low4)
 print('n',n,'diam3 connected labeled',total,'resolvable labeled',hit,'four-part witness',low4)
print('passing graph isomorphism checks',len(unique_masks))
assert counts[4][1]==0 and counts[5][1]==0
assert counts[6][1]>0 and counts[6][2]==0
assert all(iso_to_witness(6,mask,wm)for mask in unique_masks)
d=distances(6,wm);q=find_partition(d[1],parts(6));print('witness:',witness,'partition',q, 'codes',[tuple(sorted(min(d[1][v][u] for u in range(6) if q[u]==j) for j in range(max(q)+1))) for v in range(6)])
optimum=[]
for partition in parts(6):
 if find_partition(d[1],[partition]) is not None:
  optimum.append(partition)
print('all resolving partition-size counts',dict(sorted(collections.Counter(max(p)+1 for p in optimum).items())))
print('all resolving partitions',optimum)
assert len(optimum)==2 and all(max(p)+1 == 5 for p in optimum)
assert set(optimum)=={(0,1,1,2,3,4),(0,1,2,1,3,4)}
print('PASS: global diameter-two obstruction is mathematical; six-vertex diameter-three census complete')
