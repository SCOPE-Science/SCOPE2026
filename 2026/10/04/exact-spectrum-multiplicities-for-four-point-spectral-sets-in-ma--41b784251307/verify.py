from itertools import product,combinations
from collections import Counter
def zero(A,d,p):
 q4=pow(p%4,-1,4); qp=pow(4,-1,p); U=((1,0),(0,1),(-1,0),(0,-1)); c=[(0,0)]*p
 for a in A:
  e=d*a%(4*p); u=e*q4%4; v=e*qp%p; x,y=c[v]; X,Y=U[u]; c[v]=(x+X,y+Y)
 return len(set(c))==1
def T(p): return [tuple(r+4*t[r] for r in range(4)) for t in product(range(p),repeat=4)]
def I(A,p): return len({a%p for a in A})==1
def II(A,p):
 e=[a for a in A if a%2==0]; o=[a for a in A if a%2]
 return len(e)==2 and len(o)==2 and (e[0]-e[1])%(4*p)==2*p and (o[0]-o[1])%(4*p)==2*p and not I(A,p)
def dm(B,N):
 m=0
 for i,j in combinations(range(4),2):
  d=(B[i]-B[j])%N; m|=1<<d; m|=1<<((-d)%N)
 return m
for p in (3,5,7):
 n=4*p; ts=T(p); masks=[dm(B,n) for B in ts]; h=Counter()
 for A in ts:
  z=sum((1<<d) for d in range(1,n) if zero(A,d,p)); c=sum(not(m&~z) for m in masks); pred=p**4 if I(A,p) else p**2 if II(A,p) else p; assert c==pred; h[c]+=1
 print(p,dict(sorted(h.items())))
print('VERIFY_OK')
