# Reproducible rank certificate for 165 incidence curves on Fermat cubic Fano scheme.
from collections import Counter

def mul(a,b):
 z=0
 for i in range(2):
  if (b>>i)&1:z^=a<<i
 if z&8:z^=0b1110
 if z&4:z^=0b111
 return z

def pow2(a): return mul(a,a)
def normalize(v):
 t=next(x for x in v if x); inv=next(x for x in range(1,4) if mul(x,t)==1)
 return tuple(mul(x,inv) for x in v)

pts=set()
for idx in range(1,4**5):
 v=tuple((idx>>(2*i))&3 for i in range(5))
 if sum(x!=0 for x in v) in (2,4):pts.add(normalize(v))
pts=sorted(pts)
assert len(pts)==165

def herm(v,w):
 a=0
 for x,y in zip(v,w):a^=mul(pow2(x),y)
 return a
assert all(herm(p,p)==0 for p in pts)
N=len(pts)
A=[[int(p!=q and herm(p,q)==0) for q in pts] for p in pts]
assert all(sum(row)==36 for row in A)
assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
# strongly regular graph: each incident pair shares 3 others; each nonincident pair shares 9 others
for i in range(N):
 for j in range(i):
  count=sum(A[i][k]*A[j][k] for k in range(N))
  assert count==(3 if A[i][j] else 9),(i,j,count)
# A^2 = 36I+3 A+9(J-I-A)=27I-6A+9J
assert all(sum(A[i][k]*A[k][j] for k in range(N)) == (27 if i==j else 0)-6*A[i][j]+9 for i in range(N) for j in range(N))
# Thus eigenvalues = 36 (1), 3 (120), -9(44). Intersection matrix A-3I: rank 45.
fixed=sum(tuple(pow2(x) for x in p)==p for p in pts)
trace_FA=sum(herm(p,tuple(pow2(x) for x in p))==0 and tuple(pow2(x) for x in p)!=p for p in pts)
assert fixed==15 and trace_FA==30
trace_neg9=(15*fixed-5*trace_FA+N)//60
assert trace_neg9==4 and (15*fixed-5*trace_FA+N)%60==0
invariant_rank=1+(44+trace_neg9)//2
assert invariant_rank==25
print('VERIFY_OK: 165 elliptic-curve labels, GQ(4,8) parameters (165,36,3,9), Gram rank 45, F2 invariant span 25')
