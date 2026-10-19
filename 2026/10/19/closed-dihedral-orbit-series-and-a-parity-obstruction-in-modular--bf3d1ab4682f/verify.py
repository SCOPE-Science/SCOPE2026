#!/usr/bin/env python3
"""Independent periodic word enumeration against rational generating-function identities."""
from itertools import product
from collections import defaultdict

def conv(a,b,max_n):
 out=defaultdict(int)
 for i,x in a.items():
  for j,y in b.items():
   if i+j<=max_n:out[i+j]+=x*y
 return dict(out)
def seriesdiv(A,B,N):
 assert B.get(0,0)==1
 c=[0]*(N+1)
 for i in range(N+1):
  c[i]=A.get(i,0)-sum(B.get(j,0)*c[i-j] for j in range(1,i+1))
 return c

def expected(r,N):
 R=r//__import__('math').gcd(2,r)
 S={0:1,r:-1};Q={0:1,1:-1,r:-1}; D={0:1,R:-1}
 Lnum={1:1}
 Bnum=({(r+1)//2:1} if r%2 else {})
 Bden=S if r%2 else {0:1}
 Cnum=defaultdict(int)
 for j,v in Bden.items():Cnum[j]+=v
 for j,v in Bnum.items():Cnum[j]+=v
 Cnum=dict(Cnum)
 # O=(1/(1-z)) + (1+B)*(1-z^r)/((1-z^R)*Q)
 Oden=conv(conv(D,Q,N),Bden,N)
 Onum=conv(Cnum,S,N)
 O=seriesdiv(Onum,Oden,N)
 O=[a+1 for a in O]
 # V = z/(1-z) + (1+B)^2*(1-z^r)/Q -1
 Vden=conv(conv(Bden,Bden,N),Q,N)
 Vnum=conv(conv(Cnum,Cnum,N),S,N)
 V=seriesdiv(Vnum,Vden,N)
 V=[a-(1 if i==0 else 0)+(1 if i>=1 else 0) for i,a in enumerate(V)]
 # E=z/(1-z)+z(1-z^r)/[(1-z^R)^2 Q]
 Eden=conv(conv(D,D,N),Q,N)
 Enum=conv({1:1},S,N)
 E=seriesdiv(Enum,Eden,N)
 E=[a+(1 if i>=1 else 0) for i,a in enumerate(E)]
 return O,V,E

def good(bits,r):
 n=len(bits)
 idx=[i for i,x in enumerate(bits) if x]
 if not idx:return True
 for a,b in zip(idx,idx[1:]+[idx[0]+n]):
  if (b-a-1)%r:return False
 return True

def independent_count(r,n,k):
 orbit=[];seen=set()
 for i in range(n):
  if i in seen:continue
  j=(k-i)%n
  orbit.append([i] if i==j else [i,j])
  seen.add(i);seen.add(j)
 count=0
 for labels in product((0,1),repeat=len(orbit)):
  bits=[0]*n
  for a,orb in zip(labels,orbit):
   for j in orb:bits[j]=a
  if good(bits,r):count+=1
 return count

def matrix_count(r,n):
 M=[[0]*r for _ in range(r)]
 M[0][0]+=1
 for j in range(r):M[j][(j+1)%r]+=1
 def matmul(A,B):
  return [[sum(A[i][k]*B[k][j] for k in range(r)) for j in range(r)] for i in range(r)]
 A=[[int(i==j) for j in range(r)] for i in range(r)]
 for _ in range(n):A=matmul(A,M)
 return sum(A[i][i] for i in range(r))+1-r*(n%r==0)

if __name__=='__main__':
 ct=0
 for r in range(2,9):
  O,V,E=expected(r,11)
  for m in range(12):
   for n,k,a in [(2*m+1,0,O[m])]+([(2*m,0,V[m]),(2*m,1,E[m])] if m else []):
    b=independent_count(r,n,k)
    assert a==b,(r,n,k,a,b)
    ct+=1
  for n in range(1,13):
   brute=sum(good(w,r) for w in product((0,1),repeat=n))
   alg=matrix_count(r,n)
   assert brute==alg,(r,n,brute,alg)
   ct+=1
 print('VERIFY_OK: %d exact independent periodic/reflection counts for moduli 2..8'%ct)
