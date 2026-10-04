#!/usr/bin/env python3
from pathlib import Path
import itertools,collections,json
ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
def mul(a,b):
 a0,a1=a&1,(a>>1)&1;b0,b1=b&1,(b>>1)&1
 return (a0*b0^a1*b1)|(((a0*b1)^(a1*b0)^(a1*b1))<<1)
def pw(a,e):
 r=1
 while e:
  if e&1:r=mul(r,a)
  a=mul(a,a);e//=2
 return r
def cj(a):return pw(a,2)
def inv(a):return pw(a,2)
assert mul(2,2)==3 and mul(2,3)==1
def cyc(v,s):
 s%=len(v);return v[-s:]+v[:-s] if s else v[:]
def fs(t,s):return sum((cyc(b,s) for b in t),[])
def rr(A):
 A=[r[:] for r in A];r=0;P=[]
 for c in range(len(A[0])):
  p=next((i for i in range(r,len(A)) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];ii=inv(A[r][c]);A[r]=[mul(ii,x) for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][c]:
    f=A[i][c];A[i]=[A[i][j]^mul(f,A[r][j]) for j in range(len(A[0]))]
  P.append(c);r+=1
  if r==len(A):break
 return A[:r],P
def null(A):
 R,P=rr(A);n=len(A[0]);F=[c for c in range(n) if c not in P];B=[]
 for f in F:
  x=[0]*n;x[f]=1
  for row,p in reversed(list(zip(R,P))):
   s=0
   for c in F:s^=mul(row[c],x[c])
   x[p]=s
  B.append(x)
 return B
def dh(a,b):
 s=0
 for x,y in zip(a,b):s^=mul(x,cj(y))
 return s
def lc(a,B):
 v=[0]*len(B[0])
 for c,r in zip(a,B):
  if c:v=[x^mul(c,y) for x,y in zip(v,r)]
 return v
g1=([1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[2,1,1,0,0,0,0])
g2=([0]*7,[1,1,0,0,0,0,0],[2,0,2,3,1,1,0])
g3=([0]*7,[0]*7,[1]*7)
rows=[fs(g,s) for g in (g1,g2,g3) for s in range(7)]
C,_=rr(rows);assert len(C)==14
E=null(rows);assert len(E)==7
D=[[cj(x) for x in r] for r in E];assert len(rr(D)[0])==7
assert all(dh(c,d)==0 for c in C for d in D)
gram=[[dh(a,b) for b in D] for a in D]
assert len(rr(gram)[0])==6
h=D[0]
assert h==cert["hermitian_hull"]["generator_block_order"]==[1]*14+[0]*7
W=collections.Counter();mins=[]
for a in itertools.product(range(4),repeat=7):
 v=lc(a,D);w=sum(bool(x) for x in v);W[w]+=1
 if w==11:mins.append(tuple(v))
assert {str(k):v for k,v in sorted(W.items())}==cert["weight_distribution"]
S=sorted({tuple(i for i,x in enumerate(v) if x) for v in mins})
assert len(mins)==357 and len(S)==119
def sh(s,t):return tuple(sorted((i//7)*7+((i%7+t)%7) for i in s))
SS=set(S);seen=set();sizes=[]
for s in S:
 if s in seen:continue
 o={sh(s,t) for t in range(7)};assert o<=SS;seen|=o;sizes.append(len(o))
assert sorted(sizes)==[7]*17
pat=collections.Counter(tuple(sum(7*b<=i<7*(b+1) for i in s) for b in range(3)) for s in S)
assert {"-".join(map(str,k)):v for k,v in sorted(pat.items())}==cert["minimum_layer"]["block_weight_patterns"]
print("VERIFY_OK")
