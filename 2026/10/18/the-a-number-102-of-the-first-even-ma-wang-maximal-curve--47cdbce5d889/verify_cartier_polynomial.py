from functools import lru_cache
from collections import Counter
p=3;q=3;n=4;m=q**n+1;r=(q**(n-1)-1)//(q-1);b=q*(q-1)
A=(0,2,0,1); B=(1,0,1,0,1,0,1)
def mul(X,Y):
  O=[0]*(len(X)+len(Y)-1)
  for i,x in enumerate(X):
   if x:
    for j,y in enumerate(Y):
     if y: O[i+j]=(O[i+j]+x*y)%p
  while len(O)>1 and not O[-1]: O.pop()
  return tuple(O)
@lru_cache(None)
def powb(e):
  assert e>=0
  if e==0: return (1,)
  if e%2:return mul(B,powb(e-1))
  T=powb(e//2);return mul(T,T)
@lru_cache(None)
def powa(e):
  if e==0:return (1,)
  return mul(A,powa(e-1))
def divexact(num,den):
 n=list(num);d=list(den);z=[0]*max(1,len(n)-len(d)+1)
 while len(n)>=len(d):
  h=len(n)-len(d);f=n[-1]*pow(d[-1],-1,p)%p;z[h]=f
  for i,v in enumerate(d):n[i+h]=(n[i+h]-f*v)%p
  while n and n[-1]==0:n.pop()
 if any(n):raise ValueError(('nondivisible',num,den,n))
 return tuple(z)
def rank(cols,nrows):
 M=[[cols[c][i] if i<len(cols[c]) else 0 for c in range(len(cols))] for i in range(nrows)]
 piv=[]; row=0
 for col in range(len(cols)):
  k=next((i for i in range(row,nrows) if M[i][col]),None)
  if k is None: continue
  M[row],M[k]=M[k],M[row]
  inv=pow(M[row][col],-1,p)
  M[row]=[x*inv%p for x in M[row]]
  for i in range(nrows):
   if i!=row and M[i][col]:
    z=M[i][col];M[i]=[(a-z*b)%p for a,b in zip(M[i],M[row])]
  piv.append((row,col));row+=1
  if row==nrows:break
 return row, piv
D={j:max(0,j-b*(j*r//m)-1) for j in range(1,m)}
assert sum(D.values())==324
sumrank=0; data=[]
for j in range(1,m):
  src=D[j]
  if not src:continue
  jnew=(j*pow(p,-1,m))%m
  assert jnew
  target=D[jnew]
  t=(p*jnew-j)//m
  assert 0<=t<=2
  exp=j*r//m+r*t
  denom=powb(jnew*r//m)
  cols=[]
  for k in range(src):
   P=mul((0,)*k+(1,),mul(powa(t),powb(exp)))
   Q=tuple(P[e] for e in range(p-1,len(P),p))
   if not Q: Q=(0,)
   Z=divexact(Q,denom)
   if len(Z)>target and any(Z[target:]):raise ValueError(('too large',j,k,jnew,target,Z))
   cols.append(Z)
  rk,pivs=rank(cols,target)
  sumrank+=rk
  data.append((j,jnew,src,target,t,rk,src-rk))
print('genus',sum(D.values()),'cartier_rank',sumrank,'a_number',sum(D.values())-sumrank)
print('nontrivial blocks',len(data),'rank distribution',Counter((x[2],x[3],x[5]) for x in data))
print('columns failures',[(j,jnew,src,target,t,rk) for j,jnew,src,target,t,rk,z in data if rk<min(src,target)][:20])
print('total null',sum(x[-1] for x in data))
print('data',data)
