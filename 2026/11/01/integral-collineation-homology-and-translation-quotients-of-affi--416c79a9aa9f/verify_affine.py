from itertools import product
q=3
P=list(product(range(q), repeat=2)); Pidx={p:i for i,p in enumerate(P)}
D=list(range(q))+['inf']
lines=[]; line_data=[]
for d in D:
 for c in range(q):
  pts=frozenset(Pidx[p] for p in P if (p[0] if d=='inf' else (p[1]-d*p[0])%q)==c)
  lines.append(pts);line_data.append((d,c))
line_index={z:i for i,z in enumerate(lines)}
n=q*q+len(lines)
neighbors=[]
for v in range(n):
 ns=0
 for w in range(n):
  if w==v:continue
  yes=(v<q*q and w<q*q) or (v>=q*q and w>=q*q and line_data[v-q*q][0]!=line_data[w-q*q][0]) or (v<q*q and w>=q*q and v in lines[w-q*q]) or (w<q*q and v>=q*q and w in lines[v-q*q])
  if yes:ns|=1<<w
 neighbors.append(ns)
faces=[]
def rec(face,candidates):
 while candidates:
  lowest=candidates&-candidates
  v=lowest.bit_length()-1
  candidates^=lowest
  f=face|(1<<v)
  faces.append(f)
  rec(f,candidates&neighbors[v])
rec(0,(1<<n)-1)
print('faces',len(faces));print('f-vector', [sum(f.bit_count()==k for f in faces) for k in range(1,11)])
# Independent binary-chain rank computation for the complete complex.
def gf2rank(columns):
    pivots={}
    for v in columns:
        while v:
            j=v.bit_length()-1
            if j in pivots:v ^= pivots[j]
            else:
                pivots[j]=v;break
    return len(pivots)
bydim=[[f for f in faces if f.bit_count()==k+1] for k in range(max(f.bit_count() for f in faces))]
ranks={-1:0}
for k in range(1,len(bydim)):
    index={f:i for i,f in enumerate(bydim[k-1])}
    columns=[]
    for f in bydim[k]:
        z=0
        for i in range(n):
            if f>>i&1: z ^= 1<<index[f^(1<<i)]
        columns.append(z)
    ranks[k]=gf2rank(columns)
betti=[len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(len(bydim))]
assert betti == [1,0,16,16,0,0,0,0,0],betti
print('betti_mod2',betti)
def allinvertible():
 for a,b,c,d in product(range(q),repeat=4):
  if (a*d-b*c)%q:yield(a,b,c,d)
def perm(A,t):
 a,b,c,d=A;u,v=t
 op=[Pidx[((a*x+b*y+u)%q,(c*x+d*y+v)%q)] for x,y in P]
 ol=[]
 for line in lines:
  after=frozenset(op[p] for p in line)
  ol.append(q*q+line_index[after])
 return op+ol
def signrestricted(g,f):
 inds=[i for i in range(n) if f>>i&1]
 mapped=[g[i] for i in inds]
 inv=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
 return -1 if inv%2 else 1
def chi2(g):
 fp=sum(g[p]==p for p in range(q*q));fl=sum(g[i]==i for i in range(q*q,n))
 ff=sum(g[p]==p and g[q*q+j]==q*q+j for j,line in enumerate(lines) for p in line)
 return ff-fp-fl+1

def chi_top(g):
 # induced direction permutation
 pi=[D.index(line_data[g[q*q+j]-q*q][0]) for j in range(0,len(lines),q)]
 seen=set(); res=1;cycles=0
 for di in range(len(D)):
  if di in seen:continue
  cycles+=1; now=di;length=0
  while now not in seen:
   seen.add(now);length+=1;now=pi[now]
  fix=0
  for j in range(q):
   z=q*q+q*di+j
   for _ in range(length):z=g[z]
   fix+=(z==q*q+q*di+j)
  res*=fix-1
 return res*((-1)**(len(D)-cycles))

num=0
for A in allinvertible():
 for t in P:
  g=perm(A,t)
  lhs=sum((1 if f.bit_count()%2 else -1)*signrestricted(g,f) for f in faces if sum(1<<g[i] for i in range(n) if f>>i&1)==f)-1
  c2=chi2(g);ct=chi_top(g)
  if lhs!=c2-ct:raise AssertionError((A,t,lhs,c2,ct))
  num+=1
print('VERIFY_OK affine maps',num)
for A,t in [((1,0,0,1),(0,0)),((1,0,0,1),(1,0)),((0,1,1,0),(0,0)),((2,0,0,1),(0,0))]:
 g=perm(A,t);print('example',A,t,chi2(g),chi_top(g))
