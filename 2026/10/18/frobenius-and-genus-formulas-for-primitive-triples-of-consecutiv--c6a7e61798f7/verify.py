from math import comb,gcd
from functools import reduce
import heapq

def data(n):
 U,V,W=n*(n+1),(n+1)*(n+3),(n+3)*(n+4)
 c=(3 if n%3!=1 else 1)*(2 if n%2 else 1)
 assert gcd(gcd(U,V),W)==c,(n,U,V,W,c,gcd(gcd(U,V),W))
 A,B,C=U//c,V//c,W//c
 assert gcd(gcd(A,B),C)==1
 if n==2: d,u,v,z=5,1,2,A; assert B==d*u and C==d*v
 elif n%6==5:
  d=gcd(B,C);u,v,z=B//d,C//d,A
 else:
  d=gcd(A,B);u,v,z=A//d,B//d,C
 assert gcd(u,v)==1 and gcd(d,z)==1,(n,d,u,v,z)
 found=next(((i,(z-u*i)//v) for i in range(z//u+1) if (z-u*i)%v==0 and z-u*i>=0),None)
 assert found is not None,(n,d,u,v,z)
 return (A,B,C,d,u,v,z,found)

def independent_f(a):
 start=min(a);dist=[10**99]*start;dist[0]=0;pq=[(0,0)]
 while pq:
  val,r=heapq.heappop(pq)
  if val!=dist[r]: continue
  for x in a:
   k=(r+x)%start; nv=val+x
   if nv<dist[k]:dist[k]=nv;heapq.heappush(pq,(nv,k))
 return max(dist)-start, (sum(dist)//start - (start-1)//2) # genus formula careful integer /2

for n in range(2,301):
 a,b,c,d,u,v,z,rep=data(n)
 F=d*(u*v-u-v)+(d-1)*z
 if n<=160:
  f,g=independent_f((a,b,c))
  assert F==f,(n,a,b,c,F,f)
  assert 2*g==F+1,(n,F,g)
print('VERIFY_OK: 299 gcd/gluing decompositions, 159 independent Apéry computations, exact Frobenius and genus')
for n in range(2,14):
 a,b,c,d,u,v,z,rep=data(n)
 print(n,(a,b,c),'glue', (d,u,v,z),'F',d*(u*v-u-v)+(d-1)*z)
