from collections import Counter,defaultdict
from itertools import combinations
P=5
# a+bt, t^2=3
enc=lambda a,b:(a%5)+5*(b%5)
def add(x,y):return enc(x%5+y%5,x//5+y//5)
def neg(x):return enc(-x%5,-(x//5)%5)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x%5,x//5;c,d=y%5,y//5
 return enc(a*c+3*b*d,a*d+b*c)
def powr(x,n):
 r=1
 while n:
  if n&1:r=mul(r,x)
  x=mul(x,x);n//=2
 return r
def inv(x):assert x;return powr(x,23)
z=5 # t
assert powr(z,4)==4 and powr(z,8)==1
PARS=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for typ,((a,b),(c,d)) in enumerate(PARS):
 for i in [1,3,5,7]:
  for j in [1,3,5,7]:
   u=[0]*4;v=[0]*4;u[a]=v[c]=1;u[b]=powr(z,i);v[d]=powr(z,j)
   lines.append((typ,i,j,u,v))
def inter(L,M):
 a,b=L[3:5];c,d=M[3:5]
 A=[list(v) for v in zip(a,b,c,d)];n=4;pivs=[];r=0
 for col in range(4):
  k=next((j for j in range(r,n) if A[j][col]),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];v=inv(A[r][col]);A[r]=[mul(x,v) for x in A[r]]
  for j in range(n):
   if j!=r and A[j][col]:
    k=A[j][col];A[j]=[sub(x,mul(k,y)) for x,y in zip(A[j],A[r])]
  pivs.append(col);r+=1
  if r==4:return None
 assert r==3
 f=next(i for i in range(4) if i not in pivs);x=[0]*4;x[f]=1
 for j,col in enumerate(pivs):x[col]=neg(A[j][f])
 pt=[add(mul(x[0],a[i]),mul(x[1],b[i])) for i in range(4)]
 v=next(x for x in pt if x);v=inv(v)
 return tuple(mul(v,x) for x in pt)
points=defaultdict(set)
for i,j in combinations(range(48),2):
 p=inter(lines[i],lines[j])
 if p is not None:points[p].update((i,j))
assert len(points)==216 and Counter(map(len,points.values()))==Counter({2:192,4:24})
print('GF25_FERMAT_CONFIG_OK',len(points),Counter(map(len,points.values())))
