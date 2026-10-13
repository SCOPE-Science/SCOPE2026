import itertools,collections

def rank(vs,p):
 d={}
 for a in vs:
  a=list(a);a=tuple(x%p for x in a)
  for col in sorted(d):
   if a[col]:a=tuple((x-a[col]*y)%p for x,y in zip(a,d[col]))
  if any(a):
   col=next(i for i,x in enumerate(a) if x);a=tuple(x*pow(a[col],-1,p)%p for x in a);d[col]=a
 return len(d)
def spaces(n,p):
 for k in range(1,n):
  for piv in itertools.combinations(range(n),k):
   choices=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
   for vals in itertools.product(range(p),repeat=len(choices)):
    B=[[0]*n for _ in range(k)]
    for i,j in enumerate(piv):B[i][j]=1
    for (i,j),val in zip(choices,vals):B[i][j]=val
    yield tuple(map(tuple,B))
def verify(p):
 verts=[]
 for S in spaces(5,p):
  has_z=rank(S+((0,0,0,0,1),),p)==len(S)
  ok=has_z or all((a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2])%p==0 for a in S for b in S)
  if ok:
   proj=tuple(a[:4] for a in S)
   k=rank(proj,p)
   w=0 if k!=2 else int(any((a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2])%p for a in proj for b in proj))
   verts.append((proj,k,w))
 hist=collections.Counter()
 for i,(S,k,w) in enumerate(verts):
  deg=sum(rank(S+T,p)==4 for j,(T,_,_) in enumerate(verts) if i!=j)
  hist[(k,w,deg)]+=1
 predicted={
 (0,0,0):1,
 (1,0,p**3):(p**3+p**2+p+1)*(p+1),
 (2,0,p**5+p**4+p**3+p**2):(p**2+1)**2*(p+1),
 (2,1,p**5+p**4+p**2):p**2*(p**2+1),
 (3,0,p**5+3*p**4+3*p**3+2*p**2+p):p**3+p**2+p+1
 }
 print('p',p,'vertices',len(verts),'hist',hist,'expected',predicted)
 assert hist==predicted
verify(2)
verify(3)
