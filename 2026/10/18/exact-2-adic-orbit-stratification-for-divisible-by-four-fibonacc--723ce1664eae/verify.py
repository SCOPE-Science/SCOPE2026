"""Exhaustive state-cycle tests and exact matrix-lifting tests for the divisible-by-four coefficient family."""
from collections import Counter

def mul(a,b):
 return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
def matpow(m,j):
 a=(1,0,0,1)
 while j:
  if j&1:a=mul(a,m)
  m=mul(m,m); j//=2
 return a
def exp_counts(c,k):
 h=0; q=abs(c)
 while q%2==0 and q>0:q//=2; h+=1
 assert c!=0 and h>=2
 F0=1<<min(k,h)
 F=lambda j:1<<(2*min(k,h+j-1))
 out={1:F0}
 out[2]=(F(1)-F0)//2
 for j in range(2,max(2,k-h+2)):
  v=(F(j)-F(j-1))//(1<<j)
  if v:out[1<<j]=v
 return out

def orbit_counts(c,k):
 m=1<<k; visited=bytearray(m*m); ct=Counter()
 for a in range(m):
  for b in range(m):
   if visited[a*m+b]:continue
   x,y=a,b; length=0
   while not visited[x*m+y]:
    visited[x*m+y]=1; length+=1
    x,y=y,(x+c*y)%m
   assert (x,y)==(a,b)
   ct[length]+=1
 return dict(ct)

C=[-48,-32,-24,-20,-16,-12,-8,-4,4,8,12,16,20,24,28,32,44,48]
for c in C:
 for k in range(1,9):
  got=orbit_counts(c,k)
  expected=exp_counts(c,k)
  assert got==expected,(c,k,got,expected)
  assert sum(L*n for L,n in got.items())==(1<<k)**2
 for k in range(1,9):
  m=(0,1,1,c)
  h=(abs(c)&-abs(c)).bit_length()-1
  for j in range(1,9):
   a=matpow(m,1<<j); d=1<<(h+j-1)
   assert all((a[i]-(1 if i in (0,3) else 0))%d==0 for i in range(4))
   b=tuple((a[i]-(1 if i in (0,3) else 0))//d for i in range(4))
   assert (b[0]*b[3]-b[1]*b[2])%2==1,(c,j,b)
print('VERIFY_OK: 144 exhaustive cycle spectra and exact 2-adic matrix factors')
