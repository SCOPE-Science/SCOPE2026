import itertools, random
import sympy as s

def lap(N, mask):
 L=s.zeros(N); edges=list(itertools.combinations(range(N),2))
 for k,(u,v) in enumerate(edges):
  if (mask>>k)&1:
   L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
 return L

def assess(L):
 N=L.rows;t=s.Rational(1,N-2);C=(s.eye(N)+t*L).inv()
 target=s.Rational(1,2); univ=[i for i in range(N) if L[i,i]==N-1]
 assert all(C[i,i]>=target for i in range(N))
 assert [i for i in range(N) if C[i,i]==target]==univ
 for i in univ:
  for t1 in (s.Rational(1,10),s.Rational(7,4)):
   assert (s.eye(N)+t1*L).inv()[i,i]==(1+t1)/(1+N*t1)
 return True
count=0
for N in range(3,6):
 for mask in range(1<<(N*(N-1)//2)):
  L=lap(N,mask)
  # Connectivity via nullspace; avoids external graph packages.
  if L.rank()!=N-1: continue
  assess(L);count+=1
for N in (6,7,8):
 m=N*(N-1)//2
 random.seed(1000+N)
 for j in range(20):
  mask=(1<<(N-1))-1 # all edges involving vertex 0
  for k in range(N-1,m):
   if random.randrange(2):mask|=1<<k
  assess(lap(N,mask));count+=1
print('VERIFY_OK exact_connected_graphs=',count,'universal_diagonals_checked=True','strict_nouniversal_equality=True')
