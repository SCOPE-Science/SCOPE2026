"""Independent small-field checks for commuting algebra retractions in T_{<=2}(V)."""
from itertools import product
from math import prod
from collections import Counter

def mm(A,B,d,q):
 return tuple(sum(A[i*d+t]*B[t*d+j] for t in range(d))%q for i in range(d) for j in range(d))

def kron(A,B,d,q):
 n=d*d
 return tuple((A[i*d+j]*B[k*d+l])%q for i in range(d) for k in range(d) for j in range(d) for l in range(d))

def comp_right(X,F,d,q): # X is d*d x d
 return tuple(sum(X[i*d+t]*F[t*d+j] for t in range(d))%q for i in range(d*d) for j in range(d))

def comp_left(G,X,d,q):
 n=d*d
 return tuple(sum(G[i*n+t]*X[t*d+j] for t in range(n))%q for i in range(n) for j in range(d))

def matrank(A,rows,cols,q):
 b=[list(A[i*cols:(i+1)*cols]) for i in range(rows)]
 pivot=0
 for j in range(cols):
  i=next((h for h in range(pivot,rows) if b[h][j]%q),None)
  if i is None: continue
  b[pivot],b[i]=b[i],b[pivot]
  inv=pow(b[pivot][j],-1,q)
  b[pivot]=[(x*inv)%q for x in b[pivot]]
  for h in range(rows):
   if h!=pivot and b[h][j]%q:
    factor=b[h][j]
    b[h]=[(x-factor*y)%q for x,y in zip(b[h],b[pivot])]
  pivot+=1
  if pivot==rows:break
 return pivot

def rank2(F,q):return matrank(F,2,2,q)

def decompranks(F,T,q):
 r11=rank2(mm(F,T,2,q),q)
 r10=rank2(F,q)-r11
 r01=rank2(T,q)-r11
 r00=2-r10-r01-r11
 assert min(r00,r01,r10,r11)>=0
 return (r00,r01,r10,r11)

def power(q,n):return q**n

def gl(n,q):return prod((q**n-q**j) for j in range(n))

def classsize(r,q):
 d=sum(r); H=0
 for a in range(4):
  wa=sum(r[b]*r[c] for b in range(4) for c in range(4) if (b&c)==a)
  H+=r[a]*wa
 return gl(d,q)//prod(gl(v,q) for v in r)*q**(d**3-H)

def all_idempotent_F(q):
 d=2
 I=(1,0,0,1)
 return [F for F in product(range(q),repeat=4) if mm(F,F,d,q)==F]

def constraint_dimension(F,T,q):
 d=2; W=d**3; GF=kron(F,F,d,q);GT=kron(T,T,d,q)
 zeros=(0,)*W; equations=[]
 for v in range(2*W):
  Q1=tuple(1 if j==v else 0 for j in range(W)) if v<W else zeros
  Q2=tuple(1 if j+W==v else 0 for j in range(W)) if v>=W else zeros
  c1=tuple((a+b-c)%q for a,b,c in zip(comp_right(Q1,F,d,q),comp_left(GF,Q1,d,q),Q1))
  c2=tuple((a+b-c)%q for a,b,c in zip(comp_right(Q2,T,d,q),comp_left(GT,Q2,d,q),Q2))
  c3=tuple((a+b-c-e)%q for a,b,c,e in zip(comp_right(Q1,T,d,q),comp_left(GF,Q2,d,q),comp_right(Q2,F,d,q),comp_left(GT,Q1,d,q)))
  equations.append(c1+c2+c3)
 matrix=tuple(equations[v][i] for i in range(3*W) for v in range(2*W))
 return 2*W-matrank(matrix,3*W,2*W,q)

def test_all_tangent_pairs(q):
 Fs=all_idempotent_F(q); actual=Counter(); num=0
 for F in Fs:
  for T in Fs:
   if mm(F,T,2,q)!=mm(T,F,2,q): continue
   ranks=decompranks(F,T,q)
   dimension=constraint_dimension(F,T,q)
   H=sum(ranks[a]*sum(ranks[b]*ranks[c] for b in range(4) for c in range(4) if b&c==a) for a in range(4))
   assert dimension==8-H,(q,F,T,ranks,dimension,H)
   actual[ranks]+=q**dimension
   num+=1
 expected={r:classsize(r,q) for r in product(range(3),repeat=4) if sum(r)==2}
 assert dict(actual)==expected, (q,actual,expected)
 print('ALL_TANGENT_PAIRS',q,num,'TOTAL',sum(actual.values()),'CONJUGACY_TYPES',len(actual))
 return sum(actual.values())

def explicit_pair_composition(Q1,F,Q2,T,q):
 d=2;GF=kron(F,F,d,q);GT=kron(T,T,d,q)
 left=tuple((a+b)%q for a,b in zip(comp_right(Q1,T,d,q),comp_left(GF,Q2,d,q)))
 right=tuple((a+b)%q for a,b in zip(comp_right(Q2,F,d,q),comp_left(GT,Q1,d,q)))
 return left==right

def test_full_endomorphisms_binary():
 q=2; Fs=all_idempotent_F(q); allQ=list(product(range(q),repeat=8))
 elems=[]
 for F in Fs:
  GF=kron(F,F,2,q)
  for Q in allQ:
   if tuple((a+b)%q for a,b in zip(comp_right(Q,F,2,q),comp_left(GF,Q,2,q)))==Q:
    elems.append((F,Q))
 assert len(elems)==98,len(elems)
 count=0
 for F,Q in elems:
  for T,R in elems:
   if mm(F,T,2,q)==mm(T,F,2,q) and explicit_pair_composition(Q,F,R,T,q):count+=1
 assert count==sum(classsize(r,q) for r in product(range(3),repeat=4) if sum(r)==2)
 print('ALL_BINARY_PAIRS_DIRECT',len(elems),count)

if __name__=='__main__':
 test_all_tangent_pairs(2)
 test_all_tangent_pairs(3)
 test_all_tangent_pairs(5)
 test_full_endomorphisms_binary()
 print('ALL_SIMULTANEOUS_RETRACTION_CHECKS_PASSED')
