from collections import Counter
p=1000003
assert all(p%d for d in range(2, int(p**0.5)+1))  # Exact primality test
assert pow(2,p-1,p)==1 and (p-1)%6==0
zeta=next(t for t in range(2,p) if pow(t,6,p)==1 and pow(t,3,p)!=1 and pow(t,2,p)!=1)
print('zeta',zeta,p)
F=[[pow(zeta,(i*j)%6,p) for j in range(6)] for i in range(6)]
def rank(A):
 A=[row[:] for row in A];m=len(A);n=len(A[0]) if m else 0;r=0
 for j in range(n):
  i=next((i for i in range(r,m) if A[i][j]),None)
  if i is None:continue
  A[r],A[i]=A[i],A[r];inv=pow(A[r][j],-1,p)
  for col in range(j,n):A[r][col]=A[r][col]*inv%p
  for i in range(r+1,m):
   if A[i][j]:
    c=A[i][j]
    for col in range(j,n): A[i][col]=(A[i][col]-c*A[r][col])%p
  r+=1
  if r==m:break
 return r
mu={0:0}
for S in range(1,64):
 cols=[i for i in range(6) if S>>i&1]; sz=len(cols); mx=-1
 for B in range(64):
  rows=[i for i in range(6) if B>>i&1]
  if len(rows)<=mx:continue
  if rank([[F[i][j] for j in cols] for i in rows])<sz:mx=len(rows)
 mu[S]=6-mx
# This mod test checks only rank constraints; support kernels may contain some zeros, so it is lower bound.
ct=Counter();small=[]
for sf in range(1,64):
 for sg in range(1,64):
  masks=[sum(1<<j for j in range(6) if (sf>>j)&1 and (sg>>((j-k)%6))&1) for k in range(6)]
  b=sum(mu[s] for s in masks)
  ct[b]+=1
  if b<12:small.append((sf,sg,b))
print('mu class',[(i,dict(Counter(mu[s] for s in range(1,64) if s.bit_count()==i))) for i in range(1,7)])
print('lower counts',[(i,ct[i]) for i in range(0,17)])
print('small pair groups',Counter((sf.bit_count(),sg.bit_count(),b) for sf,sg,b in small))
assert len(small)==50 and all(b==6 for _,_,b in small)
assert Counter((sf.bit_count(),sg.bit_count()) for sf,sg,b in small)=={(1,1):36,(2,2):9,(3,3):4,(6,6):1}
assert all(ct[i]==0 for i in (7,8,9,10,11))
# For f=g=(1,0,0,2,0,0), the two active rows have supports 6 and 3.
f=[1,0,0,2,0,0]; g=f[:]
counts=[]
for k in range(6):
 h=[f[j]*g[(j-k)%6] for j in range(6)]
 counts.append(sum(any(x!=0 for x in [(sum(h[j]*F[e][j] for j in range(6))%p)]) for e in range(6)))
assert counts==[6,0,0,3,0,0],counts
print('attainment row support sizes:',counts,'total:',sum(counts))
