from itertools import product
from math import comb, factorial

def valid(a,n):
 for j in range(n+1):
  B=[i for i,z in enumerate(a) if z==j]
  if len(B)>2 or (len(B)==2 and 0 not in B):return False
  if j:
   B=[i for i,z in enumerate(a) if z in (0,j)]
   if len(B)>2 or (len(B)==2 and 0 not in B):return False
 return True

def fall(a,k):return factorial(a)//factorial(a-k) if 0<=k<=a else 0

def counts(n):
 R=[0]*(n+2); NR=[0]*(n+2); E=[0]*(n+2)
 for f in product(range(n+2),repeat=n+1):
  if not valid(f,n):continue
  H=set(f)-{n+1};k=len(H); R[k]+=1
  if all(f[y]==y for y in H):E[k]+=1
  if k>=2 and 0 not in H and f[0]!=n+1 and f.count(f[0])==1: NR[k]+=1
 return R,NR,E

def regular_witness(f,n):
 H=set(f)-{n+1};g=[n+1]*(n+1)
 for y in H:
  fiber=[i for i in range(n+1) if f[i]==y]
  # avoid source center whenever H has no target center and has >=2 members
  if len(H)>=2 and 0 not in H:
   z=next((x for x in fiber if x!=0),None)
   if z is None:return None
   g[y]=z
  else:g[y]=fiber[0]
 if not valid(g,n):return None
 if any(f[g[y]]!=y for y in H):return None
 return tuple(g)

for n in range(2,6):
 R,NR,E=counts(n)
 Rp=[0]*(n+2);Np=[0]*(n+2);Ep=[0]*(n+2)
 Rp[0]=1;Ep[0]=1
 for k in range(1,n+1):
  Rp[k]+=comb(n,k)*(fall(n+1,k)+k*fall(n,k))
  Ep[k]+=comb(n,k)*(k+1)
  if k>=2:Np[k]=comb(n,k)*k*fall(n,k-1)
 Rp[1]+=2*n+1;Ep[1]+=n+1
 Rp[2]+=2*n*n
 for k in range(3,n+2):Rp[k]+=comb(n,k-1)*fall(n,k-1)
 for k in range(2,n+2):Ep[k]+=comb(n,k-1)
 assert (R,NR,E)==(Rp,Np,Ep),(n,(R,NR,E),(Rp,Np,Ep))
 print('n',n,'rank',R,'nonregular',NR,'idempotents',E,'total',sum(R),'nonreg',sum(NR),'idempotents',sum(E))
 for f in product(range(n+2),repeat=n+1):
  if not valid(f,n):continue
  nonreg=(len(set(f)-{n+1})>=2 and 0 not in (set(f)-{n+1}) and f[0]!=n+1 and f.count(f[0])==1)
  assert (regular_witness(f,n) is None)==nonreg,(n,f)
 if n<=3:
  allmaps=[f for f in product(range(n+2),repeat=n+1) if valid(f,n)]
  for f in allmaps:
   H=set(f)-{n+1}
   actual=any(all(g[y]!=n+1 and f[g[y]]==y for y in H) for g in allmaps)
   expected=regular_witness(f,n) is not None
   assert actual==expected,(n,f)
  print('Exhaustive inverse search passed,',len(allmaps),'x',len(allmaps))
print('VERIFY_OK')
