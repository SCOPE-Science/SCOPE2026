"""Independent additive-Fourier pencil count with base-point binomial moments."""
from itertools import combinations
from math import comb
from gf2_ideal import smooth

S={i for i in range(1,4096) if smooth(i)}
assert len(S)==1116
xy=((1,0),(0,1),(1,1))
pts=list((p,q) for p in xy for q in xy)

def ev(F,p,q):
 a,b=p;c,d=q
 v=0
 for i in range(3):
  for j in range(4):
   if (F>>(4*i+j))&1:v^=(a**(2-i)*b**i*c**(3-j)*d**j)
 return v

# Avoid further geometric computations by using the 9 evaluation linear forms.
point_eval=[sum(ev(1<<k,p,q)<<k for k in range(12)) for p,q in pts]
# E(F,P) is parity of bits of the coefficient mask at which the monomial is nonzero.
point_smooth=[set(F for F in S if (F&m).bit_count()%2==0) for m in point_eval]

def fwht(a):
 h=1;n=len(a)
 while h<n:
  for i in range(0,n,2*h):
   for j in range(i,i+h):
    u,v=a[j],a[j+h]
    a[j],a[j+h]=u+v,u-v
  h*=2

def triples_count(T):
 A=[0]*4096
 for x in T:A[x]=1
 fwht(A)
 numer=sum(k*k*k for k in A)
 assert numer%(4096*6)==0
 return numer//(4096*6)

moments=[]
for r in range(5):
 total=0
 for I in combinations(range(9),r):
  X=S.copy()
  for j in I:X &=point_smooth[j]
  if len(X)<3:continue
  total+=triples_count(X)
 moments.append(total)
print('binomial moments',moments)
assert moments==[44070,62820,28512,3696,0]
Nk=[0]*4
Nk[3]=moments[3]
for r in (2,1,0):
 Nk[r]=moments[r]-sum(comb(k,r)*Nk[k] for k in range(r+1,4))
assert Nk==[6066,16884,17424,3696]
print('rational base distribution',Nk)
