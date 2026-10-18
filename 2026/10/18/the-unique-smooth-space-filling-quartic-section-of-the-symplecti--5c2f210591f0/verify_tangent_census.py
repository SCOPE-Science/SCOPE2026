import itertools,collections,time
P=list(itertools.product((0,1),repeat=4));P.remove((0,0,0,0));P.sort()
M=[m for m in itertools.product(range(5),repeat=4) if sum(m)==4];idx={m:i for i,m in enumerate(M)}
N=35

def mon_eval(m,p):return int(all(p[i] or m[i]==0 for i in range(4)))
def ev(poly,p):return sum(((poly>>i)&1)*mon_eval(m,p) for i,m in enumerate(M))%2
def derivative(poly,p,k):return sum(((poly>>i)&1)*(m[k]%2)*mon_eval(tuple(m[j]-(j==k) for j in range(4)),p) for i,m in enumerate(M) if m[k])%2

def gauss_extend(bas,v):
 w=v
 for t in bas:
  w=min(w,w^t)
 if w:bas.append(w);bas.sort(reverse=True);return True
 return False

rows=[sum(mon_eval(m,p)<<i for i,m in enumerate(M)) for p in P]
# standard GF2 nullspace by forward pivot leftmost pivot
pivots={}
for row in rows:
 r=row
 while r:
  bit=r & -r;j=bit.bit_length()-1
  if j in pivots:r^=pivots[j]
  else:pivots[j]=r;break
free=[j for j in range(N) if j not in pivots]
ker=[]
for j in free:
 x=1<<j
 for i in sorted(pivots,reverse=True):
  if (pivots[i]&x).bit_count()%2:x|=1<<i
 ker.append(x)
assert len(ker)==20 and all(all((x&row).bit_count()%2==0 for row in rows) for x in ker)
G3={(2,1,0,0),(1,2,0,0),(0,0,2,1),(0,0,1,2)}
gradg=[]
for p in P:
 # dg=(y^2,x^2,w^2,z^2) = (y,x,w,z)
 gradg.append((p[1],p[0],p[3],p[2]))
# g multiplied by each variable, generated quarts
base=[]
for j in range(4):
 poly=0
 for m in G3:
  n=list(m);n[j]+=1;poly^=1<<idx[tuple(n)]
 assert all(ev(poly,p)==0 for p in P)
 assert gauss_extend(base,poly)
print('g linrank',len(base),'ker dim',len(ker),flush=True)
for k in ker:gauss_extend(base,k)
assert len(base)==20
# instead find 16 complement to span g*lin
base=[]
for j in range(4):
 poly=0
 for m in G3:
  n=list(m);n[j]+=1;poly^=1<<idx[tuple(n)]
 gauss_extend(base,poly)
comp=[]
for k in ker:
 if gauss_extend(base,k):comp.append(k)
assert len(comp)==16
line_to_points={}
for i,p in enumerate(P):
 for j,q in enumerate(P):
  if i>=j:continue
  l=[z for z,r in enumerate(P) if r==p or r==q or r==tuple(a^b for a,b in zip(p,q))]
  if len(l)!=3:continue
  lmask=sum(1<<z for z in l)
  line_to_points[lmask]=l
isotropic=[ll for ll in line_to_points if sum(P[line_to_points[ll][0]][k]*gradg[line_to_points[ll][1]][k] for k in range(4))%2==0]
assert len(isotropic)==15,len(isotropic)
per_pt_grad=[ [sum(derivative(poly,p,k)<<k for k in range(4)) for p in P] for poly in comp]
# all tangent line maps indexed by (p, derivative mask) 0..15, zero for singular, actual line code
L={ll:i for i,ll in enumerate(sorted(isotropic))};tanmap={}
for i,p in enumerate(P):
 g=sum(gradg[i][j]<<j for j in range(4));
 for h in range(16):
  if h in (0,g) or sum((h>>j&1)*p[j] for j in range(4))%2:tanmap[i,h]=-1;continue
  ll=sum(1<<k for k,r in enumerate(P) if sum(g>>j&1 and r[j] for j in range(4))%2==0 and sum(h>>j&1 and r[j] for j in range(4))%2==0)
  assert ll in L,(p,h,ll)
  tanmap[i,h]=L[ll]

h=[0]*15;nt=0;matching=collections.Counter();smooth_rational=0;distinct=0;examples=[]
prev=0; t=time.time()
for n in range(1<<16):
 gray=n^(n>>1)
 if n:
  change=(gray^prev).bit_length()-1
  for i in range(15):h[i]^=per_pt_grad[change][i]
 prev=gray
 tans=[tanmap[i,h[i]] for i in range(15)]
 if -1 in tans:continue
 smooth_rational+=1
 if len(set(tans))==15:
  distinct+=1
  matching[tuple(tans)]+=1
  if len(examples)<5:examples.append((gray,tans))
print('rational_smooth',smooth_rational,'distinct_tangent_matchings',len(matching),'forms_matchings',distinct,'matching_fiber_hist',collections.Counter(matching.values()),'time',time.time()-t,flush=True)
print('examples',examples[:3],flush=True)
print('lines',[(k,[P[i] for i in line_to_points[k]]) for k in L],flush=True)
