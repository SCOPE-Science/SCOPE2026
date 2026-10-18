"""Independent exact-integer convolution-matrix census for 24 Hurwitz units.

Run: python3 check_hurwitz_census.py (standard library only).
The checked 253 identity-normalized supports exhaust all 2,024 supports
up to left translation; each normalized support has counting weight eight.
"""
from itertools import combinations,product
from collections import Counter
from time import perf_counter

G=set()
for j in range(4):
 for s in (-2,2):
  a=[0]*4;a[j]=s;G.add(tuple(a))
G.update(product((-1,1), repeat=4))
G=tuple(sorted(G)); assert len(G)==24
lookup={g:i for i,g in enumerate(G)}; identity=(2,0,0,0)

def mul(a,b):
 w,x,y,z=a;v,p,q,r=b
 N=(w*v-x*p-y*q-z*r,w*p+x*v+y*r-z*q,w*q-x*r+y*v+z*p,w*r+x*q-y*p+z*v)
 assert all(n%2==0 for n in N)
 return tuple(n//2 for n in N)

def inv(a):return (a[0],-a[1],-a[2],-a[3])
def order(g):
 z=identity
 for j in range(1,25):
  z=mul(z,g)
  if z==identity:return j
 raise AssertionError
Q8={g for g in G if any(abs(c)==2 for c in g)}
t=(-1,1,1,1)
t2=mul(t,t)
assert order(t)==3
C0=Q8; C1={mul(q,t) for q in Q8}; C2={mul(q,t2) for q in Q8}
assert (len(C0),len(C1),len(C2))==(8,8,8)
assert len(C0|C1|C2)==24
C1counts=Counter(order(x) for x in C1);C2counts=Counter(order(y) for y in C2)
assert C1counts==C2counts=={3:4,6:4}
# Exhaustive exact integer ranks, one representative per left translation class with identity in support.

def rank_int(A):
 a=[row[:] for row in A]
 nr=len(a);nc=len(a[0]);k=0;prev=1
 for col in range(nc):
  pivot=next((i for i in range(k,nr) if a[i][col]),None)
  if pivot is None:continue
  if pivot!=k:a[k],a[pivot]=a[pivot],a[k]
  piv=a[k][col]
  for i in range(k+1,nr):
   factor=a[i][col]
   for j in range(col+1,nc):
    num=piv*a[i][j]-factor*a[k][j]
    assert num%prev==0,(i,j,num,prev)
    a[i][j]=num//prev
   a[i][col]=0
  k+=1;prev=piv
  if k==nr:break
 return k

L={}
for g in G:
 A=[[0]*24 for _ in range(24)]
 for j,h in enumerate(G): A[lookup[mul(g,h)]][j]=1
 L[g]=A

def nullity(g,h):
 return 24-rank_int([[int(i==j)+L[g][i][j]+L[h][i][j] for j in range(24)] for i in range(24)])

C=Counter();edge=Counter();bad=[]
nonid=[g for g in G if g!=identity]
t0=perf_counter()
for g,h in combinations(nonid,2):
 n=nullity(g,h)
 transverse=(g in C1 and h in C2) or (g in C2 and h in C1)
 if transverse:
  es=tuple(sorted((order(g),order(h),order(mul(inv(g),h)))))
  expect={(3,3,3):16,(3,3,6):2,(3,6,6):8,(6,6,6):6}[es]
  edge[es]+=1
 else:expect=0
 if n!=expect:bad.append((g,h,n,expect))
 C[n]+=1
assert not bad,bad
assert C=={0:189,2:36,6:12,8:12,16:4},C
assert edge=={(3,3,3):4,(3,3,6):36,(3,6,6):12,(6,6,6):12},edge
print('exact ranks: 253 distinct normalized triples; elapsed',perf_counter()-t0)
print('nullity distribution over all 2024 supports:', {k:8*v for k,v in sorted(C.items())})

# Small orbit calculation used in the human-readable counting proof.
for rep, required in [
 (t,{(3,3,3):1,(3,3,6):6,(3,6,6):1}),
 (tuple(-z for z in t),{(3,3,6):3,(3,6,6):2,(6,6,6):3})
]:
 distribution=Counter(tuple(sorted((order(rep),order(y),order(mul(inv(rep),y))))) for y in C2)
 assert distribution==required, (rep,distribution)
print("Representative quaternion order-pattern tables: verified")
