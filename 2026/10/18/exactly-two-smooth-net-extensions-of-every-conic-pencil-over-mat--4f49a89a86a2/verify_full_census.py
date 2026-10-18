import itertools, collections, time
start=time.monotonic()
F=3;n=6

def encode(v):
 return sum(v[i]*3**i for i in range(6))
vec=[tuple((t//3**i)%3 for i in range(6)) for t in range(729)]
def add(a,b):return encode(tuple((x+y)%3 for x,y in zip(vec[a],vec[b])))
def mul(t,a):return encode(tuple((x*t)%3 for x in vec[a]))
addition=[[add(i,j) for j in range(729)] for i in range(729)]
proj_id=[0]*729
for v in range(1,729):
 a=vec[v];i=next(i for i,x in enumerate(a) if x)
 proj_id[v]=v if a[i]==1 else mul(2,v)
rep=sorted(set(proj_id[1:]));print('projective forms',len(rep))
def smooth(k):
 a,b,c,d,e,f=vec[k]
 A,B,C=(2*a)%3,(2*b)%3,(2*c)%3
 return ((A*(B*C-f*f)-d*(d*C-e*f)+e*(d*f-B*e))%3)!=0
valid=[smooth(t) for t in range(729)];print('smooth conics',sum(valid[t] for t in rep))

def rrefs(k):
 for pivs in itertools.combinations(range(n),k):
  nz=[(i,j) for i,p in enumerate(pivs) for j in range(p+1,n) if j not in pivs]
  for terms in itertools.product(range(3),repeat=len(nz)):
   rows=[[0]*n for _ in range(k)]
   for i,p in enumerate(pivs):rows[i][p]=1
   for (i,j),t in zip(nz,terms):rows[i][j]=t
   yield tuple(map(encode,rows))
# directions in 2d, 3d, with first nonzero 1
def directions(k):
 return [v for v in itertools.product(range(3),repeat=k) if any(v) and next(x for x in v if x)!=2]
dir2=directions(2);dir3=directions(3)
def combo(rows,ts):
 v=0
 for row,t in zip(rows,ts):
  if t:v=addition[v][row if t==1 else mul(2,row)]
 return v
# validate dimensions
pcount=0;psmooth=[]
for rows in rrefs(2):
 pcount+=1
 if all(valid[combo(rows,d)] for d in dir2):psmooth.append(rows)
print('pencils',pcount,'smooth',len(psmooth))
ncount=0;nets=[];net_direct=collections.Counter()
for rows in rrefs(3):
 ncount+=1
 if all(valid[combo(rows,d)] for d in dir3):nets.append(rows)
print('nets',ncount,'smooth',len(nets))
# all smooth pencils in nets
pencil_to_nets=collections.Counter()
for rows in nets:
 forms=[proj_id[combo(rows,d)] for d in dir3]
 for i in range(13):
  for j in range(i+1,13):
   w=proj_id[addition[forms[i]][forms[j]]]
   if w not in forms:raise Exception('not net')
  
 # canonical pencil = set 4 forms, indexed by nonzero 2d sections of PG2(3) as lines
 seen=set()
 for i in range(13):
  for j in range(i+1,13):
   u,v=forms[i],forms[j]
   r=(u,v,proj_id[addition[u][v]],proj_id[addition[u][mul(2,v)]])
   seen.add(tuple(sorted(r)))
 assert len(seen)==13,len(seen)
 for x in seen:pencil_to_nets[x]+=1
print('incidence multiplicity:',sorted(collections.Counter(pencil_to_nets.values()).items()))
print('no ext',len(psmooth)-len(pencil_to_nets),'net',len(nets),'total pencils',len(psmooth))
print('examples nets',nets[:4])
print('elapsed',time.monotonic()-start)
# Canonical row-reduced echelon representation for subspaces
def canonical(rows):
 mat=[list(vec[r]) for r in rows];k=len(mat);ii=0
 for j in range(6):
  pivot=next((t for t in range(ii,k) if mat[t][j]),None)
  if pivot is None:continue
  mat[ii],mat[pivot]=mat[pivot],mat[ii]
  if mat[ii][j]==2:mat[ii]=[(2*t)%3 for t in mat[ii]]
  for r in range(k):
   if r!=ii and mat[r][j]:
    t=mat[r][j]
    mat[r]=[(a-t*b)%3 for a,b in zip(mat[r],mat[ii])]
  ii+=1
  if ii==k:break
 assert ii==k
 return tuple(encode(r) for r in mat)

def q_eval(q,p):
 a,b,c,d,e,f=vec[q];x,y,z=p
 return (a*x*x+b*y*y+c*z*z+d*x*y+e*x*z+f*y*z)%3

def q_trans(q,M):
 co=[]
 for i in range(3):co.append(q_eval(q,[M[r][i] for r in range(3)]))
 for i,j in [(0,1),(0,2),(1,2)]:
  p=[(M[r][i]+M[r][j])%3 for r in range(3)]
  co.append((q_eval(q,p)-co[i]-co[j])%3)
 return encode(co)

GENS=[[[0,1,0],[1,0,0],[0,0,1]],[[1,1,0],[0,1,0],[0,0,1]],[[2,0,0],[0,1,0],[0,0,1]],[[0,1,0],[0,0,1],[1,0,0]]]
trans=[[q_trans(q,M) for q in range(729)] for M in GENS]

def orbit(seed,allowed):
 seen={seed};q=[seed]
 for v in q:
  for T in trans:
   nv=canonical(tuple(T[t] for t in v))
   assert nv in allowed,(nv,v)
   if nv not in seen:seen.add(nv);q.append(nv)
 return seen
allnet=set(nets)
seen=set();orbs=[]
for x in nets:
 if x not in seen:
  O=orbit(x,allnet);orbs.append(O);seen.update(O)
print('net orbit sizes',sorted(map(len,orbs)))
allpencil=set(psmooth)
seenp=set();p_orbs=[]
for x in psmooth:
 if x not in seenp:
  O=orbit(x,allpencil);p_orbs.append(O);seenp.update(O)
print('pencil orbit sizes',sorted(map(len,p_orbs)))
# test pairs of extension net types on each projective pencil via canonical 4 conics
netidx={x:i for i,O in enumerate(orbs) for x in O}
pencil_net_types=collections.Counter()
netset_by_p={}
for nt in nets:
 forms=[proj_id[combo(nt,d)] for d in dir3]
 seen=set()
 for i in range(13):
  for j in range(i+1,13):
   u,v=forms[i],forms[j];r=tuple(sorted((u,v,proj_id[addition[u][v]],proj_id[addition[u][mul(2,v)]])))
   seen.add(r)
 for pp in seen:netset_by_p.setdefault(pp,[]).append(netidx[nt])
for typ in netset_by_p.values():pencil_net_types[tuple(sorted(typ))]+=1
print('pencil -> net orbit types',pencil_net_types)
print('pencil representative RREF',psmooth[0]);print('net reps RREF',[min(o) for o in orbs])
print('elapsed total',time.monotonic()-start)
