from collections import Counter
from math import comb

def cyclic(n):return [[(i+j)%n for j in range(n)] for i in range(n)]
def klein():return [[i^j for j in range(4)] for i in range(4)]
def s3():
 import itertools
 ps=list(itertools.permutations(range(3))); pos={p:i for i,p in enumerate(ps)}
 return [[pos[tuple(p[q[k]] for k in range(3))] for q in ps] for p in ps]
def dihedral4():
 # (r,s) with s=0/1, elements encoded 2*r+s
 return [[2*((i//2 + ((-1)**(i%2))*(j//2))%4)+((i%2)^(j%2)) for j in range(8)] for i in range(8)]
def order(M,g):
 N=len(M); e=next(i for i in range(N) if all(M[i][j]==j and M[j][i]==j for j in range(N)))
 x=e
 for k in range(1,N+1):
  x=M[x][g]
  if x==e:return k
 raise AssertionError

def action(M,copies):
 N=len(M); n=N*copies
 return [[a*N + M[g][i] for a in range(copies) for i in range(N)] for g in range(N)]

def brute(M,copies):
 N=len(M); n=N*copies; ps=action(M,copies)
 elements={tuple([-1]*n)}
 for p in ps:
  for mask in range(1,1<<n):
   elements.add(tuple(p[i] if mask>>i&1 else -1 for i in range(n)))
 assert len(elements)==N*((1<<n)-1)+1
 h=Counter()
 for s in range(1<<n):
  e=tuple(i if s>>i&1 else -1 for i in range(n))
  a=s.bit_count()
  for f in elements:
   ef=tuple(e[f[i]] if f[i]>=0 else -1 for i in range(n))
   fe=tuple(f[e[i]] if e[i]>=0 else -1 for i in range(n))
   if ef==fe:h[a,sum(v>=0 for v in f)]+=1
 return h

def mul(A,B):
 C=Counter()
 for (a,b),c in A.items():
  for (x,y),d in B.items():C[a+x,b+y]+=c*d
 return C

def power(A,k):
 o=Counter({(0,0):1})
 for _ in range(k):o=mul(o,A)
 return o

def cyclepoly(d):
 o=Counter()
 for s in range(1<<d):
  a=s.bit_count();same=sum(bool(s>>i&1)==bool(s>>((i+1)%d)&1) for i in range(d))
  for b in range(same+1):o[a,b]+=comb(same,b)
 return o

def polynomial(M,copies):
 N=len(M); n=N*copies
 out=Counter()
 for g in range(N):
  d=order(M,g)
  out.update(power(cyclepoly(d),n//d))
 for a in range(n+1):out[a,0]-=(N-1)*comb(n,a)
 return +out

for name,M,m in [('C1',cyclic(1),1),('C2',cyclic(2),1),('C2',cyclic(2),2),('C2',cyclic(2),3),('C3',cyclic(3),1),('C3',cyclic(3),2),('C4',cyclic(4),1),('V4',klein(),1),('S3',s3(),1),('D8',dihedral4(),1)]:
 a=brute(M,m);b=polynomial(M,m)
 assert a==b,(name,m,a-b,b-a)
 N=len(M);n=N*m
 spec=Counter(order(M,g) for g in range(N))
 count=sum(a.values())
 closed=sum(ct*(3**d+1)**(n//d) for d,ct in spec.items())-(N-1)*2**n
 assert count==closed
 print(name,m,n,spec,'pairs',count,'monoid',N*(2**n-1)+1)
from fractions import Fraction

def recover(M):
 N = len(M)
 divisors = [d for d in range(1,N+1) if N%d==0]
 bases = [(3**d+1)**(N//d) for d in divisors]
 counts = [sum((3**order(M,g)+1)**(m*N//order(M,g)) for g in range(N)) for m in range(1,len(divisors)+1)]
 rows = [[Fraction(b**m) for b in bases]+[Fraction(counts[m-1])] for m in range(1,len(divisors)+1)]
 r=len(divisors)
 for col in range(r):
  pivot=next(k for k in range(col,r) if rows[k][col]!=0)
  rows[col],rows[pivot]=rows[pivot],rows[col]
  t=rows[col][col]
  rows[col]=[x/t for x in rows[col]]
  for i in range(r):
   if i==col:continue
   t=rows[i][col]
   rows[i]=[rows[i][j]-t*rows[col][j] for j in range(r+1)]
 recovered=[rows[i][-1] for i in range(r)]
 expected=[sum(order(M,g)==d for g in range(N)) for d in divisors]
 assert recovered==expected,(N,recovered,expected)

for M in [cyclic(4),klein(),s3(),dihedral4()]:recover(M)
print('VERIFY_OK')
