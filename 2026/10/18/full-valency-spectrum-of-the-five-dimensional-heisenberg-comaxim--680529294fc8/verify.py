from itertools import combinations, product
from collections import Counter

def rank(rows,p):
 a=[list(map(lambda z:z%p,r)) for r in rows]
 if not a:return 0
 n=len(a[0]); t=0
 for j in range(n):
  k=next((k for k in range(t,len(a)) if a[k][j]),None)
  if k is None: continue
  a[t],a[k]=a[k],a[t]
  inv=pow(a[t][j],-1,p);a[t]=[(v*inv)%p for v in a[t]]
  for i in range(len(a)):
   if i!=t and a[i][j]:
    w=a[i][j];a[i]=[(v-w*u)%p for v,u in zip(a[i],a[t])]
  t+=1
  if t==len(a):break
 return t

def spaces(n,p):
 for k in range(n+1):
  for piv in combinations(range(n),k):
   free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
   for vals in product(range(p),repeat=len(free)):
    B=[[int(j==piv[i]) for j in range(n)] for i in range(k)]
    for (i,j),v in zip(free,vals): B[i][j]=v
    yield tuple(map(tuple,B))

def bracket(v,w,p): return (v[0]*w[1]-v[1]*w[0]+v[2]*w[3]-v[3]*w[2])%p

def test(q):
 candidates=[]
 for B in spaces(5,q):
  if not B or len(B)==5:continue
  zz=(0,0,0,0,1)
  central=rank(B+(zz,),q)==len(B)
  if not central and any(bracket(v,w,q) for v,w in combinations(B,2)):continue
  P=[v[:4] for v in B]; dim=rank(P,q)
  candidates.append((B,P,dim,central))
 C=Counter(); nbr=Counter(); groups=Counter()
 for B,P,d,c in candidates:
  key=('Z' if d==0 else ('L' if d==1 else 'H' if d==3 else 'I' if any(bracket(v,w,q) for v,w in combinations(P,2))==False else 'N'))
  groups[key]+=1
  de=0
  for BB,PP,dd,cc in candidates:
   combined=B+BB
   full = rank(combined,q)==5
   if not full and any(bracket(v,w,q) for v,w in combinations(combined,2)):
    full = rank(combined+((0,0,0,0,1),),q)==5
   if full:de+=1
  C[(key,de)]+=1
 print('q=',q,'vertices',len(candidates),'groups=',groups,'degrees=',C)
 degs={
  ('Z',0):1,
  ('L',q**3):(q**3+q**2+q+1)*(q+1),
  ('I',q**5+q**4+q**3+q**2):(q+1)*(q**2+1)**2,
  ('N',q**5+q**4+q**2):q**2*(q**2+1),
  ('H',q**5+3*q**4+3*q**3+2*q**2+q):q**3+q**2+q+1
 }
 assert C==Counter(degs), (C,Counter(degs))
 return C

for q in (2,3):test(q)

print("VERIFY_OK")
