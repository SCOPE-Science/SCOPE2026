import itertools,numpy as np,math,collections
exps=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
idx={e:k for k,e in enumerate(exps)}
F={(4,0,0):1,(0,3,1):2,(0,1,3):1}
V=np.array([F.get(e,0) for e in exps],dtype=np.int16)
def mul(a,b):
 d={}
 for x,c in a.items():
  for y,e in b.items():
   k=tuple(x[i]+y[i] for i in range(3));d[k]=(d.get(k,0)+c*e)%3
 return {k:v for k,v in d.items() if v}
def powr(a,n):
 r={(0,0,0):1}
 for _ in range(n):r=mul(r,a)
 return r
def transform(F,m):
 S=[{tuple(int(t==j) for t in range(3)):int(m[i,j]) for j in range(3) if m[i,j]} for i in range(3)]
 pp=[[powr(x,k) for k in range(5)] for x in S]
 out={}
 for (a,b,c),n in F.items():
  z=mul(mul(pp[0][a],pp[1][b]),pp[2][c]);
  for k,v in z.items():out[k]=(out.get(k,0)+v*n)%3
 return {k:v for k,v in out.items() if v}
pts=sorted({tuple(int(x*pow(next(t for t in v if t),-1,3)%3) for x in v) for v in itertools.product(range(3),repeat=3) if any(v)})
inner=[p for p in pts if p[0]==0]
stab=[]
for vals in itertools.product(range(3),repeat=9):
 m=np.array(vals,dtype=int).reshape(3,3)
 if int(m[0,0]*(m[1,1]*m[2,2]-m[1,2]*m[2,1])-m[0,1]*(m[1,0]*m[2,2]-m[1,2]*m[2,0])+m[0,2]*(m[1,0]*m[2,1]-m[1,1]*m[2,0]))%3==0:continue
 im=transform(F,m)
 if im==F or im=={k:2*v%3 for k,v in F.items()}:
  if m.flat[next(i for i,z in enumerate(m.flat) if z)]==1:stab.append(m)
print('stabilizer',len(stab))
def norm(v):
 t=next(int(x)%3 for x in v if int(x)%3);return tuple(int(x*pow(int(t),-1,3)%3) for x in v)
perm=[]
for m in stab:
 pp=tuple(inner.index(norm(m@np.array(x))) for x in inner)
 perm.append(pp)
print('permutations distinct',len(set(perm)),'identity',sum(x==tuple(range(4)) for x in perm))
print('rational point set',inner)
