#!/usr/bin/env python3
"""Exact coefficient certificate for centered maximal norms on friendship graphs."""
import itertools, math, time

def mm(X,Y):
 n=len(X); Z=[[0]*n for _ in range(n)]
 for i in range(n):
  for k in range(n):
   if X[i][k]:
    t=X[i][k]
    for j in range(n): Z[i][j]+=t*Y[k][j]
 return Z

def charpoly(X):
 n=len(X); B=[[int(i==j) for j in range(n)] for i in range(n)]
 coeff=[1]
 for k in range(1,n+1):
  P=mm(X,B)
  tr=sum(P[i][i] for i in range(n))
  assert tr%k==0
  c=-tr//k
  coeff.append(c)
  for i in range(n):P[i][i]+=c
  B=P
 return coeff

def mul(x,y,D):return (x[0]*y[0]+D*x[1]*y[1],x[0]*y[1]+x[1]*y[0])

def nonnegative(x,D):
 a,b=x
 if b==0:return a>=0
 if a>=0 and b>=0:return True
 if a<0 and b<0:return False
 if a>=0:return a*a>=D*b*b
 return D*b*b>=a*a

def check(m):
 N=2*m+1; L=3*N; delta=2*m+13;D=delta*delta-144
 # t=2*L^2*lambda=N^2*(delta+sqrtD)
 T=(N*N*delta,N*N);powers=[(1,0)]
 for i in range(N):powers.append(mul(powers[-1],T,D))
 pair_types=list(itertools.product(range(3),repeat=2))
 examined=0
 for rows in itertools.combinations_with_replacement(range(9),m):
  for h in (0,1):
   A=[]
   hr=[0]*N
   if h==0:hr[0]=L
   else:hr=[3]*N
   A.append(hr)
   for i,tix in enumerate(rows):
    for j,radius in enumerate(pair_types[tix]):
     row=[0]*N
     if radius==0:row[2*i+j+1]=L
     elif radius==1:
      for k in (0,2*i+1,2*i+2):row[k]=N
     elif radius==2:row=[3]*N
     A.append(row)
   C=[[2*sum(A[i][k]*A[j][k] for k in range(N)) for j in range(N)] for i in range(N)]
   cf=charpoly(C)
   for k in range(N+1):
    x=(0,0)
    for j in range(N-k+1):
     p=powers[N-j-k];scale=cf[j]*math.comb(N-j,k)
     x=(x[0]+scale*p[0],x[1]+scale*p[1])
    if not nonnegative(x,D):
     print('FAIL',m,rows,h,k,x);return False
   examined+=1
 print('PASS m=',m,'cases=',examined,'dimension',N)
 return True

if __name__=='__main__':
 t=time.time()
 for m in (1,2,3):assert check(m)
 print('seconds',time.time()-t)
