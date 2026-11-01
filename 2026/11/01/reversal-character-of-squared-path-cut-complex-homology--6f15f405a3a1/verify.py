from itertools import combinations
from math import comb

def faces(n,k):
 r=n-k
 for p in range(0,r+1):
  out=[]
  for F in combinations(range(n),p):
   C=tuple(v for v in range(n) if v not in F)
   if any(any(b-a>=3 for a,b in zip(T,T[1:])) for T in combinations(C,k)):
    out.append(F)
  yield p-1,out

def rho(n,F):return tuple(sorted(n-1-v for v in F))
def eps(n,F):
 new=[n-1-v for v in F]
 return (-1)**sum(new[i]>new[j] for i in range(len(new)) for j in range(i+1,len(new)))

def mat_rank(A,p=101):
 if not A:return 0
 R=len(A);C=len(A[0]);i=0
 for j in range(C):
  h=next((h for h in range(i,R) if A[h][j]%p),None)
  if h is None:continue
  A[i],A[h]=A[h],A[i]
  inv=pow(A[i][j]%p,-1,p)
  A[i]=[(x*inv)%p for x in A[i]]
  for h in range(i+1,R):
   if A[h][j]%p:
    a=A[h][j]%p
    A[h]=[(x-a*y)%p for x,y in zip(A[h],A[i])]
  i+=1
  if i==R:break
 return i

def signed_complex(n,k,lam):
 levels=list(faces(n,k)); dimensions={d:F for d,F in levels};bases={}; maps={}
 for d,F in levels:
  seen=set(); bs=[]; lookup={}
  for f in F:
   if f in seen:continue
   g=rho(n,f);seen.update([f,g]);s=eps(n,f)
   if g==f and s!=lam:continue
   j=len(bs);bs.append((f, g, s));lookup[f]=j
  bases[d]=bs;maps[d]=lookup
 ranks={}
 for d in range(0,n-k):
  bs=bases[d]; target=maps[d-1]; matrix=[[0]*len(bs) for _ in range(len(bases[d-1]))]
  for j,(f,g,s) in enumerate(bs):
   terms=[(f,1)] if f==g else [(f,1),(g,lam*s)]
   for F,co in terms:
    for z in range(len(F)):
     h=F[:z]+F[z+1:]
     i=target.get(h)
     if i is not None:matrix[i][j]+=(1 if z%2==0 else -1)*co
  ranks[d]=mat_rank(matrix)
 hom={d:len(bases[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in bases}
 return hom

def B(n,k):
 r=n-k
 return comb(n-1,k-1)-sum(comb(k-1,j)*(r-j+1) for j in range(min(k-1,r)+1))+r

def C(n,k):return comb(n,k) if 0<=k<=n else 0

def T(n,k):
 r=n-k;t=r//2;m=n//2
 if n%2==0 and r%2:
  return (-1)**(t+1)*(C(m-1,t)-1)
 if n%2==0:
  h=k//2-1;s=sum(C(h,j) for j in range(min(h,t)+1))
  return (-1)**t*(C(m-1,t)-s)
 if r%2:
  h=k//2-1;s=sum(C(h,j) for j in range(min(h,t)+1))
  return (-1)**(t+1)*(s-1)
 h=(k-1)//2;s=sum(C(h,j) for j in range(min(h,t)+1))
 return (-1)**t*(C(m,t)-s)

if __name__=='__main__':
 tests=[(6,3),(7,3),(7,4),(8,3),(8,4),(8,5),(9,3),(9,5)]
 for n,k in tests:
  b=B(n,k);t=T(n,k)
  Hp=signed_complex(n,k,1);Hm=signed_complex(n,k,-1)
  gotp=(b+t)//2;gotm=(b-t)//2
  assert Hp.get(n-k-1)==gotp and Hm.get(n-k-1)==gotm,(n,k,b,t,Hp,Hm)
  assert all(x==0 for d,x in Hp.items() if d!=n-k-1),(n,k,Hp)
  assert all(x==0 for d,x in Hm.items() if d!=n-k-1),(n,k,Hm)
  print(f'n={n},k={k},beta={b},trace={t},eig=({gotp},{gotm}),direct=({Hp[n-k-1]},{Hm[n-k-1]})')
 print('PASS')

def connected_symmetry_count(n,k):
 return sum(
  1 for A in combinations(range(n),k)
  if A==tuple(sorted(n-1-x for x in A))
  and all(y-x<=2 for x,y in zip(A,A[1:]))
 )

def predicted_symmetric_count(n,k):
 r=n-k;t=r//2
 if k%2:
  if not n%2:return 0
  h=(k-1)//2
 else:
  h=k//2-1
 return sum(C(h,j) for j in range(min(h,t)+1))

def direct_oriented_trace(n,k):
 r=n-k
 vertex_orbits=[(i,n-1-i) for i in range(n//2)]
 if n%2:vertex_orbits.append((n//2,))
 total=0
 for mask in range(1<<len(vertex_orbits)):
  F=tuple(sorted(v for j,o in enumerate(vertex_orbits) if mask>>j&1 for v in o))
  if len(F)>r:continue
  complement=tuple(i for i in range(n) if i not in F)
  if any(any(b-a>=3 for a,b in zip(A,A[1:])) for A in combinations(complement,k)):
   total+=(-1)**mask.bit_count()
 return (-1)**r*total

if __name__=='__main__':
 pair_count=0
 for n in range(5,16):
  for k in range(2,n-2):
   beta=B(n,k);trace=T(n,k)
   assert direct_oriented_trace(n,k)==trace,(n,k,trace)
   assert connected_symmetry_count(n,k)==predicted_symmetric_count(n,k),(n,k)
   assert abs(trace)<=beta and (beta-trace)%2==0
   pair_count+=1
 print(f'PASS {pair_count} direct oriented-face traces and palindromic subset counts')
