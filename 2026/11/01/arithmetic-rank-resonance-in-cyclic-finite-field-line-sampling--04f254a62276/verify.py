import numpy as np, itertools

def rank_direct(p,d,edges):
 B=np.zeros((d,d), dtype=int)
 for i,a in enumerate(edges):B[i,(i+1)%d]=a;B[(i+1)%d,i]=a
 E=[(None,0)]+[(i,s) for i in range(d) for s in range(1,p)]
 V=np.zeros((len(E),len(E)),dtype=complex)
 for z,(i,s) in enumerate(E):
  for w,(j,t) in enumerate(E):
   phase=0 if i is None or j is None else int(B[i,j])*s*t%p
   V[z,w]=np.exp(2j*np.pi*phase/p)
 return len(E)-np.linalg.matrix_rank(V,tol=1e-7)

def predicted(p,d,edges):
 if d%2:return 0
 a=1;b=1
 for i,e in enumerate(edges):
  if i%2==0:a=a*e%p
  else:b=b*e%p
 r=a*pow(b,-1,p)%p
 h=1;z=r
 while z!=1:z=z*r%p;h+=1
 m=d//2
 return 2*(p-1)//h if (m%2==0 or h%2==0) else 0

num=0
for p in (2,3,5,7,11):
 for d in range(3,11):
  patterns=[[1]*d]
  for k in range(1,min(p,5)):
   patterns.append([k]+[1]*(d-1))
  if p>3:patterns.append([2,3]+[1]*(d-2))
  for edges in patterns:
   pred=predicted(p,d,edges)
   got=rank_direct(p,d,edges)
   assert pred==got,(p,d,edges,pred,got)
   num+=1
print('PASS direct complex-rank comparisons',num)
# Additional characteristic-two extension-field tests, F4 = F2[a]/(a^2+a+1).
def gf4_mul(a,b):
 x=0
 for k in range(2):
  if (b>>k)&1:x^=a<<k
 if x&8:x^=0b1100
 if x&4:x^=0b111
 return x

def gf4_trace(a):
 return a ^ gf4_mul(a,a)

def rank_gf4(d,edges):
 b=[[0]*d for _ in range(d)]
 for i,w in enumerate(edges):b[i][(i+1)%d]=w;b[(i+1)%d][i]=w
 E=[(None,0)]+[(i,s) for i in range(d) for s in (1,2,3)]
 mat=np.ones((len(E),len(E)),dtype=float)
 for row,(i,s) in enumerate(E):
  for col,(j,t) in enumerate(E):
   if i is not None and j is not None:
    w=gf4_mul(gf4_mul(b[i][j],s),t)
    assert gf4_trace(w) in (0,1)
    mat[row,col]=(-1)**gf4_trace(w)
 return len(E)-np.linalg.matrix_rank(mat,tol=1e-8)

def pred_gf4(d,edges):
 if d%2:return 0
 a=b=1
 for k,x in enumerate(edges):
  if k%2==0:a=gf4_mul(a,x)
  else:b=gf4_mul(b,x)
 inverse={1:1,2:3,3:2}
 r=gf4_mul(a,inverse[b]);ord_r={1:1,2:3,3:3}[r]
 return 2*3//ord_r if d%4==0 else 0

ct=0
for d in range(3,9):
 for k in (1,2,3):
  e=[k]+[1]*(d-1)
  got=rank_gf4(d,e);want=pred_gf4(d,e)
  assert got==want,(d,e,got,want)
  ct+=1
print('PASS characteristic-four field comparisons',ct)
