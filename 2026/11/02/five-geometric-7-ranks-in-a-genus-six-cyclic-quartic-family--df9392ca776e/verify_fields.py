#!/usr/bin/env python3
"""Independent direct Cartier iteration over F_7 and F_49 (i^2=-1)."""
import random
Q=49
ADD=[[((i%7+j%7)%7)+7*((i//7+j//7)%7) for j in range(Q)] for i in range(Q)]
MUL=[[((i%7*j%7-(i//7)*(j//7))%7)+7*(((i%7)*(j//7)+(i//7)*(j%7))%7) for j in range(Q)] for i in range(Q)]
NEG=[((-i%7)%7)+7*((-(i//7))%7) for i in range(Q)]
INV=[0]*Q
for i in range(1,Q):
 for j in range(1,Q):
  if MUL[i][j]==1: INV[i]=j; break
 assert INV[i]
FROB=[i%7 + 7*((-(i//7))%7) for i in range(Q)]
def plus(x,y): return ADD[x][y]
def prod(x,y):return MUL[x][y]
def power(x,n):
 y=1
 for _ in range(n): y=prod(y,x)
 return y
def polyprod(p,q):
 out=[0]*(len(p)+len(q)-1)
 for i,v in enumerate(p):
  for j,w in enumerate(q): out[i+j]=plus(out[i+j],prod(v,w))
 return out
def rank(A):
 if not A:return 0
 A=[list(row) for row in A];r=0;n=len(A[0])
 for j in range(n):
  k=next((k for k in range(r,len(A)) if A[k][j]),None)
  if k is None:continue
  A[k],A[r]=A[r],A[k]
  iv=INV[A[r][j]]
  A[r]=[prod(iv,v) for v in A[r]]
  for k in range(len(A)):
   if k!=r and A[k][j]:
    mul=A[k][j]
    A[k]=[plus(A[k][t],NEG[prod(mul,A[r][t])]) for t in range(n)]
  r+=1
  if r==len(A):break
 return r
def mm(A,B):
 n=len(A);k=len(B);m=len(B[0]);O=[[0]*m for _ in range(n)]
 for i in range(n):
  for t in range(k):
   if A[i][t]:
    for j in range(m):O[i][j]=plus(O[i][j],prod(A[i][t],B[t][j]))
 return O
BASIS=[(1,0),(2,0),(2,1),(3,0),(3,1),(3,2)]
def matrices(a,b,c):
 f=[c,b,0,a,0,1]
 powers={1:f};cur=[1]
 for e in range(1,6):
  cur=polyprod(cur,f)
  if e in (3,5):powers[e]=cur
 H=[[0]*6 for _ in range(6)]
 for col,(j,i) in enumerate(BASIS):
  jp=next(kk for kk in (1,2,3) if (7*kk-j)%4==0)
  pol=powers[(7*jp-j)//4]
  for row,(rr,ii) in enumerate(BASIS):
   if rr!=jp: continue
   e=7*(ii+1)-1-i
   if 0<=e<len(pol):H[row][col]=FROB[pol[e]]
 return H
def stable_rank(H):
 B=H
 for _ in range(10):
  B=mm(H,[[FROB[x] for x in row] for row in B])
 return rank(B)
def disc(a,b,c):
 terms=[(108,5,0,2),(16,4,3,0),(-900,3,1,2),(-128,2,4,0),(2000,1,2,2),(256,0,5,0),(3125,0,0,4)]
 z=0
 for v,aa,bb,cc in terms:
  q=prod(prod(power(a,aa),power(b,bb)),power(c,cc))
  z=plus(z,prod(v%7,q))
 return z
def predict(a,b,c):
 a2=prod(a,a);b2=prod(b,b);c2=prod(c,c)
 E=plus(prod(a,b2),c2)
 P=0
 for term in [prod(power(a,4),b),prod(6,prod(a2,b2)),prod(6,prod(a,c2)),prod(2,power(b,3))]: P=plus(P,term)
 W=prod(c,plus(a2,prod(2,b)))
 f=(2 if P else 0)+(2 if prod(a,E) else 1 if W else 0)
 rM=2 if prod(a,E) else 0 if (a==0 and c==0) else 1
 rV=1 if (c or P) else 0
 aa=5-rV-rM
 return f,aa
def test(seq,label):
 counts={};n=0
 for a,b,c in seq:
  if disc(a,b,c)==0:
   counts['singular']=counts.get('singular',0)+1;continue
  H=matrices(a,b,c)
  got=(stable_rank(H),6-rank(H));want=predict(a,b,c)
  assert got==want,(label,a,b,c,got,want)
  counts[got]=counts.get(got,0)+1;n+=1
 print(label,'smooth',n,'all classifications',dict(sorted(counts.items(),key=lambda kv:str(kv[0]))))
 return counts
if __name__=='__main__':
 count7=test(((a,b,c) for a in range(7) for b in range(7) for c in range(7)),'F7_EXHAUSTIVE')
 assert sum(v for k,v in count7.items())==343
 rng=random.Random(174203)
 count49=test(((rng.randrange(49),rng.randrange(49),rng.randrange(49)) for _ in range(3500)),'F49_DETERMINISTIC')
 # Independent F49 witnesses of the rank-one locus: sqrt(3) exists in F49.
 roots=[r for r in range(49) if prod(r,r)==3]
 assert len(roots)==2
 for r in roots:
  a,b,c=1,r,2
  assert disc(a,b,c)!=0
  assert (stable_rank(matrices(a,b,c)),6-rank(matrices(a,b,c)))==predict(a,b,c)
  assert predict(a,b,c)[0]==1
 print('DIRECT_GF7_GF49_SEMILINEAR_CARTIER_STRATIFICATION_OK')
